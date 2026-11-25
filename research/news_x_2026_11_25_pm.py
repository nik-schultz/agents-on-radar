"""Nov 25 PM news run: add 8 items, refresh X numbers for items dated since Nov 14.
Raw response: research/x_news_measure_2026_11_25_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_25_pm.json.txt'
MEASURED = '2026-11-25T20:37:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D5, D4 = "2026-11-25", "2026-11-24"
new = [
 {"id": "chatgpt-codex-shared-usage-limits", "date": D5, "category": "pricing", "company": "OpenAI", "impact": "notable",
  "headline": "From December, ChatGPT and Codex share one usage allowance on Plus, Pro and Business as Chat and Work merge",
  "explainer": "If you pay for ChatGPT Plus, Pro or Business, starting in December your chats, agent work and Codex coding will all draw from one allowance measured in tokens, so long agent or coding jobs can use up what you'd otherwise spend on chats; quick chats with the Instant model stay unlimited and don't count. OpenAI says most people won't wait for resets more often than now, but a spokesperson told TechCrunch a small share of the heaviest users may hit limits sooner; you'll see the combined total and reset times in Settings, then Usage, and a small group of Pro users already has the merged Chat and Work screen.",
  "source_url": "https://www.theverge.com/ai-artificial-intelligence/1042187/openai-is-combining-chatgpt-and-codex-usage-limits", "source_name": "The Verge",
  "more_sources": [{"label": "OpenAI Help Center (usage limits)", "url": "https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits"},
                   {"label": "TechCrunch", "url": "https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/"}],
  "x": xb("https://x.com/thsottiaux/status/2125284868414394550", "@thsottiaux", "official", D4)},
 {"id": "gemini-guided-vision-ios", "date": D5, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Guided Vision in Gemini Live comes to iPhone: point your camera and Gemini describes what it sees and tells you how to aim",
  "explainer": "If you're on an iPhone and are blind, have low vision or just can't read the small print, you can now share your camera in Gemini Live and get spoken descriptions plus cues like 'tilt down' or 'step back' until it can see what you asked about, such as a nutrition label, a washing-machine dial or a dropped earbud. It came to Android on Oct 1; Google says it can make mistakes and isn't a mobility aid or a replacement for a white cane.",
  "source_url": "https://x.com/GeminiApp/status/2125685936344236471", "source_name": "@GeminiApp on X",
  "more_sources": [{"label": "Google blog (Android launch, Oct 1)", "url": "https://blog.google/innovation-and-ai/products/gemini-app/guided-vision-gemini-live/"}],
  "x": xb("https://x.com/GeminiApp/status/2125685936344236471", "@GeminiApp", "official", D5)},
 {"id": "openai-private-inference-alpha", "date": D5, "category": "feature", "company": "OpenAI", "impact": "minor",
  "headline": "OpenAI starts testing Private Inference, which keeps business prompts sealed off even while the model works on them",
  "explainer": "Nothing changes in your personal ChatGPT; this is for businesses: OpenAI is testing Private Inference (an alpha) with a small group of customers, running prompts and replies on sealed-off 'confidential computing' hardware with controls customers can verify, similar to how Apple handles Siri's cloud requests. Sam Altman announced the test on Nov 25; OpenAI gave no date for a wider rollout.",
  "source_url": "https://thenextweb.com/news/openai-private-inference-testing-customers", "source_name": "The Next Web",
  "more_sources": [{"label": "OpenAI Private Intelligence", "url": "https://openai.com/business/private-intelligence/"}],
  "x": xb("https://x.com/sama/status/2125638790593274259", "@sama", "official", D5)},
 {"id": "perplexity-time-machine-api", "date": D5, "category": "feature", "company": "Perplexity", "impact": "minor",
  "headline": "Perplexity's Time Machine lets developers search the web as it was on a past date, up to a year back",
  "explainer": "Nothing changes in the Perplexity app; this is for people building or testing AI agents: Perplexity's Search and Context APIs can now show only the web as it was at a chosen date (up to 365 days back), so a research or forecasting agent can be graded on past questions without finding the answer that was published later. It costs the same as normal requests, $5 per 1,000 searches and $1 per 1,000 pages read.",
  "source_url": "https://www.unite.ai/perplexity-launches-time-machine-for-point-in-time-web-retrieval/", "source_name": "Unite.AI",
  "x": xb("https://x.com/perplexitydevs/status/2125676416834605488", "@perplexitydevs", "official", D5)},
 {"id": "grok-bot-1-3-restock-alerts", "date": D4, "category": "feature", "company": "xAI", "impact": "notable",
  "headline": "Grok Bot 1.3 adds 'Notify me' restock alerts for sold-out products, Slack handoffs between Bots and an Ashby connector",
  "explainer": "If you shop with Grok Bot, a sold-out product card now has a Notify me button that watches that seller and tells you when the item is back, and if your X Money balance is too low the purchase is now refused before a card is issued, with the Bot asking you to add funds or pay another way. Version 1.3.0 also sends answers from one team Bot to another back to your Slack DMs, connects Microsoft Teams when you sign in with a work account and adds an Ashby connector for recruiting questions; Elon Musk is pitching Grok Bot this week for researching Black Friday deals and checking they're real.",
  "source_url": "https://x.ai/changelog/bot", "source_name": "Grok Bot changelog",
  "x": xb("https://x.com/elonmusk/status/2125464682580623467", "@elonmusk", "official", D5)},
 {"id": "google-workspace-agents-must-use-mcp", "date": D4, "category": "industry", "company": "Google", "impact": "notable",
  "headline": "Google says AI agents must reach Gmail, Drive and other Workspace data through its MCP connectors from Feb 1, 2027",
  "explainer": "If an AI assistant or agent reads your Gmail, Drive, Calendar or Docs, Google now requires it to use Google's own MCP connectors or Workspace command-line tool instead of the regular APIs, enforced from February 1, 2027; agents that keep calling the old APIs directly will be held to the free tier's limits. Workplace admins also get agent audit logs, data-loss rules and the option to make you confirm sensitive actions like reading outside files or sharing data; the free Standard tier covers over 99% of developers, and a paid Scaled tier for heavy use starts billing on April 1, 2027.",
  "source_url": "https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html", "source_name": "Google Workspace Updates",
  "more_sources": [{"label": "Google for Developers (usage tiers and dates)", "url": "https://developers.google.com/workspace/guides/quota-usage-tiers"},
                   {"label": "Workspace AI Tools Addendum", "url": "https://workspace.google.com/terms/ai-tools/"}]},
 {"id": "cognition-swe-2-1", "date": D4, "category": "model release", "company": "Cognition", "impact": "minor",
  "headline": "Cognition releases SWE-2.1 for Devin, free in Devin Desktop and CLI through Dec 8",
  "explainer": "Only matters if you use Devin for coding: Cognition's new SWE-2.1 model roughly doubles its predecessor's scores on coding tests such as Terminal-Bench 4.1 (50.0 vs 24.2) and is free in Devin Desktop and the CLI on Pro, Max and Teams through December 8, then $0.50/$2.50 per million input/output tokens through January 30, 2027 and $2/$10 after that. On Cognition's own charts it still trails Claude Opus 5.5, Gemini 4 Neon and GPT-6.2 Sol on most tests, and a version with looser safeguards, SWE-2.1 Cyber, is going to Devin Security.",
  "source_url": "https://cognition.com/blog/swe-2-1", "source_name": "Cognition",
  "more_sources": [{"label": "Devin docs (models and pricing)", "url": "https://docs.devin.ai/desktop/chat/models"}],
  "x": xb("https://x.com/cognition/status/2125305349414523061", "@cognition", "official", D4)},
 {"id": "gemini-regional-voices", "date": "2026-11-16", "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Gemini adds 66 regional voices with local accents, from Geordie and Scouse to Indian English and Korean",
  "explainer": "You can now give Gemini a voice with a local accent: 66 new voices across US, UK and Indian English, Hindi, Brazilian Portuguese, Indonesian and Korean, picked from the three-dot menu in Gemini Live or 'Gemini's voice' in the app's settings on Android and iPhone. The voice you choose is used across the app, including when Gemini reads an answer aloud, and Google says the voices are tuned for natural local rhythm rather than slang.",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-app/regional-voices/", "source_name": "Google blog",
  "more_sources": [{"label": "9to5Google", "url": "https://9to5google.com/2026/11/16/gemini-rolling-out-66-new-regional-voices-on-android-and-ios-including-10-uk-dialects/"}],
  "x": xb("https://x.com/GeminiApp/status/2125629066006950339", "@GeminiApp", "official", D5)},
]
Dd = json.load(open('data/news.json')); items = Dd['items']
byid = {i['id']: i for i in items}
have = set(byid); add = [n for n in new if n['id'] not in have]
refreshed = 0
for it in items:
    x = it.get('x')
    if not x: continue
    pid = x['url'].rsplit('/', 1)[1]
    if pid in pm:
        m = pm[pid]; x.update(likes=m['like_count'], reposts=m.get('repost_count', m.get('retweet_count')), views=m['impression_count'], measured_at=MEASURED); refreshed += 1
items[:0] = add
items.sort(key=lambda i: i['date'], reverse=True)
json.dump(Dd, open('data/news.json', 'w'), indent=1, ensure_ascii=False); open('data/news.json','a').write('\n')
print('added', len(add), 'refreshed existing', refreshed)
