"""Nov 11, 2026 AM news run: add 14 items, refresh X numbers (raw: research/x_news_measure_2026_11_11_am.json.txt)."""
import json, re
raw = open("research/x_news_measure_2026_11_11_am.json.txt").read()
d = json.loads(raw[raw.find("{"):raw.rfind("}")+1])
posts = {p["id"]: p for p in d["data"]}
MEAS = "2026-11-11T12:33:00Z"
def xblock(pid, author, kind):
    p = posts[pid]; m = p["public_metrics"]
    return {"url": f"https://x.com/{author}/status/{pid}", "author": "@"+author, "kind": kind,
            "likes": m["like_count"], "reposts": m.get("repost_count", m.get("retweet_count", 0)),
            "views": m.get("impression_count", 0), "posted_at": p["created_at"][:10], "measured_at": MEAS}
NEW = [
 {"id":"alibaba-qwen4-max-preview","date":"2026-11-11","category":"model release","company":"Alibaba","impact":"notable",
  "headline":"Alibaba says Qwen4 is coming and opens a two-week preview of its top model, Qwen4-Max",
  "explainer":"Qwen4-Max is Alibaba's new flagship for coding, office work and agent tasks, and it can read images and video, search the web and use tools with a 1-million-token memory. For now it's only a preview through Alibaba's Token Plan subscription and a few of its own apps (Qwen app, QwenWork, Qoder, QwenStudio); the preview runs until Nov 25 and there's no pay-as-you-go price yet.",
  "source_url":"https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview","source_name":"Alibaba Cloud",
  "x": xblock("2120335993643684315","Alibaba_Qwen","official")},
 {"id":"minimax-h3-image-open-weights","date":"2026-11-11","category":"model release","company":"MiniMax","impact":"notable",
  "headline":"MiniMax releases H3-Image, an open image model that makes 4K pictures in about 10 seconds",
  "explainer":"It can create or edit images from a prompt and up to 16 reference photos, and the weights are free to download on Hugging Face, so image apps and bots can run it themselves. It's also in MiniMax's API and Hailuo app at half price for 4K images during launch week; check the license before commercial use, because it carries regional and revenue limits.",
  "source_url":"https://www.minimax.io/blog/minimax-h3-image","source_name":"MiniMax",
  "more_sources":[{"label":"Hugging Face","url":"https://huggingface.co/MiniMaxAI/MiniMax-H3-Image"}],
  "x": xblock("2120179737695826420","MiniMax_AI","official")},
 {"id":"chatgpt-plus-veterans-offer","date":"2026-11-11","category":"pricing","company":"OpenAI","impact":"minor",
  "headline":"Leaving the military? OpenAI's free year of ChatGPT Plus is still open, and 20,000 veterans have claimed it",
  "explainer":"US servicemembers within 12 months of leaving active duty, and veterans or retirees who left in the past 12 months, can verify with ID.me at chatgpt.com/veterans-claim and get a year of Plus free. It renews at the normal price afterwards unless you cancel, so set a reminder.",
  "source_url":"https://openai.com/index/chatgpt-plus-for-veterans","source_name":"OpenAI",
  "more_sources":[{"label":"OpenAI Help: offer terms","url":"https://help.openai.com/en/articles/12803158-chatgpt-plus-for-service-members-veterans-retirees-terms-of-service"}]},
 {"id":"chatgpt-voice-advanced-standard-retiring","date":"2026-11-10","category":"feature","company":"OpenAI","impact":"notable",
  "headline":"ChatGPT will retire its older Advanced and Standard voice modes on December 11",
  "explainer":"If you talk to ChatGPT out loud, you'll be moved to Live voice (GPT-Live), which can listen and talk at the same time and hand bigger jobs to the text models in the background. Your old voice chats stay in your history, but live video and screen sharing stay on the old Advanced voice until Live supports them, and custom GPT voice ends the same day.",
  "source_url":"https://help.openai.com/en/articles/20001638-retiring-advanced-and-standard-voice-in-chatgpt","source_name":"OpenAI Help Center",
  "more_sources":[{"label":"ChatGPT release notes","url":"https://help.openai.com/en/articles/6825453-chatgpt-release-notes"}],
  "x": xblock("2120277245713654201","OpenAINewsroom","official")},
 {"id":"claude-free-usage-reset","date":"2026-11-10","category":"pricing","company":"Anthropic","impact":"notable",
  "headline":"Paid Claude users get one free full usage reset to use any time before December 10",
  "explainer":"Anthropic says a few bugs used up more of people's limits than they should have, so every Pro, Max, Ultra and Team user can refill all their limits once, across all models, from Settings > Usage (or clau.de/reset). It doesn't fire on its own and it's one-time, so save it for a day you actually hit the wall.",
  "source_url":"https://x.com/ClaudeDevs/status/2120275296637321476","source_name":"Claude Devs on X",
  "more_sources":[{"label":"Numerama","url":"https://www.numerama.com/tech/2372047-anthropic-offre-un-reset-gratuit-de-toutes-les-limites-a-ses-abonnes-payants-comment-en-profiter.html"}],
  "x": xblock("2120275296637321476","ClaudeDevs","official")},
 {"id":"meta-muse-email-address","date":"2026-11-10","category":"feature","company":"Meta","impact":"notable",
  "headline":"Meta's Muse now has its own email address, so you can forward it emails to handle",
  "explainer":"Paid Muse subscribers in the US and Canada can copy Muse on a thread or forward it a message, and it will send the replies and follow-ups for you. Because it writes on your behalf, start with low-stakes emails and check what it sends before trusting it with clients or money.",
  "source_url":"https://www.theverge.com/tech/1031029/metas-muse-can-now-deal-with-a-forwarded-email","source_name":"The Verge",
  "x": xblock("2120201720651563286","Muse","official")},
 {"id":"gemini-robotics-2-5","date":"2026-11-10","category":"model release","company":"Google","impact":"notable",
  "headline":"Google DeepMind's Gemini Robotics 2.5 lets robots learn hundreds of hands-on chores faster",
  "explainer":"The new robot brain handled 200+ tasks, from tying a bow to serving food with tongs, and sorted car parts at Mercedes-Benz factories with a 96% success rate in a trial. It's going to robot-maker partners first, not to the public, so it's a look at where home and work robots are heading rather than something you can use today.",
  "source_url":"https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/","source_name":"Google DeepMind",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/tech/1030134/google-deepminds-new-ai-model-gives-robots-improved-dexterity"},
                  {"label":"Ars Technica","url":"https://arstechnica.com/google/2026/11/deepmind-reveals-gemini-robotics-2-5-and-open-safety-benchmark-asimov-jailbreak/"}],
  "x": xblock("2120169787896525104","GoogleDeepMind","official")},
 {"id":"pixel-10-gemini-intelligence","date":"2026-11-10","category":"feature","company":"Google","impact":"notable",
  "headline":"Pixel 10 phones get Gemini Intelligence: tidy voice typing, custom widgets and errands done for you",
  "explainer":"The November Pixel Drop brings Rambler (talk messily, get a clean message), widgets you describe in words, chat summaries, and Gemini doing multi-step jobs like ordering groceries or booking a ride, that last part only in Japan, the UK and India for now. It rolls out over the next few weeks; the Pixel 10a isn't included.",
  "source_url":"https://blog.google/products-and-platforms/devices/pixel/november-2026-pixel-drop/","source_name":"Google blog",
  "more_sources":[{"label":"Google: Gemini Intelligence features","url":"https://blog.google/products-and-platforms/platforms/android/gemini-intelligence-november-features-devices/"},
                  {"label":"Engadget","url":"https://www.engadget.com/2312136/google-november-pixel-drop-rambler-hilight-updates/"}],
  "x": xblock("2120230094379577511","9to5Google","coverage")},
 {"id":"railway-stolen-ai-keys","date":"2026-11-10","category":"industry","company":"Railway","impact":"notable",
  "headline":"Hackers stole AI keys stored on app host Railway and ran up about $740,000 in charges",
  "explainer":"The attacker went looking for AI provider keys saved on Railway and used them to run other people's AI jobs on the victims' bills; Railway says it will pay what the AI companies won't refund. If you've ever put an OpenAI, Claude or Gemini key into a hosting or bot service, set a spending cap at the provider and swap the key if that service reports a breach.",
  "source_url":"https://blog.railway.com/p/incident-report-october-security-incident","source_name":"Railway blog",
  "more_sources":[{"label":"The Hacker News","url":"https://thehackernews.com/2026/11/railway-says-stolen-customer-ai-keys.html"}],
  "x": xblock("2120157279177634266","Railway","official")},
 {"id":"openai-acquires-odessia","date":"2026-11-10","category":"industry","company":"OpenAI","impact":"notable",
  "headline":"OpenAI buys Odessia, an AI travel agent, hinting at trip planning in ChatGPT",
  "explainer":"Odessia planned and booked trips with AI, and its founder Francis Davidson (who started Sonder) now works on travel at OpenAI. OpenAI hasn't announced a travel product, and Odessia's own service has already shut down, so anyone who used it should save their trip details elsewhere.",
  "source_url":"https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/","source_name":"TechCrunch",
  "more_sources":[{"label":"BetaKit","url":"https://betakit.com/openai-acquires-sonder-co-founders-new-travel-tech-company-odessia/"}],
  "x": xblock("2120239186632396996","testingcatalog","coverage")},
 {"id":"elevenlabs-scribe-v3","date":"2026-11-10","category":"model release","company":"ElevenLabs","impact":"notable",
  "headline":"ElevenLabs' Scribe v3 transcribes speech with 27% fewer mistakes and better 'who said what'",
  "explainer":"Meeting-note apps and voice bots built on ElevenLabs should get cleaner transcripts in 102 languages, better speaker labels with three or more people, and a live version that doesn't cut you off when you pause mid-number. It's the default in the ElevenLabs app now, and developers switch by changing one model name.",
  "source_url":"https://elevenlabs.io/blog/scribe-v3","source_name":"ElevenLabs",
  "x": xblock("2120217467100541396","ElevenLabs","official")},
 {"id":"spotify-dj-new-voices","date":"2026-11-10","category":"feature","company":"Spotify","impact":"minor",
  "headline":"Spotify's AI DJ gets nine new voices and a switch to stop the chatter between songs",
  "explainer":"Premium listeners can pick from seven new English voices and two Spanish ones, and turn off the commentary so the music just plays. Find it by searching DJ in the app and tapping the three-dot menu.",
  "source_url":"https://newsroom.spotify.com/2026-11-10/dj-new-voices-controls/","source_name":"Spotify",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/11/10/spotifys-ai-dj-gets-new-voices-personalities-and-an-option-for-less-chatter/"}],
  "x": xblock("2120154511352439040","Spotify","official")},
 {"id":"otter-27-new-languages","date":"2026-11-10","category":"feature","company":"Otter","impact":"minor",
  "headline":"Otter's AI notetaker adds 13 languages now and 14 more soon, at no extra cost",
  "explainer":"Mandarin, German, Italian, Korean, Portuguese and others work today for transcripts, summaries and action items, and a coming mode will follow a meeting as people switch languages. Otter says it runs its own speech models, so your audio isn't sent to another AI company.",
  "source_url":"https://otter.ai/blog/otter-ai-announces-its-biggest-multilingual-leap-yet-27-new-languages-and-multilingual-capabilities","source_name":"Otter.ai",
  "more_sources":[{"label":"TechCrunch","url":"https://techcrunch.com/2026/11/09/otter-ai-can-now-follow-conversations-across-30-languages/"}],
  "x": xblock("2120058214037295108","otter_ai","official")},
 {"id":"gemini-memory-summary","date":"2026-11-09","category":"feature","company":"Google","impact":"notable",
  "headline":"You can now see, fix and delete what Gemini remembers about you",
  "explainer":"A new Memory summary page (Settings > Personal Intelligence on the web) lists what Gemini has learned about you by topic, and you can type 'remove my old phone number' or 'add that I speak Japanese' to change it, plus see a history of changes. It's for US English Google AI subscribers for now; worth a two-minute check if you share personal details with it.",
  "source_url":"https://9to5google.com/2026/11/09/google-gemini-memory-summary/","source_name":"9to5Google",
  "more_sources":[{"label":"The Verge","url":"https://www.theverge.com/tech/1030720/google-gemini-memory-summary-edit-correct-ai-knowledge"}],
  "x": xblock("2119834339156377734","9to5Google","coverage")},
]
p = "data/news.json"; data = json.load(open(p))
have = {i["id"] for i in data["items"]}
refreshed = 0
for it in data["items"]:
    x = it.get("x")
    if not x: continue
    m = re.search(r"status/(\d+)", x["url"])
    if m and m.group(1) in posts:
        pm = posts[m.group(1)]["public_metrics"]
        x["likes"] = pm["like_count"]; x["reposts"] = pm.get("repost_count", pm.get("retweet_count", 0))
        x["views"] = pm.get("impression_count", x.get("views", 0)); x["measured_at"] = MEAS; refreshed += 1
added = [n for n in NEW if n["id"] not in have]
data["items"] = added + data["items"]
data["items"].sort(key=lambda i: i["date"], reverse=True)
json.dump(data, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
print("added", [n["id"] for n in added], "refreshed", refreshed)
