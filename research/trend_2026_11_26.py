# Midday trending 2026-11-26 (Thanksgiving): extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-26'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item):
    if item not in lst: lst.append(item)

# Always-on agent teams with shared memory (Product Hunt #1, Nov 25) + one agent per project with a chief of staff (X, Nov 25)
add_sources('team-of-agents-with-roles',[
 {"label":"Product Hunt launch of MyClaw 3.0 (2026-11-25, #1 Product of the Day): build an always-on AI team from OpenClaw, Claude Code, Codex, Hermes Agent and others; each teammate gets its own role, tools and model, with shared memory across the team, and you assign work from the web, Slack, Telegram or WhatsApp (334 upvotes / 61 comments as shown on hunted.space, checked 2026-11-26)","url":"https://hunted.space/product/myclaw-3-0","kind":"article"},
 {"label":"X post by @leodev (2026-11-25): one agent ('captain') per project (SEO, newsletter, content, benchmarks, SDKs) plus a chief-of-staff agent that coordinates changes to how the others reply and handles big multi-project requests; 'use folders... without folders [it] turns into a complete mess' (250 likes / 14 reposts / 18 replies / 316 bookmarks / 22,799 views, measured 2026-11-26)","url":"https://x.com/leodev/status/2125653751935709627","kind":"x"}])
add(by['team-of-agents-with-roles']['watch_out'],"Give each agent one project or one job, and one 'chief of staff' agent that owns the shared rules. Teams that mix many jobs in one agent, or skip folders, get messy fast (X @leodev, Nov 25).")

# Proactive chief of staff that texts you first, approvals in WhatsApp/iMessage (Product Hunt #2, Nov 25)
add_sources('hire-a-chief-of-staff-bot',[
 {"label":"Product Hunt launch of Airbot, 'The AI chief of staff that texts you first' (2026-11-25, #2 Product of the Day): checks email, Slack, calendar and CRM, messages you only the priorities, with the work already prepared (a drafted reply, a meeting brief, a booking, a CRM change) for you to approve in WhatsApp or iMessage (294 upvotes / 64 comments as shown on hunted.space, checked 2026-11-26)","url":"https://hunted.space/product/airbots","kind":"article"}])
add(by['hire-a-chief-of-staff-bot']['watch_out'],"A chief-of-staff bot that 'texts you first' is only safe if every prepared action waits for your approval. Approving from WhatsApp or iMessage is quick, so read the draft before you tap yes (Airbot, Product Hunt Nov 25).")

# Phone-call assistants: accessibility angle (Product Hunt, Nov 25) + a business that hung up on the AI (X, Nov 26)
add_sources('call-and-book-by-phone',[
 {"label":"Product Hunt launch of Hai, 'Your AI assistant that actually makes the phone call' (2026-11-25, #8 of the day): built for bookings that only happen by phone and for people who are deaf, hard of hearing, or have speech or anxiety barriers; you approve the plan, it calls any business in any language and reports back in text; also offered as an MCP server (108 upvotes / 16 comments as shown on hunted.space, checked 2026-11-26)","url":"https://www.hunted.space/product/hai-4","kind":"article"},
 {"label":"X post by @AmineTX (2026-11-26, Thanksgiving Eve): garage-door spring snapped; his Grok Bot found repair companies and called two; 'the first hung up the moment it realized it was talking to an AI', the second stayed on and booked a last-minute job (5 likes / 4 replies / 318 views, measured 2026-11-26)","url":"https://x.com/AmineTX/status/2125780764285383087","kind":"x"}])
add(by['call-and-book-by-phone']['watch_out'],"Some businesses hang up when they realise an AI is calling. For anything urgent, have the bot line up two or three places to call, and confirm the price before it books (X @AmineTX, Nov 26).")

# Event-driven instead of polling (X, Nov 24)
add_sources('schedule-bots-without-burning-tokens',[
 {"label":"X post by @irongiantXBT (2026-11-24): one 'router' plus 4 specialist Grok Bot agents that wake only when an event (email, Slack, GitHub, webhook) has real work in it; by his numbers a routine running every 5 minutes cost 12x an hourly one for the same result; risky steps stop as a draft for approval (47 likes / 9 reposts / 9 replies / 71 bookmarks / 4,036 views, measured 2026-11-26)","url":"https://x.com/irongiantXBT/status/2125317026520641857","kind":"x"}])
add(by['schedule-bots-without-burning-tokens']['watch_out'],"Checking 'every 5 minutes' is rarely needed. Where your tool allows it, trigger the bot on an event (a new email, a message) instead of a timer, and have it drop events with nothing to do (X @irongiantXBT, Nov 24).")

# A playbook after every job (X, Nov 24)
add_sources('teach-your-bot-to-remember-what-works',[
 {"label":"X post by @choopyplug1 (2026-11-24): his Grok Bot writes a short playbook after every job so it 'never thinks about the same task twice'; after 24 playbooks, each job used about 2% of his allowance instead of 9% (37 likes / 2 reposts / 8 replies / 30 bookmarks / 761 views, measured 2026-11-26)","url":"https://x.com/choopyplug1/status/2125300628381381020","kind":"x"}])

json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
