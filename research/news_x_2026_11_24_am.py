"""Nov 24 AM news run: add 5 items (Nov 23 PM - Nov 24 AM), swap the AI Mode Personal Intelligence x block to @Google's post,
refresh X numbers for items dated since Nov 14. Raw response: research/x_news_measure_2026_11_24_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_24_am.json.txt'
MEASURED = '2026-11-24T12:33:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D3, D4 = "2026-11-23", "2026-11-24"
new = [
 {"id": "meta-muse-uk", "date": D4, "category": "agent launch", "company": "Meta", "impact": "notable",
  "headline": "Meta's Muse personal agent launches in the UK, with M&S, ASOS, Currys, easyJet and Jet2 built in",
  "explainer": "If you're 18 or over in the UK, you can now use Muse free on iOS, Android, muse.ai or inside WhatsApp to do jobs like Christmas shopping, finding a cheaper energy deal or turning saved travel Reels into an itinerary; it asks before it sends an email or buys anything, and paid plans add more usage. The UK competition regulator (CMA) says consumer law applies to agents like Muse and that Meta made its terms fairer after talks, so read what you agree to before connecting your email or shops.",
  "source_url": "https://about.fb.com/news/2026/11/introducing-muse-in-the-uk-a-personal-ai-agent-you-control/", "source_name": "Meta",
  "more_sources": [{"label": "The Guardian", "url": "https://www.theguardian.com/technology/2026/nov/24/meta-launches-muse-uk-ai-agent-do-christmas-shopping"},
                   {"label": "CMA statement", "url": "https://competitionandmarkets.blog.gov.uk/2026/11/24/cma-statement-on-uk-launch-of-meta-muse/"},
                   {"label": "BBC News", "url": "https://www.bbc.co.uk/news/articles/c9gkld2l38y6o"}],
  "x": xb("https://x.com/Muse/status/2125111851654815995", "@Muse", "official", D4)},
 {"id": "claude-plugins-one-page", "date": D3, "category": "feature", "company": "Anthropic", "impact": "notable",
  "headline": "Claude puts connectors and skills together as 'Plugins', one page with 10,000+ to browse",
  "explainer": "If you use Claude on Free, Pro, Max or Ultra, the old Customize menu is now called Plugins: one page where you find, add and manage the apps Claude can connect to and the skills it can learn, with filters, categories (including everyday life) and Verified or Community labels. Everything you already installed stays put; if you remove a plugin, check its connector separately because removing it doesn't disconnect the app; Team plans get it from November 30 and Enterprise in the following weeks.",
  "source_url": "https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page", "source_name": "Claude Help Center",
  "more_sources": [{"label": "Artificially Nerdy", "url": "https://artificiallynerdy.com/news/claude-plugins-connectors-skills-free/"}],
  "x": xb("https://x.com/claudeai/status/2124970294523945328", "@claudeai", "official", D3)},
 {"id": "chatgpt-gpt-5-6-retiring-dec-23", "date": D3, "category": "feature", "company": "OpenAI", "impact": "notable",
  "headline": "ChatGPT will retire GPT-5.6 Sol and Terra on December 23",
  "explainer": "If you pick GPT-5.6 by name in ChatGPT, it goes away on December 23: GPT-5.6 Sol leaves the Chat tab, Work and Codex, and GPT-5.6 Terra leaves Work and Codex. If you just chat, nothing to do (the Chat tab is moving to GPT-6.2); if a Work or Codex setup names a GPT-5.6 model, switch it to a newer one before then. OpenAI hasn't announced an API shutdown for these models.",
  "source_url": "https://9to5mac.com/2026/11/23/chatgpt-expands-gpt-6-2-sol-as-openai-sets-retirement-date-for-two-models/", "source_name": "9to5Mac",
  "more_sources": [{"label": "OpenAI API deprecations (no GPT-5.6 entry yet)", "url": "https://developers.openai.com/api/docs/deprecations"}],
  "x": xb("https://x.com/ChatGPT/status/2124981905380569283", "@ChatGPT", "official", D3)},
 {"id": "openai-cisco-shirudo", "date": D3, "category": "industry", "company": "OpenAI", "impact": "minor",
  "headline": "OpenAI and Cisco open-source Shirudo, which lets AI agents put temporary 'shields' on unpatched Linux servers",
  "explainer": "Nothing changes in ChatGPT for you; this is for companies that run Linux servers: Shirudo lets an AI agent write a small, signed safeguard that blocks a known security hole on a running system until the real patch is installed, and a person approves it before it goes live. It's free and open source (BSD licence) but early: production use needs special kernel changes and a TPM security chip.",
  "source_url": "https://openai.com/index/introducing-shirudo/", "source_name": "OpenAI",
  "more_sources": [{"label": "Cisco newsroom", "url": "https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m11/cisco-and-openai-launch-shirudo-a-new-project-to-safeguard-agentic-ai.html"},
                   {"label": "GitHub: shirudo-dev/shirudo", "url": "https://github.com/shirudo-dev/shirudo"}],
  "x": xb("https://x.com/OpenAI/status/2124980590717911527", "@OpenAI", "official", D3)},
 {"id": "gemini-4-neon-workspace-app", "date": D3, "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Gemini 4 Neon reaches work and school accounts in the Gemini app",
  "explainer": "If your Gemini app comes through a Google Workspace work or school account, you can now use the Gemini 4 Neon model there too, not just on personal accounts. It's only in the Gemini app for now (not inside Gmail or Docs), Google didn't say which Workspace editions get it, and your admin still controls whether the Gemini app is on.",
  "source_url": "https://x.com/OfficialLoganK/status/2125018427790344654", "source_name": "Logan Kilpatrick (Google) on X",
  "more_sources": [{"label": "ORIENS", "url": "https://ai-oriens.com/news/gemini-4-neon-workspace/"}],
  "x": xb("https://x.com/OfficialLoganK/status/2125018427790344654", "@OfficialLoganK", "official", D3)},
]
Dd = json.load(open('data/news.json')); items = Dd['items']
have = {i['id'] for i in items}; add = [n for n in new if n['id'] not in have]
for it in items:
    if it['id'] == 'google-ai-mode-wallet-personal-intelligence':
        it['x'] = xb("https://x.com/Google/status/2124981145922146739", "@Google", "official", D3)
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
print('added', len(add), 'refreshed (incl. new)', refreshed)
