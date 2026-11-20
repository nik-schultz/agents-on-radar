"""Nov 20 AM news run: add 11 items, swap gemini-computer-use-mac to the official @GeminiApp post,
refresh X numbers for items dated since Nov 12. Raw response: research/x_news_measure_2026_11_20_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_20_am.json.txt'
MEASURED = '2026-11-20T12:34:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D19 = "2026-11-19"; D18 = "2026-11-18"
new = [
 {"id": "chatgpt-dots-plus-test", "date": D19, "category": "feature", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI starts testing dots, ChatGPT's always-on agent, with a small number of Plus users, and brings them to all Business Standard users",
  "explainer": "If you pay for ChatGPT Plus you might see a dot appear, the background agent that keeps working on your tasks and goals across connected apps, which until now needed Pro or a higher business plan. It's a limited test, OpenAI hasn't said what Plus usage limits will be, and Pro users with a dot can also switch on a redesigned mobile app where the dot gets its own tab.",
  "source_url": "https://9to5mac.com/2026/11/19/openai-begins-testing-dots-with-chatgpt-plus-users-expands-business-access/", "source_name": "9to5Mac",
  "more_sources": [{"label": "The Verge (new mobile design)", "url": "https://www.theverge.com/ai-artificial-intelligence/1038334/openai-is-testing-a-new-design-for-mobile-chatgpt"}],
  "x": xb("https://x.com/thsottiaux/status/2123556256392847657", "@thsottiaux", "official", D19)},
 {"id": "meta-muse-chrome-extension", "date": D19, "category": "agent launch", "company": "Meta", "impact": "notable",
  "headline": "Meta's Muse agent comes to Chrome as a sidebar extension that can fill in forms, compare prices and chase refunds in your own browser",
  "explainer": "Muse can now work in your everyday Chrome browser, using the sites you're already logged into, in its own group of tabs you can take over by pressing Esc. Meta says it can't see your saved passwords or browsing history, but its activity can show up in your Google history, so log out of any account you don't want it to touch before connecting it.",
  "source_url": "https://www.digitaltrends.com/computing/meta-is-putting-muse-in-a-chrome-sidebar-and-the-official-announcement-just-arrived/", "source_name": "Digital Trends",
  "more_sources": [{"label": "Chrome Web Store", "url": "https://chromewebstore.google.com/detail/muse-from-meta/jnakhhjmpmoohbjgfccbccfoifnmbdjd"}],
  "x": xb("https://x.com/alexandr_wang/status/2123591819300934128", "@alexandr_wang", "official", D19)},
 {"id": "meta-muse-email-everyone", "date": D19, "category": "feature", "company": "Meta", "impact": "notable",
  "headline": "Every Muse user in supported countries can now get a @muse.ai email address their agent sends and receives from",
  "explainer": "You can forward Muse an email or ask it to write to a restaurant or a store for you, and it asks your approval before sending; the address doesn't give Muse access to your own inbox. Handles are first come, first served and can't be changed later, and anything you forward may include other people's details, so check the thread before you send it on.",
  "source_url": "https://www.meta.com/help/superintelligence/1149305437517250/", "source_name": "Meta Help Center",
  "more_sources": [{"label": "The Tech Outlook", "url": "https://www.thetechoutlook.com/new-release/software-apps/muse-now-supports-dedicated-muse-ai-email-addresses/"}],
  "x": xb("https://x.com/Muse/status/2123602791356883032", "@Muse", "official", D19)},
 {"id": "apple-computer-use-agent-report", "date": D19, "category": "industry", "company": "Apple", "impact": "notable",
  "headline": "Bloomberg: Apple is hiring to build its own AI agent that uses a Mac like a person, while macOS adds warnings for outside agents",
  "explainer": "Nothing changes for you yet: Apple's job listing describes an agent that browses, works across apps and writes code privately, and Bloomberg says a launch could come as soon as the end of next year. Sooner, macOS 27.3 will add warnings before you give third-party agents such as Gemini, ChatGPT or Claude full control of your Mac, so expect extra permission prompts.",
  "source_url": "https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/", "source_name": "TechCrunch",
  "more_sources": [{"label": "Bloomberg Law", "url": "https://news.bloomberglaw.com/california-brief/apple-is-working-on-own-ai-agent-to-rival-openai-and-anthropic"}],
  "x": xb("https://x.com/TheRundownAI/status/2123551782341107813", "@TheRundownAI", "coverage", D19)},
 {"id": "openai-gpt-live-1-1", "date": D19, "category": "model release", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI releases GPT-Live-1.1, a better-sounding voice model for developers, with a cheaper standby rate when nobody is talking",
  "explainer": "Phone and voice bots built on OpenAI should sound more natural across languages and accents and transcribe you more accurately. For builders, active talk stays $0.05 a minute, and a new standby mode on WebRTC sessions drops silent stretches to $0.02 a minute, so always-on voice helpers cost less to leave running.",
  "source_url": "https://developers.openai.com/api/docs/models/gpt-live-1.1", "source_name": "OpenAI",
  "more_sources": [{"label": "OpenAI API changelog", "url": "https://developers.openai.com/api/docs/changelog"}],
  "x": xb("https://x.com/OpenAIDevs/status/2123506733524136446", "@OpenAIDevs", "official", D19)},
 {"id": "google-search-homepage-ai-sidebar", "date": D19, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Google's desktop homepage gets a sidebar that keeps your AI Mode chats, so you can pick up an earlier search conversation",
  "explainer": "On google.com on a computer, a collapsible bar on the left now lists your recent AI Mode searches, lets you search them, start a new thread or connect a Gemini Notebook. It's rolling out worldwide on desktop; if you'd rather not keep them, AI Mode's temporary threads aren't saved to your history.",
  "source_url": "https://www.theverge.com/tech/1038059/google-search-homepage-ai-chats", "source_name": "The Verge",
  "more_sources": [{"label": "9to5Google", "url": "https://9to5google.com/2026/11/19/google-search-homepage-gemini-sidebar-update/"}],
  "x": xb("https://x.com/rmstein/status/2123500235930640844", "@rmstein", "official", D19)},
 {"id": "canva-ai-off-switch", "date": D19, "category": "feature", "company": "Canva", "impact": "notable",
  "headline": "Canva adds a switch to turn off its generative AI tools and an option to see less AI-made content in its library",
  "explainer": "Free and Pro users can hide tools like Magic Write, Magic Expand and image generation under Profile > Settings > Permissions, and show more human-made templates under Profile > Your account > AI Personalization. Editing helpers like Background Remover stay on and don't add an AI-generated label to your design.",
  "source_url": "https://www.canva.com/newsroom/news/ai-controls-canva/", "source_name": "Canva",
  "more_sources": [{"label": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1037126/canva-ai-features-off-button"}],
  "x": xb("https://x.com/canva/status/2123393385461432339", "@canva", "official", D19)},
 {"id": "meta-muse-charm-price-report", "date": D19, "category": "industry", "company": "Meta", "impact": "notable",
  "headline": "The Information: Meta plans to sell the Muse Charm, a small gadget for talking to your Muse agent, for $300 with a year of free Verizon 5G",
  "explainer": "If you've been waiting for a Muse device, the reported price is $300, with shipping still expected in time for the December holidays; Meta hasn't confirmed the price and says it will share more soon. It's a report, so wait for Meta's own listing before planning a purchase.",
  "source_url": "https://www.theverge.com/tech/1038087/meta-muse-charm-ai-price", "source_name": "The Verge",
  "more_sources": [{"label": "Engadget", "url": "https://www.engadget.com/2322541/metas-muse-charm-will-reportedly-cost-300-and-come-with-free-verizon-5g/"}],
  "x": xb("https://x.com/theinformation/status/2123514182955827445", "@theinformation", "coverage", D19)},
 {"id": "google-genie-4-gemini-api", "date": D19, "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Genie 4, Google's model that builds explorable 3D worlds, is now available to developers in the Gemini API and AI Studio",
  "explainer": "For people building apps: you can now generate a 720p world you can walk around in from a sentence or an image, with sound, and change it while it runs. It needs a paid API tier, a day after it opened to AI Ultra subscribers in Project Genie.",
  "source_url": "https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/", "source_name": "Google",
  "x": xb("https://x.com/GoogleAIStudio/status/2123479057996116143", "@GoogleAIStudio", "official", D19)},
 {"id": "hermes-enterprise-microsoft-teams", "date": D18, "category": "agent launch", "company": "Nous Research", "impact": "notable",
  "headline": "Nous Research brings its open-source Hermes Agent to Microsoft Teams, the Microsoft Store and Azure for businesses",
  "explainer": "If your company runs on Microsoft 365, staff can hand Hermes jobs like financial analysis, document drafts or inbox triage in a Teams chat and review the result there; it turns repeated work into skills colleagues can reuse. Companies with strict data rules can run it in their own Azure account, and nothing changes for people using Hermes on their own.",
  "source_url": "https://nousresearch.com/hermes-enterprise-in-microsoft-teams", "source_name": "Nous Research",
  "more_sources": [{"label": "Microsoft Marketplace", "url": "https://marketplace.microsoft.com/en-hk/product/wa200013263"}],
  "x": xb("https://x.com/NousResearch/status/2123535954946257096", "@NousResearch", "official", D19)},
 {"id": "perplexity-brain-auto-skills", "date": D18, "category": "feature", "company": "Perplexity", "impact": "notable",
  "headline": "Perplexity's Computer agent now writes its own reusable skills from how you work, and its Teammates agents come to the phone app",
  "explainer": "If you pay for Perplexity Max in the US, its Brain feature watches for jobs you repeat and writes step-by-step skills so you stop re-explaining them (up to 10, listed in the Plugins tab, and you can turn it off). Teammates and Multiagent also arrived in the iOS and Android apps for Max subscribers, with voice control for Teammates.",
  "source_url": "https://www.unite.ai/perplexity-brain-creates-and-updates-agent-skills-from-experience/", "source_name": "Unite.AI",
  "more_sources": [{"label": "Perplexity blog", "url": "https://www.perplexity.ai/hub/blog/self-improving-skills"}, {"label": "Perplexity (Teammates on mobile)", "url": "https://www.perplexity.ai/hub/blog/work-with-teammates-on-mobile-with-voice-mode"}],
  "x": xb("https://x.com/perplexity_ai/status/2123449395882701224", "@perplexity_ai", "official", D19)},
]
D = json.load(open('data/news.json')); items = D['items']
have = {i['id'] for i in items}; refreshed = 0
for it in items:
    if it['id'] == 'gemini-computer-use-mac':
        it['x'] = xb("https://x.com/GeminiApp/status/2123513203745538423", "@GeminiApp", "official", D19); continue
    x = it.get('x')
    if not x: continue
    pid = x['url'].rsplit('/', 1)[1]
    if pid in pm:
        m = pm[pid]; x.update(likes=m['like_count'], reposts=m.get('repost_count', m.get('retweet_count')), views=m['impression_count'], measured_at=MEASURED); refreshed += 1
add = [n for n in new if n['id'] not in have]
items[:0] = add
items.sort(key=lambda i: i['date'], reverse=True)
json.dump(D, open('data/news.json', 'w'), indent=1, ensure_ascii=False); open('data/news.json','a').write('\n')
print('added', len(add), 'refreshed', refreshed)
