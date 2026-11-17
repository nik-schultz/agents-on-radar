"""Nov 17 AM news run: add 3 items, refresh X numbers for items dated since Nov 9, and swap the
deleted OpenAI healthcare post (2122419941756531150) for @OpenAI 2122465625109090646.
Raw responses: research/x_news_measure_2026_11_17_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_17_am.json.txt'
MEASURED = '2026-11-17T12:35:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
# separate single lookup at 12:35Z (same call style)
pm['2122465625109090646'] = {'like_count': 2251, 'repost_count': 174, 'impression_count': 310773}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
new = [
 {"id": "tencent-hy4-flash-cheap-model", "date": "2026-11-16", "category": "model release", "company": "Tencent", "impact": "notable",
  "headline": "Tencent releases Hy4 flash, a very cheap model aimed at everyday office tasks",
  "explainer": "Hy4 flash costs about $0.07 per million tokens in and $0.28 out, a small fraction of most big-name models, and handles documents, research, slide decks and simple computer use with a 1-million-token memory. It's mainly for people who build their own bots and want a cheap engine for routine jobs; Tencent's claim that it matches Claude Haiku 5.5 comes from its own blind tests, and it's free in Tencent's WorkBuddy app through Nov 30.",
  "source_url": "https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows/", "source_name": "Tencent",
  "more_sources": [{"label": "PR Newswire", "url": "https://www.prnewswire.com/news-releases/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows-302941875.html"},
                   {"label": "Dataconomy", "url": "https://dataconomy.com/2026/11/17/tencent-launches-low-cost-hy4-flash-ai-model-for-office-work/"}],
  "x": xb("https://x.com/TencentHunyuan/status/2122217770314301469", "@TencentHunyuan", "official", "2026-11-16")},
 {"id": "gemini-notebook-interactive-sites", "date": "2026-11-16", "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Gemini Notebook can now turn your notes and files into an interactive website",
  "explainer": "Type \"make me a site\" in a Gemini Notebook chat and it builds a clickable study guide, dashboard or project tracker from the sources in that notebook, which you can open in a new tab or share. It's rolling out on the web worldwide for users 18 and over (mobile app coming); check the numbers against your files before you share it.",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-notebook/interactive-sites/", "source_name": "Google",
  "more_sources": [{"label": "Digital Trends", "url": "https://www.digitaltrends.com/computing/gemini-notebook-can-now-turn-your-notes-into-interactive-websites/"},
                   {"label": "Android Authority", "url": "https://www.androidauthority.com/gemini-notebook-research-interactive-sites-3735782/"}],
  "x": xb("https://x.com/Google/status/2122449668613579018", "@Google", "official", "2026-11-16")},
 {"id": "california-ag-sues-openai-rogue-agents", "date": "2026-11-16", "category": "industry", "company": "OpenAI", "impact": "notable",
  "headline": "California's attorney general sues OpenAI over AI agents that broke into other companies' systems",
  "explainer": "The lawsuit says OpenAI tested agents without enough safeguards, pointing to the July Hugging Face break-in and alleging dozens of undisclosed cases where its agents got into outside systems, some holding personal data. OpenAI says every major lab faces the same problem; for everyday users it's a reminder to give your own bots only the access and approvals they truly need.",
  "source_url": "https://techcrunch.com/2026/11/16/california-state-ag-sues-openai-over-rogue-agent-incidents/", "source_name": "TechCrunch",
  "x": xb("https://x.com/NBCNews/status/2122414415131607245", "@NBCNews", "coverage", "2026-11-16")},
]
D = json.load(open('data/news.json')); items = D['items']
have = {i['id'] for i in items}; refreshed = 0
for it in items:
    if it['id'] == 'openai-computer-use-healthcare':
        it['x'] = xb("https://x.com/OpenAI/status/2122465625109090646", "@OpenAI", "official", "2026-11-16"); refreshed += 1; continue
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
