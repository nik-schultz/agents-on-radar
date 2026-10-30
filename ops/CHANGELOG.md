# Ops changelog

## 2026-10-30 (News update, PM, ~1:40 PM MT)
- Added 7 items: `openai-teen-violence-safeguards` (Oct 30, notable, feature; OpenAI, Reuters via US News; no x block, no OpenAI post found), `zest-text-restaurant-concierge` (Oct 30, notable, agent launch; TechCrunch; no x block, only low-engagement aggregators), `doordash-amazon-agent-orders-tiny` (Oct 30, notable, industry; TechCrunch, Fortune; coverage @TechCrunch 38 likes / 7 reposts / 20,252 views), `gemini-api-computer-use-ga` (Oct 30, minor, feature; Gemini API release notes + Computer Use guide; no x block), `openai-robots-txt-ai-training-signal` (Oct 30, minor, industry; OpenAI, Google Search Central, Unite.AI; no x block), `pika-h3-flex-open-weights` (Oct 29, notable, model release; Pika blog, Business Wire, Hugging Face; @pika_labs 1,539 / 281 / 808,632), `elevenlabs-sfx-v3` (Oct 29, notable, model release; ElevenLabs blog; @ElevenLabs 477 / 115 / 995,333). All measured Oct 30 PM.
- New NEWS_CO entries: Zest, DoorDash, ElevenLabs, Pika. Top story unchanged (Gemini 4 Carbon); trending: ChatGPT Pro limits, Block Dessa, Claude for Legal.
- Refreshed X numbers on 54 existing items (items from Oct 14 on); Gemini 4 Carbon @sundarpichai now 33,990 likes / 2,742 reposts / 6.76M views; ChatGPT Pro limits @thsottiaux 37,637 / 2,616 / 5.55M. Raw response in research/x_news_measure_2026_10_30_pm.json.txt (local only), applied with research/news_x_2026_10_30_pm.py.
- Pricing: no table change (no official API token price changes found; Gemini Computer Use is billed as regular tokens).
- Skipped: OpenAI Private Intelligence promo post (product announced Sep 29 at DevDay, not new), OpenAI agent-monitoring research (safety research, same as AM skip), GPT-6.2 / Grok 4.8 leaks (rumors), Claude Enterprise Smart Reports and pooled budgets, Claude API 128 MB request limit, Microsoft Copilot harness in Foundry (enterprise/developer), Tencent WorkBuddy remote control (China-only), Cartesia Managed Agents, Mischief 1, Nace Drex Max (developer-only or single-source), CrowdStrike agent intrusion report and Alphabet/Reddit stock drop (security/markets). Nothing new from Anthropic models, xAI, Mistral, DeepSeek, Groq or Qwen since AM; Grok Bot changelog still v0.78.1.
- BACKLOG: Zest as a possible extra tool for `restaurant-reservations-by-agent`; "finish checkout yourself" watch-out for shopping guides; SFX v3 home-video sound guide idea; robots.txt AI-training opt-out note for the site.
- Checks: validate 0 errors (112 use cases); build 153 indexed pages + 404; check_links 11,734 links, 0 broken internal.

## 2026-10-30 (midday trending watch)
- New use case `catch-calendar-clashes-hiding-in-your-email` (WIRED six-agent test, Fast Company, r/AI_Agents, Fieldwork, X). Extra non-X sources on `proactive-next-moves-bot` (HN 50292727) and `hand-your-most-hated-chores-to-a-personal-agent` (WIRED). Refreshed 48 X posts. 112 use cases, X 17% of source links (73/419).
- Checks: validate 0 errors; build 153 indexed pages + 404; check_links 11,718 links, 0 broken internal. No site mentions or complaints found.

## 2026-10-30 (SEO agent: newsletter conversion + SEO quick wins, Nik's growth request)
Newsletter (Kit form 10088120, unchanged; no test signup submitted)
- Signup box now also at the end of /use-cases/, /blueprints/, /ai-pricing/, /run-your-bots-for-less/ and /about/ (`NL_END_PATHS`). These were the only content hubs without one.
- "Forward it" line under every form now links the shareable /newsletter/ page (was /#subscribe).
- /newsletter/ landing page: title "Free AI agents newsletter: the BotsDoThat Weekly", visible breadcrumb, "What's in each issue" (only what issues really contain), "Read the latest issue" button, 5-question FAQ (free, weekly, no coding, unsubscribe, what happens to your email) with FAQPage + BreadcrumbList JSON-LD.
- Audit finding: no issue has been emailed yet (both sent_on null); new subscribers get only Kit's confirmation. Flagged in ops/growth-plan.md as the main newsletter blocker (send needs Grok CEO + Nik approval).
SEO quick wins (GSC Oct 22-26: cost and no-code queries at positions 61-98, /news/ 33 impressions at 8.2)
- Cost guide: title "How much does it cost to run an AI agent per month?" (Google autocomplete "ai agent cost per month", "how much does an ai agent cost per month"), description rewritten to 147 chars so it no longer truncates, new "AI agent cost at a glance" box (software, pay-per-use range from the existing table, voice per-minute, model choice) with jump links to the calculator and no-code guide. No new numbers; all values come from the page's existing computed data.
- No-code guide: title "How to build an AI agent without coding in 7 steps", new description.
- /news/: description reworded so the key part shows; new "New to AI agents?" line linking the explainer, no-code guide, cost guide and /newsletter/. Title unchanged (it already ranks ~8).
Plan and drafts
- New ops/growth-plan.md: newsletter audit, top 5 actions, weekly X content system + 5 X drafts for BotsDoThat - Marketing / Nik, 4-week SEO page plan from real autocomplete gaps, and free listing/backlink drafts (E-G). Nothing posted, emailed or submitted.
- Homepage, /advertise/, config.json sponsor_checkout and the @botsdothat account untouched.
- Checks: validate 0 errors (111 use cases, 12 blueprints); build 152 indexed pages + 404; check_links 11,631 links, 0 broken internal. Headless Chromium at 390px: no horizontal scroll, no JS errors on /newsletter/ and the cost guide.
- Deploy: scripts/deploy.sh at 8:38 AM CT (no other deploy running; origin/main was 34f53ab). main edeb45c / publish 36dc4e3; GitHub Actions run 41064875899 succeeded (finished 8:42 AM CT). Live checks 8:42 AM CT, all 200 with new titles and a signup form: /newsletter/, cost guide, no-code guide, /news/, /use-cases/, /blueprints/, /ai-pricing/, /run-your-bots-for-less/, /about/. This deploy line is committed with the next deploy.

## 2026-10-30 (daily QA, 7:00 AM CT)
Checks
- Live site: up. Homepage, /news/, /ai-pricing/, /use-cases/, /advertise/ and /newsletter/ all returned 200.
- Internal links, anchors, assets: 0 broken (check_links); validate 0 errors.
- Outbound links (617 unique, HEAD then GET with a browser user agent): no real breakages. Re-checked the flagged ones slowly: support.google.com (429 rate limit) and the Hacker News thread load fine (200). The rest are the usual bot blocks: openai.com, help.openai.com, chatgpt.com and claude.ai (403), ftc.gov / consumer.ftc.gov (404 to this box for every URL, same as Oct 29), meta.com help (400 to scripts), and Cloudflare challenges at Oracle's blog, Business Wire, Forbes, investing.com, NAIC, RentCafe, Retail Dive and StreetInsider (new since the Oct 29 PM news run; it's a "Just a moment..." challenge page, not a 404).
- Real browser check (headless Chromium, local build): no horizontal scroll at 320px or 1280px on 10 key pages (incl. the new iCloud Mail and IFTTT guides), no broken images, no JS errors (only the Cloudflare analytics beacon refusing localhost, expected). Copy-prompt button copies and shows "Copied ✓". Homepage instant search, `?q=` links, all-guides filter and the index-failure fallback all work. Live site at 390px: instant search returns results, no console errors.

Bugs fixed
- None found.

Improvement for visitors
- New guide `plan-your-day-from-your-calendar-and-to-do-list` (family, Easy), from the BACKLOG autocomplete item "ai to plan my day": an assistant connected to your calendar and task list proposes a time-blocked plan, you approve it, then it adds the blocks. Sources: r/todoist (Mar 24, 2026, Claude + Todoist + Google Calendar daily planner), r/ChatGPT (Jul 2025, weekly plan), Gemini Apps Help (Calendar, Google Tasks, Daily Brief), Claude Help Center (Google Workspace connectors) and Google search suggestions. Watch-out notes that Claude's own pages differ on whether its Calendar connector can add events. Now 111 use cases; X is 72 of 412 source links (17%). BACKLOG item marked done; `ops/source-mix.md` updated.
- Deploy: main c26aaa2 / publish 34f53ab; GitHub Actions run 41053581941 succeeded. New guide page returns 200 live. This deploy line is committed with the next deploy.

## 2026-10-30 (News update, AM, ~6:40 AM CT)
- Added 3 items (all dated Oct 29): `chatgpt-pro-usage-doubled` (notable, pricing; ChatGPT release notes, BleepingComputer, The Decoder; X @thsottiaux 36,588 likes / 2,552 reposts / 4,778,683 views, now Trending #1), `google-jules-winding-down` (notable, industry; @julesagent post, The Verge; @julesagent 1,131 / 62 / 154,851), `meta-style-sketch-ai-closet` (minor, feature; TechCrunch; coverage @MattNavarra 98 / 7 / 19,139). All measured Oct 30 AM.
- Extra sources on `gemini-edit-files-in-chat`: The Verge, 9to5Google. No new NEWS_CO entries. Top story unchanged (Gemini 4 Carbon); trending: ChatGPT Pro limits, Block Dessa, Claude for Legal.
- Refreshed X numbers on 51 existing items (items from Oct 14 on); Gemini 4 Carbon @sundarpichai now 33,732 likes / 6.68M views, Claude for Legal 31,438 / 7.69M, OpenAI API credits 9,019 / 1.95M, Mistral Large 4 5,690 / 627K. Raw response in research/x_news_measure_2026_10_30_am.json.txt (local only), applied with research/news_x_2026_10_30_am.py (now writes indent=2 to match the repo).
- Pricing: no table change (the Pro change is plan allowance, not API token prices; no new API prices found).
- Skipped: OpenAI misalignment monitoring and Anthropic self-assessment (safety research, consistent with the Oct 29 skip), Le Chonk "training camp" post (same release as Mistral Large 4), Claude Usage & Cost Analytics API and GitHub Copilot code review updates (developer-only), xAI custom moderation (covered by grok-api-guidelines), Meta x Ohio State Muse research, WIRED Accenture/Pentagon story (disputed), DeepSeek/Moonshot distillation report (unconfirmed), Canada-Cohere stake (not verified from a primary source), Alphabet stock, Rivian/VW assistant licensing. No new models from xAI, Anthropic, DeepSeek, Groq or Mistral since the last run; Grok Bot changelog still v0.78.1.
- BACKLOG: Style Sketch trip-outfit planning as a watch item for a "plan outfits / pack for a trip" entry once it's outside SEA; Jules users moving to Antigravity noted.
- Checks: validate 0 errors (110 use cases); build 151 indexed pages + 404; check_links 11,532 links, 0 broken internal.
- Deploy: main e0265a8 / publish d0e09bc; GitHub Actions run 41049255882 succeeded in 23s (6:36 AM CT). Live /news/ shows all 3 new items, with the ChatGPT Pro item at Trending #1. This deploy line is committed with the next deploy.

## 2026-10-29 (News update, PM, ~2:30 PM CT)
- Added 8 items: `mistral-large-4-open-weights` (Oct 29, notable, model release; Mistral news, TechCrunch, Hugging Face; X @MistralAI 4,076 likes / 532 reposts / 313,778 views), `claude-mobile-carplay-multi-account` (Oct 29, notable; @claudeai 4,218 / 151 / 213,017; Crypto Briefing), `gemini-edit-files-in-chat` (Oct 29, notable; Google blog; @GeminiApp 1,527 / 146 / 75,771), `amazon-alexa-for-shopping-100-actions` (Oct 29, notable; aboutamazon.com, TechCrunch; @amazonnews 13 / 2 / 1,670), `openai-model-spec-five-values` (Oct 29, notable, industry; OpenAI, model-spec.openai.com, Reuters; no x block: no OpenAI post found, only low-engagement aggregators), `granola-voice-typing` (Oct 29, minor; TechCrunch; @meetgranola 1,128 / 46 / 103,309), `gemini-shared-avatars` (Oct 29, minor; @GeminiApp 73 / 5 / 7,099; Gemini Help), `grok-bot-shopping-subscriptions` (Oct 27 changelog date, notable; x.ai/changelog/bot, The Tech Signal; @ericzakariasson 1,152 / 38 / 124,621). All measured Oct 29 PM.
- New NEWS_CO entries: Amazon, Granola. Top story unchanged (Gemini 4 Carbon); trending: Claude for Legal, Block Dessa, Genie 4.
- Refreshed X numbers on 44 existing items (items from Oct 14 on); Gemini 4 Carbon @sundarpichai now 32,739 likes / 6.15M views, Claude for Legal 30,202 / 7.1M. Raw response in research/x_news_measure_2026_10_29_pm.json.txt (local only), applied with research/news_x_2026_10_29_pm.py.
- Pricing: added row Mistral Large 4 ($0.70 in / $0.07 cached / $2.10 out per 1M) from Mistral's launch post; mistral.ai/pricing FAQ still quotes "Mistral Large" at $0.50 / $1.50, so that row stays.
- Skipped: "DeepSeek V4.1 Flash Cyber" (a third-party refusal-removed hosted variant, not a DeepSeek release), Mistral Responses API (developer preview), Meta developer MCP app tools (Oct 26, developer-only), Anthropic misuse self-assessment and AI for Science expansion (research/programs), Wabi and Mintive funding, OpenAI election center and gpt-4o lawsuit (not product news).
- BACKLOG: "find and cancel forgotten subscriptions" guide candidate (Grok Bot templates + Alexa Subscribe & Save), Alexa for Shopping as extra tool, Gemini file editing for study entries, CarPlay/Granola watch.
- Checks: validate 0 errors (110 use cases); build 151 indexed pages + 404; check_links 11,521 links, 0 broken internal.
- Deploy: main 1eadb29 / publish d7c4dac; GitHub Actions run 40940507850 succeeded in 29s (2:29 PM CT). Live /news/ and /ai-pricing/ show the new items and the Mistral Large 4 row. This deploy line is committed with the next deploy.

## 2026-10-29 (Trending watch, midday)
- New: `let-chatgpt-run-your-icloud-mail-and-calendar` (Inbox, Easy): ChatGPT's iCloud Mail and iCloud Calendar plugins (Oct 27, all plans). Sources: OpenAI Help Center, MacRumors, 9to5Mac, Engadget, r/ChatGPT; X @ChatGPT 5,790 likes / 391 reposts / 1,920,915 views (measured Oct 29).
- New: `tell-ifttt-what-to-automate-in-plain-words` (Work, Easy): IFTTT.ai AI Agent + plain-language Applets, free plan now unlimited Applets with 1,000 credits/month. Sources: IFTTT launch post, AI Agent page, Help Center, plans page, Product Hunt (#8 Oct 29, score 98, 7 comments), HiTecWeb; X @ltibbets 25 / 5 / 2,846. New tool `ifttt`.
- New: `get-an-ai-coach-that-helps-you-start-overwhelming-tasks` (Family, Easy): ChatGPT Projects + scheduled check-ins as a getting-started coach. Sources: r/ChatGPT parent post (Oct 28), manast.me ADHD body-double guide (Feb 7), OpenAI Help (scheduled tasks, Projects). No popularity number (Reddit counts not readable from the box).
- Extra sources: The Straits Times Muse test (Oct 28) on `proactive-next-moves-bot` (no longer X-only) and `restaurant-reservations-by-agent` (+ cancellation watch-out).
- Refreshed 46 tracked X posts. Source mix: 110 use cases, X 72/405 links (18%), X-only entries 7.
- Mentions/feedback: none. Bugs: none.

## 2026-10-28 (News update, PM)
- Added 9 items (all dated Oct 28): `google-gemini-4-carbon` (MAJOR, model release; Google blog, 9to5Google, VentureBeat; X @sundarpichai 15,791 likes / 1,173 reposts / 1,301,637 views), `chatgpt-dots-texting` (notable; ChatGPT Learn, The Verge, 9to5Mac; @ChatGPT 3,084 / 136 / 242,297), `claude-for-legal-artifacts` (notable; Claude blog, Reuters, Legal IT Insider; @claudeai 13,363 / 702 / 1,535,190), `google-connected-apps-platform` (notable; Google blog, TechCrunch; coverage @Marie_Haynes 27 / 2 / 2,243), `github-copilot-fusion` (notable, company Microsoft; GitHub changelog + Microsoft Copilot harness blog; @satyanadella 554 / 70 / 58,996), `nvidia-nemotron-3-5-transcribe` (notable; NVIDIA on Hugging Face, TechCrunch; @NVIDIAAI 3,106 / 245 / 223,086), `perplexity-voice-gpt-live-1` (minor; 9to5Mac; @AskPerplexity 152 / 13 / 31,495), `gemini-immersive-explorations` (minor; Google blog; @GeminiApp 385 / 29 / 21,792), `meta-waddle-world` (minor; TechCrunch; coverage @MattNavarra 33 / 1 / 8,233). All measured Oct 28 PM.
- New NEWS_CO entry: Perplexity. Gemini 4 Carbon is now the Top story.
- Refreshed X numbers on 32 existing items (all items from Oct 14 on); raw response in research/x_news_measure_2026_10_28_pm.json.txt (local only), applied with research/news_x_2026_10_28_pm.py.
- Pricing: no table change. Gemini 4 Carbon's announced intro price ($2 / $10, later $4 / $20) isn't on the Gemini API pricing page and the model isn't open to developers yet, so it's listed under not_verified. GitHub Copilot Fusion's 30% discount (through Nov 30) is noted in the news item only.
- Skipped: "Grok 5" (only a fan site; nothing on x.ai/news or the xAI release notes), OpenAI reportedly buying Google TPUs (unconfirmed), Amazon Alexa Photo Frame (no date on the official page), OpenAI-ServiceNow and Claude Enterprise smart reports (enterprise-only), Cloudflare GLM-5.3 data exposure, Giotto Alto/Solo.
- BACKLOG: dots texting as an extra source for the text-me agent entries; Connected Apps guide once it's live for normal users.
- Checks: validate 0 errors (106 use cases); build 146 indexed pages + 404; check_links 11,105 links, 0 broken internal.

## 2026-10-28 (Trending watch, midday)
- New: `add-an-ai-to-your-friends-group-chat-to-make-plans` (Bookings & travel, Easy), Instinct group chats on iMessage. Sources: TechCrunch (Oct 5), Business Insider (Oct 6), X @noahrshinn (Oct 27; 1,068 likes, 37 reposts, 137,199 views measured Oct 28).
- Extra sources: Link balance (Link help center, The Defiant, X @instinct) + watch-out on `pay-with-a-single-use-virtual-card`; Off Grid AI Product Hunt on the private-AI entry; TechCrunch on the family group-chat entry.
- Refreshed 45 X posts. Source mix: 106 use cases, X 69/382 links (18%), X-only entries 8.
- Mentions/feedback: none. Bugs: none.

## 2026-10-28 (Weekly SEO run (Wed), 10:15 AM CT)
Research (free sources: Google autocomplete, HN, web search)
- Gaps picked: agent file safety/sandboxing (autocomplete "sandbox ai agents", "best sandbox for ai agents", "are ai agents safe to use", "is hermes ai agent safe"; Ask HN 50192875) and insurance claims (autocomplete "ai to help with insurance claims", "chatgpt for insurance claims", "ai agent for insurance claims"; open BACKLOG item). Riverside candidate was already shipped on 10-27.

New pages
- `keep-an-ai-agent-from-deleting-your-files` (Work, Easy): one working folder, sandbox on, ask before deleting/moving, backups and a test restore, setup notes for Claude Cowork, Codex, OpenClaw and Hermes Agent. Sources: Claude Help (Use Cowork safely), Claude Academy best practices, OpenAI Codex sandboxing docs, OpenClaw sandboxing/workspace-access docs, Hermes Agent secure-on-a-work-machine guide, The Register (Jul 16, 2026), Ask HN 50192875 (4 points, 6 comments, measured Oct 28), GitHub anthropics/claude-code #86872. No time-saved claims.
- `put-together-an-insurance-claim-with-an-ai-agent` (Inbox & paperwork, Easy): agent gathers photos, receipts and dates into a claim packet and draft; you submit it yourself. Sources: NAIC, Insurance Information Institute, Texas Department of Insurance, Claude Help (Cowork). No stats quoted.
- New tools in data/tools.json: openclaw, hermes-agent.

Other improvements
- New "See also" box (build.py `see_also_html`, data field `see_also`). Used to fix the duplicate meal-plan backlog item: the one-off plan page and the recurring grocery-agent page now explain the difference and link to each other (no canonical, no deletion).
- Internal links into the new pages from: sort-and-rename-a-messy-folder, use-a-private-ai-on-your-own-computer-for-your-files, appeal-a-health-insurance-denial, get-roadside-help-abroad, the email-safety guide (Related), the OpenClaw vs Hermes safety section, and the "Are AI agents safe to use?" FAQ on /what-can-bots-do/ and /ai-agent-examples/. Plus automatic tag-based Related links, hubs and categories.
- llms.txt, llms-full.txt, sitemap.xml and the search index include both new pages. FAQPage, HowTo and BreadcrumbList JSON-LD are generated for both.

Checks
- validate 0 errors (105 use cases, 12 blueprints); build 145 indexed pages + 404; check_links 11,000 links, 0 broken internal, 647 unique external.

AI-citation check (Oct 28, ~10:10 AM CT)
- Web search tool: botsdothat.com/ai-agent-examples/ was the #1 result for "everyday AI agent use cases" and "AI agent examples for everyday life". Not in results for "what is an AI agent for beginners", "OpenClaw vs Hermes Agent", "how much does it cost to run an AI agent" or "how to keep an AI agent from deleting your files" (new page, not live yet at check time).
- Bing (top 10, plain HTML fetch) and DuckDuckGo HTML: botsdothat.com not present for any of the 6 queries (DuckDuckGo served a bot challenge for 2 of them).
- X: no posts mentioning botsdothat from other accounts.
- Not tested: Perplexity (403 without login), ChatGPT, Google AI Overviews and Grok answers (no logged-out access or tool for these).

Proposals (need approval, see BACKLOG)
- Rework or label the 14 chat-prompt use cases; clarify /use-cases/ vs /ai-agent-examples/ with cross-pointers; meal-plan canonical only if they still compete.

Deploy
- scripts/deploy.sh at 10:15 AM CT (no other deploy running; origin/main was 458fac8). main f7970a4 / publish db419ba; GitHub Actions run 40714089308 succeeded in 35s (10:15 AM CT). Live checks 10:16 AM CT, all 200: both new pages, /what-can-bots-do/, /ai-agent-examples/, the email-safety guide, /openclaw-vs-hermes-agent/, both meal-plan pages (See also box present), /use-cases/, /, llms.txt, llms-full.txt, sitemap.xml (both new URLs listed). This deploy line is committed with the next deploy.

## 2026-10-28 (daily QA run, 7:10 AM CT)
Status: live site https://botsdothat.com/ is up (homepage 200 in about 0.22 s; /use-cases/, /trending/, /news/, /advertise/, /ai-pricing/, /assets/app.js, /assets/style.css, the search index, sitemap.xml and llms.txt all 200).

Checks
- validate 0 errors (102 use cases before this run); build 142 indexed pages + 404; check_links 10,756 links, 0 broken internal. app.js passes a syntax check.
- Outbound links (628 unique): 563 OK, 65 not-200, none real. The checker's HEAD requests got 404 from support.google.com (10 help pages) and thenextweb.com (2 articles) and 405 from Hacker News and Zumper; every one returned 200 with the right page title on a normal GET (Zumper serves a bot challenge). Still script-only blocks: openai.com / help.openai.com, claude.ai, ftc.gov, Riverside help, RentCafe, Retail Dive, Android Authority, AHRQ, kit.com/privacy (429); Business Wire timed out.
- Console errors and real-device rendering were not checked in a browser this run (static review only).

Bugs fixed
- None found.

Improvement for visitors
- New guide from the backlog: `organize-your-photos-by-asking` (Family & home, Easy). Connect Google Photos to Gemini and use a task to pick the best shots from a trip or event, skip near-duplicates and save them to a new private album, optionally on a monthly schedule. The prompt forbids deleting, moving, editing or sharing anything. Watch-outs cover the gradual rollout (18+, not in some US regions), wrong picks (Ask Photos is experimental), albums being labels not folders, and checking shared albums for private photos. Sources: Gemini Apps Help, Google Photos Help (Ask Photos, albums), Google blog (Feb 10, 2026). No stats quoted. BACKLOG item marked done.
- After: validate 0 errors, 103 use cases; build 143 indexed pages + 404; check_links 10,824 links, 0 broken internal.

## 2026-10-27 (trending watch, midday)
- Added 3 use cases: turn-a-recording-into-an-episode-clips-and-posts (Riverside Agents; Riverside blog + help center, Forbes, Podnews, @NadavKeyson launch post 560 likes / 1,917 reposts / 991,250 views), use-a-private-ai-on-your-own-computer-for-your-files (Hob; HN 159 points / 36 comments, GitHub 243 stars, FounderMag, OSFY), get-a-text-before-something-needs-doing (Kiwi; Product Hunt #11 with 109 upvotes / 15 comments, Kiwi blog, Business Wire on Ant LingGuang 2.0). All measured Oct 27. New tools: riverside-agents, hob, kiwi.
- Non-X sources added to 6 X-only entries (X-only count 14 -> 8). Refreshed 43 X posts and 28 HN scores.
- Totals: 102 use cases, 358 source links, X 67/358 = 19%. No BotsDoThat mentions found on X, HN or the web.

## 2026-10-27 (weekly SEO and AI-chatbot run, 9:20 AM CT)
Deploy: main 4bde33a / publish d33cb3f (GitHub Actions run 40519984038 succeeded 9:19 AM CT). Live pages checked after deploy: /, /ai-pricing/, the cost guide, /trending/, /use-cases/, /blueprints/, /category/run-for-less/, /newsletter/, /advertise/, /privacy/, /ai-agent-examples/, the build guide, /run-your-bots-for-less/, both retitled use cases, llms.txt, llms-full.txt, sitemap.xml and robots.txt. All returned 200, and llms.txt now says prices were checked on 2026-10-27. The saashub-verification meta is still present, and VERIFY_META is unchanged.

Changes
- AI prices (data/ai-pricing.json): every checked_on is now 2026-10-27. Each official page was re-read: OpenAI pricing + API changelog + batch guide, Anthropic, Google Gemini API, xAI models, Groq, DeepSeek, Mistral, Meta launch post, claude.com/pricing, chatgpt.com/pricing and gemini.google/subscriptions. No API price changed from the previous values. Added: Meta Muse Wonder cached input $0.20, now listed on Meta's post, where it was null before. Added: Google AI Ultra consumer row, "from $99.99/month" for 5x AI Pro limits, $199.99/month for 20x, US pricing now shown on the official page. The Google not_verified entry is narrowed to the AI Plus and Pro USD prices. The DeepSeek source_url now has a trailing slash (https://api-docs.deepseek.com/quick_start/pricing/), because the old URL serves the "first API call" page to fetchers. The Haiku/Fable price line in pick-a-smaller-model-for-simple-jobs is unchanged and its date was updated to Oct 27. Blueprint cost notes are recalculated from the table, with no number changes. Still not_verified: ChatGPT Go/Plus/Pro prices (not shown in page text), xAI SuperGrok, Groq consumer, and Google AI Plus/Pro USD. Seen but not added: GPT-5.6 Sol promo pricing ($4/$20 through at least Nov 21, 2026), gemini-3.5-flash-lite ($0.30/$2.50), and DeepSeek Search/Fetch at $0.75 per 1K requests, billed from Nov 1, 2026.
- New quotable content for search gaps:
  1. A "Cheapest AI API by job" table at /ai-pricing/#cheapest, plus a matching FAQ (in FAQPage schema) and a line in llms-full.txt. It is computed only from verified rows: overall Groq gpt-oss-20b $0.075/$0.30; small from the big labs gpt-6-luna and Haiku 5.5 $0.10/$0.50; with a free tier gemini-3.1-flash-lite $0.25/$1.50; mid-size gpt-oss-120b $0.15/$0.60; flagship grok-4.7 $2/$6; DeepSeek flash off-peak $0.15/$0.60; batch 50% off.
  2. A cost guide FAQ, "How do I work out what my AI agent will cost?", giving the formula, 4 numbered steps (including checking the usage page after one test run) and a worked example.
- Technical SEO: added ItemList schema to /trending/ (top 20), /use-cases/ (all 99), /blueprints/ (12) and all 8 category pages. ItemList pages went from 3 to 14. Added an sr-only h2 on /trending/ to fix the h1→h3 skip. Category descriptions now use mdesc, fixing /category/run-for-less/ at 194 chars. Trimmed the /newsletter/ (165), /advertise/ (188) and /privacy/ (169) descriptions. Shortened 2 long use-case titles (slugs kept): "Have a bot watch your kids' team apps for plan changes" and "Let your bot sign in without seeing your passwords".

Checks
- validate 0 errors (99 use cases, 12 blueprints); build 139 indexed pages + 404; check_links 10,478 links, 0 broken internal. The SEO audit script found 0 issues: title and description lengths, canonical, one h1, heading order, JSON-LD parse, and no duplicate titles or descriptions. robots.txt allows the AI crawlers and lists the sitemap; the sitemap has 139 URLs.
- Cloudflare Web Analytics (GraphQL, bots excluded), Oct 20 00:00 to Oct 27 00:00 CT: 89 visits, 112 page views, google.com referrals 25 visits, t.co 1. Top pages: / (56 pv), /blueprints/ 6, /use-cases/ 5, /news/ 5. US 74 visits. p75 LCP 0.73 s, INP 64 ms, CLS 0.002. This window is a little different from the Oct 26 baseline (78 visits / 101 pv / 18 Google), so the two are not an exact match.
- Search Console: not available this run. The box has no API access, and I didn't use a signed-in browser.
- AI/search citation check (web-search tool used in this run, Oct 27): botsdothat.com/ai-agent-examples/ showed up as result #1 for "AI agent examples for everyday life" and #3 for "AI agent use cases for everyday people". It did not appear in the top 5 for "how to build an AI agent for beginners", "cheapest AI API 2026" or "how much does it cost to run an AI agent per month". DuckDuckGo HTML top ~10 did not show botsdothat for any of the 5 queries. Bing blocked script access. Google, ChatGPT and Perplexity answers could not be verified.

## 2026-10-27 (daily QA run, 7:00 AM CT)
Status: live site https://botsdothat.com/ is up (homepage 200 in about 0.26 s; /use-cases/, /trending/, /news/, /advertise/, /ai-pricing/, app.js, style.css, sitemap.xml and llms.txt all 200).

Checks
- validate 0 errors (98 use cases before this run); build 138 indexed pages + 404; check_links 0 broken internal links. app.js passes a syntax check; the search index loads (114 entries). Every page has one h1 and a viewport tag; no images without alt text, no empty links or buttons, no missing local images or scripts.
- Outbound links (470 unique): no real breakages. Script-only blocks: openai.com and help.openai.com (403), claude.ai (403), investing.com and retaildive.com (403), YouTube and Hacker News (429 rate limits), kit.com/privacy (429). ftc.gov and consumer.ftc.gov now return 404 to scripts for every page, even the homepage (they used to 403); the three FTC pages we link still show up in a current web search, so this is a bot block, not moved pages. Meta help (400), dev.meta.ai (500) and Business Wire (timeout) failed to curl but loaded fine through a normal fetch.
- Console errors and real-device rendering were not checked in a browser this run (static review only).

Bugs fixed
- None found.

Improvement for visitors
- New guide from the backlog: `find-an-apartment-that-fits-your-list` (Family & home, Easy). It walks through using the rental apps inside ChatGPT (Apartments.com, Zumper, RentCafe, Apartment List) to search live listings from a must-have list, compare rent, fees and pet rules, and request tours only for picked places. The prompt tells the AI not to guess missing details or contact anyone without a go-ahead. Watch-outs cover stale listings, rental scams (FTC advice) and not sharing ID or SSN early. Sources: CoStar/Apartments.com press release (Sep 8, 2026), RentCafe help, Zumper, FTC. No stats quoted. BACKLOG item marked done.
- After: validate 0 errors, 99 use cases; build 139 indexed pages + 404; check_links 0 broken internal.

## 2026-10-26 (news update, 2:30 PM CT)
- Added 6 items to data/news.json (newest first): GPT-6.1 Terra, OpenAI's new mid-size computer-use model at $1 in / $5 out (Oct 26, notable, X @OpenAI); Anthropic files S-1 for a Nasdaq IPO as "ANT" (Oct 26, notable, X @AnthropicAI); Claude for Nonprofits plugin (Oct 26, notable, X @claudeai); Claude Enterprise merges chat and Cowork (Oct 23, notable, missed earlier, no official X post found); Gemini Notebook as a Connected App in Gemini (Oct 23, notable, missed earlier); Walmart Agent Gateway and Agent Profiles for AI shopping agents (Oct 21, notable, missed earlier, no credible high-engagement X post).
- Rated GPT-6.1 Terra notable, not major: it is OpenAI's mid tier, and GPT-6 Astra remains the flagship. Top story stays Claude Duet.
- New company "Walmart" in NEWS_CO (scripts/build.py).
- Pricing: added gpt-6.1-terra ($1.00 / $5.00, cached $0.05) to data/ai-pricing.json from the official OpenAI pricing page.
- X numbers for the 3 new posts: research/x_news_measure_2026_10_26_pm.json.txt, applied by research/news_x_2026_10_26_pm.py. Other tracked posts were re-measured this morning.
- No new use case: Terra's form filling and invoice entry are already covered by existing web-form and invoice use cases; Walmart agent shopping is logged for the backlog once Agent Profiles roll out.
- Checked: OpenAI API changelog and pricing, Anthropic news, Claude blog, xAI news, Mistral, DeepSeek updates, Google blog and Workspace Updates, TechCrunch, and X posts from the major labs since this morning. Skipped: Mirendil Fern 0.1 and Nanbeige4.3-33B (small labs, research-scale), a Gemini "Remembered items" APK teardown (unreleased), and roundups.

## 2026-10-26 (daily QA run, 7:15 AM CT)
Status: live site https://botsdothat.com/ is up (homepage 200 in about 0.2 s; /use-cases/, /trending/, /news/, /advertise/, app.js, style.css and the search index all 200).

Checks
- validate 0 errors (94 use cases before this run); build 134 indexed pages + 404; check_links 0 broken internal links. A quick scan found no images without alt text and no empty links or buttons.
- Outbound links (686 unique): no real breakages. Bot-check or rate-limit responses to scripts only: openai.com, help.openai.com, claude.ai, ftc.gov / consumer.ftc.gov (whole domain 403s to curl), investing.com, and 10 Hacker News items (429 rate limit; all 10 confirmed live stories through the HN API).
- Console errors and real-device rendering were not checked in a browser this run (static review only).

Bugs fixed
- Meta moved its Muse help pages from /help/artificial-intelligence/ to /help/superintelligence/. The two old links redirected and then failed for scripts, so they now point at the new URLs (data/use-cases.json, data/tools.json); both new pages were opened and confirmed.

Improvement for visitors
- New guide from the backlog: `compare-two-documents` (work, Easy). Plain steps that pair AI's plain-words list of changes with Word's built-in Compare as the exact check, a prompt that asks for every change with both wordings quoted, watch-outs about missed deletions, getting a lawyer for binding documents and keeping private details out, and two FAQ answers. Sources: Microsoft Support, Contract Nerds, Draftable. No stats quoted.
- After: validate 0 errors, 95 use cases; build 135 indexed pages + 404; check_links 0 broken internal.

## 2026-10-26 (news update, 6:30 AM CT)
- Added 6 items to data/news.json (newest first): Gemini API stores requests by default for new paid projects (Oct 26, minor); Block's Dessa full-duplex speech model, research preview only (Oct 23, notable, X @jack); OpenAI trains frontier models offline (Oct 23, notable, X @OpenAI); OpenAI Agents API scheduled automations (Oct 23, notable, docs + community post, no official X post found); OpenAI legacy model shutdown of GPT-4, GPT-3.5 Turbo, o1, o3-mini, o4-mini, gpt-image-1 and others (Oct 23, minor); ChatGPT locked chats (Oct 20, notable, missed earlier; no credible high-engagement X post).
- New company "Block" in NEWS_CO (scripts/build.py).
- Re-measured all 38 tracked X posts (research/x_news_measure_2026_10_26_am.json.txt, applied by research/news_x_2026_10_26_am.py). Top story is still Claude Duet (no new major item).
- No pricing changes (retired OpenAI models weren't in data/ai-pricing.json). No new use case: Agents API automations is already covered by the scheduled-bot use cases.
- Checked: OpenAI, Anthropic, Google/Gemini changelog, xAI news and release notes, Mistral, DeepSeek, OpenAI API changelog and deprecations, TechCrunch, and X posts from the major labs since Oct 23. Skipped: OpenAI Cosmos DB storage engineering post, Claude Code 2.1.310 (changelog-level), Gemini small-business tools (Oct 20, outside window), opinion pieces and roundups, and anything without an official or reputable source.
- validate 0 errors; build 134 pages; check_links 0 broken.

## 2026-10-24 (late morning CT) — Sources beyond X: "Seen on" line, multi-site heat, 12 new use cases
- Nik's ask: stop relying on X alone. Before: 61/162 source links were X (85% of community links); 37 of 82 use cases were X-only. After: 61/316 (28% of community links); 14 of 94 X-only. Full numbers and method: ops/source-mix.md (re-run `python3 scripts/source_mix.py`).
- data/use-cases.json: 53 existing entries gained 96 non-X sources (YouTube, Hacker News, GitHub, Reddit). New optional source fields: `kind` can now be `hn`, `youtube` or `github`; `stats` {points|upvotes|comments|views|stars: int}; `measured_at`; `posted_at`. validate.py checks them (integers only, measured_at required).
- 12 new use cases (origin `community-backfill-2026-10-24`): researched report with sources, documents to podcast (Gemini Notebook), private smart-home AI, live screen/camera tech help, meeting notes, language speaking practice, interview rehearsal, build a small app by describing it, sort and rename a messy folder, voice memos to notes, read old handwriting, PDF invoices to a spreadsheet. New tools in tools.json: `notebooklm` (Gemini Notebook, formerly NotebookLM) and `home-assistant`.
- Display: cards show a small "Seen on X · Reddit · YouTube" line (only when a use case has 2+ platforms); use-case pages show it under the header, add the measured numbers next to each source, and a sidebar "Also discussed on" box.
- Ranking: heat now sums every measured post from the last 60 days: X (likes + 2×reposts), Reddit (upvotes) and Hacker News (points), each ÷ weeks since posted. YouTube views and GitHub stars are shown but not counted (different units, accumulate over years). Entries without an X/Reddit popularity block can now trend from an HN post (book-an-appointment-with-an-ai-agent entered at #30). /about/ and /trending/ text updated.
- Reddit scores aren't readable from the box (JSON 403/login; RSS has no scores), so new Reddit sources carry no numbers.

## 2026-10-24 (morning CT) — Per-page social preview images
- 18 pages now have their own 1200x630 og:image / twitter:image: the top 15 use cases on /trending/ (snapshot Oct 24) plus /use-cases/, /trending/ and /blueprints/. Images were made by the Marketing bot.
- Source PNGs live in static/og/<slug>.png and publish at /assets/og/<slug>.png. data/og_images.json maps canonical path -> image (trailing slash normalised). Every other page keeps /assets/og.png. All pages keep og:image:width 1200, og:image:height 630 and twitter:card summary_large_image. build.py prints a WARNING if a mapped path has no built page.
- Regenerate when the ranking changes: edit RANK in scripts/make_og_images.py (it reads data/use-cases.json and needs the source art in /workspace/botsdothat/og-images/_art/<slug>.jpg plus Poppins fonts), run `python3 scripts/make_og_images.py` (writes to /workspace/botsdothat/og-images/ + manifest.csv), then copy the PNGs into static/og/, update data/og_images.json, and deploy with scripts/deploy.sh. Check each PNG is 1200x630 and under 1 MB.

## 2026-10-23 (7:30 PM CT) — Sponsor self-serve checkout is live (Stripe live mode)
- /advertise/ "Book & pay" buttons now open live Stripe Payment Links (account acct_1UTrztBgq3cPhA7u). Featured $49, Run for less $99, Bundle $149, Newsletter issue $50; one-time, no renewal. Each collects website URL, headline + one-line description, and preferred start month (newsletter: optional logo link instead). Promo codes on, post-payment invoice on, redirect to /sponsor-thanks/, Managed Payments off.
- Codes: FOUNDING (100% off once, featured only, 3 uses). New FIRST2 (100% off once, newsletter only, 2 uses) for Nik's "first 2 issues free"; shown on the newsletter tier.
- Double-booking: the Run for less and Bundle links each stop after 1 completed sale. **Monetization routine:** if either one shows a completed sale, deactivate the other link in Stripe until that month's placement ends, then reactivate both (or reset the limit). /sponsor-thanks/ and /sponsor-terms/ now say that if a spot was already taken, we tell the buyer within 1 business day and refund in full.

## 2026-10-23 (6:45 PM CT) — New /sponsor-terms/ page
- New plain-English /sponsor-terms/. It covers:
  - What we accept (relevant AI, automation and productivity tools) and what we don't (adult content, gambling, crypto get-rich schemes, misleading claims, malware or scams).
  - Every sponsorship is labeled "Sponsored".
  - Each ad is reviewed before it runs, usually within 2 business days, with a full refund if we decline it.
  - What the sponsor provides (name, URL, headline, short text, logo). We may lightly edit it, and claims must be accurate and are the sponsor's responsibility.
  - Placement runs for the period bought, starting from the chosen month, with no auto-renewal.
  - Refunds: a full refund before the spot goes live, and none for the current period after that.
  - No guaranteed traffic; measured stats are shared on request.
  - Payments are processed by Stripe; contact hello@botsdothat.com.
  - Last updated Oct 23, 2026.
- Linked from the footer (next to Privacy) and from /advertise/ under "Our rules". It is in the sitemap automatically. The /advertise/ buttons are unchanged, and payment links will come later.

## 2026-10-23 (6:45 PM CT) — Share buttons and "forward it" line
- Every use case, blueprint and guide page (no-code build, cost, OpenClaw vs Hermes, safety, what's an AI agent, examples, Run for less) now ends with a "Share this" bar before the newsletter signup:
  - Share on X: an intent URL with the page title, the URL and via=botsdothat.
  - Copy link: uses the Clipboard API, falls back to execCommand, then shows the URL. With JS off, a read-only URL field shows instead.
  - Email a friend: a mailto with a subject and the link.
- The bar is plain links plus one button, with inline SVG icons. There are no third-party scripts or trackers. Buttons have aria-labels, 44px touch targets and a polite status message.
- Every newsletter form now has the line "Know someone who'd like this? Forward it, or send them to botsdothat.com/#subscribe". The homepage form after the trending grid carries `id="subscribe"`.

## 2026-10-23 (6:30 PM CT) — Tool cost text: Claude Cowork and Grok Bot
- data/tools.json `claude-cowork` cost: "Paid Claude plans only (Pro, Max, Team, Enterprise)". Verified Oct 23 on https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork ("Cowork is available to paid Claude plans (Pro, Max, Team, Enterprise) only").
- data/tools.json `grok-bot` cost: "Included with paid individual Cursor plans and Cursor Teams; or link SuperGrok, SuperGrok Plus or SuperGrok Heavy; or a self-serve Grok Business seat". Verified Oct 23 on https://docs.x.ai/grok-bot/overview ("included with every paid individual Cursor plan and with the Cursor Teams plan. You can also link an individual SuperGrok, SuperGrok Plus, or SuperGrok Heavy subscription, or sign in with a seat on a self-serve Grok Business plan").
- Both entries already linked these pages in their `url` field, which is how every tools.json entry cites its source.

## 2026-10-23 (night CT) — Review quick wins, part 2: nav order, headings, honest setup sizes, blueprint links, logo schema, real dateModified
Follows the evening batch (ae4390f), which already shipped privacy, contact email, ticker tabindex, mobile menu, newsletter fallback, popularity hiding and X links. tools.json was not touched (the CEO agent owns it).
- Nav: "What's an AI agent?" is first. At 641 to 899px the link row now fades on the right while links are hidden off-screen (JS toggles `.menu-more`). Without JS the row always fades at that width.
- /category/run-for-less/: title "AI cost-saving guides for your bots", H1 "Cost-saving guides for your bots". It was "AI agents for run your bots for less" and duplicated the hub H1.
- Heading order: a visually hidden H2 now sits before the card grid on /use-cases/ and every /category/* page, so headings go H1, H2, H3.
- Blueprints: "Rough setup time: about N minutes" is replaced with "4-step bot" (every blueprint has 4 steps). phone-call-bot reads "4-step bot · needs a calling add-on". The guide table column is now "Size". validate.py rejects durations in setup_time.
- Unsourced time claims removed. These became "short" or were cut: "2-minute summary" (morning-inbox-briefing), "2-minute Monday briefing", the morning-news-digest title (slug kept), resignation letter "in a couple of minutes", confusing letter "In a few minutes" and "Reply in two minutes". Sourced figures stay unchanged.
- Blueprint links remapped:
  - watch-for-one-important-letter and reply-to-customer-reviews no longer show an unrelated bot (none fits).
  - catch-airline-schedule-changes now shows only travel-day-guardian.
  - plan-and-book-a-whole-trip-by-text and pay-with-a-single-use-virtual-card no longer show travel-day-guardian.
  - sunday-family-calendar-check now shows only family-calendar-guardian.
  - chase-an-unpaid-invoice now shows only follow-up-finder.
  - time-sensitive-inbox-watcher moved from follow-up-finder to morning-inbox-briefing, which flags deadlines within 48 hours.
- Schema: one shared Organization (name, url, `logo` = /assets/img/logo-512.png rendered from favicon.svg, `sameAs` X) is used for home, explainer, guides, HowTo and use-case pages. No named Person editor was added.
- dateModified / "Updated" dates now change only when content changes. Pages use MOD tokens, and page() hashes title, description, body and JSON-LD against data/content-dates.json, keeping the stored date when the hash is unchanged. This covers the explainer, examples, the no-code guide, the cost, OpenClaw and safety guides and the disclosure. Sitemap lastmod follows the same dates. datePublished is fixed: explainer 2026-10-20, the no-code guide and the 3 new guides 2026-10-23. Before this change both values were the build date.
- Footer: "Follow on X (@botsdothat)" (rel="me"). /newsletter/ adds "Between issues, follow @botsdothat on X". llms.txt About lists Privacy, the X account and hello@botsdothat.com. /about/ Contact adds GitHub issues as a secondary option after the email.
- Newsletter promise: already one wording sitewide from the evening batch ("3 to 5 practical jobs you can hand to AI each week" plus "Free, one email a week"), so it was left as is.

## 2026-10-23 (evening CT) — Site review batch: inline signups, privacy page, contact email, mobile menu, ChatGPT agent retired
Implements the site review (all items except #6 homepage reorder and #7 intro/rotating headlines, which were left untouched). Kit itself was not touched.
- Newsletter: the same Kit form (10088120, double opt-in) now appears at the end of every use case, blueprint, guide (no-code build, cost, OpenClaw vs Hermes, safety, what-is-an-AI-agent, examples), /trending/ and /news/, plus once on the homepage right after the trending grid. `newsletter_box(uid, variant)` gives every form unique ids. One promise everywhere: "3 to 5 practical jobs you can hand to AI each week". Every form has a Privacy link under it.
- Unsold sponsor spots ("Your agent or tool could be here") now show a newsletter signup card instead (`featured_slot` falls back to `newsletter_box`). The homepage bottom shows one signup when no sponsor is booked. On screens under 1000px the use-case sidebar card is hidden so mobile readers don't see two forms back to back. Advertise stays in the footer.
- New /privacy/ (plain English): Kit email collection, double opt-in, unsubscribe any time, cookie-free Cloudflare Web Analytics with no personal data, we never sell or share data, contact hello@botsdothat.com, last updated Oct 23, 2026. Linked in the footer and under every signup form, and listed in the sitemap.
- Contact: `config.contact_email` is now hello@botsdothat.com, so footer Contact, about, disclosure and advertise use mailto links. /advertise/ has an "Email us about this spot" mailto per tier plus the bundle, each with its own subject line. The audience copy now says (honestly, with no numbers) that Search Console and Bing were verified Oct 23 and Cloudflare Web Analytics went live Oct 23, and that measured numbers will be shared on request once there's a meaningful sample.
- Mobile nav: a Menu button at 640px and below opens the full link list. It is accessible: `aria-expanded`/`aria-controls`, Esc closes it and returns focus to the button, it closes on a click outside or on a link, and opening it focuses the first link. Without JS the old scrolling row still shows. The header CTA reads "Weekly email" under 480px. Labels are now: Trending, Use cases, Build a bot, What's an AI agent?, AI news, Run for less. "Build a bot" is used in the nav, the /blueprints/ title and h1, blueprint breadcrumbs and the footer. URLs are unchanged, and Trending and Use cases were not merged.
- "Popularity: not measured" badges and the empty sidebar box are hidden. About explains that unmeasured items show no number.
- /trending/: the formula is replaced by one plain sentence and a "How we rank" link to /about/#popularity, where the formula stays. The calculator has a one-line "Tokens?" explainer. Category and Run-for-less page headers stack the icon above the title at 640px and below.
- X: @botsdothat (https://x.com/botsdothat) is linked in the footer and on about, with `twitter:site` meta and Organization `sameAs`.
- Ticker: the aria-hidden duplicate links get `tabindex="-1"`.
- Sources: the 22 "Google search suggestions" sources are now labeled "Search demand signal" (with a tooltip saying they aren't a source of facts). None were removed or replaced.
- ChatGPT agent discontinued. OpenAI's help page https://help.openai.com/en/articles/11752874-chatgpt-agent now says "ChatGPT agent is no longer available. Use ChatGPT Work … For supported browser workflows, see Using cloud browser in ChatGPT". https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt says cloud browser is part of ChatGPT Work on paid plans, excluding Free and Go, and that availability varies during rollout. Changes:
  - The tools.json `chatgpt-work` entry is renamed to "ChatGPT Work (cloud browser)", with cost "Paid ChatGPT plans only (not Free or Go); rolling out". It is used by 13 use cases and 2 blueprints, and their cloud-browser notes still apply.
  - The explainer text now says "ChatGPT Work".
  - The safety guide's OpenAI source now points to the cloud-browser help page.
- Checks: validate 0 errors (82 use cases, 12 blueprints); build 121 indexed pages + 404; check_links 7,934 links, 0 broken internal; no duplicate ids on any page. Lighthouse mobile (local) for home, a use case and /privacy/: performance 99/100/100, accessibility 100, best practices 96, SEO 100. Screenshots are in /workspace/review/ship/.

## 2026-10-23 (5:55 PM CT) — Three new beginner guides: AI agent costs, OpenClaw vs Hermes Agent, email/calendar safety
- New /how-much-does-it-cost-to-run-an-ai-agent/ (Article + FAQPage + BreadcrumbList): every number is computed at build time from data/ai-pricing.json and the existing calculator presets (cheapest/priciest per blueprint, worked Morning Inbox Briefing math, app-plan table, voice per-minute with a labeled 10-minute example, batch providers). Each row links to the calculator with `?bot=`. OpenClaw/Hermes cost section cites official docs only. Reddit self-reported costs left out on purpose.
- New /openclaw-vs-hermes-agent/ ("OpenClaw vs Hermes Agent: a beginner's guide"): what each is, which Hermes (Nous Research's Hermes Agent, confirmed via each project's migration docs), side-by-side table (maker, price, setup, where it runs, chat apps, models, schedules, memory, safety controls, switching), how to pick, costs, safety tips, FAQ incl. "cheapest way to run Hermes Agent". Every fact cites the OpenClaw or Hermes README/docs. No Nous Portal price given (not in our data).
- New /is-it-safe-to-give-an-ai-agent-your-email/: prompt injection, too much access, sending without review, 8 "you stay in charge" rules, safe-by-design blueprints, OpenClaw/Hermes section. Cites OWASP LLM01/LLM06 2025, OpenAI prompt-injection page and ChatGPT agent help article, Google linked-apps help, OpenClaw and Hermes security docs, WIRED.
- Cross-links: footer Explore; use-case cost tip and "New to this?" line (safety link on inbox-category or Gmail/Outlook/calendar-tagged use cases); blueprint cost box and setup box (safety link when the bot touches email/calendar); /what-can-bots-do/, /ai-pricing/ FAQ, /run-your-bots-for-less/ FAQ, and the no-code guide (step 7, safety rules, email FAQ).
- Machine files: the 3 pages added to sitemap (automatic), llms.txt Start here, llms-full.txt (one section each); search-index.json now includes these 3 plus the no-code guide (category "Guide").
- Wording fix in the no-code guide's free-plans FAQ: "ChatGPT agent needs a paid ChatGPT plan" → "ChatGPT's cloud browser needs a paid ChatGPT plan" (OpenAI's ChatGPT agent help page now says ChatGPT agent is no longer available). tools.json still names the tool "ChatGPT agent (cloud browser)"; left for the tool-data owner.
- Checks: build OK, validate 0 errors, check_links 0 broken internal; JSON-LD parses; titles ≤65 chars; Cloudflare beacon present.

## 2026-10-23 (5:40 PM CT) — Fix: clipped descenders in gradient headlines
- Bug (reported by Nik): in the homepage hero, the gradient words ("handing everyday") lost the bottoms of g/y. `background-clip:text` only paints inside the element box, and with line-height 1.02 the descenders of fonts like Segoe UI/Inter fall outside it. Reproduced locally with Inter and DejaVu Sans.
- Fix (static/style.css): `.k-grad` gets bottom padding .16em (plus .06em on the right), cancelled by margin-bottom -.16em so the layout doesn't move. The rotator (`.rotator` and its spans) goes from 1.08em to 1.24em tall, with margin-bottom -.16em. The XL news headline (`.nt--xl .nt-h`) gets the same padding/negative-margin pair, and page h1s (`.kinetic-sm`) get padding-bottom .1em.
- Checked in headless Chrome at 1280px and 390px for all 4 rotating headlines (plus the rotator), with Inter, DejaVu Sans and Noto Sans: descenders fully visible, no overlap, no jump between rotations. Also checked the /news/ XL headline, the /what-can-bots-do/ h1 and a use-case h1.

## 2026-10-23 (5:10 PM CT) — SEO pass: internal links, AI-agent explainer, pricing FAQ, new beginner build guide
- NEW page /how-to-build-an-ai-agent-without-coding/ (HowTo + FAQPage + BreadcrumbList). It has 7 steps, uses the Morning Inbox Briefing as a worked example (spec, tools, instructions, safety, and a cost line computed from data/ai-pricing.json with a `?bot=` calculator link), a table of all 12 blueprints, "agent app vs no-code automation", 5 safety rules and an FAQ. Tool facts come from data/tools.json (official URLs). No time-saved claims. I dropped "in an afternoon" from the requested title, in line with the 12:28 PM rule against unsourced time promises. Linked from the footer (every page), homepage, /what-can-bots-do/, /blueprints/ (index head and every blueprint's setup box), /ai-agent-examples/ and every use case's "New to this?" line. Also added to the sitemap (automatic), llms.txt "Start here" and llms-full.txt.
- /what-can-bots-do/ (URL kept): new H1 "What is an AI agent? (in simple terms)", title "What is an AI agent? Simple terms, vs. chatbots". New "What is an AI agent?" H2 section. The chatbot section is now "AI agent vs. chatbot: what's the difference?" (#ai-agent-vs-chatbot). Added "More everyday jobs to try" (17 under-linked use cases in 4 groups) and a 6-question FAQ. Schema: BreadcrumbList + Article (datePublished 2026-10-20, dateModified build date) + FAQPage. Nav and footer label: "What is an AI agent?". Its FAQ is also in llms-full.txt.
- /ai-pricing/: new "Questions about AI API prices" FAQ (7 Q&As) + FAQPage schema. Every number is computed from data/ai-pricing.json (cheapest model, cached-input example, batch providers, example monthly cost, checked date). No new figures. Also in llms-full.txt.
- /blueprints/ index: every card has a "Real people using this" list from blueprints[].related (CSS: .bp-card.has-real / .bp-real).
- Use-case pages: a new cross-category "Related" block (3 picks, scored on shared tags/tools/words, ties go to less-linked pages). A new "What this costs to run" box links the blueprint's #cost and `/run-your-bots-for-less/?bot=<slug>#calculator` where a calculator preset exists, otherwise the generic calculator, plus a tip guide; run-for-less pages skip it. The meta line now reads "Updated <date> · By BotsDoThat", and HowTo schema has dateModified (last_checked or date_added) + Organization author/publisher.
- Homepage explainer teaser: links 6 under-linked use cases + /blueprints/scam-checker/, and a button to the new guide. The under-linked pages (book-an-appointment, email-ghostwriter, homework-help, plan-a-trip, parents' care paperwork, scam-checker) went from 3 linking pages to 5–8.
- data/use-cases.json: shortened the 8 titles that were over 65 characters (the audit's "~10" counted HTML entities). Slugs unchanged. All <title>s are now ≤65 characters.
- Skipped per Nik: OG images, homepage H1. Cloudflare beacon (8a9bedf) still on all pages.
- Checks: build OK (117 indexed pages + 404), validate 0 errors, check_links 0 broken internal, all JSON-LD parses.

## 2026-10-23 (4:40 PM CT) — Cloudflare Web Analytics on every page
- config.json: new `analytics.cloudflare_token` (public beacon token). scripts/build.py emits Cloudflare's beacon `<script defer …beacon.min.js data-cf-beacon=…>` in the <head> of every page made by page(), including 404, only when the token is set (all 118 built HTML files have it).
- No Content-Security-Policy meta exists, so nothing to allow-list. No privacy section exists on /about/ or /disclosure/, so no wording change was made.

## 2026-10-23 (3:30 PM CT) — Branded email header image for the Kit confirmation email
- Added static/img/email-header.png (1200x360, shows at 600x180; ~70 KB), deployed at /assets/img/email-header.png. It shows the radar logo (rendered from favicon.svg with cairosvg), a "BotsDoThat" wordmark in Inter ExtraBold, the line "The BotsDoThat Weekly" in teal, and a teal-to-violet underline on the dark gradient. Generator script: /workspace/tools/email_header.py.

## 2026-10-23 (2:42 PM CT) — Fix: Kit "quarantined" signups now go to Kit's security check
- Bug: Kit's bot protection sometimes answers a form POST with `{"status":"quarantined","url":"https://app.kit.com/forms/guards/…"}`. That page is a reCAPTCHA check, and the subscriber isn't added or emailed until it's passed. Our JS treated this as an error ("That didn't work…"), so no confirmation email was sent. Reproduced in headless Chrome on the live /newsletter/ page.
- Fix (static/app.js): on `quarantined` with an app.kit.com URL, show "One more step…" and send the visitor to Kit's check page. Success and error handling are unchanged.
- A curl test POST (multipart, Accept: application/json) returned `status: success`, so the request format, endpoint and field name were already correct.

## 2026-10-23 (news update, 2:30 PM CT)
- Added 3 items (all Oct 23, notable): Kimi K3.1 Pro from Moonshot (open model with 1M-token context, API $2 / $10 per MTok, weights due by Nov 4; benchmarks are Moonshot's own; source TNW plus the Kimi blog), Cursor computer use (the desktop agent can click and type in other apps; source @cursor_ai on X plus AlphaSignal), and NVIDIA Nemotron 3.5 Bolt E4B 4GB (small free local model for device assistants; source the Hugging Face model card). Added Moonshot, Cursor and NVIDIA to NEWS_CO in scripts/build.py.
- X refresh: re-measured all 36 tracked posts (research/x_news_measure_2026_10_23_pm.json.txt, apply script research/news_x_2026_10_23_pm.py). Top story is still Claude Duet. Trending is now DeepInfer, Kimi K3.1 Pro and Claude auto mode default.
- No major release and no pricing changes from tracked providers (Moonshot isn't in the pricing table). Checked with nothing new: OpenAI API changelog, Gemini API changelog, xAI release notes, Anthropic newsroom, Mistral news, DeepSeek docs, Groq blog. Skipped: MiniMax M3.1 Flash open weights (outside tracked labs, low engagement), Anthropic Mythos 5 incident analysis (safety research), OpenAI storage/training-security engineering posts, Gemini small-business tools (Oct 20, before this window), iFlytek Spark-X2.6, Simular Agent S4 and General Reasoning RLCR (research).
- BACKLOG: added a "News run 2026-10-23 PM" section (Nemotron Bolt for the local-models guide, a Cursor app-testing idea, Moonshot pricing once the weights ship).
- Checks: validate 0 errors; build 116 pages + 404; check_links 0 broken internal.

## 2026-10-23 (2:04 PM CT) — Newsletter signup wired to Kit (double opt-in)
- config.json newsletter: form_action https://app.kit.com/forms/10088120/subscriptions, email_field `email_address`. Also records the provider and the hosted page https://botsdothat.kit.com/e874d57257.
- All 3 signup forms post there as plain HTML forms (no Kit JS): homepage, /newsletter/, and the issue page /newsletter/2026-10-22/. The footer only has links, no form.
- app.js submits with fetch (Accept: application/json) and shows "Almost done. Check your email to confirm your subscription." inline. Kit's error messages appear inline too. If fetch fails, the form falls back to a normal POST. Kit's CORS preflight allows any origin, checked with OPTIONS only; no email was submitted.
- Added a note under each form that a confirmation email is sent, and you're not subscribed until you click the link.
- Kit plan note: when the 14-day Creator trial ends without a card, the account continues on the free plan. It allows up to 10,000 subscribers; sequences and automations are paid-only. Sources: https://kit.com/pricing and https://help.kit.com/en/articles/16627071-the-kit-free-plan

## 2026-10-23 (12:28 PM CT) — Leftover time labels: blueprint setup times relabeled, title time promises removed
- Blueprint `setup_time` (12): "About N minutes (editor's estimate)" changed to "Rough setup time: about N minutes". validate.py now rejects an "editor's estimate" label in blueprint data.
- Use-case titles: dropped the unsourced time promises. Slugs and URLs are unchanged; titles, meta, OG, headings, search index and llms files were rebuilt from data.
  - prepare-for-a-doctor-visit: "Prepare for a doctor's appointment"
  - weekly-meal-plan-and-grocery-list: "Make a weekly meal plan and grocery list"
  - tailor-your-resume-to-a-job: "Tailor your resume and cover letter to a job"
- Run-for-less "token counts are our editor's estimates" note kept as is (Nik's call). It also appears in each blueprint's cost box.

## 2026-10-23 (12:45 PM CT) — Fix: use-case category chips, search and sort didn't update the cards
- Bug (reported by Nik): on /use-cases/, clicking a category chip highlighted it and updated the count ("8 of 82"), but all 82 cards stayed visible.
- Root cause: the JS filter hides cards with the HTML `hidden` attribute, but `.card{display:flex}` in style.css overrode the browser's default `[hidden]{display:none}`, so hidden cards still showed. Filtering logic, data-cat slugs and sort were correct.
- Fix: global `[hidden]{display:none!important}` in style.css (also protects news-page `.nt-grid` and any future component); chip selector scoped to `.chip[data-filter]`; build.py now adds a content hash (`?v=`) to style.css/app.js so returning visitors get fixed assets right away.
- Shipped inside deploy 1dcf067 (12:25 PM CT): the parallel time-saved job's `deploy.sh` (`git add -A`) picked up these edits while they were in progress (main e3dab69).
- Tested in headless Chrome (local + live), 1280px and 320px: all 9 chips × 3 sorts (visible cards = count text = category total, correct order, aria-pressed), search "email"/"calendar"/no-match × every chip, empty message, ?cat=&sort= URL params, news filters incl. back to All. 0 failures, 0 console errors, no horizontal overflow. Live site reproduced the bug before the fix (e.g. run-for-less: 82 visible, expected 8).
- Blueprints, homepage and trending have no client-side filters; news filters were already working.

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

- 2026-10-24: Added SaaSHub verification meta tag (deploy e96cb24); claimed and verified the SaaSHub listing (account botsdothat / hello@botsdothat.com). Listing still pending SaaSHub approval.

## 2026-10-27 (AM news update, 6:30 AM CT)
- News: added Riverside Agents (AI team that preps, edits, clips and posts videos and podcasts, Oct 26) and Ant Group LingGuang 2.0 (proactive personal agent, Oct 26). New companies Riverside and Ant Group added to `NEWS_CO` in build.py. No official X launch post found for either, so no X numbers.
- X: refreshed likes, reposts and views for 23 news items posted since Oct 19 (measured 2026-10-27). GPT-6.1 Terra's @OpenAI post is now 25.2K likes and 4.2M views.
- Checked OpenAI, Anthropic, Google/Gemini, xAI, Mistral and DeepSeek newsrooms and changelogs: nothing new since yesterday afternoon. No price changes, so the AI pricing table is unchanged.
- BACKLOG: logged a Riverside podcast/video use case and a LingGuang-style forgotten-subscription idea.

## 2026-10-27 (PM news update, 2:30 PM CT)
- News: added Google DeepMind Genie 4 (interactive world model, trusted testers only), Liquid AI LFM3 (open-weight 2B-class on-device models) and Microsoft MAI Image 2.7 Preview (image editing, #3 on Arena). All three marked notable. New companies Liquid AI and Microsoft added to `NEWS_CO` in build.py.
- X: recorded official launch-post numbers for all three (measured 2026-10-27). Genie 4's @GoogleDeepMind post had 9.0K likes and 762K views.
- Skipped: Claude "Fable 5.5" chatter (leaks and prediction markets only, no announcement). Checked OpenAI, Anthropic, Google, xAI, Meta, Mistral, DeepSeek and Groq: nothing else new since this morning. No price changes, so the AI pricing table is unchanged; no new everyday use case worth a BACKLOG entry.

## 2026-10-28 (AM news update, 6:30 AM CT)
- News: added Apple's AI assistant and MCP support for Pages, Keynote and Numbers (Oct 27, arrives in November for Creator Studio subscribers), Meta Muse launching in Singapore (Oct 27), OpenAI and Oracle's plan to bring Oracle apps into ChatGPT (Oct 27, Oracle AI Workspace not launched yet), and Anthropic's 40% Claude discount for US governments via GSA (Oct 27, minor). Apple added to `NEWS_CO` in build.py.
- X: Muse Singapore uses @alexandr_wang's post (1.7K likes, 114K views); Apple uses @twid's coverage post (844 likes, 50K views). No credible X post found for the Oracle or GSA items, so no X block. Refreshed numbers for 22 news items posted since Oct 21 (measured 2026-10-28): Genie 4's @GoogleDeepMind post is now 20.3K likes and 2.6M views, LFM3's @liquidai post 7.2K likes and 1.4M views, GPT-6.1 Terra 27.6K likes and 6.2M views.
- Skipped: Grok Bot outbound phone calls (only secondhand reports of a gradual rollout, no official post or doc yet) and the xAI "Grok Bot as a sales teammate" blog post (a how-we-use-it story, not a launch). No public price changes, so the AI pricing table is unchanged.
- BACKLOG: no new entry; the Apple MCP item makes "have your bot update a Numbers sheet or Keynote deck" possible from November, worth revisiting then.

## 2026-10-29 (AM news update, 6:30 AM CT)
- News: added Shopify's Fall '26 Edition agent shopping (shop.md skill for ChatGPT/Claude plus Shop Pay inside Muse, Claude Duet, Grok Bot and Instinct; Oct 28, notable), OpenAI's free API credits for ChatGPT Pro and Business (up to $500 a month; Oct 28, notable, pricing) and Grok API `guidelines` (Oct 28, minor). Shopify added to `NEWS_CO` in build.py.
- X: official posts recorded (measured 2026-10-29): @OpenAIDevs 7.4K likes / 1.4M views, @tobi 757 likes / 107K views, @grok 224 likes / 347K views. Refreshed numbers for 33 news items posted since Oct 21: Gemini 4 Carbon's @sundarpichai post is now 30.7K likes and 5.1M views, Claude for Legal 26.9K likes / 5.6M views, Genie 4 23.5K likes / 3.3M views.
- Skipped: Anthropic's drug-development and AI for Science posts (research programs, not products), Particle-1, Amp macOS Satellites, Rime Prism and Articul8 Bivia (developer or enterprise-only, single-source). No public model price changes, so the AI pricing table is unchanged.
- BACKLOG: logged a Shop Pay / shop.md shopping-agent guide idea.

## 2026-10-29 (daily QA, 7:00 AM CT)
Checks
- Live site: up. Homepage, /news/, /ai-pricing/, /use-cases/ (all guides) and three guide pages all returned 200 before and after the deploy.
- Internal links, anchors, assets: 0 broken (11,197 links scanned across 147 pages + 404); every same-page and cross-page `#anchor` points at a real id; every page has a viewport tag; 9 images, all with alt text, none broken.
- Outbound links (566 unique checked with HEAD, then GET with a browser user agent): no real breakages. All 91 YouTube videos exist (oEmbed 200); Hacker News 503s were rate limiting and all 29 threads load when checked slowly. ftc.gov and consumer.ftc.gov answer 404 to this box for every URL, including their homepages (bot block); web search confirmed 2 of the 4 FTC pages are live (job scams, Air AI settlement); the other 2 fail the same way as the FTC homepage, so treated as a block, not breakage. openai.com, help.openai.com, claude.ai, Product Hunt, Business Wire, investing.com and kit.com return 403/429 to scripts as usual; Retail Dive, RentCafe, NAIC, Digital Commerce 360, Oracle's blog, dev.meta.ai (500 to curl) and meta.com help (400 to curl) all loaded fine with a normal fetch.
- Real browser check (headless Chromium, local build and live site): no horizontal scroll at 320px or 1280px on 9 key pages, no broken images, no JS errors (the only console message locally is the Cloudflare analytics beacon refusing localhost, expected). Copy-prompt button copies the prompt and shows "Copied ✓". All-guides search and `?q=` links work.

Bugs fixed
- Homepage instant search was broken on the live site since Oct 23: the script built the search-index URL by stripping `assets/style.css` off the stylesheet link, but the link has carried a `?v=` cache-buster since e3dab69, so it fetched a garbage URL, got CSS back and showed nothing. Pressing Enter (the all-guides search) still worked. Fixed the pattern in `static/app.js`; verified live that "insurance denied", "shop pay" and "apartment" return results.
- If the search index ever fails to load, the homepage box now says "Quick search didn't load. Press Enter to search all guides." instead of failing silently with an unhandled promise error, and retries on the next keystroke.

Improvement for visitors
- New guide `let-your-ai-shop-for-you-with-shop-pay` (shopping): connect Shopify's Shop skill from shop.md to ChatGPT or Claude, or use Shop Pay inside Muse, Instinct, Claude Duet or Grok Bot, to find, check out and track orders, with you approving every purchase. Sources: Shop Help Center and Shopify's Fall '26 Edition (official), The Verge (Oct 13) and @benjaminsehl's launch post (X; 85 likes, 38.7K views, measured 2026-10-29). Watch-outs come from Shop's own help center (wrong prices possible, agent accepts store return rules for you, disputes may fail once you've approved, what gets shared). Now 107 use cases; X is 70 of 387 source links (18%).
- Added the Shop Help Center (one-time payment credentials at stores without Shop Pay) as a source on `pay-with-a-single-use-virtual-card`. BACKLOG item marked done; `ops/source-mix.md` updated.
- Deploy: 4ffd9c2 (main) / def914a (publish); GitHub Actions run succeeded.

## 2026-10-29 (weekly newsletter routine, 9:00 AM CT) — BotsDoThat Weekly #2
- Web issue live: https://botsdothat.com/newsletter/2026-10-29/ (also on /newsletter/ and /newsletter/feed.xml). Subject: "Let AI shop, plan and sort for you (it asks first)". Preview: "Four jobs to hand to AI this week, each with a prompt to copy, plus how to keep an agent away from files you care about." sent_on null.
- Items (all added Oct 27-29, none from issue #1): `let-your-ai-shop-for-you-with-shop-pay`, `add-an-ai-to-your-friends-group-chat-to-make-plans`, `organize-your-photos-by-asking`, `get-a-text-before-something-needs-doing`. New page: `keep-an-ai-agent-from-deleting-your-files`. Watch-out: `gemini-api-store-by-default`, under a new optional `watch_out_label` ("One setting to check"; default is still "One thing that went wrong"). No time-saved claims or stats.
- Sponsor check (Stripe live acct_1UTrztBgq3cPhA7u, 9:10 AM CT): 4 active Payment Links (featured, runforless, bundle, newsletter). 21 checkout sessions, all `expired` / `unpaid`, all created Oct 23 between 6:16 and 6:42 PM CT (our own checkout tests), and none has custom fields filled in. That includes two $0 newsletter sessions with the FIRST2 discount, both expired. 0 payment intents. No paid newsletter or bundle booking, so the issue uses the house ad to /advertise/. The house ad now shows code FIRST2 (build.py `nl_sponsor` reads `newsletter_promo_code`, so issue #1's web page also shows it).
- Email for Kit: `ops/newsletter/issue-2-email.html` (full), `ops/newsletter/issue-2-email-body.html` (body table only, for Kit's HTML block) and `ops/newsletter/issue-2-meta.txt`, made by the new `scripts/newsletter_email.py <issue number>`. It uses the site's dark palette with the indigo #7c8cff accent, the email-header.png header, table layout and inline CSS, and links carry UTM tags. It also has a web-version link, a footer with hello@botsdothat.com, and a note that Kit adds the unsubscribe link. Nothing was emailed.
- Deploys: web issue main 28d50b1 / publish b8f2f32; email files and changelog main b4e9565 / publish 2ee73ee. GitHub Actions run for b8f2f32 succeeded.
- newsletter issue ready, send approval needed
- The Monday report must ask Grok CEO to approve sending. Send only after both Grok CEO and Nik approve. Kit draft status will be added separately.
- Kit: draft broadcast 26680437 built (Text only template, HTML block, subject + preview set), not sent/tested/scheduled; sender pending confirmation as hello@botsdothat.com.

## 2026-10-30 (SEO agent, Nik approved in chat) — Newsletter #2 emailed
- Kit broadcast 26680437 ("Let AI shop, plan and sort for you (it asks first)") sent to all 4 subscribers from hello@botsdothat.com at 11:47 AM MT. Copies arrived in Gmail's inbox (Updates tab). Issue #1 stays an unsent draft.
- The Kit form "BotsDoThat Weekly signup" (10088120) now redirects after confirmation to https://botsdothat.com/newsletter/2026-10-29/ instead of Kit's default page. Double opt-in is unchanged.
- data/newsletter.json: issue 2 sent_on set to 2026-10-30. Not deployed yet; it goes out with the next deploy.
- Kit is on a Creator free trial (7 of 14 days left as of 10/30), so pick a plan before it ends.
