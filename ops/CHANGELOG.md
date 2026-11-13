## 2026-11-09 (AM news run, ~8:45 AM AST)
- Added 7 items: **chatgpt-dots-sign-in-codes** (2026-11-07, notable; dots fill email sign-in codes; @JamesZmSun), **meta-muse-spaces** (2026-11-06, notable; Meta Newsroom + TechCrunch/Verge; @Muse), **anthropic-agent-memory-dreaming** (2026-11-06, notable industry; "components of agent memory" engineering post; @AnthropicAI), **claude-code-cloud-auto-setup** (2026-11-06, notable; @ClaudeDevs), **chatgpt-sites-remix** (2026-11-06, minor; Business/Enterprise; @ChatGPT), **opencode-browse** (2026-11-06, notable agent launch; @opencode), **baidu-ernie-5-5-flash-base** (2026-11-05, minor; HF weights; coverage @ivanfioravanti). Added `OpenCode` and `Baidu` to `NEWS_CO`. No new MAJOR item.
- meta-muse-specialized-models X block switched to Zuckerberg's @finkd post (most-engaged; @AIatMeta kept under more_sources).
- Refreshed X on 85 existing + 7 new posts (92; measured_at 2026-11-09T12:34:06Z; raw research/x_news_measure_2026_11_09_am.json.txt, local only). Top story still **gpt-6-cyber**; hottest overall **claude-personal-finance**.
- Pricing: no official price change found; ai-pricing.json (checked_on 2026-11-03) due weekly refresh.
- BACKLOG: Muse Spaces self-updating tracker idea; OpenCode Browse / dot sign-in codes "agent in your logged-in browser" idea.
- Sync: first push was rejected because origin/main had the Nov 8 builder commits (3e36928 PR #1, 9b7ada1 publish) that local main lacked. Applied diff 19c370e..9b7ada1 onto local main (non-site files merged cleanly; site/ rebuilt), reset local publish to origin/main, then redeployed so the live builder is kept. test_bot_builder.py 38 OK.
- Deployed: local main `03bf3c7`, publish `7d62f08` (parent 9b7ada1), Actions run 42618345698 succeeded; live /news/ shows the new items, /bot-instructions/ 200.
- Skipped: OpenAI Devs "Tomorrow." teaser (ModRetro Chromatic merch drop, not AI); Elon Grok Bot "fixes underway" posts (no shipped change); GitHub Copilot Projects (Oct 28, old); Gemini file editing, Mistral Large 4 weights, Grok API watermark, Gemini Android Auto (already in file); Anthropic $3.4B generator deal / DeepSeek agent DAU / Apple Siri plans (reports, not launches); Baidu ERNIE Evolve, NVIDIA Lyra 2.0 (research).

## 2026-11-06 (PM news run, ~3:30 PM ET / ~2:30 PM CT)
- Added 5 items: **meta-muse-specialized-models** (notable, Active Memory/Focus via Muse Wonder training; @AIatMeta), **amazon-alexa-text-shopping** (notable, Alexa for Shopping over SMS invite rollout; @amazonnews), **google-antigravity-remote-agents** (notable, cloud remote agents + voice mode rollout; @antigravity — clearer Nov 6 public push after AM skipped the Nov 3 changelog start), **visa-agentic-commerce-benchmark** (notable industry, 57.2% pass / ~43% fail shopping runs; coverage @cuysheffield), **openai-hacktron-partnership** (minor, Daybreak Red security partnership; no X block). Added `Visa` to `NEWS_CO` in build.py. No new major (flagship) item.
- Refreshed X on 23 recent/major posts + 4 new announcing posts (27 measured; measured_at 2026-11-06T20:34:06Z; raw: research/x_news_measure_2026_11_06_pm_batch1.json.txt, local only). Top story still **gpt-6-cyber** (~20.1k likes / ~3.57M views) as hottest major ≤14 days; hottest overall engagement remains claude-personal-finance (~41.8k likes / ~9.19M views).
- Pricing: no `ai-pricing.json` change.
- BACKLOG: Alexa text-shopping confirmation watch-out; Visa benchmark reinforces shopping human-confirm guidance; Antigravity remote/voice as possible coding-agent note.
- Skipped: GPT-6.2 Astra/Sol leaks (rumor); Meta Muse "Spaces" (TechCrunch only, no clear Meta product page — may overlap specialized-models demos); METR Anthropic pace report / Oumi FAiE / Quest / Ant Ling 3.2-flash (secondary or already covered angles); OpenAI ChatGPT analytics rumor.
- Deployed: local main `f8fe920` (news `52b652d` + changelog), publish `57a467d` (news `3412d88`), Actions runs 42289603338 / 42289709904 succeeded; live /news/ 200.

# Ops changelog

## 2026-11-06 (midday trending, ~1:10 PM ET / noon CT)
- Added `ask-claude-about-your-own-spending` (Claude Personal Finance US beta via Plaid; read-only; inbox). Sources: Claude article, Help, Verge, Plaid, Engadget, HN 50382192 (11/10). Not framed as deal/bill-cutting.
- Extended `practice-a-job-interview-out-loud` with Meta Muse voice + full-screen avatar (Meta newsroom 2026-11-05, Verge, TNW).
- Updated `make-a-customer-service-call` and `call-and-book-by-phone` for native Grok Bot US phone calls (TeslaNorth, Teslarati); kept bill-negotiation demos out of framing.
- Refreshed popularity on 49 tracked X posts. Mentions/feedback of BotsDoThat: none. Bugs: none.
- Source mix after run: 123 use cases, 497 source links, X 74/497 = 15% (community 29%).
- Deployed: local main `9a59b57`, publish `d99c37c`. Push Actions 42268633847 / 42269798102 hit transient Pages failures (build OK); workflow_dispatch 42270368813 succeeded. Live: /use-cases/ask-claude-about-your-own-spending/ 200.


## 2026-11-06 (daily QA, ~7:00 AM CT)
Checks
- Live site up: `/` `/news/` `/use-cases/` `/ai-pricing/` `/trending/` and sample use-case pages all HTTP 200. validate: 122 use cases, 12 blueprints, 0 errors. build: 168 indexed pages + 404. check_links: 13,493 links scanned, 0 broken internal (960 unique external; not run with `--external` this run).
- Headless Chrome at 320px on home, news, use-cases, ai-pricing, trending, and 2 guides: no horizontal overflow, no JS pageerrors, images load after lazy scroll (0 broken). Homepage instant search loads `/assets/search-index.json` (200) and finds the resignation guide; `/use-cases/?q=resignation` shows "1 of 122 use cases"; copy-prompt button flips to "Copied ✓". Viewport meta present. All 68 `<img>` tags have `alt` (decorative ones empty). No bugs found in `static/app.js`.

Bugs fixed
- None.

Improvement for visitors
- `restaurant-reservations-by-agent` and `book-an-appointment-with-an-ai-agent`: added a watch-out that agents can report a booking as done when it never went through (Eon 19-model false-"done" finding), plus a See also link to `make-your-agent-prove-it-finished-the-job`. BACKLOG "did it really happen?" item marked done. last_checked set to 2026-11-06.

Deploy
- local main `d338009` (QA `fb7e0ad` + changelog), publish `6ec644a` (QA `354bcd1`), Actions runs 42223871811 / 42224496710 succeeded; live restaurant guide shows the new Eon watch-out.

## 2026-11-06 (AM news run, ~7:30 AM ET / CT)
- Added 6 notable items (all dated 2026-11-05, missed by the Nov 5 PM window): **claude-personal-finance** (Anthropic US beta via Plaid; @claudeai), **meta-muse-voice-avatars** (Meta Muse voice + expressive avatars; @alexandr_wang), **perplexity-teammates** (always-on Max work agents; @perplexity_ai), **cursor-build-live-apps** (cloud agent builds/deploys shareable apps; @cursor_ai), **mistral-studio-managed-agents** (Studio managed agents/apps; @MistralAI), **thinking-machines-inkling-2-small** (594B MoE / 17B active on Tinker; @thinkymachines). Added `Thinking Machines` to `NEWS_CO` in build.py. No new major (flagship) item.
- Refreshed X on 46 recent posts (measured 2026-11-06T12:31:45Z; raw: research/x_news_measure_2026_11_06_am_batch{1,2}.json.txt, local only). Top story still **gpt-6-cyber** (~18.1k likes / ~2.89M views) as hottest major ≤14 days; hottest overall engagement is claude-personal-finance (~34.8k likes / ~6.33M views) → Trending #1.
- Pricing: no `ai-pricing.json` change (no listed text-API price changes; Inkling Tinker pricing and Omni video $/sec stay outside the table).
- BACKLOG: Claude Personal Finance spending Q&A idea; Muse voice interview-rehearsal idea; Cursor/Perplexity noted as paid/dev-leaning.
- Skipped: GPT-6 Cyber / Omni 1.2 Flash / Conductor / Pierre (already listed); Anthropic Claude Enterprise security center (enterprise admin); Google Antigravity Remote Agents (changelog start Nov 3, not a clear Nov 6 launch); Baidu ERNIE 5.5 Flash Base, Planet satellite AI, Glasshand, Rerun (niche/single-digest); Genie 4 already listed.
- Deployed: local main `a086159` (news `c55674a` + changelog), publish `e365834` (news `0f78833`), Actions runs 42218612508 / 42218872218 succeeded; live /news/ 200. Top story still gpt-6-cyber; Trending #1 claude-personal-finance.


## 2026-11-05 (PM news run, ~3:30 PM ET / ~2:30 PM CT)
- Added 5 items: **gpt-6-cyber** (major, OpenAI Daybreak Red security model), gemini-omni-1-2-flash (notable, 15s video + 30% cheaper), openai-linux-lpe-pipeline (notable, 948 Linux LPE exploits + patches), meta-acquires-conductor (notable), openai-acquire-pierre (notable, no X block — no strong official post).
- Refreshed X on 93 posts (measured 2026-11-05T20:35Z). Top story is now gpt-6-cyber (~10.2k likes / ~0.90M views) as hottest major ≤14 days; Carbon still higher absolute engagement (~34.1k likes / ~6.95M views) but outside that window ranking.
- Pricing: no `ai-pricing.json` change (Omni is video $/sec, not in text API table; GPT-6 Cyber is restricted Daybreak pricing).
- BACKLOG: logged Omni video guide idea + skipped candidates.
- Deployed: local main `b56e1fc` (news `f1222c2` + changelog), publish `dec13ae`, Actions runs 42104182841 / 42104333902 / 42104526932 succeeded; live /news/ 200, GPT-6 Cyber is Top story.

## 2026-11-04 (daily QA, ~9:10 AM AST)
Checks
- Live site up (homepage 200 in 0.24s). validate 0 errors; build 161 indexed pages + 404; check_links 12,960 links, 0 broken internal.
- Outbound links (743 unique hrefs, GET with a browser user agent): no real breakages. 70 non-2xx are the usual bot blocks/rate limits (403/405/429, FTC, X); only U.S. News and two Business Wire pages timed out, as in earlier runs.
- Headless Chrome on the live site, all 163 pages at 320px: no horizontal scroll, no JS exceptions, no failed requests, no broken images. All-guides search `?q=resignation` shows "1 of 119 use cases"; copy-prompt button shows "Copied ✓".
- No bugs found, so no fixes needed.

Improvement for visitors
- New guide `understand-your-tax-forms-with-ai-safely` (inbox, Easy), from the BACKLOG autocomplete item "can ai fill out tax forms": use AI to explain forms and build a checklist and question list, with personal details stripped, and file with tax software or a pro. Sources: NYT (Mar 5, 2026, chatbots off by over $2,000 on average), NerdWallet, CBS News, IRS Taxpayer Advocate Service, IRS Topic 254. Now 120 use cases. BACKLOG item marked done.

## 2026-11-04 (AM news run, ~8:45 AM AST)
- Added 3 news items: Tencent Hy4 open-weight model with vision (Nov 4, notable, @TencentHunyuan official post), Netflix AI Discover mood-based tab (Nov 3, notable, @YahooFinance coverage), Google Guided Learning in Classroom/Search plus Gemini off by default for K-12 student accounts (Nov 3, notable, @Marie_Haynes coverage). Tencent and Netflix added to `NEWS_CO`. No major releases.
- Refreshed X engagement on 82 existing items (measured 2026-11-04); Gemini 4 Carbon (34,092 likes / 6.93M views) still top story.
- Skipped: Claude Enterprise "smart reports / group budgets" (single unofficial source), monday.com-in-Gemini connector (partner blog only), XPENG GroundingPI (research). Checked OpenAI changelog, Anthropic, Google, xAI, Meta, Mistral, DeepSeek: nothing else new. No pricing table changes (Hy4 not in table).
- BACKLOG: logged a "pick a movie by mood" idea.

## 2026-11-03 (PM news run, ~4:45 PM AST)
- Added 3 news items: OpenAI "engineering for the physical world" (notable), Anthropic FlashProve provable inference (notable), xAI Grok Bot Data Bot (notable, agent launch). No major releases.
- Refreshed X engagement on 79 existing items (measured 2026-11-03); new items carry official-post X blocks (@OpenAI, @AnthropicAI, @bot).
- No pricing changes; ai-pricing.json untouched. BACKLOG PM section added.

## 2026-11-03 (SEO on-site fixes from the traffic research, ~2:15 PM CT; asked via the SEO agent after Nik's "get more traffic" request)
From the GSC export Oct 22–Nov 1 (446 impressions, 3 clicks) and ops/drafts/traffic-research-2026-11-03.md, items #1, #2, #3, #7, #10. Item #6 is left for the weekly run.
- #1 Titles and descriptions for zero-click pages. New optional use-case field `seo_description` (build.py uses it before the generated description). Blueprints now also accept `seo_title` and `seo_description`.
  - add-events-and-reminders-by-asking-your-bot: "Add calendar events and reminders just by asking your bot" -> "Add calendar events and reminders by asking AI (Grok, Gemini)"
  - practice-speaking-a-new-language: "Practice speaking a new language out loud with AI" -> "Practice speaking a new language with an AI voice partner"
  - weekend-family-activities: seo_title "AI weekend activity ideas that fit your kids and weather" -> "Weekend ideas for kids, matched to the weather by AI"
  - control-your-smart-home-with-a-private-ai: "Control your smart home by talking to a private AI" -> "Private AI voice control for your smart home (Home Assistant)"
  - hire-a-chief-of-staff-bot: "Set up a “chief of staff” bot that plans your other bots" -> "AI chief of staff: one bot that plans which bots you need"
  - let-chatgpt-run-your-icloud-mail-and-calendar: seo_title "ChatGPT with iCloud Mail and your iPhone calendar" -> "ChatGPT for iCloud Mail and iPhone Calendar: how to set it up"
  - /news/: "Latest in AI: new models and AI agent launches, explained" -> "AI news this week: new models and AI agent launches, explained"
  - Each use case above also got a hand-written seo_description (all 155 characters or fewer).
- #2 compare-two-documents: "Compare two versions of a document or contract" -> seo_title "What tool can compare two versions of a contract?" plus seo_description. New optional `compare_table` field, rendered as "Which tool should you use to compare two contract versions?". Rows: Word Compare (Microsoft Support), Google Docs Compare documents (Google Docs Editors Help, added to sources) and ChatGPT/Claude/Gemini/Grok. last_checked set to 2026-11-03.
- #3 New guide /can-ai-make-phone-calls-for-you/ ("Can AI make phone calls for you? What works and what it costs"). Contents:
  - Answer-first lead, then what AI can do on the phone, which agents can call (Grok Bot with a calling add-on, Meta Muse, Instinct, Cue by Manus), and per-minute costs.
  - A "What goes wrong" section, 6 FAQs (FAQPage JSON-LD) and a sources list.
  - Linked from the cost guide, /what-can-bots-do/ and the 4 phone use cases (call-and-book-by-phone, make-a-customer-service-call, let-a-bot-answer-and-screen-your-calls, restaurant-reservations-by-agent). It is also in NEW_GUIDES, so it appears in search and llms.txt.
  - /blueprints/phone-call-bot/: "Phone Call Bot: a bot blueprint" -> "Phone call bot: have AI make calls and book for you", plus seo_description.
- Voice prices: new `voice_platforms` list in data/ai-pricing.json, from official pricing pages checked 2026-11-03. validate.py now checks its source_url and checked_on.
  - Retell AI pay-as-you-go: $0.07–$0.31/min; voice engine $0.055/min; US Twilio calls $0.015/min; number $2/mo. Source: https://www.retellai.com/pricing
  - Bland Start: $0.14/min with the model, STT and voices included; $0 platform fee; transfer $0.05/min. Source: https://www.bland.ai/pricing
  - Vapi pay as you go: $0.05/min hosting, with providers billed at cost on top; Vapi's own calculator shows $82–$129 for 1,000 min. Source: https://vapi.ai/pricing
  - Re-verified the existing `voice` rows on their official pages: xAI grok-voice-3.0 $0.08/min, OpenAI gpt-live-1 $0.05/min, Mistral Voxtral 3 voice agent API $0.04/min.
- #7 /what-can-bots-do/:
  - Title "What is an AI agent? Simple terms, vs. chatbots" -> "What is an AI agent, and what can it do for you?".
  - The lead now gives personal-use examples.
  - New #personal-use section with 10 linked examples. The meta description has a computed count.
- #7 /ai-agent-examples/:
  - Title "{n} AI agent examples for everyday life" -> "{n} AI agent examples for personal use and everyday life". The count is still computed (119 today); the "115" in search results was Google's cached copy.
  - New answer-first lead.
  - New FAQ "What are examples of AI agents for personal use?".
- #10 Cost guide:
  - Answer-first lead for a personal bot (computed API range plus per-minute voice range, noting the lowest is a hosting fee).
  - Description now starts "What a personal AI agent costs per month".
  - #voice renamed "AI voice agent cost per minute and per month", with a platform table (per minute, one 5-min call, 20 min/month, 300 min/month, what the price covers, source and date) and the voice-model list kept under it.
  - Voice FAQ updated; new FAQ "How much does an AI phone call cost per minute?".
- Homepage: only the computed "linked sources" count changed (408 -> 409). No layout change. Untouched: /advertise/, sponsor_checkout, X.
- Drafts only, nothing submitted (gitignored ops files):
  - ops/launch_drafts.md draft A now targets alvinreal/awesome-openclaw (the old URL redirects there).
  - New section E there with free directories only (ToolDirectory.ai, toolhype.dev, Future Tools, Nukkadly, AlternativeTo; SaaSHub pending). TAAFT ($49), Futurepedia (no public form) and Toolify ($99) were dropped.
  - growth-plan.md and content-calendar.md point to it.
- Checks: validate 0 errors; build 161 pages; check_links 0 broken internal.

## 2026-11-03 (Starter Pack signup wording, deployed ~1:35 PM CT, approved by Nik via chat)
Deployed after Kit form 10088120's confirmation email was confirmed to deliver StarterPack.pdf (Download incentive).
- scripts/build.py: new NL_PACK_* constants. `newsletter_box()` copy for every signup box (homepage, /newsletter/, issue pages, end-of-article, mid-article, hub and sidebar cards):
  - Full/end variant: "Get the free Starter Pack: 7 AI agents you can put on a schedule", with a line naming ChatGPT, Claude, OpenClaw and Hermes Agent, the power-user bonus, and asks-before-sending/buying/deleting. Button "Send me the Starter Pack".
  - Mid-article (`nl-mid`) and sidebar card variant: "Free Starter Pack for subscribers", so the 6 long guides never show two identical box headings.
  - Note under the form: "We'll email you a confirm button. Click it to confirm and get your Starter Pack."
- Use-case pages: the nl-pointer line now mentions the free Starter Pack (7 setups plus a power-user bonus).
- /newsletter/:
  - Hero lead mentions the pack.
  - New section #subscriber-extras, "What subscribers get that the site doesn't" (the pack's 7 setups, the bonus, prompts and steps for 4 tools, the safety rule, arrives on confirm).
  - New FAQ "What is the Starter Pack, and how do I get it?" (FAQPage JSON-LD stays valid).
  - Meta description mentions the pack.
- llms.txt newsletter line mentions the pack. static/app.js success message: "Almost there: check your inbox and click Confirm to get your Starter Pack."
- Left out on purpose: the weekly subscriber-only extras and "first word" bullets from signup-copy.md (not built yet, so the site doesn't promise them).
- Untouched: homepage layout, /advertise/ (only the global app.js cache-bust hash changes), sponsor_checkout, X.
- Drafts: ops/drafts/starter-pack/starter-pack.md and .pdf gained "8. Bonus for power users: the self-improving ops desk (Hermes Agent)", with sources. The PDF was copied to /workspace/StarterPack.pdf for the Kit upload.
- Checks: validate 0 errors; build 160 pages; check_links 0 broken internal.
- Subscriber-only fix (approved): added `ops/drafts/` to .gitignore and ran `git rm -r --cached ops/drafts/`. The files stay on disk, but the next deploy stops publishing them.
  - Caveat: the 7-setup PDF the midday deploy pushed (25ab406) is still in public git history, so the old version can still be downloaded from that commit.
  - kit-setup.md size note updated to about 0.32 MB.

## 2026-11-03 (Agentic rework of 14 chat-prompt use cases + hub notes, ~9:45 AM CT, asked by Nik in chat)
The 14 chat-prompt use cases from the Oct 28 backlog proposal (the 12 migrated Oct 19 pages plus the two letter pages added Oct 20-21; every tool was a plain chat app).
Rewritten as agent tasks (same slugs; new steps, prompt, tool notes, setup, FAQ "Which AI tools can do this?"; every product claim cites an official help page):
- `understand-a-confusing-letter`: reads the letter from a photo, Google Drive PDF or Gmail; asks first, then puts the deadline on Google Calendar; sends an email reply only after approval. New title "…and let AI handle the next step", seo_title "Understand a confusing letter with AI, then act on it". Notes that Claude's Gmail connector sees attachment names only.
- `appeal-a-health-insurance-denial`: reads denial/EOB from a Drive folder, adds the appeal deadline (+1 week-before event) after you OK it, writes the appeal and a call log as Google Docs; you send it the way the plan asks. Guide steps 1, 2 and 5 updated to match.
- `write-a-complaint-that-gets-fixed`: searches Gmail for order and support emails, builds a dated timeline, drafts the complaint and sends it only after approval; adds the deadline to the calendar. See also: let-ai-send-emails-for-you, make-a-customer-service-call.
- `moving-checklist-and-change-of-address`: Claude finds every company with your address in your email and puts utility dates on the calendar; ChatGPT Work's cloud browser fills in address-change pages, pauses for sign-in and asks before it saves; USPS left to you on usps.com.
- `organize-a-parents-care-paperwork`: Claude reads a Drive folder of scans and PDFs, builds a care binder Google Doc with sources per fact and a call log, and adds appointments after you OK them. See also: medication-reminders-for-a-parent.
- Sources added: Claude Help "Use Google Workspace connectors", OpenAI Help "Using cloud browser in ChatGPT", "Managing app permissions in ChatGPT", ChatGPT release notes. Tools now carry notes on who can do which step (Gemini/Grok/ChatGPT free = explain and draft only).
Labeled "Chat prompt" (an honest agentic version would just duplicate an existing page). New optional field `chat_prompt: {"agentic_alt": slug}`; build.py shows a "Chat prompt" badge on the page header, on cards and in /ai-agent-examples/, plus a note above the steps pointing to the agentic page:
- `fill-out-a-long-form` → hand-a-clunky-web-form-to-an-agent
- `review-a-lease-before-signing` → understand-a-confusing-letter
- `prepare-for-a-doctor-visit` → prescription-ready-and-time-to-leave
- `homework-help-that-teaches` → school-email-digest
- `tailor-your-resume-to-a-job` → job-match-digest
- `sell-your-stuff-online` → sell-on-marketplace-with-rules
- `test-a-side-hustle-idea` → get-a-researched-report-with-sources
- `write-a-letter-of-recommendation` → email-ghostwriter-style-guide
- `write-a-resignation-letter` → let-ai-send-emails-for-you
/use-cases/ vs /ai-agent-examples/
- /use-cases/: title "AI agent use cases you can copy and run, step by step"; new description; note under the lead: "Each use case is a step-by-step page you can copy and run… Want a quick overview first? AI agent examples puts everything agents can do on one page, grouped by part of life. Pages marked Chat prompt are one-off prompts…"
- /ai-agent-examples/: title unchanged; description now "…on one page, grouped by inbox, calls, shopping, travel, family, health and work. Each links to a how-to."; note: "This page is the one-page overview of what AI agents can do, grouped by part of life. To set one up, open its step-by-step page, or search and filter all of them in use cases…"
- CSS: .chat-badge, .chat-note, .hub-note in static/style.css (appended). BACKLOG.md: both Oct 28 proposals marked done.
- Deployed with scripts/deploy.sh at ~9:43 AM CT: main 29b81d2, publish 4abd7d6, GitHub Pages run 41666837834 success. Live check: /use-cases/, /ai-agent-examples/ and the rewritten and labeled pages return 200 with new titles, notes and badges; CSS live. (This line is committed with the next deploy.)

## 2026-11-03 (SEO improvement pass, ~9:30 AM CT, asked by Nik in chat)
Audit (all 159 built pages: titles, descriptions, H1s, heading order, image alt, canonicals, JSON-LD parse, sitemap, llms.txt, in-content links)
- Clean: one H1 per page, canonical on every page, every JSON-LD block parses, no image without alt, no heading-level skips, no duplicate titles or descriptions, every indexed page in the sitemap.
- Fixed: 8 use-case titles were 63-65 chars (cut off in Google). Added keyword-first `seo_title` (51-57 chars) to plan-your-day, daily ads/sales report, prescription-ready, weekend activities, team of agents, people-search removal, shared Apple account, scanned paper mail.
- Fixed: /about/ meta description was 83 chars; now a full sentence about how use cases are found, measured and sourced.
- llms.txt: added the newsletter, a link to each of the 8 category hubs and the past newsletter issues (were missing). llms-full.txt: each use case now includes its FAQ answers (31 use cases have them).
Internal links (build.py)
- Every use-case page: "New to this?" line now links "what an AI agent is, in simple terms" (/what-can-bots-do/ was linked from only 6 pages' content) before the no-code guide; pages that list OpenClaw or Hermes Agent as a tool link the OpenClaw vs Hermes guide.
- Use-case sidebar "More in <category>" box: added "All <category> use cases →" (category hub) and "Every AI agent example on one page →" (/ai-agent-examples/ was linked from 3 pages' content).
Newsletter signups
- Use-case pages: one-line pointer under the copy-paste prompt, "Want one new job like this each week, with a prompt to copy? Get the free BotsDoThat Weekly email" → /newsletter/ (was linked from 3 pages' content; existing sidebar card and end-of-page form unchanged).
- Long guides (cost, no-code, OpenClaw vs Hermes, email safety, what is an AI agent, AI agent examples): added a mid-article signup (existing newsletter_box, inline variant, after the 3rd section) in addition to the end form. New NL_MID_PATHS + _insert_mid in build.py.
New pages (Google autocomplete pulled Nov 3; neither duplicates an existing page)
- `let-ai-send-emails-for-you` (inbox, Easy), title tag "Can AI send emails for you? ChatGPT, Claude and Gemini". Targets "can chatgpt send emails for me / on my behalf", "can claude send emails for me", "can gemini send emails for me", "can ai agents send emails". Approve-before-send prompt, setup (official connect buttons, permission settings, drafts-only option), watch-outs, 4-question FAQ. Sources: OpenAI release notes + app permissions help, Claude Google Workspace connectors help, Gemini Apps tasks help, TechRadar hands-on (Jun 9, 2026; no attachments), Tatsulok comparison (Oct 14, 2026), Google suggestions. No stats.
- `set-up-chatgpt-scheduled-tasks` (work, Easy), title tag "ChatGPT scheduled tasks: ideas and how to set one up". Targets "chatgpt scheduled tasks ideas / examples / free / not working", "how to schedule chatgpt tasks". Plan limits (3 Free/Go, 5 Plus, 10 Business/Edu, 15 Pro/Enterprise), notification setup, why tasks pause, shared-link privacy, Pulse retirement, 5-question FAQ. Sources: OpenAI scheduled tasks help + release notes (Jun 17, Aug 25, 2026), Claude Cowork scheduling help, XDA and MakeUseOf hands-ons, 2 r/ChatGPT threads, Google suggestions. No stats.
- Now 118 use cases; source mix X 73/455 = 16% (both new pages use 0 X links).
- Deployed with scripts/deploy.sh at ~9:35 AM CT: main 61de7a6, publish a934e61, GitHub Pages run 41665358379 success. Live check: both new pages 200 with new titles, nl-pointer and mid-article signups live, new seo_titles and /about/ description live, both pages in sitemap. (This line is committed with the next deploy.)

## 2026-11-03 (Weekly SEO + AI-answer run, ~7:45 AM PT)
Audit (titles, descriptions, H1s, canonicals, JSON-LD, sitemap, robots.txt, llms.txt)
- 157 pages: no duplicate titles or descriptions, one H1 per page, canonical on every indexed page; robots.txt allows search + AI crawlers and points to the sitemap; llms.txt/llms-full.txt and sitemap include the new page. Descriptions already capped at 155 chars by mdesc (the 160+ hits were HTML entities).
- Fix: 4 use-case titles were 76-87 chars and truncated in Google. New optional `seo_title` field (build.py) used for the shopping-list photo cart, IFTTT plain-words, AI coach and ChatGPT + iCloud Mail guides.
New / improved pages (Google autocomplete pulled Nov 3: "ai agent to book flights", "can chatgpt book flights", "can ai agents book flights", "ai voice agent cost per month", "personal ai agent cost")
- New `book-a-flight-with-an-ai-agent` (travel, Medium), title tag "Can an AI agent book flights for you? How to do it safely": short answer up top, 5 steps, copy prompt with stop-before-payment, setup, watch-outs, 3-question FAQ (FAQPage + HowTo JSON-LD). Sources: OpenAI Help (cloud browser), Google blog (AI Mode travel), HN 49904198 (Dots trip review), HN 50174185 (Show HN flight booking in Claude), Travel Distribution News. 0 X. BACKLOG item closed.
- Cost guide: 2 new FAQ answers (on page, FAQPage JSON-LD and llms-full.txt) for "How much does an AI voice agent cost per month?" (300-minute example from the official per-minute prices) and "How much does a personal AI agent cost?" (plan range computed from the consumer price table).
- Source mix: 116 use cases, X 73/440 = 17% (ops/source-mix.md).
AI price refresh (all rows re-checked on official pages Nov 3; checked_on = 2026-11-03)
- Unchanged: OpenAI (gpt-6-astra, 6.1-sol, 6.1-terra, 6-luna, GPT-Live), Anthropic (Fable 5.1, Opus/Sonnet/Haiku 5.5), Google (4 Argon, 3.8 Flash, 3.1 Flash-Lite), xAI (grok-4.7, 4.3, voice), Groq, Mistral (Large, Large 4, Voxtral 3), Meta Muse Wonder, DeepSeek.
- Added: gemini-3.5-flash-lite $0.30 / $2.50 (cached $0.03); Gemini 2.5 Flash-Lite calls redirect to it from Dec 1.
- Plans: Claude Max is now $100 (5x) and a separate Claude Ultra is $200 (10x weekly, no 5-hour limit, $200 API credits); was "Max from $100, 5x or 20x". Google AI Plus $4.99 and AI Pro $19.99 a month are now shown in USD on gemini.google, so added and removed from "not verified". ChatGPT plan prices and SuperGrok still not shown on official pages (stay unverified).
- Blueprint cost notes and the cost guide are computed from the table at build time, so they follow automatically (blueprint models unchanged in price).
AI answers / analytics
- Citation checks: no direct access to ChatGPT, Perplexity, Google AI Overviews or Grok answers from this box; a web-search engine check for "how much does it cost to run an AI agent per month" and "how to build an AI agent without coding" did not cite botsdothat.com. The site is indexed for brand queries.
- Search Console and Cloudflare analytics: not accessed this run; no numbers reported.
- Checks: validate 0 errors (116 use cases); build 157 indexed pages + 404; check_links 12,082 links, 0 broken internal.
- Deploy: main cc21c29 / publish 10c018c; GitHub Actions run 41662208153 succeeded (7:17 AM PT). Live 200: /, new flight guide, cost guide (new FAQs present), /ai-pricing/ (Claude Ultra row present). This deploy line is committed with the next deploy.

## 2026-11-03 (News update, AM, ~7:40 AM ET)
- Added 3 items: `google-dreambeans-india` (Nov 3, minor, feature; Google India blog, TechCrunch, The Hindu; no x block, only low-engagement coverage), `gemini-2-5-auto-route-december` (Nov 2, notable, pricing; Gemini API changelog + deprecations; no x block), `apple-watch-live-rewind-siri-recap-beta` (Nov 2, notable, feature; TechCrunch, Apple Support, Engadget; no x block, top posts under 5 likes).
- X: re-measured 79 posts, measured_at 2026-11-03; raw research/x_news_measure_2026_11_03_am.json.txt (local), script research/news_x_2026_11_03_am.py. Top story unchanged: Gemini 4 Carbon 34,093 likes / 2,750 reposts / 6.91M views. No MAJOR release.
- Pricing: no table change (no Gemini 2.5 rows in the table). BACKLOG: Apple Watch recap use-case idea; Gemini 2.5 auto-route note for cost pages.
- Skipped: Claude message threads (already covered Nov 2), OpenAI Grid Protectors (energy policy), Anthropic amended S-1 (already covered), NYT v. Brave lawsuit, Squarespace/SUSE layoffs, Garry Tan token spend, GPT-Rosalind-6 (trusted access only), Hydrogen-1.0 (developer science model), enterprise agent press releases (Aion, Sequel, Abacum, Tripo, 10x), markets news, a mis-dated "Grok 4 released" aggregator entry.
- Checks: validate 0 errors; build 156 indexed pages + 404; check_links 11,994 links, 0 broken internal.
- Deploy: main b78dacf / publish 73b061a; GitHub Actions run 41635612757 succeeded in 23s (7:26 AM ET). This deploy line is committed with the next deploy.

## 2026-11-02 (News update, PM, ~3:30 PM ET)
- Added 6 items, all dated 2026-11-02: Claude API message threads beta (Claude Platform release notes; @ClaudeDevs), OpenAI LifeVal everyday-tasks eval (openai.com; @OpenAI), Meituan LongCat-2.5 (LongCat API changelog; @Meituan_LongCat), SemiAnalysis GDPx benchmark (SemiAnalysis; @SemiAnalysis_), ChatGPT Chat+Work tab merge and ChatGPT Classic retiring Jan 30, 2027 (TechCrunch, 9to5Mac; @9to5mac), Claude watermark extended to Mythos 5 / Opus 4.7 / Opus 4.6 / Sonnet 4.6 from Nov 3 (Mashable, Claude Help Center; no X post).
- build.py NEWS_CO: added Meituan and SemiAnalysis.
- X: re-measured 79 posts (74 existing refreshed + 5 new), measured_at 2026-11-02; raw file research/x_news_measure_2026_11_02_pm.json.txt (local, gitignored); script research/news_x_2026_11_02_pm.py.
- Top story unchanged: Gemini 4 Carbon (major, Oct 28), 34,089 likes / 2,750 reposts / 6.90M views. No MAJOR release this run.
- Pricing: no change to data/ai-pricing.json. BACKLOG: LifeVal chores as use-case ideas, GDPx watch-out, Chat+Work/Classic guide updates.
- Checks: validate 0 errors; check_links 11,986 links, 0 broken internal.
- Deploy: main 4960b80 / publish 627fe47; GitHub Actions run 41519811834 succeeded (3:31 PM ET). Live: /news/ 200 with the new items. This deploy line is committed with the next deploy.

## 2026-11-02 (Trending watch, midday)
- New: `turn-a-photo-of-your-shopping-list-into-a-cart` (shopping, Easy): photograph a handwritten list or export it from Notes and Walmart's Sparky turns it into a cart matched to your usual store and past purchases; you check every line and pay yourself. Sources: Walmart newsroom (Oct 30), PPC Land (Oct 30), Winning With Walmart, Market & Tech (Nov 2), Hip2Save hands-on (Oct 14). New tool `walmart-sparky` in tools.json. No price/deal framing.
- New: `make-your-agent-prove-it-finished-the-job` (work, Easy): a standing "no proof, not done" rule so agents show a confirmation number, email, link or screenshot and say NOT DONE when something failed. Sources: Eon benchmark (Oct 28; 19 models, 41 tasks, false "done" the most common violation, 290 runs, all 19 models), Ctech (Oct 30), arXiv 2606.09863 (false success 45-48% of failures in airline/retail tasks; AI judges best AUROC 0.65), booking-truth (0 vs 17 false successes in 120 sandbox trials), Ashutosh Singhal Substack (Jul 1).
- Extra sources: Engadget "How to use Claude Duet" (Oct 31; weekly sales and cashflow dashboard example) on `daily-ads-and-sales-report`; CAR Confidence used-car guide (UK, updated Oct 11) on `research-a-used-car-from-a-listing`. Both were X-only; X-only use cases now 5 (was 7).
- Refreshed 48 X posts. 115 use cases; X 17% of source links (73/435); all 12 new links are non-X.
- Checks: validate 0 errors; build 156 indexed pages + 404; check_links 11,965 links, 0 broken internal. Mentions/feedback: none (X search botsdothat / botsdothat.com / "bots do that" / @botsdothat since Oct 30 = unrelated uses; HN Algolia "botsdothat" 0 hits; web search shows only our own pages). Bugs/complaints: none.
- Deploy: main e0eecfc / publish acfda08; GitHub Actions run 41497739366 succeeded (1:08 PM ET). Live: both new guides and the two updated guides return 200. This deploy line is committed with the next deploy.

## 2026-11-02 (daily QA, 7:00 AM CT)
Checks
- Live site: up. Homepage, /news/, /use-cases/, /ai-pricing/, /advertise/, /newsletter/ and /run-your-bots-for-less/ all returned 200 (0.13-0.25s).
- Internal links: 0 broken (11,752 links before the change, 11,821 after; 154 indexed pages + 404). validate 0 errors.
- Outbound links (798 unique): no real breakages. The HEAD check flagged 15 support.google.com help pages, 3 The Next Web articles (including this morning's Apple Intelligence China source) and a YouTube video as 404/500, but every one loads (200) with a normal GET; the only exception is one Google help page that rate-limited (429). FTC pages still 404 to this box for every URL (known bot block). openai.com, Hacker News (405 to HEAD), Fast Company, Retail Dive, RentCafe, StreetInsider, Riverside, AHRQ, NAIC and Search Engine Land return the usual 403/405 bot blocks; Business Wire, U.S. News and thetechsignal.co timed out.
- Real browser (headless Chrome, live site): all 155 pages scanned at 320px wide with no page-level horizontal scroll, no JS exceptions and no failed requests or broken images. Homepage quick search ("spend limit") returns results, all-guides search `?q=resignation` shows "1 of 112 use cases", the copy-prompt button shows "Copied ✓", and the cost calculator deep link loads the Web Page Watcher preset.

Bug fixed
- On phones 380px wide or narrower, the homepage's opening "scanning X, Reddit and the web…" splash box was about 18px wider than the screen at 320px, so the end of the first line was cut off. It now uses a smaller font and padding on narrow screens (`static/style.css`). The other hero items that extend past 320px are decorative (radar art and hidden blip labels) and are already clipped by `.hero`.

Improvement for visitors
- New guide `practice-negotiating-your-salary-or-job-offer` (work, Easy), from the BACKLOG autocomplete item "ai to negotiate salary": pick a target and walk-away number from real pay data, draft a short counteroffer or raise email, and role-play the recruiter or manager with feedback. Sources: Forbes (Jun 15, 2025), Fortune (May 25, 2023), the BLS guide to using wage data in salary negotiations, and Google search suggestions. Watch-outs: the AI doesn't know real pay for your area, never invent a competing offer, keep internal pay data out of the chat. No stats or claims beyond the sources. Now 113 use cases; X is 73 of 423 source links (17%). BACKLOG item marked done; `ops/source-mix.md` updated.
- Deploy: main ce56a9b / publish 62761a8; GitHub Actions run 41451320890 succeeded. Live: the new guide returns 200 and the live stylesheet has the narrow-phone fix. This deploy line is committed with the next deploy.

## 2026-11-02 (News update, AM, ~7:30 AM ET)
- Added 6 items: `chatgpt-codex-shared-usage-december` (Oct 31, notable, pricing; OpenAI Help Center usage-limits + card/device-limits articles, The Decoder; coverage @codexresets_ 663 likes / 57 reposts / 80,390 views), `deepseek-dsh-superagent-prototype` (Oct 31, notable, agent launch; GitHub, TechNode, Help Net Security; no x block, no official DeepSeek post), `apple-intelligence-china-qwen` (Oct 31, notable, feature; Apple China newsroom, The Verge, The Next Web; no x block, only low-engagement reposts), `grok-api-text-watermark` (Oct 31, minor, feature; xAI docs; no x block), `claude-ultra-plan-no-5-hour-limit` (Oct 30, notable, pricing; Claude Help Center, The Next Web, claude.com/pricing; @claudeai 31,905 / 1,931 / 6.90M), `chatgpt-mobile-account-switching` (Oct 30, minor, feature; ChatGPT release notes; @thsottiaux 14,461 / 650 / 3.17M). All measured Nov 2 AM.
- Updated `openai-robots-txt-ai-training-signal`: headline/explainer now cover Microsoft (honors it from Feb 1, 2027) and Anthropic (already honors it); added The Verge and Search Engine Land sources.
- No new NEWS_CO entries. Top story unchanged: Gemini 4 Carbon (@sundarpichai 34,087 likes / 2,750 reposts / 6.89M views). Trending: ChatGPT Pro limits doubled (38,663 / 2,674 / 6.91M), Claude Ultra plan (new, 31,905 / 1,931 / 6.90M), Block Dessa.
- Refreshed X numbers on 71 existing items (all x blocks posted in the last 60 days). Raw response in research/x_news_measure_2026_11_02_am.json.txt (local only), applied with research/news_x_2026_11_02_am.py.
- Pricing: no table change (subscription-plan changes only; no official API token price changes found).
- Skipped: Gemini Drops October roundup (items already covered), Google PlanAssist for UK planning officers (government tool), OpenAI Agents API weekly updates (developer, employee post, no docs), Cursor marketplace malicious Claude Code extension (security incident), Android Studio Rabbit 2 bring-your-own-agent (developer-only), CNBC JPMorgan/Amazon agent-blocking analysis (analysis of known blocks), OpenAI short film teaser, OpenAI $20B raise / UAE deals / policy push, Anthropic monitor-evasion research (safety research), Meta-Fourier humanoid "Max" (anonymous-source report), GPT-6.2 Astra / Claude Mythos 5.5 / GLM-5.5 (rumors), LongCat-2.5 (developer-only open model), finance/markets stories. Nothing new on anthropic.com/news, Mistral news (since Oct 29), DeepSeek API updates (since Oct 17), Gemini API changelog (since Oct 30) or the Grok Bot changelog (still v0.78.1).
- BACKLOG: ChatGPT/Codex shared allowance + device caps + Claude Ultra rename for the run-for-less/cost pages; Apple Intelligence China watch; DeepSeek Super-agent watch for an always-on agent comparison.
- Checks: validate 0 errors (112 use cases); build 153 indexed pages + 404; check_links 11,752 links, 0 broken internal.
- Deploy: main f415f5d / publish bf6cd92; GitHub Actions run 41445977346 succeeded in 24s (7:36 AM ET). Live /news/ (200) shows all 6 new items and the updated robots.txt headline. This deploy line is committed with the next deploy.

## 2026-10-30 (News update, PM, ~1:40 PM MT)
- Added 7 items: `openai-teen-violence-safeguards` (Oct 30, notable, feature; OpenAI, Reuters via US News; no x block, no OpenAI post found), `zest-text-restaurant-concierge` (Oct 30, notable, agent launch; TechCrunch; no x block, only low-engagement aggregators), `doordash-amazon-agent-orders-tiny` (Oct 30, notable, industry; TechCrunch, Fortune; coverage @TechCrunch 38 likes / 7 reposts / 20,252 views), `gemini-api-computer-use-ga` (Oct 30, minor, feature; Gemini API release notes + Computer Use guide; no x block), `openai-robots-txt-ai-training-signal` (Oct 30, minor, industry; OpenAI, Google Search Central, Unite.AI; no x block), `pika-h3-flex-open-weights` (Oct 29, notable, model release; Pika blog, Business Wire, Hugging Face; @pika_labs 1,539 / 281 / 808,632), `elevenlabs-sfx-v3` (Oct 29, notable, model release; ElevenLabs blog; @ElevenLabs 477 / 115 / 995,333). All measured Oct 30 PM.
- New NEWS_CO entries: Zest, DoorDash, ElevenLabs, Pika. Top story unchanged (Gemini 4 Carbon); trending: ChatGPT Pro limits, Block Dessa, Claude for Legal.
- Refreshed X numbers on 54 existing items (items from Oct 14 on); Gemini 4 Carbon @sundarpichai now 33,990 likes / 2,742 reposts / 6.76M views; ChatGPT Pro limits @thsottiaux 37,637 / 2,616 / 5.55M. Raw response in research/x_news_measure_2026_10_30_pm.json.txt (local only), applied with research/news_x_2026_10_30_pm.py.
- Pricing: no table change (no official API token price changes found; Gemini Computer Use is billed as regular tokens).
- Skipped: OpenAI Private Intelligence promo post (product announced Sep 29 at DevDay, not new), OpenAI agent-monitoring research (safety research, same as AM skip), GPT-6.2 / Grok 4.8 leaks (rumors), Claude Enterprise Smart Reports and pooled budgets, Claude API 128 MB request limit, Microsoft Copilot harness in Foundry (enterprise/developer), Tencent WorkBuddy remote control (China-only), Cartesia Managed Agents, Mischief 1, Nace Drex Max (developer-only or single-source), CrowdStrike agent intrusion report and Alphabet/Reddit stock drop (security/markets). Nothing new from Anthropic models, xAI, Mistral, DeepSeek, Groq or Qwen since AM; Grok Bot changelog still v0.78.1.
- BACKLOG: Zest as a possible extra tool for `restaurant-reservations-by-agent`; "finish checkout yourself" watch-out for shopping guides; SFX v3 home-video sound guide idea; robots.txt AI-training opt-out note for the site.
- Checks: validate 0 errors (112 use cases); build 153 indexed pages + 404; check_links 11,734 links, 0 broken internal.
- Deploy: main 5d99c99 / publish 4c649ed; GitHub Actions run 41115896772 succeeded in 23s (1:31 PM MT). Live /news/ shows all 7 new items; top story and trending unchanged. This deploy line is committed with the next deploy.

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

## 2026-11-03 (daily QA, 7:00 AM CT)
- Live site up (/, /news/, /use-cases/, /ai-pricing/ all 200). validate: 115 use cases, 0 errors. check_links: 11,994 links, 0 broken internal. Form inputs and menu button have labels. No bugs found.
- Improvement: `set-ai-spend-limits-and-alerts` watch-out now warns that scheduled bots stop silently when a spend limit is hit, and to alert on the limit itself and check jobs ran (BACKLOG idea from @SRKDAN marked done).

## 2026-11-04 (weekly SEO run, SEO agent)
- New guides (all facts from official docs or named security research; no invented stats or time-saved claims):
  - /is-openclaw-safe/ — CVE-2026-25253 (depthfirst), Kaspersky Securelist malicious-skills findings, Microsoft Security Blog isolation advice, OpenClaw security FAQ; 6 rules; FAQPage + Article JSON-LD.
  - /chatgpt-agent-mode-is-gone/ — verified first: OpenAI Help "ChatGPT agent is no longer available. Use ChatGPT Work…"; ChatGPT Work introduced in release notes July 9, 2026 (paid plans except Free/Go). No retirement date claimed (OpenAI hasn't published one).
  - /switch-openclaw-or-hermes-to-a-cheaper-model/ — commands from OpenClaw docs (/model, openclaw models set, fallbacks, utilityModel) and Hermes docs (hermes model, /model --global/--once); warnings on weaker models + prompt-cache cost. Uses existing LESS_RATIO from our price table.
- Internal links: cost guide, email-safety guide, run-for-less FAQ, /what-can-bots-do/ "Go deeper" line now link the new guides; new guides link to CLAW/SAFE/COST/LESS/pricing and 3 use cases. Added to NEW_GUIDES (llms.txt, search index), llms-full.txt sections, sitemap, share bar and end-of-page newsletter.
- Research notes: r/openclaw beginners repeatedly ask about token cost / model choice (threads 1spm5ux, 1sbgj89, 1r6fc2w) — basis for the cheaper-model guide.
- Checks: validate 120 use cases, 0 errors; check_links 13,224 links, 0 broken internal.

## 2026-11-04 PM news run
- Added 3 notable items: grok-bot-phone-calls (TeslaNorth, Teslarati; @bot 2118043939592942052), ricursive-ripple-65b-preview (ricursive.com, Together AI; @RicursiveAI), anthropic-claude-vault-particles (Anthropic research, Science; @AnthropicAI). New NEWS_CO entry "Ricursive".
- Refreshed X numbers on 70 existing items (raw: research/x_news_measure_2026_11_04_pm.json.txt, local only). Top story still google-gemini-4-carbon (34,094 likes / 2,746 reposts / 6.94M views).
- No pricing change; nothing major. Skipped rumors (OpenAI "Astra/Sol" Friday report, "ChatBLT" tease) and Kimi K3.1 Pro weights (already listed).

## 2026-11-05 AM news run
- Added 1 notable item: chatgpt-images-2-6-gifs (OpenAI Help Center, heise, OpenAI system card; @OpenAI 2118124944928432327).
- Updated kimi-k3-1-pro: weights are now on Hugging Face (Kimi K3.1 Pro License); added the model card as a source.
- Refreshed X numbers on 82 items (raw: research/x_news_measure_2026_11_05_am.json.txt, local only).
- No pricing table change; nothing major. Skipped items already listed (Tencent Hy4, Claude Duet, Mistral Large 4) and non-consumer news (OpenAI infrastructure compact, Linux exploit research, funding/acquisitions).

## 2026-11-05 (daily QA, 7:00 AM CT)
- Live site up (/, /news/, /use-cases/, /ai-pricing/ all 200). validate: 121 use cases, 0 errors. check_links: 13,313 links, 0 broken internal. Spot check at 320px (home, news, use cases, pricing, is-openclaw-safe): no overflow, no broken images, no JS errors. No bugs found.
- Improvement: `stop-your-ai-chats-being-used-for-training` gets a watch-out that share links stay visible to anyone with the link even with training off, so strip personal details first (The Verge on Meta Muse added as a source; BACKLOG item marked done).

## 2026-11-05 (weekly newsletter routine, 9:00 AM CT) — BotsDoThat Weekly #3
- Web issue: https://botsdothat.com/newsletter/2026-11-05/ (also on /newsletter/ and /newsletter/feed.xml). Subject: "Hand AI your shopping list, your raise talk and your day plan". sent_on null.
- Items: `turn-a-photo-of-your-shopping-list-into-a-cart`, `practice-negotiating-your-salary-or-job-offer`, `plan-your-day-from-your-calendar-and-to-do-list`, `understand-your-tax-forms-with-ai-safely`. Improved page: `stop-your-ai-chats-being-used-for-training` (new share-link watch-out). No watch-out news item. No stats or time-saved claims.
- Sponsor check (Stripe live, 10 AM ET): 20 most recent checkout sessions all expired/unpaid with empty custom fields (4 new ones on Nov 1, same pattern as our tests). No paid newsletter or bundle booking, so house ad to /advertise/ with FIRST2.
- Email files: ops/newsletter/issue-3-email.html, issue-3-email-body.html, issue-3-meta.txt (scripts/newsletter_email.py 3). Nothing emailed. Kit draft broadcast still to be built (draft only, from hello@botsdothat.com).
- newsletter issue ready, send approval needed
- The Monday report must ask Grok CEO to approve sending. Send only after both Grok CEO and Nik approve.

## 2026-11-09 (standing site QA, ~9:10 AM AST)
- Live: /, /bot-instructions/, /advertise/, /sponsor-terms/, /sitemap.xml all 200 (~0.1-0.2s). /builder/ is 404 by design (builder lives at /bot-instructions/). Local main tree matches origin/main (includes 9b7ada1 builder).
- check_links: 14,192 links, 0 broken internal. 150 outbound links spot-checked: no hard failures. Homepage and builder assets all 200; viewport meta present; images have alt/dimensions; builder inputs labelled, status regions aria-live. 38 builder tests pass. Console/mobile not testable from this box (static checks only).
- Bugs: none found.
- Improvement: 404 page now offers "Build your bot" and "Browse use cases" next to the home link, instead of only "Back to the live feed".

## 2026-11-09 PM news run
- Added 1 major item: claude-fable-5-2 (Anthropic launch post, pricing page, CNBC, The Verge; @claudeai 2119867114450268322). Fable 5.2 generally available; Mythos 5.2 limited to vetted orgs.
- Added 3 notable items: meta-muse-ember (Meta AI blog; @AIatMeta 2119853591703998787), chatgpt-dots-multiple-computers (ChatGPT Learn; @OpenAIDevs 2119883176726409645), bytedance-seedream-5-5 (ByteDance Seed; @ByteDanceSeed_ 2119720475068920181). New NEWS_CO entry "ByteDance".
- Pricing table: Claude Fable 5.1 row replaced by Claude Fable 5.2 ($8 / $40, cached $0.20, from Anthropic pricing page); added Meta Muse Ember ($0.10 / $0.50, cached $0.004, from Meta's launch post); Anthropic cache note covers Fable 5.2.
- Refreshed X numbers on 92 existing items (raw: research/x_news_measure_2026_11_09_pm.json.txt, local only; apply script research/news_x_2026_11_09_pm.py).
- Skipped: OpenAIDevs "Tomorrow." teaser (no announcement yet), Grok Bot weekly-limit reset (one-off), Automattic Spacefast and Qwen Office 2.0 (not verified from primary sources this run). 2 BACKLOG notes.

## 2026-11-10 AM news run
- Added 3 notable items: meta-muse-smartwatch (MacRumors, The Verge; @Muse 2119919277692383330), google-antigravity-knowledge-work (Antigravity blog + changelog, 9to5Google; @antigravity 2119913586109579283), anthropic-ipo-roadshow (Anthropic; $70-$78/share, ~825M shares, Nasdaq ANT; @AnthropicAI 2120117722230968385).
- Added 1 minor item: openai-control-room (OpenAI; @OpenAI 2119913172039868579).
- Refreshed X numbers on 73 items from the last two weeks (raw: research/x_news_measure_2026_11_10_am.json.txt, local only; apply script research/news_x_2026_11_10_am.py).
- No major release, no pricing table change. Skipped: Claude model-choice guide (guidance, not news), Muse Ember on Google Cloud (already covered), Google Maps Platform in AI Studio (developer-only), MiniMax H3 Image early access, Spacefast and other startup launches (not verified from primary sources). 2 BACKLOG notes.

## 2026-11-10 (standing site QA, ~9:10 AM AST)
- Live: /, /news/, /use-cases/, /ai-pricing/, /bot-instructions/, /sitemap.xml all 200 (0.1-0.4s). validate: 124 use cases, 0 errors. check_links: 14,298 links, 0 broken internal. Console/mobile not testable from this box. No bugs found.
- Improvement: none deployed this run; the BACKLOG candidates (MRI/lab report, land research, bus tickets) need 2+ verified independent sources and the news runs already deployed today. Left for the next trending run.

## 2026-11-10 (weekly SEO + AI-answer pass, ~9:30 AM AST)
- New guide **/how-to-write-instructions-for-an-ai-agent/** (6-part template, 3 copyable examples, where to paste in ChatGPT/Claude/Gemini, "instructions are not a lock", 3-minute test, mistakes; Article+FAQPage+HowTo JSON-LD; sources: OpenAI prompting guide + custom instructions help, Claude projects help, Gemini Gems help). Gap: current results for the query are enterprise/dev docs. Linked from /what-can-bots-do/, build guide "Next step", /blueprints/ lead; in llms.txt, llms-full.txt, search index, sitemap.
- **/openclaw-vs-hermes-agent/** (#2 page by visits) freshened from official docs: OpenClaw Skill Workshop now learns skills by default (undoable, propose mode); Hermes Cloud hosted option; new FAQ "Does OpenClaw learn new skills on its own like Hermes Agent?"; sources oc_workshop + hm_vs.
- **/bot-instructions/**: title "Free AI bot instructions builder: copy-paste templates", sharper description, WebApplication JSON-LD (free, no model call, no storage). Privacy description rewritten.
- seo_title added: stop-your-ai-chats-being-used-for-training, teach-your-bot-to-remember-what-works.
- Pricing: ai-pricing.json re-verified from official pages, all checked_on 2026-11-10. No price changed, none dropped vs Nov 9. Fable 5.2 $8/$40 and Muse Ember $0.10/$0.50 (<=200K) confirmed. Fixed Gemini note: it is gemini-2.5-flash (not 2.5 Flash-Lite) that routes to 3.5 Flash-Lite from Dec 1, 2026. Fixed stale Fable 5.1 $10/$50 in pick-a-smaller-model-for-simple-jobs watch_out. Blueprint models unchanged.
- Cloudflare RUM (real browsers, ChromeHeadless excluded), Nov 3 11:00 to Nov 10 11:00 AST: 121 visits / 133 page views. Top: / 32, /openclaw-vs-hermes-agent/ 16, keep-an-ai-agent-from-deleting-your-files 9, /news/ 8, /trending/ 6, /ai-agent-examples/ 6. Referrers: direct 109, bing 5, google 5, github 1, t.co 1. ChromeHeadless (our QA) 389 visits excluded.
- Search Console: no API access on box (manual CSV in /workspace/gsc only).
- AI-answer check (WebSearch tool's engine only): /ai-agent-examples/ #1 and cited for "AI agent examples for everyday life"; cost guide #1 and cited for monthly cost query; #4 for "AI agent use cases for everyday people"; not top 5 for "how to build an AI agent for beginners 2026" or "openclaw vs hermes agent". Google/Perplexity/ChatGPT/Grok not verified (Bing/DDG scraping from box returns generic/no results).
- Open: newsletter #3 title 73 chars (left); /sponsor/ noindex by design.
- Deployed: local main `9ca8229`, publish `457c56c`, Actions run 42843784478 succeeded; live /, new guide, /openclaw-vs-hermes-agent/, /bot-instructions/, /ai-pricing/, /blueprints/, sitemap, llms.txt, robots all 200.

## 2026-11-10 PM news run (~4:30 PM AST)
- Local main checked against origin first: origin/main is the separate `publish` history (by design, see README "Why two histories"); `publish` == origin/main (010bc07d) and main's tree matched, so nothing to fast-forward. No force-push.
- Added 1 major item: gemini-4-carbon-available (Google blog + Gemini API pricing page; @sundarpichai 2120185896469496180). Carbon now GA for paying API developers and Google AI Ultra (Gemini app, AI Mode, Antigravity); Antigravity /swarm preview.
- Added 7 notable items: claude-sheets-whiteboards-data (Claude articles, TechCrunch, Fortune; @claudeai 2120206365759094857), chatgpt-businesses-business-agents (OpenAI, TechCrunch, Reuters; @OpenAI 2120216592395174382), n8n-nod-personal-agent (n8n blog, GitHub; no credible engaged X post, no x block), adobe-max-creative-agent-mcp (Adobe newsroom, TechCrunch, The Verge, 9to5Mac; no x block), ebay-blocks-ai-agents (The Verge; no x block), notion-ai-chats-fireworks-breach (Notion advisory 11-09, The Hacker News; @TheHackersNews coverage 2120224129471361452), apple-intelligence-usage-packs (Apple Support, 9to5Mac, The Verge; @9to5mac coverage 2119830429448503579). New NEWS_CO entries: n8n, Adobe, eBay, Notion.
- Pricing table: added gemini-4-carbon ($2 / $10, cached $0.10 through Nov 30; $4 / $20 from Dec 1) from ai.google.dev/gemini-api/docs/pricing. No other price changed.
- Refreshed X numbers on 106 existing items (posted in the last 30 days) + 5 new blocks (raw: research/x_news_measure_2026_11_10_pm.json.txt, local only; apply script research/news_x_2026_11_10_pm.py). Top story stays claude-fable-5-2 (hottest major of 14 days); trending #1 claude-sheets-whiteboards-data.
- Skipped: Grok 4.8 (Musk says soft rollout later this week, not released), OpenAI "Cyber at the Frontier" Thursday keynote teaser, OpenAI/Upwork freelance research and education posts (research, not product), Amazon Mitra-v2 and Linux Foundation ANS (developer-only), Anthropic IPO pricing retraction (existing item's $70-$78 / ~825M shares confirmed by CNBC). 2 BACKLOG notes.
- Deployed: local main `66fa93ab`, publish `d4d40d70`, Actions run 42896508435 succeeded; live /, /news/, /ai-pricing/, /news/feed.xml 200 and new items present.

## 2026-11-11 AM news run (~8:30 AM AST)
- Local main checked against origin first: `publish` == origin/main (d4d40d70) and main (bc8a0d55) differed only by the CHANGELOG line, so nothing to fast-forward. No force-push.
- Added 11 notable items: alibaba-qwen4-max-preview (Alibaba Cloud docs; @Alibaba_Qwen 2120335993643684315), minimax-h3-image-open-weights (MiniMax blog, Hugging Face; @MiniMax_AI 2120179737695826420), chatgpt-voice-advanced-standard-retiring (OpenAI Help Center + release notes; @OpenAINewsroom 2120277245713654201), claude-free-usage-reset (@ClaudeDevs 2120275296637321476, Numerama), meta-muse-email-address (The Verge; @Muse 2120201720651563286), gemini-robotics-2-5 (DeepMind blog, The Verge, Ars Technica; @GoogleDeepMind 2120169787896525104), pixel-10-gemini-intelligence (Google blog x2, Engadget; @9to5Google coverage 2120230094379577511), railway-stolen-ai-keys (Railway incident report, The Hacker News; @Railway 2120157279177634266), openai-acquires-odessia (TechCrunch, BetaKit; @testingcatalog coverage 2120239186632396996), elevenlabs-scribe-v3 (ElevenLabs blog; @ElevenLabs 2120217467100541396), gemini-memory-summary (9to5Google, The Verge; @9to5Google coverage 2119834339156377734).
- Added 3 minor items: chatgpt-plus-veterans-offer (OpenAI + Help terms; no x block), spotify-dj-new-voices (Spotify newsroom, TechCrunch; @Spotify 2120154511352439040), otter-27-new-languages (Otter blog, TechCrunch; @otter_ai 2120058214037295108). New NEWS_CO entries: Alibaba, MiniMax, Railway, Spotify, Otter.
- No major release (Grok 4.8 still not released: no x.ai/news or Musk post since the Nov 10 "soft rollout later this week"; OpenAI "Cyber at the Frontier" keynote is Thursday Nov 12, not yet held). No pricing table change.
- Refreshed X numbers on 111 existing items (posted in the last 30 days) + 13 new blocks (raw: research/x_news_measure_2026_11_11_am.json.txt, local only; apply script research/news_x_2026_11_11_am.py). Top story stays claude-fable-5-2; trending #1 claude-sheets-whiteboards-data.
- Skipped: DeepMind AlphaProof Code / Signal proof (research), Gemini for healthcare and ChatGPT Enterprise on AWS Marketplace (enterprise-only), Google TPU 8tx/8i Max (infrastructure), New York RAISE Act registration (lab compliance), Oura-Counsel Health, Bay funding, Reddit Reviews test, Claris Harbor early access, Muse Expedia connector, OpenAI caregivers/education posts. 2 BACKLOG notes.
- Deployed: local main `dbd2e217`, publish `b9826275`, Actions run 43021741320 succeeded; live /, /news/, /news/feed.xml, /ai-pricing/ 200 and new items present.

## 2026-11-11 (standing site QA, ~9:20 AM AST)
- Live: /, /news/, /use-cases/, /bot-instructions/, /ai-pricing/, /sitemap.xml, /news/feed.xml, /llms.txt, /robots.txt, /404.html all 200 (/ ~0.2s). Site was not down. validate: 125 use cases, 0 errors; test_bot_builder passes; check_links: 14,534 links, 0 broken internal. Homepage: viewport meta, skip link, lang, one h1, all images have alt/width/height and below-the-fold ones are lazy. Console/mobile not testable from this box (static checks only).
- External (--external): 960 OK, 143 not-200, nearly all 403/429/timeouts from bot-blocking (businesswire, forbes, nytimes, perplexity, etc.). The two ftc.gov 404s are box-side (ftc.gov root also 404s from here); the FTC Operation AI Comply URL matches the title Reuters/NBC report, so left as is.
- Bugs: none.
- Improvement: homepage "Live feed · updated <date>" showed the newest guide date (Nov 10) while news items dated Nov 11 were live; it now uses the newest of guides and news (scripts/build.py).
- Deployed: local main `df1ed22d`, publish `3f9a9e4b`, Actions run 43029071523 succeeded; live homepage shows "updated Nov 11, 2026".

## 2026-11-11 (weekly SEO run, content half, SEO agent, ~11:20 AM AST)
- New guides (facts only from official docs/READMEs/launch posts, linked inline; no stats or time-saved claims):
  - /how-to-install-hermes-agent/ — desktop app (Mac Apple silicon/Windows) vs one-line installer (Linux/macOS/WSL2, PowerShell), Termux/Docker notes, `hermes setup` modes (Quick/Full/Blank Slate), 64K-context minimum, first test chat, 5 safe-setup rules (approvals, Docker backend, gateway allowlists/pairing, .env perms, read-only first job), failed-install table, update/uninstall. Article + FAQPage (7 Q) + HowTo + Breadcrumb JSON-LD. Sources: Hermes docs installation, quickstart, security, updating, migrate-from-openclaw, Hermes vs OpenClaw page. Targets autocomplete "hermes agent install" (+windows/mac/linux/docker/failed), "is hermes agent safe/free".
  - /openclaw-alternatives/ — Hermes Agent, n8n Nod, nanobot, NanoClaw, ZeroClaw, IronClaw table (maker/licence, install, what stands out; GitHub READMEs + n8n blog, repos checked via GitHub API Nov 11), how to pick, no-install options (Hermes Cloud, ChatGPT Work), safety rules. Article + FAQPage (6 Q) + ItemList + Breadcrumb JSON-LD. Targets "openclaw alternatives" (+hermes, open source, for windows/mac, reddit).
- Internal links: OpenClaw vs Hermes "How to pick" → both; /what-can-bots-do/ "Go deeper" → both; /is-openclaw-safe/ next step → alternatives; new guides link CLAW/OCSAFE/CHEAPMODEL/COST/SAFE/INSTR/AGENTMODE/BUILD, blueprints, builder and 2 use cases. Added to NEW_GUIDES (llms.txt, search index with extra keywords), llms-full.txt sections, sitemap, share bar, end-of-page newsletter.
- Improved: `set-ai-spend-limits-and-alerts` new first watch-out on stolen keys (Railway incident report Nov 10: ~$740,000 estimated unauthorized spend) + Railway and The Hacker News sources; last_checked 2026-11-11 (BACKLOG 11-11 AM news note closed).
- Outreach drafts J-L appended to ops/launch_drafts.md (awaiting Grok CEO approval; nothing sent).
- Checks: validate 125 use cases, 0 errors; test_bot_builder OK; check_links 14,717 links, 0 broken internal.

- Deployed: local main `fe19c3b0`, publish `26620fc6`, Actions run 43057778495 succeeded (deployed ~10:23 AM CT / 12:23 PM AST, before the 1 PM CT routine); live /how-to-install-hermes-agent/, /openclaw-alternatives/, /use-cases/set-ai-spend-limits-and-alerts/, /openclaw-vs-hermes-agent/, /what-can-bots-do/, /is-openclaw-safe/, llms.txt, llms-full.txt, sitemap.xml all 200 with the new content.

## 2026-11-11 (midday trending, ~2:05 PM AST / 12:05 PM CT)
- Added `let-ai-agents-dig-through-public-data-for-your-hobby` (teams of agents on free public data: Maya lidar site, later found already mapped; TESS TOI 7930 planet candidates). Sources: Miotti blog, HN 50452455 (759/283), NASA ExoFOP, Gizmodo, @p_rabtsevich X (8,730 likes). Trending #2 after build.
- Extended `stop-your-ai-chats-being-used-for-training` (Gemini Connected Apps human review: HN 50429426 727/147, Google Help, CyberInsider, DailyAI), `hand-off-tasks-by-voice-while-driving` (Gemini on Apple CarPlay, Nov 11: Google blog, 9to5Google, 9to5Mac; setup steps added), `control-your-smart-home-with-a-private-ai` (HA-MCP GitHub, 7,145 stars; admin-token watch-out).
- Refreshed 50 tracked X posts (raw metrics in /workspace/agent-tools, local only). Mentions/feedback of BotsDoThat: none. Bugs: none.
- Source mix: 126 use cases, 525 source links, X 76/525 = 14%.
- Deployed: local main `3db66bc0`, publish `10f5c9df`, Actions run 43074107363 succeeded; live /, /trending/, new page and 3 extended pages 200 (new entry on homepage, CarPlay and Gemini human-review text live).

## 2026-11-11 PM news run (~4:30 PM AST)
- Added 4 notable items: gemini-decisions-api (Google blog; @OfficialLoganK 2120581433639198885), baidu-ernie-5-5-flash-preview (Baidu ERNIE release page; @Baidu_ERNIE 2120425542688379314), gmail-help-me-write-all-workspace (Google Workspace Updates, The Verge; no x block), google-workspace-skills-rollout (Google Workspace Updates; no x block).
- No major release: big-lab X accounts quiet since the AM run; Grok 4.8 still not released (only pre-training-done remarks); OpenAI cyber keynote is Nov 12. No pricing table change: DeepSeek pricing page re-checked (V4-Pro $1.32/$3.96 peak, unchanged); Gemini Decision 1 is a scoring endpoint, not a chat model, so not added to the table.
- Refreshed X numbers on 124 existing items (posted in the last 30 days) + 2 new blocks (raw: research/x_news_measure_2026_11_11_pm.json.txt, local only; apply script research/news_x_2026_11_11_pm.py).
- Skipped: Laplace Atlas "DeepSeek launches V4-Pro, 1,000% price rise" (not on DeepSeek's changelog or pricing page; V4-Pro dates from April), AlphaGenome 2 (research), Runway Praxis-1 open weights and MBZUAI PAN 2 (robotics/research developer models), Databricks Genie update (enterprise), Visual Studio Copilot SDK/BYOM (developer), Perplexity Computer adding Carbon (covered by Carbon item), Plurai funding. 2 BACKLOG notes.
- Deploy: local main `32728988`, publish pushed to GitHub (`10f5c9df..56053f5e`); Actions run 43096314164 still queued ~40 min later because GitHub Actions has a major outage (githubstatus: Actions major outage, Pages partial outage). Live site up (/, /news/, /ai-pricing/ 200) on the previous build; this run's items go live automatically when the queued run executes. Next run should confirm.
## 2026-11-12 AM news run (~8:30 AM AST / ~7:30 AM CT)
- Stuck Nov 11 PM publish: Actions run 43096314164 (push of publish 56053f5e) was still `queued` ~16 h later although githubstatus showed all systems operational; live /news/ still had last-modified 2026-11-11 18:04 UTC (midday build), so gemini-decisions-api etc. were NOT live. This run's deploy pushes a new publish commit that also carries those items.
- Added 4 items: **united-blocks-ai-agent-bookings** (2026-11-11, notable industry; The Verge/WSJ; coverage @Complex), **gemini-live-carplay** (2026-11-11, notable; Google blog; @GeminiApp), **chatgpt-finances-desktop** (2026-11-11, minor; 9to5Mac + OpenAI Help; @ChatGPT), **openai-india-api-local-processing** (2026-11-12, minor; The Hindu + Economic Times; no X block). Added `United` to `NEWS_CO`. No new MAJOR item.
- No major release: OpenAI "Cyber at the Frontier" keynote is today at 10 AM PT (had not happened at run time; PM run should check); Grok 4.8 still not released (x.ai/news and release notes still on Grok 4.7; only "soft rollout this week" remarks); Anthropic's Nov 12 "Our initial public offering" post is IPO marketing, already covered by anthropic-ipo-roadshow. DeepSeek changelog unchanged since 2026-10-17, so the V4-Pro price-hike story stays unverified and skipped. No pricing table change.
- Refreshed X numbers on 125 existing items (posted in the last 30 days) + 3 new blocks (measured_at 2026-11-12T12:35Z; raw research/x_news_measure_2026_11_12_am.json.txt, local only; apply script research/news_x_2026_11_12_am.py).
- Skipped: Nvidia board weighing Jensen Huang's future (no decision announced), OpenAI $2M children's-safety research pledge (policy), Google TPU 8tx/8i Max (infrastructure), ElevenLabs Summit enterprise fine-tuning (coming months), Muse email for free plans ("soon", not shipped), Apple Siri AI developer preview (Nov 3, older than a week; BACKLOG), 2wai avatar app backlash, a16z agent-traffic charts (commentary). 3 BACKLOG notes.
- Deploy: local main `a18ef1ee`, publish `5f7b147c` (`56053f5e..5f7b147c`), Actions run 43219514895 succeeded (26 s); live /news/ last-modified 2026-11-12 12:37 UTC shows the 4 new items plus the Nov 11 PM items (gemini-decisions-api, ERNIE 5.5 Flash Preview, Workspace skills), so the stuck publish is now live. Ghost run 43096314164 still shows `queued` but `gh run cancel` says it is already completed, so it can't redeploy the older tree.

## 2026-11-12 site health run (~9:10 AM AST)
- QA: live https://botsdothat.com/ 200; check_links 14,833 links, 0 broken internal. No bugs found.
- Improvement: `book-a-flight-with-an-ai-agent` new first watch-out that United (Nov 2026) and others block personal AI agents from booking, so stop at the payment page and check out yourself (matches existing news item united-blocks-ai-agent-bookings); last_checked 2026-11-12. BACKLOG United note closed.

## 2026-11-12 (weekly newsletter routine) — BotsDoThat Weekly #4
- Web issue: https://botsdothat.com/newsletter/2026-11-12/ (also on /newsletter/ and /newsletter/feed.xml). Subject: "Let AI book your flight and take errands from your car or watch". Preview: "Four jobs to hand to AI this week, each with a prompt to copy, plus a new guide to writing instructions your agent actually follows." sent_on null.
- Items: `book-a-flight-with-an-ai-agent` (new United agent-block watch-out), `hand-off-tasks-by-voice-while-driving` (Gemini on CarPlay, Nov 11), `hand-your-agent-an-errand-from-your-watch` (Muse on Apple Watch/Wear OS), `let-ai-agents-dig-through-public-data-for-your-hobby` (Maya lidar + TOI 7930 candidates). All have copy-paste prompts; none repeat issues 1-3. New page: `/how-to-write-instructions-for-an-ai-agent/` (guide added 2026-11-10; new_page uses path/title since it isn't a use case). Watch-out: `railway-stolen-ai-keys`. No stats or time-saved claims.
- Sponsor check (Stripe live, ~11:15 AM AST): 25 checkout sessions on the account, all expired/unpaid with empty custom fields (latest Nov 1, our tests); 0 charges. No paid newsletter or bundle booking, so house ad to /advertise/ with FIRST2.
- Email files: ops/newsletter/issue-4-email.html, issue-4-email-body.html, issue-4-meta.txt (scripts/newsletter_email.py 4). Header image https://botsdothat.com/assets/img/email-header.png (200). Nothing emailed. Kit draft broadcast is being built separately (draft only, from hello@botsdothat.com).
- newsletter issue ready, send approval needed
- The Monday report must ask Grok CEO to approve sending. Send only after both Grok CEO and Nik approve.
- Deployed main 715efd7b / publish f419dd75 / Actions 43245508669 (success). Live: /newsletter/2026-11-12/, /newsletter/, /newsletter/feed.xml all 200 with issue #4.
- Kit (11:21 AM AST): the Creator trial had ended and locked the account, so it was moved to Kit's Free plan (Nik's Oct 23 choice; no card). Free turns off sequences, Visual Automations, integrations and custom branding. Issue #4 built as unsent draft broadcast 26986945 (https://app.kit.com/campaigns/26986945/draft), from BotsDoThat <hello@botsdothat.com>, to All Subscribers (5). No test email, not sent, not scheduled, not published. Draft 26817411 (#3) still unsent.

## 2026-11-12 (midday trending, ~2:15 PM AST / 1:15 PM CT)
- Added `let-an-ai-agent-tap-through-your-phone-for-you` (Advanced; GitHub DIYgod/pinky 1,990 stars, JosssphZhou/poki 1,022, lxe/phoneuse 628, poki.bot; no popularity block, so it shows in Just added, not Trending) and `back-up-your-ai-agent-and-move-it-to-a-new-computer` (Medium; X @hgruenhagen 2120611235204841909 50 likes/2,860 views, OpenClaw migration + backups docs, MacMyths guide).
- Extended `get-meeting-notes-and-action-items` (Yogurt: HN 50454625 280/108, GitHub 826 stars; setup tip + no-bot recording watch-out), `book-a-flight-with-an-ai-agent` (HN 50458900 641/667), `control-your-smart-home-with-a-private-ai` (hermes-voice 685 stars + Echo unlock watch-out); `let-ai-agents-dig-through-public-data-for-your-hobby` HN now 1,023/385.
- Refreshed 51 tracked X posts (raw /workspace/agent-tools/x_trend_2026_11_12.json, local only). Mentions/feedback of BotsDoThat: none. Bugs: none.
- Source mix: 128 use cases, 537 source links, X 77/537 = 14%.
- Deployed: local main `178fa89a`, publish `442d96b5`, Actions run 43276254201 succeeded; live /, both new pages 200.

## 2026-11-12 PM news run (~4:30 PM AST / ~3:30 PM CT)
- Added 3 items: **gemini-4-hydrogen** (2026-11-12, MAJOR model release; Google blog + Gemini API pricing; X @GoogleDeepMind 2120940338869055788, 4,407 likes / 357 reposts / 340,147 views), **wirex-navoka-agent-own-card** (2026-11-12, notable agent launch; PR Newswire; no credible X post, so no X block; added `Wirex` to `NEWS_CO`), **openai-daybreak-red-team-defense-factory** (2026-11-12, minor agent launch for security teams from the Cyber at the Frontier keynote; The Deep View + openai.com Daybreak pages; no official OpenAI post found in X search, so no X block).
- Pricing: added `gemini-4-hydrogen` row ($1.50 / $7.50, cached $0.075, free tier) from ai.google.dev/gemini-api/docs/pricing, checked 2026-11-12; removed the stale not_verified "Gemini 4 Carbon API price" entry (Carbon has a verified row since Nov 10).
- Deploy: local main `fb659dde`, publish `a3d8df89`, Actions run 43300653611 succeeded; live /news/ shows Hydrogen.
- X: measured 4 new posts at 2026-11-12T20:31Z (raw research/x_news_measure_2026_11_12_pm.json.txt, local only; apply script research/news_x_2026_11_12_pm.py). No broad refresh this run; the AM run refreshed 125 items 8 hours earlier.
- Skipped: Runway Praxis-1 (robotics), Lara Mini, ZONOS3-Mini, Salesforce SOV-Transcribe-1, Hark Handoff 2 (small/dev models), Nectar Creator Agent, NiCE Cognigy, Semgrep, Alibaba AgenticOps (enterprise), advocacy lawsuit to freeze new models (filing only). 2 BACKLOG notes.

## 2026-11-13 AM news run (~6:40 AM CT)
- Added 4 notable items: **claude-meetings-beta** (2026-11-12, Anthropic; claude.com + Help Center + VentureBeat; X @claudeai 2120973994191094179, 63,393 likes / 3,963 reposts / 5,488,446 views), **chatgpt-dots-custom-instructions** (2026-11-12, OpenAI; learn.chatgpt.com What's new + Gadgets 360; X @ChatGPT 2120970988796170275, 3,647 / 208 / 1,032,303), **yandex-alice-do-it-agent** (2026-11-12, Yandex newsroom; X @yandexcom 2120905470231925168, 76 / 4 / 5,115; added `Yandex` to `NEWS_CO`), **google-labs-tabletop** (2026-11-11, Google blog + The Verge; X @GoogleLabs 2120549258692882702, 1,510 / 128 / 129,514). X measured 2026-11-13T12:34Z (raw research/x_news_measure_2026_11_13_am.json.txt, local only).
- No major release, no pricing change. Skipped: GPT-6.1 Terra coverage (already listed, Oct 26), ChatGPT Wallet (unannounced policy pages), Edge0-145B / Haru-4B / Perplexity Decider v1.3 (small or developer models), Databricks always-on Genie, NiCE Cognigy (enterprise), Anthropic Claude for Manufacturing (industry plugin), nonprofits' lawsuit (filing only), ByteDance assistant (report). 2 BACKLOG notes.
- Deploy: local main `81486c13`, publish `14acd3fa` (`a3d8df89..14acd3fa`), Actions run 43426366468 succeeded; live /news/ shows the new items.

## 2026-11-13 (site health, 7:10 AM CT)
- Live site: /, /news/, /newsletter/, /advertise/, /sitemap.xml, /feed.xml all 200 (home 0.14s). validate.py: 128 use cases, 12 blueprints, 0 errors. check_links.py: 15,102 links scanned, 0 broken internal. No bugs found, no source changes, no deploy. Browser-level console/mobile checks not run this pass.
- Improvement: none this run (candidate backlog items still wait on second sources).

## 2026-11-13 (midday trending, ~12:10 PM CT)
- Added `share-a-scam-check-bot-with-an-older-parent` (Easy, family; X @0chob 2120909462286254271 161 likes / 11 reposts / 193 bookmarks / 33,513 views, xAI Grok Bot 1.0 post, Flavio Copes Grok Bot 1.0 guide, Product Hunt Nov 12 #10 score 122, FCC grandparent-scam alert) and `design-an-embroidery-pattern-with-an-ai-agent` (Advanced; ZigZag: HN 50470488 689/223, GitHub simpsoka/zigzag 565 stars, It's FOSS, zigzag.diy; no popularity block).
- Extended `make-a-customer-service-call` (Muse calls US businesses for paid subscribers since Nov 12: TechCrunch, Engadget; popularity now @alexandr_wang 2120930586827391350 1,382 likes / 114 reposts / 92,273 views; Muse tool + setup + disclosure watch-out), `control-your-smart-home-with-a-private-ai` (Coway local-control blog + HN 50474959 423/123; watch-out), `hand-your-most-hated-chores-to-a-personal-agent` (n8n Nod: n8n blog, Product Hunt 296 upvotes, GitHub 991 stars; setup steps + watch-out; new `nod` tool).
- Refreshed 51 tracked X posts (raw /workspace/agent-tools/x_trend_2026_11_13.json, local only). Mentions/feedback of BotsDoThat: none. Bugs: none.
- Source mix: 130 use cases, 554 source links, X 79/554 = 14% (this run's new links: 2 of 17 X).
- Deployed: local main `39aa2c91` (also carried unpushed f3c8d6dc + the 7:10 AM site-health note), publish `b86e165f` (`14acd3fa..b86e165f`), Actions run 43479399608 succeeded (25 s); live /, both new pages and 3 extended pages 200 with the new text.

## 2026-11-13 PM news run (~2:45 PM CT)
- Added 4 items: **chatgpt-wallet-dots-purchases** (2026-11-13, notable agent launch; openai.com + TechCrunch; X @ChatGPT 2121283151729496235, 2,913 likes / 218 reposts / 277,258 views), **sierra-poppy-1-0-muse-shopify** (2026-11-13, notable industry; Sierra blog; X @SierraPlatform 2121296788766519431, 166 / 17 / 14,822; added `Sierra` to `NEWS_CO`), **deepseek-app-features-api** (2026-11-13, minor; DeepSeek API change log + AGI Pulse; X @deepseek_ai 2121247896918253875, 6,349 / 522 / 461,148), **grok-bot-joins-meetings** (2026-11-11 changelog v1.0.1, notable; x.ai changelog + docs; X @bot 2121320089920430181 posted Nov 13, 2,386 / 190 / 373,774). X measured 2026-11-13T20:31Z (raw research/x_news_measure_2026_11_13_pm.json.txt, local only).
- No major release, no pricing change (DeepSeek tool fees are add-ons; search/fetch price unchanged). 2 BACKLOG notes; skips listed in BACKLOG.
