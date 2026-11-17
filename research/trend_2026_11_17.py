# Midday trending 2026-11-17: extend/refresh existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-17'
def setstars(slug,url,stars,label=None):
    for s in by[slug]['sources']:
        if s['url']==url:
            s['stats']={'stars':stars}; s['measured_at']=M
            if label: s['label']=label
            return
    raise SystemExit('missing '+url)
# Phone-agent repos (GitHub API, 2026-11-17)
ph='let-an-ai-agent-tap-through-your-phone-for-you'
setstars(ph,'https://github.com/DIYgod/pinky',2364,"GitHub: DIYgod/pinky, 'Let AI agents use your phone, with you in the loop' (iPhone and Android, Apache-2.0, pre-alpha; 2,364 stars, measured 2026-11-17)")
setstars(ph,'https://github.com/JosssphZhou/poki',1563,"GitHub: JosssphZhou/poki, 'Poki uses your iPhone like you do' (local MCP server for Claude Code or Codex, AGPL-3.0; 1,563 stars, measured 2026-11-17)")
setstars(ph,'https://github.com/lxe/phoneuse',679,"GitHub: lxe/phoneuse, see and operate an unmodified iPhone from a Linux PC (MIT; 679 stars, measured 2026-11-17)")
by[ph]['last_checked']=M
sh='control-your-smart-home-with-a-private-ai'
setstars(sh,'https://github.com/homeassistant-ai/ha-mcp',7947,"GitHub: homeassistant-ai/ha-mcp, configure and automate Home Assistant by asking Claude, ChatGPT and other assistants (v9.2.0 released 2026-11-11; 7,947 stars, measured 2026-11-17)")
setstars(sh,'https://github.com/majorminorlabs/hermes-voice',719,"GitHub: majorminorlabs/hermes-voice, talk to a Hermes Agent profile out loud through Home Assistant Assist on an old Amazon Echo (MIT; 719 stars, measured 2026-11-17)")
by[sh]['last_checked']=M
# Memory notes: reader tip (reply to @botsdothat, 2026-11-16) -> plain watch-out, no source link needed
m=by['teach-your-bot-to-remember-what-works']
tip="If you let the bot tidy or rewrite its own notes (Anthropic calls this 'dreaming'), keep a dated copy of the notes file first, and ask it to list what it changed. A bad cleanup is then easy to spot and undo."
if tip not in m['watch_out']: m['watch_out'].insert(1,tip)
m['last_checked']=M
# Haircut booking (was X-only): Google Ask Maps now finds beauty appointments and calls businesses (Nov 16)
h=by['book-a-haircut-by-email']
if not any(t['id']=='google-ask-maps' for t in h['tools']):
    h['tools'].insert(0,{"id":"google-ask-maps","note":"US: ask for a time (e.g. 'a 4 p.m. nail appointment near me'); it shows open slots and can call the business"})
step="No email needed in the US? Ask Google Maps' Ask Maps for the time you want (for example 'a haircut near me Saturday morning'). It shows open slots at nearby businesses and can call to book; check the time and price it confirms before you go."
if step not in h['setup']: h['setup'].append(step)
w="An AI phone call or email shares the details you give it with the business. Only include your name and the time you want."
if w not in h['watch_out']: h['watch_out'].append(w)
new=[{"label":"TechCrunch (2026-11-16): Google Maps' Ask Maps can find beauty, pet care, auto and home-repair appointments online and call local businesses for you (e.g. 'Find me a 4 p.m. nail appointment near me')","url":"https://techcrunch.com/2026/11/16/google-maps-can-now-build-trip-itineraries-with-real-time-details-about-each-stop/","kind":"article"},
{"label":"Engadget (2026-11-16): Ask Maps can find appointments such as beauty, pet care and auto repair and call businesses to book them; appointment booking is US-only at first","url":"https://www.engadget.com/2318186/google-maps-chatbot-can-find-appointments-and-call-to-book-them-for-you/","kind":"article"}]
have={x['url'] for x in h['sources']}
h['sources']+=[x for x in new if x['url'] not in have]
h['last_checked']=M
json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
