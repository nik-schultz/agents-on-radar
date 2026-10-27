"""Oct 27, 2026 AM news run: adds Ant Group LingGuang 2.0 and Riverside Agents; refreshes X numbers on 23 items
posted since Oct 19. Numbers: research/x_news_measure_2026_10_27_am.json.txt (get_posts_by_ids, measured 2026-10-27 ~6:30 AM CT).
No official X post found for either new item (no @AntGroup or @RiversidedotFM launch post), so no x block."""
import json, re
M = "2026-10-27"
raw = open("research/x_news_measure_2026_10_27_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
n_ref = 0
for it in data["items"]:
    x = it.get("x")
    if not x: continue
    pid = x["url"].rsplit("/", 1)[1]
    if pid in posts:
        m = posts[pid]["public_metrics"]
        x.update(likes=m["like_count"], reposts=m["repost_count"], views=m["impression_count"], measured_at=M)
        n_ref += 1
NEW = [
 {"id":"riverside-agents","date":"2026-10-26","category":"agent launch","company":"Riverside","impact":"notable",
  "headline":"Riverside adds a team of AI agents that edit, clip and post your videos and podcasts",
  "explainer":"If you record a podcast or videos on Riverside, four new agents can now prep your interview questions, edit the recording into a finished episode, cut social clips, and write captions and schedule posts. They're on web and mobile on every Riverside plan (some features depend on your tier), and nothing goes live until you approve it.",
  "source_url":"https://riverside.com/blog/first-team-of-ai-agents-built-for-video","source_name":"Riverside",
  "more_sources":[{"label":"Podnews: Riverside launches Riverside Agents","url":"https://podnews.net/press-release/riverside-agents"},
                  {"label":"Forbes: Riverside Agents are a new team for AI production of podcasts","url":"https://www.forbes.com/sites/marksparrow/2026/10/26/riverside-agents-are-a-new-team-for-ai-production-of-podcasts/"}]},
 {"id":"ant-lingguang-2","date":"2026-10-26","category":"agent launch","company":"Ant Group","impact":"notable",
  "headline":"Ant Group's LingGuang 2.0 turns its AI assistant into a helper that acts before you ask",
  "explainer":"Ant Group, the company behind Alipay, upgraded its LingGuang app into a personal agent that, with your permission, keeps working after you close the chat, following up on tasks and flagging things like price drops on a trip you booked or a subscription you forgot. It's another sign that everyday assistants are moving from answering questions to quietly running errands in the background.",
  "source_url":"https://www.businesswire.com/news/home/20261026586960/en/Ant-Group-Upgrades-LingGuang-to-2.0-Turning-Its-AI-Assistant-into-a-Proactive-Personal-Agent","source_name":"Business Wire (Ant Group)"},
]
for n in NEW:
    assert n["id"] not in byid, n["id"]
    data["items"].append(n)
order = ["id","date","category","company","impact","headline","explainer","source_url","source_name","more_sources","x"]
data["items"] = [{k: x[k] for k in order if k in x} | {k: v for k, v in x.items() if k not in order} for x in data["items"]]
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
# NEWS_CO entries for new companies
b = "scripts/build.py"; s = open(b).read()
if '"Riverside"' not in s:
    s = s.replace('"Walmart": ("Wm", "#6fb6ff")}', '"Walmart": ("Wm", "#6fb6ff"),\n           "Riverside": ("Rv", "#ff9ad5"), "Ant Group": ("AG", "#7fe0c3")}', 1)
    assert '"Riverside"' in s
    open(b,"w").write(s)
print("refreshed", n_ref)
