"""Nov 2, 2026 AM news run: 6 new items + X re-measure (research/x_news_measure_2026_11_02_am.json.txt)."""
import json
MEASURED = "2026-11-02"
raw = open("research/x_news_measure_2026_11_02_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"chatgpt-codex-shared-usage-december","date":"2026-10-31","category":"pricing","company":"OpenAI","impact":"notable",
  "headline":"ChatGPT and Codex will share one usage allowance from December, and paid accounts per device are now capped",
  "explainer":"On Plus, Pro and Business, your chats and your Codex or agent work will draw from one token-based pool, so long agent jobs can eat into your chat time (Instant chats don't count). Check Settings > Usage to see your balance; OpenAI also now limits how many paid ChatGPT accounts one device or card can hold, so juggling several cheap subscriptions may stop working.",
  "source_url":"https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits","source_name":"OpenAI Help Center",
  "more_sources":[{"label":"OpenAI: card and device limits","url":"https://help.openai.com/en/articles/20001559-understanding-card-and-device-limits-in-chatgpt"},{"label":"The Decoder","url":"https://the-decoder.com/openai-is-steering-chatgpt-users-toward-more-paid-usage/"}],
  "_x":("2116622548985073905","coverage")},
 {"id":"deepseek-dsh-superagent-prototype","date":"2026-10-31","category":"agent launch","company":"DeepSeek","impact":"notable",
  "headline":"DeepSeek open-sources Super-agent, an always-on coding agent that takes requests from team chat",
  "explainer":"It watches one GitHub repo (and optionally a Feishu chat), picks up requests from people you allow, works on them in parallel and comes back with a pull request, pinging you only when needed. It's a free MIT-licensed research prototype, not an official DeepSeek product, so it's for tinkerers who can run it themselves.",
  "source_url":"https://github.com/deepseek-ai/dsh-superagent-prototype","source_name":"GitHub (DeepSeek)",
  "more_sources":[{"label":"TechNode","url":"https://technode.com/2026/11/02/deepseek-team-open-sources-proactive-coding-agent-research-prototype/"},{"label":"Help Net Security","url":"https://www.helpnetsecurity.com/2026/11/02/deepseek-dsh-superagent/"}]},
 {"id":"apple-intelligence-china-qwen","date":"2026-10-31","category":"feature","company":"Apple","impact":"notable",
  "headline":"Apple Intelligence comes to iPhones in China with iOS 27.3, with Alibaba's Qwen built in",
  "explainer":"iPhone owners in China get Writing Tools, Live Translation, Visual Intelligence, Clean Up, Genmoji and summaries, with Qwen answering inside Siri, Writing Tools and Visual Intelligence, much like ChatGPT does elsewhere. Testing starts in the iOS 27.3 beta on Nov 4 with the full release in December; the new Siri isn't included.",
  "source_url":"https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/","source_name":"Apple Newsroom (China)",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/tech/1023974/apple-intelligence-china-ios-27-3"},{"label":"The Next Web","url":"https://thenextweb.com/news/apple-intelligence-china-ios-27-3-alibaba-qwen"}]},
 {"id":"grok-api-text-watermark","date":"2026-10-31","category":"feature","company":"xAI","impact":"minor",
  "headline":"Text from Grok's API will carry an invisible watermark by default from Nov 7",
  "explainer":"Apps and bots built on Grok 4.x through the API will produce text that xAI can later recognize as AI-written, which it says is for the EU AI Act; nothing changes in how the text looks. Team admins can opt out per model, and the Grok app itself isn't covered by this change.",
  "source_url":"https://docs.x.ai/developers/advanced-api-usage/watermarking","source_name":"xAI docs"},
 {"id":"claude-ultra-plan-no-5-hour-limit","date":"2026-10-30","category":"pricing","company":"Anthropic","impact":"notable",
  "headline":"Claude renames Max 20x to Ultra and drops the five-hour limit for verified Ultra accounts",
  "explainer":"At the same $200 a month, verified Ultra subscribers can now use their whole week's allowance whenever they like instead of hitting a reset every five hours; the weekly limit itself didn't change. The $100 Max 5x plan is now just called Max, and you don't need to do anything if you subscribe.",
  "source_url":"https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan","source_name":"Claude Help Center",
  "more_sources":[{"label":"The Next Web","url":"https://thenextweb.com/news/claude-ultra-max-plan-rename-five-hour-limit"},{"label":"Claude pricing","url":"https://claude.com/pricing"}],
  "_x":("2116220869479428500","official")},
 {"id":"chatgpt-mobile-account-switching","date":"2026-10-30","category":"feature","company":"OpenAI","impact":"minor",
  "headline":"ChatGPT's phone apps let you stay signed in to two accounts and switch between them",
  "explainer":"Handy if you have a personal and a work ChatGPT: switch in a tap instead of logging out. Each account keeps its own chats, memory, files and subscription, and it's rolling out gradually on iOS and Android.",
  "source_url":"https://help.openai.com/en/articles/6825453-chatgpt-release-notes","source_name":"ChatGPT release notes",
  "_x":("2116405414921384099","official")},
]
p = "data/news.json"; data = json.load(open(p))
have = {x["id"] for x in data["items"]}
def mets(q):
    m = q["public_metrics"]
    return m["like_count"], m.get("repost_count", m.get("retweet_count")), m.get("impression_count")
def xblock(pid, kind):
    q = posts[pid]; l, r, v = mets(q)
    return {"url": q["url"], "author": "@" + users[q["author_id"]], "kind": kind, "likes": l,
            "reposts": r, "views": v, "posted_at": q["created_at"].replace(".000Z","Z"), "measured_at": MEASURED}
n = 0
for x in data["items"]:
    if x.get("x"):
        pid = x["x"]["url"].rsplit("/",1)[1]
        if pid in posts:
            l, r, v = mets(posts[pid])
            x["x"].update(likes=l, reposts=r, views=v, measured_at=MEASURED); n += 1
added = []
for it in reversed(NEW):
    if it["id"] in have: continue
    xs = it.pop("_x", None)
    if xs: it["x"] = xblock(*xs)
    data["items"].insert(0, it); added.append(it["id"])
for x in data["items"]:
    if x["id"] == "openai-robots-txt-ai-training-signal":
        x["headline"] = "OpenAI, Google, Microsoft and Anthropic back one shared robots.txt switch to keep a website out of AI training"
        x["explainer"] = "If you run a blog or small business site, you'll soon be able to say 'don't train AI on this' once, for every participating AI company, instead of blocking each crawler separately. Anthropic already honors it, OpenAI says support comes in the next few months, and Google and Microsoft (from Feb 1, 2027) follow next year; it's based on an IETF draft that isn't final yet."
        ms = x.setdefault("more_sources", [])
        for lab, u in [("The Verge","https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out"),("Search Engine Land (Microsoft)","https://searchengineland.com/microsoft-bing-gives-publishers-more-control-over-how-ai-uses-their-content-499967")]:
            if u not in [m["url"] for m in ms]: ms.append({"label":lab,"url":u})
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=2, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", len(added))
