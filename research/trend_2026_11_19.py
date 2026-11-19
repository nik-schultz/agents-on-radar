# Midday trending 2026-11-19: extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-19'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item,pos=None):
    if item not in lst:
        lst.insert(pos,item) if pos is not None else lst.append(item)

# Contractors: Grok Bot called contractors, collected bids, booked the pick (BACKLOG 2026-11-18 item, original post found)
c=by['line-up-contractors-for-a-home-project']
add_sources('line-up-contractors-for-a-home-project',[
 {"label":"X post by @thecsguy (2026-11-17): 'had my grok bot call contractors for bids today. it negotiated with each one of them, brought me a pick and a price, then booked my choice on a day it knew i'd be home' (31 likes, 1 repost, 7 replies, 3 bookmarks, 2,078 views; measured 2026-11-19)","url":"https://x.com/thecsguy/status/2122828378478887268","kind":"x"},
 {"label":"The Agent Field newsletter (2026-11-18): 'Grok Bot got contractor bids and booked one': the bot phoned contractors, came back with a pick and a price, then booked the choice for a day the calendar showed he'd be home; check the contractor's licence on your state board's site before work starts","url":"https://theagentfield.beehiiv.com/p/grok-bot-got-contractor-bids-and-booked-one-plus-4-more-use-cases","kind":"article"}])
c['popularity']={"platform":"x","post_id":"2122828378478887268","author":"@thecsguy","url":"https://x.com/thecsguy/status/2122828378478887268","posted_at":"2026-11-17","likes":31,"reposts":1,"replies":7,"bookmarks":3,"views":2078,"measured_at":M}
c['summary']="Instead of calling round electricians, plumbers and roofers yourself, let an agent reach out to all of them (by message or, with Grok Bot or Muse, by phone), collect their prices and put them side by side. You pick, and it can book the one you chose."
add(c['what_the_bot_does'],"Once you pick one, books the visit on a day your calendar shows you're home, and tells you what was agreed.")
c.setdefault('setup',[])
add(c['setup'],"Write a short brief first: the job, your address area, when you're free, photos if you have them, and the questions every contractor must answer (the source pre-agreed his questions before the calls).")
add(c['setup'],"With Grok Bot or Muse you can ask it to phone each business for a price instead of messaging. Approve the list of numbers before it dials.")
add(c['setup'],"Ask for a table of the bids, pick one yourself, then let it call back to book. Check the date it booked against your calendar.")
add(c['watch_out'],"Tell the bot what it may agree to. A bot that 'negotiates' should only ask for prices and dates, not accept terms, pay a deposit or sign anything.")
add(c['tags'],"phone calls"); add(c['tags'],"bids")

# Customer-service call: Muse made the call and patched the user in when a PIN was needed
s=by['make-a-customer-service-call']
add_sources('make-a-customer-service-call',[
 {"label":"X post by @poetnchief (2026-11-17): Muse made a call to Spectrum, then called him and connected him to the call when they needed his 4-digit PIN; he finished the last 6 minutes himself (0 likes, 52 views; measured 2026-11-19)","url":"https://x.com/poetnchief/status/2122744123597967615","kind":"x"}])
add(s['setup'],"If the company will ask for a PIN or security answer, tell the bot to bring you in at that point rather than handing it the code. One Muse user says it called him and connected him to the call when the PIN was needed.")

# Weekend activities: Dot suggested a nearby family event unprompted; r/AI_Agents user runs a daily local-events itinerary agent
w=by['weekend-family-activities']
add_sources('weekend-family-activities',[
 {"label":"X post by @RealDavidIsrael (2026-11-19): 'My Dot just messaged me randomly telling me it found a family event nearby that I may be interested in. I hadn't asked it to do so.' (0 likes, 35 views; measured 2026-11-19)","url":"https://x.com/RealDavidIsrael/status/2123433284579316204","kind":"x"},
 {"label":"Reddit r/AI_Agents, 'What's your actual daily workflow with AI agents?' (Oct 2026): a commenter runs 'a daily agent that crawls my local area and aggregates all the events and things to do in a single itinerary'","url":"https://www.reddit.com/r/AI_Agents/comments/1x3vm1c/whats_your_actual_daily_workflow_with_ai_agents/","kind":"reddit"}])
w.setdefault('setup',[])
add(w['setup'],"Ask your assistant to run this every Thursday or Friday on a schedule (a scheduled task, routine or recurring Gemini task), so the ideas arrive before you've made plans.")
add(w['setup'],"Some assistants (ChatGPT Dots, for example) may suggest nearby events on their own once they know your town and your kids' ages. Tell it how often you want that, so it doesn't turn into noise.")

# X-only -> add a non-X source
add_sources('give-your-agents-a-shared-apple-account',[
 {"label":"Reddit r/AI_Agents, u/supermario218 (Nov 2026): connected the Grok app's Mac access to Reminders, Calendar, Contacts and Messages and made a bot ('Siri 2.0') that handles his iCloud items and coordinates with his other bots to set reminders","url":"https://www.reddit.com/r/AI_Agents/comments/1xvs8tr/what_im_doing_with_my_ai_agents_as_a_normal_person/","kind":"reddit"}])
add_sources('one-bot-per-brand',[
 {"label":"SpaceXSI (2026-11-17), 'Building an accounting team with Grok Bot': five Bots, each owning one scoped job with its own operating manual and permissions, handing work to each other (for example Collections Bot works with Billing and Cash Applications Bots on refunds)","url":"https://x.ai/news/grok-bot-accounting","kind":"official"}])
json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
