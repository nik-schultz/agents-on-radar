"""Nov 4, 2026 AM news run: 3 new items + X re-measure (research/x_news_measure_2026_11_04_am.json.txt)."""
import json
MEASURED = "2026-11-04"
raw = open("research/x_news_measure_2026_11_04_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
def xb(pid, author):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": "official",
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count")), "views": m["impression_count"],
            "posted_at": p["created_at"][:10], "measured_at": MEASURED}
def xc(pid, author):
    b = xb(pid, author); b["kind"] = "coverage"; return b
NEW = [
 {"id":"tencent-hy4-open-model","date":"2026-11-04","category":"model release","company":"Tencent","impact":"notable",
  "headline":"Tencent releases Hy4, an open-weight model that can now see images and run longer agent tasks",
  "explainer":"Hy4 is one of the strongest open models you can get, now with image and chart understanding and better long multi-step tasks, at about $0.90 per million input tokens and $2.70 per million output tokens (half off on Tencent Cloud through Dec 31). Tencent says the downloadable weights come in the next few days and admits it still trails the top closed models from OpenAI, Anthropic and Google.",
  "source_url":"https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/","source_name":"Tencent",
  "more_sources":[{"label":"South China Morning Post","url":"https://www.scmp.com/tech/big-tech/article/3373227/tencent-unveils-hy4-open-weight-ai-race-deepseek-zai-alibaba-heats"}],
  "x": xb("2117870250838630539","TencentHunyuan")},
 {"id":"netflix-ai-discover-tab","date":"2026-11-03","category":"feature","company":"Netflix","impact":"notable",
  "headline":"Netflix tests an AI Discover tab that picks something to watch based on your mood",
  "explainer":"Pick a theme like \"something light\", \"scare me\" or \"quick watches\" and Netflix's AI suggests titles, and you can tell it to stop showing ones you don't want. It's rolling out first to English-language US members on supported TVs, as an experiment Netflix may change.",
  "source_url":"https://techcrunch.com/2026/11/03/netflixs-new-ai-discover-tab-helps-you-find-something-to-watch-based-on-your-mood/","source_name":"TechCrunch",
  "x": xc("2117776361318195613","YahooFinance")},
 {"id":"google-guided-learning-search-classroom","date":"2026-11-03","category":"feature","company":"Google","impact":"notable",
  "headline":"Google brings Guided Learning homework help to Classroom and Search, and switches Gemini off by default for K-12 students",
  "explainer":"Guided Learning walks a student through a problem step by step instead of handing over the answer; it's live worldwide in Google Classroom for teacher-assigned work and is being piloted in Search at select US schools this month. Parents should know that Gemini and Search will be off by default for K-12 school accounts until the school turns them on, and Search can't be enabled without its AI features.",
  "source_url":"https://blog.google/products-and-platforms/products/education/ai-learning-era-updates-2026/","source_name":"Google",
  "more_sources":[{"label":"9to5Google","url":"https://9to5google.com/2026/11/03/google-search-ai-guided-learning-changes/"},{"label":"AP News","url":"https://apnews.com/article/ai-schools-classroom-students-google-7ba4219e505db1c11d672f6eefe7155a"}],
  "x": xc("2117645444717158420","Marie_Haynes")},
]
p = "data/news.json"; data = json.load(open(p))
have = {x["id"] for x in data["items"]}
n = 0
for x in data["items"]:
    if x.get("x"):
        pid = x["x"]["url"].rsplit("/",1)[1]
        if pid in posts:
            m = posts[pid]["public_metrics"]
            x["x"].update(likes=m["like_count"], reposts=m.get("repost_count", m.get("retweet_count")), views=m.get("impression_count"), measured_at=MEASURED); n += 1
added = [it["id"] for it in NEW if it["id"] not in have]
data["items"] = [it for it in NEW if it["id"] not in have] + data["items"]
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=2, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", added)
