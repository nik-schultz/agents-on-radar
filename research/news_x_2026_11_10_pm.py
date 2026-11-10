"""Nov 10, 2026 PM news run: add 8 items, refresh X numbers (raw: research/x_news_measure_2026_11_10_pm.json.txt)."""
import json, re
raw = open("research/x_news_measure_2026_11_10_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-10T20:32:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"gemini-4-carbon-available","date":"2026-11-10","category":"model release","company":"Google","impact":"major",
  "headline":"Google's top model, Gemini 4 Carbon, is now open to paying developers and Google AI Ultra subscribers",
  "explainer":"Carbon is Google's strongest model for long, multi-step jobs like big coding projects, research and security work, and it's now in the Gemini API for every paying developer at $2 in / $10 out per million tokens until Nov 30 ($4 / $20 from Dec 1), plus the Gemini app, AI Mode and Antigravity for Ultra subscribers. It uses more tokens than Gemini 4 Argon to think things through, so Google still points most everyday work to Argon; Antigravity also gets a /swarm preview that turns one prompt into a team of agents.",
  "source_url":"https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/","source_name":"Google blog",
  "more_sources":[{"label":"Gemini API pricing","url":"https://ai.google.dev/gemini-api/docs/pricing"}],
  "x": xblock("2120185896469496180","sundarpichai","official")},
 {"id":"claude-sheets-whiteboards-data","date":"2026-11-10","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude can now build spreadsheets and whiteboards with you, and open apps like Notion or Adobe right beside the chat",
  "explainer":"Ask for a budget or a tracker and Claude makes a real sheet with tabs, formulas and drop-downs you can edit together and export to Excel or CSV; Whiteboards turns a messy plan into a board with owners and dates (both beta on paid plans), and Claude Data (formerly Dashboards) is now generally available. Anthropic also announced Claude Meetings, which joins Google Meet calls as a visible participant for Team and Enterprise plans, and connected apps can now open full-size so Claude can make changes in them while you approve each action.",
  "source_url":"https://claude.com/resources/articles/sheets-whiteboards-data","source_name":"Claude",
  "more_sources":[{"label":"Claude: interactive connectors","url":"https://claude.com/resources/articles/interactive-connectors-full-tool"},
                  {"label":"TechCrunch","url":"https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/"},
                  {"label":"Fortune","url":"https://fortune.com/2026/11/10/anthropic-launches-office-knowledge-worker-product-launch-ahead-of-ipo/"}],
  "x": xblock("2120206365759094857","claudeai","official")},
 {"id":"chatgpt-businesses-business-agents","date":"2026-11-10","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"Businesses can now claim a profile in ChatGPT, and some US shops can add their own chat agent",
  "explainer":"When ChatGPT mentions a business you may now see its verified profile and, for eligible US online stores and services, a clearly labeled Business Agent you can ask about products. That agent speaks for the business, not for you, and some can be sponsored placements, so double-check claims; OpenAI says businesses don't see your chats, only aggregated numbers.",
  "source_url":"https://openai.com/index/introducing-businesses-chatgpt","source_name":"OpenAI",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/"},
                  {"label":"Reuters (via Investing.com)","url":"https://www.investing.com/news/stock-market-news/openai-lets-businesses-claim-chatgpt-profiles-adds-ai-agents-for-us-ecommerce-firms-5016475"}],
  "x": xblock("2120216592395174382","OpenAI","official")},
 {"id":"n8n-nod-personal-agent","date":"2026-11-10","category":"agent launch","company":"n8n","impact":"notable",
  "headline":"n8n releases Nod, a free open-source agent that runs errands on your own Mac or Windows PC",
  "explainer":"Nod works in its own sandbox and browser on your computer, so it can cancel a subscription, watch a price or download monthly invoices, and it checks with you before it sends, pays, posts or deletes anything. It's a research preview: you bring your own AI provider (API key or ChatGPT plan) and pay for that usage, it asks once a task passes $5, and it stops when your laptop sleeps.",
  "source_url":"https://blog.n8n.io/meet-nod/","source_name":"n8n blog",
  "more_sources":[{"label":"Nod on GitHub","url":"https://github.com/n8n-io/nod"}]},
 {"id":"adobe-max-creative-agent-mcp","date":"2026-11-10","category":"agent launch","company":"Adobe","impact":"notable",
  "headline":"Adobe puts its Creative Agent across Firefly and Creative Cloud and previews a way for outside agents to edit your Photoshop files",
  "explainer":"You can describe a multi-step edit in Firefly, Premiere, Illustrator or InDesign and the assistant (beta) does it, and new always-on agents (preview) can sort incoming files or prep content in the background. A local MCP preview will let agents like Claude or ChatGPT make changes inside your Photoshop, Illustrator, Premiere and After Effects files while keeping layers editable; 9to5Mac reports that part arrives in 2027.",
  "source_url":"https://news.adobe.com/news/2026/11/adobe-powers-new-era-of-creativity","source_name":"Adobe",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/"},
                  {"label":"The Verge","url":"https://www.theverge.com/tech/1030593/adobe-max-ai-agents-mcp-firefly-assistant-updates"},
                  {"label":"9to5Mac","url":"https://9to5mac.com/2026/11/10/adobe-unveils-new-ai-tools-for-photoshop-premiere-and-more-with-mcp-support-coming-in-2027/"}]},
 {"id":"ebay-blocks-ai-agents","date":"2026-11-10","category":"industry","company":"eBay","impact":"notable",
  "headline":"eBay appears to be blocking AI agents like Meta's Muse from browsing its listings",
  "explainer":"If your bot used to pull eBay deals into a daily digest, it may now come back empty or send you to copycat sites; eBay says it restricts agent access in some cases and already banned agents that buy without a person reviewing the order. Amazon also blocks outside agents, so check the store's own app or alerts when your bot hits a wall.",
  "source_url":"https://www.theverge.com/tech/1030838/ebay-ai-agents-meta-muse-agentic-shopping","source_name":"The Verge"},
 {"id":"notion-ai-chats-fireworks-breach","date":"2026-11-09","category":"industry","company":"Notion","impact":"notable",
  "headline":"A breach at AI vendor Fireworks exposed some Notion AI chat transcripts",
  "explainer":"Fewer than 1% of Notion workspaces were affected and most chats had no names attached, but Notion says to treat them as exposed and change any password or API key you pasted into Notion AI. It's a reminder that what you type into an AI tool can pass through other companies, so keep secrets out of chats.",
  "source_url":"https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor","source_name":"Notion",
  "more_sources":[{"label":"The Hacker News","url":"https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html"}],
  "x": xblock("2120224129471361452","TheHackersNews","coverage")},
 {"id":"apple-intelligence-usage-packs","date":"2026-11-09","category":"pricing","company":"Apple","impact":"notable",
  "headline":"Apple starts selling $49.99 packs of extra AI use, starting in Logic Pro",
  "explainer":"It's Apple's first charge for extra Apple Intelligence use: Creator Studio subscribers who hit the monthly limit on features like the Logic Pro assistant can buy a one-time pack that rolls over and expires after 12 months. It isn't shareable with family or refundable, so check Show Usage before buying; Apple Intelligence on your phone is still free.",
  "source_url":"https://support.apple.com/en-us/127888","source_name":"Apple Support",
  "more_sources":[{"label":"9to5Mac","url":"https://9to5mac.com/2026/11/09/apple-launches-50-intelligence-usage-packs-for-select-ai-features/"},
                  {"label":"The Verge","url":"https://www.theverge.com/tech/1030084/apple-intelligence-usage-packs-ai-features-creator-studio-logic-pro"}],
  "x": xblock("2119830429448503579","9to5mac","coverage")},
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
