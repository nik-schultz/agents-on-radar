"""Oct 29, 2026 PM news run: 8 new items + X re-measure (research/x_news_measure_2026_10_29_pm.json.txt)."""
import json
MEASURED = "2026-10-29"
raw = open("research/x_news_measure_2026_10_29_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"mistral-large-4-open-weights","date":"2026-10-29","category":"model release","company":"Mistral","impact":"notable",
  "headline":"Mistral releases the weights of Mistral Large 4 ('Le Chonk'), now the strongest open model for coding",
  "explainer":"Anyone can now download Mistral's biggest model and run it on their own servers, so private, self-hosted bots get a lot more capable. Mistral says it's the best open-weight model for coding and defensive security; on its API it now costs $0.70 in / $2.10 out per million tokens, and it's also on OpenRouter and Microsoft Foundry.",
  "source_url":"https://mistral.ai/news/mistral-large-4-oss/","source_name":"Mistral",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/"},{"label":"Hugging Face model card","url":"https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B"}],
  "_x":("2115811242556137820","official")},
 {"id":"claude-mobile-carplay-multi-account","date":"2026-10-29","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude's phone apps add CarPlay voice chats, account switching and a faster voice mode",
  "explainer":"You can now talk to Claude hands-free through Apple CarPlay (open it from the car screen first) and stay signed in to a personal and a work account at once. Voice mode answers faster, copes better with noisy rooms and now speaks 33 languages; on iPad, what Claude makes opens beside the chat.",
  "source_url":"https://x.com/claudeai/status/2115859377488072879","source_name":"Claude on X",
  "more_sources":[{"label":"Crypto Briefing","url":"https://cryptobriefing.com/claude-mobile-apps-multitasking-carplay-update/"}],
  "_x":("2115859377488072879","official")},
 {"id":"gemini-edit-files-in-chat","date":"2026-10-29","category":"feature","company":"Google","impact":"notable",
  "headline":"Gemini can now make and edit documents, PDFs, slides and spreadsheets right in the chat",
  "explainer":"Ask Gemini for a file, like a PDF study guide from photos of your handwritten notes, then type your own edits or highlight a part and ask Gemini to change it. It's free for all users; PDFs work on web and mobile, other formats on the web only.",
  "source_url":"https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/","source_name":"Google blog",
  "_x":("2115845164824711247","official")},
 {"id":"amazon-alexa-for-shopping-100-actions","date":"2026-10-29","category":"feature","company":"Amazon","impact":"notable",
  "headline":"Alexa for Shopping can now handle 100+ Amazon chores, from skipping deliveries to tracking refunds",
  "explainer":"In the Amazon app or website you can just ask Alexa to edit lists and registries, skip or pause Subscribe & Save, change delivery instructions, check Prime benefits or chase a refund. It's live for all US Amazon customers; check what it changed on your account, especially billing.",
  "source_url":"https://www.aboutamazon.com/news/retail/alexa-for-shopping-new-capabilities","source_name":"Amazon",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/10/29/amazon-updates-alexa-to-help-you-manage-shopping-lists-subscriptions-and-update-delivery-instructions/"}],
  "_x":("2115829760261546108","official")},
 {"id":"openai-model-spec-five-values","date":"2026-10-29","category":"industry","company":"OpenAI","impact":"notable",
  "headline":"OpenAI rewrites its rulebook for how ChatGPT should behave around five core values",
  "explainer":"OpenAI's updated Model Spec tells its models to follow what you actually mean, avoid harm, be honest about what they did and don't know, respect your choices and show care. It also adds guidance for agents acting on your behalf and changes some default behaviors, so ChatGPT may answer a bit differently over time.",
  "source_url":"https://openai.com/index/updated-model-spec","source_name":"OpenAI",
  "more_sources":[{"label":"Model Spec (2026/10/29)","url":"https://model-spec.openai.com/2026-10-29.html"},{"label":"Reuters via StreetInsider","url":"https://www.streetinsider.com/Reuters/OpenAI+says+human+intent+at+center+of+updated+AI+model+guidelines/27256894.html"}]},
 {"id":"granola-voice-typing","date":"2026-10-29","category":"feature","company":"Granola","impact":"minor",
  "headline":"Granola, the meeting-notes app, now types for you by voice in any app, free",
  "explainer":"On a Mac, hold the Fn key and talk; Granola cleans up your words and types them into email, chats or AI prompts, with unlimited words for free. iOS and Windows are coming soon.",
  "source_url":"https://techcrunch.com/2026/10/29/granola-crunches-up-a-dictation-feature-to-compete-with-wispr/","source_name":"TechCrunch",
  "_x":("2115837013975081208","official")},
 {"id":"gemini-shared-avatars","date":"2026-10-29","category":"feature","company":"Google","impact":"minor",
  "headline":"Gemini lets you share your avatar so friends can put you in AI images and videos",
  "explainer":"Create an avatar of yourself in Gemini, share it with a friend's Gmail address, and they can tag you with @ in prompts to make pictures and videos of you together. You choose who can use it and can take access away at any time.",
  "source_url":"https://x.com/GeminiApp/status/2115885244805251519","source_name":"Gemini on X",
  "more_sources":[{"label":"Gemini Apps Help: avatars","url":"https://support.google.com/gemini/answer/16984474"}],
  "_x":("2115885244805251519","official")},
 {"id":"grok-bot-shopping-subscriptions","date":"2026-10-27","category":"feature","company":"xAI","impact":"notable",
  "headline":"Grok Bot can now buy things you approve, track the order and cancel subscriptions you don't use",
  "explainer":"Grok Bot 0.78.1 shows shopping results as product cards with a Buy now button that still waits for your OK, then tracks the package. New templates start a free trial and cancel it before it bills, find unused subscriptions and watch renewal prices, and the Bot confirms with you before changing anything.",
  "source_url":"https://x.ai/changelog/bot","source_name":"Grok Bot changelog",
  "more_sources":[{"label":"The Tech Signal","url":"https://thetechsignal.co/2026/10/29/grok-bot-0-78-shopping-subscriptions/"}],
  "_x":("2115586309096083730","official")},
]
p = "data/news.json"; data = json.load(open(p))
have = {x["id"] for x in data["items"]}
def mets(q):
    m = q["public_metrics"]
    return m["like_count"], m.get("repost_count", m.get("retweet_count")), m.get("impression_count")
def xblock(pid, kind):
    q = posts[pid]; l, r, v = mets(q)
    return {"url": q["url"], "author": "@" + users[q["author_id"]], "kind": kind, "likes": l,
            "reposts": r, "views": v, "posted_at": q["created_at"].replace(".000Z","Z"), "measured_at": MEASURED}
n = 0
for x in data["items"]:
    if x.get("x"):
        pid = x["x"]["url"].rsplit("/",1)[1]
        if pid in posts:
            l, r, v = mets(posts[pid])
            x["x"].update(likes=l, reposts=r, views=v, measured_at=MEASURED); n += 1
added = []
for it in reversed(NEW):
    if it["id"] in have: continue
    xs = it.pop("_x", None)
    if xs: it["x"] = xblock(*xs)
    data["items"].insert(0, it); added.append(it["id"])
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", len(added))
