"""Nov 12, 2026 AM news run: add 4 items, refresh X numbers (raw: research/x_news_measure_2026_11_12_am.json.txt, local only)."""
import json, re
raw = open("research/x_news_measure_2026_11_12_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-12T12:35:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"openai-india-api-local-processing","date":"2026-11-12","category":"feature","company":"OpenAI","impact":"minor",
  "headline":"OpenAI's API can now process requests inside India, starting with GPT-6 Luna",
  "explainer":"Eligible businesses can pick India for both storage and processing in a new API project, so the request and the AI's answer are handled in the country. It's a business setting that needs Zero Data Retention and pay-as-you-go billing, so nothing changes for everyday ChatGPT users.",
  "source_url":"https://www.thehindu.com/business/openai-now-allows-enterprises-to-process-ai-requests-within-india/article71692799.ece","source_name":"The Hindu",
  "more_sources":[{"label":"The Economic Times","url":"https://economictimes.indiatimes.com/ai/ai-insights/openai-brings-local-inference-to-india-starting-with-gpt-6-luna/articleshow/135760461.cms"}]},
 {"id":"united-blocks-ai-agent-bookings","date":"2026-11-11","category":"industry","company":"United","impact":"notable",
  "headline":"United Airlines won't let personal AI agents book its flights",
  "explainer":"Agents like Meta's Muse or ChatGPT's dots can still find and compare United fares, but you'll have to finish the booking yourself on United's site or app. United cites privacy, purchases you didn't mean to make, and federal rules such as travelers confirming their bags carry no explosives, so tell your travel bot to stop at the checkout page.",
  "source_url":"https://www.theverge.com/ai-artificial-intelligence/1031623/united-unauthorized-ai-agents","source_name":"The Verge",
  "x": xblock("2120580158717600222","Complex","coverage")},
 {"id":"gemini-live-carplay","date":"2026-11-11","category":"feature","company":"Google","impact":"notable",
  "headline":"Gemini Live now works on Apple CarPlay, so iPhone drivers can talk through email and calendar hands-free",
  "explainer":"Tap the Gemini icon on the car screen to get a daily brief, hear summaries of unread emails, talk through a reply, or rehearse a pitch out loud, and the chat syncs back to your iPhone when you park. It's rolling out worldwide to all Gemini users on iOS; the Daily Brief isn't available to under-18s or in the EEA and Nigeria.",
  "source_url":"https://blog.google/innovation-and-ai/products/gemini-app/gemini-on-apple-carplay/","source_name":"Google blog",
  "x": xblock("2120626195033473228","GeminiApp","official")},
 {"id":"chatgpt-finances-desktop","date":"2026-11-11","category":"feature","company":"OpenAI","impact":"minor",
  "headline":"ChatGPT Finances, the money dashboard for your linked bank accounts, arrives in the desktop app",
  "explainer":"US users on Free, Go, Plus and Pro can now open Finances in the Mac app's sidebar to see spending, bills, subscriptions and investments and ask questions about them. It reads your accounts through Plaid (and your credit report through Experian if you choose) but can't move money, pay bills or make trades.",
  "source_url":"https://9to5mac.com/2026/11/11/openais-personal-finance-features-for-chatgpt-expands-to-mac-app/","source_name":"9to5Mac",
  "more_sources":[{"label":"OpenAI Help Center","url":"https://help.openai.com/en/articles/20001222-finances-in-chatgpt"}],
  "x": xblock("2120604108893896965","ChatGPT","official")},
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
