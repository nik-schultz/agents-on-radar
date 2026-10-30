"""Oct 30, 2026 PM news run: 7 new items + X re-measure (research/x_news_measure_2026_10_30_pm.json.txt)."""
import json
MEASURED = "2026-10-30"
raw = open("research/x_news_measure_2026_10_30_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"openai-teen-violence-safeguards","date":"2026-10-30","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"ChatGPT tightens weapons answers for teens and can end chats fixated on violence",
  "explainer":"If a teen in your house uses ChatGPT, it will now refuse more weapons details, and for everyone it limits step-by-step recreations of past mass attacks. It can also end conversations stuck on violence and may briefly pause an account, and OpenAI says it will publish its first community safety report in early 2027.",
  "source_url":"https://openai.com/index/community-safety-report-and-new-protections-for-teens/","source_name":"OpenAI",
  "more_sources":[{"label":"Reuters (via US News)","url":"https://money.usnews.com/investing/news/articles/2026-10-30/openai-to-limit-weapons-information-for-teens-on-chatgpt-in-violence-prevention-push"}]},
 {"id":"zest-text-restaurant-concierge","date":"2026-10-30","category":"agent launch","company":"Zest","impact":"notable",
  "headline":"Zest launches a restaurant agent you just text, and it books tables for your group chat",
  "explainer":"Text it what you're craving and it suggests places and books through OpenTable, Resy or SevenRooms, with no app to install. Add it to a group chat and it runs a vote on where to eat; linking a credit card lets it learn where you actually like to eat, so only share that if you're comfortable.",
  "source_url":"https://techcrunch.com/2026/10/30/zests-new-ai-agent-finds-restaurants-and-books-reservations-over-text/","source_name":"TechCrunch"},
 {"id":"doordash-amazon-agent-orders-tiny","date":"2026-10-30","category":"industry","company":"DoorDash","impact":"notable",
  "headline":"Reality check: DoorDash has seen only 'several hundred' orders from outside AI shopping agents",
  "explainer":"Agents like Meta's Muse can order food for you, but almost nobody is doing it yet: DoorDash counts a few hundred agent orders against millions of normal ones, and Amazon's CEO called outside shopping agents 'still not great.' For now, your bot works best for finding and comparing; expect to finish checkout yourself on many stores.",
  "source_url":"https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/","source_name":"TechCrunch",
  "more_sources":[{"label":"Fortune (Amazon's Jassy)","url":"https://fortune.com/2026/10/29/amazon-ceo-says-shopping-agents-like-metas-muse-not-great/"}],
  "_x":("2116168014911398369","coverage")},
 {"id":"gemini-api-computer-use-ga","date":"2026-10-30","category":"feature","company":"Google","impact":"minor",
  "headline":"Gemini's Computer Use tool is now generally available for developers",
  "explainer":"Apps built on Gemini can now officially let the AI look at a screen and click, type and scroll in a browser, desktop or phone. Expect more third-party bots that fill in forms for you, and look for ones that ask before checking out or changing sensitive info, which Google turns on by default.",
  "source_url":"https://ai.google.dev/gemini-api/docs/changelog","source_name":"Gemini API release notes",
  "more_sources":[{"label":"Computer Use guide","url":"https://ai.google.dev/gemini-api/docs/computer-use"}]},
 {"id":"openai-robots-txt-ai-training-signal","date":"2026-10-30","category":"industry","company":"OpenAI","impact":"minor",
  "headline":"OpenAI and Google back one shared robots.txt switch to keep a website out of AI training",
  "explainer":"If you run a blog or small business site, you'll soon be able to say 'don't train AI on this' once, for every participating AI company, instead of blocking each crawler separately. OpenAI says support comes in the next few months and Google aims for 2027; it's based on an IETF draft that isn't final yet.",
  "source_url":"https://openai.com/index/helping-websites-express-ai-training-preferences/","source_name":"OpenAI",
  "more_sources":[{"label":"Google Search Central","url":"https://developers.google.com/search/blog/2026/10/ai-training-control"},{"label":"Unite.AI","url":"https://www.unite.ai/openai-to-honor-shared-robots-txt-signal-for-ai-training-preferences/"}]},
 {"id":"pika-h3-flex-open-weights","date":"2026-10-29","category":"model release","company":"Pika","impact":"notable",
  "headline":"Pika releases H3 Flex, a fast video-with-sound model with open weights",
  "explainer":"It makes a 15-second clip with a soundtrack in seconds, can follow up to 12 reference images, videos or voice clips, and upscales your favorite to 4K. It's on the Pika API now and comes to the Pika app on Nov 2; the downloadable weights' license excludes the US, EU, UK and Korea.",
  "source_url":"https://pika.art/blog/pika-h3-flex","source_name":"Pika",
  "more_sources":[{"label":"Business Wire","url":"https://www.businesswire.com/news/home/20261029115507/en/Pika-Launches-Pika-H3-Flex-a-Video-Model-Built-for-Professional-Iteration"},{"label":"Hugging Face","url":"https://huggingface.co/Pika-Labs/Pika-H3-Flex"}],
  "_x":("2115860471215788262","official")},
 {"id":"elevenlabs-sfx-v3","date":"2026-10-29","category":"model release","company":"ElevenLabs","impact":"notable",
  "headline":"ElevenLabs launches SFX v3, which turns one sentence into a layered sound scene",
  "explainer":"Describe a scene, like rain, thunder and a dog barking, and it now gets each sound in, in order, with cleaner audio and better music and vocals. Handy for giving home videos, reels or school projects real sound; it's in the ElevenLabs app, ElevenCreative and the API.",
  "source_url":"https://elevenlabs.io/blog/sound-effects-v3","source_name":"ElevenLabs",
  "_x":("2115867078964187368","official")},
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
json.dump(data, open(p,"w"), indent=2, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", len(added))
