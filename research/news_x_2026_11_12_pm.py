"""Nov 12, 2026 PM news run: add 3 items + Hydrogen pricing row (raw: research/x_news_measure_2026_11_12_pm.json.txt, local only)."""
import json
raw = open("research/x_news_measure_2026_11_12_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-12T20:31:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"gemini-4-hydrogen","date":"2026-11-12","category":"model release","company":"Google","impact":"major",
  "headline":"Google releases Gemini 4 Hydrogen, a fast Gemini 4 model for everyone, including free users",
  "explainer":"Your Gemini app, Google Search and Gemini in Sheets now get a quicker Gemini 4 model that Google says follows instructions more closely and picks the right tools more often, so everyday tasks like email drafts, comparisons and Gmail or Drive lookups need less back-and-forth. Free Gemini users get it through auto model selection; developers pay $1.50 per million input tokens and $7.50 per million output tokens, with a free tier in the Gemini API.",
  "source_url":"https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/","source_name":"Google blog",
  "more_sources":[{"label":"Gemini API pricing","url":"https://ai.google.dev/gemini-api/docs/pricing"}],
  "x": xblock("2120940338869055788","GoogleDeepMind","official")},
 {"id":"openai-daybreak-red-team-defense-factory","date":"2026-11-12","category":"agent launch","company":"OpenAI","impact":"minor",
  "headline":"OpenAI launches Daybreak Red Team and Defense Factory, teams of AI agents that find and fix security holes",
  "explainer":"These are tools for security and engineering teams, not everyday users: Red Team agents test web apps to confirm which flaws can really be exploited, and Defense Factory agents trace each flaw through the code and propose a patch in Codex for an engineer to review. Red Team is in early access with a waitlist, and Defense Factory is available through the Daybreak plugin in Codex; OpenAI hasn't shared prices.",
  "source_url":"https://thedeepview.com/articles/openai-sees-a-new-enterprise-frontier-in-cyber","source_name":"The Deep View",
  "more_sources":[{"label":"OpenAI: Daybreak Red Team","url":"https://openai.com/daybreak/red-team/"},{"label":"OpenAI: Daybreak Defense Factory","url":"https://openai.com/daybreak/defense-factory/"}]},
 {"id":"wirex-navoka-agent-own-card","date":"2026-11-12","category":"agent launch","company":"Wirex","impact":"notable",
  "headline":"Wirex's Navoka gives an AI agent its own bank account and debit card, with spending limits you set",
  "explainer":"Instead of handing an AI your own card, Navoka gives the agent a separate account and card that you top up, and every payment is checked against the merchants, caps and countries you allow, with anything else waiting for your approval. It's invite-only for now, works by messaging it on Telegram or connecting it to ChatGPT, Claude or Grok, and has a kill switch to freeze the card.",
  "source_url":"https://www.prnewswire.com/news-releases/wirex-launches-navoka-an-ai-agent-that-pays-from-its-own-bank-account-and-card-302938065.html","source_name":"PR Newswire (Wirex)"},
]
p = "data/news.json"; data = json.load(open(p))
have = {i["id"] for i in data["items"]}
added = [n for n in NEW if n["id"] not in have]
data["items"] = added + data["items"]
data["items"].sort(key=lambda i: i["date"], reverse=True)
json.dump(data, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
print("added", [n["id"] for n in added])
# pricing
pp = "data/ai-pricing.json"; pr = json.load(open(pp))
if not any(r.get("model")=="gemini-4-hydrogen" for r in pr["api"]):
    i = next(k for k,r in enumerate(pr["api"]) if r.get("model")=="gemini-3.8-flash")
    pr["api"].insert(i, {"provider":"Google","model":"gemini-4-hydrogen","tier":"mid","input":1.5,"output":7.5,"cached_input":0.075,
      "note":"Fast Gemini 4 model for everyday and agent work, released Nov 12, 2026; same price across the full 1M-token context. Free tier available.",
      "source_url":"https://ai.google.dev/gemini-api/docs/pricing","checked_on":"2026-11-12"})
pr["not_verified"] = [r for r in pr["not_verified"] if r.get("what")!="Gemini 4 Carbon API price"]
json.dump(pr, open(pp,"w"), indent=1, ensure_ascii=False); open(pp,"a").write("\n")
print("pricing ok")
