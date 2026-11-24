"""Nov 24 PM news run: add 9 items (Nov 23 - Nov 24 PM), refresh X numbers for items dated since Nov 14.
Raw response: research/x_news_measure_2026_11_24_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_24_pm.json.txt'
MEASURED = '2026-11-24T20:31:00Z'
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
 {"id": "claude-install-artifacts-as-apps", "date": D4, "category": "feature", "company": "Anthropic", "impact": "notable",
  "headline": "Claude can turn an artifact it builds for you into a real Mac or Windows app",
  "explainer": "If you use Claude for Mac or Windows, you can ask it to build a small tool (say, a tracker or a meeting-prep page), click \"Install as app\" in the Share menu, and it opens in its own window with its own icon, can use your connectors and, if you allow it, send notifications or sit in your menu bar. It's a beta on all plans and uses your normal Claude usage; Claude asks for permission again after every update, only apps you (or your company) made can get full computer access, and Anthropic doesn't review apps, so only install ones you trust.",
  "source_url": "https://claude.com/resources/articles/install-as-app", "source_name": "Claude",
  "more_sources": [{"label": "Claude release notes", "url": "https://support.claude.com/en/articles/12138966-release-notes"},
                   {"label": "9to5Mac", "url": "https://9to5mac.com/2026/11/24/anthropic-just-gave-claude-users-a-new-way-to-make-mac-apps/"}],
  "x": xb("https://x.com/ClaudeDevs/status/2125315491522650299", "@ClaudeDevs", "official", D4)},
 {"id": "meta-muse-instagram-dms", "date": D4, "category": "feature", "company": "Meta", "impact": "notable",
  "headline": "Meta's Muse agent arrives in Instagram DMs and can turn your saved posts into plans",
  "explainer": "If you use Instagram in the US, Canada, Mexico, Japan or Singapore, you can now DM Muse to ask about a post, place or product, catch up on chats you missed, or have it turn saved reels into a trip itinerary, a grocery list from a recipe video, or tidy collections. Meta says nothing is shared, posted or sent without your OK and you can ask Muse to forget or undo things; the save-to-Muse prompt is US and Canada only for now.",
  "source_url": "https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/", "source_name": "TechCrunch",
  "more_sources": [{"label": "The Verge", "url": "https://www.theverge.com/tech/1041374/you-can-now-dm-your-muse-ai-agent-on-instagram"},
                   {"label": "Adam Mosseri on Threads", "url": "https://www.threads.com/@mosseri/post/DgIelvvmi00/we-recently-rolled-out-a-new-muse-feature-thats-pretty-useful-for-instagram/"},
                   {"label": "@instagram on X", "url": "https://x.com/instagram/status/2125295853816692960"}],
  "x": xb("https://x.com/Muse/status/2125284171417637002", "@Muse", "official", D4)},
 {"id": "claude-skills-over-mcp-tasks", "date": D4, "category": "feature", "company": "Anthropic", "impact": "notable",
  "headline": "Claude's connected apps can now bring their own skills, run long jobs, and stop to ask you first",
  "explainer": "If you connect apps to Claude on Pro, Max or Ultra, those apps can now ship built-in know-how (\"skills\") that Claude loads only when needed, hand off long jobs that finish in the background, and pause mid-task to ask you for a sign-off through a form, for example before spending money or deleting something. Skills over MCP is a beta that's on by default for Pro, Max and Ultra (Team needs an admin); Tasks and the ask-first step are generally available, and file passing is coming soon.",
  "source_url": "https://claude.com/resources/articles/skills-over-mcp-tasks-and-more", "source_name": "Claude",
  "x": xb("https://x.com/ClaudeDevs/status/2125289794871963935", "@ClaudeDevs", "official", D4)},
 {"id": "claude-monthly-recap-out-of-beta", "date": D4, "category": "feature", "company": "Anthropic", "impact": "minor",
  "headline": "Claude's monthly recap is out of beta, and you can now delete stored recaps",
  "explainer": "If you use Claude on Free, Pro, Max or Ultra with memory on, the monthly recap (Settings, Reflect) is now a regular feature on web, desktop and mobile, can include your cloud Claude Code sessions and Cowork tasks, and you can delete stored recaps from that page. It isn't available on Team or Enterprise plans.",
  "source_url": "https://support.claude.com/en/articles/12138966-release-notes", "source_name": "Claude Help Center",
  "more_sources": [{"label": "See your monthly recap (Claude Help Center)", "url": "https://support.claude.com/en/articles/15672559-see-your-monthly-recap"}]},
 {"id": "openai-healthcare-responses-api", "date": D4, "category": "feature", "company": "OpenAI", "impact": "minor",
  "headline": "OpenAI's API gets healthcare versions of its GPT-6.2 models that search only medical sources",
  "explainer": "Nothing changes in ChatGPT; this is for apps built on OpenAI's API: developers can now pick healthcare configurations of GPT-6.2 Astra, GPT-6.2 Sol and two older models that pair the model with a setup tuned for clinical questions, and when it searches the web it uses a dedicated index of medical sources. A health app you use may get more careful answers, but it's still not a doctor.",
  "source_url": "https://developers.openai.com/api/docs/changelog", "source_name": "OpenAI API changelog"},
 {"id": "deepmind-humanitys-first-exam", "date": D4, "category": "industry", "company": "Google", "impact": "minor",
  "headline": "Google DeepMind's new test checks whether AI gets simple everyday questions right every time",
  "explainer": "It's a reminder that today's best chatbots still slip on easy things: on Humanity's First Exam, 544 simple text and picture questions, top models score 96-98% on a first try but only about 86% when asked the same thing four slightly different ways, and most mistakes come from reading images, like counting objects. So double-check counts, colours and details from photos; the leaderboard is led by GPT-6.2 Astra (90.7%), and anyone can submit questions AI gets wrong on Kaggle until December 15.",
  "source_url": "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/", "source_name": "Google",
  "more_sources": [{"label": "Kaggle leaderboard", "url": "https://www.kaggle.com/benchmarks/deepmind/hfe/leaderboard"}],
  "x": xb("https://x.com/kaggle/status/2125313430303244739", "@kaggle", "official", D4)},
 {"id": "claude-vp-vnp-proof-claim", "date": D3, "category": "industry", "company": "Anthropic", "impact": "notable",
  "headline": "Anthropic posts a Claude-written proof that VP is not equal to VNP, a decades-old maths question; no human has checked it",
  "explainer": "Nothing changes in the Claude app; it's another sign that AI models are starting to produce serious maths, with a big caveat: Anthropic says an internal research Claude model found and wrote up a proof that two classes of algebraic circuits differ (an algebraic cousin of P vs NP, which it does not settle), and the Lean proof passes two independent proof checkers. Anthropic itself says no human mathematician has checked the proof and no machine checks that the Lean statement says what's claimed, so treat headlines about it as unconfirmed.",
  "source_url": "https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md", "source_name": "Anthropic on GitHub",
  "more_sources": [{"label": "Paper (PDF)", "url": "https://raw.githubusercontent.com/anthropics/formal-math/main/vp-vnp/paper.pdf"},
                   {"label": "GitHub pull request #51", "url": "https://github.com/anthropics/formal-math/pull/51"}]},
 {"id": "canva-mcp-open-to-every-agent", "date": D3, "category": "agent launch", "company": "Canva", "impact": "minor",
  "headline": "Canva opens its design tools to any AI agent, so chat apps can hand back editable designs and videos",
  "explainer": "If you ask ChatGPT, Claude, Gemini or Muse for something like an Instagram post or a short product video, the Canva connector can now return a real, editable Canva design (with your brand kit) instead of a flat image, and you fix details by hand beside the chat. The bigger change is for developers: Canva MCP is out of waitlist for any agent, with new APIs and access to Canva's own Craft image model.",
  "source_url": "https://www.canva.com/newsroom/news/canva-mcp-update/", "source_name": "Canva",
  "more_sources": [{"label": "The Next Web", "url": "https://thenextweb.com/news/canva-mcp-ai-agents-developers"},
                   {"label": "Canva Developers blog", "url": "https://www.canva.dev/blog/developers/canva-mcp-ga/"}],
  "x": xb("https://x.com/canva/status/2124926205313081394", "@canva", "official", D3)},
 {"id": "google-antigravity-carbon-ai-pro", "date": D3, "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Google's Antigravity coding agent gives AI Pro subscribers Gemini 4 Carbon and resets everyone's quotas",
  "explainer": "If you pay for Google AI Pro ($19.99 a month) and build things with the Antigravity agent, you now get Google's top Gemini 4 Carbon model there, which used to need the $99.99 Ultra plan, and Google reset Gemini quotas for all Antigravity users. Google also says the fast Gemini 4 Hydrogen model is coming to all Antigravity users, and Gemini 4 Argon and 3.8 Flash leave Antigravity on November 30.",
  "source_url": "https://9to5google.com/2026/11/23/antigravity-gemini-4-carbon/", "source_name": "9to5Google",
  "x": xb("https://x.com/_mohansolo/status/2124960419429458207", "@_mohansolo", "official", D3)},
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
