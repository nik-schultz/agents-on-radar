// Signed Stripe webhooks. verify_jwt is false because Stripe has no user JWT.
// Entitlement writes use BILLING_DB_URL as role billing_writer. The service-role
// key is not read. A browser return never reaches this function.
import Stripe from "npm:stripe@23.0.0";
import postgres from "npm:postgres@3.4.5";
import { assertSandboxRestrictedKey, handleWebhook } from "../_shared/billing_http.js";

const API_VERSION = "2026-09-30.endive";

let db: ReturnType<typeof postgres> | null = null;

function database() {
  if (db) return db;
  const connection = Deno.env.get("BILLING_DB_URL") || "";
  if (!connection) throw new Error("missing BILLING_DB_URL");
  db = postgres(connection, { max: 1, prepare: false, ssl: "require" });
  return db;
}

Deno.serve(async (req) => {
  const siteOrigin = Deno.env.get("SITE_ORIGIN") || "";
  let stripe: Stripe;
  try {
    const key = Deno.env.get("STRIPE_RESTRICTED_KEY") || "";
    assertSandboxRestrictedKey(key);
    if (!Deno.env.get("STRIPE_WEBHOOK_SECRET") || !Deno.env.get("BILLING_DB_URL")) {
      throw new Error("missing webhook configuration");
    }
    stripe = new Stripe(key, { apiVersion: API_VERSION });
  } catch (_err) {
    return new Response(JSON.stringify({ error: "Webhook is not configured." }), {
      status: 503,
      headers: { "Content-Type": "application/json", "Content-Security-Policy": "default-src 'none'" },
    });
  }
  const prices = {
    three: Deno.env.get("STRIPE_PRICE_THREE") || "",
    five: Deno.env.get("STRIPE_PRICE_FIVE") || "",
  };
  return handleWebhook(req, {
    siteOrigin,
    prices,
    webhookSecret: Deno.env.get("STRIPE_WEBHOOK_SECRET") || "",
    constructEvent: (raw: Uint8Array, header: string | null, now: number) =>
      stripe.webhooks.constructEventAsync(raw, header || "", Deno.env.get("STRIPE_WEBHOOK_SECRET") || "", 300, undefined, now),
    applyEvent: async (event: unknown, allowlist: { three: string; five: string }) => {
      const sql = database();
      const rows = await sql`
        select public.apply_billing_event(${sql.json(event)}, ${sql.json(allowlist)}) as result
      `;
      return rows[0].result;
    },
  });
});
