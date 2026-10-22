"""2026-10-21: 'Run your bots for less' section (saving money ON AI services).
Writes data/ai-pricing.json (official pricing pages only, checked 2026-10-21 ~9:20-9:30 AM CT),
adds the run-for-less category (in the old Money slot, reusing cat-money art), an Ollama tool entry,
and 8 sourced guides. Prices that couldn't be verified on an official page are left out."""
import json
D="2026-10-21"
OAI="https://platform.openai.com/docs/pricing"; ANT="https://docs.anthropic.com/en/docs/about-claude/pricing"; ANTP="https://claude.com/pricing"
GEM="https://ai.google.dev/gemini-api/docs/pricing"; XAI="https://docs.x.ai/docs/models"; GROQ="https://console.groq.com/docs/models"; MIS="https://mistral.ai/pricing"
def a(provider,model,tier,inp,out,cached,src,note=""):
    return {"provider":provider,"model":model,"tier":tier,"input":inp,"output":out,"cached_input":cached,"note":note,"source_url":src,"checked_on":D}
pricing={
 "_help":"Refresh weekly: re-open each source_url, update numbers and checked_on. Only official pricing pages. If a price can't be verified, remove it (don't guess). Prices in USD per 1M tokens, standard (non-batch) tier, short prompts.",
 "checked_on":D,"currency":"USD","unit":"per 1M tokens",
 "api":[
  a("OpenAI","gpt-6-astra","flagship",10.00,50.00,1.00,OAI,"Short context (≤272K input tokens)."),
  a("OpenAI","gpt-6.1-sol","mid",2.00,10.00,0.10,OAI,"Short context (≤272K input tokens)."),
  a("OpenAI","gpt-6-luna","small",0.10,0.50,0.01,OAI,"Short context (≤272K input tokens)."),
  a("Anthropic","Claude Fable 5.1","flagship",10.00,50.00,0.25,ANT,""),
  a("Anthropic","Claude Opus 5.5","flagship",4.00,20.00,0.20,ANT,""),
  a("Anthropic","Claude Sonnet 5.5","mid",2.00,10.00,0.10,ANT,""),
  a("Anthropic","Claude Haiku 5.5","small",0.10,0.50,0.01,ANT,"Prompts up to 100,000 tokens; longer prompts cost $0.50 / $2.50."),
  a("Google","gemini-4-argon","flagship",2.00,10.00,0.10,GEM,"Price through Nov 30, 2026; $4.00 / $20.00 from Dec 1, 2026. Not on the free tier."),
  a("Google","gemini-3.8-flash","mid",0.75,3.75,0.075,GEM,"Price through Dec 31, 2026; $1.50 / $7.50 from Jan 1, 2027. Free tier available."),
  a("Google","gemini-3.1-flash-lite","small",0.25,1.50,0.025,GEM,"Text/image/video input. Free tier available."),
  a("xAI","grok-4.7","flagship",2.00,6.00,0.50,XAI,"Prompts under 200K tokens; $4.00 / $12.00 above."),
  a("xAI","grok-4.3","mid",1.25,2.50,0.20,XAI,"Prompts under 200K tokens; $2.50 / $5.00 above."),
  a("Groq","openai/gpt-oss-120b","mid",0.15,0.60,None,GROQ,"Open-weight model hosted by Groq (Developer plan)."),
  a("Groq","openai/gpt-oss-20b","small",0.075,0.30,None,GROQ,"Open-weight model hosted by Groq (Developer plan)."),
  a("Mistral","Mistral Large","mid",0.50,1.50,None,MIS,"As quoted in the FAQ on Mistral's pricing page."),
 ],
 "discounts":[
  {"provider":"OpenAI","what":"Batch API: 50% off, results within 24 hours","source_url":"https://platform.openai.com/docs/guides/batch","checked_on":D},
  {"provider":"Anthropic","what":"Batch API: 50% off input and output. Prompt cache reads cost 0.1x the input price (0.05x on Opus/Sonnet 5.5, 0.025x on Fable 5.1); 5-minute cache writes cost 1.25x.","source_url":ANT,"checked_on":D},
  {"provider":"Google","what":"Batch API: 50% cost reduction (paid tier). Free tier: free input and output tokens on some models, and your content is used to improve Google's products.","source_url":GEM,"checked_on":D},
  {"provider":"Mistral","what":"Batch processing: 50% off. Cached input tokens: up to 90% off for repeated prompts.","source_url":MIS,"checked_on":D},
 ],
 "consumer":[
  {"provider":"Anthropic","plan":"Claude Free","price":"$0","period":"","note":"","source_url":ANTP,"checked_on":D},
  {"provider":"Anthropic","plan":"Claude Pro","price":"$20","period":"per month billed monthly ($17/month billed annually, $200 up front)","note":"Excludes tax. Includes hand-off and scheduled tasks.","source_url":ANTP,"checked_on":D},
  {"provider":"Anthropic","plan":"Claude Max","price":"from $100","period":"per month","note":"5x or 20x Pro usage; includes $100 to $200 a month in API credits.","source_url":ANTP,"checked_on":D},
  {"provider":"Mistral","plan":"Free","price":"$0","period":"","note":"Limited access.","source_url":MIS,"checked_on":D},
  {"provider":"Mistral","plan":"Pro","price":"$14.99","period":"per month","note":"Excluding taxes. Students: $5.99/month.","source_url":MIS,"checked_on":D},
  {"provider":"OpenAI","plan":"ChatGPT Free","price":"$0","period":"","note":"","source_url":"https://chatgpt.com/pricing","checked_on":D},
  {"provider":"Google","plan":"Gemini (free)","price":"$0","period":"","note":"With a Google Account.","source_url":"https://gemini.google/subscriptions/","checked_on":D},
 ],
 "not_verified":[
  {"provider":"OpenAI","what":"ChatGPT Go, Plus and Pro prices","why":"Not shown in the text of the official pricing page when we checked."},
  {"provider":"Google","what":"Google AI Plus, Pro and Ultra prices in USD","why":"The official page showed Canadian-dollar prices to our checker."},
  {"provider":"xAI","what":"SuperGrok price","why":"Not shown on the official Grok page when we checked."},
  {"provider":"Groq","what":"Consumer plan","why":"Groq sells API access, not a consumer chat plan."},
 ],
 "blueprint_models":["Claude Haiku 5.5","gemini-3.8-flash","Claude Sonnet 5.5","gpt-6-astra"],
 "voice":[
  {"provider":"xAI","what":"Grok Voice (speech to speech)","price_per_min":0.08,"source_url":XAI,"checked_on":D},
  {"provider":"OpenAI","what":"GPT-Live 1 voice sessions (model and tool usage billed separately)","price_per_min":0.05,"source_url":OAI,"checked_on":D},
 ],
}
json.dump(pricing,open('data/ai-pricing.json','w'),indent=1,ensure_ascii=False)

c=json.load(open('data/categories.json'))
if not any(x['slug']=='run-for-less' for x in c):
    c.insert(1,{"slug":"run-for-less","name":"Run your bots for less","icon":"🪙","art":"cat-money","blurb":"Spend less on AI services: right-size the model, cache, batch, schedule sensibly and cap your spending."})
json.dump(c,open('data/categories.json','w'),indent=1,ensure_ascii=False)
t=json.load(open('data/tools.json'))
t.setdefault("ollama",{"name":"Ollama (local models)","url":"https://ollama.com","cost":"Free to download; runs open models on your own computer","kind":"local"})
json.dump(t,open('data/tools.json','w'),indent=1,ensure_ascii=False)

def S(label,url,kind="docs"): return {"label":label,"url":url,"kind":kind}
G=[]
G.append(dict(slug="pick-a-smaller-model-for-simple-jobs",title="Use a small model for simple jobs and save the big one for hard ones",
 summary="Most bot jobs (sorting email, summarizing, checking a page) don't need the most powerful model. The small models cost a fraction as much, so route easy work to them and only send hard problems up.",
 what_the_bot_does=["Sends routine work (summaries, sorting, yes/no checks) to a small, cheap model.","Sends hard work (tricky reasoning, long documents, important drafts) to a bigger model.","Optionally lets the small model decide: if it isn't sure, it hands the job up.","Logs which model handled what, so you can see where the money goes."],
 what_you_end_up_with="The same results on everyday jobs for a fraction of the cost, with the expensive model kept for the jobs that need it.",
 difficulty="Medium",
 tools=[{"id":"n8n","note":"Route steps to different models in one workflow"},{"id":"make"},{"id":"zapier"},{"id":"grok-bot","note":"Pick the model per bot where the app allows it"}],
 prompt="You are a triage step. Read the task below and answer with one word: SIMPLE (summarize, sort, extract, yes/no) or HARD (multi-step reasoning, legal/medical/financial wording, long documents, anything you're unsure about). Task: [paste task].",
 watch_out=["Test the small model on 10 real examples before switching. Cheap is no good if it gets things wrong.","Prices change. Anthropic's small Haiku 5.5 lists $0.10 / $0.50 per million tokens and its top Fable 5.1 $10 / $50 (checked Oct 21, 2026); see our price table for the latest."],
 sources=[S("Anthropic pricing docs: \"Choose Haiku for simple tasks, Sonnet for most production workloads, and Opus for the most complex reasoning\"",ANT),S("OpenAI API pricing (official)",OAI),S("Gemini API pricing (official)",GEM)],
 tags=["model choice","routing","small model","cost"]))
G.append(dict(slug="test-your-bot-on-a-free-tier",title="Build and test your bot on a free tier before you pay",
 summary="Several AI providers let you try their API or app for free. Use that to prove your bot works before you put a card on file, and know what you give up on the free tier.",
 what_the_bot_does=["Runs your bot on a free plan or free API tier while you test it.","Uses small, realistic test runs (a day's email, one web page).","Shows you how many tokens each run uses, so you can estimate a real bill.","Moves to a paid plan only once it's doing a job you'd pay for."],
 what_you_end_up_with="A bot you know works, a realistic cost estimate, and no surprise bill while you were experimenting.",
 difficulty="Easy",
 tools=[{"id":"gemini","note":"Gemini API has a free tier on some models"},{"id":"claude","note":"New API users get a small amount of free credit"},{"id":"chatgpt","note":"ChatGPT has a free plan"},{"id":"grok","note":"Free to try on the web and in the apps"}],
 prompt="I'm testing a bot on a free tier. After each run, tell me roughly how many input and output tokens you used, and keep a running total for this test. Use only the sample data I give you: [sample].",
 watch_out=["Google says content sent on the Gemini API free tier is used to improve its products; paid-tier content isn't. Don't test with private data on a free tier.","Free tiers have lower limits and some models aren't included (Gemini 4 Argon isn't on the free tier)."],
 sources=[S("Gemini API pricing: free tier, \"Content used to improve our products\"",GEM),S("Anthropic pricing FAQ: \"New users receive a small amount of free credits to test the API\"",ANT),S("ChatGPT pricing: \"The free version of ChatGPT is available to everyone\"","https://chatgpt.com/pricing"),S("xAI: Grok is \"Free to try on the web and in the apps\"","https://x.ai/grok")],
 tags=["free tier","testing","cost estimate"]))
G.append(dict(slug="subscription-or-pay-per-use",title="Decide between a monthly AI plan and paying per use",
 summary="A monthly plan (like Claude Pro) gives you a flat price with usage limits. Paying per use through an API costs exactly what you use. Which is cheaper depends on how much your bots run.",
 what_the_bot_does=["Looks at how often your bots run and roughly how much they read and write.","Estimates a monthly API bill from the providers' official per-token prices.","Compares that with the flat monthly plans you're considering.","Tells you which is cheaper for your usage, and where the limits would bite."],
 what_you_end_up_with="A clear answer for your own usage: stay on a plan, switch to pay-per-use, or mix both.",
 difficulty="Easy",
 tools=[{"id":"claude"},{"id":"chatgpt"},{"id":"gemini"}],
 prompt="Help me compare costs. My bots: [list each bot, how often it runs, and roughly how much it reads, e.g. '30 emails a day']. Assume about 4 characters per token. Using these official per-million-token prices: [paste rows from the price table], estimate my monthly API cost for each model. Then compare with these plans: [plan and price]. Show your math.",
 watch_out=["Plans have usage limits. Anthropic says paid plans reset on a rolling five-hour window with weekly limits on top.","On Claude, when you hit a plan limit you can turn on usage credits billed at standard API rates, and Max plans include $100 to $200 a month in API credits.","Token counts vary. Anthropic says its newer models' tokenizer makes about 30% more tokens for the same text."],
 sources=[S("Claude plans and FAQ (official)",ANTP),S("Anthropic API pricing (official)",ANT),S("Mistral pricing: Pro $14.99/month, plus how API pricing is calculated",MIS)],
 tags=["subscription","api","pay per use","plans"]))
G.append(dict(slug="cut-costs-with-caching-and-batch",title="Cut your AI bill with prompt caching and batch discounts",
 summary="If your bot sends the same long instructions every time, caching makes the repeat part much cheaper. If results can wait a few hours, batch processing halves the price at several providers.",
 what_the_bot_does=["Puts the parts that never change (instructions, examples, reference docs) at the start of the prompt so they can be cached.","Re-uses that cached part on every run instead of paying full price for it.","Collects jobs that aren't urgent (nightly summaries, weekly reports) into one batch.","Sends the batch at the discounted rate and picks up the results later."],
 what_you_end_up_with="The same bot output, with repeated instructions billed at a fraction of the input price and non-urgent work at half price.",
 difficulty="Advanced",
 tools=[{"id":"n8n","note":"Call batch endpoints from a workflow"},{"id":"claude","note":"Prompt caching and Message Batches on the API"},{"id":"gemini","note":"Batch API and context caching on the paid tier"}],
 prompt="Rewrite my bot prompt for caching. Put everything that stays the same on every run (role, rules, examples, reference text) first, and everything that changes (today's emails, today's date) last. Mark where the fixed part ends. My prompt: [paste].",
 watch_out=["Caching only pays if the same prefix is re-used soon: Anthropic's 5-minute cache write costs 1.25x, and a read costs 0.1x the input price on most models.","Batch jobs aren't instant. OpenAI says each batch completes within 24 hours.","Not every model supports batch; check the provider's model page."],
 sources=[S("OpenAI Batch API guide: 50% cost discount, completes within 24 hours","https://platform.openai.com/docs/guides/batch"),S("Anthropic pricing: prompt caching multipliers and 50% Batch API discount",ANT),S("Gemini API pricing: Batch API (50% cost reduction) and context caching",GEM),S("Mistral pricing FAQ: batch reduces price by 50%, cached input up to 90% off",MIS)],
 tags=["prompt caching","batch api","discount","cost"]))
G.append(dict(slug="run-open-models-on-your-own-computer",title="Run open models on your own computer (or a cheap host) for simple jobs",
 summary="Open-weight models can run on your own computer with a free tool like Ollama, so routine jobs cost nothing per message. Some hosts also run open models for a fraction of big-model prices.",
 what_the_bot_does=["Installs a local model runner like Ollama on your computer.","Downloads an open model that fits your machine.","Points your bot's simple, private jobs (sorting, summarizing notes) at the local model.","Keeps a paid cloud model only for jobs the local one can't handle."],
 what_you_end_up_with="Routine bot jobs that run on your own hardware with no per-message bill, and your private text staying on your machine.",
 difficulty="Advanced",
 tools=[{"id":"ollama","note":"Runs open models locally"},{"id":"n8n","note":"Can call a local model from a workflow"}],
 prompt="Help me run [task, e.g. 'sort my notes into categories'] on a local model. My computer: [Mac/Windows, RAM, graphics card if known]. Suggest one open model that fits, the exact Ollama commands to install and run it, and a short test so I can check the quality before relying on it.",
 watch_out=["Local models are usually less capable than top cloud models. Test on real examples first.","Your computer has to be on, and big models need a lot of memory.","Licences vary. Mistral says its open-weight models are Apache 2.0 for research and individual use, while commercial deployments need a Mistral licence."],
 sources=[S("Ollama: \"Run AI models locally and in the cloud\"; prompts \"never stored or trained on\"","https://ollama.com","article"),S("GroqCloud models and prices: hosted open-weight gpt-oss-120b at $0.15 / $0.60 per million tokens",GROQ),S("Mistral pricing FAQ: self-hosting and open-weight licences",MIS)],
 tags=["local models","ollama","open source","privacy","self-host"]))
G.append(dict(slug="schedule-bots-without-burning-tokens",title="Stop always-on bots from burning tokens: run them less often, or on demand",
 summary="Every scheduled run costs tokens, even when nothing has changed. Match the schedule to how often the thing really changes, and switch fun-but-idle bots to run only when you ask.",
 what_the_bot_does=["Lists every scheduled bot and how often it runs.","Asks how often the thing it watches really changes (daily, weekly, rarely).","Lowers the schedule to match, or switches the bot to on-demand.","Makes each run cheap when nothing changed: a quick check first, a full report only if something did."],
 what_you_end_up_with="The same alerts and reports with far fewer paid runs.",
 difficulty="Easy",
 tools=[{"id":"grok-bot","note":"Routines can be scheduled or run on demand"},{"id":"chatgpt-dots"},{"id":"claude-cowork","note":"Scheduled tasks"},{"id":"zapier"}],
 prompt="Here are my scheduled bots: [name, what it does, how often it runs]. For each one, suggest the least frequent schedule that still catches what matters, or say if it should run only when I ask. For watchers, rewrite the instructions so each run first checks whether anything changed and stops with a one-line 'no change' if nothing did.",
 watch_out=["One user who set several agents to run multiple times a day says he switched them all to on-demand once he saw what autopilot cost.","A slower schedule means slower alerts. Keep fast checks only for things that are really time-sensitive."],
 sources=[{"label":"X post by @sunfellow (2026-10-20): moved his Grok Bot agents from several runs a day to on-demand after seeing the cost","url":"https://x.com/sunfellow/status/2112585672657969563","kind":"x"},S("Anthropic pricing docs: \"Monitor usage patterns: Track token consumption to identify optimization opportunities\"",ANT)],
 popularity={"platform":"x","post_id":"2112585672657969563","author":"@sunfellow","url":"https://x.com/sunfellow/status/2112585672657969563","posted_at":"2026-10-20","likes":10,"reposts":1,"replies":2,"bookmarks":5,"views":538,"measured_at":D},
 tags=["schedule","on demand","tokens","always-on agents"]))
G.append(dict(slug="keep-prompts-and-context-short",title="Keep your bot's prompts, tools and context short",
 summary="You pay for everything the model reads on every run: your instructions, tool definitions, pasted pages and the conversation so far. Trimming those is often the easiest saving.",
 what_the_bot_does=["Measures how many tokens each run reads (most consoles show this).","Cuts instructions to the rules that matter and removes repeated examples.","Turns off tools the bot doesn't need for this job.","Starts fresh conversations instead of dragging a long history along, and sends only the part of a page it needs."],
 what_you_end_up_with="Smaller, faster runs that cost less, with the same results.",
 difficulty="Medium",
 tools=[{"id":"claude"},{"id":"chatgpt"},{"id":"n8n","note":"Trim inputs before they reach the model"}],
 prompt="Here is my bot's full prompt: [paste]. Shorten it to the fewest words that keep every rule and the output format. List anything you removed so I can check. Then tell me which tools or attachments it doesn't need for this job.",
 watch_out=["Tools aren't free. Anthropic says its browser toolset adds about 6,600 input tokens per request and computer use about 4,500, before any screenshots.","Pages add up: Anthropic estimates an average 10 kB web page at about 2,500 tokens and a 500 kB PDF at about 125,000.","Don't cut safety rules (like 'ask before sending') to save tokens."],
 sources=[S("Anthropic pricing docs: tool overhead, web fetch token examples, tokenizer note",ANT)],
 tags=["prompt length","context","tokens","tools"]))
G.append(dict(slug="set-ai-spend-limits-and-alerts",title="Set spend limits and usage alerts on your AI accounts",
 summary="Before a bot runs on autopilot, put a hard cap on what it can spend and check usage weekly, so a runaway loop can't run up a big bill.",
 what_the_bot_does=["You set a monthly spend limit in each provider's billing settings.","You give each bot its own workspace or project, with its own lower limit where the provider allows it.","You check the usage dashboard once a week.","When a limit is hit, requests stop instead of costing more."],
 what_you_end_up_with="A known worst-case monthly bill, and an early warning when a bot starts using more than expected.",
 difficulty="Easy",
 tools=[{"id":"claude","note":"Spend limits per organization and workspace in the Claude Console"},{"id":"chatgpt"},{"id":"gemini"}],
 prompt="Help me set safe limits. My providers: [list]. My expected monthly use: [estimate]. For each provider, tell me where in its official billing settings to set a spend limit and usage alerts, and suggest a limit about [1.5x] my estimate. Point me to the provider's own help page for each step.",
 watch_out=["Anthropic says that when you reach a spend limit you set, API requests stop until you raise it or the period resets. Make sure your bot tells you when that happens.","On Anthropic you can't set spend limits on the default workspace, so put bots in their own workspace.","Consumer plans work differently: you hit usage limits instead of a bill."],
 sources=[S("Anthropic docs: spend limits, setting your own limit, workspace limits","https://docs.anthropic.com/en/api/rate-limits"),S("Mistral pricing FAQ: the Studio dashboard tracks API usage and costs",MIS)],
 tags=["spend limit","budget alerts","usage","billing"]))
for x in G:
    x.update(category="run-for-less",date_added=D,last_checked=D,origin="run-for-less-2026-10-21",setup=[],source_date=D)
    x.setdefault("popularity",None)
json.dump(G,open('data/incoming/2026-10-21-run-for-less.json','w'),indent=1,ensure_ascii=False)
print(len(G))
