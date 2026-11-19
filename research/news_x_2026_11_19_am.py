"""Nov 19 AM news run: add 11 items, refresh X numbers for items dated since Nov 12.
Raw response: research/x_news_measure_2026_11_19_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_19_am.json.txt'
MEASURED = '2026-11-19T12:28:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D18 = "2026-11-18"; D17 = "2026-11-17"
new = [
 {"id": "gemini-4-neon", "date": D18, "category": "model release", "company": "Google", "impact": "major",
  "headline": "Google releases Gemini 4 Neon, a fast model that Google says nearly matches its top Carbon model on hard work",
  "explainer": "If you pay for Google AI Pro or Ultra, you can now pick Gemini 4 Neon (\"Deeper analysis\") in the Gemini app for long documents, spreadsheets and multi-step agent jobs, and Google says it makes things up less often than its earlier models. Developers pay $3 per million input tokens and $15 per million output tokens with no free tier, which works out cheaper than Carbon once Carbon's promo price ends on Nov 30.",
  "source_url": "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/", "source_name": "Google",
  "more_sources": [{"label": "Gemini API pricing", "url": "https://ai.google.dev/gemini-api/docs/pricing"},
                   {"label": "9to5Google", "url": "https://9to5google.com/2026/11/18/gemini-4-neon-announcement/"}],
  "x": xb("https://x.com/sundarpichai/status/2123167780988125621", "@sundarpichai", "official", D18)},
 {"id": "chatgpt-live-dictation", "date": D18, "category": "feature", "company": "OpenAI", "impact": "notable",
  "headline": "ChatGPT's dictation now types your words as you talk, and the 10-minute limit is gone",
  "explainer": "Tap the microphone and your words appear while you speak, so long voice notes, meeting recaps or brain dumps for your bot no longer get cut off at 10 minutes. It's rolling out to every ChatGPT plan on iPhone, Android, web and desktop; the audio stays with the chat until you delete it.",
  "source_url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes", "source_name": "ChatGPT release notes",
  "more_sources": [{"label": "9to5Mac", "url": "https://9to5mac.com/2026/11/18/chatgpt-app-gains-enhanced-live-dictation-streaming-without-10-minute-limit/"}],
  "x": xb("https://x.com/ChatGPT/status/2123114715257946334", "@ChatGPT", "official", D18)},
 {"id": "chatgpt-for-accounting", "date": D18, "category": "feature", "company": "OpenAI", "impact": "notable",
  "headline": "ChatGPT for Accounting: a free plugin that drafts bank reconciliations, invoice entries and month-end reports for you to check",
  "explainer": "In the ChatGPT desktop app with computer use, the Accounting plugin works from your spreadsheets or a connected app like QuickBooks Online, Xero, FreshBooks or BILL and prepares drafts, flagging missing or uncertain items for you to review. It's for ChatGPT Business and Enterprise workspaces (Enterprise admins must approve it first), so a small business owner or bookkeeper still signs off on every number.",
  "source_url": "https://help.openai.com/en/articles/20001709-using-chatgpt-for-accounting-work", "source_name": "OpenAI Help Center",
  "more_sources": [{"label": "ChatGPT release notes", "url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes"},
                   {"label": "Gadgets 360", "url": "https://www.gadgets360.com/ai/news/openai-chatgpt-live-dictation-update-release-accounting-features-12349148"}],
  "x": xb("https://x.com/ChatGPT/status/2123159134963196357", "@ChatGPT", "official", D18)},
 {"id": "anthropic-ipo-priced", "date": D18, "category": "industry", "company": "Anthropic", "impact": "notable",
  "headline": "Anthropic prices its IPO at $83 a share, raising about $81 billion, with trading on Nasdaq as ANT from Nov 19",
  "explainer": "The maker of Claude priced above its expected range in what CNBC calls the largest IPO on record. Nothing changes in your Claude app or plan today, but Claude's maker is now a public company answering to shareholders, so watch for its next moves on prices and plans.",
  "source_url": "https://www.anthropic.com/news/anthropic-prices-initial-public-offering", "source_name": "Anthropic",
  "more_sources": [{"label": "CNBC", "url": "https://www.cnbc.com/2026/11/18/anthropic-ipo-ai-offering-price.html"}],
  "x": xb("https://x.com/AnthropicAI/status/2123196808675405860", "@AnthropicAI", "official", D18)},
 {"id": "grok-bot-travel-booking", "date": D18, "category": "feature", "company": "xAI", "impact": "notable",
  "headline": "Grok Bot can now search and book flights, hotels and rental cars for you in one chat",
  "explainer": "Tell your Grok Bot where and when you're going and it compares fares, rooms and cars, shows bag and refund rules, maps and reviews, then books once you approve. Some airlines, such as United, don't let AI agents finish a booking, and the Bot sends you the link when it can't confirm the final purchase, so check the details before you say yes.",
  "source_url": "https://x.com/bot/status/2123121401762918718", "source_name": "Grok Bot on X",
  "more_sources": [{"label": "Grok Bot changelog", "url": "https://x.ai/changelog/bot"}],
  "x": xb("https://x.com/bot/status/2123121401762918718", "@bot", "official", D18)},
 {"id": "grok-bot-tool-permissions", "date": D18, "category": "feature", "company": "xAI", "impact": "minor",
  "headline": "Grok Bot lets you set each connected tool to Always allow, Auto-review, Needs approval or Blocked",
  "explainer": "On each connector's page you can now decide, tool by tool, what your Bot may do on its own, for example let it read your calendar freely but always ask before it sends an email. Routines that lose a sign-in now pause and send you a reconnect card instead of failing quietly, and new sign-ups must be 18 or older.",
  "source_url": "https://x.ai/changelog/bot", "source_name": "Grok Bot changelog"},
 {"id": "meta-muse-loblaw-canada", "date": D18, "category": "feature", "company": "Meta", "impact": "notable",
  "headline": "Canadians can now plan meals, fill a grocery basket and check out with Loblaw stores inside Meta's Muse",
  "explainer": "Loblaw is the first Canadian retailer connected to Muse, so you can ask your Muse for a week of meals and it builds the basket at participating Loblaw banners, remembering brands and food allergies for next time. Muse voice chats and Spaces (custom planners you describe) also reach Canada, and Muse asks before sensitive steps like a purchase.",
  "source_url": "https://about.fb.com/news/2026/11/meta-welcomes-loblaw-as-first-canadian-retail-partner-to-muse/", "source_name": "Meta",
  "more_sources": [{"label": "Loblaw", "url": "https://www.loblaw.ca/en/loblaw-becomes-first-canadian-retailer-to-bring-ai-powered-shopping-to-metas-muse/"}]},
 {"id": "banks-ai-agent-liability-citi-pnc", "date": D18, "category": "industry", "company": "Citi", "impact": "notable",
  "headline": "Citi, PNC and Citizens tell customers they're on the hook for anything their AI agents do in their bank accounts, even after a hack",
  "explainer": "Citi changed its online terms this week so that if you give a third-party AI agent your bank login and it makes a wrong payment, or the tool gets hacked, the losses are yours; JPMorgan and Bank of America announced similar policies last month. If your bot helps with money, keep it read-only (like summarizing statements) and make every payment yourself.",
  "source_url": "https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/", "source_name": "TechCrunch",
  "x": xb("https://x.com/TechCrunch/status/2123107245005189365", "@TechCrunch", "coverage", D18)},
 {"id": "mistral-vibe-desktop", "date": D17, "category": "agent launch", "company": "Mistral", "impact": "minor",
  "headline": "Mistral launches Vibe Desktop, a Mac and Windows app for its Work and coding agents",
  "explainer": "Vibe Desktop puts Mistral's Vibe Work assistant and its coding agent in one app that can use folders on your computer or run tasks in a cloud sandbox while you do something else. It's mostly for people who code or use Mistral at work; Linux support is coming later.",
  "source_url": "https://docs.mistral.ai/resources/release-notes", "source_name": "Mistral docs",
  "x": xb("https://x.com/MistralAI/status/2123073168659141119", "@MistralAI", "official", D18)},
 {"id": "google-ai-mode-temporary-threads", "date": D17, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Google Search's AI Mode gets temporary threads, a private mode that isn't saved to your history",
  "explainer": "Click the temporary threads icon in the top-right of AI Mode and that conversation won't show up in your search history, won't use your past activity and won't shape future recommendations, which helps for health, money or gift questions. It's rolling out worldwide on desktop and mobile, and a closed thread can't be recovered.",
  "source_url": "https://blog.google/products-and-platforms/products/search/temporary-threads-ai-mode/", "source_name": "Google",
  "more_sources": [{"label": "Google Search Help", "url": "https://support.google.com/websearch/answer/18752729"},
                   {"label": "TechCrunch", "url": "https://techcrunch.com/2026/11/18/googles-ai-feature-in-search-gets-its-own-incognito-mode/"}],
  "x": xb("https://x.com/9to5Google/status/2122736668121661520", "@9to5Google", "coverage", D17)},
 {"id": "x-pauses-grok-training-agent-data-ireland", "date": D17, "category": "industry", "company": "xAI", "impact": "notable",
  "headline": "After Ireland's privacy regulator stepped in, X stopped training its AI on other people's data collected by Grok Bot",
  "explainer": "Ireland's Data Protection Commission told POLITICO that X had been using third-party data gathered by Grok Bot since late October, like details about people in photos or emails a user shares with the Bot, and agreed to suspend it. It's a reminder that what your agent reads about friends, family or clients can travel further than you expect; the regulator says it's also talking to another, unnamed tech company.",
  "source_url": "https://www.politico.eu/article/x-stops-training-ai-with-agents-data-after-ireland-intervened/", "source_name": "POLITICO Europe",
  "more_sources": [{"label": "heise online", "url": "https://www.heise.de/news/X-stoppt-Grok-KI-Training-mit-Drittanbieterdaten-auf-Druck-aus-Irland-11528427.html"}],
  "x": xb("https://x.com/POLITICOEurope/status/2122663275082973443", "@POLITICOEurope", "coverage", D17)},
]
D = json.load(open('data/news.json')); items = D['items']
have = {i['id'] for i in items}; refreshed = 0
for it in items:
    x = it.get('x')
    if not x: continue
    pid = x['url'].rsplit('/', 1)[1]
    if pid in pm:
        m = pm[pid]; x.update(likes=m['like_count'], reposts=m.get('repost_count', m.get('retweet_count')), views=m['impression_count'], measured_at=MEASURED); refreshed += 1
add = [n for n in new if n['id'] not in have]
items[:0] = add
items.sort(key=lambda i: i['date'], reverse=True)
json.dump(D, open('data/news.json', 'w'), indent=1, ensure_ascii=False); open('data/news.json','a').write('\n')
print('added', len(add), 'refreshed', refreshed)
