# Ops changelog

## 2026-10-21 (11:30 PM CT) — Rebrand to BotsDoThat ("There's a bot for that. Here's how.")
- Nik picked **BotsDoThat**. botsdothat.com was unregistered at 11:13 PM CT; Nik is buying it himself at IONOS. We bought nothing.
- **Config:**
  - `site_name` is now BotsDoThat.
  - New tagline: "There's a bot for that. Here's how."
  - The old tagline is kept as `subtagline`.
- **Wordmark:** the header and footer logo read "BotsDoThat", with "Do" in the cyan-to-violet accent. The spinning radar dot and all radar art stay.
- **Tagline placement:**
  - under the live-feed eyebrow on the homepage (the 4 rotating headlines are unchanged);
  - in the footer, the homepage `<title>`, llms.txt and llms-full.txt;
  - in the og image ("There's a bot for that. Here's how: …");
  - in the JSON-LD Organization `slogan`. WebSite JSON-LD gets `alternateName` "Bots Do That" and a publisher.
- **Picked up the new name automatically:** titles, og:site_name, RSS titles, About, Advertise and Disclosure copy.
- **Newsletter renamed** from "the weekly radar" to "The BotsDoThat Weekly":
  - the nav button now reads "Get the weekly email";
  - the Advertise newsletter-tier copy is updated to match.
- **Docs updated:** README, PLAN, ops/launch_drafts.md (name, Product Hunt tagline, a note to swap URLs after cutover) and the affiliate research title.
- **Domain not switched yet:** `cname` is still empty and `base_url` is still https://nik-schultz.github.io/agents-on-radar/.
- **Cutover prepared:**
  - ops/domain_cutover.md: IONOS DNS records checked against GitHub's docs, plus domain verification steps and a checklist.
  - scripts/domain_cutover.sh with `check`, `apply`, `https` and `rollback` (Pages custom domain and Enforce HTTPS via gh api, config switch, deploy.sh).
  - A dry-run build on botsdothat.com gave 0 broken links, with robots.txt and the sitemap at the root.
- Committed the pending .gitignore line, which keeps research/domain_candidates.md private.

## 2026-10-21 (10:45 PM CT) — Sponsor launch prices published (approved by Nik)
- Nik approved research/sponsor_pricing.md exactly as proposed. The file is marked approved, dated Oct 21, 2026.
- /advertise/ now shows the prices:
  - newsletter slot: first 2 issues free, then $50 per issue until 1,000 subscribers, then $25 per 1,000 subscribers ($50 minimum);
  - featured tool listing: $49/month, first month free for the first 3 sponsors;
  - Run-for-less tile: $99/month, one sponsor at a time;
  - bundle of all three: $149/month.
- The page says these are launch rates that may change once traffic is measured. The honest audience wording is unchanged. The contact button ("Contact us to book a spot") still opens GitHub Issues, because no private email is set.

## 2026-10-21 (late night) — Monetization groundwork: Advertise, disclosure, paid labels, Search Console prep
- **New /advertise/ page.** Audience is described honestly ("New and growing", live since Oct 21, no visitor numbers until measured), with real content counts. It explains what we will measure: Search Console/Bing impressions and clicks, sponsor UTM clicks, newsletter stats once it sends.
  - Three options: newsletter sponsor slot, featured tool listing on matching blueprints and guides, and a sponsored tile in the homepage Run-for-less band.
  - Rules and an FAQ (with FAQPage schema). No prices: "Contact us for launch pricing" goes to `contact_email`, or to GitHub issues while that's empty.
  - /sponsor/ is now a noindex redirect to /advertise/.
- **New /disclosure/ page.** Its "Right now" line is computed from data/sponsors.json, so today it says there are no sponsors and no affiliate links.
- **Reusable labels in build.py:** `paid_label("sponsored"|"affiliate")` and `aff_link(url, text)` (rel="sponsored", labeled, links to /disclosure/). The existing sponsored slot uses the label.
- **New sponsor slots in data/sponsors.json:** `featured_tool` (on blueprints and use cases by slug or category) and `run_for_less_tile` (homepage band). Both render nothing while empty. They were tested with a dummy entry, then reverted.
- **Footer:** Advertise plus "Affiliate & sponsor disclosure". About and llms.txt link to both.
- **Search Console and Bing prep:** config.json `verification.google` and `verification.bing`. When set, every page outputs `google-site-verification` / `msvalidate.01` meta tags. validate.py rejects a pasted whole tag. Tested with dummy values, then reverted to empty.
- **Private research and drafts.** research/affiliate_programs.md is in the repo. research/sponsor_pricing.md (proposed prices for Nik to approve) and ops/launch_drafts.md (X, Reddit, Show HN and Product Hunt drafts) are gitignored, so they stay off the public repo.
- **Nothing was applied for, signed up for, posted or emailed.**

## 2026-10-21 (night) — "Run your bots for less" is now the #2 feature, plus a bot cost calculator
- Homepage: a new band right after Trending, headed "Same bot. A fraction of the bill." It has 4 tip tiles linking to guides: up to 100× cheaper with a small model (OpenAI gpt-6-luna $0.10/$0.50 vs gpt-6-astra $10/$50), 50% off with batch (Anthropic, Google, Mistral, OpenAI), cached reads at 0.1× (Anthropic), and $0 to test on Google's free tier. It also has a live cheapest-vs-top-model table per provider (from data/ai-pricing.json, checked Oct 21, 2026), a mini calculator and buttons to the hub.
- "What will my bot cost?" calculator on /run-your-bots-for-less/#calculator, in vanilla JS (app.js), server-rendered so it works without JS.
  - Inputs: a blueprint preset or your own runs (per day, weekday, week or month), a size of each run or exact tokens in and out, what the bot needs (small, mid or flagship), a batch toggle and a model picker.
  - Results: the cheapest option that fits, the priciest fit, and every model side by side.
  - Assumptions are stated on the page. Prices are the official table only. Not included: caching, tools, voice, taxes, free tiers and plans.
  - URL prefill works: ?bot=<slug>, n, unit, in, out, tier, batch=1.
- Cross-links:
  - Nav "Run for less" is a green pill with a dot.
  - Each blueprint's "What this costs to run" has a button to the calculator, prefilled.
  - The 8 run-for-less guide pages get a calculator callout.
  - Pricing news tiles on /news/ get "What this means for your bill →".
  - /ai-pricing/ links to the calculator.
- SEO:
  - Hub title is "How to reduce AI API costs: AI agent cost calculator", with new meta.
  - A 4-question FAQ, where every number is computed from the price data, with FAQPage and WebApplication JSON-LD.
  - /ai-pricing/ title is "Cheapest LLM API? AI API prices compared, with sources".
  - llms.txt has a calculator line. llms-full.txt has the formula and worked monthly examples for each preset.
- Checked at 320px with an iframe probe (no overflow). JS probe: prefill from the URL and the batch maths are correct (web page watcher, mid, batch: Groq gpt-oss-120b $0.04 vs Claude Fable 5.1 $1.27/month).
- Previews: previews/home-run-for-less.png, previews/calculator-desktop.png, previews/calculator-mobile.png.

## 2026-10-21 (evening) — LAUNCH on GitHub Pages (approved by Nik)
- Live: https://nik-schultz.github.io/agents-on-radar/ · public repo: https://github.com/nik-schultz/agents-on-radar. Pages source: GitHub Actions.
- Kept private (gitignored, untracked on main, never in the public repo): `art/incoming/*.png` (10 raw art PNGs, about 7 MB; the site uses the WebP versions in static/img), raw X API dumps (`research/*.json.txt`, `research/x_posts_full.json`), logs, .env and key files, `previews/`. A secret scan of tracked files found no tokens or keys.
- Public history is a fresh squashed `publish` branch (one commit per deploy, same tree as main) pushed to origin/main. Local main keeps its full history, which still has the PNGs in old commits, and is never pushed.
- Subpath support: `base_url` = https://nik-schultz.github.io/agents-on-radar/. Build derives origin + base path from it, so links, assets, canonicals, sitemap, RSS, llms.txt and og URLs all carry /agents-on-radar. check_links.py now checks own-domain absolute URLs and flags root links missing the base path.
- Contact links pointed to hello@agentsonradar.com, a domain we don't own. They now go to GitHub issues (`contact_url`) until a real email is set.
- Workflow now re-runs validate + check_links on the committed, locally built `site/` and publishes it unchanged (no Pillow needed in CI). New `scripts/deploy.sh "msg"` = validate → build → link check → commit → squash onto publish → push. README/PLAN updated; routine deploys approved.
- Verified live: homepage, /news/, /ai-pricing/, a guide page, /run-your-bots-for-less/, sitemap.xml, robots.txt, llms.txt, llms-full.txt, both RSS feeds, CSS, JS, og.png, WebP art and search-index.json all return 200. A crawl of every sitemap URL and every internal href/src found 123 URLs, 0 not 200. The styled 404 page works. Live screenshots render with CSS and art.

## 2026-10-21 (news update, 3:00 PM CT)
- 3 verified items added (30 total), all dated Oct 21: Claude Duet research preview (Anthropic, agent launch, major; claude.com/blog/claude-duet, plus The Verge and 9to5Mac), OpenAI Patch the Planet PHP flaws (industry, notable; OpenAI, PHP Foundation, BleepingComputer), and Claude Security continuous scanning (feature, minor; Enterprise beta).
- X numbers measured 2026-10-21 with get_posts_by_ids (raw in research/x_news_measure_2026_10_21_pm.json.txt): @claudeai Duet 12,097 likes / 800 reposts / 548,899 views; @OpenAI PHP 12,260 / 2,489 / 3,535,793; @claudeai Security 4,666 / 219 / 252,894.
- Top story is now Claude Duet. Skipped: Gemini 4 Carbon (partner early access only, no official launch), MiniMax M3.1 Flash and other smaller labs (outside the tracked companies), Anthropic's Public Benefit Report and Long-Term Benefit Trust appointment (not about bots).
- No price changes (Duet is included in Pro/Max), so ai-pricing.json is untouched. Two candidate ideas logged in BACKLOG.md.
- Checks: validate 0 errors; build 109 pages + 404; check_links 5,155 links, 0 broken internal. Not deployed (site still has no host), so nothing was redeployed.

## 2026-10-21 (later) — /news/ redesign: bento tiles, real X popularity, top story + trending
- New popularity signal. X engagement was measured on 2026-10-21 through the X API: `search_posts_all` to find posts, then `get_posts_by_ids` to re-measure (raw response in `research/x_news_measure_2026_10_21.json.txt`). 22 of 27 items have numbers. 21 come from the official company or founder post. Grok Voice 3.0 uses the most-engaged credible post about it (@ArtificialAnlys). No post was found for Claude Sonnet 5.5, the Agents API browser update, idle-sandbox billing, Gemini Skills or the Spark Task button, so those 5 have no number.
- Heat = (likes + 2 × reposts) ÷ weeks since posted, the same formula as use-case trending. New `impact` field (major / notable / minor), labelled as importance, not popularity. New `company` field for colour and monogram.
- Top story = the hottest `major` item of the last 14 days: GPT-6 for everyone (Oct 7; 23,952 likes / 1,898 reposts). Trending: DeepSeek DeepInfer open-source (Oct 20; 39,630 / 4,507), DeepSeek V4.1-Flash-1017 (Oct 17; 36,986 / 4,123), Claude Dashboards & Motion (Oct 8; 60,507 / 4,599).
- 4 verified items added (27 total): OpenAI dots (Sep 29, agent launch), Claude for Google Workspace (Oct 6), Claude Dashboards & Motion (Oct 8), DeepSeek DeepInfer (Oct 20). The Groq item now covers the Muse Spark Open release itself (Meta source, with Groq as an extra source).
- /news/ is now a bento layout. It has a Top story mega-tile with radar art, then 3 large Trending tiles with a 🔥 badge and real "39.6K likes on X" numbers. Below that are This week / Earlier tile grids, where major items span 2 columns. Each tile has a company monogram and accent colour, a category chip, the date and a one-line "For you". Filter chips: All / Trending (sorted by heat) / Model releases / Agent launches / Pricing / Features. The chips need JS; without it the bento still shows. Entry and hover animations are off under reduced motion. Works at 320px.
- The homepage "Latest in AI" strip is now a top story tile plus 4 small tiles (3 trending + newest).
- Validator now checks impact, company, and the x fields (posted_at, @author, kind, integer views). README routine now covers capturing X engagement. Fixed a pre-existing 320px overflow in the homepage newsletter box. The llms.txt price-table line now lists all 8 providers.
- Checks: validate 0 errors; internal links 0 broken (5,047 scanned). New sources return 200, except openai.com / help.openai.com / investing.com, which return 403 to scripts (bot blocking).
- Previews: previews/news-desktop.png, previews/news-top.png, previews/news-mobile.png, previews/home-news-strip.png.

## 2026-10-21 — Rotating headlines + "Latest in AI" news feed
- Hero headline now cycles through 4 headlines (the original "What AI agents / are doing / for real people" plus 3 alternates). It's pure CSS: all four sit in one grid cell, so there is no layout jump. The cycle runs 28s, 7s per headline, with fade + slide + blur using the site's cubic-bezier easing. The subhead is synced to each headline. Only version (a) is a real H1; the alternates are aria-hidden. With prefers-reduced-motion, only (a) shows. Checked at 3 lines and equal height in every state on desktop (1440) and mobile (390).
- New `data/news.json`: 23 verified items from 2026-09-21 to 2026-10-21 (14 model release, 4 pricing, 3 feature, 1 agent launch, 1 industry). Each item links to an official post or a reputable outlet. One item has X numbers (Grok Bot Team Bots: 6,404 likes / 574 reposts, measured 2026-10-21).
- The homepage has a "Latest in AI" rail (newest 8), placed after the stats. New `/news/` page with ItemList + NewsArticle schema, `/news/feed.xml` RSS, nav + footer links, sitemap, llms.txt / llms-full.txt sections.
- Price-moving news is reflected in `data/ai-pricing.json`: Meta Muse Wonder API, DeepSeek V4.1-Flash + V4-Pro (with the off-peak discount), OpenAI 12-hour prompt caching, Mistral Voxtral 3 voice-agent API. The table now covers 8 API providers.
- Validator: news items need an id, a valid date, a category from the list, a headline, an explainer, and an https source. X blocks need real integers + measured_at. It warns if the newest item is more than 3 days old. README documents the daily news routine.
- Checks: validate 0 errors; internal links 0 broken. External links: not-200 results only from bot-blocked sites (openai.com 403, Android Authority 403) and older FTC/HN links that were already in the report.
- Previews: previews/home-top.png, previews/home-mobile-top.png, previews/news-desktop.png.

## 2026-10-21 (refocus on agentic bots + "Run your bots for less", 9:14–9:35 AM CT)
Asked by Nik: focus the site on agentic bots, keep the design, animation, art and layout exactly as they are, and make the only money angle spending less ON AI services. Not deployed.

Archived (moved to `data/archive/`, not deleted): 11 everyday money-saving guides (contest-a-traffic-ticket, ask-for-a-lower-bill, dispute-a-credit-report-error, get-a-refund-on-an-accidental-charge, deal-hunting-that-knows-what-you-own, find-money-leaking-from-your-inbox, track-prices-across-stores-with-universal-cart, hidden-subscription-fee-finder, replace-a-paid-app-with-a-shortcut, question-a-medical-bill, cancel-a-subscription), the Money category and the bill-and-subscription-watchdog blueprint. The hospital-bill backlog guide was stopped, and the other money items in BACKLOG.md are marked dropped.
Reframed (agentic, no savings angle): cancel-a-subscription-by-phone → `make-a-customer-service-call`; mail-to-bill-pay-with-anomaly-alerts → `sort-scanned-paper-mail-with-alerts`; deal-desk-inbox-watcher → `time-sensitive-inbox-watcher`; plus the web-page watcher, airline-change alerts, single-use card, delayed-flight rebooking, trip, side-hustle and complaint guides. Blueprint price-drop-watcher → `web-page-watcher`. Travel Day Guardian lost its refund wording.
Added: 10 sourced agentic guides (phone booking, newsletter report, prescription-ready alert, used-car research, contractors, web forms, roadside help abroad, voice hand-off while driving, team of agents, shared Apple account) and the `phone-call-bot` blueprint.
New "Run your bots for less" section, in the old Money slot with its art (`cat-money`), so the 8-tile bento is unchanged:
- 8 guides (model routing, free tiers, plan vs pay-per-use, caching + batch, local/open models, schedules/on-demand, short prompts, spend limits), sourced from official docs plus one X post.
- `/run-your-bots-for-less/` hub and `/ai-pricing/` table, built from `data/ai-pricing.json`: 15 API rows across 6 providers (OpenAI, Anthropic, Google, xAI, Groq, Mistral) plus 7 plan rows. Each row has its official source and was checked 2026-10-21. Left out because they couldn't be verified: ChatGPT Go/Plus/Pro, Google AI plans in USD, SuperGrok.
- Every blueprint now has a "What this costs to run" note, calculated from the table using stated token assumptions (blueprint `cost` field). The phone bot gets a per-minute voice estimate.
- `validate.py` now checks the price file and warns if it is more than 7 days old. The weekly refresh is documented in the README.
- Added to the nav, the footer, the sitemap, llms.txt and llms-full.txt.
Copy: new homepage headline "What AI agents [are doing] for real people." (same rotator animation, now with plain verbs), with the lead "And build your own…". Also new title, meta description, tagline and description, search placeholder, explainer, hub FAQ and og.png text. Broken explainer links to archived guides were fixed.
Checks: validate 75 use cases / 12 blueprints / 0 errors. Build 106 indexed pages + 404. Internal links 4,717 scanned / 0 broken. External links 117 OK / 10 not-200; these are the same bot-blocked or known pages as earlier, and none are from the new pricing sources.
Previews: `previews/home-top.png` and `previews/home-mobile-top.png`, taken with headless Chrome plus `--use-gl=swiftshader --enable-unsafe-swiftshader`. Without those flags the masked hero radar art doesn't render.

## 2026-10-21 (daily QA run, 7:00 AM CT)
Status: site is still **not deployed** (no GitHub login on the box, no domain), so QA ran against the local build in `site/` and nothing was redeployed.

Checks
- validate: 68 use cases, 12 blueprints, 0 errors. Build: 97 indexed pages + 404.
- Internal links: 3,987 scanned, 0 broken. All images on pages exist on disk and every `<img>` has alt text. Every copy button points at an element that exists. The search index covers every guide and blueprint.
- Outbound links (119): all reachable. Three FTC pages return 404/403 to curl from the box (Akamai bot block) but load fine through a normal fetch; claude.ai, help.openai.com and openai.com return bot-check 403s to scripts, and the OpenAI dots page loads fine through a normal fetch.
- JavaScript passes a syntax check. Console errors and real-device rendering were not checked in a browser this run (static review only).

Bugs fixed: none found.

Improvement for visitors
- New guide from the backlog: `write-a-letter-of-recommendation` (work). Plain steps, a fill-in prompt that tells the AI not to invent achievements, watch-outs about only signing what's true and keeping private details out of the chat, and two FAQ answers. No stats or time-saved estimates.

## 2026-10-20 (weekly SEO and AI-chatbot run, 9:06 AM CT)
Status: site is still **not deployed** (no GitHub login on the box, no domain), so nothing could be redeployed, there is no Search Console or analytics data, and no AI assistant can cite the site yet. All changes are in the local build in `site/` and ship with the first deploy.

Changes
- Titles: the " · Agents on Radar" suffix is now dropped when it would push a `<title>` past about 62 characters, so Google shows the guide's own words instead of a cut-off brand. 40+ pages were over before.
- Meta descriptions: use-case pages now combine the summary and the result, cut at a word boundary under 155 characters (several were 64 characters, the homepage was 249). Blueprint pages and the blueprints index got the same treatment; homepage uses a new `meta_description` in `config.json`.
- Every use-case page now has a "Questions people ask" section and FAQPage schema (was 20 of 60). Pages without hand-written FAQs get three answers built only from the page's own data: which tools can do it, how hard it is, and the top watch-out. This gives AI assistants short, quotable answers.
- New page `/ai-agent-examples/`: all 62 guides on one page grouped by part of life, answer-first intro, ItemList + FAQPage + breadcrumb schema. Targets autocomplete "ai agents examples" and "ai agent for everyday life/use". Linked from the homepage, the explainer, the footer, llms.txt and the sitemap.
- Two new sourced guides from the backlog: `dispute-a-credit-report-error` (FTC and AnnualCreditReport.com as sources; 30-day investigation, free disputes, weekly free reports) and `write-a-resignation-letter`.
- Research: fresh Google autocomplete pulls added to BACKLOG.md (search suggestions, not volume numbers).

Checks: validate 0 errors, 62 use cases; build 91 indexed pages + 404; check_links 3,724 links, 0 broken internal; all JSON-LD parses. Page weight is small (CSS 32 KB, JS 6 KB, largest image 29 KB), no speed work needed.

## 2026-10-20 (daily QA run, 7:04 AM CT)
Status: site is still **not deployed** (no GitHub login or remote yet, see PLAN.md section 10), so QA ran against the local build in `site/`. Nothing was redeployed.

Checks
- Build: OK, 34 indexed pages + 404.
- Internal links, anchors, assets: 0 broken across 35 HTML pages. Every page has `lang`, a viewport tag and exactly one `h1`. No images on the site yet, so no broken images.
- Outbound links (48): all reachable. ftc.gov (2 links) and help.openai.com (2 links) refuse curl but loaded fine through a normal fetch; claude.ai returns a bot-check 403 to scripts, which is expected.
- JavaScript: `static/app.js` passes a syntax check. Console errors and real-device rendering were not checked in a browser this run (static review only).

Bugs fixed
- Homepage instant search missed obvious matches because it only looked at title, problem and outcome, and didn't strip punctuation. The search box's own example, "insurance denied", returned no results, and so did "vacation", "apartment", "refund", "eBay" and "Gmail". It now uses the same text (including tags and category name) and the same normalization as the all-guides page. The search index gained a `search` field.
- Small phones (320px wide): guide cards had a 290px minimum width inside a 280px content area, which could cause sideways scrolling. Grids now use `min(…, 100%)`, and the newsletter email field no longer forces 200px.
- Homepage search now handles a failed index download gracefully instead of silently doing nothing.

Improvement for visitors
- Homepage search now tells people (and screen readers, via a polite live region) how many guides match, says when only the first 6 are shown, and a no-match message links straight to the all-guides search with their words already filled in.
- Added `BACKLOG.md` with 18 candidate guides taken from the autocomplete research, so future runs have a queue of high-intent topics.
