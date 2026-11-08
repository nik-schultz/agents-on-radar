# Saved setups: what is built, and what is not live

Updated 2026-11-08. This is not an approved legal policy. Checkout is not on. Sign-in is not on.

## What a saved setup is

A saved setup is the instruction text for a job the person runs in their own chat app (ChatGPT, Claude, Gemini, Copilot, Grok, or similar). This site does not host the bot, does not open a calendar, and does not send the plan anywhere.

The free builder at `/bot-instructions/` still works with nothing stored. Weekly planning is the starter. Email drafts and quote comparisons stay available. The guides and blueprints on the rest of the site stay as they are.

## Proposed prices (not on sale)

| Plan | Price | What the number means |
|---|---|---|
| 3 setups | $9/month | Up to 3 saved instruction setups |
| 5 setups | $14/month | Up to 5 saved instruction setups, $5 more |

The number is not three or five connected products, and it does not include a model subscription. More than one setup can be a weekly plan.

These prices are not charged. `config.json` keeps `saved_setups.sign_in`, `billing`, `live_launch`, and `auth_email_ready` false. `validate.py` fails the build if that changes. There is no Stripe Price ID in the repo. Stripe Billing would add 0.7% of Billing volume plus the applicable processing fee. That is not a quote and no paid Stripe plan was activated.

An assisted human service is not offered. Do not put a second price on the page.

## What is implemented in this branch

- Postgres migration `supabase/migrations/20261108160000_saved_setups.sql`: tables, RLS, and functions to create, save a new version, and soft-delete. The cap locks the entitlement row. Downgrade and past-due do not delete rows. New creates and edits stop when the account is not active or is at the cap. Export of remaining rows stays allowed by the select policy.
- `accounts/billing.py`: Checkout Session parameters (subscription, allowlisted price, no `automatic_tax`, no `payment_method_types`), webhook signature checks, duplicate event ids, out-of-order events, cancel, failed payment, and unknown prices. A browser return cannot grant a plan. No code path deletes setups.
- `accounts/library.py`: in-memory model of the same cap, including two threads at a limit of one.
- `static/accounts.js`: on the default build it leaves sign-in and checkout disabled. The signed-in library can list, save a version, export, delete, and import the on-device weekly copy only after a click. It does not send a sign-in email while `auth_email_ready` is false. Checkout and portal buttons stay disabled unless `billing` and `live_launch` are both true, and even then they send only `plan_code` or `{action: "portal"}`. A return link does not grant a plan.
- `supabase/functions/billing` and `supabase/functions/stripe-webhook`: Edge Functions. Checkout uses a `Stripe` client instance at API `2026-09-30.endive`, dynamic payment methods, and no `automatic_tax`. The webhook verifies the Stripe signature and calls `public.apply_billing_event` through `BILLING_DB_URL`. `verify_jwt` is false only for the webhook. See `ops/accounts-billing-config.md`.
- `supabase/migrations/20261108183000_billing_event.sql`: idempotent entitlement updates, including duplicate, stale, cancel-at-period-end, failed payment, and unknown price. The function is security invoker. Role `billing_writer` cannot read setups. No public function is security definer.
- Local tests: `accounts/test_billing.py`, `accounts/test_http_billing.mjs`, `accounts/test_library_ui.mjs`, `accounts/test_secrets.py`, and `accounts/test_rls.py` (local Postgres only, with a stub `auth.uid()`, not a Supabase project).

## What was not run

- No Supabase project was created or migrated. The inspected organization is not approved for this product. Do not create the project there unless that choice is made separately.
- No Stripe sandbox, product, price, webhook, or portal configuration was created. The connected live account is sponsorships only and is not approved for these integration tests. Live mode was not used.
- The Stripe Node SDK is in the Edge Function source and is not called from this environment. No Checkout Session was created.
- Customer auth email was not sent. Built-in Supabase mail is not a customer signup path. That is a blocker, not a passing test.
- `accounts.js` was exercised with a local stub client. That is not Supabase Auth and not production.
- Webhook delivery from Stripe was not received. Tests use signed fixtures and local Postgres.
- Stripe Tax was not enabled. Do not turn on `automatic_tax`. Stripe collects no tax until a registration exists, and this integration does not assume a tax outcome.
- Directory lookup and Stripe Projects were not completed. Do not treat a browser-auth error as permission to log in with the CLI or to extract a key.

## Launch gates before any recurring charge

1. A new Supabase project for this product only. Apply the migration there. Do not point this at an unrelated project. Keep the `private` schema out of the Data API exposed schemas.
2. Confirm the current Supabase free-tier limits (database size, monthly active users, egress) on Supabase's pricing page. This file does not freeze a number.
3. Auth: email magic link or another Supabase-supported method. Allowlist only the real site URL as the redirect. No passwords in this app.
4. Two Stripe products, one monthly price each: $9 for 3 setups and $14 for 5. Use a restricted key (`rk_`) for the billing server. Store it in a secrets manager, not in git, the browser, or logs.
5. Deploy the Edge Functions in `supabase/functions/` only after the secret names in `ops/accounts-billing-config.md` exist. Use a new sandbox restricted key (`rk_test_`). Do not use the live account. `BILLING_OPEN` stays unset until an end-to-end sandbox payment is verified. The webhook writer is role `billing_writer`, not the project service role.
6. Webhook events to handle: `checkout.session.completed`, `checkout.session.async_payment_succeeded`, `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.payment_failed`, `charge.refunded`, `charge.dispute.created`, `radar.early_fraud_warning.created`. Record the event id before applying it.
7. Customer Portal so a person can upgrade, downgrade, or cancel. Downgrade must not delete setups. Over the cap: they can still read and export; they cannot create another until they are back under the cap or on the higher plan.
8. Set `sign_in` and `billing` only in a private environment, with `live_launch` still false, and click through sign-in, reload, a second user, the cap, a duplicate webhook, and cancel. Then set `live_launch` in that environment, not by committing secrets.
9. Privacy policy update that names Supabase and Stripe before any account exists. The current policy says this build does not store setups.
10. Proposed, not approved: cancel at period end in the Stripe portal; no refund of a month already started unless a separate decision says so; no support promise that a person will revise a week. The free builder remains the support that exists today.
11. Stripe fees and Supabase overage are operating costs. Read the current price pages before launch. This change does not start a paid Stripe or Supabase plan.

## Fallback

If the database or the billing server is down, the public site must keep the free builder and keep sign-in and checkout disabled. Do not pretend a setup was saved.
