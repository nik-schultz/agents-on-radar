"""2026-10-21: seed data/news.json from sources fetched this morning (official posts / reputable outlets).
Dates are the official publish dates shown on the source. X numbers measured 2026-10-21 ~9:40 AM CT."""
import json
CL="https://developers.openai.com/api/docs/changelog"
def N(id,date,cat,headline,explainer,url,name,more=None,x=None):
    d={"id":id,"date":date,"category":cat,"headline":headline,"explainer":explainer,"source_url":url,"source_name":name}
    if more: d["more_sources"]=[{"label":l,"url":u} for l,u in more]
    if x: d["x"]=x
    return d
items=[
N("openai-models-on-google-cloud","2026-10-21","industry","OpenAI's models are coming to Google Cloud",
  "Companies on Google Cloud will be able to use GPT-6 models and Codex without a separate OpenAI account (private preview now, wider launch planned in the coming weeks). For you it mostly means more places your work tools can quietly plug in OpenAI models.",
  "https://openai.com/index/openai-models-google-cloud","OpenAI",[("CNBC","https://www.cnbc.com/2026/10/21/openai-bring-its-ai-models-to-googles-cloud-expands-beyond-microsoft.html")]),
N("mistral-voxtral-3","2026-10-20","model release","Mistral launches Voxtral 3 for voice agents that can take calls",
  "A new set of speech models plus a kit for building phone and web voice agents that listen, look things up and talk back in 50+ languages. Mistral lists its voice agent API at $0.04 a minute with Mistral Small 4, so phone bots keep getting cheaper to run.",
  "https://mistral.ai/news/voxtral-3/","Mistral"),
N("openai-12-hour-prompt-caching","2026-10-20","pricing","OpenAI adds 12-hour prompt caching",
  "Bots that run hours apart (like a morning and an evening check) can now keep their fixed instructions cached and pay the lower cached-input price. Writing to the 12-hour cache costs 2.5x the normal input price, so it pays off when the same setup is reused several times.",
  CL,"OpenAI API changelog"),
N("android-police-gems-become-skills","2026-10-18","feature","Google turns Gemini Gems into Skills and moves Spark into the main chat",
  "From November 17, Google starts converting personal Gems into Skills you call with a slash in the main chat, and Scheduled Actions no longer need a paid plan (still rolling out to free accounts). If you built a Gem-based bot, test it before the switch.",
  "https://www.androidpolice.com/googles-renamed-gemini-features-field-guide/","Android Police"),
N("deepseek-v4-1-flash-1017","2026-10-17","model release","DeepSeek updates its V4.1 Flash model: faster and shorter answers, same price",
  "DeepSeek says the update finishes tasks faster with shorter outputs, which means fewer tokens to pay for. The API name and prices are unchanged, and the open weights are on Hugging Face.",
  "https://api-docs.deepseek.com/updates/","DeepSeek API changelog",[("SiliconANGLE","https://siliconangle.com/2026/10/18/deepseek-releases-updated-v4-1-flash-model-it-says-completes-tasks-faster/")]),
N("deepseek-search-fetch-api","2026-10-17","pricing","DeepSeek opens its own web search and page-fetch tools to developers",
  "Bots built on DeepSeek can now search the web and read pages through DeepSeek's own API at $0.75 per 1,000 requests each. Calls made through some coding agents are free until billing starts on November 1 (Beijing time).",
  "https://api-docs.deepseek.com/quick_start/pricing","DeepSeek pricing"),
N("groq-muse-spark-open","2026-10-15","model release","Meta's open-weight Muse Spark Open lands on Groq in limited preview",
  "Meta's new open model for coding agents is available on GroqCloud at launch, running at 350+ tokens per second per user. Faster answers matter for agents, because each task is a long chain of model calls.",
  "https://groq.com/blog/meta-s-muse-spark-open-release-is-now-in-limited-preview-on-groqcloud","Groq"),
N("grok-voice-3","2026-10-14","model release","xAI releases Grok Voice 3.0, its new speech-to-speech model",
  "The voice model behind Grok Bot's voice mode and Tesla's in-car assistant got an upgrade, at the same $0.08 a minute on the API. xAI says it answers in under a second and handles interruptions, which is what makes a phone bot feel natural.",
  "https://x.ai/news/grok-voice-3","xAI",[("SiliconANGLE","https://siliconangle.com/2026/10/14/grok-voice-3-0-from-spacexsi-outscores-openai-and-google-on-speech-to-speech-index/")]),
N("gemini-4-argon-available","2026-10-13","model release","Google's Gemini 4 Argon is now available to developers and paid Gemini users",
  "Google's new top model is in the API at an introductory $2 / $10 per million tokens, and in the Gemini app for Google AI Pro and Ultra subscribers. Google built it for long, multi-step work, the kind agents do.",
  "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/","Google",[("Gemini API release notes","https://ai.google.dev/gemini-api/docs/changelog")]),
N("meta-muse-wonder","2026-10-12","model release","Meta releases Muse Wonder, its first frontier model",
  "Meta says Muse Wonder will soon power its Muse personal agent, starting with paying subscribers. Developers can use it through Meta's API at $4 / $20 per million tokens.",
  "https://dev.meta.ai/resources/blog/build-with-muse-wonder","Meta",[("TechCrunch","https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/")]),
N("gemini-spark-becomes-task","2026-10-12","feature","Gemini's Spark agent moves to a \"Task\" button on the app's home screen",
  "Handing a job to Google's background agent is now one tap away in the Gemini app, with a new Scheduled page that shows active, paused and finished tasks. It's live on Android and iOS; web wasn't confirmed yet.",
  "https://9to5google.com/2026/10/12/gemini-spark-task-redesign/","9to5Google",[("Android Authority","https://www.androidauthority.com/gemini-spark-tasks-button-3723394/")]),
N("openai-agents-sandbox-billing","2026-10-09","pricing","OpenAI stops charging agents for idle sandbox time",
  "Agents built on OpenAI's Agents API run in a hosted sandbox computer, and that is now billed only during active turns, not while the agent waits for you. Sandboxes can also be pre-warmed so replies start faster.",
  CL,"OpenAI API changelog"),
N("gpt-6-for-everyone","2026-10-07","model release","GPT-6 rolls out to everyone in ChatGPT, with interactive answers",
  "ChatGPT answers can now include charts, buttons, forms and small tools you use right in the chat. Paid plans get GPT-6 Sol and Free and Go users get GPT-6 Luna, starting October 8.",
  "https://openai.com/index/gpt-6-for-everyone/","OpenAI"),
N("claude-haiku-5-5","2026-10-07","model release","Anthropic releases Claude Haiku 5.5, a fast, cheap model for high-volume bot work",
  "At $0.10 / $0.50 per million tokens for prompts up to 100,000 tokens, Anthropic says it costs about 75% less to run than Haiku 4.5. It's built for summaries, sorting and browser use: the simple, repeated jobs most everyday bots do.",
  "https://www.anthropic.com/news/claude-haiku-5-5","Anthropic"),
N("claude-sonnet-cache-cut-and-credits","2026-10-07","pricing","Anthropic halves Sonnet 5.5 cache reads and gives Max and Team plans monthly API credits",
  "Cached reads on Claude Sonnet 5.5 dropped from $0.20 to $0.10 per million tokens, which Anthropic says makes most agent work about 20% cheaper. Max subscribers get $100 or $200 a month in API credits, and Team plans up to $500, to build their own bots.",
  "https://www.anthropic.com/news/claude-haiku-5-5","Anthropic"),
N("mistral-large-4-preview","2026-10-06","model release","Mistral previews Mistral Large 4, with open weights promised by month's end",
  "Mistral's biggest model yet is in a public preview on its API, and Mistral says anyone will be able to download and run it themselves later this month. That's good news if you want a strong model you can host privately.",
  "https://mistral.ai/news/mistral-large-4","Mistral"),
N("gpt-6-1-sol","2026-09-29","model release","OpenAI releases GPT-6.1 Sol: near-top performance at a fifth of the price",
  "OpenAI says GPT-6.1 Sol nearly matches its top model, GPT-6 Astra, on agent work at one-fifth of Astra's token prices ($2 / $10 per million). For bot builders, it's a cheaper middle option for jobs a small model can't handle.",
  "https://openai.com/index/introducing-gpt-6-1-sol/","OpenAI",[("OpenAI API changelog",CL)]),
N("openai-agents-api-computer-use","2026-09-29","feature","OpenAI's Agents API can now use a web browser",
  "Agents built on OpenAI's platform can now complete tasks in an OpenAI-hosted browser, with the app asking you before it visits a site and handling sign-in. Expect more third-party bots that click through websites for you.",
  CL,"OpenAI API changelog"),
N("claude-sonnet-5-5","2026-09-28","model release","Anthropic releases Claude Sonnet 5.5",
  "Anthropic says Sonnet 5.5 runs 30%+ faster than Sonnet 5 and costs up to 30% less for most work. It's the middle model many agent apps use by default.",
  "https://www.anthropic.com/news/claude-sonnet-5-5","Anthropic"),
N("grok-bot-team-bots","2026-09-28","agent launch","Grok Bot adds Team Bots: shared AI teammates for a whole team",
  "One person sets up a bot with the files, apps and skills it needs, then the whole team can use it in Slack or Grok Bot, while each person's chats stay private. It's in public beta for Teams and Enterprise plans.",
  "https://x.ai/news/team-bots","xAI",[("TeslaNorth","https://teslanorth.com/2026/09/28/spacexai-team-bots-launch/")],
  {"url":"https://x.com/bot/status/2104661562715967548","author":"@bot","likes":6404,"reposts":574,"posted_at":"2026-09-28","measured_at":"2026-10-21"}),
N("claude-opus-5-5","2026-09-22","model release","Anthropic releases Claude Opus 5.5",
  "Anthropic says Opus 5.5 leads in agentic coding and knowledge work and costs 40% less to run than Opus 5 on typical workloads. It's the model to reach for when a bot's job is hard, not routine.",
  "https://www.anthropic.com/news/claude-opus-5-5","Anthropic"),
N("gpt-6-sol-and-luna","2026-09-22","model release","OpenAI releases GPT-6 Sol and GPT-6 Luna",
  "Two new models: Sol for most work and Luna, a very cheap one at $0.10 / $0.50 per million tokens. Luna is the kind of model to use for simple, frequent bot jobs.",
  CL,"OpenAI API changelog"),
N("grok-4-7","2026-09-21","model release","xAI releases Grok 4.7",
  "xAI's new model for coding and knowledge work keeps the same $2 / $6 per million token price as Grok 4.6. xAI says it was trained to work inside the Grok Bot harness, which should make Grok Bot better at everyday tasks.",
  "https://x.ai/news/grok-4-7","xAI",[("SiliconANGLE","https://siliconangle.com/2026/09/21/spacex-launches-grok-4-7-with-long-horizon-processing-safety-upgrades/")]),
]
items.sort(key=lambda x:x["date"],reverse=True)
json.dump({"_help":"Latest in AI. Newest first. Every item: date (official publish date), plain headline, 1-2 sentence beginner explainer, category, source_url (official announcement or reputable outlet you actually opened). Optional x: real numbers + measured_at. If an item changes model prices, update data/ai-pricing.json too.","categories":["model release","agent launch","feature","pricing","industry"],"items":items},open('data/news.json','w'),indent=1,ensure_ascii=False)
print(len(items))

p=json.load(open('data/ai-pricing.json'))
D="2026-10-21"
have={r["model"] for r in p["api"]}
new=[{"provider":"Meta","model":"Muse Wonder","tier":"flagship","input":4.0,"output":20.0,"cached_input":None,"note":"Meta Model API. Price from Meta's launch post (Oct 12, 2026).","source_url":"https://dev.meta.ai/resources/blog/build-with-muse-wonder","checked_on":D},
     {"provider":"DeepSeek","model":"deepseek-flash (V4.1-Flash-1017)","tier":"small","input":0.30,"output":1.20,"cached_input":0.006,"note":"Peak-hour price; off-peak (most hours and weekends) is half.","source_url":"https://api-docs.deepseek.com/quick_start/pricing","checked_on":D},
     {"provider":"DeepSeek","model":"deepseek-v4-pro","tier":"mid","input":1.32,"output":3.96,"cached_input":0.044,"note":"Peak-hour price; off-peak is half.","source_url":"https://api-docs.deepseek.com/quick_start/pricing","checked_on":D}]
p["api"]+= [r for r in new if r["model"] not in have]
for d in p["discounts"]:
    if d["provider"]=="OpenAI" and "12-hour" not in d["what"]:
        d["what"]+=". Prompt caching: cached input is far cheaper; 12-hour cache writes (added Oct 20, 2026) cost 2.5x the input price."
        d["source_url"]=CL
if not any(d["provider"]=="DeepSeek" for d in p["discounts"]):
    p["discounts"].append({"provider":"DeepSeek","what":"Off-peak discount: prices are half outside peak hours (01:00-04:00 and 06:00-10:00 UTC on weekdays). Cache hits are far cheaper than misses.","source_url":"https://api-docs.deepseek.com/quick_start/pricing","checked_on":D})
if not any(v["provider"]=="Mistral" for v in p["voice"]):
    p["voice"].append({"provider":"Mistral","what":"Voxtral 3 voice agent API with Mistral Small 4","price_per_min":0.04,"source_url":"https://mistral.ai/news/voxtral-3/","checked_on":D})
json.dump(p,open('data/ai-pricing.json','w'),indent=1,ensure_ascii=False)
