# PLAN

> **Update 2026-10-20: new direction.** The site is now a LIVE hub: a sourced feed of real AI agent use cases
> (Trending now → Just added → Categories), real popularity numbers (X likes/reposts, Reddit upvotes, with
> source URL and date measured; null when unknown), plus a beginner layer ("What can bots actually do?" and 12
> build-your-own-bot blueprints). Working name: **Agents on Radar** (one-line swap in `config.json`). Seeded with
> 40 new use cases researched on 2026-10-20 + the best 20 from the first version. The daily routine is documented in
> README.md (`scripts/daily.sh`). Sections below that describe the first version (brand "Let The Bot", top-20
> table) are kept for history; the brand was rejected and the content model has been replaced.
>
> **Future agents for the live hub:** (1) Scout: daily X/Reddit/web search, writes `data/incoming/*.json`;
> (2) Meter: refreshes popularity via `get_posts_by_ids` and runs `refresh_popularity.py`; (3) Fact-checker:
> verifies sources and tool claims, flags stale tool facts; (4) Blueprint writer: turns trending use cases into
> blueprints; (5) Newsletter editor: weekly "radar" issue from the history log; (6) Link/SEO ops: link check,
> sitemap, llms.txt; (7) Sponsor ops. A human approves publishing and any outbound message. Routine deploys of the live site (`scripts/deploy.sh`) were approved on 2026-10-21.


Owner: Nik Schultz · Working brand: **Let The Bot** (letthebot.com, unregistered per RDAP on 2026-10-19; not purchased)
Sources for every number below: `research/SOURCES.md`. Raw autocomplete pulls: `research/autocomplete.txt`.

## 1. Positioning
**"Hand your boring life admin to an AI, step by step, in plain English."**
A problem-first site for non-technical people. Each page starts from a real-life chore (a denied claim, a confusing letter,
an appointment you can't get), says what you'll end up with, and gives a copy-paste prompt, the tools that work, and safety checks.
This is a fully separate brand. Money is one category among nine.

Why there's a gap:
- The big AI directories are tool-first and aimed at pros and businesses. There's An AI For That maps 50,000+ tools to tasks
  (Digica). Futurepedia now belongs to HubSpot and describes itself as "where businesses figure out AI" (LinkedIn).
  TAAFT traffic was estimated at 3.5M visits in Sep 2026, down 26% month over month, with most of the drop from organic search (Sigpik).
  That's a third-party estimate, but it suggests directory pages are losing search traffic.
- Interest is far ahead of use, and trust is low. 40.1% of US adults would hand at least one of 13 everyday tasks to an AI agent,
  but only 7.7% say they use agentic AI, and 40.6% aren't sure agents are a good idea (Channel V/Prosper, June 2026).
  Among AI users, 41% have tried an agent and 24% use one regularly (Menlo 2026). People need guided, safe how-tos.
- People want guardrails: 34% of Canadians want human review above a set amount and 29% want a "panic button" (Visa, Feb 2026).
  Our "ask before you confirm" prompts and "watch out" sections speak to exactly that.
- Plain-English players exist (aiforregulars.com, personalaiuse.com, beginnersinai.org, realagentcases.com), but they're mostly
  generic "30 ways to use AI" lists or story collections. Few offer deep, sourced, task-level playbooks with official rules.
  Our edge: one page per real problem, official deadlines and rules cited, agent-era instructions (what the agent can actually do
  according to vendor help pages), and honest limits.

## 2. Brand names (RDAP .com checks via rdap.verisign.com, 2026-10-19)
| Name | .com | Notes |
|---|---|---|
| **Let The Bot** ✅ picked | letthebot.com: **not registered** (RDAP 404, rechecked) | Short, plain, verb-led ("let the bot do it"); works for chat and agents; memorable in conversation. |
| PileClear | pileclear.com: not registered | "Clear your pile" is a good life-admin metaphor, but it doesn't say AI. |
| Send The Agent | sendtheagent.com: not registered | Agent-forward. Could date as the jargon shifts, and "agent" confuses non-tech readers. |
| Agent Kindly | agentkindly.com: not registered | Warm, but vague. |
| Do It With An AI | doitwithanai.com: not registered | Good for SEO, weak as a brand. |
Taken (RDAP 200): handittoai, everydayagent, agenthowto, aierrands, lifeadminai, errandagent, plainagent, askyouragent, agentforthat and others (see research/rdap.txt).
Caveats: RDAP shows registry status only. A name can be registered by someone else before purchase, and premium/aftermarket pricing isn't shown.
I ran a quick web search and found no obvious conflicting brand, but **no trademark search was done** (do a USPTO TESS check before buying).

## 3. Audience
Busy, non-technical adults 30–70 with lots of household admin: parents, caregivers for aging parents, renters, freelancers
and one-person businesses. Two data points: 45% of Boomers had used AI, and parents are heavy users (79% had used it, 29% daily) (Menlo 2025).
They know ChatGPT exists, but they don't know what to type and don't trust it to act for them.

## 4. Top 20 use cases (all built as pages)
"Signal" is why we think people search for it. Autocomplete shows that people type these phrases; it does not give volumes.
| # | Use case | Category | Intent signal |
|---|---|---|---|
| 1 | Appeal a health insurance denial (full guide) | Health | Autocomplete "using ai to appeal insurance denial", "ai to fight insurance denials"; Reddit/HN success stories; KFF: <1% of denied claims appealed |
| 2 | Understand a confusing letter (full guide) | Paperwork | "ai to read my pdf", "use ai to write a letter…"; IRS scam guidance |
| 3 | Have an AI agent book an appointment (full guide) | Bookings | "ai agent to book appointments/restaurants/flights"; restaurant booking was the #1 task people would delegate (12.1%); 21% want AI to book doctor visits (EY) |
| 4 | Question a medical bill | Money | "ai to negotiate medical bills"; widely shared self-reported $195k→$33k story |
| 5 | Find & cancel forgotten subscriptions | Money | "use ai to cancel subscription"; vendors use it as a cloud-browser example |
| 6 | Write a complaint that gets fixed | Money | 34% would prefer AI contacts customer service for them (EY); "letter of complaint" |
| 7 | Get through a long form | Paperwork | "can ai fill out forms for me", "…pdf forms", "…tax forms" |
| 8 | Review a lease before signing | Paperwork | "chatgpt lease review", "chatgpt lease agreement" |
| 9 | Moving checklist + change of address | Paperwork | USPS warns about $40+ third-party sites; self-reported X story |
| 10 | Plan a trip itinerary | Bookings | "use chatgpt to plan a trip", "ai to plan travel itinerary" |
| 11 | Prepare for a doctor visit | Health | 14% of US adults used AI for health questions (Menlo 2025) |
| 12 | Organize an aging parent's care paperwork | Health | r/AgingParents thread |
| 13 | Weekly meal plan + grocery list | Family | 16% use AI for meal planning (Menlo 2025); "ai meal planner" |
| 14 | Homework help that teaches | Family | "ai to help with homework" (top suggestion) |
| 15 | Clean up your email inbox | Time | Email is the #1 AI use at 19% (Menlo 2025); "use ai to organize gmail" |
| 16 | Tailor resume + cover letter | Jobs | "ai to help with resume", "can ai fill out job applications for me" |
| 17 | Sell your stuff online | Side hustles | "use ai to sell on facebook marketplace/ebay/etsy" |
| 18 | Test a side hustle idea (and spot AI-income scams) | Side hustles | "how to use ai to make money" is the top "how to use ai to" suggestion; FTC Operation AI Comply |
| 19 | Reply to customer reviews | Small business | "ai to respond to google reviews" |
| 20 | Chase an unpaid invoice | Small business | "use ai to make invoices" |
Next wave: job interview practice, family calendar/chores, getting quotes from home services, room design ("how to use ai to decorate a room"),
finding apartments, credit report disputes, organizing photos/files, property tax appeals, car buying, school/college forms.

## 5. Site structure (built: /workspace/platform/site)
- Home: search with instant results, 3 full guides, featured (sponsor) spot, 9 categories, how-it-works, newsletter.
- /use-cases/: client-side search (`?q=` deep links) and category chips. /category/<slug>/ pages.
- /use-cases/<slug>/: problem, outcome, difficulty, time saved (labeled as an estimate), steps, a **copy-prompt button**, tools
  (labeled chat vs agent, with cost), watch-outs, self-reported examples, FAQ, sources, last-checked date, related guides, sidebar sponsor slot, newsletter.
- /newsletter/, /sponsor/ (3 tiers, pricing on request, sponsorship rules), /about/ (fact-checking method, disclosures), 404.
- Data-driven: data/use-cases.json + tools.json + categories.json + sponsors.json → scripts/build.py (stdlib Python).

## 6. SEO and traffic
- Target long-tail "how to use AI to [task]" / "can AI [task]" phrasing that autocomplete shows people actually type. One page per task, with the task in the title/H1.
- Built in: unique titles/meta, canonical, HowTo + FAQPage + BreadcrumbList JSON-LD, sitemap with lastmod, robots.txt that welcomes AI crawlers, llms.txt + llms-full.txt.
  Pages are static with about 3 KB of JS and no third-party requests.
- Get cited by AI assistants: clear, sourced, dated answers are what chatbots quote. AI referrals are small today (Semrush shows ~1% of
  Futurepedia's traffic from ChatGPT) but growing; llms.txt is cheap insurance.
- Publish 3–5 new guides a week from the backlog. Refresh "last checked" monthly, since agent features change fast.
- Distribution: answer real Reddit/forum questions (r/AgingParents, r/personalfinance, r/smallbusiness), linking only where it truly helps;
  short "watch me do it" screen recordings for YouTube Shorts/TikTok; pitch caregiver, library and senior-center newsletters; submit to AI directories (TAAFT basic listing is $49 per Digica).
- After launch: Google Search Console + Bing Webmaster (needs DNS/HTML verification).

## 7. Newsletter
"One useful AI errand a week": one task, the prompt, the watch-outs, plus one "agent news that matters for normal life" item.
Provider TBD (beehiiv, Buttondown or Kit). Wire it up by pasting the form POST URL into config.json → newsletter.form_action. The form is a disabled placeholder until then.
Growth: opt-in on every guide page; a printable "10 prompts for life admin" PDF as a lead magnet later.

## 8. Monetization (in order)
1. Sponsored featured spots (home, category, guide sidebar) and newsletter sponsorships. Slots and labels are already in the layout via data/sponsors.json.
2. Affiliate links to genuinely useful tools (always disclosed; never changes rankings).
3. Paid "done-with-you" packs (printable prompt kits for caregivers or small businesses), only after traffic proves demand.
4. B2B later: licensing the guide library to libraries, employers' benefits portals, senior services.
Guardrails: no "guaranteed AI income", debt-relief or crypto sponsors; never claim an AI replaces a lawyer or doctor (the FTC's DoNotPay order).

## 9. Specialized agents to spin up later
| Agent | Job |
|---|---|
| Research | Weekly sweep of autocomplete, Reddit and X for new task demand; verifies vendor help pages when agent features change; proposes new use cases with sources. |
| Content | Drafts new use-case JSON entries to the schema (prompt, steps, watch-outs, FAQ, sources), runs the build, flags unsourced claims. |
| Fact-check / freshness | Monthly re-check of every source link and rule (deadlines, fees, product capabilities); bumps last_checked; opens a list of stale pages. |
| SEO | Search Console monitoring, title/meta tests, internal linking, new-page briefs from queries we nearly rank for. |
| Newsletter | Turns the week's best guide into an issue, drafts it for Nik's approval, tracks open/click once the provider is live. |
| Monetization / partnerships | Builds the sponsor prospect list, drafts outreach for approval, manages data/sponsors.json and enforces sponsor rules. |
| Ops | Builds, link checks, deploys, uptime, and the domain/DNS/hosting checklist. |

## 10. Hosting and launch
Recommended: **GitHub Pages** via the included Actions workflow (free, simple, versioned). Cloudflare Pages is an equally good free
alternative with faster global caching and easy DNS if the domain is bought at Cloudflare. Netlify also works, but its free tier has build/bandwidth limits.
Status (2026-10-21): **LIVE** at https://nik-schultz.github.io/agents-on-radar/ (repo https://github.com/nik-schultz/agents-on-radar, approved by Nik). Deploy with `scripts/deploy.sh "msg"`; routine deploys are approved (README → Deploy).
Still open (older notes, the brand is now Agents on Radar; nothing purchased):
1. GitHub: log in on the box (`gh auth login`) or give the account/org to use, and approve creating the public repo `letthebot`.
2. Domain: approve buying letthebot.com (about the standard .com price at a registrar such as Cloudflare or Namecheap; confirm the price at checkout) after a quick trademark check.
3. Email: a contact inbox for hello@letthebot.com (e.g. Cloudflare Email Routing → Nik's inbox). The site already lists it.
4. Newsletter provider account (beehiiv / Buttondown / Kit) → paste the form URL.
5. Sponsor pricing: tiers say "on request" until Nik sets prices.
