# Ops changelog

## 2026-10-23 (12:25 PM CT) — Unsourced "editor's estimate" time-saved lines replaced or removed
- 19 use cases had a time-saved line labeled "by our editor's estimate" with no source (rendered in the FAQ + FAQPage JSON-LD).
- Sourced (5), each phrased as the source states it, linked, checked 2026-10-23:
  - appeal-a-health-insurance-denial: 7 vs 23 min per appeal letter, 7 physicians (ASTRO 2026 abstract, UCLA).
  - clean-up-your-email-inbox: 2 fewer hours/week on email, 7,137 workers at 66 firms (Dillon et al., AER: Insights).
  - reply-to-customer-reviews: 10 min to ~2 min per Google review at Jackson Hewitt (Sprinklr case study, vendor).
  - plan-a-trip-itinerary: nearly 7 hours saved, self-reported (Qlik/Censuswide survey, July 2025).
  - sell-your-stuff-online: listing time down 48% avg in beta (Poshmark via Digital Commerce 360).
- Removed (14): no credible source states a figure for that task. Includes fill-out-a-long-form (the CHItaly 2025 study covers technical MICS forms, which aren't comparable).
- Schema: `time_saved` is optional; when present it must be `{text, source, url (https), checked}`. The FAQ renders it as "How much time can it save?" with a source link.
- validate.py: rejects string or unsourced time_saved, any "editor's estimate" text in use-case data, and an editor label in build.py's time-saved template. Also checks blueprint time_saved.
- Not changed, flagged for Nik: blueprint `setup_time` values "(editor's estimate)" (12) and the run-for-less "token counts are our editor's estimates" note. These are setup and token estimates, not time-saved claims.

## 2026-10-23 (weekly monetization review, 10:10 AM CT)
- No active sponsors or affiliate links; data/sponsors.json is empty and /disclosure/ says so. Live /advertise/ rate card matches the approved Oct 21 pricing.
- No traffic or subscriber data yet: Search Console and Bing verification are still unset in config.json, and there is no analytics. Too early to start outreach or affiliate links; no changes made.

## 2026-10-23 (daily QA run, 7:20 AM CT)
- **Status:** live and healthy. https://botsdothat.com/ returned 200 on every page checked: home, /use-cases/ and 3 guides, /blueprints/ and 2 blueprints, /news/, /ai-pricing/, /run-your-bots-for-less/ (with ?bot= prefill), /trending/, /newsletter/ and the Oct 22 issue, /advertise/, robots.txt, sitemap.xml, feed.xml, /news/feed.xml, llms.txt, /assets/app.js, /assets/style.css and /assets/search-index.json. /nope-xyz-404/ returns the 404 page. TLS cert CN=botsdothat.com is valid until Jan 20, 2027. https://www.botsdothat.com/ 301s to the apex.
- **Checks:**
  - validate: 0 errors. build: OK (115 pages + 404 after today's guide). Internal links: 0 broken (5,762 scanned).
  - External links: 228 unique, 19 not-200 to the HEAD check. Expected bot blocks: claude.ai, help.openai.com, openai.com (403); ftc.gov and consumer.ftc.gov (404 to curl; the FTC job-scams page loads fine through a normal fetch); Android Authority (403). New this run: chatgpt.com/pricing 403 to HEAD. It and these returned 200 to a browser-UA GET: chatgpt.com/pricing, two support.google.com pages, ahrq.gov, news.ycombinator.com (405 to HEAD) and a google.com/search source link (URLError to HEAD). Nothing actually broken.
  - Static checks (all 117 HTML files): every img has alt text and an existing file (69 imgs). Every data-copy button points at an existing id. The search index covers all 81 use cases and 12 blueprints. All JSON-LD blocks parse (309 before the new guide). app.js and all inline JS pass `node --check` (the 2 flags were the calculator's `application/json` data blocks, which parse as JSON). Every page has a width=device-width viewport, and there are no fixed widths over 320px.
  - Headless Chrome (own instance, throwaway temp profile, driven over CDP from Shell; Node 20 needs `--experimental-websocket` for the /workspace/qa scripts):
    - Console: 0 console errors and 0 JS exceptions on 13 live pages at 320px and 1280px. The only network error was the intended 404 test page.
    - Function tests: /use-cases/?q=resignation filters to 1 result, homepage instant search returns results, the Copy button reaches "Copied ✓" (also on the new guide), and the calculator renders with the ?bot= prefill.
    - Overflow: a full 320px scan of all 115 pages, run locally, flagged only the homepage hero radar art, which is clipped on purpose (page scrollWidth stays 320).
- **Bugs fixed:** none found.
- **Improvement for visitors:** new guide **Add calendar events and reminders just by asking your bot** (https://botsdothat.com/use-cases/add-events-and-reminders-by-asking-your-bot/, family category, Easy).
  - What it covers: pick Grok Bot (phone Calendar/Reminders/Contacts, rolling out Oct 22) or Gemini (Google Calendar + Google Tasks), allow only the apps you need, ask in plain words or paste a text, read back what it added, and use Undo. Includes the Gemini Maps saved places + Calendar tip. Copy-paste prompt included.
  - Watch-outs, each sourced: per-app Allow buttons (Digital Trends, TeslaNorth); Gemini can hallucinate, default calendar, guest emails can't be undone (Gemini Apps Help, calendar events); Gemini can bulk-change Google Tasks without confirmation (Gemini Apps Help, tasks & workflows); availability on both platforms still unclear (TeslaNorth).
  - Also: a 3-question FAQ, no stats or time-saved estimates, and `popularity: null`. Backlog item marked `[x]`.
- **Deploy commits:** publish 1bb22fa (guide; main beaaca5), then 8a7b15a (this log). GitHub Actions run succeeded. The news routine's staged BACKLOG line went out in the same commit.
- **Not checked:** Reddit (blocked from the box), real-device or Safari/iOS rendering (Chrome emulation only), Lighthouse/performance scores, and the http→https redirect (outbound port 80 is blocked from the box).

## 2026-10-23 (news update, 6:30 AM CT)
- **Added 4 items** (all opened at the source, all Oct 22, all notable): Claude apps switch to auto mode by default next week on Pro/Max/Team (Anthropic, @claudeai); Grok Bot can use the phone's Calendar, Reminders, Contacts and more (Digital Trends + TeslaNorth, @bot); Grok Bot signs in with 1Password without seeing passwords (1Password partner page + 1Password for Agents blog, @bot); Gemini Personal Intelligence now uses Google Maps saved places with Calendar (9to5Google, @GeminiApp).
- **X refresh:** re-measured all 33 tracked posts (get_posts_by_ids, 2026-10-23 AM; raw response kept locally in research/). Top story is still Claude Duet; trending is now Claude auto mode, DeepSeek DeepInfer and Grok Bot phone apps.
- No price changes, so the AI pricing table is unchanged. No major releases this run. Skipped: Claude on Google Cloud GA (enterprise), Anthropic formal-verification research post, Google Gemini API CLI / Agent Compute Engine (developer previews), MiniMax M3.1-Flash and iFlytek Spark X2.6 (outside tracked labs), Arena rumors about Kimi K3.1 / Qwen 4 (unconfirmed).
- BACKLOG: added a phone calendar-and-reminders bot guide idea.
- Checks: validate 0 errors, build 114 pages + 404, 0 broken internal links.

## 2026-10-22 (news update, 2:30 PM CT)
- **Added 4 items** (all opened at the source): Anthropic donates the Agent Skills standard to the Agentic AI Foundation (Oct 22, notable, no official X post found so no `x` block); OpenAI Decisions API generally available (Oct 22, minor, @OpenAIDevs); Canva Craft, Canva's first image model (Oct 22, notable, TechCrunch + @canva); Gemini Personal Intelligence on Android Auto (Oct 20, notable, Google blog + @Google). New company `Canva` added to `NEWS_CO` in build.py.
- **X refresh:** re-measured all 29 tracked posts (get_posts_by_ids, 2026-10-22 PM; raw response kept locally in research/). Top story is still Claude Duet; trending is DeepSeek DeepInfer, the PHP-flaws item and DeepSeek V4.1 Flash.
- No price changes from these items, so the AI pricing table is unchanged. No major releases this run. Skipped: xAI partner network (enterprise-only), Hugging Face Carbon-X DNA model (research), Mistral/NVIDIA engineering tie-up (no consumer impact yet).
- BACKLOG: added a hands-free car assistant guide idea.
- Checks: validate 0 errors, build 114 pages + 404, 0 broken internal links.

## 2026-10-22 (weekly newsletter routine, 9:10 AM CT) — BotsDoThat Weekly #1 published on the web
- **New:** newsletter web archive. `data/newsletter.json` holds issues; build.py renders `/newsletter/` (signup + past issues), one page per issue at `/newsletter/<date>/` (Article + Breadcrumb JSON-LD, in the sitemap) and `/newsletter/feed.xml`. Item outcomes, prompts and sources are pulled from data/use-cases.json, so they stay in sync with the guides. Empty `sponsor` renders a house ad pointing to /advertise/.
- **Issue #1 (Oct 22): "4 jobs you can hand to an AI this week":** research a used car from its listing link, line up contractors for a home project, send a long video or thread to your bot, set AI spend limits and alerts. New on the site: Fill out a job application faster. Watch-out: Meta paused Muse chat sharing (The Verge). Sponsor: none booked, house ad.
- **Not emailed.** No email provider is wired yet (`config.newsletter.form_action` is empty, signup form still disabled) and Nik hasn't approved sending. `sent_on` stays null.
- /newsletter/ lead copy now matches the routine's format (3 to 5 jobs with prompts, one new guide, one thing that went wrong).

## 2026-10-22 (daily QA run, 7:20 AM CT)
- **Status:** live and healthy. https://botsdothat.com/ returned 200 on every page checked: home, /use-cases/ and 3 guides, /blueprints/ and 2 blueprints, /news/, /ai-pricing/, /run-your-bots-for-less/ (with ?bot= prefill), /trending/, /advertise/, robots.txt, sitemap.xml, feed.xml, app.js and the search index. /nope-xyz/ returns the 404 page. TLS cert CN=botsdothat.com is valid until Jan 20, 2027. https://www.botsdothat.com/ and the old github.io deep link (/agents-on-radar/news/) both 301 to botsdothat.com. Outbound port 80 is blocked from the box, so the http→https redirect was confirmed through a normal web fetch instead.
- **Checks:**
  - validate: 0 errors, 0 warnings. build: OK. Internal links: 0 broken (5,539 scanned).
  - External links: 203 unique. The not-200 results were the expected bot blocks: claude.ai, help.openai.com and openai.com (403); the two ftc.gov pages (404 to curl), which load fine through a normal fetch; and Android Authority (403 Cloudflare challenge), which also loads fine through a normal fetch. These four gave errors to the HEAD check but returned 200 to a browser-UA GET: gemini.google/subscriptions, news.ycombinator.com (405 to HEAD), two support.google.com pages and ahrq.gov.
  - Static checks (all 113 HTML files): every img has alt text and an existing file (69 imgs). Every data-copy button points at an existing id. The search index covers all 78 use cases and 12 blueprints. All 298 JSON-LD blocks parse. app.js and the inline scripts pass `node --check`. Every page has a width=device-width viewport. There are no inline or CSS fixed widths over 320px.
  - Headless Chrome (already installed, driven over CDP from Shell):
    - Console: 0 console errors and 0 JS exceptions on 13 live pages at 320px and 1280px.
    - Function tests: /use-cases/?q=resignation filters to 1 result, homepage instant search returns results, the Copy button reaches "Copied ✓", and the calculator renders with the ?bot= prefill.
    - Overflow: a full 320px scan of all 112 pages, run locally, found the bug below. After the fix, the only flag left was the homepage hero radar art, which is clipped on purpose (page scrollWidth stays 320).
- **Bugs fixed:**
  - Horizontal overflow at 320px on blueprint pages: job-match-scout was 389px wide and receipt-matcher 327px, so text was cut off on the right because body has overflow-x:hidden.
    - Cause: `.uc-grid` items kept `min-width:auto`, so the wide "What this costs to run" table and a long email address in a step forced the column wider than the screen.
    - Fix in static/style.css: `.uc-grid` now uses `grid-template-columns:minmax(0,1fr)` and `.uc-grid>*{min-width:0;overflow-wrap:anywhere}`. The table now scrolls inside its `.table-wrap` as intended.
    - Deployed and verified live: both pages are 320px wide and the CSS is served.
- **Improvement for visitors:** new guide **Fill out a job application faster with an agent** (https://botsdothat.com/use-cases/fill-out-a-job-application-faster/, work category).
  - What it covers: write a fact sheet once, have a browser agent fill in the employer's careers page, sign in yourself, have the agent list anything it can't answer instead of guessing, and stop before Submit. Copy-paste prompt included.
  - Watch-outs, each sourced:
    - OpenAI Help "Using cloud browser in ChatGPT": secure sign-in form, confirmation before consequential actions, some sites block the agent, check results.
    - FTC "Job Scams": honest employers never ask you to pay to get a job, plus the fake-check scam.
    - LinkedIn User Agreement §8.2: bans bots and unauthorized automated methods, so apply on the employer's own site.
  - Also: a 3-question FAQ, no stats and no time-saved estimate, and `popularity: null`.
  - Cross-linked from the Job Match Scout blueprint. Backlog item marked `[x]`.
- **Deploy commits:** publish b854687 (guide), then 0b02d66 (overflow fix). Both GitHub Actions runs succeeded. The news routine deployed 1411bd7 between them, with no conflict.
- **Not checked:** Reddit (blocked from the box), real-device or Safari/iOS rendering (Chrome emulation only), and Lighthouse/performance scores.

## 2026-10-22 (news update, 7:10 AM CT)
- Added 2 verified items: **Recursive releases Flint**, a free laptop-sized coding model (Oct 21, TechCrunch; notable; new company "Recursive" added to `NEWS_CO` in build.py) and **Meta pauses Muse chat sharing** after 6,800+ share links were found in public web records (Oct 20, The Verge + Ars Technica; notable; no credible high-engagement X post, so no `x` block).
- X numbers re-measured 2026-10-22 for 13 recent posts (raw in research/x_news_measure_2026_10_22_am.json.txt, applied by research/news_x_2026_10_22.py). @RichardSocher Flint 7,127 likes / 759 reposts / 2,836,719 views; @claudeai Duet 48,646 / 3,710 / 7,089,059.
- Google Cloud item now uses @OpenAI's own announcement (4,242 likes / 329 reposts / 368,443 views) instead of @googlecloud, since it is the most-engaged official post.
- Checked with nothing new to add: OpenAI API changelog (Oct 21 service-tier setting is admin-only), Gemini API changelog, xAI release notes, Anthropic newsroom. Skipped smaller or unverified items (Mercury 3, Nemotron 3.5 Super VL, Hugging Face Carbon-X, an aggregator calling July's Kimi K3 new). No price-table changes.
- BACKLOG: logged a laptop coding-helper guide idea and a share-link watch-out.

## 2026-10-21 (11:40 PM CT) — Live on https://botsdothat.com/
- **Domain and DNS:** Nik bought botsdothat.com on Cloudflare. Records are DNS-only: 4 A and 4 AAAA records to GitHub Pages, www as a CNAME to nik-schultz.github.io, and the GitHub challenge TXT. The domain is verified on his GitHub account.
- **Cutover:** `scripts/domain_cutover.sh apply` set the Pages custom domain, set `cname` and `base_url=https://botsdothat.com/`, and deployed with deploy.sh. The certificate was already approved (Let's Encrypt, botsdothat.com + www, expires 2027-01-19), so `https` turned on Enforce HTTPS right away.
- **Verified:**
  - https://botsdothat.com/ returns 200.
  - http (apex and www) returns 301 to https://botsdothat.com/.
  - https://www.botsdothat.com/ redirects to the apex and returns 200.
  - Old github.io URLs (including deep links like /agents-on-radar/advertise/) redirect to the same path on botsdothat.com and return 200.
  - /robots.txt and /sitemap.xml are served at the root, with sitemap URLs on the new domain.
  - Canonical, og:url, og:image, JSON-LD, RSS and llms.txt all use https://botsdothat.com/.
- **Docs:** launch-draft links now point to botsdothat.com, and README, PLAN and the cutover runbook show the live domain.

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
