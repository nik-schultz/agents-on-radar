# Affiliate and referral programs for BotsDoThat (formerly Agents on Radar)

Researched Oct 21, 2026 (evening, CT). Terms are quoted or paraphrased from each program's **official page** unless marked "third-party". Programs change terms. Re-read the official page on the day you apply.

**Status: nothing applied for, nothing signed up for.** Every program below needs Nik to create the account himself.

**How to use them on the site:**
- Put links in `data/` only once approved.
- Render links with `aff_link()` in build.py. It adds `rel="sponsored"` and the "Affiliate link" label pointing to /disclosure/.
- Turn on the disclosure page's "Right now" wording.

## Fit with our audience

- **Who reads the site:** everyday people building their first bot: inbox, calendar, shopping, phone calls, family.
- **What they need:**
  - an automation tool (Make, n8n, Zapier);
  - an agent builder (Lindy, Relevance AI, Gumloop);
  - phone/voice agents (ElevenLabs, Retell, Vapi, Synthflow);
  - somewhere to host a bot (Railway, DigitalOcean);
  - a password manager to keep bot logins safe (1Password).

## Top 5 to apply for first

| # | Program | Commission (as stated) | Who can join / approval | New low-traffic site? | Why first |
|---|---|---|---|---|---|
| 1 | **Make** — https://www.make.com/en/affiliate (help: https://help.make.com/affiliate-program) | 35% of referred users' subscription payments for 12 months (window starts at registration, not first payment). Not on extra operations. 30-day cookie. Payout via Wise once you have $100 **and** 3 unique paying referrals. | "Anyone with a Make account can become an affiliate." No traffic minimum stated. | **Yes**: no approval gate stated. | Several blueprints already use Make-style automations; highest stated rate; open to anyone. |
| 2 | **n8n** — https://n8n.io/affiliates/ (apply: PartnerStack) | 30% of net earnings on n8n Cloud referrals for 12 months. PayPal, monthly, min €100. PartnerStack listing says 90-day cookie. | "Anyone can become an n8n affiliate." Application reviewed. PartnerStack form says up to 2 weeks because of high volume. | **Likely**: open application, content creators invited; no traffic minimum stated. | n8n is the self-host/low-cost pick that fits "Run your bots for less". |
| 3 | **ElevenLabs** — https://elevenlabs.io/affiliate (terms: https://elevenlabs.io/affiliates-terms) | 22% for the first 12 months on Starter/Creator/Pro/Scale; 11% on Business; none on Enterprise. Paid via PartnerStack after a 90-day hold. $5 minimum. | Natural persons only. One account each. May have to prove you own the site. No self-referrals. | **Likely**: no traffic minimum stated. | Phone/voice bots are a site category. ElevenLabs also sells consumer plans our readers can afford. |
| 4 | **Railway** — https://docs.railway.com/community/affiliate-program | Referred signups get $20 credits. You get 15% of the first 12 months of their invoices. Withdraw via GitHub Sponsors or Buy Me a Coffee. | Any Railway user: copy the link from the dashboard's Refer page. | **Yes**: no application at all. | "Where do I host my bot" comes up in blueprints. The $20 credit is a genuine reader benefit. |
| 5 | **Retell AI** — https://www.retellai.com/affiliate | 15% of each referral's revenue, monthly, for 12 months. 90-day cookie. Monthly payouts, "no thresholds". | Sign up and get the link "in minutes". Aimed at creators, newsletter writers and communities. | **Yes** (seems self-serve). | Best-documented open voice-agent program; fits the phone-call use cases. |

**Order to apply:**
1. Make and Railway first (instant, no review).
2. Then n8n and ElevenLabs (reviewed; worth having a few weeks of published content first).
3. Then Retell.

## Also checked

| Program | Terms (as stated) | Join | Notes |
|---|---|---|---|
| **Lindy** — PartnerStack https://market.partnerstack.com/page/lindy · Dub https://partners.dub.co/lindy | PartnerStack: 30% year one, 15% year two. Dub creator program: 20% per sale for 1 year, plus 20% of referred partners' commissions, plus social bounties. | Application. The Dub program says it is available in the US, UK, Canada and Australia. | Good fit (an agent product). Strong #6. |
| **Gumloop** — https://www.gumloop.com/partners/apply-to-be-a-creator | 20% of a new customer's subscription for up to 12 months. | Creator application. | Business-leaning agent builder. |
| **Relevance AI** — https://relevanceai.com/affiliate-program | "Recurring commissions"; rates are shown only inside the portal. A third-party summary of their terms page says 15% for 12 months, 60-day window and $50 minimum (**unverified**). | Apply via Rewardful. | Business audience, weaker fit. |
| **1Password** — https://1password.com/affiliate | $2 per completed signup + 25% of the first year or month's payment ($2 minimum). One-time, not recurring. | Through a CJ Affiliate account; approval required. | Good safety fit ("give your bot its own login"). Low payout. CJ approval can be harder for new sites. |
| **Synthflow** — https://synthflow.ai/partners | Official changelog (June 2024) said the affiliate rate rose to 30% for up to 15 months (https://feedback.synthflow.ai/changelog/make-plugin-custom-actions-v2-contacts-payments-and-more-rocket). The current partner page doesn't publish a rate. | Application. | Verify the current rate before relying on it. |
| **Vapi** — https://vapi.ai/creators | 15% referral revenue (creator program). | **"Applications on hold"** as of today. | Not available now. |
| **DigitalOcean** — https://www.digitalocean.com/referral-program | You get $25 credit after the referred user spends their first $25. Credit, not cash. | Any customer. | Low value; only if Nik already uses DO. |
| **Zapier** — https://zapier.com/legal/ambassador-affiliate-terms | Rates only in the partner portal. | **Invite or approval only** ("invited to apply or approved"); creator program via PartnerStack. The Solution Partner program needs a business site and custom-domain email. | Not realistic for a new site yet. |
| **OpenRouter** | No public affiliate or referral program found on its site or docs (https://openrouter.ai/docs/faq). | — | Skip. |
| **Hetzner** | Referral program discontinued (https://docs.hetzner.com/cloud/general/faq/). | — | Skip. |
| **Bitwarden** | Says it has no monetary referral program (official blog). Partner program is for MSPs and resellers (https://bitwarden.com/partners/). | — | Skip. |

## Rules to follow once approved

- Label every affiliate link (the `paid_label("affiliate")` component) and keep /disclosure/ accurate. This follows the FTC endorsement guides.
- Never let commission change the calculator, price table, rankings or "Which tool to use" order. Always show free or non-affiliate options alongside.
- r/automation and r/SideProject reportedly ban affiliate/referral links (see ops/launch_drafts.md). Never put affiliate links in community posts.
- Make: don't bid on the "Make" trademark in paid ads (their FAQ).
