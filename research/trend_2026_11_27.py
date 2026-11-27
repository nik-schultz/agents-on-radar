# Midday trending 2026-11-27 (day after Thanksgiving): extend existing use cases with measured, sourced data.
import json
P='data/use-cases.json'
u=json.load(open(P)); by={x['slug']:x for x in u}
M='2026-11-27'
def add_sources(slug,new):
    x=by[slug]; have={s['url'] for s in x['sources']}
    x['sources']+=[s for s in new if s['url'] not in have]; x['last_checked']=M
def add(lst,item):
    if item not in lst: lst.append(item)

# Official tool "error" messages that carry hidden instructions (Reddit r/ClaudeCode via Hacker News, Nov 26)
add_sources('keep-hidden-instructions-in-email-from-steering-your-bot',[
 {"label":"Reddit r/ClaudeCode, 'Heads up if you wire Notion's official MCP into Claude Code' (2026-11-24): when the workspace hit its hourly query limit, Notion's hosted connector returned an error with 'client_guidance' telling the agent to show a 'Try it free' upsell as a tidy Markdown link, even after the task had finished another way; seen with Claude and with Gemini","url":"https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/","kind":"reddit"},
 {"label":"Hacker News 50658093: 'Notion's official MCP inject hidden upsell instructions into agent context' (58 points / 22 comments, measured 2026-11-27)","url":"https://news.ycombinator.com/item?id=50658093","kind":"hn","stats":{"points":58,"comments":22},"posted_at":"2026-11-26","measured_at":M}])
add(by['keep-hidden-instructions-in-email-from-steering-your-bot']['watch_out'],"Hidden instructions don't only come from strangers' emails. An official app connector's error message told agents to slip a sales link into their answer (Notion MCP, Reddit r/ClaudeCode, Nov 24). Tell your bot to treat text coming back from apps as information, not orders, and never to pass on links it was told to add.")

# Google's Workspace MCP rule: the Gmail server can draft but not send (Hacker News front page, Nov 26)
add_sources('let-ai-send-emails-for-you',[
 {"label":"Tech Stackups, 'Google Will Make AI Agents Use Its Workspace MCP Servers. The Gmail One Can't Send Email' (2026-11-26): from Feb 1, 2027 tools that are or are driven by an AI agent must reach Gmail, Drive and Calendar through Google's MCP servers; the public Gmail server can search, read and create drafts but not send, reply or forward (partner-only), while Anthropic's Claude connector advertises sending","url":"https://techstackups.com/articles/google-workspace-ai-agents-mcp/","kind":"article"},
 {"label":"Hacker News 50653477: 'Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email' (408 points / 327 comments, measured 2026-11-27)","url":"https://news.ycombinator.com/item?id=50653477","kind":"hn","stats":{"points":408,"comments":327},"posted_at":"2026-11-26","measured_at":M}])
add(by['let-ai-send-emails-for-you']['watch_out'],"Built your own email bot on Gmail? Google's new terms say AI agents must use its Workspace MCP servers from Feb 1, 2027, and the public Gmail one can make drafts but not send. Big assistants such as Claude keep sending through their own connectors (Tech Stackups, Nov 26).")

# One notes vault shared by every bot, with a conflicts note and an inbox folder (X, Nov 26) + Obsidian connectors (official, Nov 25)
add_sources('build-a-second-brain-your-bot-reads',[
 {"label":"Obsidian Help, 'Connectors' (2026-11-25): official connectors for Claude, ChatGPT (including Codex and Dots), Grok Bot, Hermes and other agents, so several bots can read and write one vault","url":"https://obsidian.md/help/connectors","kind":"official"},
 {"label":"X post by @0xAIlabs (2026-11-26): moved his Grok Bot 'Brain' wiki into Obsidian so every AI reads the same vault: Grok Bot files bookmarks overnight, Claude checks claims against sources in the morning and writes a conflicts note instead of picking a winner; new links land in an inbox folder and nothing enters the wiki until a second agent checks it (49 likes / 21 replies / 25 bookmarks / 1,324 views, measured 2026-11-27)","url":"https://x.com/0xAIlabs/status/2125983190095417707","kind":"x"}])
add(by['build-a-second-brain-your-bot-reads']['watch_out'],"If a bot saves links into your notes every night, have new items land in an 'inbox' folder first and only move into the main notes after you (or a second bot) check them, so one bad page can't rewrite what your bots believe (X @0xAIlabs, Nov 26).")

# A separate shopping inbox the bot runs (X, Nov 26)
add_sources('give-your-agent-its-own-email-address',[
 {"label":"X post by @Yumzlef (2026-11-26): Grok Bot demo where store checkouts go to a separate inbox; the bot keeps receipts, handles sign-in codes and unsubscribes after a sender's third promo; of 486 emails only 3 reached the person (a trial about to renew, a return window closing, a package pickup) (47 likes / 12 replies / 29 bookmarks / 805 views, measured 2026-11-27)","url":"https://x.com/Yumzlef/status/2125960003391561904","kind":"x"}])

# Second opinions from other models inside Muse (X, Nov 26)
add_sources('have-two-ais-check-each-other',[
 {"label":"X post by @_simonsmith (2026-11-26): set up OpenRouter in Muse so he and Muse consult other models (Neon, Opus, Sol) for second opinions and to compare how they think (61 likes / 2 reposts / 4 replies / 24 bookmarks / 5,245 views, measured 2026-11-27)","url":"https://x.com/_simonsmith/status/2126052366353043667","kind":"x"}])

# Late-night stock check by phone (X, Nov 26)
add_sources('have-your-bot-call-stores-to-check-if-something-is-in-stock',[
 {"label":"X post by @Scott_Weidig (2026-11-26, Thanksgiving Eve): asked his AI chief of staff who had a 1-gallon pitcher in stock; under 25 minutes later three stores were closed, one open, and a voice agent had called Meijer and put 3 on hold at the service desk under his name (2 likes / 2 replies / 38 views, measured 2026-11-27)","url":"https://x.com/Scott_Weidig/status/2125838375756210407","kind":"x"}])

json.dump(u,open(P,'w'),indent=1,ensure_ascii=False)
print('ok')
