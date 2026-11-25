# Midday trending 2026-11-25: extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-25'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item):
    if item not in lst: lst.append(item)

# People-search removal by a team of agents, re-check every 3 months (X, Nov 25)
add_sources('remove-your-number-from-people-search-sites',[
 {"label":"X post by @ScottyBeamIO (2026-11-25): name, number, email and home address were for sale on 14 people-search sites (parents' address on 9, 2 sites hid the opt-out link); three agents split the job (find the listings, work out each opt-out, file and chase the removal requests), asked once before removing his parents too, and now re-check every 3 months because the sites re-list you (57 likes / 14 replies / 28 bookmarks / 1,118 views, measured 2026-11-25)","url":"https://x.com/ScottyBeamIO/status/2125622785456349645","kind":"x"}])
add(by['remove-your-number-from-people-search-sites']['watch_out'],"It isn't a one-time cleanup. People-search sites can put you back after a few months, so have the bot check again every 3 months, and have it ask before it touches family members' listings (X @ScottyBeamIO, Nov 25).")

# Per-agent email rules in plain English (Product Hunt, Nov 24)
add_sources('keep-hidden-instructions-in-email-from-steering-your-bot',[
 {"label":"Product Hunt launch of Clam AI (2026-11-24, #3 Product of the Day): you connect Gmail to Clam, not to the agent, and write each agent's rules in plain English ('Read flight, hotel and booking emails and build my itinerary. Draft replies to hosts for me to review. Never send.'); everything else is denied, 'ask me first' actions wait for approval, every allowed or blocked action is logged; capped Gmail beta (184 upvotes / 13 comments as shown on hunted.space, checked 2026-11-25)","url":"https://www.hunted.space/product/clam-ai","kind":"article"}])
add(by['keep-hidden-instructions-in-email-from-steering-your-bot']['watch_out'],"Give each bot only the slice of your inbox it needs, in plain words ('read travel emails, draft replies, never send'). Permission tools such as Clam AI (Gmail beta, Nov 24) enforce rules like that and log what each agent tried.")

# Family assistants in one channel; cross-product agents talking (blogs, Nov 24)
add_sources('team-of-agents-with-roles',[
 {"label":"Agent Relay blog, 'Put the Whole Family in One Thanksgiving Channel' by Khaliq Gant (2026-11-24): family members' ChatGPT, Gemini, Muse and Grok Bot join one #thanksgiving channel to sort who brings what, arrival times, dietary needs and the shopping list; Grok Bot and Muse answer @mentions on their own, while ChatGPT and Gemini only see a mention the next time their person asks","url":"https://agentrelay.com/blog/thanksgiving-family-assistants-relay-channel","kind":"article"},
 {"label":"AI with Remy newsletter by Remy Gaskell (2026-11-24): put his Grok Bot 'Chief' and Claude in one OpenPod group chat so Claude can ask his CFO, legal and tax Grok Bots directly; 'it only works one way' because Claude isn't always-on and never replies when a Grok Bot messages first; keeps personal and work agents in separate silos","url":"https://aiwithremy.beehiiv.com/p/i-turned-claude-into-a-clipping-agency","kind":"article"}])
add(by['team-of-agents-with-roles']['watch_out'],"Mixing agents from different apps? Only always-on agents (such as Grok Bot or Muse) reply on their own; chat assistants like ChatGPT, Gemini or Claude only see a message the next time you open them, so don't make them the one others wait on (Agent Relay; AI with Remy, Nov 24).")

# Holiday drive time-zone miss (hands-on test)
add_sources('plan-a-trip-itinerary',[
 {"label":"AIvsTool hands-on test by Alex Chen (2026-11-10): the same Thanksgiving-eve brief (Chicago to Columbus, 355 miles, two kids, a dog, leaving 3:10 p.m. Nov 25) to ChatGPT and Gemini; Gemini's arrival was 2 minutes off the timed drive, ChatGPT's was 1 hour 53 minutes early because it missed the time-zone change and picked toll roads without saying so; ChatGPT wrote the better car packing list","url":"https://aivstool.com/blog/chatgpt-vs-gemini-thanksgiving-drive","kind":"article"}])
add(by['plan-a-trip-itinerary']['watch_out'],"Driving across a time zone? Say so in your prompt and check the arrival time yourself. In one timed Thanksgiving test, ChatGPT's arrival was almost 2 hours early because it ignored the zone change (AIvsTool).")

# Booking-confirmation checks catch real mistakes (GPT Dot use-case page)
add_sources('turn-your-booking-emails-into-one-trip-sheet',[
 {"label":"GPT Dot, 'Can a ChatGPT Dot plan your trips?' (updated 2026-10-17; 54 real trips): the win that repeats most is a dot reading booking confirmations in the inbox and comparing them with the calendar, which caught a stay booked for the wrong month, a hotel booked a year late, a ride to the wrong terminal and two tickets with different bag allowances","url":"https://gptdot.net/use-cases/travel-planner/","kind":"article"}])

json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
