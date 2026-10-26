"""Oct 26, 2026 PM news run: adds GPT-6.1 Terra, Anthropic S-1 filing, Claude for Nonprofits plugin,
Claude Enterprise chat+Cowork merge, Gemini Notebook connected app, Walmart Agent Gateway; adds gpt-6.1-terra to pricing.
Numbers: research/x_news_measure_2026_10_26_pm.json.txt (get_posts_by_ids, measured 2026-10-26 ~2:40 PM CT)."""
import json
M = "2026-10-26"
raw = open("research/x_news_measure_2026_10_26_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
def xb(pid, author):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@" + author, "kind": "official",
            "posted_at": p["created_at"][:10], "likes": m["like_count"], "reposts": m["repost_count"],
            "views": m["impression_count"], "measured_at": M}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
NEW = [
 {"id":"openai-gpt-6-1-terra","date":"2026-10-26","category":"model release","company":"OpenAI","impact":"notable",
  "headline":"GPT-6.1 Terra: OpenAI's new fast, cheaper model for bots that use apps and screens",
  "explainer":"GPT-6.1 Terra is a new mid-size OpenAI model that's better at reading what's on a screen and clicking through apps for you, like filling out forms or entering invoices, and makes fewer factual mistakes than GPT-5.6 Terra. It's in ChatGPT Work, Codex and the API at $1 in / $5 out per million tokens, half the price of GPT-6.1 Sol, so bots that do lots of computer work get cheaper to run; the benchmark claims are OpenAI's own.",
  "source_url":"https://developers.openai.com/api/docs/changelog","source_name":"OpenAI API changelog",
  "more_sources":[{"label":"OpenAI: Introducing GPT-6.1 Terra","url":"https://openai.com/index/introducing-gpt-6-1-terra"},
                  {"label":"AWS: GPT-6.1 Terra on Amazon Bedrock","url":"https://aws.amazon.com/about-aws/whats-new/2026/10/openai-gpt-6-1-terra-on-amazon-bedrock/"}],
  "x": xb("2114780711664398349","OpenAI")},
 {"id":"anthropic-s1-ipo-filing","date":"2026-10-26","category":"industry","company":"Anthropic","impact":"notable",
  "headline":"Anthropic, the maker of Claude, files to go public on Nasdaq",
  "explainer":"Anthropic has filed the paperwork with the SEC for a stock market listing under the symbol ANT; the share count and price aren't set yet. Nothing changes in Claude for you today, but a public Anthropic will have to report its business openly, which can shape pricing and plans down the road.",
  "source_url":"https://www.anthropic.com/news/s1-sec","source_name":"Anthropic",
  "x": xb("2114705042817110293","AnthropicAI")},
 {"id":"claude-for-nonprofits-plugin","date":"2026-10-26","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude gets a free plugin for nonprofits that helps with fundraising, marketing and hiring",
  "explainer":"Verified nonprofits using Claude now get a plugin, built with about 30 nonprofits, with ready-made skills for grant research, donor reports, marketing and hiring that follow the group's own policies. If you volunteer for or run a small nonprofit, it's a quicker way to get Claude doing the paperwork that eats your week.",
  "source_url":"https://claude.com/resources/articles/expanding-claude-for-nonprofits","source_name":"Claude",
  "x": xb("2114780227465338985","claudeai")},
 {"id":"claude-enterprise-chat-cowork-merge","date":"2026-10-23","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude Enterprise merges chat and Cowork into one Claude that keeps working in the cloud",
  "explainer":"At companies on Claude Enterprise, people no longer pick between a quick chat and handing Claude a bigger job: every conversation starts as a chat and moves into the cloud when it needs to work with files or code, then hands back the finished document or deck. The work keeps going after you close your laptop, and admins get controls and a new Efficient mode to manage usage.",
  "source_url":"https://claude.com/resources/articles/unified-claude-enterprise","source_name":"Claude"},
 {"id":"gemini-notebook-connected-app","date":"2026-10-23","category":"feature","company":"Google","impact":"notable",
  "headline":"Gemini can now create notebooks and add sources to Gemini Notebook from your chat",
  "explainer":"Type @Gemini Notebook in a Gemini chat to make a notebook, add a link or this chat as a source, or ask what your notebooks say, without switching apps. It's on by default for personal and Workspace accounts outside Europe, so double-check before asking it to delete anything, since it can change your notebooks too.",
  "source_url":"https://workspaceupdates.googleblog.com/2026/10/take-actions-on-your-notebooks-from-Gemini-Notebook-directly-in-the-Gemini-app.html","source_name":"Google Workspace Updates",
  "more_sources":[{"label":"9to5Google: Gemini Notebook now a Connected App","url":"https://9to5google.com/2026/10/23/gemini-notebook-connected-app/"}]},
 {"id":"walmart-agent-gateway","date":"2026-10-21","category":"agent launch","company":"Walmart","impact":"notable",
  "headline":"Walmart opens its store to AI shopping agents, with spending limits you set",
  "explainer":"Walmart is building a direct connection so approved AI agents like ChatGPT, Gemini and Muse can search and buy from Walmart and Sam's Club for you, starting with an invite-only beta for developers. Next month, each agent gets its own profile in your Walmart account where you can require approval for every order or set a spending cap, and agents never see your card details.",
  "source_url":"https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers","source_name":"Walmart",
  "more_sources":[{"label":"TechCrunch: While Amazon blocks AI agents, Walmart rolls out the welcome mat","url":"https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/"},
                  {"label":"Retail Dive: Walmart welcomes external AI agents","url":"https://www.retaildive.com/news/walmart-welcomes-external-ai-shopping-agents-terms-boundaries/833723/"}]},
]
for n in NEW:
    assert n["id"] not in byid, n["id"]
    data["items"].append(n)
order = ["id","date","category","company","impact","headline","explainer","source_url","source_name","more_sources","x"]
data["items"] = [{k: x[k] for k in order if k in x} | {k: v for k, v in x.items() if k not in order} for x in data["items"]]
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
# pricing
pp = "data/ai-pricing.json"; pr = json.load(open(pp))
assert not any(r["model"]=="gpt-6.1-terra" for r in pr["api"])
i = next(k for k,r in enumerate(pr["api"]) if r["model"]=="gpt-6.1-sol")
pr["api"].insert(i+1, {"provider":"OpenAI","model":"gpt-6.1-terra","tier":"mid","input":1.0,"output":5.0,"cached_input":0.05,
  "note":"New Oct 26, 2026. Short context (\u2264272K input tokens).","source_url":"https://platform.openai.com/docs/pricing","checked_on":M})
json.dump(pr, open(pp,"w"), indent=1, ensure_ascii=False); open(pp,"a").write("\n")
print("ok", len(data["items"]))
