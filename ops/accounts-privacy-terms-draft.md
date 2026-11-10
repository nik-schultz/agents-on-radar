# Draft for review: saved-setup privacy and terms

Not published. Not a contract. The live privacy page still describes the site as it is today: the free builder does not store setups, Kit handles the newsletter, and Stripe handles sponsor payments. Do not replace that page until this draft is reviewed and a project actually exists.

Words like "would" below mean "only if the project is later provisioned and checkout is opened." They are not a description of the current site.

## Who we are

BotsDoThat, contact hello@botsdothat.com. This draft covers a future optional account for saved instruction setups. It does not cover sponsor ads or the newsletter, which already have their own pages.

## What a saved setup would be

Instruction text the customer pastes into their own chat app. BotsDoThat would store that text so the customer can edit, export, or delete it. BotsDoThat would not run the bot, open a calendar, send the email, or pay a vendor.

The free builder would keep working with no account. Nothing typed there is sent to BotsDoThat unless the customer later chooses "Import the weekly setup saved on this device" while signed in.

## What we would store, and who would process it

Conditional, because neither processor is connected for this product:

- Supabase, if a dedicated project is created: the account email, a sign-in session, and the customer's setups, versions, and entitlement row (plan, status, cap, Stripe customer id, period end). Proposed. Not provisioned. An existing unrelated organization is not approved for this.
- Stripe, if a separate sandbox is verified and, later, live prices are created: the subscription, payment method, and receipts. Card numbers would stay with Stripe. Proposed. Not provisioned. The connected live Stripe account is sponsorships only and is not approved for these tests.
- Kit already stores newsletter addresses. That does not change.
- Stripe already processes sponsor payments. That does not change.

No other processor is proposed. No model API is proposed.

## Sign-in email

Customer sign-in email is blocked. Supabase's built-in mail only reaches organization team members and is limited to about 2 messages an hour. It is not suitable for customer signup or recovery. No sign-in email is sent until an approved mail provider is configured and a specific test recipient is approved.

## Caps and access

A $9 monthly plan would allow 3 saved setups. A $14 monthly plan would allow 5. The database would enforce the cap. If a payment fails, the price is not one of those two, or the subscription ends, the customer could still read and export what is already saved. New saves and edits would stop. Deleting a setup would be the customer's action. We would not delete setups because a subscription changed.

## Checkout

A browser return from Checkout would not turn a plan on. Only a signed Stripe webhook would. Checkout is closed until that path is verified. The page would not ask the customer for an amount or a cap.

## Cancellation, refunds, and tax

This draft does not promise a refund, a cancel-anytime right, a notice period, or a credit. If a subscription is later sold, Stripe's customer portal is the place a customer would change or stop it, and Stripe's own terms would govern the payment. A subscription marked to stop at period end would keep the current cap until Stripe reports it ended. We do not promise that period in a contract beyond what Stripe reports.

Stripe Billing's published fee for this kind of subscription is 0.7% of Billing volume plus the applicable card-processing fee. That is Stripe's price, not a quote we have been invoiced, and no paid Stripe plan was activated for this product.

Stripe Tax is not enabled. Prices would be shown as the subscription price only. We would not turn on automatic tax, and we would not change payout, bank, refund, or tax registration settings, unless a later review says so.

## Support

Support today is the free builder and email to hello@botsdothat.com about the site. Nobody is on call to revise a week, fix a chat reply, or fulfill a setup by hand. A saved setup would not add that service.

## What this draft is not

It is not legal advice, not an approved policy, and not evidence that accounts or payments are available.
