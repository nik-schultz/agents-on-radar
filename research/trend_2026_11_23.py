# Midday trending 2026-11-23: extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-23'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item):
    if item not in lst: lst.append(item)

# Fax entry: the X post was deleted (get_posts_by_ids: Not Found, 2026-11-23). Drop it and clear popularity.
f=by['have-your-bot-fax-an-office-that-wont-answer']
f['sources']=[s for s in f['sources'] if '2122741428543463744' not in s['url']]
f['popularity']=None; f['last_checked']=M

# Local news digest (X, Nov 21)
add_sources('morning-news-digest',[
 {"label":"X post by @lalovestrump (2026-11-21): has Grok Bot search for local news and new businesses opening in her area and send updates every morning or night: 'It's kind of like a personalized local newsletter' (11 likes / 9 replies / 847 views, measured 2026-11-23)","url":"https://x.com/lalovestrump/status/2124262215348027882","kind":"x"}])
add(by['morning-news-digest']['watch_out'],"Want local news? Name your town and the kinds of things you care about (new shops, road closures, school news), and ask for links to the local paper or city site, so you can check anything it found.")

# Phone booking: venue ring-round (non-X write-up) + ring-round guide
add_sources('call-and-book-by-phone',[
 {"label":"Agents In Use (2026-11-16): Grok Bot called 5 venues for company Christmas party dates and prices, showed a side-by-side comparison, then called the chosen venue back and booked it (source @LucasImpLLC; no deposit or contract described)","url":"https://agentsinuse.com/use-cases/grok-bot-calls-five-venues-books-christmas-party/","kind":"article"},
 {"label":"Usecasy: 'Have your AI bot phone a company for you' (updated 2026-11-22): call-brief prompt with what the bot may and must never agree to, plus a ring-round prompt for several shops","url":"https://usecasy.com/use-case/grokbot-phone-company-for-you/","kind":"article"}])
add(by['call-and-book-by-phone']['watch_out'],"Booking a party or event? Have it collect dates and prices from every venue first, pick one yourself, then let it call back to book. Don't let it agree to a deposit or contract on the phone.")

json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
