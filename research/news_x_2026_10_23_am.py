"""Oct 23, 2026 AM news run: adds Claude auto mode default in apps, Grok Bot phone apps, Grok Bot + 1Password,
Gemini Maps saved places; refreshes X numbers.
Numbers: research/x_news_measure_2026_10_23_am.json.txt (get_posts_by_ids, measured 2026-10-23 ~6:35 AM CT)."""
import json
M = "2026-10-23"
raw = open("research/x_news_measure_2026_10_23_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
p = "data/news.json"; data = json.load(open(p))
byid = {x["id"]: x for x in data["items"]}
def xb(pid, author, posted):
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@" + author, "kind": "official", "posted_at": posted}
NEW = [
 {"id":"claude-auto-mode-default-apps","date":"2026-10-22","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude will stop asking permission for every step, starting next week",
  "explainer":"Starting next week, Claude's web, desktop and mobile apps on Pro, Max and Team plans begin sessions in auto mode, where an automated check lets safe actions go ahead and blocks risky ones instead of asking you to approve each step. Longer tasks finish with fewer interruptions, and you can switch any session back to manual approvals.",
  "source_url":"https://claude.com/resources/articles/auto-mode-default-in-claude-code","source_name":"Anthropic",
  "x": xb("2113360845409583307","claudeai","2026-10-22")},
 {"id":"grok-bot-phone-apps","date":"2026-10-22","category":"feature","company":"xAI","impact":"notable",
  "headline":"Grok Bot can now use your phone's Calendar, Reminders and Contacts",
  "explainer":"With your permission, Grok Bot on iOS and Android can add calendar events, set and check reminders, look up contacts and reach apps like Messages and Home, and you allow each app separately. That makes \"add this to my calendar\" or \"remind me tonight\" something you can just ask your bot to do; it's rolling out now.",
  "source_url":"https://www.digitaltrends.com/phones/grok-bot-can-now-manage-your-calendar-reminders-and-more/","source_name":"Digital Trends",
  "more_sources":[{"label":"TeslaNorth","url":"https://teslanorth.com/2026/10/22/grok-bot-phone-calendar-reminders-contacts/"}],
  "x": xb("2113393684209176718","bot","2026-10-22")},
 {"id":"grok-bot-1password","date":"2026-10-22","category":"feature","company":"xAI","impact":"notable",
  "headline":"Grok Bot can sign in to your accounts with 1Password, without seeing your passwords",
  "explainer":"You approve which saved logins your bot may use, and 1Password fills them in, one-time codes included, so the bot never sees the password. 1Password says the same approach is rolling out for Meta's Muse and coming soon to Claude Duet and ChatGPT Work, at no extra cost on its Individual and Family plans.",
  "source_url":"https://1password.com/partners/spacexsi-grokbot","source_name":"1Password",
  "more_sources":[{"label":"1Password blog: 1Password for Agents","url":"https://1password.com/blog/1password-for-ai-agents"}],
  "x": xb("2113332983226831339","bot","2026-10-22")},
 {"id":"gemini-maps-saved-places","date":"2026-10-22","category":"feature","company":"Google","impact":"notable",
  "headline":"Gemini can now plan your day from your Google Maps saved places and calendar",
  "explainer":"If you turn on Personal Intelligence, Gemini can check your Maps searches and saved places alongside your Calendar, so \"which restaurant on my list is near my last meeting?\" gets a real answer. Google is also telling AI Ultra subscribers that Gemini 4 Argon will soon replace the Deep Think mode.",
  "source_url":"https://9to5google.com/2026/10/22/gemini-personal-intelligence-maps/","source_name":"9to5Google",
  "x": xb("2113343041805127839","GeminiApp","2026-10-22")},
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
