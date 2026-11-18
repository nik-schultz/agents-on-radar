"""Nov 18 PM news run: add 5 items, refresh X numbers for items dated since Nov 11.
Raw response: research/x_news_measure_2026_11_18_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_18_pm.json.txt'
MEASURED = '2026-11-18T20:40:00Z'
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
 {"id": "google-project-genie-4-ultra", "date": D18, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Google opens Genie 4 to AI Ultra subscribers, so you can build a 3D world from a sentence and change it while you walk around",
  "explainer": "Project Genie now runs Google DeepMind's Genie 4 world model with live audio and dialogue, lets you type a new prompt mid-session to change the weather or add a character, and adds a helper agent that builds a world with you through conversation. It's for fun and creative play, and only eligible Google AI Ultra subscribers get it today (AI Pro members can join a waitlist).",
  "source_url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/", "source_name": "Google",
  "x": xb("https://x.com/GoogleDeepMind/status/2123117733709586849", "@GoogleDeepMind", "official", D18)},
 {"id": "gemini-app-android-go", "date": D18, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "The Gemini app now runs on cheaper, lower-memory Android phones, including Android Go models",
  "explainer": "Google rebuilt the app so Gemini Live voice chat (45+ languages), camera help with notes and forms, and Nano Banana image making work on phones with less memory. If you or a family member has a budget Android phone, you can now get Gemini from Google Play or by holding the power button on supported phones.",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-app/gemini-lower-memory-devices/", "source_name": "Google",
  "x": xb("https://x.com/GeminiApp/status/2123100943604707606", "@GeminiApp", "official", D18)},
 {"id": "google-stitch-loop", "date": D18, "category": "agent launch", "company": "Google", "impact": "notable",
  "headline": "Google Labs previews Stitch Loop, an always-on agent that keeps improving an app after it launches",
  "explainer": "Stitch Loop connects to a product's code and live numbers, suggests fixes for security, speed, accessibility or goals like checkout sales, writes the code in a sandbox and opens a pull request that a person must approve before anything changes. It's for small teams that run an app or website, and it's waitlist-only for now, with Google AI Ultra users first.",
  "source_url": "https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/", "source_name": "Google",
  "x": xb("https://x.com/Google/status/2123101724047200432", "@Google", "official", D18)},
 {"id": "grok-4-8-soft-rollout", "date": D17, "category": "model release", "company": "xAI", "impact": "notable",
  "headline": "Elon Musk says Grok 4.8 is in a soft rollout to some Grok Bot users, with a general release a week or two away",
  "explainer": "Musk said on X that xAI has quietly started giving some Grok Bot users Grok 4.8 but still needs another week or two of polish before everyone gets it; there's no xAI release note or price yet. If your Grok Bot seems to answer differently this week, this may be why, but most people won't see it until the general release.",
  "source_url": "https://x.com/elonmusk/status/2122758986483269956", "source_name": "Elon Musk on X",
  "more_sources": [{"label": "TechCity Authority", "url": "https://www.techcityauthority.com/2026/11/grok-4-8-soft-rollout.html"}],
  "x": xb("https://x.com/elonmusk/status/2122758986483269956", "@elonmusk", "official", D17)},
 {"id": "perplexity-orchestrator-api", "date": D17, "category": "feature", "company": "Perplexity", "impact": "minor",
  "headline": "Perplexity launches Orchestrator, one developer API for 45+ AI models with one bill and automatic backup providers",
  "explainer": "Developers can call OpenAI, Anthropic and open-weight models through one Perplexity key, and it switches providers automatically when one is busy or down. It's a builder tool, but it can make bots built on it more reliable and easier to move between models.",
  "source_url": "https://docs.perplexity.ai/docs/orchestrator/quickstart", "source_name": "Perplexity docs",
  "more_sources": [{"label": "Perplexity blog", "url": "https://www.perplexity.ai/hub/blog/introducing-orchestrator"}],
  "x": xb("https://x.com/perplexity_ai/status/2122785177135096053", "@perplexity_ai", "official", D17)},
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
