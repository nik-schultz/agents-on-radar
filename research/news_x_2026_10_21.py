"""Adds measured X engagement + impact to data/news.json (Oct 21, 2026).
Numbers come from research/x_news_measure_2026_10_21.json.txt (X API get_posts_by_ids, measured 2026-10-21)."""
import json, re
MEASURED = "2026-10-21"
raw = open("research/x_news_measure_2026_10_21.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
# news id -> (post id, kind) ; kind: official = company/founder account, coverage = most-engaged post about it
MAP = {
 "openai-models-on-google-cloud": ("2112896659608785181", "official"),
 "mistral-voxtral-3": ("2112574615318876178", "official"),
 "openai-12-hour-prompt-caching": ("2112603916076781778", "official"),
 "deepseek-v4-1-flash-1017": ("2111375640717033777", "official"),
 "deepseek-search-fetch-api": ("2111375650414309859", "official"),
 "meta-muse-spark-open": ("2110779754274292212", "official"),
 "grok-voice-3": ("2110421964095713743", "coverage"),
 "gemini-4-argon-available": ("2110039322229649783", "official"),
 "meta-muse-wonder": ("2109691148943999167", "official"),
 "gpt-6-for-everyone": ("2107894997538525580", "official"),
 "claude-haiku-5-5": ("2107894039626277339", "official"),
 "claude-sonnet-cache-cut-and-credits": ("2107894060229034197", "official"),
 "mistral-large-4-preview": ("2107457414387622310", "official"),
 "gpt-6-1-sol": ("2104986129686741046", "official"),
 "grok-bot-team-bots": ("2104661562715967548", "official"),
 "claude-opus-5-5": ("2102435511222890900", "official"),
 "gpt-6-sol-and-luna": ("2102460975790137662", "official"),
 "grok-4-7": ("2102071804495872374", "official"),
 "openai-dots": ("2104984504133918973", "official"),
 "claude-google-workspace": ("2107522596845822135", "official"),
 "claude-dashboards-motion": ("2108271552991252810", "official"),
 "deepseek-deepinfer": ("2112476496283775135", "official"),
}
IMPACT = {
 "major": ["gemini-4-argon-available","meta-muse-wonder","gpt-6-for-everyone","claude-opus-5-5","grok-4-7","openai-dots"],
 "minor": ["openai-12-hour-prompt-caching","deepseek-search-fetch-api","gemini-spark-becomes-task","openai-agents-sandbox-billing","deepseek-deepinfer"],
}
NEW = [
 {"id":"deepseek-deepinfer","date":"2026-10-20","category":"industry","headline":"DeepSeek open-sources the engine that runs its own API",
  "explainer":"DeepInfer is the software DeepSeek uses to serve V4.1 Flash cheaply, now free under Apache 2.0. Hosting companies can copy the tricks, which could push the price of running open models down for your bots.",
  "source_url":"https://github.com/deepseek-ai/DeepInfer","source_name":"DeepSeek (GitHub)",
  "more_sources":[{"label":"The New Stack","url":"https://thenewstack.io/deepseek-deepinfer-huawei-nvidia/"}]},
 {"id":"claude-dashboards-motion","date":"2026-10-08","category":"feature","headline":"Claude can now build live dashboards from your data and animated explainers",
  "explainer":"Ask a question in plain words and Claude builds a dashboard that stays current, showing the query behind every number. Motion turns a report into a short animation you can export as MP4. Both are in beta on paid plans (Motion on Team and Enterprise).",
  "source_url":"https://claude.com/resources/articles/dashboards-and-motion","source_name":"Anthropic",
  "more_sources":[{"label":"Reuters via Investing.com","url":"https://www.investing.com/news/stock-market-news/anthropic-launches-dashboard-animation-tools-for-claude-4939641"}]},
 {"id":"claude-google-workspace","date":"2026-10-06","category":"feature","headline":"Claude now works inside Google Docs, Sheets and Slides",
  "explainer":"A Claude sidebar can read the file you have open and edit it in place, asking before each change by default. It's in beta on all paid Claude plans, so your doc-and-spreadsheet chores can go to Claude without copy-pasting.",
  "source_url":"https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides","source_name":"Anthropic",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/ai-artificial-intelligence/1006111/you-can-use-claude-directly-in-google-docs-slides-and-sheets-with-a-new-add-on"}]},
 {"id":"openai-dots","date":"2026-09-29","category":"agent launch","headline":"OpenAI launches dots: always-on agents with their own computer",
  "explainer":"A dot runs on GPT-6 Astra with its own cloud computer, connects to your apps, and keeps working between chats, checking with you on decisions. It's rolling out to ChatGPT Pro and Business Premium users first (not the EU, Switzerland or the UK on Pro at launch).",
  "source_url":"https://openai.com/index/introducing-dots/","source_name":"OpenAI",
  "more_sources":[{"label":"OpenAI Help Center","url":"https://help.openai.com/en/articles/20001530-getting-started-with-your-dot"},{"label":"The Verge","url":"https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor"}]},
]
p = "data/news.json"; data = json.load(open(p))
items = [x for x in data["items"] if x["id"] not in {n["id"] for n in NEW}]
for x in items:
    if x["id"] == "groq-muse-spark-open":
        x.update({"id":"meta-muse-spark-open","headline":"Meta releases Muse Spark Open, the most capable US open-weight model so far",
          "explainer":"Meta's new open model is built for coding and agent work, and you can call it on day one through Groq, OpenRouter, Together AI and other APIs. Groq runs it at 350+ tokens per second per user. That speed matters for agents, because each task is a long chain of model calls.",
          "source_url":"https://research.meta.ai/blog/muse-spark-open","source_name":"Meta",
          "more_sources":[{"label":"Groq (limited preview)","url":"https://groq.com/blog/meta-s-muse-spark-open-release-is-now-in-limited-preview-on-groqcloud"},{"label":"Hugging Face","url":"https://huggingface.co/blog/meta-muse-spark-open"}]})
items += NEW
for x in items:
    x["impact"] = next((k for k, v in IMPACT.items() if x["id"] in v), "notable")
    if x["id"] in MAP:
        pid, kind = MAP[x["id"]]; q = posts[pid]; m = q["public_metrics"]
        x["x"] = {"url": q["url"], "author": "@" + users[q["author_id"]], "kind": kind,
                  "likes": m["like_count"], "reposts": m["repost_count"], "views": m.get("impression_count"),
                  "posted_at": q["created_at"][:10], "measured_at": MEASURED}
    else:
        x.pop("x", None)
order = ["id","date","category","impact","headline","explainer","source_url","source_name","more_sources","x"]
items = [{k: x[k] for k in order if k in x} for x in items]
items.sort(key=lambda x: x["date"], reverse=True)
data["items"] = items
data["impact_levels"] = ["major","notable","minor"]
data["_impact_rule"] = "Importance, not popularity. major = a new flagship model or a major agent launch from a big lab (OpenAI, Anthropic, Google, Meta, xAI). minor = small changelog-level tweaks (a billing detail, a new tool price, a UI move, infrastructure code). notable = everything in between."
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print(len(items), sum(1 for x in items if "x" in x))
