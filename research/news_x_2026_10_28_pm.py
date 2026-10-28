"""Oct 28, 2026 PM news run: 9 new items + X re-measure (research/x_news_measure_2026_10_28_pm.json.txt)."""
import json
MEASURED = "2026-10-28"
raw = open("research/x_news_measure_2026_10_28_pm.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
users = {u["id"]: u["username"] for u in d["includes"]["users"]}
posts = {p["id"]: p for p in d["data"]}
NEW = [
 {"id":"google-gemini-4-carbon","date":"2026-10-28","category":"model release","company":"Google","impact":"major",
  "headline":"Google announces Gemini 4 Carbon, its new top model, but only a few security teams can use it so far",
  "explainer":"Carbon is Google's strongest model yet: it now ranks #1 on the Artificial Analysis Intelligence Index and is built for long coding jobs and for finding and fixing security holes. This week only selected cyber defenders get it; Google says developers, businesses and the Gemini app get it 'as soon as possible', at the same intro API price as Argon ($2 in / $10 out per million tokens, later $4 / $20).",
  "source_url":"https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/","source_name":"Google blog",
  "more_sources":[{"label":"9to5Google","url":"https://9to5google.com/2026/10/28/gemini-4-carbon-announcement/"},{"label":"VentureBeat","url":"https://venturebeat.com/technology/google-unveils-gemini-4-carbon-retaking-the-worlds-no-1-spot-on-updated-harder-benchmarks-but-access-is-limited"}],
  "_x":("2115489219804352921","official")},
 {"id":"chatgpt-dots-texting","date":"2026-10-28","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"You can now text your ChatGPT dot over iMessage or RCS",
  "explainer":"Your dot (ChatGPT's always-on agent) can now take tasks by text, photo or voice note from your phone's Messages app, and text you back when something needs you. It's a beta for US ChatGPT Pro users only, one-to-one (no group chats), and it can't see your other text conversations.",
  "source_url":"https://learn.chatgpt.com/docs/dots/channels","source_name":"ChatGPT Learn",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/ai-artificial-intelligence/1021183/openai-now-lets-you-text-your-dot"},{"label":"9to5Mac","url":"https://9to5mac.com/2026/10/28/openai-expanding-chatgpt-dot-access-to-imessage-and-rcs/"}],
  "_x":("2115496387613786374","official")},
 {"id":"claude-for-legal-artifacts","date":"2026-10-28","category":"feature","company":"Anthropic","impact":"notable",
  "headline":"Claude for Legal gets ready-made tools for contract review, cite checks and rule tracking",
  "explainer":"Legal teams can start from a gallery of ready-to-use Claude 'artifacts', such as a contract comparison table, a citation checker and a regulation timeline, add their own documents and share them with coworkers. Every answer links back to its source, and a lawyer still reviews the result; it's aimed at businesses and law firms, not personal legal advice.",
  "source_url":"https://claude.com/resources/articles/introducing-artifacts-for-legal-work","source_name":"Claude blog",
  "more_sources":[{"label":"Reuters via Economic Times","url":"https://economictimes.indiatimes.com/tech/artificial-intelligence/anthropic-unveils-additional-claude-tools-for-lawyers/articleshow/135271177.cms"},{"label":"Legal IT Insider","url":"https://legaltechnology.com/anthropic-moves-further-up-the-legal-tech-stack-with-launch-of-claude-for-legal-artifacts/"}],
  "_x":("2115467192276025500","official")},
 {"id":"google-connected-apps-platform","date":"2026-10-28","category":"feature","company":"Google","impact":"notable",
  "headline":"Google opens Gemini and Search to more outside apps, starting with Adobe, Calm and Peloton",
  "explainer":"More of the apps you already use will work right inside the Gemini app and Google Search, so you can ask Gemini to plan a Peloton workout or use Adobe without switching apps. Google launched a developer preview (US, waitlist) that lets any app plug in through MCP; more than 50 Connected Apps are live, and Calm is coming to both Search and Gemini.",
  "source_url":"https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/","source_name":"Google blog",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/10/28/as-ai-agents-reshape-the-web-google-opens-gemini-and-search-to-more-apps/"}],
  "_x":("2115507306163208445","coverage")},
 {"id":"github-copilot-fusion","date":"2026-10-28","category":"feature","company":"Microsoft","impact":"notable",
  "headline":"GitHub Copilot Fusion picks the AI model for you, and Microsoft opens its Copilot agent engine to builders",
  "explainer":"If you code with GitHub Copilot, you can now choose 'Copilot Fusion' and an effort level instead of a model; it routes each task to cheaper or stronger models and GitHub says it came within 2 points of Claude Code with Opus 5.5 at about half the cost per task (30% off for paid plans through Nov 30). Microsoft also made the harness behind Copilot available in Microsoft Foundry, so companies can build their own agents on it.",
  "source_url":"https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/","source_name":"GitHub Changelog",
  "more_sources":[{"label":"Microsoft blog: Copilot harness","url":"https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/"},{"label":"GitHub Universe 2026","url":"https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/"}],
  "_x":("2115490856685990244","official")},
 {"id":"nvidia-nemotron-3-5-transcribe","date":"2026-10-28","category":"model release","company":"NVIDIA","impact":"notable",
  "headline":"NVIDIA releases Nemotron 3.5 Transcribe, a free open model that writes up recordings and says who spoke",
  "explainer":"Expect better, cheaper meeting-notes and transcription bots: this free, open-weight model transcribes 40 languages, translates, tells up to eight speakers apart and handles recordings up to an hour. It works on recorded audio, not live calls, and is meant for app builders rather than a ready-made app.",
  "source_url":"https://huggingface.co/blog/nvidia/nemotron-transcribe-granary","source_name":"NVIDIA on Hugging Face",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/"}],
  "_x":("2115462300241141882","official")},
 {"id":"perplexity-voice-gpt-live-1","date":"2026-10-28","category":"feature","company":"Perplexity","impact":"minor",
  "headline":"Perplexity's voice mode can now run several Computer tasks at once",
  "explainer":"On the Mac app and web, Pro and Max subscribers can talk to Perplexity to start new Computer tasks, check on several running at once and manage Projects in one voice session. It now runs on OpenAI's gpt-live-1 voice model, which can listen while it talks.",
  "source_url":"https://9to5mac.com/2026/10/28/perplexity-upgrades-mac-app-with-chatgpt-powered-voice-mode/","source_name":"9to5Mac",
  "_x":("2115471825031610611","official")},
 {"id":"gemini-immersive-explorations","date":"2026-10-28","category":"feature","company":"Google","impact":"minor",
  "headline":"Gemini adds interactive 'immersive explorations' for learning a topic layer by layer",
  "explainer":"Students and curious adults can zoom through interactive scenes, like inside a jet engine or along the Silk Road, and tap labels to dig deeper. It's free for all users from the Gemini student hub for now, with direct access in chats and audio narration coming soon.",
  "source_url":"https://blog.google/innovation-and-ai/products/gemini-app/immersive-explorations-student-hub/","source_name":"Google blog",
  "_x":("2115507092660289631","official")},
 {"id":"meta-waddle-world","date":"2026-10-28","category":"feature","company":"Meta","impact":"minor",
  "headline":"Meta tests Waddle World, an AI virtual pet app, in the Philippines",
  "explainer":"Waddle World is a Tamagotchi-style app where an AI pixel pet gets to know you, turns what you tell it into illustrated journal entries and can send a weekly email. It's a test in the Philippines only (iOS and Android, 18+), and Meta says it's not a chatbot or an assistant.",
  "source_url":"https://techcrunch.com/2026/10/28/meta-has-a-new-ai-pet-app-called-waddle-world/","source_name":"TechCrunch",
  "_x":("2115210391462551845","coverage")},
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
added = []
for it in reversed(NEW):
    if it["id"] in have: continue
    xs = it.pop("_x", None)
    if xs: it["x"] = xblock(*xs)
    data["items"].insert(0, it); added.append(it["id"])
data["items"].sort(key=lambda x: x["date"], reverse=True)
json.dump(data, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
print("refreshed", n, "added", len(added))
