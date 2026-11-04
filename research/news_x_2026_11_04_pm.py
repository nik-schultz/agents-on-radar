"""Nov 4, 2026 PM news run: 3 new items + X re-measure (research/x_news_measure_2026_11_04_pm.json.txt)."""
import json
MEASURED = "2026-11-04"
raw = open("research/x_news_measure_2026_11_04_pm.json.txt").read()
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
 {"id":"grok-bot-phone-calls","date":"2026-11-04","category":"feature","company":"xAI","impact":"notable",
  "headline":"Grok Bot can now phone businesses for you, like cancelling a plan or booking an appointment",
  "explainer":"Tell Grok Bot who to call and why, approve the call, and it waits on hold, works the phone menu and talks to the agent while you watch a live transcript and can take over at any time, then it sends you a summary. It only calls U.S. numbers for now (not Washington or Illinois), says up front that it's a virtual assistant, and some reps may refuse to deal with an AI.",
  "source_url":"https://teslanorth.com/2026/11/04/grok-bot-phone-calls-live/","source_name":"TeslaNorth",
  "more_sources":[{"label":"Teslarati","url":"https://www.teslarati.com/elon-musks-grok-bot-is-picking-up-the-phone-now-and-the-first-calls-are-wild/"}],
  "x": xb("2118043939592942052","bot")},
 {"id":"ricursive-ripple-65b-preview","date":"2026-11-04","category":"model release","company":"Ricursive","impact":"notable",
  "headline":"Ricursive releases Ripple-65B Preview, a free open coding model small enough to run on a high-end laptop",
  "explainer":"Ripple-65B is a downloadable model (Apache 2.0 license) that its maker says is the best U.S. open model at agent-style coding, and it can run on a MacBook Pro or NVIDIA DGX Spark. Hosted versions start around $0.20 in / $0.60 out per million tokens on OpenRouter; the benchmark scores are Ricursive's own.",
  "source_url":"https://www.ricursive.com/ripple","source_name":"Ricursive Intelligence",
  "more_sources":[{"label":"Together AI","url":"https://www.together.ai/models/ripple-65b-preview"}],
  "x": xb("2118046765857546733","RicursiveAI")},
 {"id":"anthropic-claude-vault-particles","date":"2026-11-04","category":"industry","company":"Anthropic","impact":"notable",
  "headline":"Anthropic's lab used Claude to map a mystery protein 'vault' from bacteria-infecting viruses",
  "explainer":"Claude searched billions of proteins, designed the DNA and processed the microscope data, so a step that normally takes three days took about 90 minutes and a first 3D model was ready in 34 hours. It's an example of AI speeding up real lab science; the scientists still chose what to test, and the paper isn't peer-reviewed yet.",
  "source_url":"https://www.anthropic.com/research/investigating-vault-particles-with-claude","source_name":"Anthropic",
  "more_sources":[{"label":"Science","url":"https://www.science.org/content/article/ai-company-s-research-deepens-mystery-vaults-cells-strangest-particles"}],
  "x": xb("2118073665296228863","AnthropicAI")},
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
