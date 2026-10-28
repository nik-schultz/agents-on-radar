"""Oct 28, 2026 AM news run: 4 new items + X re-measure (research/x_news_measure_2026_10_28_am.json.txt)."""
import json
MEASURED = "2026-10-28"
raw = open("research/x_news_measure_2026_10_28_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"apple-iwork-assistant-mcp","date":"2026-10-27","category":"feature","company":"Apple","impact":"notable",
  "headline":"Apple puts an AI assistant in Pages, Keynote and Numbers, and opens them to outside agents",
  "explainer":"Your bot will be able to read and edit Pages, Keynote and Numbers files on a Mac. Apple's new assistant (built on Apple models and OpenAI) drafts text, builds slides and charts data, and new MCP support lets outside AI agents work in the apps directly; it arrives in November for Apple Creator Studio subscribers ($12.99/month), in beta, US English only, and MCP needs macOS 27.",
  "source_url":"https://www.apple.com/newsroom/2026/10/apple-creator-studio-adds-powerful-new-ai-features-and-even-more-creative-tools/","source_name":"Apple Newsroom",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/tech/1019373/apple-pages-keynote-numbers-ai-chatbot-update"}],
  "_x":("2115131652259434648","coverage")},
 {"id":"meta-muse-singapore","date":"2026-10-27","category":"agent launch","company":"Meta","impact":"notable",
  "headline":"Meta's Muse personal agent launches in Singapore, its first country after the US",
  "explainer":"Muse, Meta's do-it-for-you agent, now works in Singapore with local apps like Grab, Shopee and Singapore Airlines. It's free for most tasks, keeps your passwords and cards out of the agent's view, and asks before sending an email or buying anything.",
  "source_url":"https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/","source_name":"Meta",
  "more_sources":[{"label":"CNA","url":"https://www.channelnewsasia.com/singapore/meta-muse-ai-agent-singapore-shopping-travel-email-connectors-6499331"}],
  "_x":("2115252079593967826","official")},
 {"id":"openai-oracle-apps-chatgpt","date":"2026-10-27","category":"industry","company":"OpenAI","impact":"notable",
  "headline":"OpenAI and Oracle plan to bring Oracle business apps into ChatGPT",
  "explainer":"If your job runs on Oracle software, you may soon handle approved tasks like finance or HR lookups by asking ChatGPT. Oracle AI Workspace is still in development with no launch date; what's live now is that US Oracle customers can buy ChatGPT Work, Codex and the OpenAI API through Oracle Marketplace.",
  "source_url":"https://openai.com/index/oracle-apps-in-chatgpt","source_name":"OpenAI",
  "more_sources":[{"label":"Oracle blog","url":"https://blogs.oracle.com/ai-and-datascience/introducing-oracle-ai-workspace"},{"label":"CNBC","url":"https://www.cnbc.com/2026/10/27/oracle-openai-chatgpt-codex-google-tpus.html"}]},
 {"id":"anthropic-gsa-40-discount","date":"2026-10-27","category":"pricing","company":"Anthropic","impact":"minor",
  "headline":"Anthropic gives US federal, state and local governments 40% off Claude",
  "explainer":"Government offices can now buy Claude Enterprise, Claude for Government and the Claude API at 40% off with no minimum spend. Prices for everyone else don't change, but your city or state may start using Claude for forms and backlogs.",
  "source_url":"https://www.anthropic.com/news/expanding-partnership-gsa","source_name":"Anthropic",
  "more_sources":[{"label":"GSA","url":"https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-anthropic-reach-onegov-agreement-on-discounted-consumptionbased-pricing-10272026"}]},
]
p = "data/news.json"; data = json.load(open(p))
have = {x["id"] for x in data["items"]}
def xblock(pid, kind):
    q = posts[pid]; m = q["public_metrics"]
    return {"url": q["url"], "author": "@" + users[q["author_id"]], "kind": kind, "likes": m["like_count"],
            "reposts": m.get("repost_count", m.get("retweet_count")), "views": m.get("impression_count"), "posted_at": q["created_at"].replace(".000Z","Z"), "measured_at": MEASURED}
n = 0
for x in data["items"]:
    if x.get("x"):
        pid = x["x"]["url"].rsplit("/",1)[1]
        if pid in posts:
            q = posts[pid]; m = q["public_metrics"]
            x["x"].update(likes=m["like_count"], reposts=m.get("repost_count", m.get("retweet_count")), views=m.get("impression_count"), measured_at=MEASURED); n += 1
for it in NEW:
    if it["id"] in have: continue
    xs = it.pop("_x", None)
    if xs: it["x"] = xblock(*xs)
    data["items"].append(it)
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n)
