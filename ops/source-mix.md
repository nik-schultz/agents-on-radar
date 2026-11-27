# Source mix: where BotsDoThat's use cases come from

Why this exists: Nik asked (2026-10-24) for use cases to be sourced from more than X (Reddit, Hacker News, YouTube, GitHub, blogs, official docs) so they're more trustworthy. Re-measure any time with `python3 scripts/source_mix.py "Title"`.

How it's counted: each link in a use case's `sources` list, grouped by platform. "Community links" = X + Reddit + Hacker News + YouTube + GitHub + Product Hunt. Official docs, news and blogs and Google search-demand lookups are counted separately.

## Before (measured 2026-10-24)

- Use cases: **82**; source links: **162**
- X share of source links: **61/162 = 38%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **61/72 = 85%**
- X-only use cases (every source is an X post): **37** (45%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **8**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 104

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 68 | 33 |
| X | 61 | 50 |
| Search demand (Google) | 22 | 18 |
| Reddit | 9 | 7 |
| GitHub | 1 | 1 |
| Hacker News | 1 | 1 |

Top domains: x.com (61), google.com (22), docs.anthropic.com (7), support.google.com (5), reddit.com (5), menlovc.com (5), help.openai.com (4), mistral.ai (4), reddit.sentinel-team.org (4), ai.google.dev (3), wired.com (3), gemini.google (3)

The "104 x.com vs 8 reddit.com" figure that prompted this counted every URL in the file, including popularity blocks and examples. Counting only the visible Sources lists: 61 X links.

## After (measured 2026-10-24)

- Use cases: **94**; source links: **316**
- X share of source links: **61/316 = 19%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **61/215 = 28%**
- X-only use cases (every source is an X post): **14** (15%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **66**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 104

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| YouTube | 88 | 60 |
| Official docs, news and blogs | 79 | 41 |
| X | 61 | 50 |
| Hacker News | 28 | 22 |
| Reddit | 27 | 20 |
| Search demand (Google) | 22 | 18 |
| GitHub | 11 | 9 |

Top domains: youtube.com (88), x.com (61), news.ycombinator.com (28), reddit.com (23), google.com (22), support.google.com (11), github.com (11), docs.anthropic.com (7), menlovc.com (5), help.openai.com (4), mistral.ai (4), reddit.sentinel-team.org (4)

What changed in this pass (2026-10-24):
- 53 existing use cases gained 96 non-X sources (YouTube walkthroughs, Hacker News threads, GitHub projects, Reddit threads and comments). Engagement was measured on 2026-10-24 and is stored on the source (`stats` + `measured_at`).
- 12 new use cases were added, sourced mainly from Hacker News, YouTube, GitHub, Reddit and official help pages (origin `community-backfill-2026-10-24`). None depend on X.
- Still X-only (no genuine non-X source found yet): proactive-next-moves-bot (its second source is Anthropic's own X post), give-your-agents-a-shared-apple-account, get-roadside-help-abroad, research-a-used-car-from-a-listing, prescription-ready-and-time-to-leave, sunday-family-calendar-check, plan-and-book-a-whole-trip-by-text, book-a-haircut-by-email, one-bot-per-brand, find-dead-conversations-to-follow-up, household-restock-list, weekend-family-activities, medication-reminders-for-a-parent, daily-ads-and-sales-report.

Limits on what could be measured from the server:
- Reddit: www.reddit.com JSON returns 403, old.reddit JSON redirects to login, pullpush returns 429. Reddit's RSS feeds are readable but slow (heavily rate-limited) and carry no upvote counts. So the new Reddit sources show no score; we never estimate one.
- YouTube: watch pages return 429 from the server. View counts were read from YouTube search results on 2026-10-24 and titles/channels confirmed with YouTube's oEmbed endpoint. Exact upload dates weren't available, so YouTube sources have no posted_at.
- Hacker News points/comments come from the hn.algolia.com API; GitHub stars from github.com, both on 2026-10-24.

## After (measured 2026-10-26 midday)

- Use cases: **98**; source links: **336**
- X share of source links: **66/336 = 20%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **66/224 = 29%**
- X-only use cases (every source is an X post): **14** (14%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **68**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 110

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| YouTube | 91 | 62 |
| Official docs, news and blogs | 90 | 45 |
| X | 66 | 52 |
| Hacker News | 29 | 23 |
| Reddit | 27 | 20 |
| Search demand (Google) | 22 | 18 |
| GitHub | 11 | 9 |

Top domains: youtube.com (91), x.com (66), news.ycombinator.com (29), reddit.com (23), google.com (22), support.google.com (11), github.com (11), docs.anthropic.com (7), menlovc.com (5), help.openai.com (4), mistral.ai (4), reddit.sentinel-team.org (4)


## After (measured 2026-10-27 midday)

- Use cases: **102**; source links: **358**
- X share of source links: **67/358 = 19%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **67/232 = 29%**
- X-only use cases (every source is an X post): **8** (8%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **74**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 112

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 104 | 51 |
| YouTube | 91 | 62 |
| X | 67 | 53 |
| Hacker News | 30 | 24 |
| Reddit | 28 | 21 |
| Search demand (Google) | 22 | 18 |
| GitHub | 14 | 12 |
| Product Hunt | 2 | 2 |

Top domains: youtube.com (91), x.com (67), news.ycombinator.com (30), reddit.com (24), google.com (22), github.com (14), support.google.com (11), docs.anthropic.com (7), menlovc.com (5), help.openai.com (4), mistral.ai (4), reddit.sentinel-team.org (4)


What changed in this pass (2026-10-27 midday): 3 new use cases (Riverside Agents, Hob, Kiwi) with 12 links, only 1 of them on X. Non-X sources added to 6 X-only entries (weekend-family-activities, plan-and-book-a-whole-trip-by-text, sunday-family-calendar-check, household-restock-list, find-dead-conversations-to-follow-up, medication-reminders-for-a-parent). X-only entries left: give-your-agents-a-shared-apple-account, get-roadside-help-abroad, research-a-used-car-from-a-listing, prescription-ready-and-time-to-leave, book-a-haircut-by-email, one-bot-per-brand, daily-ads-and-sales-report, proactive-next-moves-bot (its 2nd source is an official X post).

## After (measured 2026-10-28 midday)

- Use cases: **106**; source links: **382**
- X share of source links: **69/382 = 18%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **69/237 = 29%**
- X-only use cases (every source is an X post): **8** (8%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **75**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 115

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 123 | 57 |
| YouTube | 91 | 62 |
| X | 69 | 54 |
| Hacker News | 31 | 25 |
| Reddit | 28 | 21 |
| Search demand (Google) | 22 | 18 |
| GitHub | 15 | 13 |
| Product Hunt | 3 | 3 |

Top domains: youtube.com (91), x.com (69), news.ycombinator.com (31), reddit.com (24), google.com (22), github.com (15), support.google.com (14), docs.anthropic.com (7), menlovc.com (5), techcrunch.com (4), support.claude.com (4), blog.google (4)


What changed (2026-10-28 midday trending run): 1 new use case (Instinct group chats; 2 news sources + 1 X post) and 5 non-X sources added to existing entries (Link help center, The Defiant, TechCrunch, Product Hunt Off Grid AI). 4 of the 6 new links are non-X.

## After (measured 2026-10-29 daily QA)

- Use cases: **107**; source links: **387**
- X share of source links: **70/387 = 18%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **70/238 = 29%**
- X-only use cases (every source is an X post): **8** (7%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **75**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 117

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 127 | 58 |
| YouTube | 91 | 62 |
| X | 70 | 55 |
| Hacker News | 31 | 25 |
| Reddit | 28 | 21 |
| Search demand (Google) | 22 | 18 |
| GitHub | 15 | 13 |
| Product Hunt | 3 | 3 |

Top domains: youtube.com (91), x.com (70), news.ycombinator.com (31), reddit.com (24), google.com (22), github.com (15), support.google.com (14), docs.anthropic.com (7), menlovc.com (5), techcrunch.com (4), support.claude.com (4), blog.google (4)


What changed (2026-10-29 daily QA run): 1 new use case (let-your-ai-shop-for-you-with-shop-pay; 2 official Shopify/Shop pages + The Verge + 1 X post) and 1 official source (Shop Help Center) added to pay-with-a-single-use-virtual-card. 4 of the 5 new links are non-X.

## After (measured 2026-10-29 midday)

- Use cases: **110**; source links: **405**
- X share of source links: **72/405 = 18%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **72/243 = 30%**
- X-only use cases (every source is an X post): **7** (6%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **78**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 121

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 140 | 62 |
| YouTube | 91 | 62 |
| X | 72 | 57 |
| Hacker News | 31 | 25 |
| Reddit | 30 | 23 |
| Search demand (Google) | 22 | 18 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (72), news.ycombinator.com (31), reddit.com (26), google.com (22), github.com (15), support.google.com (14), help.openai.com (7), docs.anthropic.com (7), menlovc.com (5), producthunt.com (4), techcrunch.com (4)


What changed (2026-10-29 midday trending run): 3 new use cases (ChatGPT iCloud Mail/Calendar, IFTTT.ai, AI getting-started coach) with 16 links, 2 of them on X; The Straits Times (Oct 28) added to `proactive-next-moves-bot` (no longer X-only) and `restaurant-reservations-by-agent`. 16 of the 18 new links are non-X. X-only entries left (7): give-your-agents-a-shared-apple-account, get-roadside-help-abroad, research-a-used-car-from-a-listing, prescription-ready-and-time-to-leave, book-a-haircut-by-email, one-bot-per-brand, daily-ads-and-sales-report.

## After (measured 2026-10-30 daily QA)

- Use cases: **111**; source links: **412**
- X share of source links: **72/412 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **72/245 = 29%**
- X-only use cases (every source is an X post): **7** (6%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **79**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 121

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 144 | 63 |
| YouTube | 91 | 62 |
| X | 72 | 57 |
| Reddit | 32 | 24 |
| Hacker News | 31 | 25 |
| Search demand (Google) | 23 | 19 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (72), news.ycombinator.com (31), reddit.com (28), google.com (23), support.google.com (17), github.com (15), help.openai.com (7), docs.anthropic.com (7), support.claude.com (5), menlovc.com (5), producthunt.com (4)


What changed (2026-10-30 daily QA): new use case `plan-your-day-from-your-calendar-and-to-do-list` with 7 links (2 Reddit, 4 official Gemini/Claude help pages, 1 Google search suggestions), none on X.

## After (measured 2026-10-30 midday trending run)

- Use cases: **112**; source links: **419**
- X share of source links: **73/419 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **73/248 = 29%**
- X-only use cases (every source is an X post): **7** (6%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **81**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 122

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 148 | 64 |
| YouTube | 91 | 62 |
| X | 73 | 58 |
| Reddit | 33 | 25 |
| Hacker News | 32 | 26 |
| Search demand (Google) | 23 | 19 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (73), news.ycombinator.com (32), reddit.com (29), google.com (23), support.google.com (17), github.com (15), help.openai.com (7), docs.anthropic.com (7), wired.com (5), support.claude.com (5), menlovc.com (5)


What changed (2026-10-30 midday trending run): new use case `catch-calendar-clashes-hiding-in-your-email` with 5 links (WIRED, Fast Company, r/AI_Agents, Fieldwork, 1 X post), so 4 of 5 are non-X; added HN 50292727 (Claude Duet post) to `proactive-next-moves-bot` and WIRED's six-agent test to `hand-your-most-hated-chores-to-a-personal-agent`. 6 of 7 new links are non-X.

## After (measured 2026-11-02 daily QA)

- Use cases: **113**; source links: **423**
- X share of source links: **73/423 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **73/248 = 29%**
- X-only use cases (every source is an X post): **7** (6%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **81**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 122

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 151 | 65 |
| YouTube | 91 | 62 |
| X | 73 | 58 |
| Reddit | 33 | 25 |
| Hacker News | 32 | 26 |
| Search demand (Google) | 24 | 20 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (73), news.ycombinator.com (32), reddit.com (29), google.com (24), support.google.com (17), github.com (15), help.openai.com (7), docs.anthropic.com (7), wired.com (5), support.claude.com (5), menlovc.com (5)


What changed (2026-11-02 daily QA): new use case `practice-negotiating-your-salary-or-job-offer` with 4 links (Forbes, Fortune, BLS, Google search suggestions), none on X.

## After (measured 2026-11-02 midday trending run)

- Use cases: **115**; source links: **435**
- X share of source links: **73/435 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **73/248 = 29%**
- X-only use cases (every source is an X post): **5** (4%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **81**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 122

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 163 | 69 |
| YouTube | 91 | 62 |
| X | 73 | 58 |
| Reddit | 33 | 25 |
| Hacker News | 32 | 26 |
| Search demand (Google) | 24 | 20 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (73), news.ycombinator.com (32), reddit.com (29), google.com (24), support.google.com (17), github.com (15), help.openai.com (7), docs.anthropic.com (7), wired.com (5), support.claude.com (5), menlovc.com (5)


What changed (2026-11-02 midday trending run): new use cases `turn-a-photo-of-your-shopping-list-into-a-cart` (Walmart newsroom, PPC Land, Winning With Walmart, Market & Tech, Hip2Save) and `make-your-agent-prove-it-finished-the-job` (Eon, Ctech, arXiv, booking-truth, Substack), 10 links, none on X; added Engadget to `daily-ads-and-sales-report` and CAR Confidence to `research-a-used-car-from-a-listing`, so both are no longer X-only (X-only 7 -> 5). All 12 new links are non-X.

## After weekly SEO run (measured 2026-11-03)

- Use cases: **116**; source links: **440**
- X share of source links: **73/440 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **73/250 = 29%**
- X-only use cases (every source is an X post): **5** (4%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **82**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 122

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 166 | 70 |
| YouTube | 91 | 62 |
| X | 73 | 58 |
| Hacker News | 34 | 27 |
| Reddit | 33 | 25 |
| Search demand (Google) | 24 | 20 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (73), news.ycombinator.com (34), reddit.com (29), google.com (24), support.google.com (17), github.com (15), help.openai.com (8), docs.anthropic.com (7), blog.google (5), wired.com (5), support.claude.com (5)

- Added this run: book-a-flight-with-an-ai-agent (5 sources: OpenAI Help, Google blog, 2 Hacker News threads, Travel Distribution News; 0 X).

## After midday trending run (measured 2026-11-03)

- Use cases: **119**; source links: **468**
- X share of source links: **70/468 = 15%**
- X-only use cases: **5**
- Added this run: keep-a-visa-application-on-track (3 sources: Toki blog, The Straits Times, Hacker News; 0 X). Refreshed 48 X popularity blocks.

## After midday trending run (measured 2026-11-04)

- Use cases: **121**; source links: **478**
- X share of source links: **73/478 = 15%** (community links: 73/255 = 29%)
- X-only use cases: **5**
- Added this run: stop-your-ai-chats-being-used-for-training (4 sources: 2 Hacker News threads, OpenAI Help, Google Gemini Privacy Hub; 0 X). Refreshed 48 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (HN Algolia 0 hits, X search only unrelated "bots do that" replies, web search only our own pages).

## After midday trending run (measured 2026-11-05)

- Use cases: **122**; source links: **484**
- X share of source links: **74/484 = 15%** (community links: 74/256 = 29%)
- Added this run: research-your-family-history-with-an-ai-agent (5 sources: MyHeritage blog, MyHeritage Help, Business Wire, Genealogy's Star blog, 1 X post by @MyHeritage). Refreshed 48 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (HN Algolia 0 hits; X search only our own @botsdothat posts).
## After midday trending run (measured 2026-11-06)

- Use cases: **123**; source links: **497**
- X share of source links: **74/497 = 15%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **74/257 = 29%**
- X-only use cases (every source is an X post): **5** (4%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **86**
- x.com URLs anywhere in the file (sources + popularity blocks + examples): 124

| Platform | Source links | Use cases citing it |
|---|---:|---:|
| Official docs, news and blogs | 214 | 80 |
| YouTube | 91 | 62 |
| X | 74 | 59 |
| Hacker News | 38 | 30 |
| Reddit | 35 | 26 |
| Search demand (Google) | 26 | 22 |
| GitHub | 15 | 13 |
| Product Hunt | 4 | 4 |

Top domains: youtube.com (91), x.com (74), news.ycombinator.com (38), reddit.com (31), google.com (26), support.google.com (20), help.openai.com (18), github.com (15), support.claude.com (13), docs.anthropic.com (7), blog.google (5), wired.com (5)

- Added this run: ask-claude-about-your-own-spending (6 sources: Claude article, Claude Help, Verge, Plaid, Engadget, HN 50382192; 0 X). Extended practice-a-job-interview-out-loud with Muse voice (Meta newsroom, Verge, TNW). Added TeslaNorth + Teslarati native-call sources to make-a-customer-service-call and call-and-book-by-phone. Refreshed 49 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (HN Algolia 0 hits; X search only our own @botsdothat posts and unrelated "bots do that" phrases; web search only our own pages).

## After PM trending run (measured 2026-11-09)

- Use cases: **124**; source links: **502**
- X share of source links: **74/502 = 15%** (community links: 74/259 = 29%); X-only use cases: **5**
- Added this run: teach-your-bot-to-remember-what-works (5 sources: Anthropic Engineering, 2 Hacker News threads 184/103 and 186/108, LoreKit blog, Claude Help Center; 0 X). Refreshed 49 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (HN Algolia 0 hits; X search_posts_all 0 results; Reddit blocked from this box).

## After PM trending run (measured 2026-11-10)

- Use cases: **125**; source links: **510**
- X share of source links: **75/510 = 15%** (community links: 75/261 = 29%); X-only use cases: **5**
- Added this run: hand-your-agent-an-errand-from-your-watch (5 sources: TechCrunch, Gadgets & Wearables, PCMag, Times of India Gadgets Now, @Muse X post 4,609 likes / 393k views; 1 of 5 X). Extended keep-an-ai-agent-from-deleting-your-files with the Claude Code "Don't ask again" password watch-out (The Hacker News, HN 50407882 624 pts / 425 comments, LATENT; 0 X). Refreshed 49 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (HN Algolia 0 hits; X search since Nov 9 only unrelated "bots do that" phrases; Reddit blocked from this box).

## After midday trending run (measured 2026-11-11)

- Use cases: **126**; source links: **525**
- X share of source links: **76/525 = 14%** (community links: 76/265 = 29%); X-only use cases: **5**
- Added this run: let-ai-agents-dig-through-public-data-for-your-hobby (5 sources: Pietro Miotti blog, Hacker News 50452455 759 pts / 283 comments, NASA ExoFOP TOI 7930, Gizmodo, @p_rabtsevich X thread 8,730 likes / 1.22M views; 1 of 5 X).
- Extended (0 X): stop-your-ai-chats-being-used-for-training (+HN 50429426 727/147, Gemini Connected Apps help, CyberInsider, DailyAI); hand-off-tasks-by-voice-while-driving (was X + YouTube; +Google blog, 9to5Google, 9to5Mac on Gemini for CarPlay); control-your-smart-home-with-a-private-ai (+GitHub homeassistant-ai/ha-mcp 7,145 stars). Refreshed 50 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (HN Algolia 0 hits; X search since Nov 10 only unrelated "bots do that" phrases; Reddit blocked from this box).

## After midday trending (measured 2026-11-12)

- Use cases: **128**; source links: **537**
- X share of source links: **77/537 = 14%** (community links: 77/273 = 28%); X-only use cases: **5**
- Added this run: let-an-ai-agent-tap-through-your-phone-for-you (4 sources, 0 X: GitHub pinky 1,990 stars, poki 1,022, phoneuse 628, poki.bot); back-up-your-ai-agent-and-move-it-to-a-new-computer (4 sources, 1 X: @hgruenhagen 50 likes, OpenClaw migration + backups docs, MacMyths).
- Extended (0 X): get-meeting-notes-and-action-items (+HN 50454625 280/108, +GitHub yogurt 826 stars); book-a-flight-with-an-ai-agent (+HN 50458900 641/667); control-your-smart-home-with-a-private-ai (+GitHub hermes-voice 685 stars). Maya HN refreshed to 1,023/385. Refreshed 51 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (X search since Nov 5 only unrelated "bots do that" phrases; HN Algolia 0 hits; Reddit blocked from this box).

## After midday trending (measured 2026-11-13)

- Use cases: **130**; source links: **554**
- X share of source links: **79/554 = 14%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **79/281 = 28%**
- X-only use cases (every source is an X post): **5** (4%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **91**
- Added this run: share-a-scam-check-bot-with-an-older-parent (5 sources, 1 X: @0chob 161 likes / 33,513 views, xAI Grok Bot 1.0 post, Flavio Copes guide, Product Hunt Nov 12 leaderboard, FCC grandparent-scam alert); design-an-embroidery-pattern-with-an-ai-agent (4 sources, 0 X: HN 50470488 689/223, GitHub simpsoka/zigzag 565 stars, It's FOSS, zigzag.diy).
- Extended: make-a-customer-service-call (+TechCrunch, Engadget, 1 X @alexandr_wang 1,382 likes / 92,273 views on Muse calling); control-your-smart-home-with-a-private-ai (+Coway blog, HN 50474959 423/123; 0 X); hand-your-most-hated-chores-to-a-personal-agent (+n8n Nod blog, Product Hunt 296 upvotes, GitHub n8n-io/nod 991 stars; 0 X). New links this run: 17, of which 2 X (12%). Refreshed 51 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (X search since Nov 12 only unrelated "bots do that" phrases; HN Algolia 0 hits; web search only our own pages; Reddit blocked from this box).

## After midday trending (measured 2026-11-16)

- Use cases: **131**; source links: **567**
- X share of source links: **80/567 = 14%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **80/284 = 28%**
- X-only use cases (every source is an X post): **5** (4%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **92**
- Added this run: turn-your-booking-emails-into-one-trip-sheet (7 sources, 1 X: @witcheer 42 likes / 17 bookmarks / 2,377 views; Hermes recipes #28, Hermes HQ use case, Yandex Alice "Do it!" Nov 13, Travel Wallet guide, Moonjar Help, GitHub fistfulayen/ubtrippin 5 stars).
- Extended: book-an-appointment-with-an-ai-agent (+Google blog Ask Maps Nov 16, Android Authority, Digital Trends, Google Search Help; 0 X; new tool google-ask-maps); keep-an-ai-agent-from-deleting-your-files (+Tom's Hardware, HN 50499114 51/75; 0 X). New links this run: 13, of which 1 X (8%). Refreshed 53 X popularity blocks.
- Mentions/feedback of BotsDoThat: none found (X search since Nov 12 only unrelated "bots do that" phrases; HN Algolia 0 hits; Reddit RSS search empty, scores blocked from this box).

## After midday trending (measured 2026-11-17)

- Use cases: **132**; source links: **578**
- X share of source links: **82/578 = 14%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **82/290 = 28%**
- X-only use cases (every source is an X post): **4** (3%) — book-a-haircut-by-email is no longer X-only
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **93**
- By domain: youtube.com 91, x.com 82, news.ycombinator.com 49, reddit.com 33, google.com 26, github.com 25, support.google.com 22, help.openai.com 18, support.claude.com 14, techcrunch.com 7, blog.google 7, docs.anthropic.com 7
- Added this run: get-a-daily-training-check-in-from-your-fitness-watch (9 sources, 2 X: @mikepat711 X article 51 likes / 64 bookmarks / 12,620 views, @hellobeekay 3 likes; Reddit r/the5krunner Daash thread, Reddit r/Garmin beginner question, HN 50081045 61/74, GitHub Taxuspt/garmin_mcp 1,516 stars, Daash, garmlink and Garmin Community MCP setup guides).
- Extended: book-a-haircut-by-email (+TechCrunch, Engadget on Ask Maps appointment finding/calls; 0 X); teach-your-bot-to-remember-what-works (+reader tip: keep a dated copy of the notes file before letting the bot tidy it). New links this run: 11, of which 2 X (18%).
- Refreshed: 54 X popularity blocks + 64 community stats (42 Hacker News items via Algolia, 22 GitHub repos via API). Biggest moves: HN Coway 423→801 points, n8n-io/nod 991→2,280 stars, FrigadeHQ/yogurt 826→1,977, zigzag 565→889, hob 243→551, pinky 1,990→2,364, poki 1,022→1,563. Non-X share of refreshed items: 64/118 = 54%.
- Mentions/feedback of BotsDoThat: one reply to @botsdothat (X @NabhaniMehdi, 2026-11-16, on the "dreaming" memory post): suggestion to keep a dated copy of the notes file; folded into teach-your-bot-to-remember-what-works. HN Algolia 0 hits; Reddit blocked from this box.

## After midday trending (measured 2026-11-18)

- Use cases: **134**; source links: **592**
- X share of source links: **87/592 = 15%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **87/296 = 29%**
- X-only use cases (every source is an X post): **4** (3%)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **94**
- By domain: youtube.com 91, x.com 87, news.ycombinator.com 49, reddit.com 34, google.com 26, github.com 25, support.google.com 23, help.openai.com 18, support.claude.com 14, blog.google 9, techcrunch.com 8, docs.anthropic.com 7
- Added this run: book-a-car-service-by-letting-ai-call-the-shops (5 sources, 1 X: @GeminiApp Tasks launch 3,112 likes / 264 reposts / 728,025 views; Google blog dealership example, TechCrunch, Android Authority, The Verge); get-a-meeting-prep-brief-every-morning (5 sources, 2 X: @WesRoth 32 likes / 2,267 views, @free_ai_guides morning-page prompt 17 likes / 35 bookmarks / 4,657 views; Google blog, Reddit r/AI_Agents morning-briefing thread, Gemini Apps Help).
- Extended: make-a-customer-service-call (+@derariob Muse got a lost Express receipt emailed, 150 views; +Android Authority); reorder-your-regular-groceries (+@JeremyCainadian Gemini Tasks Walmart cart, 405 views; +The Verge). New links this run: 14, of which 5 X (36%).
- Refreshed: 55 X popularity blocks + 64 community stats (42 Hacker News via Algolia, 22 GitHub via API). Biggest moves: n8n-io/nod 2,280→2,470 stars, FrigadeHQ/yogurt 1,977→2,294, pinky 2,364→2,453. Non-X share of refreshed items: 64/119 = 54%.
- Mentions/feedback of BotsDoThat: none found (X search since Nov 17: only our own @botsdothat posts and unrelated "bots do that" phrases; HN Algolia 0 hits; Reddit blocked from this box).

## After midday trending (measured 2026-11-19)

- Use cases: **137**; source links: **613**
- X share of source links: **92/613 = 15%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **92/306 = 30%**
- X-only use cases (every source is an X post): **2** (1%; give-your-agents-a-shared-apple-account and one-bot-per-brand now have non-X sources)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **98**
- By domain: x.com 92, youtube.com 91, news.ycombinator.com 49, reddit.com 38, github.com 26, google.com 26, support.google.com 23, help.openai.com 18, support.claude.com 14, blog.google 9, techcrunch.com 8, docs.anthropic.com 7
- Added this run: onboard-a-new-bot-by-talking-it-through (5 sources, 1 X: @poteto 1,726 likes / 78 reposts / 628 bookmarks / 107,980 views; SpaceXSI accounting-team post, Reddit r/AI_Agents u/supermario218, Agent Cookbook, Grok Bot changelog); ask-your-bot-where-you-put-things (4 sources, 0 X: Reddit u/supermario218, Agent Cookbook, Wheredai on OpenApps, OnHand); have-your-bot-fax-an-office-that-wont-answer (5 sources, 1 X: @CtnMcKinley1971 0 likes / 32 views; Artificially Nerdy, Faxwell guide, GitHub vannet/gotfreefax-mcp 0 stars, Faxify MCP).
- Extended: line-up-contractors-for-a-home-project (+@thecsguy 31 likes / 2,078 views, now the popularity post; +The Agent Field newsletter); make-a-customer-service-call (+@poetnchief Muse patched him in for a PIN, 52 views); weekend-family-activities (+@RealDavidIsrael Dot suggested a family event unprompted, 35 views; +Reddit r/AI_Agents daily local-events agent); give-your-agents-a-shared-apple-account (+Reddit); one-bot-per-brand (+SpaceXSI official). New links this run: 21, of which 5 X (24%).
- Refreshed: 56 X popularity blocks + 64 community stats (42 Hacker News via Algolia, 22 GitHub via API). Biggest moves: @GeminiApp Tasks post 3,112→3,292 likes (728,025→870,557 views), n8n-io/nod 2,470→2,644 stars, FrigadeHQ/yogurt 2,294→2,579, DIYgod/pinky 2,453→2,527. Non-X share of refreshed items: 64/120 = 53%.
- Mentions/feedback of BotsDoThat: none found (X search Nov 17-19 for botsdothat / @botsdothat / url:botsdothat.com: 0 results; "bots do that" phrase hits are unrelated; HN Algolia 0 hits; Reddit blocked from this box, nothing found via web search).

## After midday trending (measured 2026-11-20)

- Use cases: **140**; source links: **631**
- X share of source links: **100/631 = 16%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **100/315 = 32%**
- X-only use cases (every source is an X post): **1** (1%; prescription-ready-and-time-to-leave now has Gemini Apps Help + Engadget; get-roadside-help-abroad is the last one)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **99**
- By domain: x.com 100, youtube.com 91, news.ycombinator.com 49, reddit.com 39, github.com 26, google.com 26, support.google.com 24, help.openai.com 18, support.claude.com 14, blog.google 9, techcrunch.com 8, docs.anthropic.com 7
- Added this run: check-on-every-package-and-chase-the-late-ones (5 sources, 2 X: TechRadar Gemini Tasks hands-on 2026-11-20; @silentguyy66 48 likes / 30 bookmarks / 1,114 views; Bot Shelf Package Tracker template; Grok Bot Templates Order Concierge; @lutefiskguy reply); keep-hidden-instructions-in-email-from-steering-your-bot (4 sources, 1 X: Grok Bot security docs, Meta "How We Built Safety Into Muse", Get Personal AI Agents prompt-injection explainer, @jwilkes Inbox Sentry 12 views); rebook-your-clients-after-a-surprise-schedule-change (3 sources, 2 X: @ShuiCohen 2 likes / 62 views, Reddit r/SaaS salon/barber WhatsApp booking thread, @lukesammons Clinic Desk 26 views).
- Extended: rebook-a-delayed-flight (+@therookiehacker rental car held from the plane; + watch-out), pay-with-a-single-use-virtual-card (+@alexmichael Grok Bot purchase passkeys 219 likes / 14 reposts / 89 bookmarks / 11,063 views; +Up to Speed with AI write-up; + watch-out), book-an-appointment-with-an-ai-agent (+@lukesammons), prescription-ready-and-time-to-leave (X-only → +Gemini Apps Help, +Engadget). New links this run: 18, of which 8 X (44%).
- Refreshed: 59 X popularity blocks + 64 community stats (42 Hacker News via Algolia, 22 GitHub via API). Biggest moves: @GeminiApp Tasks post 3,292→3,324 likes (870,557→1,034,848 views), @poteto 1,726→1,739 likes (107,980→116,250 views), n8n-io/nod 2,644→2,792 stars, FrigadeHQ/yogurt 2,579→2,737, browser-use 121,498→121,606. Non-X share of new + refreshed items: 74/141 = 52%.
- Mentions/feedback of BotsDoThat: none found (X search Nov 18-20 for botsdothat / @botsdothat / url:botsdothat.com, excluding our own account: 0 results; HN Algolia 0 hits; web search returns only botsdothat.com's own pages; Reddit blocked from this box).

## After midday trending (measured 2026-11-23)

- Use cases: **142**; source links: **646**
- X share of source links: **105/646 = 16%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **105/317 = 33%**
- X-only use cases (every source is an X post): **1** (get-roadside-help-abroad)
- By domain: x.com 105, youtube.com 91, news.ycombinator.com 49, reddit.com 40, support.google.com 26, github.com 26, google.com 26, help.openai.com 18, support.claude.com 14, blog.google 10, techcrunch.com 8, docs.anthropic.com 7
- Added this run: have-your-bot-call-stores-to-check-if-something-is-in-stock (8 sources, 3 X: @theshaneemoret Home Depot Christmas-tree call 995 likes / 53 reposts / 377 bookmarks / 384,514 views and Publix follow-up 15 likes / 2,158 views; @FlipFlip daily restock calls 33 likes / 12,060 views; Google Shopping Help "Let Google call", Gemini Apps Help calls, Google blog, Digital Trends Pixel Drop, Usecasy ring-round guide); run-the-family-secret-santa-with-your-bot (5 sources, 2 X: @sjpusey 4 likes / 3 replies / 114 views; Agents 101 write-up, secretsanta.name MCP server, Reddit r/ChristmasGiftIdeas 4 points / 22 comments, @oddorithm 38-ask random-draw test 38 views).
- Extended: morning-news-digest (+@lalovestrump personalized local newsletter, 11 likes / 847 views; + watch-out), call-and-book-by-phone (+Agents In Use 5-venue Christmas party booking, +Usecasy call-brief guide; + watch-out), have-your-bot-fax-an-office-that-wont-answer (deleted X post removed, popularity null). New links this run: 16, of which 6 X (38%).
- Refreshed: 60 X popularity blocks (1 deleted post dropped) + 65 community stats (42 Hacker News via Algolia, 23 GitHub via API). Biggest moves: n8n-io/nod 2,792→3,237 stars, FrigadeHQ/yogurt 2,737→3,057, browser-use 121,606→121,846; @GeminiApp Tasks post 3,324→3,382 likes (1,034,848→1,284,038 views), @poteto 1,739→1,761 likes (116,250→131,638 views). Non-X share of new + refreshed items: 75/141 = 53%.
- Mentions/feedback of BotsDoThat: none found (X search Nov 20-23 for botsdothat / "botsdothat.com" / url:botsdothat.com excluding our account: 0 results; HN Algolia "botsdothat" since Nov 20: 0 hits; Reddit blocked from this box).

## After midday trending (measured 2026-11-24)

- Use cases: **144**; source links: **658**
- X share of source links: **112/658 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **112/329 = 34%**
- X-only use cases (every source is an X post): **1** (get-roadside-help-abroad)
- By domain: x.com 112, youtube.com 91, news.ycombinator.com 49, reddit.com 41, support.google.com 26, github.com 26, google.com 26, help.openai.com 18, support.claude.com 14, blog.google 10, techcrunch.com 8, docs.anthropic.com 7
- Added this run: let-your-bot-project-manage-your-holiday-dinner (5 sources, 3 X: AI-Empowered Mom four-agent Thanksgiving test 2026-11-22; The Weekend Queue #6 Gemini Tasks Thanksgiving handoff 2026-11-20; @CatOrman1 Muse Instacart 32 likes / 2,197 views; @ErinnFL Grok Bot game plan + timers 11 likes / 307 views; @WhatPeopleDoAI two-turkey host 126 views); have-your-bot-grab-an-earlier-appointment-when-one-opens (5 sources, 2 X: @LaiskyCai ChatGPT Dots Costco tire slot 5 likes / 552 views; August official article; @anuruddh_m August launch 2,075 likes / 508 reposts / 3,658,368 views; Reddit r/MetaAI Muse restaurant cancellation 6 points / 4 comments; Muse Task Hub cancellation-watch page).
- Extended: team-of-agents-with-roles (+@michaelhyunkim three agents from three products coordinating by email, 30 likes / 714 views; + watch-out), keep-prompts-and-context-short (+@DaveMiz bots re-reading 95k tokens of chat, 85 views; + watch-out). New links this run: 12, of which 7 X (58%).
- Refreshed: 62 X popularity blocks + 65 community stats (42 Hacker News via Algolia, 23 GitHub via API). Biggest moves: n8n-io/nod 3,237→3,366 stars, FrigadeHQ/yogurt 3,057→3,178, browser-use 121,846→121,928; @GeminiApp Tasks post 3,382→3,399 likes (1,284,038→1,415,051 views). Non-X share of new + refreshed items: 70/139 = 50%.
- Mentions/feedback of BotsDoThat: 1 citation, no feedback. X Article by @WestAIcommerce, "每日你好｜11月23日（周一 · 美股更新）" (2026-11-24 00:56 UTC, 323 views, 0 likes), lists "Anthropic 数学家称 Claude 协助完成黎曼猜想证明，验证工具确认无误（botsdothat，11/22）" with botsdothat as the source (https://x.com/WestAIcommerce/status/2125030700240023932). HN Algolia "botsdothat": 0 hits; Reddit blocked from this box.

## After midday trending (measured 2026-11-25)

- Use cases: **146**; source links: **675**
- X share of source links: **116/675 = 17%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **116/334 = 35%**
- X-only use cases (every source is an X post): **1** (get-roadside-help-abroad)
- By domain: x.com 116, youtube.com 91, news.ycombinator.com 49, reddit.com 42, support.google.com 26, github.com 26, google.com 26, help.openai.com 19, support.claude.com 14, blog.google 10, techcrunch.com 8, docs.anthropic.com 7
- Added this run: plan-gifts-for-everyone-on-your-list-and-hit-the-order-by-dates (6 sources, 2 X: @ShannonMFHill first Grok Bot gift-list organizer 15 likes / 6 reposts / 400 views; BAARP gift-list-and-budget guide 2026-11-09; todo.is gift-list prompt page; Grokbot Agents holiday gift-list template updated 2026-11-10; @BurnsZA 29 views; Reddit r/Gifts gift-idea tracking thread 1 point / 54 comments); set-up-a-talk-to-it-bot-for-a-parent-who-finds-typing-hard (5 sources, 1 X: @evrgn11112231 Muse for his mom's non-profit report and his dad with arthritis 262 likes / 52 bookmarks / 16,156 views; Ask It Simply one-visit setup guide; Future Leaders in AI parent guide; Meta newsroom Muse voice; OpenAI Help ChatGPT Voice).
- Extended: remove-your-number-from-people-search-sites (+@ScottyBeamIO 14 sites, three agents, re-check every 3 months, 57 likes / 1,118 views; + watch-out), keep-hidden-instructions-in-email-from-steering-your-bot (+Clam AI Product Hunt #3, 184 upvotes / 13 comments; + watch-out), team-of-agents-with-roles (+Agent Relay family Thanksgiving channel blog, +AI with Remy OpenPod newsletter; + watch-out), plan-a-trip-itinerary (+AIvsTool timed Thanksgiving-drive test; + watch-out), turn-your-booking-emails-into-one-trip-sheet (+GPT Dot 54-trip travel page). New links this run: 17, of which 4 X (24%).
- Refreshed: 64 existing X popularity blocks (+2 new, 66 in one get_posts_by_ids call) + 65 community stats (42 Hacker News via Algolia, 23 GitHub via API; browser-use re-measured separately after a timeout). Biggest moves: n8n-io/nod 3,366→3,491 stars, FrigadeHQ/yogurt 3,178→3,495, JosssphZhou/poki 1,911→2,063; @GeminiApp Tasks post 3,399→3,419 likes (1,473,004 views). Non-X share of new links + refreshed items: 78/146 = 53%.
- Mentions/feedback of BotsDoThat: 1 citation, no feedback. X post by @yu_luo26312, "每日 AI 行业简报 · 2026-11-25" (2026-11-25 00:58 UTC, 652 views / 2 likes), lists "botsdothat" among its cross-check sources and says Claude Ship is "本周 X 上讨论度最高的 agent 新品之一（botsdothat 趋势第 2）" (https://x.com/yu_luo26312/status/2125393672229491197). @WestAIcommerce's Nov 24 citation now 401 views. HN Algolia "botsdothat" (30 days): 0 hits; Reddit blocked from this box (403), web search found nothing.

## After midday trending (measured 2026-11-26)
- Use cases: **148**; source links: **693**
- X share of source links: **122/693 = 18%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **122/341 = 36%**
- X-only use cases (every source is an X post): **1** (get-roadside-help-abroad)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **103**
- By domain: x.com 122, youtube.com 91, news.ycombinator.com 49, reddit.com 42, github.com 27, support.google.com 26, google.com 26, help.openai.com 19, support.claude.com 14, blog.google 11, techcrunch.com 8, docs.anthropic.com 7
- Added this run: have-your-bot-build-your-holiday-card-list-and-find-missing-addresses (5 sources, 1 X: Khe Hy Substack ChatGPT dot gathers addresses from Excel, email and iMessage into Notion and exports a Shutterfly CSV, 2026-11-19; @rpeacock75 Grok Bot moved the family card setup Minted to Shutterfly 6 likes / 343 views; Every Prompt Grok Bot card-list + label template; Picpost holiday page "Can my AI assistant make my list?"; Banjos address-request workflow); get-a-leave-time-check-before-a-long-holiday-drive (6 sources, 1 X: @BrianRoemmele Drive Window Grok Bot 13 likes / 3 reposts / 9 bookmarks / 4,645 views; Google blog Maps holiday traffic trends 2026-11-16; Willamette News Practical AI Thanksgiving drive + TripCheck 2026-11-16; Navi leave-time texts; Musecases shared Muse prompt; GitHub nicglazkov/commutescout 6 stars).
- Extended: team-of-agents-with-roles (+MyClaw 3.0 Product Hunt #1 Nov 25, 334 upvotes / 61 comments; +@leodev one agent per project + chief of staff, 250 likes / 316 bookmarks / 22,799 views; + watch-out), hire-a-chief-of-staff-bot (+Airbot Product Hunt #2 Nov 25, 294 upvotes / 64 comments; + watch-out), call-and-book-by-phone (+Hai Product Hunt #8 Nov 25, 108 upvotes / 16 comments; +@AmineTX first garage-repair shop hung up on the AI, 5 likes / 318 views; + watch-out), schedule-bots-without-burning-tokens (+@irongiantXBT event router instead of polling, 47 likes / 71 bookmarks / 4,036 views; + watch-out), teach-your-bot-to-remember-what-works (+@choopyplug1 playbook after every job, 37 likes / 761 views). New links this run: 18, of which 6 X (33%).
- Refreshed: 66 existing X popularity blocks (+2 new, 68 merged from one get_posts_by_ids call of 66 + one 12-post candidate lookup) + 65 community stats (42 Hacker News via Algolia, 23 GitHub via API). Biggest moves: n8n-io/nod 3,491→3,888 stars, FrigadeHQ/yogurt 3,495→3,663, JosssphZhou/poki 2,063→2,139, browser-use 122,047→122,138; @evrgn11112231 talk-to-it post 262→279 likes (16,156→19,694 views); @GeminiApp Tasks post 3,419→3,429 likes (1,484,526 views). Non-X share of new links + refreshed items: 77/149 = 52%.
- Mentions/feedback of BotsDoThat: none found. X search Nov 25 12:00 UTC to now for botsdothat / "botsdothat.com" / url:botsdothat.com excluding our account: 0 results; HN Algolia "botsdothat" and "botsdothat.com" (30 days, stories + comments): 0 hits; Reddit blocked from this box (403); web search returned only botsdothat.com's own pages (our /how-to-use-chatgpt-dots/ guide ranked first for a generic "how I set up an AI agent" query).

## After midday trending (measured 2026-11-27)
- Use cases: **150**; source links: **718**
- X share of source links: **130/718 = 18%**
- X share of community links (X, Reddit, Hacker News, YouTube, GitHub, Product Hunt): **130/352 = 37%**
- X-only use cases (every source is an X post): **1** (get-roadside-help-abroad)
- Use cases with at least one non-X community source (Reddit, Hacker News, YouTube, GitHub, Product Hunt): **105**
- By domain: x.com 130, youtube.com 91, news.ycombinator.com 51, reddit.com 43, support.google.com 27, github.com 27, google.com 26, help.openai.com 20, support.claude.com 14, blog.google 11, techcrunch.com 9, docs.anthropic.com 7
- Added this run: turn-a-saved-recipe-video-into-a-grocery-list (8 sources, 1 X: Meta UK Muse post "turn a recipe Reel you've saved into a shopping list" 2026-11-23; TechCrunch Muse in Instagram DMs 2026-11-24; Instagram on Threads; MediaPost; gemini.google "List the ingredients from this cooking video"; Gemini Apps Help Keep lists; TheNextGenAI tested Keep prompt 2026-11-19; @HamonPaulm Claude on a cloud iPhone, 17 likes / 943 views); get-a-short-lesson-every-morning-on-something-you-want-to-learn (8 sources, 3 X: @parker__conrad daily painting lesson 188 likes / 9,609 views; @guidetoaitool 15-minute tutor template; @SusanVadenMeser daily Grok Bot lesson; OpenAI Help scheduled tasks; MakeUseOf spaced repetition with Tasks; dusk.bot learning prompts; FreakyJolly; LinkedIn morning brief + daily lesson).
- Extended: keep-hidden-instructions-in-email-from-steering-your-bot (+Reddit r/ClaudeCode Notion MCP upsell instructions; +HN 50658093 58 points / 22 comments; + watch-out), let-ai-send-emails-for-you (+Tech Stackups Google Workspace MCP rule; +HN 50653477 408 points / 327 comments; + watch-out), build-a-second-brain-your-bot-reads (+Obsidian Help connectors; +@0xAIlabs shared vault with conflicts note and inbox folder, 49 likes / 1,324 views; + watch-out), give-your-agent-its-own-email-address (+@Yumzlef separate shopping inbox, 486 emails / 3 reached the person, 47 likes / 805 views), have-two-ais-check-each-other (+@_simonsmith OpenRouter second opinions inside Muse, 61 likes / 5,245 views), have-your-bot-call-stores-to-check-if-something-is-in-stock (+@Scott_Weidig Thanksgiving Eve pitcher hold). New links this run: 25, of which 8 X (32%).
- Refreshed: 68 existing X popularity blocks (+2 new = 70 merged; one 68-id get_posts_by_ids call + one 14-post candidate lookup) + 66 community stats (42 Hacker News via Algolia, 24 GitHub via API). Non-X share of new links + refreshed items: 83/161 = 52%.
- Mentions/feedback of BotsDoThat: none found. X search Nov 26 12:00 UTC to now (botsdothat / "botsdothat.com" / url:botsdothat.com, excluding our account): 0; HN Algolia "botsdothat" / "botsdothat.com" (30 days): 0; Reddit still 403 from the box (old.reddit JSON too).
