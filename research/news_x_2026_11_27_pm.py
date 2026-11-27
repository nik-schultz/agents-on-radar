"""Nov 27 PM news run (Black Friday): add 1 item, refresh X numbers for items dated since Nov 14.
Raw responses: research/x_news_measure_2026_11_27_pm.json.txt (100 posts) + x_news_measure2_2026_11_27_pm.json.txt (4 incl. new), local only."""
import json
MEASURED = '2026-11-27T20:36:00Z'
pm = {}
for RAW in ('research/x_news_measure_2026_11_27_pm.json.txt', 'research/x_news_measure2_2026_11_27_pm.json.txt'):
    txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
    raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
    pm.update({p['id']: p['public_metrics'] for p in raw['data']})
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
new = [
 {"id": "openrouter-drops-providers-prompt-leaks", "date": "2026-11-22", "category": "industry", "company": "OpenRouter", "impact": "notable",
  "headline": "OpenRouter dropped three model hosts and pulled its 'no data kept' label from 125 models after a test caught prompts being read",
  "explainer": "If you use a bot or app that runs its AI model through OpenRouter, some prompts may have been seen by people who shouldn't have them: OpenRouter removed three hosting providers, took the Zero Data Retention label off 125 model options and emailed customers who may be affected, after security firm Dragos planted about two million prompts with fake passwords and links (July to November) and saw some of them used. OpenRouter says it wasn't breached itself; if you got its email or ever pasted a password or key into a prompt, change it, and treat 'no data kept' labels as a promise rather than a guarantee.",
  "source_url": "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/", "source_name": "OpenRouter",
  "more_sources": [{"label": "The Next Web", "url": "https://thenextweb.com/news/openrouter-drops-providers-dragos-ai-prompt-theft-canaries"},
                   {"label": "TechRepublic", "url": "https://www.techrepublic.com/article/news-openrouter-ai-prompt-leaks-zero-data-retention/"},
                   {"label": "BleepingComputer", "url": "https://www.bleepingcomputer.com/news/security/openrouter-drops-ai-providers-over-leaked-prompts-and-secrets/"}],
  "x": xb("https://x.com/OpenRouter/status/2124315081899200715", "@OpenRouter", "official", "2026-11-22")},
]
Dd = json.load(open('data/news.json')); items = Dd['items']
have = {i['id'] for i in items}; links = {i['source_url'] for i in items}
add = [n for n in new if n['id'] not in have and n['source_url'] not in links]
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
