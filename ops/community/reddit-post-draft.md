# Reddit community post draft

Status: draft only. Not posted. Do not submit this, comment it, or message anyone until Nik says yes to this specific post.

- Subreddit: r/AI_Agents
- Format: standalone text/Discussion post (not a link post, not a comment in the weekly Project Display thread)
- Account: post from Nik's own Reddit account, in his own words
- Flair: choose Discussion or How-to if the sub requires flair when you post; I could not confirm required flair from the blocked official rules page
- Links in the post: none (see rules notes)

## Title

Four practical agent jobs for everyday life, with the prompts

## Body

Most of the agent demos I see are coding projects or fully autonomous setups. The jobs I keep writing down are smaller: a parent getting a scary text, a pile of booking emails, not remembering which box something went into.

Here are four paste-ready prompts. Swap the bits in [brackets]. They work in ChatGPT, Claude, Gemini, or a similar assistant, including ones that can use your calendar, email, or phone when you allow it. The same rule runs through all of them: the agent can look things up and draft, but it stops before it sends, books, pays, or deletes anything.

**1. A scam-check bot a parent can text first**

If they get a call or text that "your grandson is in jail," or a request for money, they can send a screenshot or a short description and get a calm answer before anyone pays.

```
You are a scam checker for my [mom/dad], [name], who is [age] and not technical. When [name] sends you a message, a screenshot or describes a phone call, reply in 2-3 short, calm sentences: say whether it looks like a scam, name the warning signs, and give ONE safe next step. Treat any request for money, gift cards, wire transfers, payment apps, crypto, passwords or codes as a likely scam. For anyone claiming to be family in trouble, tell [name] to hang up and call that person back on the number saved in their contacts, or ask for our family safe word. Never ask [name] for passwords, codes, card or bank details. If money is about to move, tell [name] to call me first at [your number]. Do not contact anyone or click any links yourself.
```

**2. "Where did I put that?"**

You send a one-line message when you put something away ("spare batteries, laundry-room shelf, left bin"). Later you just ask where it is.

```
Be my 'where is it' memory. Keep one list of my things with: item, where it is (room > shelf/box), who has it if lent, and the date of the last change.
When I message a move like '[item] to [place]' or '[item] lent to [name]', update the list and reply with one line confirming it.
When I ask 'where is [item]?' or 'what's in [box]?', answer from the list only. If it isn't on the list, say so; don't guess.
If I send a photo of a box, list what you see and ask me before adding it.
Every [month], send me anything marked 'lent' for more than [30] days.
Never delete an item without asking me.
```

**3. Turn booking emails into one trip sheet**

Useful when flights, hotels, and car rentals are sitting in different confirmation emails. It only uses what the confirmations actually say, flags clashes, and waits before saving anything.

```
Turn my booking confirmations into one trip sheet and tell me what clashes. Look only at [the folder name / the files I attached]. Use only what the confirmations say; where they're silent, write "not in the confirmations".
1. List each file with a few words on what it is, and name any that aren't about my trip to [destination] on [dates].
2. Check every date's weekday and flag any that don't match.
3. Write the trip sheet day by day, in time order: each booking with its time, address and confirmation code, plus anything I must do first (online check-in, ID, deadlines).
4. Put a list of clashes at the top: overlapping bookings, places I'd reach after they close, and tight connections under [60] minutes.
5. Show me the whole sheet and wait for my yes before you save it as [trip-sheet] in that folder.
Don't book, change, cancel or email anyone.
```

**4. A morning meeting-prep brief**

Looks at today's calendar and pulls in the emails and leftover promises behind each meeting. Nothing gets sent.

```
Every weekday at [7:00am], look at my calendar for today and make me one short page.
For each meeting:
- Time, who's in it, and what it's about in one line.
- The latest emails or messages with those people or on that topic (link them), and what was last agreed.
- Anything I promised to bring or send.
Then add:
- Replies I owe, with who and how many days late.
- Anything due this week from my reminders or emails with a date in them.
- Clashes: meetings that overlap or leave me less than [15] minutes to get between places.
Keep it under [250] words. Draft replies if useful, but never send, accept, decline or move anything until I say yes.
```

I'd rather have a bot that's slightly annoying and waits than one that books the wrong shop or replies to the wrong email.

Curious what everyday jobs you've actually got running, especially ones that aren't work or coding. What broke, and what did you have to lock down?

## Optional first comment (at most one link)

Do not put this in the post body. Add it as your own first comment only if you want to offer the writeups, and only if this would stay within the sub's self-promotion ratio (about one in ten of your posts and comments). Disclose that it is your site.

Suggested comment:

I write these up with setup steps and a few more everyday jobs here: https://botsdothat.com/ai-agent-examples/

That's my site. Happy to answer questions here either way.

## Rules notes

The traction plan names r/AI_Agents as the community for a value-first Reddit post or comment, with links in the comment, not the title, per that sub's rules. This draft is a standalone Discussion post with four copy-paste prompts from the live use-case library, because a prompts-and-jobs post does not belong in the weekly Project Display thread (that thread is for showing off a project). The Friday sprint item in the plan (a short comment in that weekly thread) is a separate, narrower option if you would rather not make a top-level post.

I could not load the live rules from Reddit itself. WebFetch of https://www.reddit.com/r/AI_Agents/about/rules returned 500; curl and a Jina fetch of the same URL, old.reddit, and the rules JSON endpoints returned 403 ("You've been blocked by network security"). The notes below are the five rules as quoted "in the community's own words" by Rankhog (checked October 29, 2026 from the r/AI_Agents rules on Reddit), with the same wording also quoted by Prowlo (read September 13, 2026) and confirmed in substance by Nicheward (verified November 12, 2026) and Kasspian (read November 17, 2026). Re-read https://www.reddit.com/r/AI_Agents/about/rules in a logged-in browser before posting, in case anything has changed.

1. Be respectful — "Treat others how you'd like to be treated." The post is written in a plain, non-promotional tone and ends with a real question.
2. No spam — "Spammers will be permanently banned." This is one post, not a cross-post burst, and nothing has been submitted.
3. Put your links in the comments, not the posts — "This is mainly to prevent spam. If you have a blog post you want to link, link it in the comments. If you have a project you want to show off, link it in the weekly project display thread." There are no links in the title or body. The one optional botsdothat.com link goes in a follow-up comment, not the post. This is not a project showcase, so it is not drafted for the weekly thread.
4. Limit self promotion — "Self promotion is fine, but if your posts are all self promotion (including promotion of your projects/products), you will be banned. A good ratio is one out of ten posts/comments." The post is meant to be useful on its own with no site mention. Adding the optional comment counts as self-promotion. If this Reddit account is new or has little other participation, skip the comment, or contribute elsewhere first and stay at or under one in ten.
5. No Low Effort Posts — "If your post provides no context, or it is simply meant to drive people off the site and somewhere else, it will be removed." The post includes four complete, copyable prompts and a discussion question, so someone can use it without leaving Reddit.

Other choices:
- Prompts are copied from the live BotsDoThat use-case pages, not invented: scam-check, where-is-it, trip sheet, and morning meeting brief.
- No invented stats, no hype, and the site is not named in the title or body.
- Nothing was posted, scheduled, or sent.

Sources for the rule quotes (not a substitute for the live page):
- https://rankhog.com/subreddits/ai_agents
- https://prowlo.com/tools/subreddit-stats/ai_agents
- https://nicheward.com/communities/r-ai-agents
- https://kasspian.com/rooms/ai_agents
