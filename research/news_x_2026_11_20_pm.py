"""Nov 20 PM news run: add 8 items, refresh X numbers for items dated since Nov 12.
Raw response: research/x_news_measure_2026_11_20_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_20_pm.json.txt'
MEASURED = '2026-11-20T20:32:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D20 = "2026-11-20"; D19 = "2026-11-19"
new = [
 {"id": "grok-bot-quickbooks", "date": D20, "category": "feature", "company": "xAI", "impact": "notable",
  "headline": "Grok Bot now works with QuickBooks: ask about cash flow and who owes you, and it drafts invoices and reminders for you to approve",
  "explainer": "If you run a small business on QuickBooks Online in the US, you can connect it to Grok Bot and ask about profit, cash flow or overdue customers, then have it draft invoices, estimates and payment reminders that wait for your OK. It's your real books, so set the QuickBooks tools to Needs approval in Grok Bot's per-tool permissions and check every draft before it goes out.",
  "source_url": "https://x.com/bot/status/2123840024747946383", "source_name": "Grok Bot on X",
  "more_sources": [{"label": "TeslaNorth", "url": "https://teslanorth.com/2026/11/20/grok-bot-quickbooks-invoices-us/"},
                   {"label": "Grok Bot changelog", "url": "https://x.ai/changelog/bot"}],
  "x": xb("https://x.com/bot/status/2123840024747946383", "@bot", "official", D20)},
 {"id": "chatgpt-space-plus", "date": D20, "category": "feature", "company": "OpenAI", "impact": "notable",
  "headline": "ChatGPT Space, for shared pages and slides that can keep themselves up to date, comes to Plus users",
  "explainer": "If you pay for ChatGPT Plus, a new Space tab replaces Library: ask ChatGPT to build a page or slides, like a to-do list or trip plan, set it to update itself from your connected apps, and invite others to edit with you. It's for adults 18+, rolling out gradually; people on the free plan can't open what you share, and there are no public links.",
  "source_url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes", "source_name": "OpenAI Help Center",
  "more_sources": [{"label": "Getting started with Space", "url": "https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt"},
                   {"label": "Engadget", "url": "https://www.engadget.com/2323016/openai-brings-its-collaborative-space-hubs-to-plus-users/"}],
  "x": xb("https://x.com/ChatGPT/status/2123850912867471807", "@ChatGPT", "official", D20)},
 {"id": "signal-blocks-ai-agent-screenshots", "date": D20, "category": "industry", "company": "Signal", "impact": "notable",
  "headline": "Signal now blocks screenshots by default so phone AI assistants like Siri and Gemini can't read your chats",
  "explainer": "If you ask Siri, Gemini or another phone assistant to read or act on your Signal messages, expect it to be blocked: on iPhone (iOS 27) Block Siri AI is on by default, and on Android screen security switches on the first time an assistant tries to read Signal. You can turn it off (iPhone also offers Off for 10 minutes), but Signal warns that lets assistants scan your and your contacts' messages.",
  "source_url": "https://signal.org/blog/protecting-your-privacy/", "source_name": "Signal",
  "more_sources": [{"label": "Signal Support (settings)", "url": "https://support.signal.org/hc/en-us/articles/11338514641306-Screen-security-blocking-Siri-AI"},
                   {"label": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app"}],
  "x": xb("https://x.com/Reuters/status/2123833793567973717", "@Reuters", "coverage", D20)},
 {"id": "google-assistant-speakers-gemini-2027", "date": D20, "category": "industry", "company": "Google", "impact": "notable",
  "headline": "Google Assistant on Nest speakers and displays will be replaced by Gemini for Home on August 2, 2027, and the Nest app shuts on January 25",
  "explainer": "If you talk to a Google or Nest speaker or smart display, it will switch to Gemini for Home by August 2, 2027, which understands normal speech instead of fixed commands; you can switch now in the Google Home app under Home Settings. Separately, the Nest app stops working on January 25, 2027: your devices move to Google Home automatically, but download any saved custom video clips first because they won't transfer.",
  "source_url": "https://9to5google.com/2026/11/20/nest-app-google-assistant/", "source_name": "9to5Google",
  "more_sources": [{"label": "The Verge", "url": "https://www.theverge.com/tech/1038834/google-assistant-smart-speakers-nest-app-killed-shut-down"},
                   {"label": "Android Authority", "url": "https://www.androidauthority.com/assistant-gemini-home-devices-3737857/"}],
  "x": xb("https://x.com/GoogleHome/status/2123839652641796449", "@GoogleHome", "official", D20)},
 {"id": "gemini-gif-maker", "date": D20, "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Gemini can now make short looping GIFs from a prompt, photo or video",
  "explainer": "If you pay for a Google AI plan, ask Gemini for a GIF (a looping photo effect or a meme) and it makes a clip of about three seconds you can copy, paste or download as a .gif. It uses the Omni 1.2 Flash video model and is rolling out in the US, Canada, UK, Japan, Korea, Australia, Germany and France for adults 18+.",
  "source_url": "https://www.androidauthority.com/gemini-gif-generation-rollout-3737901/", "source_name": "Android Authority",
  "more_sources": [{"label": "The Verge", "url": "https://www.theverge.com/tech/1038771/googles-gemini-app-can-now-make-gifs"},
                   {"label": "Gemini Apps Help", "url": "https://support.google.com/gemini/answer/16126339?co=GENIE.Platform%3DDesktop&hl=en"}],
  "x": xb("https://x.com/GeminiApp/status/2123813017855103449", "@GeminiApp", "official", D20)},
 {"id": "thinking-machines-inkling-2-mini", "date": D20, "category": "model release", "company": "Thinking Machines", "impact": "notable",
  "headline": "Thinking Machines releases Inkling 2 Mini, an open-weight model small enough to run on a laptop",
  "explainer": "If you run a bot on your own computer, there's a new free model to try: Inkling 2 Mini has 26.4B parameters (3.4B active), reads text and images, and takes about 20GB of memory and runs on a Mac with at least 32GB of RAM through Ollama. Thinking Machines says it leads open models under 100B parameters on agent-coding tests; it's also on Tinker at $0.15 per million input tokens and $0.50 per million output.",
  "source_url": "https://thinkingmachines.ai/news/inkling-2-mini/", "source_name": "Thinking Machines Lab",
  "more_sources": [{"label": "Hugging Face blog", "url": "https://huggingface.co/blog/inkling2mini"},
                   {"label": "Tinker pricing", "url": "https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/"}],
  "x": xb("https://x.com/thinkymachines/status/2123871643797995872", "@thinkymachines", "official", D20)},
 {"id": "claude-riemann-hypothesis-claim", "date": D20, "category": "industry", "company": "Anthropic", "impact": "notable",
  "headline": "An Anthropic mathematician says he and Claude proved the Riemann hypothesis; it hasn't been checked yet",
  "explainer": "Nothing changes in the Claude app: this is one researcher's claim, posted as a computer-checkable Lean proof on his own website, and outside experts haven't verified it yet. If it holds up it would be a landmark for AI-assisted math, but Anthropic hasn't commented, so treat headlines saying 'Claude solved it' as unconfirmed for now.",
  "source_url": "https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem", "source_name": "The Verge",
  "more_sources": [{"label": "Scientific American", "url": "https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/"},
                   {"label": "Phys.org (AFP)", "url": "https://phys.org/news/2026-11-anthropic-claude-math-greatest-riddle.html"}],
  "x": xb("https://x.com/verge/status/2123818443862573211", "@verge", "coverage", D20)},
 {"id": "chatgpt-health-android-dots", "date": D19, "category": "feature", "company": "OpenAI", "impact": "notable",
  "headline": "ChatGPT Health comes to Android, the desktop app, dots and Sites, with Android Health Connect support",
  "explainer": "If you're in the US, you can now connect Android Health Connect to ChatGPT and ask about patterns in your sleep and workouts, and Pro users' dots can suggest things like moving a workout when a meeting clashes. It's available on Free, Go, Plus and Pro in the US, rolling out gradually; it's health data, so check which apps and records you connect under Health in the sidebar.",
  "source_url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes", "source_name": "OpenAI Help Center",
  "x": xb("https://x.com/ChatGPT/status/2123545961381216325", "@ChatGPT", "official", D19)},
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
