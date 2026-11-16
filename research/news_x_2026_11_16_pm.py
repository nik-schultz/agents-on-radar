"""Nov 16 PM news run: add 3 items and refresh X numbers for items dated since Nov 9.
Raw response: research/x_news_measure_2026_11_16_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_16_pm.json.txt'
MEASURED = '2026-11-16T20:31:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder().raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm), 'errors', raw.get('errors'))

def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}

new = [
 {"id": "alibaba-qwen4-max-release", "date": "2026-11-16", "category": "model release", "company": "Alibaba", "impact": "notable",
  "headline": "Alibaba fully releases Qwen4-Max, its top model, at about a quarter of the price of the big US flagships",
  "explainer": "The preview from last week is now a regular paid model: $1.50 per million tokens in and $4.50 per million out on QwenCloud, 25% cheaper than Qwen3.8-Max, with a 1-million-token memory, image and video reading and tool use. It's mostly for people building their own bots who want a cheaper engine for coding and office tasks; Alibaba's claim of ~60% lower cost per task comes from its own test, so your savings may differ.",
  "source_url": "https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max", "source_name": "Alibaba Cloud",
  "more_sources": [{"label": "QwenCloud pricing", "url": "https://www.qwencloud.com/models/qwen4-max"},
                   {"label": "eWeek", "url": "https://www.eweek.com/news/alibaba-qwen4-max-features-pricing/"}],
  "x": xb("https://x.com/Alibaba_Qwen/status/2122148127520289151", "@Alibaba_Qwen", "official", "2026-11-16")},
 {"id": "openai-computer-use-healthcare", "date": "2026-11-16", "category": "agent launch", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI puts computer-use agents to work in healthcare offices, filling in insurance and referral forms",
  "explainer": "Agents that click and type through existing software are now available in ChatGPT for Healthcare, ChatGPT for Clinicians (free for US clinicians) and the API, and CVS Health, Cigna, Abridge and Ambience are using them for prior authorizations, referrals and discharge planning. For patients it could mean less waiting on paperwork; OpenAI says organizations can require human approval before the agent submits anything and keep an audit log.",
  "source_url": "https://openai.com/index/advancing-computer-use-for-healthcare-teams/", "source_name": "OpenAI",
  "x": xb("https://x.com/OpenAI/status/2122419941756531150", "@OpenAI", "official", "2026-11-16")},
 {"id": "google-ask-maps-appointments-calls", "date": "2026-11-16", "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Google Maps' Ask Maps can now find open appointments and call local businesses for you",
  "explainer": "In the US you can ask something like \"find me a 4 p.m. nail appointment near me\" and Ask Maps checks open slots online or calls the shop, then shows you the times so you pick one; it covers beauty, pet care, auto and home repair. The same update adds day-by-day road-trip itineraries and search across your saved places, and brings Ask Maps to 30+ more countries in Europe.",
  "source_url": "https://blog.google/products-and-platforms/products/maps/ask-maps-holiday-travel-features-2026/", "source_name": "Google",
  "more_sources": [{"label": "Engadget", "url": "https://www.engadget.com/2318186/google-maps-chatbot-can-find-appointments-and-call-to-book-them-for-you/"}],
  "x": xb("https://x.com/googlemaps/status/2122396544729305165", "@googlemaps", "official", "2026-11-16")},
]
D = json.load(open('data/news.json'))
items = D['items']
have = {i['id'] for i in items}
refreshed = 0
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
