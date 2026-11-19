"""Nov 19 PM news run: add 5 items, refresh X numbers for items dated since Nov 12.
Raw response: research/x_news_measure_2026_11_19_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_19_pm.json.txt'
MEASURED = '2026-11-19T20:30:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D19 = "2026-11-19"; D16 = "2026-11-16"
new = [
 {"id": "gemini-computer-use-mac", "date": D19, "category": "agent launch", "company": "Google", "impact": "notable",
  "headline": "Gemini's Mac app can now click, type and work through your apps and websites for you in a background window",
  "explainer": "Describe a chore, like copying details from PDFs into a shipping form or staging resale listings from a folder of photos, and Gemini does the clicking in a separate window while you keep using your Mac. You pick which apps it can touch and approve key steps; it's rolling out in English in the US for Google AI Plus, Pro and Ultra subscribers on Apple Silicon Macs (macOS 15+).",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/", "source_name": "Google",
  "more_sources": [{"label": "TechCrunch", "url": "https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/"}],
  "x": xb("https://x.com/9to5mac/status/2123490417559716018", "@9to5mac", "coverage", D19)},
 {"id": "meta-muse-privacy-reuters", "date": D19, "category": "industry", "company": "Meta", "impact": "notable",
  "headline": "Reuters: Meta staff say Muse mixed up people's conversations and showed other users' private details, like bank balances",
  "explainer": "Internal posts seen by Reuters describe Muse surfacing orders, childcare requests and bank balances that belonged to someone else, and nudging one employee about her Signal messages she didn't think it could see. Meta says employees test different versions than the public gets; if you use Muse, review which apps and notifications it can read and don't share more than the job needs.",
  "source_url": "https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/", "source_name": "TechCrunch",
  "x": xb("https://x.com/Cointelegraph/status/2123499173781610567", "@Cointelegraph", "coverage", D19)},
 {"id": "superhuman-go-personal-assistant", "date": D19, "category": "agent launch", "company": "Superhuman", "impact": "notable",
  "headline": "Superhuman (the Grammarly company) announces a nameable personal AI assistant in Go that flags what needs you and drafts in your voice",
  "explainer": "Go, which Superhuman says has over 1 million monthly users, will get a personal assistant you can name that watches your connected tools, suggests next steps and drafts replies, with you deciding what gets done; an inbox agent for Superhuman Mail and Gmail/Outlook is in beta this month. The assistant itself rolls out over the next few months, so it's a sign-up-for-early-access item for now.",
  "source_url": "https://blog.superhuman.com/superhuman-expands-go-unveils-personal-ai-assistant/", "source_name": "Superhuman",
  "x": xb("https://x.com/shishirmehrotra/status/2123422259029463095", "@shishirmehrotra", "official", D19)},
 {"id": "gemini-api-tool-retrieval", "date": D19, "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Gemini API adds Tool Retrieval, so an agent with hundreds of tools loads only the ones it needs",
  "explainer": "For people building their own bots on Gemini: mark tools as deferred and the model fetches a tool's details only when it needs it, which cuts input tokens and keeps it picking the right tool. There's no extra charge; it's in preview in the Interactions API for Gemini 3.6 and later, including all Gemini 4 models.",
  "source_url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/", "source_name": "Google",
  "x": xb("https://x.com/GoogleAIStudio/status/2123489911684866251", "@GoogleAIStudio", "official", D19)},
 {"id": "deepseek-free-chat-limits", "date": D16, "category": "industry", "company": "DeepSeek", "impact": "notable",
  "headline": "DeepSeek's free app and website start rationing chats, citing a shortage of computing power",
  "explainer": "Users report a daily message quota, prompts capped at about 40,000 Chinese characters, and long chats left idle for more than 7 days that can no longer be continued; the developer API isn't affected. If you lean on DeepSeek's free chat for long projects, keep a copy of important conversations and have a backup app ready.",
  "source_url": "https://technode.com/2026/11/16/deepseek-users-report-chat-limits-as-the-service-cites-capacity-constraints/", "source_name": "TechNode",
  "more_sources": [{"label": "Lianhe Zaobao", "url": "https://www.zaobao.com.sg/en/news/china/deepseek-usage-limits-over-computing-shortages-raise-doubts-about-sustainability-free-service"}],
  "x": xb("https://x.com/thePandaily/status/2122279329036222717", "@thePandaily", "coverage", D16)},
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
