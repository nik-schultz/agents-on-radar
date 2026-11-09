"""Nov 9, 2026 AM news run: new items + X re-measure (research/x_news_measure_2026_11_09_am.json.txt)."""
import json
MEASURED = open("/tmp/measured").read().strip()
raw = open("research/x_news_measure_2026_11_09_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
def xb(pid, author, kind="official"):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count")), "views": m["impression_count"],
            "posted_at": p["created_at"][:10], "measured_at": MEASURED}
NEW = [
 {"id":"chatgpt-dots-sign-in-codes","date":"2026-11-07","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"Your ChatGPT dot can now read sign-in codes from your inbox and log in for you",
  "explainer":"When a website emails a one-time sign-in code, your dot (ChatGPT's always-on agent) can now pull it from your connected inbox and finish the login, and you choose whether it may do that once or every time. Only allow it for accounts you're happy for the agent to enter, and still check that the task it logged in for actually got done.",
  "source_url":"https://x.com/JamesZmSun/status/2119147164039618879","source_name":"James Sun (OpenAI) on X",
  "more_sources":[{"label":"ByteForward","url":"https://bytefwd.com/openai-dots-connected-apps-availability/"}],
  "x": xb("2119147164039618879","JamesZmSun")},
 {"id":"meta-muse-spaces","date":"2026-11-06","category":"feature","company":"Meta","impact":"notable",
  "headline":"Meta's Muse can now build you a custom 'space' like a planner, tracker or game",
  "explainer":"Describe what you want (a gift tracker, wedding planner, school-events dashboard or trip planner) and Muse builds it as a space inside the app that you can pin to your tabs and keep editing. If you connect apps like Gmail, Calendar or OpenTable, a space updates itself in the background; it's available everywhere Muse is.",
  "source_url":"https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/","source_name":"Meta Newsroom",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/"},{"label":"The Verge","url":"https://www.theverge.com/tech/1028871/meta-muse-ai-spaces"}],
  "x": xb("2118782474486501510","Muse")},
 {"id":"anthropic-agent-memory-dreaming","date":"2026-11-06","category":"industry","company":"Anthropic","impact":"notable",
  "headline":"Anthropic explains how 'dreaming' helps Claude fix and organize its memory between sessions",
  "explainer":"Anthropic shows how Claude can go back over its own past work while idle to correct wrong notes, merge duplicates and build a wiki of what it knows, so a long-running agent repeats fewer mistakes. It's an engineering explainer, not a new button, but it's a good model for any bot you run: have it review and tidy its notes regularly.",
  "source_url":"https://www.anthropic.com/research/components-of-agent-memory","source_name":"Anthropic",
  "x": xb("2118814753154064501","AnthropicAI")},
 {"id":"claude-code-cloud-auto-setup","date":"2026-11-06","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude Code cloud sessions now set up your project on their own",
  "explainer":"On Pro, Max and Ultra plans, Claude works out which packages, network access and API keys a project needs in a cloud session and saves that setup for next time. Keys are stored as secrets that Claude never sees, so you no longer have to write a setup script before a cloud coding agent can start.",
  "source_url":"https://x.com/ClaudeDevs/status/2118795192090386454","source_name":"Claude Devs on X",
  "more_sources":[{"label":"Claude Code docs: cloud environments","url":"https://code.claude.com/docs/en/cloud-environments"}],
  "x": xb("2118795192090386454","ClaudeDevs")},
 {"id":"chatgpt-sites-remix","date":"2026-11-06","category":"feature","company":"OpenAI","impact":"minor",
  "headline":"ChatGPT Remix lets work teams copy a teammate's Site and make their own version",
  "explainer":"In ChatGPT Business and Enterprise, you can now take a Site a colleague built, tell ChatGPT what to change, and keep editing your own copy while the original stays untouched. It's rolling out to work accounts only, not personal plans.",
  "source_url":"https://x.com/ChatGPT/status/2118827837239226387","source_name":"ChatGPT on X",
  "more_sources":[{"label":"RuntimeWire","url":"https://runtimewire.com/article/openai-chatgpt-remix-sites-business-enterprise"}],
  "x": xb("2118827837239226387","ChatGPT")},
 {"id":"opencode-browse","date":"2026-11-06","category":"agent launch","company":"OpenCode","impact":"notable",
  "headline":"OpenCode Browse lets AI agents use your real browser, logins included",
  "explainer":"A free Chrome extension plus MCP server lets agents like OpenCode, Claude Code, Cursor or Codex open background tabs in your own browser and use the sites you're already signed into. It hands the tab back to you for logins, 2FA and payments, and you can limit a session to sites you name; that's worth doing, because it acts as you.",
  "source_url":"https://opencode.ai/product/browse","source_name":"OpenCode",
  "more_sources":[{"label":"Chrome Web Store","url":"https://chromewebstore.google.com/detail/browse/mfnicocicmmlkpjnaffgihfjhdgjkdjg"}],
  "x": xb("2118895128152621153","opencode")},
 {"id":"baidu-ernie-5-5-flash-base","date":"2026-11-05","category":"model release","company":"Baidu","impact":"minor",
  "headline":"Baidu posts free download of its ERNIE 5.5 Flash base model for developers to train",
  "explainer":"Baidu released the raw (not chat-tuned) weights of ERNIE 5.5 Flash, a 280-billion-parameter model that uses 14 billion per word, so developers can fine-tune their own assistants on it. It's a building block rather than an app you can chat with, and its license excludes the EU, UK and South Korea.",
  "source_url":"https://huggingface.co/baidu/ERNIE-5.5-Flash-Base","source_name":"Hugging Face (Baidu)",
  "more_sources":[{"label":"ERNIE release page","url":"https://ernie.baidu.com/release/ernie-5-5-flash-base/"}],
  "x": xb("2118288752749543531","ivanfioravanti","coverage")},
]
p = "data/news.json"; data = json.load(open(p))
have = {x["id"] for x in data["items"]}
n = 0
for x in data["items"]:
    if x["id"] == "meta-muse-specialized-models":
        x["x"] = xb("2118767522782626104","finkd")  # Zuckerberg's post is the most-engaged announcement
        x.setdefault("more_sources",[])
        if not any(s["url"].startswith("https://x.com/AIatMeta") for s in x["more_sources"]):
            x["more_sources"].append({"label":"AI at Meta on X","url":"https://x.com/AIatMeta/status/2118768974779634084"})
        n += 1; continue
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
