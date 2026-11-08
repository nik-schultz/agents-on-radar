# Account and billing configuration

This is a requirements list for a later project. It does not provision anything. No value in this file is a credential. Checkout stays closed. Customer email stays blocked.

The free builder does not need any of these settings.

## Topology

GitHub Pages serves the site. A dedicated Supabase project on the Free plan would provide Auth, Postgres, row level security, and Edge Functions. No separate hosting vendor is required for the billing server. Edge Functions are a suitable free-plan place for Checkout, the Customer Portal, and the webhook: the Free plan includes 500,000 function invocations, and extra invocations are not billed as a surprise invoice on Free (fair use and a grace period apply). This is conditional on a project that does not exist yet.

Do not attach this product to an existing organization or an unrelated project. An infrastructure check found only an unrelated Free organization and no BotsDoThat project. That finding is not approval to create the project there. Wait for an organizational choice and a cost confirmation.

Do not use the connected live Stripe account for these tests. It has sponsorship products only. No subscription price exists. No sandbox exists. Stripe Directory and Stripe Projects could not be initialized from this environment (`Invalid user agent`, `BROWSER_AUTH_REQUIRED`). Do not work around that with `stripe login` or by reading a key out of a browser.

## Secret names

Set these only in the Supabase function secret store, or in the database role password that the connection string points at. Never commit them, paste them into chat, or put them in `config.json`.

| Name | Where | Least privilege |
|---|---|---|
| `SUPABASE_URL` | `billing` function, and later the public site config after a parent checks the value | Project URL only. Not a secret, but it must be the dedicated project. |
| `SUPABASE_PUBLISHABLE_KEY` | `billing` function and, after a parent check, `config.json` `saved_setups.supabase_publishable_key` | `sb_publishable_` key. Safe in the browser. Never a secret key. |
| `SUPABASE_ANON_KEY` | Optional fallback the `billing` function reads if the publishable name is unset | Legacy browser key. Not a service role. |
| `BILLING_DB_URL` | `stripe-webhook` function only | Transaction-pooler URI (port 6543) for role `billing_writer`. `prepare` must stay off. The role can insert and update `entitlements`, insert `stripe_events`, and execute `public.apply_billing_event`. It cannot read or delete `setups` or `setup_versions`. Do not substitute the project service-role key or `sb_secret_`. |
| `STRIPE_RESTRICTED_KEY` | Both functions, server only | Sandbox restricted key, prefix `rk_test_`. The code rejects `rk_live_` and `sk_`. Permissions: Checkout Sessions write, Customer Portal sessions write, Customers read, Subscriptions read, Prices read. No tax, payout, refund, dispute, or account-setting writes. No bank or payout change. |
| `STRIPE_WEBHOOK_SECRET` | `stripe-webhook` only | Signing secret for the sandbox endpoint. |
| `STRIPE_PRICE_THREE` | Both functions | Sandbox Price id for the $9 / 3-setup product. One product, one monthly price. |
| `STRIPE_PRICE_FIVE` | Both functions | Sandbox Price id for the $14 / 5-setup product. A separate product. |
| `SITE_ORIGIN` | Both functions | `https://botsdothat.com` when the site is the caller. Success, cancel, and portal return URLs are built from this. The browser cannot supply them. |
| `BILLING_OPEN` | `billing` function | Leave unset. The string `true` is the only value that opens Checkout and the portal. Do not set it until a sandbox payment, webhook, and portal session have been verified end to end. |

The platform may also inject `SUPABASE_SERVICE_ROLE_KEY`. The functions do not read it.

## Flags that stay false in git

`saved_setups.sign_in`, `billing`, `live_launch`, and `auth_email_ready` stay false. `validate.py` fails if any of them is true. The public page therefore never calls Auth or Checkout.

## Auth email blocker

Supabase's built-in mail sends only to organization team members and is limited to about 2 messages an hour. That cannot sign up or recover a customer. Production needs an approved mail provider (custom SMTP or an OAuth provider) before any customer sign-in email. Until `auth_email_ready` is turned on in a private environment, the page disables the email button and does not call `signInWithOtp`. A local stub session is not a successful customer sign-in. No test recipient is approved, so no sign-in email should be sent.

## Webhook

`supabase/config.toml` sets `verify_jwt = false` for `stripe-webhook` only, because Stripe does not send a user JWT. The function verifies the Stripe signature with `constructEventAsync` and then writes the entitlement. `billing` keeps `verify_jwt = true` and also calls `getUser`. Plan state is never taken from `user_metadata` or `app_metadata`.

Events the SQL function applies: `checkout.session.completed`, `checkout.session.async_payment_succeeded` (only when `payment_status` is `paid` or `no_payment_required` and the price is allowlisted), `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.payment_failed`, `charge.refunded`, `charge.dispute.created`, and `radar.early_fraud_warning.created`. A duplicate event id is a no-op. An older `created` time does not overwrite a newer row. Cancel at period end keeps access until the subscription is deleted. Failed payment and an unknown price stop new saves and edits. Rows are not deleted.

## Stripe Tax

Do not enable Stripe Tax or `automatic_tax`. No registration is in place. Do not change tax, payout, bank, refund, or account settings.

## What this environment did not prove

No Deno deploy, no Supabase Auth round trip, no Stripe API call, no sandbox, no live charge, and no customer email. The product is not money-ready.
