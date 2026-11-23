"""Nov 23 PM news run: add 9 items dated Nov 23, refresh X numbers for items dated since Nov 13.
Raw response: research/x_news_measure_2026_11_23_pm.json.txt (local only)."""
import json
RAW = 'research/x_news_measure_2026_11_23_pm.json.txt'
MEASURED = '2026-11-23T20:28:00Z'
txt = open(RAW).read(); txt = txt[txt.index('{"data"'):]
raw, _ = json.JSONDecoder(strict=False).raw_decode(txt)
pm = {p['id']: p['public_metrics'] for p in raw['data']}
print('measured', len(pm))
def xb(url, author, kind, posted):
    pid = url.rsplit('/', 1)[1]; m = pm[pid]
    return {"url": url, "author": author, "kind": kind, "likes": m['like_count'], "reposts": m.get('repost_count', m.get('retweet_count')),
            "views": m['impression_count'], "posted_at": posted, "measured_at": MEASURED}
D = "2026-11-23"
new = [
 {"id": "chatgpt-gpt-6-2-chat-tab", "date": D, "category": "model release", "company": "OpenAI", "impact": "notable",
  "headline": "ChatGPT's everyday Chat tab gets GPT-6.2, better at photos, detailed requests and comparing options online",
  "explainer": "If you pay for ChatGPT Plus, Pro, Business or Enterprise, the normal Chat tab is switching to a version of GPT-6.2 Sol over the coming days, so it should follow long, detailed requests better, read photos more accurately and weigh options like hotels by your priorities; there's nothing to turn on. OpenAI's own tests show big gains over GPT-6 (image questions 71.7% vs 47.4%), and it may now offer to tell you when a price drops; Free and Go plans and the Work and Codex models aren't part of this update.",
  "source_url": "https://help.openai.com/en/articles/6825453-chatgpt-release-notes", "source_name": "ChatGPT release notes",
  "more_sources": [{"label": "GPT-6.2 in ChatGPT system card", "url": "https://deploymentsafety.openai.com/gpt-6-2-chatgpt/gpt-6-2-chatgpt.pdf"},
                   {"label": "Exame", "url": "https://exame.com/inteligencia-artificial/chatgpt-gpt-6-2-sol-aba-chat/"}],
  "x": xb("https://x.com/ChatGPT/status/2124942186425069836", "@ChatGPT", "official", D)},
 {"id": "walmart-agent-gateway-muse-live", "date": D, "category": "agent launch", "company": "Walmart", "impact": "notable",
  "headline": "Muse can now shop Walmart's Black Friday deals for you, with a spending limit you set",
  "explainer": "If you use Meta's Muse, you can ask it to find Walmart deals, build a cart and check out in the chat with a card saved in your Walmart account, after you sign in to Walmart and set a spending limit in a new Agent Profile. You can approve purchases and see everything Muse bought there, prices match Walmart.com and normal returns apply; Walmart says other assistants are 'on the way' but only Muse works today.",
  "source_url": "https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday", "source_name": "The Verge",
  "more_sources": [{"label": "Unite.AI", "url": "https://www.unite.ai/walmart-enables-muse-shopping-through-its-agent-gateway/"},
                   {"label": "Walmart (Oct 21 announcement)", "url": "https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers"}],
  "x": xb("https://x.com/verge/status/2124821529750032710", "@verge", "coverage", D)},
 {"id": "claude-ship-pr-agents", "date": D, "category": "agent launch", "company": "Anthropic", "impact": "notable",
  "headline": "Anthropic launches Claude Ship: Claude reviews code changes, fixes what's blocking them and can approve routine ones",
  "explainer": "If your company's software team uses Claude Team or Enterprise with GitHub, Claude can now take a code change from review to fixes (failing tests, merge conflicts, reviewer comments) and, if your team's rules allow, approve routine changes itself. The two new agents, PR Steward and Claude Approvals, are in beta; teams decide what counts as 'routine', and riskier changes still go to a person.",
  "source_url": "https://www.theverge.com/ai-artificial-intelligence/1040134/anthropic-claude-ship-ai-pull-requests", "source_name": "The Verge",
  "more_sources": [{"label": "CNA (Reuters)", "url": "https://www.channelnewsasia.com/business/anthropic-launches-claude-ship-help-developers-ship-code-faster-6575946"},
                   {"label": "Numerama", "url": "https://www.numerama.com/tech/2382945-anthropic-lance-claude-ship-un-outil-qui-veut-valider-votre-code-a-la-place-de-vos-collegues.html"}],
  "x": xb("https://x.com/ClaudeDevs/status/2124959436640858475", "@ClaudeDevs", "official", D)},
 {"id": "google-ai-mode-wallet-personal-intelligence", "date": D, "category": "feature", "company": "Google", "impact": "notable",
  "headline": "Google's AI Mode can now use your Google Wallet spending, with Drive and the Gemini app coming next",
  "explainer": "If you use AI Mode in Google Search, you can now opt in to connect Google Wallet so it can suggest ways to trim spending and get more from your card rewards; Google says it can only read your accounts, not move money. Drive and your Gemini app chats can be connected in the coming weeks; turn each one on in Search Personalization > Connected Apps only if you want Search to see it.",
  "source_url": "https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/", "source_name": "Google",
  "x": xb("https://x.com/rmstein/status/2124933562918908333", "@rmstein", "official", D)},
 {"id": "openai-openworks-small-business", "date": D, "category": "industry", "company": "OpenAI", "impact": "notable",
  "headline": "OpenAI's OpenWorks pays local AI experts to help small businesses for free, plus 3 months of ChatGPT Business",
  "explainer": "If you own an independent US small business, such as a shop, restaurant or service firm, you can apply to OpenWorks for free one-on-one help from a local AI expert on a project you pick, plus 3 months of ChatGPT Business at no cost. The pilot covers 20 cities so far (including Chicago, Kansas City, St. Louis, Austin and Houston); software, venture-backed and private-equity-owned firms can't join, and experts can apply for a stipend of up to $8,000 a month.",
  "source_url": "https://openai.com/openworks/", "source_name": "OpenAI",
  "more_sources": [{"label": "Tech Startups", "url": "https://techstartups.com/2026/11/23/openai-to-pay-ai-experts-up-to-8000-a-month-to-help-small-businesses-adopt-ai/"}],
  "x": xb("https://x.com/OpenAI/status/2124922133545714160", "@OpenAI", "official", D)},
 {"id": "grok-oregon-virginia-lawsuits", "date": D, "category": "industry", "company": "xAI", "impact": "notable",
  "headline": "Oregon and Virginia sue SpaceX over sexual deepfakes made with Grok",
  "explainer": "Nothing changes in Grok or Grok Bot today, but two US states are suing SpaceX, which owns X and Grok, saying it marketed Grok as safe while it let people make sexual images of real people without consent, including of children. The states want court orders and fines; SpaceX's X Safety team says it acts on accounts that try this and reports them to police.",
  "source_url": "https://www.doj.state.or.us/media-home/news-media-releases/ag-rayfield-takes-legal-action-against-grok-for-failing-to-block-child-exploitation/", "source_name": "Oregon Department of Justice",
  "more_sources": [{"label": "CNBC", "url": "https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html"},
                   {"label": "AP", "url": "https://apnews.com/article/grok-lawsuit-elon-musk-ai-abuse-images-452cc64e7169a55868f797982d0e8238"},
                   {"label": "X Safety statement", "url": "https://x.com/Safety/status/2124853016377397403"}],
  "x": xb("https://x.com/CNBC/status/2124846393089012085", "@CNBC", "coverage", D)},
 {"id": "mistral-vibe-pro-free-month-europe", "date": D, "category": "pricing", "company": "Mistral", "impact": "minor",
  "headline": "Mistral gives everyone in Europe a free month of Vibe Pro, with no cap this time",
  "explainer": "If you're in Europe, you can get a month of Mistral's Vibe Pro free with the code MISTRALVIBE; last week's capped trial ran out in under an hour, and Mistral says this one has no limit. Coverage says you add a payment method to redeem it, so set a reminder to cancel if you don't want it to renew.",
  "source_url": "https://x.com/MistralAI/status/2124905610386780451", "source_name": "Mistral AI on X",
  "more_sources": [{"label": "mydealz", "url": "https://www.mydealz.de/deals/gratis-mistral-vibe-pro-1-monat-kostenlos-fur-entwickler-in-europa-code-mistralvibe-2879842"}],
  "x": xb("https://x.com/MistralAI/status/2124905610386780451", "@MistralAI", "official", D)},
 {"id": "claude-zero-retention-safeguards-beta", "date": D, "category": "feature", "company": "Anthropic", "impact": "minor",
  "headline": "Anthropic opens a public beta that lets businesses keep zero data with Anthropic while still getting misuse checks",
  "explainer": "Nothing changes in the Claude app for individuals: businesses on the Claude Platform, Amazon Bedrock or Google Cloud can now join a beta where prompts and replies are stored only in their own cloud storage, while Anthropic's automated system still looks for misuse across many requests. Anthropic says nobody at Anthropic or the cloud provider reads the data and it isn't used for training; eligible customers get an invite.",
  "source_url": "https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards", "source_name": "Claude",
  "x": xb("https://x.com/claudeai/status/2124929944530587712", "@claudeai", "official", D)},
 {"id": "gemini-api-file-slicing", "date": D, "category": "feature", "company": "Google", "impact": "minor",
  "headline": "Gemini API can now read just the pages, cells or clip of a file you ask for, and bills only that part",
  "explainer": "If you build a bot on the Gemini API, you can upload a PDF, Office file, spreadsheet, audio or video once and ask Gemini to look at only certain pages, cells or minutes, paying tokens just for what it inspects. It works with all Gemini 4 models and adds Word, PowerPoint and OpenDocument uploads; prices per token don't change.",
  "source_url": "https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/", "source_name": "Google",
  "x": xb("https://x.com/GoogleAIStudio/status/2124928707529674979", "@GoogleAIStudio", "official", D)},
]
Dd = json.load(open('data/news.json')); items = Dd['items']
have = {i['id'] for i in items}; add = [n for n in new if n['id'] not in have]
refreshed = 0
for it in items:
    x = it.get('x')
    if not x: continue
    pid = x['url'].rsplit('/', 1)[1]
    if pid in pm:
        m = pm[pid]; x.update(likes=m['like_count'], reposts=m.get('repost_count', m.get('retweet_count')), views=m['impression_count'], measured_at=MEASURED); refreshed += 1
items[:0] = add
items.sort(key=lambda i: i['date'], reverse=True)
json.dump(Dd, open('data/news.json', 'w'), indent=1, ensure_ascii=False); open('data/news.json','a').write('\n')
print('added', len(add), 'refreshed existing', refreshed)
