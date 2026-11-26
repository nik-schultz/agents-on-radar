"""Nov 26 PM news run (Thanksgiving): add 2 items, refresh X numbers for items dated since Nov 14.
Raw response: research/x_news_measure_2026_11_26_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_26_pm.json.txt'
MEASURED = '2026-11-26T20:30:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
new = [
 {"id": "openclaw-2026-11-10-deep-research-knowledge", "date": "2026-11-25", "category": "feature", "company": "OpenClaw", "impact": "notable",
  "headline": "OpenClaw 2026.11.10 adds Deep Research in chat, a Knowledge notebook of your people and decisions, and a way to take over its browser for sign-ins",
  "explainer": "If you run OpenClaw as your personal agent, this update lets you ask it in chat for a deep-research report with citations, side-by-side quotes where sources disagree and a list of what's still unresolved, and lets you take over its browser tab yourself for a sign-in, 2FA code or CAPTCHA, then hand it back. Deep Research is on by default and uses your existing model and web tools, saved reports stay for seven days, and the new Knowledge memory (one setting to turn on) keeps a local Markdown notebook of people, projects and decisions from your chats, notes and Granola meetings.",
  "source_url": "https://docs.openclaw.ai/releases/2026.11.10", "source_name": "OpenClaw release notes",
  "more_sources": [{"label": "GitHub release", "url": "https://github.com/openclaw/openclaw/releases/tag/v2026.11.10"},
                   {"label": "Deep Research guide", "url": "https://docs.openclaw.ai/tools/deep-research"},
                   {"label": "Knowledge guide", "url": "https://docs.openclaw.ai/plugins/knowledge"}],
  "x": xb("https://x.com/openclaw/status/2125591827600531554", "@openclaw", "official", "2026-11-25")},
 {"id": "apple-pulls-minimax-talkie", "date": "2026-11-25", "category": "industry", "company": "MiniMax", "impact": "notable",
  "headline": "Apple pulls MiniMax's Talkie AI companion app from the App Store worldwide after a report on sexual messages to children",
  "explainer": "If your kids use AI companion or role-play apps, this is a reason to check which ones are on their devices: Apple removed MiniMax's Talkie from the App Store on Wednesday, citing sexual content, after a Bureau of Investigative Journalism and ABC investigation found its AI characters sending sexual and abusive messages to children. Talkie is still available on the web and Google Play, and its users can create and share their own characters, so an age rating or a store listing alone isn't a safeguard.",
  "source_url": "https://appleinsider.com/articles/26/11/26/ai-chatbot-companion-app-talkie-pulled-from-apple-app-store-after-investigation", "source_name": "AppleInsider",
  "more_sources": [{"label": "South China Morning Post", "url": "https://www.scmp.com/tech/tech-trends/article/3375791/minimax-chatbot-talkie-removed-apple-app-store-over-alleged-sexual-content"},
                   {"label": "The Bureau of Investigative Journalism (investigation)", "url": "https://www.thebureauinvestigates.com/stories/2026-11-24/talkie-china-chatbot-children"}],
  "x": xb("https://x.com/appleinsider/status/2125832007322075363", "@appleinsider", "coverage", "2026-11-26")},
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
