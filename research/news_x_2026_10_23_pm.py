"""Oct 23, 2026 PM news run: adds Kimi K3.1 Pro (Moonshot), Cursor computer use, NVIDIA Nemotron 3.5 Bolt E4B 4GB;
refreshes X numbers. Numbers: research/x_news_measure_2026_10_23_pm.json.txt (get_posts_by_ids, measured 2026-10-23 ~2:40 PM CT)."""
import json
M = "2026-10-23"
raw = open("research/x_news_measure_2026_10_23_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
def xb(pid, author, posted):
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@" + author, "kind": "official", "posted_at": posted}
NEW = [
 {"id":"kimi-k3-1-pro","date":"2026-10-23","category":"model release","company":"Moonshot","impact":"notable",
  "headline":"Kimi K3.1 Pro: a new open model that says it nearly matches Claude Opus 5.5 at coding",
  "explainer":"Moonshot's new Kimi K3.1 Pro is out now in the Kimi apps and API, and its full weights are due by Nov 4, so anyone will be able to download and run it. Its API price is $2 in / $10 out per million tokens, half of Claude Opus 5.5's list price; the coding scores are Moonshot's own and haven't been checked independently yet.",
  "source_url":"https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber","source_name":"The Next Web",
  "more_sources":[{"label":"Kimi: Introducing Kimi K3.1 Pro","url":"https://www.kimi.ai/blog/kimi-k3-1-pro"}],
  "x": xb("2113680701770068067","Kimi_Moonshot","2026-10-23")},
 {"id":"cursor-computer-use-desktop","date":"2026-10-23","category":"feature","company":"Cursor","impact":"notable",
  "headline":"Cursor's coding bot can now click and type in other apps on your computer",
  "explainer":"After you update the Cursor app, its agent can drive desktop apps such as the iPhone simulator to test the features it just built, instead of you tapping through them yourself. Because it works by looking at your screen, close private windows before you let it take over.",
  "source_url":"https://x.com/cursor_ai/status/2113661506634305834","source_name":"Cursor (on X)",
  "more_sources":[{"label":"AlphaSignal","url":"https://alphasignal.ai/news/cursor-s-computer-use-lets-its-coding-agent-click-through-desktop-apps"}],
  "x": xb("2113661506634305834","cursor_ai","2026-10-23")},
 {"id":"nvidia-nemotron-3-5-bolt-e4b","date":"2026-10-23","category":"model release","company":"NVIDIA","impact":"notable",
  "headline":"NVIDIA releases a free 4GB AI model for assistants that run on your own device",
  "explainer":"Nemotron 3.5 Bolt E4B is a small, free open model built for fast local voice and device assistants that can follow instructions and use tools, so a simple bot can run on your own computer with no per-message bill. It's text-only with a 64K-token memory, so save bigger jobs for the large cloud models.",
  "source_url":"https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB","source_name":"NVIDIA (Hugging Face)",
  "more_sources":[{"label":"NVIDIA build page","url":"https://build.nvidia.com/nvidia/nemotron-3.5-bolt-e4b"}],
  "x": xb("2113657112408785153","NVIDIAAI","2026-10-23")},
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
