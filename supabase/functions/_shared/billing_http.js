"use strict";
/* Checkout, portal, and webhook decisions for the Edge Functions.
   No Stripe key, webhook secret, or database URL belongs in this file.
   A browser return never grants a plan. */

const PLANS = {three: 3, five: 5};
const FORBIDDEN_BODY = ["amount", "setup_limit", "price", "price_id", "customer", "success_url", "cancel_url", "return_url", "payment_method_types", "automatic_tax", "user_id", "session_id"];

function corsHeaders(origin, allowed) {
  const headers = {
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "authorization, apikey, content-type, stripe-signature",
    "Access-Control-Max-Age": "600",
    "Content-Security-Policy": "default-src 'none'",
    "X-Content-Type-Options": "nosniff",
    "Vary": "Origin"
  };
  if (origin && allowed && origin === allowed) headers["Access-Control-Allow-Origin"] = origin;
  return headers;
}

function reply(status, body, origin, allowed) {
  return new Response(JSON.stringify(body), {
    status: status,
    headers: Object.assign({"Content-Type": "application/json"}, corsHeaders(origin, allowed))
  });
}

function suffix() {
  const letters = "abcdefghijklmnopqrstuvwxyz";
  const bytes = crypto.getRandomValues(new Uint8Array(8));
  let out = "";
  for (let i = 0; i < bytes.length; i++) out += letters[bytes[i] % 26];
  return out;
}

function hourStamp(date) {
  const now = date || new Date();
  const p = function (n) { return String(n).padStart(2, "0"); };
  return now.getUTCFullYear() + p(now.getUTCMonth() + 1) + p(now.getUTCDate()) + p(now.getUTCHours());
}

function assertHttpsOrigin(origin) {
  if (!origin || !/^https:\/\/[A-Za-z0-9.-]+(?::\d+)?$/.test(origin)) throw new Error("site origin not configured");
}

function checkoutParams(userId, body, prices, origin, now) {
  if (!userId) throw new Error("missing user");
  if (!body || typeof body !== "object" || Array.isArray(body)) throw new Error("bad body");
  FORBIDDEN_BODY.forEach(function (key) {
    if (Object.prototype.hasOwnProperty.call(body, key)) throw new Error("client cannot set " + key);
  });
  if (body.action && body.action !== "checkout") throw new Error("unknown action");
  if (!PLANS[body.plan_code]) throw new Error("unknown plan");
  const price = prices && prices[body.plan_code];
  if (!price || String(price).indexOf("price_") !== 0) throw new Error("price not configured");
  assertHttpsOrigin(origin);
  const params = {
    mode: "subscription",
    client_reference_id: userId,
    line_items: [{price: price, quantity: 1}],
    success_url: origin + "/bot-instructions/?billing=return",
    cancel_url: origin + "/bot-instructions/?billing=cancel",
    metadata: {user_id: userId, plan_code: body.plan_code, price_id: price},
    subscription_data: {metadata: {user_id: userId, plan_code: body.plan_code}},
    integration_identifier: "botsdothat_setups_" + suffix()
  };
  if (Object.prototype.hasOwnProperty.call(params, "payment_method_types") || Object.prototype.hasOwnProperty.call(params, "automatic_tax")) {
    throw new Error("forbidden field");
  }
  return {params: params, idempotencyKey: "setups-" + userId + "-" + body.plan_code + "-" + hourStamp(now)};
}

function portalParams(customerId, origin) {
  if (!customerId || String(customerId).indexOf("cus_") !== 0) throw new Error("no customer");
  assertHttpsOrigin(origin);
  return {customer: customerId, return_url: origin + "/bot-instructions/"};
}

function hostedUrl(url, host) {
  let parsed;
  try { parsed = new URL(url); } catch (err) { throw new Error("unexpected redirect host"); }
  if (parsed.protocol !== "https:" || parsed.hostname !== host) throw new Error("unexpected redirect host");
  return parsed.toString();
}

function assertSandboxRestrictedKey(key) {
  const value = String(key || "");
  if (value.indexOf("rk_test_") !== 0) throw new Error("sandbox restricted key required");
  if (value.indexOf("sk_") === 0 || value.indexOf("rk_live_") === 0) throw new Error("live or secret key refused");
}

function verifySignature(payload, header, secret, now, tolerance) {
  tolerance = tolerance || 300;
  if (typeof payload === "string") payload = new TextEncoder().encode(payload);
  const parts = {};
  String(header || "").split(",").forEach(function (item) {
    const eq = item.indexOf("=");
    if (eq < 0) return;
    const k = item.slice(0, eq).trim();
    const v = item.slice(eq + 1).trim();
    parts[k] = parts[k] || [];
    parts[k].push(v);
  });
  if (!parts.t || !parts.v1) throw new Error("missing signature");
  const stamp = parseInt(parts.t[0], 10);
  if (!Number.isFinite(stamp) || Math.abs(Number(now) - stamp) > tolerance) throw new Error("stale signature");
  return crypto.subtle.importKey("raw", new TextEncoder().encode(secret), {name: "HMAC", hash: "SHA-256"}, false, ["sign"]).then(function (key) {
    const data = new Uint8Array(stamp.toString().length + 1 + payload.length);
    const prefix = new TextEncoder().encode(stamp + ".");
    data.set(prefix, 0);
    data.set(payload, prefix.length);
    return crypto.subtle.sign("HMAC", key, data);
  }).then(function (sig) {
    const mac = Array.from(new Uint8Array(sig)).map(function (b) { return b.toString(16).padStart(2, "0"); }).join("");
    const ok = parts.v1.some(function (candidate) {
      if (candidate.length !== mac.length) return false;
      let diff = 0;
      for (let i = 0; i < mac.length; i++) diff |= mac.charCodeAt(i) ^ candidate.charCodeAt(i);
      return diff === 0;
    });
    if (!ok) throw new Error("signature mismatch");
    return JSON.parse(new TextDecoder().decode(payload));
  });
}

function bearer(req) {
  const header = req.headers.get("authorization") || "";
  const match = header.match(/^Bearer\s+(\S+)$/i);
  return match ? match[1] : "";
}

async function userId(req, deps) {
  const token = bearer(req);
  if (!token || token.indexOf("sb_secret_") === 0 || token.indexOf("service_role") !== -1) {
    const error = new Error("sign-in required");
    error.status = 401;
    throw error;
  }
  const user = await deps.getUser(token);
  if (!user || !user.id) {
    const error = new Error("sign-in expired");
    error.status = 401;
    throw error;
  }
  if (user.user_metadata || user.app_metadata) {
    delete user.user_metadata;
    delete user.app_metadata;
  }
  return user.id;
}

async function handleSignedIn(req, deps) {
  const origin = req.headers.get("origin") || "";
  const allowed = deps.siteOrigin || "";
  if (req.method === "OPTIONS") return new Response(null, {status: 204, headers: corsHeaders(origin, allowed)});
  if (req.method !== "POST") return reply(405, {error: "POST only"}, origin, allowed);
  if (!deps.billingOpen) return reply(403, {error: "Checkout is closed."}, origin, allowed);
  let id;
  try { id = await userId(req, deps); }
  catch (err) { return reply(err.status || 401, {error: err.message}, origin, allowed); }
  let body;
  try { body = await req.json(); }
  catch (err) { return reply(400, {error: "bad body"}, origin, allowed); }
  try {
    if (body && body.action === "portal") {
      if (body.customer || body.return_url || body.plan_code) return reply(400, {error: "client cannot set customer"}, origin, allowed);
      const customer = await deps.customerFor(id);
      const params = portalParams(customer, deps.siteOrigin);
      const session = await deps.stripe.billingPortal.sessions.create(params);
      return reply(200, {url: hostedUrl(session && session.url, "billing.stripe.com")}, origin, allowed);
    }
    const built = checkoutParams(id, body, deps.prices, deps.siteOrigin);
    const session = await deps.stripe.checkout.sessions.create(built.params, {idempotencyKey: built.idempotencyKey});
    return reply(200, {url: hostedUrl(session && session.url, "checkout.stripe.com")}, origin, allowed);
  } catch (err) {
    return reply(400, {error: err.message || "rejected"}, origin, allowed);
  }
}

async function handleWebhook(req, deps) {
  const origin = req.headers.get("origin") || "";
  const allowed = deps.siteOrigin || "";
  if (req.method !== "POST") return reply(405, {error: "POST only"}, origin, allowed);
  const raw = new Uint8Array(await req.arrayBuffer());
  const header = req.headers.get("stripe-signature");
  const now = deps.now ? deps.now() : Math.floor(Date.now() / 1000);
  try {
    const event = deps.constructEvent
      ? await deps.constructEvent(raw, header, now)
      : await verifySignature(raw, header, deps.webhookSecret, now);
    const result = await deps.applyEvent(event, deps.prices);
    if (!result || result.delete_setups) return reply(500, {error: "entitlement write refused"}, origin, allowed);
    return reply(200, {received: true, action: result.action}, origin, allowed);
  } catch (err) {
    return reply(400, {error: "webhook rejected"}, origin, allowed);
  }
}

export {
  PLANS, checkoutParams, portalParams, hostedUrl, assertSandboxRestrictedKey,
  handleSignedIn, handleWebhook, verifySignature, corsHeaders
};
