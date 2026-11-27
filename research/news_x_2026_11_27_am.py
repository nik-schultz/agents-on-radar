"""Nov 27 AM news run (day after Thanksgiving): add 3 items, refresh X numbers for items dated since Nov 14.
Raw responses: research/x_news_measure_2026_11_27_am.json.txt (100 posts) + x_news_measure2_2026_11_27_am.json.txt (3 new), local only."""
import json
MEASURED = '2026-11-27T12:31:00Z'
pm = {}
for RAW in ('research/x_news_measure_2026_11_27_am.json.txt', 'research/x_news_measure2_2026_11_27_am.json.txt'):
    txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
    raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
    pm.update({p['id']: p['public_metrics'] for p in raw['data']})
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
new = [
 {"id": "grok-bot-usage-11-percent-routines-50", "date": "2026-11-26", "category": "pricing", "company": "xAI", "impact": "notable",
  "headline": "Grok Bot plans now go about 11% further, and scheduled routines up to 50% further, at the same price",
  "explainer": "If you pay for Grok Bot, the same plan now covers about 11% more work, and routines (jobs you set to run on a schedule or when something happens) can use up to 50% less of your allowance, because simple, repetitive steps no longer need a call to the AI model. Prices didn't change and the 50% is the best case, not every routine; Grok Bot's separate hourly run limits still apply, so a routine that runs every hour is now cheaper but not unlimited.",
  "source_url": "https://x.com/SamSokolin/status/2126027973568466949", "source_name": "Sam Sokolin (Grok Bot team) on X",
  "more_sources": [{"label": "Tesla North", "url": "https://teslanorth.com/2026/11/26/grok-bot-update-gives-users-up-to-50-more-routine-runs/"},
                   {"label": "Lapaas Voice", "url": "https://lapaasvoice.com/grok-bot-plans-get-11-more-usage-with-up-to-50-extra-for-automated-routines/"}],
  "x": xb("https://x.com/SamSokolin/status/2126027973568466949", "@SamSokolin", "official", "2026-11-26")},
 {"id": "meta-muse-fca-sandbox-declined", "date": "2026-11-26", "category": "industry", "company": "Meta", "impact": "notable",
  "headline": "Meta turned down the UK financial regulator's offer to test Muse's payments together before the UK launch",
  "explainer": "If you use Muse in the UK to shop or renew things for you, no regulator has tested how it pays on your behalf: the Financial Conduct Authority's head of innovation told WIRED that Meta declined a joint sandbox test the week before Tuesday's launch, and the FCA, the competition watchdog and the data watchdog say they're watching the rollout closely. Meta says it has worked constructively with regulators; until there's more scrutiny, keep Muse's purchase approvals on and check every order before you confirm it.",
  "source_url": "https://www.wired.com/story/meta-refused-to-share-muse-for-testing-uk-financial-watchdog-complains/", "source_name": "WIRED",
  "more_sources": [{"label": "The Next Web", "url": "https://thenextweb.com/news/meta-muse-agent-fca-sandbox-test-wired"},
                   {"label": "Meta (Muse UK launch)", "url": "https://about.fb.com/news/2026/11/introducing-muse-in-the-uk-a-personal-ai-agent-you-control/"}],
  "x": xb("https://x.com/choblin29/status/2125990634762981749", "@choblin29", "coverage", "2026-11-26")},
 {"id": "obsidian-connectors-every-agent", "date": "2026-11-25", "category": "feature", "company": "Obsidian", "impact": "notable",
  "headline": "Obsidian's official connectors now work with Claude, ChatGPT, Dots, Grok Bot, Hermes and more, so several bots can share one set of notes",
  "explainer": "If you keep notes in Obsidian, you can now add Obsidian from the plugin directory of Claude, ChatGPT (including Codex and Dots), Cursor, Grok Bot, Hermes or Kiro, and other agents can install it from Obsidian's help page, so every bot you use can read and write the same vault. The connectors are written skills, not a server: an agent that can run commands on your computer can search and edit the vault while the Obsidian desktop app is open, a chat-only bot can only write notes in Obsidian's format, and any note a bot reads goes to its AI model, so keep private folders out and back up the vault before letting a bot reorganize it.",
  "source_url": "https://obsidian.md/help/connectors", "source_name": "Obsidian Help",
  "more_sources": [{"label": "Obsidian skills on GitHub", "url": "https://github.com/obsidianmd/obsidian-skills"},
                   {"label": "Hermes Marketplace (Obsidian)", "url": "https://hermes-agent.nousresearch.com/marketplace/obsidian"},
                   {"label": "Sulat", "url": "https://news.sulat.com/2026/11/26/obsidian-connectors-agents/"}],
  "x": xb("https://x.com/obsdmd/status/2125700941156651151", "@obsdmd", "official", "2026-11-25")},
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
