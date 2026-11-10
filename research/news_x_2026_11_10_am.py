"""Nov 10, 2026 AM news run: add 4 items, refresh X numbers (raw: research/x_news_measure_2026_11_10_am.json.txt)."""
import json, re
raw = open("research/x_news_measure_2026_11_10_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-10T12:28:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"meta-muse-smartwatch","date":"2026-11-09","category":"feature","company":"Meta","impact":"notable",
  "headline":"Meta's Muse agent now works on Apple Watch and Wear OS watches",
  "explainer":"You can call Muse, text it or dictate a request from your wrist, and Apple Watch gets a watch-face shortcut, so you can hand it a quick errand like a booking or a calendar clash without pulling out your phone. The Apple Watch app is a companion to the iPhone app (watchOS 9 or later), Meta hasn't listed which Wear OS watches work, and since Muse can reach your email and calendar, only connect what you're comfortable with.",
  "source_url":"https://www.macrumors.com/2026/11/09/meta-muse-apple-watch/","source_name":"MacRumors",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/tech/1030492/muse-is-now-available-on-smartwatches"}],
  "x": xblock("2119919277692383330","Muse","official")},
 {"id":"google-antigravity-knowledge-work","date":"2026-11-09","category":"feature","company":"Google","impact":"notable",
  "headline":"Google Antigravity gets a simpler Knowledge Work layout for research and writing, not just coding",
  "explainer":"The same agent, models, plugins and connectors are there, but the Git, terminal and code-diff clutter is hidden and permission prompts are described in plain words. Personal Google accounts can switch in Settings, General, Interface Layout (version 2.30.0); business and enterprise accounts stay on the developer layout, and voice mode is now rolled out to everyone else.",
  "source_url":"https://antigravity.google/blog/antigravity-for-knowledge-work","source_name":"Google Antigravity",
  "more_sources":[{"label":"Antigravity changelog","url":"https://antigravity.google/docs/changelog/"},
                  {"label":"9to5Google","url":"https://9to5google.com/2026/11/09/google-antigravity-knowledge-work/"}],
  "x": xblock("2119913586109579283","antigravity","official")},
 {"id":"anthropic-ipo-roadshow","date":"2026-11-10","category":"industry","company":"Anthropic","impact":"notable",
  "headline":"Anthropic starts its IPO roadshow, aiming for $70 to $78 a share on Nasdaq as ANT",
  "explainer":"Claude's maker plans to sell about 825 million shares, so the listing is close but the shares aren't sold yet. Nothing changes in Claude for you today; once public, Anthropic has to report its business openly, which can shape prices and plans later.",
  "source_url":"https://www.anthropic.com/news/roadshow-launch","source_name":"Anthropic",
  "x": xblock("2120117722230968385","AnthropicAI","official")},
 {"id":"openai-control-room","date":"2026-11-09","category":"industry","company":"OpenAI","impact":"minor",
  "headline":"OpenAI built Control Room, an internal off switch that halts research AI jobs within 35 seconds",
  "explainer":"It covers OpenAI's own training and testing work, not the ChatGPT you use, and it blocks a flagged job's model output even if the job itself keeps running. It's a sign labs are adding hard stops as agents get more capable.",
  "source_url":"https://openai.com/index/control-room","source_name":"OpenAI",
  "x": xblock("2119913172039868579","OpenAI","official")},
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
