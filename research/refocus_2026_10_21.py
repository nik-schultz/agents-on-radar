"""One-off edit (2026-10-21): refocus kept entries on the agent's action, not savings.
The archive step (11 money guides, Money category, bill blueprint -> data/archive/) ran before this script."""
import json
P='data/use-cases.json'; u=json.load(open(P)); U={x['slug']:x for x in u}
def setf(_s, **kw):
    x=U[_s]
    for k,v in kw.items(): x[k]=v
    x['last_checked']='2026-10-21'
# 1 phone call
x=U['cancel-a-subscription-by-phone']
setf('cancel-a-subscription-by-phone', slug='make-a-customer-service-call', category='inbox',
  title='Have your bot make a customer-service phone call for you',
  summary='Some jobs still need a phone call, like cancelling a service or sorting out an account. With a phone-calling add-on, your bot can make the call, sit on hold and report back.',
  what_you_end_up_with='The call handled (for example, a service cancelled), a plain summary of what was said and any confirmation number, without you sitting on hold.',
  tags=['phone call','customer service','hold music','cancel a service','calling agent'])
x['what_the_bot_does']=["Gets a phone number of its own through a calling add-on you connect.","Looks up the company's customer-service line and the account details it will need.","Calls, says up front that it's an AI assistant calling for you, and asks for exactly what you said (in the shared example, cancelling a streaming service).","Sticks to your rules: it turns down offers and agrees to nothing you didn't approve.","Tells you what was said and saves any confirmation number."]
x['watch_out']=[w if not w.startswith('Check your next statement') else "Check afterwards that the change really happened (for example, the next charge doesn't appear)." for w in x['watch_out']]
x['prompt']=x['prompt'].replace("Turn down any discount or pause offer unless it's [what you'd accept]. Don't agree to anything that costs money.","Turn down any offers unless it's [what you'd accept], and don't agree to anything else.")
# 2 mail
x=U['mail-to-bill-pay-with-anomaly-alerts']
setf('mail-to-bill-pay-with-anomaly-alerts', slug='sort-scanned-paper-mail-with-alerts', category='inbox',
  title='Have a bot sort your scanned paper mail and flag what needs you',
  summary='A virtual mailbox service scans your paper mail to email. The bot reads every letter, queues up the routine ones for your OK, and pulls you in only when something looks unusual.',
  what_you_end_up_with='Your paper mail read and sorted, routine items queued for one quick approval, and only the unusual ones in front of you.',
  tags=['paper mail','virtual mailbox','scanning','alerts','admin'])
x['what_the_bot_does']=['A virtual mailbox service opens and scans your paper mail to PDF.','The bot reads each scanned letter in your email.','Sorts it: routine (like a usual monthly payment), needs a reply, or just information.','Compares routine items with past ones and flags anything unusual (the person who shared this uses "more than 20% different").','Queues routine items for your OK and messages you about the rest.']
x['prompt']="Each time a scanned letter arrives in my email from [mail service], read it and add it to my mail log: sender, what it is, any due date, what it asks me to do. If it's a routine item I've approved before, compare it with the last 3 from that sender. If it's more than 20% different, or the sender is new, stop and message me. Otherwise add it to my 'ready to approve' list. Do not pay, reply or sign anything until I approve."
x['watch_out']=["Start by approving every action. Only loosen that once you trust it.","Scanned mail contains account numbers and personal details. Use tools you trust with that data.","The person who shared this adds his own caveats about the hype; read the full post."]
x['sources'][0]['label']='X post by @mikekamo (2026-09-23): Claude reads scanned paper mail, handles routine items and flags anything more than 20% different'
# 3 web page
x=U['watch-a-web-page-for-changes']
setf('watch-a-web-page-for-changes', title='Have a bot watch any web page and ping you when it changes',
  tags=['monitoring','alerts','restock','new listing','appointment slot'])
x['what_the_bot_does'][0]='Takes a link and what you care about, like a restock, a new listing or an appointment slot opening.'
x['tools']=[t for t in x['tools'] if t['id']!='google-universal-cart']
x['prompt']="Watch this page: [link]. What matters: [back in stock / new listing / appointment slot opens / status or policy change]. Check it [every morning]. Message me only when that changes, with the old and new value and the link. Don't buy, book or sign up for anything."
# 4 airline
x=U['catch-airline-schedule-changes']
setf('catch-airline-schedule-changes', title='Get alerted the moment your airline changes your flight',
  summary='Airlines quietly move flight times. An agent watching your inbox spots the change, tells you what moved, and lays out your options.',
  what_you_end_up_with="An alert when your flight changes, your options under the airline's rules, and a request drafted for whichever one you pick.",
  tags=['flights','schedule change','alerts','inbox monitoring'])
x['what_the_bot_does']=['Watches your email for airline itinerary changes.','Compares the new times with your original booking.',"Checks the airline's rules for what you can do: keep it, rebook, or cancel.",'Drafts the rebooking or cancellation request for you to approve.']
x['prompt']="Watch my email for any message from an airline about a schedule change, a time change or a cancellation. When you find one, tell me the old and new times and the size of the change, and check that airline's published rules for my options (keep, rebook, cancel). Draft the request for the option I pick, but don't change or cancel anything without my OK."
x['watch_out']=['Cancelling may give up your seat. Decide before you send anything.',"WIRED's reviewer says her agent caught a 90-minute change she had missed."]
# 5 misc
setf('pay-with-a-single-use-virtual-card', category='shopping', title='Give your agent a single-use card before it books or buys anything')
setf('plan-a-trip-itinerary', title='Plan a trip itinerary that fits your pace')
setf('test-a-side-hustle-idea', title='Test a side hustle idea before you commit')
setf('write-a-complaint-that-gets-fixed', category='inbox')
x=U['hand-your-most-hated-chores-to-a-personal-agent']
x['prompt']=x['prompt'].replace("check my email for bills due next week and list them","check my email for school forms and deadlines due next week and list them")
assert not [x for x in u if x['category']=='money']
json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
h=open('data/popularity-history.jsonl').read().replace('"cancel-a-subscription-by-phone"','"make-a-customer-service-call"').replace('"mail-to-bill-pay-with-anomaly-alerts"','"sort-scanned-paper-mail-with-alerts"')
open('data/popularity-history.jsonl','w').write(h)
c=json.load(open('data/categories.json'))
for x in c:
    if x['slug']=='inbox': x['name']='Inbox, calls & paperwork'; x['blurb']='Email, phone calls, letters, forms and the admin that piles up.'
    if x['slug']=='shopping': x['blurb']='Meal plans, grocery carts, restocks and errands your agent can run.'
json.dump(c,open('data/categories.json','w'),indent=1,ensure_ascii=False)
print('ok', len(u))
