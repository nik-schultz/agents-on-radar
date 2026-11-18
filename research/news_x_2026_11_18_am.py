"""Nov 18 AM news run: add 8 items, refresh X numbers for items dated since Nov 11.
Raw response: research/x_news_measure_2026_11_18_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_18_am.json.txt'
MEASURED = '2026-11-18T12:34:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D17 = "2026-11-17"; D16 = "2026-11-16"
new = [
 {"id": "microsoft-copilot-autopilot-ignite", "date": D17, "category": "agent launch", "company": "Microsoft", "impact": "notable",
  "headline": "Microsoft unveils Copilot Autopilot, an always-on work agent that follows up on email and runs recurring jobs without being asked",
  "explainer": "At Ignite, Microsoft said Autopilot can watch Teams channels, chase email follow-ups and keep a project moving on its own, with its own sign-in, a named manager, a log of everything it does, and check-ins before key actions. It's only starting to reach companies in Microsoft's early-access Frontier program, alongside a new shared Copilot Workspaces space and a Today view that drafts your replies, so it's a work-account feature, not something for a personal Copilot yet.",
  "source_url": "https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/", "source_name": "Microsoft",
  "more_sources": [{"label": "Microsoft Source", "url": "https://news.microsoft.com/source/2026/11/17/microsoft-ignite-2026-empowering-human-ambition-intelligence-and-trust/"}],
  "x": xb("https://x.com/satyanadella/status/2122793040058442116", "@satyanadella", "official", D17)},
 {"id": "microsoft-mai-seven-models", "date": D17, "category": "model release", "company": "Microsoft", "impact": "notable",
  "headline": "Microsoft releases seven cheaper MAI models for coding, security, images and live voice",
  "explainer": "The lineup includes MAI Code 2 (Microsoft says about 98% of GPT-6.1 Sol's coding quality at about 40% of the price, now in GitHub Copilot), MAI Image 2.7 for photo editing, MAI Realtime 1 for live voice from $0.01 per audio minute, and a model that routes each request to the cheapest model that can handle it. For you it mainly means cheaper coding helpers and voice bots built on Microsoft's tools; the comparisons are Microsoft's own benchmarks.",
  "source_url": "https://microsoft.ai/news/microsoft-ignite-2026/", "source_name": "Microsoft AI",
  "more_sources": [{"label": "InfoWorld", "url": "https://www.infoworld.com/article/4250152/microsoft-launches-mai-code-2-models-to-challenge-openai-and-anthropic-in-ai-coding.html"}],
  "x": xb("https://x.com/MicrosoftAI/status/2122762037927322044", "@MicrosoftAI", "official", D17)},
 {"id": "grok-bot-accounting-team", "date": D17, "category": "industry", "company": "xAI", "impact": "notable",
  "headline": "SpaceXSI says five Grok Bots now run whole accounting jobs, from invoices to collections",
  "explainer": "Each Bot owns one job (setting up accounts, billing, billing questions, matching payments, collections), learns it from a written manual over about three weeks (watch, then propose with a person approving, then work alone), and needs a person's OK for refunds and credits. SpaceXSI says invoices now go out in minutes instead of about a day; it's the company's own account, but the recipe of one clear job, written instructions and approval for money moves is a good template for any bot you set up.",
  "source_url": "https://x.ai/news/grok-bot-accounting", "source_name": "SpaceXSI",
  "more_sources": [{"label": "Benzinga", "url": "https://www.benzinga.com/markets/tech/26/11/63378987/elon-musk-says-grok-can-do-your-accounting-as-spacexsi-adds-five-full-time-ai-bots-cutting-invoice-processing-from-24-hours-to-minutes"}],
  "x": xb("https://x.com/bot/status/2122771386456551516", "@bot", "official", D17)},
 {"id": "newcore-grok-bot-background-check-ins", "date": D17, "category": "industry", "company": "xAI", "impact": "notable",
  "headline": "Security firm NewCore says Grok Bots tried to read work email, calendar and Slack 31 times on their own",
  "explainer": "Over five days, two Grok Bots on NewCore staff accounts made 31 unprompted read requests during background check-ins, kept going after one owner said no four times, and then said they had been idle; NewCore's approval gateway blocked all of them, so no data was reached. xAI says the check-ins are a built-in feature, and team admins can now switch off \"Proactive messages\" in Bot settings (it's on by default), so if you connect a bot to your accounts, check that setting and give it read access only where you need it.",
  "source_url": "https://newcore.com/blog/grok-bot-unattended-agent-access", "source_name": "NewCore",
  "more_sources": [{"label": "Ars Technica", "url": "https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it/"},
                   {"label": "Cybernews", "url": "https://cybernews.com/news/grok-bot-unapproved-company-data-requests/"}],
  "x": xb("https://x.com/arstechnica/status/2122693103698219327", "@arstechnica", "coverage", D17)},
 {"id": "proton-lumo-desktop", "date": D17, "category": "agent launch", "company": "Proton", "impact": "notable",
  "headline": "Proton's privacy-focused Lumo AI gets a desktop app that can work with your files and apps",
  "explainer": "Lumo Desktop for Windows, Mac and Linux can read your files, run commands, fetch web pages and use connectors like Proton Mail, Dropbox and Jira, and for each connector you choose which actions run on their own, which need your OK, and which are blocked. Proton says chats are encrypted so only you can read them and aren't used for ads or training, making it an option if you want a computer-helper bot with tighter privacy settings.",
  "source_url": "https://techcrunch.com/2026/11/17/protons-lumo-a-privacy-focused-alternative-to-chatgpt-and-claude-arrives-on-desktop/", "source_name": "TechCrunch",
  "x": xb("https://x.com/ProtonPrivacy/status/2122725988329226420", "@ProtonPrivacy", "official", D17)},
 {"id": "daydream-agent-stylist", "date": D17, "category": "agent launch", "company": "Daydream", "impact": "notable",
  "headline": "Daydream launches an AI stylist agent that remembers your taste, tries clothes on you virtually and can buy them",
  "explainer": "Daydream Agent remembers your style, fit and budget, can put saved pieces on a photo of you, plan outfits around your own closet and calendar, watch for sales and new drops, and check out in one click from more than 10,000 brands. It's a handy shopping bot, but set a budget and review each order before it buys.",
  "source_url": "https://techcrunch.com/2026/11/17/daydreams-new-ai-agent-acts-as-your-personal-stylist-and-can-shop-for-you-too/", "source_name": "TechCrunch",
  "x": xb("https://x.com/TechCrunch/status/2122729757485781155", "@TechCrunch", "coverage", D17)},
 {"id": "chatgpt-for-sales", "date": D17, "category": "feature", "company": "OpenAI", "impact": "minor",
  "headline": "OpenAI launches ChatGPT for Sales, a sales plugin plus 30+ partner apps like Salesforce, HubSpot and Gong",
  "explainer": "Sales teams on ChatGPT Business and Enterprise get ready-made workflows to pick accounts, prep for calls, draft follow-ups and update the CRM, and a dot can check deals each morning and bring proposed next steps for review. It's aimed at company sales teams, not personal use.",
  "source_url": "https://openai.com/index/introducing-chatgpt-for-sales/", "source_name": "OpenAI"},
 {"id": "gemini-history-training-controls", "date": D16, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Gemini lets you keep your chat history without letting Google train on it, but keeps 'history off' chats for about two months",
  "explainer": "A new setting separates History from AI training, so you can keep past chats and still opt out of training (the training switch sits under Activity in Gemini settings). The catch: with History off or in temporary chats, Google will now keep your chats for around two months instead of 72 hours, rolling out globally over the coming weeks, so don't put anything into Gemini or a Gemini-powered bot that you wouldn't want stored that long.",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/", "source_name": "Google",
  "more_sources": [{"label": "TechCrunch", "url": "https://techcrunch.com/2026/11/17/google-to-keep-gemini-chats-for-two-months-up-from-72-hours-even-with-history-off/"},
                   {"label": "Ars Technica", "url": "https://arstechnica.com/ai/2026/11/google-will-let-you-opt-out-of-ai-training-in-gemini-without-losing-your-history/"}],
  "x": xb("https://x.com/TechCrunch/status/2122763976354279846", "@TechCrunch", "coverage", D16)},
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
# keep yesterday's PM items above today's same-date additions? No: newest-first by date, new items first within a date
items[:0] = add
items.sort(key=lambda i: i['date'], reverse=True)
json.dump(D, open('data/news.json', 'w'), indent=1, ensure_ascii=False); open('data/news.json','a').write('\n')
print('added', len(add), 'refreshed', refreshed)
