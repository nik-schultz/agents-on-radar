"""Nov 23 AM news run (covers Nov 20 PM - Nov 23 AM): add 11 items, refresh X numbers for items dated since Nov 13.
Raw response: research/x_news_measure_2026_11_23_am.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_23_am.json.txt'
MEASURED = '2026-11-23T12:34:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D23 = "2026-11-23"; D22 = "2026-11-22"; D21 = "2026-11-21"; D20 = "2026-11-20"; D19 = "2026-11-19"
new = [
 {"id": "glm-5-4-loop-transformer", "date": D23, "category": "model release", "company": "Z.ai", "impact": "notable",
  "headline": "Z.ai releases GLM-5.4, a big coding model that runs some of its layers twice to think harder",
  "explainer": "If you subscribe to Z.ai's GLM Coding Plan or use Z.ai Chat or its ZCode app, you can try GLM-5.4 now; there's no pay-as-you-go API price yet, and Z.ai says the API and free open weights come after safety testing. Z.ai says the 750B model matches models several times its size but published no benchmark scores, and admits it can get stuck in very long 'marathon thinking'.",
  "source_url": "https://z.ai/blog/glm-5.4", "source_name": "Z.ai",
  "more_sources": [{"label": "The Next Web", "url": "https://thenextweb.com/news/zai-glm-5-4-loop-transformer-coding-model"}],
  "x": xb("https://x.com/Zai_org/status/2124811995912286352", "@Zai_org", "official", D23)},
 {"id": "openai-perplexity-common-limits", "date": D22, "category": "industry", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI publishes how fast its models' core ability has grown and proposes shared limits for all AI labs",
  "explainer": "Nothing changes in ChatGPT today: OpenAI's chief scientist published how much better its models have got at predicting text since GPT-3.5 and proposes that AI labs agree on common limits, with progress past them only once we can understand how the models behave. Sam Altman and Microsoft AI chief Mustafa Suleyman back the idea, but no shared limit exists yet, and OpenAI didn't release its test data, so outsiders can't check the numbers.",
  "source_url": "https://openai.com/index/perplexity-and-intelligence/", "source_name": "OpenAI",
  "more_sources": [{"label": "Sam Altman on X", "url": "https://x.com/sama/status/2124551594691932405"},
                   {"label": "Mustafa Suleyman on X", "url": "https://x.com/mustafasuleyman/status/2124663594449318173"}],
  "x": xb("https://x.com/merettm/status/2124549218995949967", "@merettm", "official", D22)},
 {"id": "meta-wang-superintelligence-essay", "date": D22, "category": "industry", "company": "Meta", "impact": "notable",
  "headline": "Meta's chief AI officer says superintelligence is arriving and the industry must change course on safety",
  "explainer": "Nothing changes in Muse or Meta AI today: Alexandr Wang, Meta's chief AI officer, wrote that AI smarter than people in every field is coming soon, pointing to the Riemann proof, and said labs must put safety first rather than accept a 'handover' of society to AI. It's an opinion essay with no new rules or product changes, but it stands out because Meta has usually been the most upbeat big lab.",
  "source_url": "https://www.aljazeera.com/economy/2026/11/23/ai-superintelligence-arriving-warns-top-meta-executive", "source_name": "Al Jazeera",
  "more_sources": [{"label": "Mashable", "url": "https://me.mashable.com/tech/78622/superintelligence-is-coming-metas-alexandr-wang-says-humanity-must-rethink-control-before-its-too-la"}],
  "x": xb("https://x.com/alexandr_wang/status/2124636606959345776", "@alexandr_wang", "official", D22)},
 {"id": "riemann-proof-lean-certified", "date": D21, "category": "industry", "company": "Anthropic", "impact": "notable",
  "headline": "Mathematicians' checking tools confirm the Riemann hypothesis proof made with Claude is correct",
  "explainer": "Nothing changes in the Claude app, but the proof of the Riemann hypothesis that an Anthropic mathematician made with Claude's help has now been checked: the Lean and Mathlib open-source math communities say several independent proof-checking programs confirm it is correct. Mathematicians still want a written explanation of the new ideas, but it's the strongest sign yet that AI can help solve problems people couldn't.",
  "source_url": "https://leanprover-community.github.io/blog/posts/riemann-hypothesis/", "source_name": "Lean community blog",
  "more_sources": [{"label": "Scientific American", "url": "https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/"}],
  "x": xb("https://x.com/leanprover/status/2124159121645801562", "@leanprover", "official", D21)},
 {"id": "together-ai-prompt-leak", "date": D21, "category": "industry", "company": "Together AI", "impact": "notable",
  "headline": "Together AI says some customer prompts were stolen after an AI coding agent published an access key",
  "explainer": "If you run a bot on Together AI, some prompts sent to its MiniMax M3, GLM-5.2 and Kimi K2.6 models in June and July were downloaded by an outsider after an AI coding agent accidentally published an access key; Together will contact affected customers and suggests turning on zero data retention. It's a lesson for anyone using a coding agent: check what it commits, and never paste passwords or keys into prompts.",
  "source_url": "https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026", "source_name": "Together AI",
  "more_sources": [{"label": "Unite.AI", "url": "https://www.unite.ai/together-ai-discloses-prompt-leak-after-coding-agent-exposed-credential/"}]},
 {"id": "google-connected-apps-groceries-taxes", "date": D20, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Google Search and Gemini can now fill your grocery cart at Target, Safeway and Albertsons, and help with credit and taxes",
  "explainer": "If you're in the US, you can now build a grocery order and check out with Target, Albertsons, Safeway or Shaw's right inside Google Search or the Gemini app, check your credit with Experian in Search, and estimate your taxes and refund with H&R Block. Angi and Thumbtack, for finding local repair pros, come to Search in the next few weeks; you link each account yourself, so connect only the ones you want Google to use.",
  "source_url": "https://blog.google/products-and-platforms/products/search/connected-apps-holiday-errands/", "source_name": "Google",
  "x": xb("https://x.com/NewsFromGoogle/status/2123863538078773505", "@NewsFromGoogle", "official", D20)},
 {"id": "meta-muse-marketplace-listings", "date": D20, "category": "feature", "company": "Meta", "impact": "notable",
  "headline": "Muse can turn a photo into a Facebook Marketplace listing, with a cleaned-up picture and a suggested price",
  "explainer": "If you sell things on Facebook Marketplace, send Muse a photo of the item and it makes cleaner versions of the picture, writes the listing and suggests a price from similar items, and nothing goes live until you approve it. Check the price and make sure the edited photos still show the item honestly, because buyers will expect it to look like the picture.",
  "source_url": "https://x.com/Muse/status/2123885256596193297", "source_name": "Muse on X",
  "more_sources": [{"label": "All Things Muse", "url": "https://www.allthingsmuse.com/articles/muse-sell-facebook-marketplace/"}],
  "x": xb("https://x.com/Muse/status/2123885256596193297", "@Muse", "official", D20)},
 {"id": "perplexity-computer-chromium-extension", "date": D20, "category": "feature", "company": "Perplexity", "impact": "notable",
  "headline": "Perplexity's Computer agent now works inside Chrome and other Chromium browsers through its extension",
  "explainer": "If you use Perplexity Computer, you can now hand it a task from the Perplexity extension's side panel in Chrome or another Chromium browser and watch it work across your open tabs and tools. It can act on sites where you're signed in, so consider a separate browser profile without your bank or email logged in; Perplexity didn't say which plans get it.",
  "source_url": "https://www.fathom.news/perplexity-ai-agent-chrome/", "source_name": "Fathom",
  "x": xb("https://x.com/perplexity_ai/status/2123896048510996827", "@perplexity_ai", "official", D20)},
 {"id": "claude-mobile-redesign-computer-use-teams", "date": D20, "category": "feature", "company": "Anthropic", "impact": "notable",
  "headline": "Claude's phone app gets a new design, and Claude can now use desktop apps for Team and Enterprise users",
  "explainer": "If you use Claude on an iPhone, a new look with a bottom bar for chats, Projects, Code and Artifacts is rolling out (it needs iOS 26 or later, Android comes later), with nothing to turn on. Separately, on Team and Enterprise plans Claude can now see your screen and work in the desktop apps you allow, in beta; it stays off until your organization's owner turns it on.",
  "source_url": "https://support.claude.com/en/articles/12138966-release-notes", "source_name": "Claude Help Center",
  "more_sources": [{"label": "The Verge", "url": "https://www.theverge.com/ai-artificial-intelligence/1039188/claude-has-a-new-mobile-design-too"},
                   {"label": "Set up computer use (Team and Enterprise)", "url": "https://support.claude.com/en/articles/18483812-set-up-computer-use-for-team-and-enterprise-plans"}],
  "x": xb("https://x.com/daniel__designs/status/2123860186951516287", "@daniel__designs", "official", D20)},
 {"id": "microsoft-copilot-gpt-6-2", "date": D20, "category": "feature", "company": "Microsoft", "impact": "notable",
  "headline": "Microsoft Copilot adds OpenAI's GPT-6.2 Sol and Astra, including in Word, Excel and PowerPoint",
  "explainer": "If your job gives you Microsoft 365 Copilot, OpenAI's newest GPT-6.2 Sol model is rolling out in Copilot Chat, Cowork, Word, Excel and PowerPoint, and the stronger GPT-6.2 Astra in Copilot Cowork and Copilot Studio. Your IT admin decides which models you get, and Copilot only draws on files and chats you can already open.",
  "source_url": "https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-openais-gpt-6-2-sol-and-gpt-6-2-astra-in-microsoft-copilot/4574229", "source_name": "Microsoft Copilot Blog"},
 {"id": "obsidian-grok-bot-plugin", "date": D19, "category": "feature", "company": "Obsidian", "impact": "notable",
  "headline": "Obsidian releases an official plugin so Grok Bot can create, search and organize notes in your vault",
  "explainer": "If you keep notes in Obsidian, you can add Obsidian's official plugin to Grok Bot so it can create, search and edit notes, fix links, save web pages as notes, and build Bases and Canvas files (the same plugin also works in ChatGPT, Codex and Cursor). Any note the bot reads goes to the AI model, so point it only at a vault you're happy to share.",
  "source_url": "https://obsidian.md/help/skills", "source_name": "Obsidian Help",
  "more_sources": [{"label": "Obsidian skills on GitHub", "url": "https://github.com/obsidianmd/obsidian-skills"}],
  "x": xb("https://x.com/obsdmd/status/2123484964268413341", "@obsdmd", "official", D19)},
]
D = json.load(open('data/news.json')); items = D['items']
have = {i['id'] for i in items}; refreshed = 0
for it in items:
    if it['id'] == 'claude-riemann-hypothesis-claim' and 'Update' not in it['explainer']:
        it['explainer'] += " Update, Nov 21: the Lean and Mathlib communities have now checked the proof and say it is correct (see 'Mathematicians' checking tools confirm...')."
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
