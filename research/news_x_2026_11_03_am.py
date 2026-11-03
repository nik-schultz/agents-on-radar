"""Nov 3, 2026 AM news run: 3 new items + X re-measure (research/x_news_measure_2026_11_03_am.json.txt)."""
import json
MEASURED = "2026-11-03"
raw = open("research/x_news_measure_2026_11_03_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"google-dreambeans-india","date":"2026-11-03","category":"feature","company":"Google","impact":"minor",
  "headline":"Google's Dreambeans app, which turns your Gmail, Photos and Calendar into illustrated daily stories, launches in India",
  "explainer":"If you're in India and 18+, you can now try Google's experimental Dreambeans app in English and 13 Indian languages; it reads only the Google apps you connect (Gmail, Photos, Calendar, Search, Gemini, YouTube) to make a personal daily story feed. It's its first country outside the US, it can get things wrong, and you can disconnect apps or delete your data in the app.",
  "source_url":"https://blog.google/intl/en-in/products/dreambeans-is-now-available-to-everyone-in-india/","source_name":"Google India blog",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/11/02/google-takes-dreambeans-to-india-in-bid-to-bring-ai-generated-personal-stories-to-the-masses/"},{"label":"The Hindu","url":"https://www.thehindu.com/sci-tech/technology/google-rolls-out-personal-intelligence-with-experimental-ai-app-dreambeans-in-india/article71659379.ece"}]},
 {"id":"gemini-2-5-auto-route-december","date":"2026-11-02","category":"pricing","company":"Google","impact":"notable",
  "headline":"Google retires Gemini 2.5 Pro and 2.5 Flash in its API; from Dec 1 requests are switched to newer models and billed at their rates",
  "explainer":"If a bot or app you use still calls Gemini 2.5 Pro or 2.5 Flash, it will quietly be moved on Dec 1, 2026: 2.5 Pro goes to Gemini 3.8 Flash and 2.5 Flash to Gemini 3.5 Flash-Lite, billed at those models' prices. Some features work differently on the new models, so whoever runs the bot should switch and test before then.",
  "source_url":"https://ai.google.dev/gemini-api/docs/changelog","source_name":"Gemini API changelog",
  "more_sources":[{"label":"Gemini API deprecations","url":"https://ai.google.dev/gemini-api/docs/deprecations"}]},
 {"id":"apple-watch-live-rewind-siri-recap-beta","date":"2026-11-02","category":"feature","company":"Apple","impact":"notable",
  "headline":"Apple Watch's AI that rewinds the last 15 seconds of a conversation and writes recaps of your day enters beta",
  "explainer":"On Apple Watch Series 12 and Ultra 4, Live Rewind shows the last 15 seconds of what someone said as text when you double-press the crown, and Siri Recap can take short summary notes of conversations (on a schedule you set) that delete after 7 days unless saved. It's a developer beta in English for now; Apple says no audio is recorded, but the people you talk to haven't opted in, so tell them.",
  "source_url":"https://techcrunch.com/2026/11/02/apple-watchs-ai-features-for-rewinding-and-recapping-conversations-begin-beta-testing/","source_name":"TechCrunch",
  "more_sources":[{"label":"Apple Support","url":"https://support.apple.com/en-ca/148354"},{"label":"Engadget","url":"https://www.engadget.com/2304993/apples-latest-watchos-27-beta-enables-siri-recap-and-live-rewind-audio-features/"}]},
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
