"""Oct 22, 2026 PM news run: adds Anthropic Agent Skills -> AAIF, OpenAI Decisions API GA, Canva Craft,
Gemini Personal Intelligence on Android Auto; refreshes X numbers.
Numbers: research/x_news_measure_2026_10_22_pm.json.txt (get_posts_by_ids, measured 2026-10-22 ~2:30 PM CT)."""
import json
M = "2026-10-22"
raw = open("research/x_news_measure_2026_10_22_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
def xb(pid, author, posted):
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@" + author, "kind": "official", "posted_at": posted}
NEW = [
 {"id":"anthropic-agent-skills-to-aaif","date":"2026-10-22","category":"industry","company":"Anthropic","impact":"notable",
  "headline":"Anthropic hands Agent Skills to a neutral foundation",
  "explainer":"Skills are little instruction folders that teach an AI agent a specific task, and more than 70 tools, including ChatGPT, Cursor and GitHub Copilot, already read them. Moving the standard to the Linux Foundation's Agentic AI Foundation makes it more likely a skill you set up once keeps working across different bots.",
  "source_url":"https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation","source_name":"Anthropic"},
 {"id":"openai-decisions-api-ga","date":"2026-10-22","category":"feature","company":"OpenAI","impact":"minor",
  "headline":"OpenAI's quick-answer Decisions API is now open to all developers",
  "explainer":"The Decisions API turns text or images into short typed answers, like sorting an email or approving a request, without writing a full reply, and it now handles up to 400 questions per request with prompt-cache discounts. Apps built on it can make these small calls faster and cheaper, which adds up for bots that triage a lot.",
  "source_url":"https://developers.openai.com/api/docs/changelog","source_name":"OpenAI API changelog",
  "x": xb("2113346642787086538","OpenAIDevs","2026-10-22")},
 {"id":"canva-craft","date":"2026-10-22","category":"model release","company":"Canva","impact":"notable",
  "headline":"Canva launches Craft, its own image model built for designs with readable text",
  "explainer":"Craft plans the layout first, then makes images up to 2K in about 30 sizes, and is trained on human-made Canva templates so text comes out legible. It's free to try for all Canva users in Dream Lab, and Canva plans to let ChatGPT and Gemini use it too.",
  "source_url":"https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/","source_name":"TechCrunch",
  "x": xb("2113348707223753165","canva","2026-10-22")},
 {"id":"gemini-android-auto-personal-intelligence","date":"2026-10-20","category":"feature","company":"Google","impact":"notable",
  "headline":"Gemini in your car can now use your Gmail, Calendar and Maps to help",
  "explainer":"With your permission, Gemini on Android Auto can pull your flight gate from email, find the restaurant you saved, or take you to your next appointment without you looking anything up. It's rolling out now on Android Auto for eligible personal accounts and is off until you turn it on.",
  "source_url":"https://blog.google/products-and-platforms/platforms/android/android-auto-cars-with-google-built-in-gemini-personal-intelligence/","source_name":"Google",
  "x": xb("2112655614132285592","Google","2026-10-20")},
]
for n in NEW:
    assert n["id"] not in byid, n["id"]
    data["items"].append(n); byid[n["id"]] = n
n_ref = 0
for x in data["items"]:
    b = x.get("x")
    if not b: continue
    pid = b["url"].rstrip("/").rsplit("/",1)[1]
    if pid in posts:
        m = posts[pid]["public_metrics"]
        b.update({"likes":m["like_count"],"reposts":m.get("repost_count", m.get("retweet_count")),"views":m["impression_count"],"measured_at":M})
        n_ref += 1
order = ["id","date","category","company","impact","headline","explainer","source_url","source_name","more_sources","x"]
data["items"] = [{k: x[k] for k in order if k in x} | {k: v for k, v in x.items() if k not in order} for x in data["items"]]
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n_ref)
