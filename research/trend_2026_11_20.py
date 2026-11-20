# Midday trending 2026-11-20: extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-20'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item,pos=None):
    if item not in lst:
        lst.insert(pos,item) if pos is not None else lst.append(item)

# Delayed flight: bot called the rental-car line so the car was held (X, Nov 20)
add_sources('rebook-a-delayed-flight',[
 {"label":"X post by @therookiehacker (2026-11-20): boarding a badly delayed flight, he realised he'd miss the rental car's 2-hour grace period; Grok Bot called the rental help line, added his flight details to the reservation and confirmed the car would be ready (1 like / 23 views, measured 2026-11-20)","url":"https://x.com/therookiehacker/status/2123627093011386548","kind":"x"}])
w=by['rebook-a-delayed-flight']
add(w.setdefault('watch_out',[]),"Don't forget what's booked at the other end. If you'll land late, have the bot call or message the rental car desk or hotel with your new arrival time, so they don't release the car or room (one Grok Bot user did this from the plane, Nov 20).")

# Purchase approval with a passkey (Grok Bot)
add_sources('pay-with-a-single-use-virtual-card',[
 {"label":"X post by @alexmichael (2026-11-18): 'Grok Bot purchase passkeys are live': before it pays for anything it booked, like flights and hotels, you press Pay and confirm with a passkey in your browser; setup emails you a code, then you save a passkey (219 likes / 14 reposts / 89 bookmarks / 11,063 views, measured 2026-11-20)","url":"https://x.com/alexmichael/status/2123162266530877548","kind":"x"},
 {"label":"Up to Speed with AI: 'Grok Bot now lets you approve purchases with a passkey': confirmed the Passkeys screen (Add Passkey) in the app; a passkey approves purchases only on the device you add it on; no official announcement or help page yet when checked","url":"https://uptospeedwithai.com/whats-new/grok-bot-passkeys/","kind":"article"}])
w=by['pay-with-a-single-use-virtual-card']
add(w['watch_out'],"If your assistant offers a purchase passkey (Grok Bot added one in November 2026), turn it on: every purchase then waits for your fingerprint or face on your own device. It works alongside a one-time card, not instead of it.")

# Booking/rescheduling appointments by phone with a 'Clinic Desk' bot
add_sources('book-an-appointment-with-an-ai-agent',[
 {"label":"X post by @lukesammons (2026-11-20): his Grok Bot 'Clinic Desk' made 8+ calls to 4 clinics in two weeks to book, confirm and reschedule family doctor, dentist, blood-test and orthopedic appointments, then passed them to his chief-of-staff bot, which put them on his iOS calendar (1 like / 26 views, measured 2026-11-20)","url":"https://x.com/lukesammons/status/2123587073202647177","kind":"x"}])

# X-only -> add non-X sources
add_sources('prescription-ready-and-time-to-leave',[
 {"label":"Gemini Apps Help: Create & manage schedules for tasks in Gemini: 'Gmail monitors' run a task whenever an email matching a Gmail filter arrives (use one for 'ready for pickup' emails); schedules can run daily at a set time","url":"https://support.google.com/gemini/answer/17094710?co=GENIE.Platform%3DDesktop&hl=en","kind":"official"},
 {"label":"Engadget, '5 clever ways Gemini can automate everyday tasks' (2026-10-13): schedule Gemini to check your calendar and 'estimate total travel and driving time using Maps every morning at 7:30AM'; it may not use real-time traffic, so check the route in Maps before you leave","url":"https://www.engadget.com/2282226/clever-ways-gemini-automate-everyday-tasks/","kind":"article"}])
w=by['prescription-ready-and-time-to-leave']
add(w.setdefault('watch_out',[]),"Gemini's scheduled travel-time check may not use live traffic (Engadget, Oct 2026), so treat 'leave now' as a heads-up and glance at Maps before you go.")

# New-package entry pairs with the holiday-shopping watch-out
json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
