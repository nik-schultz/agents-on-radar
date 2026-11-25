"""Nov 25 AM news run: add 6 items (Nov 24, after the PM run), update 2 existing items, refresh X numbers for items dated since Nov 14.
Raw response: research/x_news_measure_2026_11_25_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_25_am.json.txt'
MEASURED = '2026-11-25T12:30:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D4 = "2026-11-24"
new = [
 {"id": "shellbench-agents-fail-everyday-tasks", "date": D4, "category": "industry", "company": "OpenClaw", "impact": "notable",
  "headline": "New ShellBench test: even the best AI agents fail about 4 in 10 everyday jobs, and 1 in 6 runs breaks a safety rule",
  "explainer": "If you hand your bot real chores like matching receipts to a spreadsheet, planning a dinner or paying invoices, check its work before anything is sent or paid: on ShellBench's 100 everyday tasks built from real agent sessions, the top models (GPT-6 Astra 62.5%, Claude Fable 5.2 61.9%, GPT-6.1 Sol 61.4%) still missed a requirement about 4 times in 10, and the best one got the same task right on all three tries only 48.8% of the time. Across all 53,100 runs, 15.7% broke at least one safety rule, such as recommending a duplicate or wrong invoice payment or not withholding a sensitive bank token; the tests didn't use the Muse, Dots or Claude Duet apps themselves, so results there may differ.",
  "source_url": "https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/", "source_name": "TechCrunch",
  "more_sources": [{"label": "OpenClaw blog", "url": "https://openclaw.ai/blog/shellbench"},
                   {"label": "Paper (arXiv)", "url": "https://arxiv.org/abs/2611.32946"}],
  "x": xb("https://x.com/openclaw/status/2125326970976366734", "@openclaw", "official", D4)},
 {"id": "character-ai-chat-sale-ags-object", "date": D4, "category": "industry", "company": "Character.AI", "impact": "notable",
  "headline": "42 state attorneys general ask a court to block Character.AI's auction of users' private chats",
  "explainer": "If you or your kids ever used Character.AI, your chat history, IP address and other account data are part of a bankruptcy auction set for December 1, and the buyer would not have to follow Character.AI's privacy policy or honour deletion requests, so consider deleting your account and chats now. California and a bipartisan group of 42 attorneys general asked the court on Nov 24 to reject the sale or at least leave out children's chats and other sensitive data; it's also a reminder that what you tell any chatbot can outlive the company.",
  "source_url": "https://oag.ca.gov/news/press-releases/attorney-general-bonta-opposes-asset-sale-characterai-amid-child-safety-concerns", "source_name": "California Attorney General",
  "more_sources": [{"label": "Oregon DOJ", "url": "https://www.doj.state.or.us/media-home/news-media-releases/ag-rayfield-asks-court-to-block-sale-of-private-character-ai-chats-including-kids-data/"},
                   {"label": "Connecticut Attorney General", "url": "https://portal.ct.gov/ag/press-releases/2026-press-releases/attorney-general-tong-challenges-plan-to-auction-off-character-ai-private-chats"}]},
 {"id": "openai-gpt-6-protein-design", "date": D4, "category": "industry", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI shows GPT-6 models can design new proteins that bind their targets in lab tests",
  "explainer": "Nothing changes in ChatGPT; it's a research result showing the same general models you chat with can do serious biology: GPT-6.2 designed small proteins using only reasoning and code, and in lab tests with Onava 35 of 322 designs (10.9%) stuck to their intended targets across five proteins, including one some cancers use to hide from the immune system. Specialised biology models still supplied the sequences and picked candidates, and it's a long way from a safe medicine, so don't read it as a new treatment.",
  "source_url": "https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/", "source_name": "OpenAI",
  "x": xb("https://x.com/OpenAI/status/2125334383490105601", "@OpenAI", "official", D4)},
 {"id": "openai-matrix-exponent-nine-fourths", "date": D4, "category": "industry", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI posts a proof claim that multiplying matrices can never get faster than n^2.25, a famous open maths question",
  "explainer": "Nothing changes in ChatGPT and your apps won't get faster; it's another AI-lab maths claim to treat as unconfirmed for now: a 111-page OpenAI preprint says the 'speed limit' for multiplying large grids of numbers (the core sum behind AI itself) is exactly n^2.25, ruling out the long-hoped-for n^2. OpenAI's Lean computer check covers only part of the result (circuits without division), and outside mathematicians haven't reviewed it yet.",
  "source_url": "https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026", "source_name": "OpenAI on GitHub",
  "more_sources": [{"label": "Paper (PDF)", "url": "https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf"},
                   {"label": "Lean formalization scope", "url": "https://github.com/openai/math/blob/main/lean/docs/107.md"}]},
 {"id": "uk-cma-ai-agent-problem-reports", "date": D4, "category": "industry", "company": "UK CMA", "impact": "minor",
  "headline": "The UK competition watchdog asks people to report problems they've had with AI agents",
  "explainer": "If you live in the UK and an AI agent like Muse, ChatGPT dots or Claude Duet bought the wrong thing, misled you or was hard to cancel, you can now tell the CMA through an online form, anonymously if you like, with screenshots or other evidence. The CMA can't sort out individual complaints or give legal advice (go to a consumer advice service for that), but reports feed its oversight of the agents now launching in the UK.",
  "source_url": "https://www.gov.uk/guidance/tell-us-your-views-on-personal-ai-agents", "source_name": "GOV.UK (CMA)",
  "more_sources": [{"label": "CMA statement on Meta Muse", "url": "https://competitionandmarkets.blog.gov.uk/2026/11/24/cma-statement-on-uk-launch-of-meta-muse/"}]},
 {"id": "bytedance-xiaodou-personal-agent-beta", "date": D4, "category": "agent launch", "company": "ByteDance", "impact": "minor",
  "headline": "ByteDance's Doubao team opens an invite-only beta of Xiaodou, a separate personal AI agent app",
  "explainer": "Nothing to try outside China yet: Xiaodou is an invite-only public beta of a standalone personal assistant from the team behind ByteDance's Doubao chatbot, aimed at everyday tasks beyond work, and ByteDance calls it experimental with more abilities to come. It's one more sign that the big chat companies (Meta with Muse, Tencent, OpenAI with dots) are racing to give everyone an always-on personal agent.",
  "source_url": "https://www.caixinglobal.com/2026-11-25/bytedance-expands-personal-ai-agent-push-with-xiaodou-beta-102508431.html", "source_name": "Caixin Global"},
]
Dd = json.load(open('data/news.json')); items = Dd['items']
byid = {i['id']: i for i in items}
# Updates to existing items (verified Nov 24 sources)
g = byid['gemini-history-training-controls']
if 'Update, Nov 24' not in g['explainer']:
    g['explainer'] += " Update, Nov 24: the setting is now widely rolling out; on gemini.google.com open Settings, then 'Gemini History' at the bottom, where 'Chat content including text & attachments' under training is on by default, so switch it off if you don't want your chats used."
    if not any('9to5google.com/2026/11/24' in s['url'] for s in g.get('more_sources', [])):
        g.setdefault('more_sources', []).append({"label": "9to5Google (Nov 24 rollout)", "url": "https://9to5google.com/2026/11/24/gemini-history-ai-training/"})
c = byid['claude-skills-over-mcp-tasks']
if 'Update, Nov 24' not in c['explainer']:
    c['explainer'] = c['explainer'].replace(", and file passing is coming soon.", ".") + " Update, Nov 24: Claude's release notes say sending files to connected apps and saving files from them is now rolling out gradually in beta on Pro, Max and Ultra (Team and Enterprise when an owner turns it on)."
    c.setdefault('more_sources', []).append({"label": "Claude release notes", "url": "https://support.claude.com/en/articles/12138966-release-notes"})
have = set(byid); add = [n for n in new if n['id'] not in have]
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
