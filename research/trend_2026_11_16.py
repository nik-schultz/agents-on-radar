import json
P='data/use-cases.json'; T='data/tools.json'
u=json.load(open(P)); t=json.load(open(T))
t.setdefault('google-ask-maps',{"name":"Ask Maps (Google Maps)","url":"https://blog.google/products-and-platforms/products/maps/ask-maps-holiday-travel-features-2026/","cost":"Free in the Google Maps app; appointment finding US-only at launch","kind":"agent"})
by={x['slug']:x for x in u}
b=by['book-an-appointment-with-an-ai-agent']
if not any(x['id']=='google-ask-maps' for x in b['tools']):
    b['tools'].insert(1,{"id":"google-ask-maps","note":"Finds open beauty, pet care, auto and home repair slots, checking online or calling nearby businesses for you (US, rolling out Nov 16, 2026)"})
b['setup'] = b.get('setup') or []
s="Google Maps (US): open Ask Maps and ask something like \"Find me a 4 p.m. nail appointment near me.\" Google says it checks online booking or calls local businesses, then shows open slots across nearby places so you pick one. It covers beauty, pet care, auto and home repair, and is rolling out on Android and iOS from Nov 16, 2026."
if s not in b['setup']: b['setup'].append(s)
w="When an AI calls a business for you, it may share your request details with them. Google's help page for its AI price-check calls says your request, which may include your name, is shared with the businesses it calls."
if w not in b['watch_out']: b['watch_out'].append(w)
new=[{"label":"Google blog (2026-11-16): New Ask Maps features for the holidays: find beauty, pet care, auto and home repair appointments online and call local businesses for you (US first)","url":"https://blog.google/products-and-platforms/products/maps/ask-maps-holiday-travel-features-2026/","kind":"official"},
{"label":"Android Authority (2026-11-16): Ask Maps gets itineraries, list search and appointment booking","url":"https://www.androidauthority.com/google-maps-ask-maps-update-3735628/","kind":"article"},
{"label":"Digital Trends (2026-11-16): Google Maps can now organize multi-day trips and call businesses to check appointments","url":"https://www.digitaltrends.com/phones/google-maps-can-now-organize-multi-day-trips-and-call-businesses-to-check-appointments/","kind":"article"},
{"label":"Google Search Help: have AI contact businesses to check availability and prices (shares your request details, which may include your name)","url":"https://support.google.com/websearch/answer/16421135?hl=en","kind":"official"}]
have={x['url'] for x in b['sources']}
b['sources']+= [x for x in new if x['url'] not in have]
b['last_checked']='2026-11-16'
k=by['keep-an-ai-agent-from-deleting-your-files']
w2="It can happen on a tiny job. A University of Chicago law professor asked Claude to renumber pages, and it deleted his whole current syllabus and a year of lecture notes; he got them back only because they were in Dropbox (Tom's Hardware, Nov 2026). Keep anything you hand an agent in a folder with version history or a backup."
if w2 not in k['watch_out']: k['watch_out'].insert(1,w2)
new2=[{"label":"Tom's Hardware (2026-11-06): Claude asked to renumber pages deletes a law professor's syllabus and a year of lecture notes; recovered from Dropbox","url":"https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits","kind":"article"},
{"label":"Hacker News 50499114: \"Claude asked to renumber pages deletes professor's syllabus, year of notes\" (51 points / 75 comments, measured 2026-11-16)","url":"https://news.ycombinator.com/item?id=50499114","kind":"article"}]
have={x['url'] for x in k['sources']}
k['sources']+= [x for x in new2 if x['url'] not in have]
k['last_checked']='2026-11-16'
json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
json.dump(t,open(T,'w'),indent=1,ensure_ascii=False); open(T,'a').write('\n')
print('ok')
