"""Nov 26 AM news run (Thanksgiving): add 2 items, refresh X numbers for items dated since Nov 14.
Raw response: research/x_news_measure_2026_11_26_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_26_am.json.txt'
MEASURED = '2026-11-26T12:29:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
new = [
 {"id": "chatgpt-gpt-6-2-billing-fix-banked-reset", "date": "2026-11-26", "category": "pricing", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI fixes a GPT-6.2 billing mistake, so paid ChatGPT and Codex users hit limits up to 40% sooner; everyone gets one banked reset",
  "explainer": "If you pay for ChatGPT (Go, Plus, Pro or Business) and use GPT-6.2 Astra or Sol, the same work now uses more of your allowance: OpenAI says you'll reach your limits 40% faster on Astra and 25% faster on Sol than last week, because a launch bug had been undercounting them; other models aren't affected and past usage won't be charged. As an apology every Go, Plus, Pro and Business account gets one banked reset, which you redeem in Usage settings on the web or desktop app (not mobile) once an allowance is below 80%, so save it for a day you're about to run out.",
  "source_url": "https://www.techradar.com/ai-platforms-assistants/chatgpt/weve-fixed-this-now-so-the-same-work-will-use-more-of-your-plans-usage-allowance-openai-admits-it-made-a-mistake-when-launching-gpt-6-2-and-now-paying-chatgpt-users-could-hit-their-usage-limits-up-to-40-percent-faster", "source_name": "TechRadar",
  "more_sources": [{"label": "Notebookcheck", "url": "https://www.notebookcheck.net/ChatGPT-users-hit-limits-up-to-40-sooner-after-OpenAI-billing-fix.1460643.0.html"},
                   {"label": "OpenAI Help Center (banked resets)", "url": "https://help.openai.com/en/articles/20001498-how-resets-work-in-codex"}],
  "x": xb("https://x.com/thsottiaux/status/2125784147889393806", "@thsottiaux", "official", "2026-11-26")},
 {"id": "gemini-for-home-nov-25-update", "date": "2026-11-25", "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Gemini for Home update: faster smart-home commands, follow-ups like 'turn them back on', steerable bedtime stories and sources on displays",
  "explainer": "If you're in the Gemini for Home early access on a Google or Nest speaker or display, everyday commands like lights should respond faster, follow-ups such as 'turn them back on' now remember which lights you meant, and 'Hey Google, tell me a story' is back with stories you can change as they go. Google is also rolling out its improved Gemini Live ('Hey Google, let's chat') over the coming weeks, smart displays get a Sources button for web answers, and the Home app adds a remote 30-second siren on some outdoor cameras.",
  "source_url": "https://support.google.com/googlehome/answer/15962877?hl=en", "source_name": "Google Home release notes",
  "more_sources": [{"label": "9to5Google", "url": "https://9to5google.com/2026/11/25/google-home-update-nest-cam-thermostat-gemini-features/"}],
  "x": xb("https://x.com/9to5Google/status/2125708656805040147", "@9to5Google", "coverage", "2026-11-25")},
]
Dd = json.load(open('data/news.json')); items = Dd['items']
have = {i['id'] for i in items}; add = [n for n in new if n['id'] not in have]
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
