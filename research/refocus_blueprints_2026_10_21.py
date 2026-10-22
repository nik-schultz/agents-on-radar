"""One-off (2026-10-21): agentic refocus of blueprints. Bill & Subscription Watchdog was archived to data/archive/blueprints-money.json."""
import json
P='data/blueprints.json'; b=json.load(open(P)); B={x['slug']:x for x in b}
w=B['price-drop-watcher']
w.update(slug='web-page-watcher', title='Web Page Watcher',
  goal='Get one ping when a page you care about changes (a restock, a new listing, an appointment slot, a status update) and stop refreshing it yourself.',
  trigger='Every morning at 8:00am (or every few hours for time-sensitive pages)',
  watches='The web pages you give it',
  steps=['You paste links and say what matters on each one (back in stock, new listing, slot opens, status changes).',"The bot saves how each page looks today.",'It re-checks on schedule.','It messages you only when something you care about changes, with the old and new value and the link.'],
  tools=[{'id':'grok-bot','how':'Routine that checks the pages on a schedule'},{'id':'chatgpt-dots','how':'Ask it to keep watching'},{'id':'make','how':'No-code scheduled page check'}],
  instructions="You are my Page Watcher bot.\nWatch these pages:\n- [link 1]: tell me when [it's back in stock / a new listing appears / an appointment slot opens / the status changes]\n- [link 2]: tell me when [what matters]\nEvery morning at 8:00am, check each page. Only message me when something I asked about changes. Include the old value, the new value and the link.\nRules: never buy, book or sign up for anything, never create accounts, never enter my details.",
  safety=['Watching is safe; acting on what it finds is a separate decision you make.',"Some sites block bots. If checks keep failing, use the site's own alerts instead."],
  related=['watch-a-web-page-for-changes','catch-airline-schedule-changes','watch-for-one-important-letter'],
  sources=[{'label':'X: a Grok bot that watches pages and pings only on change','url':'https://x.com/teeRex247/status/2111981455077466525'}])
t=B['travel-day-guardian']
t['goal']=t['goal'].replace('with options and a refund request ready','with your options and a request ready to send')
t['steps']=[s.replace('Drafts a refund or rebooking request for your OK.','Drafts a rebooking or cancellation request for your OK.') for s in t['steps']]
for s in t['sources']:
    if '$550' in s['label']: s['label']='WIRED: Instinct caught a 90-minute schedule change the reviewer had missed'
phone={'slug':'phone-call-bot','title':'Phone Call Bot','art':'cat-work','difficulty':'Medium','setup_time':"About 20 minutes once a calling add-on is connected (editor's estimate)",
 'goal':'Hand off the phone calls you keep putting off: booking a table, a vet visit or a haircut, or a quick customer-service call.',
 'trigger':'Only when you ask it to (never on its own)',
 'watches':'Nothing. It waits for your request, then makes one call at a time',
 'steps':['You say who to call and what you want, for example "book Gourmet Italia, 4 people, tonight around 7".',"It finds the number, asks you for anything missing (name, flexibility, callback number) and reads the plan back.",'It waits for your OK, then calls and says it is an AI assistant calling for you.','After the call it tells you what happened in plain English, quotes what the other side said, and offers to add it to your calendar.'],
 'tools':[{'id':'grok-bot','how':'Needs a phone-calling add-on connected so the bot has its own number (the shared example used one with a free starter tier)'},{'id':'meta-muse','how':'Can call businesses for you'},{'id':'instinct','how':'Messages or calls small businesses'}],
 'instructions':"You are my Phone Call bot.\nWhen I ask you to call somewhere:\n1. Find the business's official phone number.\n2. Ask me for anything you need: name to use, callback number, how flexible I am, what you may agree to.\n3. Read the whole plan back and wait for my OK before you dial.\n4. Start the call by saying you're an AI assistant calling on behalf of [my name].\n5. Get what I asked for, and agree to nothing else. Never give card or deposit details, never leave a voicemail unless I said so, one call at a time.\n6. Afterwards, tell me what happened, quote what they said, give me any confirmation number, and offer to add it to my calendar.",
 'safety':['A phone call is harder to undo than an email. Be specific about what it may agree to.','Have it say it\'s an AI right away. One user says a restaurant owner almost hung up until it did.','Some companies only act for the account holder, so some calls will still need you.','Never let it share card numbers or deposit details on a call.'],
 'related':['call-and-book-by-phone','make-a-customer-service-call','restaurant-reservations-by-agent'],
 'sources':[{'label':'X post by @BrianRoemmele (2026-10-18): a Grok Bot that calls a restaurant and books the table, with its guardrails','url':'https://x.com/BrianRoemmele/status/2111812467500458135'},{'label':'X post by @skeptrune (2026-10-20): Grok Bot making a real customer-service call with a phone-calling add-on','url':'https://x.com/skeptrune/status/2112563230019289456'},{'label':'X post by @james_fowler_ (2026-10-18): a restaurant owner nearly hung up until the bot said it was an AI','url':'https://x.com/james_fowler_/status/2111888527826813404'}]}
i=[x['slug'] for x in b].index('web-page-watcher')
b.insert(i+1, phone)
json.dump(b,open(P,'w'),indent=1,ensure_ascii=False)
print([x['slug'] for x in b])
