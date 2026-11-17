"""Nov 17 PM news run: add 5 items, refresh X numbers for items dated since Nov 9.
Raw response: research/x_news_measure_2026_11_17_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_17_pm.json.txt'
MEASURED = '2026-11-17T20:32:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D17 = "2026-11-17"
new = [
 {"id": "gpt-6-2-astra-sol", "date": D17, "category": "model release", "company": "OpenAI", "impact": "major",
  "headline": "OpenAI releases GPT-6.2 Astra and GPT-6.2 Sol, smarter models that use fewer words to get work done",
  "explainer": "GPT-6.2 Astra is OpenAI's new top model for hard projects like documents, spreadsheets and code, and GPT-6.2 Sol is the faster everyday model that OpenAI says beats the older GPT-6 Astra on everyday life tasks at about a seventh of the cost. Both are in ChatGPT for Plus, Pro, Enterprise and Edu users and in the API; Astra's API price drops 20% to $8 in / $40 out per million tokens, while Sol keeps $2 / $10, so bots you build on them should get cheaper per job.",
  "source_url": "https://openai.com/index/introducing-gpt-6-2-astra-sol/", "source_name": "OpenAI",
  "more_sources": [{"label": "OpenAI API pricing", "url": "https://developers.openai.com/api/docs/pricing"},
                   {"label": "@OpenAIDevs on X", "url": "https://x.com/OpenAIDevs/status/2122752256923873753"}],
  "x": xb("https://x.com/OpenAI/status/2122750124543926515", "@OpenAI", "official", D17)},
 {"id": "gemini-tasks-free", "date": D17, "category": "agent launch", "company": "Google", "impact": "major",
  "headline": "Google makes Tasks in Gemini (formerly Spark) free, so Gemini can make calls, pay and book things for you",
  "explainer": "Flip the Gemini app's toggle from Chat to Task and it works on a to-do for you, free in the US, Japan, Korea, Canada, Australia and India, running on the new Gemini 4 Hydrogen model. In the US it can also call businesses to compare quotes, buy with Google Pay after you approve, sign in with Google Password Manager, and take jobs you forward to gemini@google.com or text it; it stops and asks before purchases, and calling isn't available in Indiana, Louisiana, Minnesota, Montana or Nebraska.",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/", "source_name": "Google",
  "more_sources": [{"label": "The Verge", "url": "https://www.theverge.com/tech/1035756/google-spark-ai-tasks-free"},
                   {"label": "TechCrunch", "url": "https://techcrunch.com/2026/11/17/google-expands-access-to-gemini-tasks-which-can-help-with-calls-purchases/"},
                   {"label": "9to5Google", "url": "https://9to5google.com/2026/11/17/gemini-tasks-free/"}],
  "x": xb("https://x.com/sundarpichai/status/2122741728247738688", "@sundarpichai", "official", D17)},
 {"id": "cognition-devin-bots", "date": D17, "category": "agent launch", "company": "Cognition", "impact": "notable",
  "headline": "Cognition launches Devin Bots, always-on coding agents that run a team of Devins toward a goal",
  "explainer": "Instead of one coding task at a time, you give a Devin Bot an ongoing goal (say, keep an Android app matching the iPhone app) and it splits the work, runs several Devin sessions and only comes back when it needs your decision, by web, Slack or iMessage. It's aimed at software teams rather than everyday users, no pricing is published yet, and a shared Bot uses its creator's sign-ins and bills to them, so set it up with care.",
  "source_url": "https://devin.ai/blog/introducing-devin-bots", "source_name": "Cognition",
  "more_sources": [{"label": "Fortune", "url": "https://fortune.com/2026/11/17/exclusive-cognition-bets-on-devin-bots-coding-agents-in-challenge-to-anthropics-duet-and-openais-dots/"}],
  "x": xb("https://x.com/cognition/status/2122737511684587551", "@cognition", "official", D17)},
 {"id": "claude-linked-billing", "date": D17, "category": "feature", "company": "Anthropic", "impact": "notable",
  "headline": "Claude's linked billing lets apps charge Claude use to your own Anthropic account without you sharing an API key",
  "explainer": "Apps like Linear, Ramp, Factory and Warp can now bill their Claude usage straight to your Claude Platform organization, with a monthly spend limit per app and an unlink button, so you no longer paste a secret key into each tool. It's in beta and only for organizations that pay Anthropic directly (not a regular Claude subscription), and your own data settings such as zero data retention don't carry over to those requests.",
  "source_url": "https://claude.com/resources/articles/linked-billing-on-claude-platform", "source_name": "Anthropic",
  "more_sources": [{"label": "The Next Web", "url": "https://thenextweb.com/news/anthropic-linked-billing-claude-api-customers-pay"}],
  "x": xb("https://x.com/ClaudeDevs/status/2122751844455956760", "@ClaudeDevs", "official", D17)},
 {"id": "meta-muse-australia", "date": D17, "category": "agent launch", "company": "Meta", "impact": "notable",
  "headline": "Meta's Muse personal agent launches in Australia, with local shopping, property and fitness connectors",
  "explainer": "Australians can now use Muse on iOS, Android, the web and Mac to handle email, calendars and restaurant bookings, with local connectors like Domain, realestate.com.au, Officeworks, MECCA, SWEAT and Ticketek rolling out over time. Muse also adds real-time voice chats and Spaces (custom planners you describe), and it asks before sensitive steps like sending an email or buying something.",
  "source_url": "https://about.fb.com/news/2026/11/muse-is-now-available-in-australia/", "source_name": "Meta",
  "x": xb("https://x.com/alexandr_wang/status/2122762964419870792", "@alexandr_wang", "official", D17)},
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

# AI price table: GPT-6.2 rows (official pricing page, checked Nov 17)
P = json.load(open('data/ai-pricing.json'))
api = P['api']; models = [r['model'] for r in api]
if 'gpt-6.2-astra' not in models:
    i = models.index('gpt-6-astra')
    api.insert(i, {"provider": "OpenAI", "model": "gpt-6.2-astra", "tier": "flagship", "input": 8.0, "output": 40.0, "cached_input": 0.4,
                   "note": "New Nov 17, 2026 (20% below GPT-6 Astra; cached input 60% lower). Short context (≤272K input tokens).",
                   "source_url": "https://platform.openai.com/docs/pricing", "checked_on": D17})
    for r in api:
        if r['model'] == 'gpt-6-astra': r['tier'] = 'flagship'; r['note'] = "Previous flagship; GPT-6.2 Astra is cheaper. Short context (≤272K input tokens)."
        if r['model'] == 'gpt-6.1-sol':
            r.update(model='gpt-6.2-sol', note="New Nov 17, 2026; same prices as GPT-6.1 Sol. Short context (≤272K input tokens).", checked_on=D17)
    P['blueprint_models'] = ['gpt-6.2-astra' if m == 'gpt-6-astra' else m for m in P['blueprint_models']]
    json.dump(P, open('data/ai-pricing.json', 'w'), indent=1, ensure_ascii=False); open('data/ai-pricing.json','a').write('\n')
    print('pricing updated')
