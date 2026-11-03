"""Nov 3, 2026 PM news run: 3 new items + X re-measure (research/x_news_measure_2026_11_03_pm.json.txt)."""
import json
MEASURED = "2026-11-03"
raw = open("research/x_news_measure_2026_11_03_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
def xb(pid, author):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": "official",
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count")), "views": m["impression_count"],
            "posted_at": p["created_at"][:10], "measured_at": MEASURED}
NEW = [
 {"id":"openai-engineering-physical-world","date":"2026-11-03","category":"industry","company":"OpenAI","impact":"notable",
  "headline":"OpenAI shows ChatGPT and Codex designing physical products, including a small device built with almost no human edits",
  "explainer":"OpenAI says its models now help engineers with CAD drawings, circuit boards and simulations, and two staff used GPT-6 Astra to design a small Codex talk-to device that a factory then built in under a month. It's a progress report and a call for engineering partners, not a new product you can buy, and OpenAI admits the model still missed manufacturing limits that humans had to fix.",
  "source_url":"https://openai.com/index/accelerating-engineering-for-the-physical-world","source_name":"OpenAI",
  "x": xb("2117692475775258785","OpenAI")},
 {"id":"anthropic-flashprove-provable-inference","date":"2026-11-03","category":"industry","company":"Anthropic","impact":"notable",
  "headline":"Anthropic open-sources FlashProve, a way to mathematically prove which AI model wrote a reply",
  "explainer":"FlashProve lets an AI company publish a fingerprint of its model and then attach a proof to each answer showing that exact model produced it, so you could check you're not being quietly served a cheaper model. It's an early research prototype (tested on Meta's open Llama 4 Maverick, short 1,024-token requests only), and Anthropic hasn't said it will offer proofs for Claude.",
  "source_url":"https://www.anthropic.com/research/provable-inference","source_name":"Anthropic",
  "more_sources":[{"label":"FlashProve technical report","url":"https://assets.claude.com/a492b1fea80e6dcfe4e908ed77bd44961f8c02c2.pdf"}],
  "x": xb("2117707052948898271","AnthropicAI")},
 {"id":"grok-bot-data-bot","date":"2026-11-02","category":"agent launch","company":"xAI","impact":"notable",
  "headline":"xAI shows Data Bot, a shared Grok Bot that answers any employee's data questions like a data scientist",
  "explainer":"xAI's data team taught a shared Team Bot their metrics, experiment rules and chart styles, so anyone can ask it in chat or Slack to dig into numbers or build a dashboard. xAI estimates it did about 70 hours of the data team's work in one week (its own figure), and it's a how-we-use-it example you can copy with Team Bots, not a separate product.",
  "source_url":"https://x.ai/news/data-bot","source_name":"xAI",
  "x": xb("2117349540168876334","bot")},
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
