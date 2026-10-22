"""Oct 22, 2026 AM news run: adds Recursive Flint + Meta Muse sharing pause, refreshes X numbers.
Numbers: research/x_news_measure_2026_10_22_am.json.txt (get_posts_by_ids, measured 2026-10-22).
@OpenAI Google Cloud post (2112988118471295323) measured via search_posts_all on 2026-10-22: 4242 likes / 329 reposts / 368443 views."""
import json
M = "2026-10-22"
raw = open("research/x_news_measure_2026_10_22_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
NEW = [
 {"id":"recursive-flint","date":"2026-10-21","category":"model release","company":"Recursive","impact":"notable",
  "headline":"Recursive releases Flint, a free coding model that runs on a laptop",
  "explainer":"Flint is a free, open coding model small enough to run on an ordinary laptop, so a coding bot can work offline, keep your files private and skip per-use fees. Its maker says it still needs smaller, step-by-step tasks than the big paid assistants.",
  "source_url":"https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/","source_name":"TechCrunch",
  "more_sources":[{"label":"Richard Socher on X","url":"https://x.com/RichardSocher/status/2112944385415426249"}],
  "x":{"url":"https://x.com/RichardSocher/status/2112944385415426249","author":"@RichardSocher","kind":"official","posted_at":"2026-10-21"}},
 {"id":"meta-muse-sharing-paused","date":"2026-10-20","category":"feature","company":"Meta","impact":"notable",
  "headline":"Meta pauses Muse chat sharing after shared chats turned up on the web",
  "explainer":"Researchers found more than 6,800 Muse share links through public web records, some showing loan applications, revenue reviews and work calendars, so Meta switched sharing off while it reviews. Treat any AI \"share link\" as public, and keep private details out of chats you share.",
  "source_url":"https://www.theverge.com/tech/1014627/meta-muse-ai-sharing-ai-chats","source_name":"The Verge",
  "more_sources":[{"label":"Ars Technica","url":"https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/"}]},
]
for n in NEW:
    assert n["id"] not in byid
    data["items"].append(n); byid[n["id"]] = n
g = byid["openai-models-on-google-cloud"]
g["x"] = {"url":"https://x.com/OpenAI/status/2112988118471295323","author":"@OpenAI","kind":"official","likes":4242,"reposts":329,"views":368443,"posted_at":"2026-10-21","measured_at":M}
n_ref = 0
for x in data["items"]:
    xb = x.get("x")
    if not xb: continue
    pid = xb["url"].rstrip("/").rsplit("/",1)[1]
    if pid in posts:
        m = posts[pid]["public_metrics"]
        xb.update({"likes":m["like_count"],"reposts":m.get("repost_count", m.get("retweet_count")),"views":m["impression_count"],"measured_at":M})
        n_ref += 1
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n_ref)
