# Bot instruction builder: launch readiness

Status on 2026-11-08: the free builder can ship. The $29 pilot must not be charged. Checkout stays closed. This note is a plan, not a live support desk.

## What works in this version

`/bot-instructions/` is a static page. `scripts/bot_builder.py` and `static/bot-builder.js` fill the same fixed template from the reader's answers. Troubleshooting matches a written list of four patterns (missing inputs, invented facts, wrong format, skipped steps). Neither step calls a model.

Tasks, all text the person pastes into a chat they already have:

- Plan one week from notes they type. No calendar connection.
- Draft a professional email. Drafting does not send it.
- Compare everyday quotes they paste. No shopping, payment, or "buy this" verdict.

The page refuses passwords, long private numbers, and medical, legal, financial, insurance, and lending topics. User text is quoted as data so it cannot delete the permission boundaries. With JavaScript off, fictional samples are still on the page.

Nothing from the form is submitted. There is no account and no database row.

## What the page tells people

- The builder is a template, not a live reviewer.
- A tick that "a test matched" is the reader's report. BotsDoThat has not seen the chat.
- $29 is a proposed one-time introductory price for one task, a tailored setup, a walkthrough, and troubleshooting for seven days.
- No recurring bill and no guaranteed business result.
- Checkout is closed. The button is disabled. There is no payment URL.

`data/bot-builder.json` keeps `offer.status` at `closed` and `checkout_url` empty. `scripts/validate.py` fails the build if that changes.

## Proposed offer (not on sale)

| Item | Proposal |
|---|---|
| Price | $29 once |
| Scope | One task from the three on the page |
| Included | Tailored setup, a walkthrough of how to paste and run the written tests, troubleshooting replies for seven days after delivery |
| Not included | A second task, a subscription, account access, sending email, buying anything, medical/legal/financial advice, a guaranteed outcome |
| Proof | The customer runs the tests. A match they report is not an independent check |

Do not publish this as available until the blockers below are actually done.

## Lean fulfillment flow (proposed, not operating)

One person (Nik) would do this. There is no support staff, and this document does not create any.

1. The customer uses the free builder and runs the tests themselves. That part exists today.
2. A future checkout charges $29 once, as its own product, with no renewal.
3. After payment, a private intake asks only for: which task, the same non-secret answers, which chat app they will paste into, and an email for replies. Reject secrets. Say how long the task text is kept (decision needed: delete the task text 30 days after the seven-day window; the payment record stays with the processor as their rules require).
4. Delivery is a reply with the instructions, a short walkthrough (where to paste, how to run test 1 and test 2, what "pass" means), and the clock-start time.
5. For seven calendar days from that delivery, replies use the same four patterns plus a human reading of "expected" versus "actual". A cap on replies has to be chosen before sale (a draft to approve: 8 replies, or day 7, whichever comes first). Do not advertise a cap that has not been approved.
6. Close the case as "customer reported a match" or "ended on day 7 without a reported match". Neither label means the chat was reproduced here.
7. Refunds are not live. A draft to approve before any charge: full refund if the setup was not sent yet; no refund for a change of mind after delivery; full refund if the setup is not delivered within 3 business days. Those sentences are not terms of sale until they are approved and shown before payment.

## What existing free infrastructure can and cannot do

No new service was installed for this, and none should be installed just to "open checkout".

| Already here | Useful for | Not useful for |
|---|---|---|
| GitHub Pages (`scripts/deploy.sh` only) | Serving the free builder | Private intake. A form POST has nowhere to go. Do not add a form that pretends to send and then drops the text. |
| Public GitHub issues (`contact_url` in `config.json`) | Public site bugs | Task details. Issues are public. Do not ask a customer to paste their notes there. |
| `hello@botsdothat.com` | The published contact address | A support queue. There is no ticket id, no shared inbox procedure, and no backup when Nik is away. Mail by itself is not case tracking. Do not call this mailbox a pilot desk until a retention rule and a label convention are written down and agreed. |
| Kit | The newsletter, double opt-in | Support. Do not send a broadcast. Do not add pilot customers as subscribers for this. |
| Stripe sponsor Payment Links on `/advertise/` | Sponsor spots only (different prices, monthly, different refund terms in `sponsor-terms`) | This pilot. Do not reuse those links. Do not add a new Payment Link in the same change as the free page. |
| Cloudflare Web Analytics | Page counts, no cookies | Form contents. It does not receive the builder answers. |

## Exact blockers before any payment link

All of these are open. Opening checkout while any one is missing is the failure this page is built to avoid.

1. Private intake that is not GitHub issues, not a static form, and not Kit. The customer’s task text must be readable only by the person doing the work.
2. A delivery channel Nik will actually answer, plus a rule for what happens if he is away (if there is no away plan, checkout stays closed while he is away).
3. A case record with: id, email, task, amount, paid time, delivery time, day-7 end, reply count, and outcome label. Access limited to Nik. Not a public board.
4. Written limits he has approved: one task, seven days, the reply cap, and the out-of-scope list above.
5. Written refund terms he has approved, shown before payment, not only in this file.
6. A new one-time $29 product. Not the sponsor links. No recurring price. No trial that converts to a subscription.
7. A privacy-policy change that covers storing the task text. The current policy only covers the browser-only builder and the newsletter.
8. A cap on how many pilots can be open at once. He picks the number. It is not invented here.
9. No public quote, star rating, or "customer result" unless that person agrees in a separate message that is not the purchase itself.
10. Support copy that does not say "team", "agents standing by", "verified", or "fixed" unless a person actually checked that chat.

## What not to do when this is turned on later

- Do not deploy with anything except `scripts/deploy.sh`.
- Do not mark `offer.status` open in `data/bot-builder.json` until the blockers are done. Validate will fail a checkout URL on purpose.
- Do not paste a Stripe link into the builder page "just in case".
- Do not describe local template rules as an AI agent that tested the bot.
