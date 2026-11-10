import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import {
  assertSandboxRestrictedKey, checkoutParams, handleSignedIn, handleWebhook
} from "../supabase/functions/_shared/billing_http.js";

const ORIGIN = "https://botsdothat.example";
const USER = "11111111-1111-1111-1111-111111111111";
const PRICES = {three: "price_three_test", five: "price_five_test"};

function request(url, body, headers) {
  return new Request(url, {
    method: "POST",
    headers: Object.assign({"content-type": "application/json", origin: ORIGIN, authorization: "Bearer user-jwt"}, headers || {}),
    body: typeof body === "string" ? body : JSON.stringify(body)
  });
}

function deps(extra) {
  const calls = [];
  const base = {
    billingOpen: true,
    siteOrigin: ORIGIN,
    prices: PRICES,
    calls,
    getUser: async () => ({id: USER, user_metadata: {plan: "five"}, app_metadata: {role: "admin"}}),
    customerFor: async (id) => {
      calls.push(["customer", id]);
      return "cus_owner";
    },
    stripe: {
      checkout: {sessions: {create: async (params, opts) => {
        calls.push(["checkout", params, opts]);
        return {url: "https://checkout.stripe.com/c/pay/cs_test_session"};
      }}},
      billingPortal: {sessions: {create: async (params) => {
        calls.push(["portal", params]);
        return {url: "https://billing.stripe.com/p/session/test"};
      }}}
    }
  };
  return Object.assign(base, extra || {});
}

test("checkout uses the signed-in user and the allowlisted price", async () => {
  const env = deps();
  const res = await handleSignedIn(request("https://fn.example/billing", {action: "checkout", plan_code: "three"}), env);
  assert.equal(res.status, 200);
  const created = env.calls.find((item) => item[0] === "checkout");
  assert.equal(created[1].line_items[0].price, "price_three_test");
  assert.equal(created[1].client_reference_id, USER);
  assert.equal(created[1].metadata.user_id, USER);
  assert.match(created[1].integration_identifier, /^botsdothat_setups_[a-z]{8}$/);
  assert.equal(Object.hasOwn(created[1], "payment_method_types"), false);
  assert.equal(Object.hasOwn(created[1], "automatic_tax"), false);
  assert.match(created[2].idempotencyKey, /^setups-/);
  assert.equal(created[1].success_url, ORIGIN + "/bot-instructions/?billing=return");
  const payload = await res.json();
  assert.equal(payload.url, "https://checkout.stripe.com/c/pay/cs_test_session");
  assert.equal(res.headers.get("access-control-allow-origin"), ORIGIN);
  assert.equal(res.headers.get("content-security-policy"), "default-src 'none'");
});

test("a client amount, url, or other origin cannot open checkout", async () => {
  const env = deps();
  const rejected = await handleSignedIn(request("https://fn.example/billing", {
    action: "checkout", plan_code: "three", amount: 100, success_url: "https://evil.example/phish"
  }), env);
  assert.equal(rejected.status, 400);
  assert.equal(env.calls.some((item) => item[0] === "checkout"), false);
  const closed = await handleSignedIn(request("https://fn.example/billing", {plan_code: "five"}), deps({billingOpen: false}));
  assert.equal(closed.status, 403);
  const foreign = await handleSignedIn(request("https://fn.example/billing", {plan_code: "three"}, {origin: "https://evil.example"}), env);
  assert.equal(foreign.status, 200);
  assert.equal(foreign.headers.get("access-control-allow-origin"), null);
  const expired = await handleSignedIn(request("https://fn.example/billing", {plan_code: "three"}, {authorization: "Bearer expired"}), deps({
    getUser: async () => null
  }));
  assert.equal(expired.status, 401);
  const secret = await handleSignedIn(request("https://fn.example/billing", {plan_code: "three"}, {authorization: "Bearer sb_secret_nope"}), env);
  assert.equal(secret.status, 401);
});

test("portal uses only the signed-in customer's id", async () => {
  const env = deps();
  const res = await handleSignedIn(request("https://fn.example/billing", {action: "portal", customer: "cus_other", return_url: "https://evil.example"}), env);
  assert.equal(res.status, 400);
  assert.equal(env.calls.some((item) => item[0] === "portal"), false);
  const ok = await handleSignedIn(request("https://fn.example/billing", {action: "portal"}), env);
  assert.equal(ok.status, 200);
  const portal = env.calls.find((item) => item[0] === "portal");
  assert.deepEqual(portal[1], {customer: "cus_owner", return_url: ORIGIN + "/bot-instructions/"});
  const stranger = await handleSignedIn(request("https://fn.example/billing", {action: "portal"}), deps({
    customerFor: async () => "user_not_a_customer"
  }));
  assert.equal(stranger.status, 400);
});

test("webhooks reject a bad signature and keep duplicate and stale results", async () => {
  const secret = "whsec_test";
  const event = {id: "evt_1", created: 100, type: "checkout.session.completed", data: {object: {payment_status: "paid"}}};
  const raw = JSON.stringify(event);
  const stamp = 100;
  const mac = createHmac("sha256", secret).update(stamp + "." + raw).digest("hex");
  const header = "t=" + stamp + ",v1=" + mac;
  const seen = [];
  const res = await handleWebhook(new Request("https://fn.example/stripe-webhook", {
    method: "POST",
    headers: {"stripe-signature": header},
    body: raw
  }), {
    siteOrigin: ORIGIN,
    prices: PRICES,
    webhookSecret: secret,
    now: () => 100,
    applyEvent: async (parsed) => {
      seen.push(parsed.id);
      return {action: "duplicate"};
    }
  });
  assert.equal(res.status, 200);
  assert.deepEqual(seen, ["evt_1"]);
  assert.equal((await res.json()).action, "duplicate");
  const bad = await handleWebhook(new Request("https://fn.example/stripe-webhook", {
    method: "POST",
    headers: {"stripe-signature": "t=100,v1=deadbeef"},
    body: raw
  }), {siteOrigin: ORIGIN, prices: PRICES, webhookSecret: secret, now: () => 100, applyEvent: async () => ({action: "applied"})});
  assert.equal(bad.status, 400);
  const stale = await handleWebhook(new Request("https://fn.example/stripe-webhook", {
    method: "POST",
    headers: {"stripe-signature": header},
    body: raw
  }), {siteOrigin: ORIGIN, prices: PRICES, webhookSecret: secret, now: () => 100, applyEvent: async () => ({action: "stale"})});
  assert.equal((await stale.json()).action, "stale");
  const grant = await handleWebhook(new Request("https://fn.example/stripe-webhook", {
    method: "POST",
    headers: {"stripe-signature": header},
    body: raw
  }), {siteOrigin: ORIGIN, prices: PRICES, webhookSecret: secret, now: () => 100, applyEvent: async () => ({action: "applied", delete_setups: ["x"]})});
  assert.equal(grant.status, 500);
});

test("only a sandbox restricted key is accepted", () => {
  assert.throws(() => assertSandboxRestrictedKey("sk_test_example"));
  assert.throws(() => assertSandboxRestrictedKey("rk_live_example"));
  assert.throws(() => assertSandboxRestrictedKey(""));
  assert.doesNotThrow(() => assertSandboxRestrictedKey("rk_test_example"));
  const params = checkoutParams(USER, {plan_code: "five"}, PRICES, ORIGIN);
  assert.equal(params.params.line_items[0].price, "price_five_test");
});

test("function source does not take a service-role key or a live charge", () => {
  const billing = readFileSync(new URL("../supabase/functions/billing/index.ts", import.meta.url), "utf8");
  const webhook = readFileSync(new URL("../supabase/functions/stripe-webhook/index.ts", import.meta.url), "utf8");
  const config = readFileSync(new URL("../supabase/config.toml", import.meta.url), "utf8");
  assert.match(billing, /new Stripe\(/);
  assert.match(webhook, /constructEventAsync/);
  assert.doesNotMatch(billing + webhook, /SUPABASE_SERVICE_ROLE_KEY|api_key\s*=|payment_method_types|automatic_tax/);
  assert.match(config, /\[functions\.stripe-webhook\][\s\S]*verify_jwt = false/);
  assert.match(config, /\[functions\.billing\][\s\S]*verify_jwt = true/);
  assert.doesNotMatch(config, /^project_id\s*=/m);
});
