# BotsDoThat growth plan: newsletter, social, SEO (written Oct 30, 2026 by BotsDoThat - SEO)

Status: PLAN + DRAFTS ONLY. Nothing here has been posted, emailed or submitted. Anything external needs Grok CEO approval (and Nik's where noted). Social posting is owned by BotsDoThat - Marketing; the X drafts below are for Marketing / Nik to review.

Real data this plan is based on (no estimates):
- Google Search Console, Oct 22-26 (first data): 3 clicks, 183 impressions, avg position 22.7; 117 pages indexed. Cost and no-code queries sit at positions 61-98. /news/ had 33 impressions at avg position 8.2.
- Cloudflare Web Analytics, week to Oct 28: 106 visits (79 direct, 25 from Google).
- Bing: sitemap read, no impressions yet.
- Google autocomplete (free, pulled Oct 30, 2026 ~8:50 AM CT), suggestions seen: "ai agent cost per month", "how much does an ai agent cost per month", "how much does an ai agent cost to run", "ai voice agent cost per month", "personal ai agent cost", "build ai agent without coding", "can i build ai agent without coding", "ai agent news today", "ai agent newsletter", "openclaw alternatives", "openclaw vs hermes", "hermes agent install", "best ai agent for personal assistant", "best ai agent for travel planning", "ai agent to book flights", "ai agent to book restaurants", "ai agent for email triage", "free ai agent for job application". Autocomplete shows demand exists, not volume.
- @botsdothat (from /workspace/botsdothat/weekly-results.md): first posts got 6-9 impressions each.

## 1. Newsletter audit (Oct 30)

How it works today
- Provider: Kit (form 10088120, double opt-in), hosted page https://botsdothat.kit.com/e874d57257. Forms POST to https://app.kit.com/forms/10088120/subscriptions via fetch with an inline "check your email" message; Kit's "quarantined" bot check is handled (redirects to Kit's reCAPTCHA page). No Supabase table is involved.
- Where the form appears: homepage (mid-page + bottom), /newsletter/, every web issue, the end of every use case and blueprint, /trending/, /news/, the 6 beginner guides, plus a card in unsold sponsor spots on category pages and use-case sidebars. Nav has a "Get the weekly email" button on every page.
- Pages that had NO signup before today: /use-cases/, /blueprints/, /ai-pricing/, /run-your-bots-for-less/, /about/ (fixed today), plus /advertise/, /disclosure/, /privacy/, /sponsor*/ (left alone on purpose).
- End-to-end: config and JS are wired and Kit's CORS preflight was checked on Oct 23. I did NOT submit a test email today (that would create a real subscriber). The Oct 23 changelog notes only a test address had signed up at that time; I can't see the current subscriber count (needs Kit login).

BLOCKER, the biggest one for newsletter growth
- No issue has ever been emailed. data/newsletter.json has issue #1 (Oct 22) and #2 (Oct 29) with sent_on = null. Issue #2 is a Kit draft (broadcast 26680437), sender pending confirmation as hello@botsdothat.com, waiting for Grok CEO + Nik approval. People who subscribe get a confirmation email and then nothing. Fix this before pushing signups hard, or the first subscribers churn and directories like Letterlist (which ask for subscriber count) stay out of reach.

## 2. Shipped today (one batched deploy; see ops/CHANGELOG.md)
- Signup box added to /use-cases/, /blueprints/, /ai-pricing/, /run-your-bots-for-less/, /about/.
- "Forward it" line under every form now points to the shareable /newsletter/ page instead of /#subscribe.
- /newsletter/ is now a real landing page: title "Free AI agents newsletter: the BotsDoThat Weekly", "What's in each issue", "Read the latest issue" button, 5-question FAQ (free, how often, no coding, unsubscribe, what happens to your email) with FAQPage + BreadcrumbList schema, visible breadcrumb.
- Cost guide: title "How much does it cost to run an AI agent per month?" (matches "ai agent cost per month" autocomplete), new description that no longer truncates, and a new "AI agent cost at a glance" box (software, pay-per-use range, voice per-minute, model choice) with jump links and links to the calculator and the no-code guide.
- No-code guide: title "How to build an AI agent without coding in 7 steps", new description.
- /news/: description no longer truncates the key part; new "New to AI agents?" line linking the explainer, no-code guide, cost guide and /newsletter/.

## 3. Top 5 next actions (prioritized)
1. Send the newsletter (needs Grok CEO + Nik). Approve the Kit sender hello@botsdothat.com and send issue #2 (Kit draft 26680437), then keep a fixed weekly day. Everything else in this plan converts better once issues actually arrive.
2. Kit welcome email on the free plan (needs Nik's Kit login; free). The free plan has no sequences/automations (Kit pricing page, per Oct 23 changelog), but the confirmation "thank you" redirect can point to the latest web issue (/newsletter/2026-10-29/) so new subscribers get value immediately. Draft redirect URL: https://botsdothat.com/newsletter/2026-10-29/?utm_source=kit&utm_medium=confirm
3. Push the two pages Google already shows: /news/ (pos 8.2) and the cost/no-code guides (61-98). Today's title/description/answer changes are step one; next is earning 3-5 relevant links (section 6, drafts) and adding the "voice agent cost per month" and "personal ai agent cost" answers to the cost guide.
4. Turn @botsdothat into a reply-led account (Marketing bot). With 6-9 impressions per post, replies under bigger AI accounts are the fastest way to be seen. Use the weekly system in section 5; every post links one page and every Thursday post links /newsletter/ (only once a send is approved).
5. Ship 1-2 query-gap pages per week (section 6), each with the in-content signup box (automatic on use cases), and add each to the next issue.

Needs approval
- Grok CEO + Nik: sending newsletter issues; Kit sender address; Kit confirmation-redirect change; every X post/reply below; every directory/listing/PR/Show HN/Product Hunt submission; any homepage change.
- Nik only (logins): Kit settings; Product Hunt / directory accounts.

## 4. Newsletter growth (free)
- On-site (done/next): signup on every content page (done), /newsletter/ landing page (done). Next, propose only: homepage "start here" strip with a newsletter line (waiting on Nik's homepage decision; proposal goes to the CoS, not shipped).
- Content upgrade idea (no new promise): link "Get next week's 4 jobs by email" from each issue's web page share line; issues are already public web pages, so share each new issue on X the day it's sent.
- Free directories that need a real subscriber count (Letterlist, InboxReads): wait until issues are being sent; drafts live in /workspace/botsdothat/directories/kit.md (Marketing).
- Cross-links: llms.txt already lists the newsletter; add the newsletter RSS (/newsletter/feed.xml) to free RSS directories later.

## 5. Social follower plan for @botsdothat (for BotsDoThat - Marketing and Nik; drafts only)

Weekly content system, built only from site pages (all numbers come from the linked page):
- Mon: "Bot of the week" - one blueprint (instructions to copy).
- Tue: "What it costs" - one number from /ai-pricing/ or the cost guide, with the page.
- Wed: "Real person, real job" - the week's top /trending/ use case, credit the original poster.
- Thu: Newsletter day - the issue's web link + /newsletter/ (only after sending is approved).
- Fri: "Watch out" - one safety tip (file deletion, email safety) linking the guide.
- Daily: 3 helpful replies under bigger AI accounts already followed (see /workspace/botsdothat/follows-log.md), no links in replies unless asked; 5-10 relevant follows a day (Nik approved Oct 23).
- Free growth levers: pin the best-performing post weekly; quote-post official launches from /news/ with the "what it means for you" line; tag the tool's official account when a page covers it (e.g. @NousResearch for Hermes) without asking for reposts; put the X link in every newsletter footer; no engagement bait, no follow-for-follow, no paid boosts.

Five ready-to-post X drafts (each under 280 characters with the link; verify numbers on the page the day it posts):

D1 (cost)
What does an AI agent cost to run? For the 11 everyday bots in our blueprints: under 1¢ to $5.28 a month at official API prices. Math shown, plus app plans, OpenClaw and Hermes.
https://botsdothat.com/how-much-does-it-cost-to-run-an-ai-agent/

D2 (no-code)
You don't need to code to build an AI agent. Pick one boring job, write it in four lines (Goal, Runs, Watches, Never), paste it into an agent app, test once, then schedule it.
7 steps, worked example:
https://botsdothat.com/how-to-build-an-ai-agent-without-coding/

D3 (safety)
Before an AI agent touches your computer: give it one folder of copies, keep a backup it can't reach, and turn on its sandbox or ask-first setting. Setup notes for Claude Cowork, Codex, OpenClaw and Hermes:
https://botsdothat.com/use-cases/keep-an-ai-agent-from-deleting-your-files/

D4 (cheapest API)
Cheapest AI API per token in our table right now: Groq's gpt-oss-20b at $0.075 in / $0.30 out per 1M tokens. Cheapest small model from the big labs: $0.10 / $0.50. Checked against official pages, sources linked:
https://botsdothat.com/ai-pricing/#cheapest
(Re-check /ai-pricing/#cheapest the day it posts; prices were checked Oct 27.)

D5 (newsletter, only after a send is approved)
The BotsDoThat Weekly: 3 to 5 practical jobs you can hand to AI each week, each with a prompt to copy, plus one new guide and one thing to watch out for. Free.
Read this week's issue first:
https://botsdothat.com/newsletter/

## 6. SEO traffic plan, next 4 weeks (Nov 2 - Nov 27, 2026)

Week 1 (Nov 2-6): strengthen what Google already shows
- Re-check GSC on Wed Nov 4 for the new titles (cost, no-code, /news/, /newsletter/). If /news/ holds near 8, propose (don't ship without data) adding "AI agent news" wording to its title/H1, since "ai agent news today" is an autocomplete suggestion.
- Cost guide: add short answers for "ai voice agent cost per month" (voice section already has per-minute prices) and "personal ai agent cost" (link app-plan table). Only official prices.
- New page: "Book flights with an AI agent" (BACKLOG; autocomplete "ai agent to book flights"); approval-before-payment covered.

Week 2 (Nov 9-13): OpenClaw / Hermes cluster (real autocomplete demand: "openclaw alternatives", "hermes agent install", "openclaw vs hermes")
- New page: "OpenClaw alternatives for beginners" (Hermes Agent, agent apps, no-code tools), linked from /openclaw-vs-hermes-agent/.
- New page: "How to install Hermes Agent safely (beginner walkthrough)" from Nous Research docs only.

Week 3 (Nov 16-20): personal-assistant intent
- New page: "Best AI agent for a personal assistant: what each can actually do" (comparison from official docs; no rankings by opinion, criteria shown). Autocomplete "best ai agent for personal assistant".
- New use case: "Triage your inbox with an AI agent" if not already covered by clean-up-your-email-inbox / flag-only-emails-that-need-a-reply; otherwise retitle one of those toward "ai agent for email triage" after checking GSC.

Week 4 (Nov 23-27): consolidate
- Act on the open backlog: the 14 chat-prompt use cases (rework/label), /use-cases/ vs /ai-agent-examples/ cross-pointers (proposed Oct 28, awaiting approval).
- Refresh dates and internal links on every page that gained impressions; report real GSC deltas.

Free backlink and listing ideas (DRAFTS ONLY; nothing submitted; needs Grok CEO approval):
- Already drafted in ops/launch_drafts.md: awesome-openclaw PR (A), awesome-hermes-agent issue (B), Ask HN reply (C), Show HN (section 3), Product Hunt (section 4), Reddit posts (section 2).
- New draft E, free AI-tool/resource directories (submit the site as a free resource, not a tool): There's An AI For That, Futurepedia, Toolify, AlternativeTo. Listing text:
  Name: BotsDoThat
  URL: https://botsdothat.com/
  Short: Real things people hand to AI agents, with sources, copy-paste prompts and build-your-own-bot blueprints. Free.
  Long: BotsDoThat tracks real, sourced examples of people handing jobs to AI agents (inbox, phone calls, shopping, travel, family, work), with plain-English guides, copy-paste prompts, a free AI agent cost calculator and an official-source AI price table. No sign-up needed; optional free weekly email.
  Category: AI agents / Education / Directories. Pricing: Free.
- New draft F, GitHub awesome-lists for AI agents for beginners (one-line entry, only where the list accepts guides/resources and only after reading CONTRIBUTING.md):
  "- [BotsDoThat](https://botsdothat.com/) - Sourced, real-world AI agent use cases with copy-paste prompts, beginner build guides and a free AI agent cost calculator."
- New draft G, the free price table as a linkable asset: reply/mention in threads where people ask "how much does running an agent cost" (Reddit r/AI_Agents, r/LocalLLaMA, HN), linking /how-much-does-it-cost-to-run-an-ai-agent/ only when it directly answers the question. Nik posts in his own words.
- Keep: SaaSHub listing (claimed Oct 24, awaiting their approval).
