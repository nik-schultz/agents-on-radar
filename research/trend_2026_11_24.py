# Midday trending 2026-11-24: extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-24'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item):
    if item not in lst: lst.append(item)

# Agents from different products coordinating over email (X, Nov 23)
add_sources('team-of-agents-with-roles',[
 {"label":"X post by @michaelhyunkim (2026-11-23): a user connected three personal agents from three different products and let them coordinate over email; one audited another's backup instructions and caught outdated tasks and a wrong date, and they agreed 'a handoff doesn't count until the receiving agent explicitly acknowledges it' (30 likes / 8 replies / 14 bookmarks / 714 views, measured 2026-11-24)","url":"https://x.com/michaelhyunkim/status/2124914421549949292","kind":"x"}])
add(by['team-of-agents-with-roles']['watch_out'],"Handoffs get lost. Make it a rule that a job only moves when the receiving agent says it got it, and have one agent check the others' instructions for old tasks and wrong dates (X @michaelhyunkim, Nov 23).")

# Bots re-reading their own long chats (X, Nov 24)
add_sources('keep-prompts-and-context-short',[
 {"label":"X post by @DaveMiz (2026-11-24): hit his Grok Bot weekly limit 3 weeks running; the usage CSV showed the average call re-read 95k tokens of chat history. Fix: each bot keeps a 300-word note (its job, his decisions, open work), and a bot whose chat passes 100k is restarted with an empty chat that reads the note (1 like / 85 views, measured 2026-11-24)","url":"https://x.com/DaveMiz/status/2125052646499156293","kind":"x"}])
add(by['keep-prompts-and-context-short']['watch_out'],"Long-running bots re-read their whole chat every time. If you keep hitting your limit, have each bot keep a short note of its job and your decisions, and start it a fresh chat that reads the note (X @DaveMiz, Nov 24).")

json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
