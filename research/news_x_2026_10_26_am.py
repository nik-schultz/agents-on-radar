"""Oct 26, 2026 AM news run: adds Block Dessa, OpenAI offline training, OpenAI Agents API scheduled automations,
OpenAI legacy model shutdowns, ChatGPT locked chats, Gemini API request storage default; refreshes X numbers.
Numbers: research/x_news_measure_2026_10_26_am.json.txt (get_posts_by_ids, measured 2026-10-26 ~6:30 AM CT)."""
import json
M = "2026-10-26"
raw = open("research/x_news_measure_2026_10_26_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
def xb(pid, author, posted):
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@" + author, "kind": "official", "posted_at": posted}
NEW = [
 {"id":"gemini-api-store-by-default","date":"2026-10-26","category":"feature","company":"Google","impact":"minor",
  "headline":"Gemini API now saves requests by default for new paid projects",
  "explainer":"If you set up a new paid Gemini API project, the prompts your bot sends are now stored by default, matching Google's Interactions API; existing projects don't change. If you'd rather they weren't kept, send store=false or turn off Generate Content API logging under Logs and Datasets.",
  "source_url":"https://ai.google.dev/gemini-api/docs/changelog","source_name":"Gemini API changelog"},
 {"id":"block-dessa","date":"2026-10-23","category":"model release","company":"Block","impact":"notable",
  "headline":"Block shows Dessa, a voice AI that talks with human-like pauses and emotion",
  "explainer":"Dessa is a speech model from the company behind Square and Cash App that listens and talks at the same time, so conversations with it sound strikingly like a real person. There's no public access yet, only early access for safety researchers, but it's a reminder that a lifelike voice on the phone may not be a person.",
  "source_url":"https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/","source_name":"TechCrunch",
  "more_sources":[{"label":"Block: Dessa","url":"https://block.xyz/dessa"}],
  "x": xb("2113697902916751661","jack","2026-10-23")},
 {"id":"openai-offline-training","date":"2026-10-23","category":"industry","company":"OpenAI","impact":"notable",
  "headline":"OpenAI cuts its newest models off the live internet while they're being trained",
  "explainer":"OpenAI says its frontier models now train in an offline copy of the web instead of the real internet, a safety step so a model in training can't reach outside systems. Nothing changes in ChatGPT for you, but it shows labs are treating stronger models as something to keep fenced in.",
  "source_url":"https://openai.com/index/securing-our-frontier-model-training-environment/","source_name":"OpenAI",
  "x": xb("2113718797505036665","OpenAI","2026-10-23")},
 {"id":"openai-agents-api-scheduled-automations","date":"2026-10-23","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"OpenAI's Agents API can now run bots on a schedule",
  "explainer":"Developers can now tell an OpenAI agent to run on a repeating schedule, like every morning at 10, or once at a set time, and the agent can even set up its own schedules when you ask in plain words. Expect more apps that do a recurring job for you, such as a daily digest, without you opening them.",
  "source_url":"https://developers.openai.com/api/docs/guides/agents-api/sessions/automations","source_name":"OpenAI API docs",
  "more_sources":[{"label":"OpenAI Developer Community announcement","url":"https://community.openai.com/t/introducing-scheduled-automations-to-the-agents-api/1409223"}]},
 {"id":"openai-legacy-models-shutdown-oct-23","date":"2026-10-23","category":"industry","company":"OpenAI","impact":"minor",
  "headline":"OpenAI switched off older models including GPT-4, GPT-3.5 Turbo, o4-mini and gpt-image-1",
  "explainer":"If an older app or bot of yours suddenly stopped working on Oct 23, this may be why: OpenAI retired a batch of older models announced back in April. Switching it to a current model such as GPT-5.6 usually fixes it.",
  "source_url":"https://developers.openai.com/api/docs/deprecations","source_name":"OpenAI API deprecations"},
 {"id":"chatgpt-locked-chats","date":"2026-10-20","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"ChatGPT lets you lock private chats behind a PIN",
  "explainer":"You can now lock a sensitive ChatGPT chat from its ••• menu so it's hidden from your history and search and opens only with a 4-digit PIN or your phone's face or fingerprint unlock. Write the PIN down, because resetting a forgotten one deletes every locked chat for good; it's rolling out gradually.",
  "source_url":"https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/","source_name":"TechCrunch",
  "more_sources":[{"label":"OpenAI Help Center: Using locked chats","url":"https://help.openai.com/en/articles/20001411-using-locked-chats-in-chatgpt"}]},
]
for n in NEW:
    assert n["id"] not in byid, n["id"]
    data["items"].append(n); byid[n["id"]] = n
n_ref = 0
for x in data["items"]:
    b = x.get("x")
    if not b: continue
    pid = b["url"].rstrip("/").rsplit("/",1)[1]
    if pid in posts:
        m = posts[pid]["public_metrics"]
        b.update({"likes":m["like_count"],"reposts":m.get("repost_count", m.get("retweet_count")),"views":m["impression_count"],"measured_at":M})
        n_ref += 1
order = ["id","date","category","company","impact","headline","explainer","source_url","source_name","more_sources","x"]
data["items"] = [{k: x[k] for k in order if k in x} | {k: v for k, v in x.items() if k not in order} for x in data["items"]]
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n_ref)
