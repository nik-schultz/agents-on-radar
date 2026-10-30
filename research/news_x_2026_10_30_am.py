"""Oct 30, 2026 AM news run: 3 new items + X re-measure (research/x_news_measure_2026_10_30_am.json.txt)."""
import json
MEASURED = "2026-10-30"
raw = open("research/x_news_measure_2026_10_30_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"chatgpt-pro-usage-doubled","date":"2026-10-29","category":"pricing","company":"OpenAI","impact":"notable",
  "headline":"OpenAI doubles ChatGPT Pro's Work and Codex limits and cancels the planned Pro 200 cut",
  "explainer":"Same price, more agent time: Pro 100 and Pro 500 now get twice their previous Work and Codex allowance, Business Premium gets more too, and the Pro 200 reduction announced in September is off. It applies automatically from Oct 29, and usage by your dot still counts separately.",
  "source_url":"https://help.openai.com/en/articles/6825453-chatgpt-release-notes","source_name":"ChatGPT release notes",
  "more_sources":[{"label":"BleepingComputer","url":"https://www.bleepingcomputer.com/news/artificial-intelligence/openai-doubles-chatgpt-pro-usage-limits-after-backlash-over-planned-50-percent-cut/"},{"label":"The Decoder","url":"https://the-decoder.com/openai-doubles-usage-limits-on-pro-plans-as-competition-with-anthropic-heats-up/"}],
  "_x":("2115850175868727621","official")},
 {"id":"google-jules-winding-down","date":"2026-10-29","category":"industry","company":"Google","impact":"notable",
  "headline":"Google is shutting down Jules, its background coding agent, and folding it into Antigravity",
  "explainer":"If you used Jules to fix bugs or write code in the background, start moving that work to Google's Antigravity, which will get Jules-style remote tasks. Google hasn't given a shutdown date yet, so save anything you need from Jules now.",
  "source_url":"https://x.com/julesagent/status/2115883717705261283","source_name":"Jules on X",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/tech/1022729/google-is-sunsetting-its-ai-coding-agent-jules"}],
  "_x":("2115883717705261283","official")},
 {"id":"meta-style-sketch-ai-closet","date":"2026-10-29","category":"feature","company":"Meta","impact":"minor",
  "headline":"Meta quietly launches Style Sketch, an AI app that plans outfits from the clothes you own",
  "explainer":"It builds a virtual closet from your Instagram photos or pictures you snap, suggests outfits, shows them on a model matched to your body, and plans day-by-day trip outfits using the weather. For now it's only in Indonesia, Singapore and Thailand.",
  "source_url":"https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/","source_name":"TechCrunch",
  "_x":("2115263172923756995","coverage")},
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
