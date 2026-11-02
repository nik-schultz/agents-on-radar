"""Nov 2, 2026 PM news run: 6 new items + X re-measure (research/x_news_measure_2026_11_02_pm.json.txt)."""
import json
MEASURED = "2026-11-02"
raw = open("research/x_news_measure_2026_11_02_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"claude-api-message-threads","date":"2026-11-02","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude's API can now remember the conversation for you, making long agent sessions about a third faster to answer",
  "explainer":"If you use Claude-powered agents or coding tools, long sessions should start replying faster: with the new message threads beta the server keeps the conversation, so the app only sends new messages, and Anthropic says the median wait for the first word drops about 35% on very long (500k to 1M token) chats. Price and token use stay the same, and a thread expires five minutes after its last request.",
  "source_url":"https://platform.claude.com/docs/en/release-notes/overview","source_name":"Claude Platform release notes",
  "more_sources":[{"label":"Claude: message threads","url":"https://claude.com/resources/articles/message-threads"},{"label":"The Next Web","url":"https://thenextweb.com/news/anthropic-message-threads-beta-claude-api-agents"}],
  "_x":("2117332449382510884","official")},
 {"id":"openai-lifeval","date":"2026-11-02","category":"industry","company":"OpenAI","impact":"notable",
  "headline":"OpenAI releases LifeVal, a test of how well AI handles everyday life chores like childcare, groceries and government forms",
  "explainer":"It's a sign of where ChatGPT is headed: OpenAI built the test from time-use surveys and a survey of 3,995 people about the tasks they most want help with, such as budgeting, ordering groceries or finding a home, and frames it as a step toward ChatGPT acting as a personal assistant. Its own showcase tasks score 90 to 100%, but it's OpenAI grading its own homework, so treat it as a direction, not proof.",
  "source_url":"https://openai.com/index/lifeval/","source_name":"OpenAI",
  "_x":("2117307611338997846","official")},
 {"id":"meituan-longcat-2-5","date":"2026-11-02","category":"model release","company":"Meituan","impact":"notable",
  "headline":"Meituan releases LongCat-2.5, a giant agent model that plugs into Claude Code and Codex",
  "explainer":"Food-delivery giant Meituan's new model (1.6 trillion parameters, about 48 billion active at a time) sees images, reads up to 1 million tokens and is built for long coding and agent jobs; it works inside the Claude Code, Codex and Hermes tools. It's API-only for now through the LongCat platform and was trained on Chinese-made chips, so it's mainly for developers shopping for cheaper agent models.",
  "source_url":"https://longcat.chat/platform/docs/ChangeLog.html","source_name":"LongCat API changelog",
  "more_sources":[{"label":"Meituan news","url":"https://www.meituan.com/news/NN261102280001343"},{"label":"Crypto Briefing","url":"https://cryptobriefing.com/meituan-releases-longcat-2-5-multimodal-model/"}],
  "_x":("2117264311714537633","official")},
 {"id":"semianalysis-gdpx-benchmark","date":"2026-11-02","category":"industry","company":"SemiAnalysis","impact":"notable",
  "headline":"New GDPx test finds even the best AI agent finishes only 12% of real expert work tasks",
  "explainer":"A useful reality check before handing an agent serious professional work: across 206 long tasks in 11 fields, Claude Opus 5.5 scored 12.0%, Gemini 4 Carbon 10.9% and GPT-6 Astra 9.6%, and every model scored zero on the finance and legal tasks under pass/fail grading. SemiAnalysis says it will refresh the leaderboard every three to six months.",
  "source_url":"https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities","source_name":"SemiAnalysis",
  "more_sources":[{"label":"GDPx leaderboard","url":"https://gdpx.semianalysis.com/"},{"label":"9to5Google","url":"https://9to5google.com/2026/11/02/gemini-4-carbon-benchmark/"}],
  "_x":("2117075900575477855","official")},
 {"id":"chatgpt-chat-work-merge-classic-retiring","date":"2026-11-02","category":"feature","company":"OpenAI","impact":"minor",
  "headline":"ChatGPT will merge its Chat and Work tabs into one, and the old ChatGPT Classic desktop app retires Jan 30, 2027",
  "explainer":"Soon you won't have to pick between Chat and Work: a small test group gets one screen where you can talk, bring in files and plugins, and have ChatGPT build a site, make slides or act on the web, while Codex stays separate. If you still use the ChatGPT Classic Mac app, move to the new ChatGPT desktop app before Jan 30, 2027; your chat history comes with you.",
  "source_url":"https://techcrunch.com/2026/11/02/openai-is-finally-merging-chatgpts-chat-and-work-tabs/","source_name":"TechCrunch",
  "more_sources":[{"label":"9to5Mac","url":"https://9to5mac.com/2026/11/02/openai-is-retiring-chatgpt-classic-app-will-soon-combine-chat-and-work-tabs-in-new-app/"},{"label":"OpenAI Help Center: new desktop app","url":"https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app"}],
  "_x":("2117347857351037023","coverage")},
 {"id":"claude-watermark-older-models","date":"2026-11-02","category":"feature","company":"Anthropic","impact":"minor",
  "headline":"Claude adds an invisible text watermark to more models, including Opus 4.7 and Sonnet 4.6, from Nov 3",
  "explainer":"Text from Claude Mythos 5, Opus 4.7, Opus 4.6 and Sonnet 4.6 will carry a hidden mark that lets Anthropic later recognize it as AI-written, which it says is for the EU AI Act; it doesn't change how replies look and contains no personal info. Amazon Bedrock follows a few days later, and the detection tool is only in private preview.",
  "source_url":"https://sea.mashable.com/tech/56556/anthropic-expands-text-watermarking-to-older-claude-versions-beginning-november-3","source_name":"Mashable",
  "more_sources":[{"label":"Claude Help Center","url":"https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content"},{"label":"Techweez","url":"https://techweez.com/2026/11/02/anthropic-is-bringing-text-watermarking-to-more-claude-models/"}]},
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
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=2, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", len(added))
