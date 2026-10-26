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

