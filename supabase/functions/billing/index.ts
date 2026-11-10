// Checkout and Customer Portal. Checkout stays closed unless BILLING_OPEN is the
// string "true". This file never reads a service-role key and never grants a plan.
import Stripe from "npm:stripe@23.0.0";
import { createClient } from "npm:@supabase/supabase-js@2.49.1";
import { assertSandboxRestrictedKey, handleSignedIn } from "../_shared/billing_http.js";

const API_VERSION = "2026-09-30.endive";

function stripeClient(): Stripe {
  const key = Deno.env.get("STRIPE_RESTRICTED_KEY") || "";
  assertSandboxRestrictedKey(key);
  return new Stripe(key, { apiVersion: API_VERSION });
}

Deno.serve(async (req) => {
  const siteOrigin = Deno.env.get("SITE_ORIGIN") || "";
  let stripe: Stripe;
  try {
    stripe = stripeClient();
  } catch (_err) {
    return new Response(JSON.stringify({ error: "Billing is not configured." }), {
      status: 503,
      headers: { "Content-Type": "application/json", "Content-Security-Policy": "default-src 'none'" },
    });
  }
  const url = Deno.env.get("SUPABASE_URL") || "";
  const publishable = Deno.env.get("SUPABASE_PUBLISHABLE_KEY") || Deno.env.get("SUPABASE_ANON_KEY") || "";
  const token = (req.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
  const userClient = url && publishable
    ? createClient(url, publishable, {
      global: { headers: { Authorization: "Bearer " + token } },
      auth: { persistSession: false, autoRefreshToken: false },
    })
    : null;
  const deps = {
    billingOpen: Deno.env.get("BILLING_OPEN") === "true",
    siteOrigin,
    prices: {
      three: Deno.env.get("STRIPE_PRICE_THREE") || "",
      five: Deno.env.get("STRIPE_PRICE_FIVE") || "",
    },
    stripe,
    getUser: async (jwt: string) => {
      if (!userClient) return null;
      const { data, error } = await userClient.auth.getUser(jwt);
      if (error || !data.user) return null;
      return { id: data.user.id };
    },
    customerFor: async (userId: string) => {
      if (!userClient) return "";
      const { data, error } = await userClient.from("entitlements").select("stripe_customer_id").eq("user_id", userId).maybeSingle();
      if (error || !data) return "";
      return data.stripe_customer_id || "";
    },
  };
  return handleSignedIn(req, deps);
});
