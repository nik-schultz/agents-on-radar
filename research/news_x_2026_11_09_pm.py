"""Nov 9, 2026 PM news run: add 4 items, refresh X numbers (raw: research/x_news_measure_2026_11_09_pm.json.txt)."""
import json, re
raw = open("research/x_news_measure_2026_11_09_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-09T20:45:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"claude-fable-5-2","date":"2026-11-09","category":"model release","company":"Anthropic","impact":"major",
  "headline":"Anthropic releases Claude Fable 5.2, its top model, 20% cheaper and up to 30% faster",
  "explainer":"Claude's most capable generally available model gets better at coding, reasoning and vision, and is built to run long projects and teams of agents. It's out today on all platforms at $8 / $40 per million tokens (down from $10 / $50), eligible paid Claude plans get extra Fable usage this week, and the cyber- and biology-unlocked twin, Mythos 5.2, stays limited to vetted organizations.",
  "source_url":"https://www.anthropic.com/claude-fable-and-mythos-5-2","source_name":"Anthropic",
  "more_sources":[{"label":"Anthropic pricing","url":"https://docs.anthropic.com/en/docs/about-claude/pricing"},
                  {"label":"CNBC","url":"https://www.cnbc.com/2026/11/09/anthropic-claude-fable-5-2-mythos-5-2.html"},
                  {"label":"The Verge","url":"https://www.theverge.com/ai-artificial-intelligence/1030005/anthropic-claude-fable-mythos-5-2"}],
  "x": xblock("2119867114450268322","claudeai","official")},
 {"id":"meta-muse-ember","date":"2026-11-09","category":"model release","company":"Meta","impact":"notable",
  "headline":"Meta's new Muse Ember is a tiny, very cheap model built for the busywork agents repeat all day",
  "explainer":"At $0.10 in / $0.50 out per million tokens, Ember is meant for tool calls, quick coding fixes, sorting and reading long documents, and Meta says it matches Claude Haiku 5.5 at about a third of the cost per task. It's on the Meta Model API and Muse Code now, with a 1M-token context window, so cheap helper bots can run far more steps for pennies.",
  "source_url":"https://research.meta.ai/blog/muse-ember","source_name":"Meta AI",
  "x": xblock("2119853591703998787","AIatMeta","official")},
 {"id":"chatgpt-dots-multiple-computers","date":"2026-11-09","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"ChatGPT dots can now use more than one of your computers and you pick which one per task",
  "explainer":"Connect each computer from the ChatGPT desktop app on it, then tell your dot which machine a task should run on, for example building and testing on a spare desktop while you keep working on your laptop. Each computer needs the ChatGPT app open and online, and you can revoke access per machine.",
  "source_url":"https://learn.chatgpt.com/docs/dots/computers-and-apps","source_name":"ChatGPT Learn",
  "x": xblock("2119883176726409645","OpenAIDevs","official")},
 {"id":"bytedance-seedream-5-5","date":"2026-11-09","category":"model release","company":"ByteDance","impact":"notable",
  "headline":"ByteDance's Seedream 5.5 image model can keep editing one picture for 100 rounds without it degrading",
  "explainer":"Areas you didn't ask to change stay put, it can make images with transparent backgrounds ready to drop into a design, and photos and small text look more realistic. It's rolling out in Dreamina, CapCut and BytePlus.",
  "source_url":"https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5","source_name":"ByteDance Seed",
  "x": xblock("2119720475068920181","ByteDanceSeed_","official")},
]
p = "data/news.json"; data = json.load(open(p))
have = {i["id"] for i in data["items"]}
refreshed = 0
for it in data["items"]:
    x = it.get("x")
    if not x: continue
    m = re.search(r"status/(\d+)", x["url"])
    if m and m.group(1) in posts:
        pm = posts[m.group(1)]["public_metrics"]
        x["likes"] = pm["like_count"]; x["reposts"] = pm.get("repost_count", pm.get("retweet_count", 0))
        x["views"] = pm.get("impression_count", x.get("views", 0)); x["measured_at"] = MEAS; refreshed += 1
added = [n for n in NEW if n["id"] not in have]
data["items"] = added + data["items"]
data["items"].sort(key=lambda i: i["date"], reverse=True)
json.dump(data, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
print("added", [n["id"] for n in added], "refreshed", refreshed)
