"""Nov 16 AM news run: add 4 items and refresh X numbers for items dated since Nov 2.
Raw response: research/x_news_measure_2026_11_16_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_16_am.json.txt'
MEASURED = '2026-11-16T12:29:00Z'
txt = open(RAW).read()
raw, _ = json.JSONDecoder().raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
# Musk post measured by search_posts_all in the same run (2026-11-16 ~12:29Z)
pm['2121628295234023654'] = {'like_count': 9351, 'repost_count': 781, 'impression_count': 2331244}

def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}

new = [
 {"id": "openai-science-blog-standard-model", "date": "2026-11-15", "category": "industry", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI starts a science blog with a physicist explaining how GPT-6 Astra helped him attack a 50-year-old physics problem",
  "explainer": "It's a sign of how far the top models have come: a UC Santa Barbara physicist says GPT-6 Astra took the lead on the detailed proof behind a candidate way to define the Standard Model on a grid, with human experts checking it. He calls the result a candidate that still needs expert review, so it's a research milestone, not a new feature in ChatGPT.",
  "source_url": "https://openai.com/index/step-toward-defining-the-standard-model/", "source_name": "OpenAI",
  "x": xb("https://x.com/OpenAI/status/2122123437141553630", "@OpenAI", "official", "2026-11-16")},
 {"id": "gemini-google-wallet-finance", "date": "2026-11-13", "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Gemini can now look at your Google Wallet spending to help with budgets and forgotten subscriptions",
  "explainer": "If you're in the US and turn it on, you can tag @Google Wallet in Gemini and ask things like which subscriptions went up in price or how much you spent on gifts last year, and it can draw charts of your spending. Google says Gemini can only read this data and can't move, manage or invest your money, and you can switch the connection off any time.",
  "source_url": "https://blog.google/innovation-and-ai/products/gemini-app/google-wallet-gemini-app/", "source_name": "Google",
  "more_sources": [{"label": "Android Central", "url": "https://www.androidcentral.com/apps-software/ai/gemini-can-now-tap-into-google-wallet-to-help-manage-your-money"}],
  "x": xb("https://x.com/Google/status/2121293823837921433", "@Google", "official", "2026-11-13")},
 {"id": "claude-duet-us-waitlist-invited", "date": "2026-11-13", "category": "agent launch", "company": "Anthropic", "impact": "notable",
  "headline": "Anthropic invites everyone on the US Claude Duet waitlist, its always-on personal agent",
  "explainer": "If you joined the waitlist on a US Pro, Max or Ultra plan, you should now have an invite to Claude Duet, which checks your email and calendar, sends a morning brief and asks before it sends, pays, signs or deletes anything. Its background checks count against your plan's limits, so Anthropic is adding free limit resets during the preview (three on Pro, one on Max and Ultra) that expire December 15.",
  "source_url": "https://support.claude.com/en/articles/17631495-get-started-with-claude-duet", "source_name": "Claude Help Center",
  "more_sources": [{"label": "Frontier Now", "url": "https://frontiernow.dev/en/news/claude-duet-waitlist/"}],
  "x": xb("https://x.com/ahuja_karan/status/2121332990836163033", "@ahuja_karan", "coverage", "2026-11-13")},
 {"id": "grok-bot-usage-efficiency", "date": "2026-11-13", "category": "pricing", "company": "xAI", "impact": "minor",
  "headline": "Grok Bot plans now stretch about 7% further, and up to 15% on routine runs",
  "explainer": "After complaints that Grok Bot limits were running out too fast, the team says behind-the-scenes fixes give you roughly 7% more work from the same plan and up to about 15% more on scheduled routines. Prices didn't change; it just means recurring bots should use a bit less of your allowance.",
  "source_url": "https://x.com/SamSokolin/status/2121303079803089179", "source_name": "Sam Sokolin (Grok Bot team) on X",
  "more_sources": [{"label": "Tesla North", "url": "https://teslanorth.com/2026/11/14/grok-bot-efficiency-more-usage/"}],
  "x": xb("https://x.com/elonmusk/status/2121628295234023654", "@elonmusk", "official", "2026-11-14")},
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
