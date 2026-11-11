"""Nov 11, 2026 PM news run: add 4 items, refresh X numbers (raw: research/x_news_measure_2026_11_11_pm.json.txt)."""
import json, re
raw = open("research/x_news_measure_2026_11_11_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-11T20:27:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"gemini-decisions-api","date":"2026-11-11","category":"model release","company":"Google","impact":"notable",
  "headline":"Google's new Gemini Decision 1 model answers up to 1,000 yes/no or pick-one questions in a fraction of a second",
  "explainer":"Instead of writing a reply, it scores fixed choices (is this email urgent, which tool should the bot use, does this photo break a rule) and returns how confident it is in about 150-250 milliseconds. It's a developer tool in Google AI Studio at $0.10 per million input tokens with nothing charged for output, so bot builders can make cheap, fast sorting and routing steps without paying a big model to think.",
  "source_url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/","source_name":"Google blog",
  "x": xblock("2120581433639198885","OfficialLoganK","official")},
 {"id":"baidu-ernie-5-5-flash-preview","date":"2026-11-11","category":"model release","company":"Baidu","impact":"notable",
  "headline":"Baidu releases ERNIE 5.5 Flash Preview, a fast model for coding and office work that it plans to make free to download",
  "explainer":"It's the first trained-up version of the ERNIE 5.5 Flash base Baidu posted last week, with a 1-million-token memory, and developers can already use it through Baidu's Qianfan API. Baidu says the weights will be released soon under the Apache 2.0 license, and warns this is an early checkpoint that may still fall short until the full release.",
  "source_url":"https://ernie.baidu.com/release/ernie-5-5-flash-preview/","source_name":"Baidu ERNIE",
  "x": xblock("2120425542688379314","Baidu_ERNIE","official")},
 {"id":"gmail-help-me-write-all-workspace","date":"2026-11-10","category":"feature","company":"Google","impact":"notable",
  "headline":"Gmail's AI 'Help me write' and thread summaries are coming to every work and school account",
  "explainer":"All Google Workspace users 18 and older will get Gemini email drafting and an AI summary at the top of long threads over about two weeks, starting Nov 10. Both are on by default; you can switch them off yourself, and your admin can turn them off for everyone.",
  "source_url":"https://workspaceupdates.googleblog.com/2026/11/expanding-gemini-in-gmail-to-more-Google-Workspace-users.html","source_name":"Google Workspace Updates",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/ai-artificial-intelligence/1031489/google-is-bringing-gmails-help-me-write-ai-tool-to-work-accounts"}]},
 {"id":"google-workspace-skills-rollout","date":"2026-11-09","category":"feature","company":"Google","impact":"notable",
  "headline":"Skills, reusable instructions for Gemini, are rolling out across Gmail, Docs, Slides, Drive and Chat for work accounts",
  "explainer":"You write your team's rules, templates and reference files once as a skill, and Gemini applies it automatically when it fits or when you @mention it; skills can also kick off Workspace Studio automations. It uses the same open SKILL.md format as other AI tools, so you can copy instructions between them by hand; Rapid Release domains get it first and Scheduled Release domains from Nov 30.",
  "source_url":"https://workspaceupdates.googleblog.com/2026/11/skills-in-workspace.html","source_name":"Google Workspace Updates"},
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
