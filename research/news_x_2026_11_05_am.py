"""Nov 5, 2026 AM news run: 1 new items + X re-measure (research/x_news_measure_2026_11_05_am.json.txt)."""
import json
MEASURED = "2026-11-05"
raw = open("research/x_news_measure_2026_11_05_am.json.txt").read()
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
 {"id":"chatgpt-images-2-6-gifs","date":"2026-11-04","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"ChatGPT Images 2.6 can make animated GIFs and remember a saved reference photo",
  "explainer":"Ask ChatGPT for a looping GIF or to animate a still photo, and save a photo (say, of your dog) under a name so you can reuse it later by typing @ and that name. It's on all ChatGPT plans and in Codex, about 50% faster than before, with GIFs rolling out gradually; ChatGPT can't edit an animated GIF you upload.",
  "source_url":"https://help.openai.com/en/articles/11084440-images-in-chatgpt","source_name":"OpenAI Help Center",
  "more_sources":[{"label":"heise online","url":"https://www.heise.de/en/news/ChatGPT-Images-2-6-adds-GIFs-SVGs-and-speed-11512895.html"},{"label":"OpenAI system card","url":"https://deploymentsafety.openai.com/chatgpt-images-2-6/gif-risks-safeguards-and-evaluations"}],
  "x": xb("2118124944928432327","OpenAI")},
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
for x in data["items"]:
    if x["id"]=="kimi-k3-1-pro":
        x["explainer"]="Moonshot's Kimi K3.1 Pro is in the Kimi apps and API, and its full weights are now on Hugging Face (under Moonshot's own Kimi K3.1 Pro License), though at 2.8 trillion parameters it needs data-center hardware to run. Its API price is $2 in / $10 out per million tokens, half of Claude Opus 5.5's list price; the coding scores are Moonshot's own."
        x.setdefault("more_sources",[]).append({"label":"Hugging Face model card","url":"https://huggingface.co/moonshotai/Kimi-K3.1-Pro"})
json.dump(data, open(p,"w"), indent=2, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", added)
