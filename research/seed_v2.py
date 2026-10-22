#!/usr/bin/env python3
"""One-off seed for the live-hub rebuild (2026-10-20).
Writes data/categories.json, data/tools.json, data/use-cases.json (migrated 20 + new entries).
Popularity numbers come ONLY from research/x_posts_full.json (X API reads on 2026-10-20)
or are null. Never edit numbers by hand; run scripts/refresh_popularity.py."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, *p)
XP = json.load(open(D("research", "x_posts_full.json")))
MEASURED = "2026-10-20"
ADDED = "2026-10-20"

# Extra posts read with get_posts_by_ids on 2026-10-20
XP.update({
 "2072663153532666045": {"user": "tomchris", "created": "2026-07-02T12:46:18.000Z", "metrics": {"like_count": 8, "repost_count": 1, "reply_count": 3, "bookmark_count": 3, "impression_count": 1371, "quote_count": 0}, "url": "https://x.com/tomchris/status/2072663153532666045"},
 "2104442538254123102": {"user": "_architected", "created": "2026-09-28T05:26:14.000Z", "metrics": {"like_count": 10, "repost_count": 0, "reply_count": 1, "bookmark_count": 0, "impression_count": 780, "quote_count": 0}, "url": "https://x.com/_architected/status/2104442538254123102"},
 "2108012315602034988": {"user": "johnmccoyx", "created": "2026-10-08T01:51:15.000Z", "metrics": {"like_count": 4, "repost_count": 0, "reply_count": 4, "bookmark_count": 3, "impression_count": 894, "quote_count": 0}, "url": "https://x.com/johnmccoyx/status/2108012315602034988"},
})
json.dump(XP, open(D("research", "x_posts_full.json"), "w"), indent=1)

def xpop(pid):
    p = XP[pid]; m = p["metrics"]
    return {"platform": "x", "post_id": pid, "author": "@" + p["user"], "url": p["url"],
            "posted_at": p["created"][:10], "likes": m["like_count"], "reposts": m.get("repost_count", 0),
            "replies": m.get("reply_count"), "bookmarks": m.get("bookmark_count"), "views": m.get("impression_count"),
            "measured_at": MEASURED}

def xsrc(pid, label):
    p = XP[pid]
    return {"label": f"X post by @{p['user']} ({p['created'][:10]}): {label}", "url": p["url"], "kind": "x"}

def src(label, url, kind="article"): return {"label": label, "url": url, "kind": kind}

WIRED = src("WIRED, Sep 24 2026: “I Think I Found an AI Agent Worth the Risk” (Instinct review)", "https://www.wired.com/story/i-finally-found-an-ai-agent-worth-the-risk/")
MUSE_BLOG = src("Meta: “How We Designed Muse” (launch essay)", "https://introducing.muse.ai/", "official")
MUSE_HELP = src("Meta Help Center: How to get started with Muse", "https://www.meta.com/help/artificial-intelligence/1331373868832401/", "official")
SPARK_BLOG = src("Google blog: Gemini Spark announcement (May 2026)", "https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/", "official")
SPARK_PAGE = src("Google: Gemini Spark overview page (example tasks and schedules)", "https://gemini.google/overview/agent/spark/", "official")
UCART = src("Google blog, Oct 15 2026: Universal Cart launches in the U.S.", "https://blog.google/products-and-platforms/products/shopping/universal-cart-launch/", "official")
VERGE_UC = src("The Verge, Oct 15 2026: Google launches its universal shopping cart", "https://www.theverge.com/tech/1011797/google-ai-universal-cart-shopping-tool-launch")
SCHOOL = src("Anna Burgess Yang: How I created a digest of school emails with Claude Cowork", "https://tinkeringwithideas.io/school-email-digest-claude-cowork/")
RAI = src("Reddit r/AI_Agents: “What AI agents are actually worth running for personal use?” (archived snapshot, Sep 5 2026)", "https://reddit.sentinel-team.org/posts/1w4e3ji/snapshots/2026-09-05T09%3A24%3A43.696105Z", "reddit")
RAI_LIVE = src("Original Reddit thread", "https://www.reddit.com/r/AI_Agents/comments/1w4e3ji/what_ai_agents_are_actually_worth_running_for/", "reddit")
N8N_JOBS = src("Reddit r/n8n: LinkedIn job-matching workflow that scores jobs against your CV (Apr 2026)", "https://www.reddit.com/r/n8n/comments/1ssdtg7/built_a_n8n_linkedin_job_automation_ai_agent/", "reddit")
N8N_JOBS2 = src("Reddit r/n8n: Can n8n realistically auto-apply to jobs? (discussion of bans and fragile submission)", "https://www.reddit.com/r/n8n/comments/1u30kw5/can_n8n_realistically_power_an_automated_job/", "reddit")

CATS = [
 {"slug": "inbox", "name": "Inbox & paperwork", "icon": "📥", "art": "cat-inbox", "blurb": "Email, letters, forms and the admin that piles up."},
 {"slug": "money", "name": "Money & bills", "icon": "💸", "art": "cat-money", "blurb": "Refunds, bills, subscriptions and money leaking out quietly."},
 {"slug": "shopping", "name": "Shopping & groceries", "icon": "🛒", "art": "cat-shopping", "blurb": "Meal plans, grocery carts, price drops and restocks."},
 {"slug": "travel", "name": "Bookings & travel", "icon": "✈️", "art": "cat-travel", "blurb": "Tables, haircuts, flights, delays and whole trips."},
 {"slug": "family", "name": "Family & home", "icon": "🏡", "art": "cat-family", "blurb": "School emails, calendars, chores and household logistics."},
 {"slug": "health", "name": "Health & care", "icon": "🩺", "art": "cat-health", "blurb": "Insurance fights, appointments and caring for a parent."},
 {"slug": "work", "name": "Work & career", "icon": "💼", "art": "cat-work", "blurb": "Job hunting, follow-ups and a chief-of-staff bot."},
 {"slug": "business", "name": "Small business & side hustles", "icon": "🏪", "art": "cat-business", "blurb": "Receipts, leads, reviews, invoices and selling stuff."},
]

TOOLS = {
 "chatgpt": {"name": "ChatGPT", "url": "https://chatgpt.com", "cost": "Free plan; paid plans add more", "kind": "chat"},
 "claude": {"name": "Claude", "url": "https://claude.ai", "cost": "Free plan; paid plans add more", "kind": "chat"},
 "gemini": {"name": "Gemini", "url": "https://gemini.google.com", "cost": "Free plan; paid plans add more", "kind": "chat"},
 "grok": {"name": "Grok", "url": "https://grok.com", "cost": "Free plan; paid plans add more", "kind": "chat"},
 "chatgpt-work": {"name": "ChatGPT agent (cloud browser)", "url": "https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt", "cost": "Paid ChatGPT plans only (not Free or Go)", "kind": "agent"},
 "chatgpt-dots": {"name": "ChatGPT dots (always-on agents)", "url": "https://openai.com/index/introducing-dots/", "cost": "Rolling out to eligible paid plans; check OpenAI's page", "kind": "agent"},
 "claude-cowork": {"name": "Claude Cowork", "url": "https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork", "cost": "Check plan requirements on Anthropic's help page", "kind": "agent"},
 "gemini-spark": {"name": "Gemini Spark", "url": "https://gemini.google/overview/agent/spark/", "cost": "Google AI Pro and Ultra subscribers in select countries", "kind": "agent"},
 "gemini-opentable": {"name": "Gemini + OpenTable", "url": "https://support.google.com/gemini/answer/17090712", "cost": "Works in the Gemini app", "kind": "agent"},
 "google-universal-cart": {"name": "Google Universal Cart", "url": "https://blog.google/products-and-platforms/products/shopping/universal-cart-launch/", "cost": "In Google Search and the Gemini app (U.S.)", "kind": "agent"},
 "grok-bot": {"name": "Grok Bot (personal agents)", "url": "https://docs.x.ai/grok-bot/overview", "cost": "Check plan requirements in xAI's docs", "kind": "agent"},
 "meta-muse": {"name": "Meta Muse", "url": "https://www.meta.com/help/artificial-intelligence/1331373868832401/", "cost": "Free with a usage limit; paid tier for more", "kind": "agent"},
 "instinct": {"name": "Instinct", "url": "https://instinct.co", "cost": "Invite-only beta (per WIRED, Sep 2026)", "kind": "agent"},
 "zapier": {"name": "Zapier", "url": "https://zapier.com", "cost": "Free plan; paid plans add more", "kind": "automation"},
 "n8n": {"name": "n8n", "url": "https://n8n.io", "cost": "Free to self-host; paid cloud plans", "kind": "automation"},
 "make": {"name": "Make", "url": "https://www.make.com", "cost": "Free plan; paid plans add more", "kind": "automation"},
}

def uc(slug, title, category, summary, does, endup, difficulty, tools, prompt, watch, sources, pop=None, source_date=None, tags=(), setup=None):
    return {"slug": slug, "title": title, "category": category, "date_added": ADDED,
            "source_date": source_date or (pop["posted_at"] if pop else None),
            "summary": summary, "what_the_bot_does": does, "what_you_end_up_with": endup,
            "difficulty": difficulty, "tools": tools, "prompt": prompt, "setup": setup or [],
            "watch_out": watch, "sources": sources, "popularity": pop, "tags": list(tags),
            "last_checked": MEASURED, "origin": "seed-2026-10-20"}

T = lambda i, note=None: ({"id": i, "note": note} if note else {"id": i})
NEW = []
NEW += [
uc("family-meal-plan-and-grocery-order", "Plan a week of family meals and fill the grocery cart", "shopping",
   "A bot keeps your recipe list, writes the week's meal plan and turns it into a shopping list that fills your grocery cart.",
   ["Keeps a simple list of the recipes your family actually eats.", "Every week, picks meals that fit your schedule and budget.", "Prints a meal plan you can stick on the fridge.", "Turns the plan into one shopping list, grouped by aisle.", "Hands the list to a shopping agent that fills your Instacart cart. You check out yourself."],
   "A printed weekly meal plan and a filled grocery cart waiting for your OK.", "Medium",
   [T("grok-bot", "Keeps the recipe library and runs it weekly"), T("chatgpt-work", "Fills a grocery cart from a pasted list"), T("claude"), T("gemini-spark", "Instacart connection announced by Google")],
   "Every Thursday, plan [5] dinners for [2 adults and 2 kids]. Use only recipes from my recipe list below, avoid [allergies], keep the week under [$ budget]. Reuse ingredients so little goes to waste. Give me: (1) a one-page meal plan I can print, (2) one shopping list grouped by store section, leaving out what I said we already have. Don't buy anything.\n\nMy recipes: [paste a list or link]\nAlready in the fridge: [list]",
   ["Do the checkout yourself. Read the cart before you pay.", "Some stores block shopping agents. One user says Amazon blocked his agent, so he moved his groceries to Instacart."],
   [xsrc("2107888353630908437", "a custom Grok bot plans 15 family meals a week and feeds a shopping list into Instacart"), xsrc("2110749518518235276", "Amazon blocked his agent, so groceries moved to Instacart"), xsrc("2103607960996086113", "Claude meal plan from fridge photos plus Instacart")],
   xpop("2107888353630908437"), tags=["meal plan", "groceries", "instacart", "recipes", "family"]),

uc("sunday-family-calendar-check", "Catch family calendar clashes before the week starts", "family",
   "Every Sunday a bot reads the next two weeks of your family calendar and school notices and flags the clashes.",
   ["Reads your shared family calendar for the next 14 days.", "Reads recent school notices for dates you haven't added yet.", "Spots clashes between work, school and activities.", "Lists anything you need to prepare, like forms, payments or kit."],
   "A short Sunday note: what's coming up, what clashes, and what to prepare.", "Easy",
   [T("grok-bot", "Schedule it as a weekly routine"), T("gemini-spark", "Reads Google Calendar and Gmail"), T("claude-cowork", "Can run as a scheduled task"), T("meta-muse")],
   "Every Sunday at 6pm, review our family calendar for the next 14 days. Highlight important events, scheduling conflicts, missing information and anything we need to prepare. Keep it under 10 bullet points. Don't change or delete any calendar events. Just tell me.",
   ["Give it read-only calendar access to start.", "Use initials instead of your kids' names if you prefer."],
   [xsrc("2108579992456327489", "7 jobs to give a family bot, with prompts")],
   xpop("2108579992456327489"), tags=["calendar", "kids", "school", "weekly"]),

uc("hand-your-most-hated-chores-to-a-personal-agent", "Hand your most-hated weekly chores to a personal agent", "inbox",
   "Personal agents like Meta Muse, Grok Bot and Gemini Spark work in the background on a schedule. Start with the chore you hate most.",
   ["Asks what you'd like help with and which apps it may use.", "Works through the task in the background on its own computer and browser.", "Repeats on a schedule you set, like every morning or every Friday.", "Messages you only when something needs your decision."],
   "One recurring chore that now happens without you, plus a message when it needs a yes or no.", "Easy",
   [T("meta-muse", "Free with a usage limit"), T("grok-bot"), T("gemini-spark"), T("chatgpt-dots"), T("instinct", "Works over iMessage and WhatsApp")],
   "I want to hand you one boring chore. Here it is: [describe the chore, e.g. 'every Friday, check my email for bills due next week and list them']. Before you start, ask me any questions you need answered. Show me the first result before you set it to repeat. Never send, buy, delete or book anything without asking me first.",
   ["Pick ONE chore first. Users who tried a general “do everything” assistant say they stopped using it within weeks; narrow tasks stuck.", "Meta's own help page says Muse “may be inaccurate or take unexpected actions”. Check what it does."],
   [xsrc("2107254007412756589", "video: 6 everyday use cases for Meta Muse"), MUSE_HELP, RAI],
   xpop("2107254007412756589"), tags=["personal agent", "muse", "chores", "getting started"]),

uc("email-scam-filter", "Get a daily scam check on your inbox", "inbox",
   "A read-only bot reads your new email each morning and gives each suspicious message a risk score and the red flags.",
   ["Every morning, reads the new mail in your inbox. It can only read; it can't change anything.", "Checks each message for phishing, fake invoices, impostor “IT” alerts and prize scams.", "Keeps up with the latest scam alerts from public sources.", "Gives each suspicious email a risk level and the exact red flags, like a lookalike link."],
   "A morning list: “Confirmed scam / High suspicion / Possible / Clear”, with what to do next.", "Easy",
   [T("grok-bot", "Shared as a ready-made bot template"), T("gemini-spark"), T("claude-cowork"), T("chatgpt", "Paste in one suspicious email at a time")],
   "Every morning at 7am, check new emails in my inbox for scams: phishing, fake invoices, fake prize offers, blackmail emails and fake 'IT department' alerts. For each suspicious email give a risk level (Confirmed scam / High suspicion / Possible / Clear), the exact red flags (sender address, lookalike links, urgency, payment requests) and safe next steps. You are read-only: never click links, never reply, never delete.",
   ["Keep it read-only. It should never click links or reply.", "A bot can miss scams too. If in doubt, call the company using a number you already trust."],
   [xsrc("2110008406807568813", "a read-only Grok Bot that scores email scam risk every morning")],
   xpop("2110008406807568813"), tags=["scams", "phishing", "email", "safety", "older parents"]),

uc("run-family-logistics-from-the-group-chat", "Run family logistics from the family group chat", "family",
   "New “family agents” sit in your family chat and handle the small jobs: restocking, booking the dentist and reminders.",
   ["Lives in your family group chat, so anyone can ask it for something.", "Restocks groceries on a shared shopping account.", "Books appointments like the dentist.", "Sends reminders, for example to Grandma about her meds."],
   "Fewer “did anyone book…?” messages, and one place where family requests get done.", "Easy",
   [T("meta-muse"), T("instinct", "Works in iMessage and WhatsApp"), T("grok-bot")],
   "You're our family assistant in this group chat. Jobs you can do: keep a shared shopping list, remind people about appointments, and draft bookings for my approval. Rules: confirm with me before booking or buying anything; never share our address or schedule with anyone outside this chat; reply in one short message.",
   ["Agree as a family what it may book or buy. Set a spending limit.", "This is a new product category. Coral was announced on Oct 11, 2026, and we haven't tested it."],
   [xsrc("2109330165381910817", "launch of Coral, a family agent that works from the family chat")],
   xpop("2109330165381910817"), tags=["family chat", "reminders", "groceries", "dentist"]),

uc("get-a-refund-on-an-accidental-charge", "Get a refund on a charge you didn't mean to make", "money",
   "Point an agent at an accidental or unfair charge. It contacts support (sometimes the company's own bot) and asks for a refund.",
   ["Reads the bill or receipt and works out what went wrong.", "Finds the right support channel.", "Writes or chats a polite, specific refund request.", "Reports back on what the company offered."],
   "A refund request sent and a clear answer, without you sitting in a support queue.", "Medium",
   [T("chatgpt-work", "Can use support chat in a cloud browser"), T("instinct"), T("meta-muse"), T("claude", "Drafts the request for you to send")],
   "I was charged [amount] by [company] on [date] for [what]. It was a mistake because [reason]. Find their refund or support channel and draft a short, polite request for a refund to my original payment method. 'Resolved' means CASH back to my card, not store credit or a coupon. Show me the message before sending, and tell me if they offer anything other than a refund.",
   ["Spell out what “resolved” means. One user says his agent accepted $40 store credit when he wanted cash.", "WIRED's reviewer says her agent cancelled a delayed food order and she lost $64, even though she'd said “only if refunded”."],
   [xsrc("2105887752437023129", "an agent asked a cloud provider's support agent for a refund"), xsrc("2099545931129762087", "an agent “resolved” a refund as $40 store credit"), WIRED],
   xpop("2105887752437023129"), tags=["refund", "customer service", "bills"]),

uc("deal-hunting-that-knows-what-you-own", "Shop for deals with a bot that knows what you already own", "shopping",
   "Ask a bot connected to your email to find deals. It can check your old receipts so you don't buy the same thing twice.",
   ["Searches stores for deals on what you asked for.", "Looks through old order receipts in your email.", "Points out what you already own (“you have this in green and blue”).", "Shows the deals with links, without buying anything."],
   "A short list of real deals, minus duplicates of things you already have.", "Easy",
   [T("grok-bot"), T("gemini-spark", "Reads Gmail receipts"), T("google-universal-cart", "Tracks price drops on saved items"), T("chatgpt-work")],
   "Find current deals on [item/brand] in my size [size]. Before you suggest anything, search my email for past order receipts from [store] and tell me what I already own. Give me the 5 best deals with the price, the store and a link. Don't buy anything.",
   ["Giving a bot access to your email lets it see a lot. Start with one search only if you're comfortable with that."],
   [xsrc("2091487956955492861", "a Grok Bot found his 2023 receipts while deal hunting")],
   xpop("2091487956955492861"), tags=["deals", "receipts", "shopping"]),

uc("reorder-your-regular-groceries", "Let an agent reorder your regular groceries", "shopping",
   "Some people now let an agent handle their weekly grocery order and switch stores when a better offer appears.",
   ["Knows your usual items and brands.", "Builds the weekly order on a grocery site that allows agents.", "Swaps in a better offer when it finds one.", "Asks for your OK (“confirm”) before paying."],
   "Groceries ordered after a quick chat and one confirm tap.", "Medium",
   [T("chatgpt-work", "Uses a cloud browser; asks before payments"), T("meta-muse"), T("instinct"), T("gemini-spark", "Instacart connection announced by Google")],
   "Here's my usual weekly grocery list: [list with brands and sizes]. Build this order on [Instacart / store site]. If an item is out of stock, pick the closest match and tell me. If the same item is cheaper elsewhere, tell me but don't switch stores without asking. Stop at checkout and show me the total.",
   ["Some sites block agents. One user says Amazon blocked his.", "Always review substitutions and the final total before paying."],
   [xsrc("2110749518518235276", "groceries moved to Instacart after Amazon blocked his agent"), src("X post by @mulhollandsr (2026-09-25): Amazon blocked Muse from his cart", "https://x.com/mulhollandsr/status/2103533570203717674", "x")],
   xpop("2110749518518235276"), tags=["groceries", "instacart", "amazon", "weekly"]),

uc("plan-and-book-a-whole-trip-by-text", "Plan and book a whole trip by texting your bot", "travel",
   "One parent says his bot booked the flight, the rental car, the vacation rental, a restaurant and event tickets, all over text.",
   ["Takes your dates, budget and who's coming.", "Finds and compares flights, cars and places to stay.", "Books each piece after you say yes.", "Makes restaurant bookings and buys event tickets.", "Keeps every confirmation in one thread."],
   "A booked trip with every confirmation in one chat.", "Medium",
   [T("grok-bot"), T("instinct"), T("meta-muse", "Can book travel"), T("chatgpt-work", "Asks before bookings and payments")],
   "Plan a trip for [who] to [place] from [date] to [date], budget [$]. I need: a flight from [city] (no red-eyes), a car, a place to stay near [area] with [needs], one dinner reservation on [night] and tickets to [event]. Show me 2 options for each with prices. Book only after I reply YES for that item, and send me every confirmation number in one list.",
   ["Use a card with a low limit, or a single-use virtual card.", "Double-check dates, names and cancellation rules before you say yes."],
   [xsrc("2110721195817509068", "a Grok bot booked flight, Turo, Vrbo, dinner and event tickets by text")],
   xpop("2110721195817509068"), tags=["travel", "flights", "vrbo", "texting"]),

uc("rebook-a-delayed-flight", "Get rebooked fast when your flight is delayed", "travel",
   "When a flight slips, an agent can find the fastest alternative and ask the airline for a refund on the original.",
   ["Notices the delay from your airline email or what you tell it.", "Searches for the fastest flight that gets you there on time.", "Books it, if you've allowed that.", "Asks for a refund on the delayed ticket."],
   "A new flight confirmation in your chat, and a refund request for the old one.", "Medium",
   [T("instinct"), T("chatgpt-work"), T("grok-bot"), T("meta-muse")],
   "My flight [flight number] from [city] to [city] is delayed by [hours]. I need to arrive by [time]. Find the 3 fastest options on any airline, with price and on-time risk. If I reply with a number, book that one with my saved card. Then ask [airline] for a refund on the delayed ticket and show me the request first.",
   ["Decide ahead of time whether it may book without asking. One user's agent did, and it worked out. Yours might not.", "Refund rules depend on the airline, the fare and the country."],
   [xsrc("2098109328112636407", "agent booked the only on-time flight and got the delayed one refunded"), WIRED],
   xpop("2098109328112636407"), tags=["flights", "delays", "refund", "airline"]),

uc("catch-airline-schedule-changes", "Catch airline schedule changes that earn you a refund", "travel",
   "Airlines quietly move flight times. An agent watching your inbox can spot the change and check whether you're owed a refund.",
   ["Watches your email for airline itinerary changes.", "Compares the new times with your original booking.", "Checks the airline's rules for whether the change qualifies for a refund.", "Drafts the cancellation or refund request for you to approve."],
   "An alert when your flight changes, and a refund request ready if you're owed one.", "Medium",
   [T("instinct", "Did this in WIRED's test"), T("gemini-spark", "Reads Gmail"), T("grok-bot"), T("chatgpt")],
   "Watch my email for any message from an airline about a schedule change, a time change or a cancellation. When you find one, tell me the old and new times and the size of the change, and check that airline's published rules on whether I can get a full refund. Draft the request but don't cancel anything without my OK.",
   ["Cancelling may give up your seat. Decide before you ask for the refund.", "WIRED's reviewer says her agent caught a 90-minute change she had missed, which got her about $550 back."],
   [WIRED, src("Assistant Benchmark: Instinct profile (quotes and test notes)", "https://assistantbenchmark.com/agents/instinct")],
   None, source_date="2026-09-24", tags=["flights", "refund", "schedule change"]),

uc("restaurant-reservations-by-agent", "Book restaurant tables by message, even at phone-only places", "travel",
   "Restaurant bookings are the gateway task for many agent users, including small places that only take WhatsApp or calls.",
   ["Takes where you'll be, when, and what you like.", "Finds places nearby and checks availability.", "Books online, or messages the restaurant if there's no booking site.", "Sends you the confirmation."],
   "A table booked and a confirmation in your chat.", "Easy",
   [T("gemini-opentable", "Book, cancel or check OpenTable reservations"), T("instinct", "WhatsApps small restaurants"), T("meta-muse", "Can call restaurants"), T("grok-bot")],
   "Book dinner for [number] people on [date] around [time] near [address]. I like [cuisine], budget about [$ per person]. Give me 3 options first. After I pick, book it under my name, and tell me the cancellation policy.",
   ["It can be slower than doing it yourself. One startup timed agents taking 4 to 14+ minutes for a dinner booking; the founder did it in 37 seconds.", "Don't let it hold tables you won't use. WIRED reports one investor got banned from Resy after his bot hit it about 200 times an hour."],
   [WIRED, xsrc("2105372125288976402", "timed comparison of agents making a dinner reservation")],
   xpop("2105372125288976402"), tags=["restaurant", "reservation", "opentable", "whatsapp"]),

uc("book-a-haircut-by-email", "Book a haircut or appointment, even when the form won't work", "travel",
   "When the online booking needs a local phone number, an agent can just email the business instead.",
   ["Finds salons or providers and reads reviews.", "Shows you options with photos.", "Tries online booking, or writes the business a normal email.", "Confirms the slot with you."],
   "A confirmed appointment without the back-and-forth.", "Easy",
   [T("instinct"), T("meta-muse"), T("grok-bot"), T("chatgpt", "Drafts the email for you to send")],
   "Find 3 well-reviewed [salons/barbers/dentists] near [area] that can do [service]. Show me reviews and prices. After I pick, book [day/time range]. If online booking doesn't work, email them asking for that slot, sign it with my name, and say I'm using an assistant. Tell me when it's confirmed.",
   ["Be honest that an assistant is writing. One user said the salon didn't realize an AI wrote the email."],
   [xsrc("2100245612910571873", "Instinct emailed a salon when online booking needed a Danish number")],
   xpop("2100245612910571873"), tags=["appointment", "haircut", "booking", "email"]),
]
NEW += [
uc("small-business-receipt-matching", "Match every business expense to its receipt, weekly", "business",
   "A read-only bot checks your card and payment activity against the receipts in a dedicated inbox and lists what's missing.",
   ["Gets read-only access to your business card activity and a receipts@ inbox.", "Every week, matches each charge to a receipt.", "Lists charges with no receipt and receipts with no charge.", "Flags odd fees, refunds and pending items."],
   "A weekly reconciliation list with the gaps to chase.", "Advanced",
   [T("grok-bot", "Used with the Whop CLI in the source post"), T("claude-cowork"), T("zapier", "Forward receipts into a sheet"), T("n8n")],
   "Pull this week's business card and payment activity. Match each expense to a receipt in the receipts@ inbox. Give me a table: date, merchant, amount, receipt found (yes/no), notes. List unmatched charges first. You are read-only: never change cards, send payouts or move money.",
   ["Keep it read-only. The person who shared this says the bot “does not need permission to change cards, send payouts, or move money.”", "Ask your accountant before changing how you keep your books."],
   [xsrc("2094755088841457892", "finance admin automated with Grok Bot + a receipts inbox, read-only")],
   xpop("2094755088841457892"), tags=["receipts", "bookkeeping", "expenses", "small business"]),

uc("hire-a-chief-of-staff-bot", "Set up a “chief of staff” bot that plans your other bots", "work",
   "Instead of building lots of bots, start with one that asks what you do and suggests which helpers you need.",
   ["Lists what a human chief of staff would handle for you.", "Writes its own job description (the “system prompt”).", "Suggests the first 1–3 helper bots and what each one does.", "Briefs those helpers so you don't have to."],
   "A short, sensible plan for which bots you need, often fewer than you thought.", "Easy",
   [T("grok-bot"), T("chatgpt-dots"), T("gemini-spark"), T("claude-cowork")],
   "You're my Chief of Staff bot. Give me a list of all the things a typical chief of staff would be responsible for, then suggest a system prompt you can install for yourself.\n\nAbout me: [who you are and what you do].\nWhat I want help with: [goals].\nSuggest the first bots you'd hire and what each one owns.",
   ["Start small. The poster says a friend's 5-bot setup “nothing ran”; two bots were enough."],
   [xsrc("2099808193178485185", "the 2-sentence chief-of-staff prompt")],
   xpop("2099808193178485185"), tags=["chief of staff", "getting started", "productivity"]),

uc("one-bot-per-brand", "Run several brands or jobs with one bot each", "business",
   "If you juggle several brands or clients, give each its own bot with its own tools, plus a coordinator that collects a daily note.",
   ["Each bot connects only to one brand's email, files and chat.", "Each writes one short daily note, even if it's just “no updates”.", "A coordinator bot reads the notes and passes tasks to the right helper.", "Heavier jobs go to specialist tools, which report back."],
   "One daily note per brand, and tasks that never land in the wrong account.", "Advanced",
   [T("grok-bot"), T("claude-cowork"), T("n8n", "Glue between accounts")],
   "You are the bot for [Brand]. You only use [Brand]'s email, drive and chat. Every weekday at 5pm, write a note in [folder]: new requests, decisions needed, deadlines this week. Write 'no updates' if nothing changed. Never act on another brand's accounts.",
   ["Keeping accounts separate is the point. Don't connect one bot to everything."],
   [xsrc("2107076101293969587", "a multi-brand Grok Bot fleet with daily notes")],
   xpop("2107076101293969587"), tags=["multiple brands", "freelancers", "agencies"]),

uc("deal-desk-inbox-watcher", "Catch offers and deadlines the moment they land in your inbox", "work",
   "For deal-heavy work (real estate, sales, hiring), a bot in your inbox and calendar texts you when something time-sensitive arrives.",
   ["Watches your inbox for offers, counteroffers and deadlines.", "Texts you who sent it and the key numbers before you open the email.", "Builds your follow-up list every Monday.", "Flags clashing dates, like a closing that collides with a funding deadline.", "Drafts routine emails for your OK."],
   "No missed offers, a Monday follow-up list and early warnings on deadline clashes.", "Medium",
   [T("grok-bot"), T("gemini-spark"), T("claude-cowork"), T("zapier", "For simple “if email contains X, text me”")],
   "Watch my inbox for offers, counteroffers and deadline changes on my active deals: [list]. When one arrives, text me: who, price and terms, and the deadline. Every Monday at 8am, give me a follow-up list of everyone waiting on me. Flag any two dates on my calendar that conflict. Draft replies but never send them.",
   ["Don't let it send anything to clients without your review.", "Check the numbers it reports against the actual document."],
   [xsrc("2105719791751487542", "8 days with an agent in a commercial real estate inbox")],
   xpop("2105719791751487542"), tags=["real estate", "sales", "deadlines", "inbox"]),

uc("mail-to-bill-pay-with-anomaly-alerts", "Turn paper mail into paid bills, with alerts when one looks wrong", "money",
   "Paper mail gets scanned to email. The bot reads each bill and pays the normal ones, and pulls you in only when a bill is more than 20% off.",
   ["A virtual mailbox service opens and scans your paper mail to PDF.", "The bot reads each scanned letter in your email.", "Compares each bill with what you usually pay.", "Pays normal bills and flags anything unusual (for example, 20% higher)."],
   "Bills handled, and you only see the weird ones.", "Advanced",
   [T("claude-cowork"), T("gemini-spark", "Can parse statements on a schedule"), T("grok-bot")],
   "Each time a scanned bill arrives in my email from [mail service], read it and add it to my bills sheet: payee, amount, due date. Compare it with the last 3 bills from that payee. If it's more than 20% different, or it's a payee I've never paid before, stop and message me. Otherwise, add it to my 'ready to pay' list. Do not pay anything until I approve the list.",
   ["Start by approving every payment. Only loosen that once you trust it.", "The person who shared this adds his own caveats about the hype; read the full post."],
   [xsrc("2102768278812680522", "Claude reads scanned mail, pays bills, flags >20% changes")],
   xpop("2102768278812680522"), tags=["bills", "mail", "virtual mailbox", "autopay"]),

uc("find-money-leaking-from-your-inbox", "Find subscriptions and money quietly leaking out of your inbox", "money",
   "A bot sweeps years of receipts for forgotten subscriptions, unpaid invoices, duplicate charges and claimable delays, then drafts every claim for your OK.",
   ["Searches your email for receipts and renewals.", "Flags subscriptions you haven't used in 90+ days.", "Finds invoices you sent but never chased.", "Spots duplicate charges and quiet price hikes.", "Drafts each cancellation or claim and waits for your yes."],
   "A list of leaks with a draft fix for each one.", "Medium",
   [T("grok-bot"), T("gemini-spark", "Can flag hidden fees in card statements monthly"), T("claude-cowork"), T("chatgpt", "Paste in a statement instead")],
   "Search my email from the last [2] years for receipts, renewals and invoices. List: (1) subscriptions with no sign I've used them in 90 days, (2) invoices I sent with no payment, (3) duplicate charges or price increases. For each, draft the cancellation, reminder or claim. Rule: no claim without the original receipt attached. Send nothing until I say yes.",
   ["The poster says his bot once started a claim against a vendor who owed him nothing, so he added the rule “no claim without the original receipt attached”.", "The poster's dollar figures are his own claim; we haven't verified them."],
   [xsrc("2092341990868365451", "a Grok Bot swept 4 years of email for leaking money"), SPARK_BLOG],
   xpop("2092341990868365451"), tags=["subscriptions", "refunds", "invoices", "budget"]),

uc("watch-a-web-page-for-changes", "Watch any web page for a price drop, restock or new listing", "shopping",
   "Instead of refreshing a page, tell a bot what matters on it. It checks on a schedule and pings you only when that changes.",
   ["Takes a link and what you care about, like the price going under $X.", "Saves how the page looks now.", "Checks again on a schedule.", "Messages you only when that thing changes."],
   "One ping when it matters, and no more refreshing.", "Easy",
   [T("grok-bot", "Shared as a free template"), T("google-universal-cart", "Price-drop and restock alerts on saved items"), T("chatgpt-dots"), T("make"), T("zapier")],
   "Watch this page: [link]. What matters: [price below $X / back in stock / new listing / policy change]. Check it [every morning]. Message me only when that changes, with the old and new value and the link. Don't buy anything.",
   ["Some sites block automated checks. Use official alerts where they exist.", "A Reddit user says a narrow watcher like this is the one they kept using; general assistants didn't stick."],
   [xsrc("2111981455077466525", "a Grok bot that watches pages and pings only on change"), RAI],
   xpop("2111981455077466525"), tags=["price drop", "restock", "alerts", "listings"]),

uc("track-prices-across-stores-with-universal-cart", "Track price drops across stores with one cart", "shopping",
   "Google's Universal Cart (live in the U.S. since Oct 15, 2026) saves items from many stores and alerts you to price drops and restocks.",
   ["Save products from different stores into one cart from Search or the Gemini app.", "The cart watches prices and stock for you.", "It suggests promo codes and which of your cards gives the best perk.", "You check out with Google Pay or on the store's own site."],
   "One cart with price-drop and restock alerts across stores.", "Easy",
   [T("google-universal-cart"), T("gemini")],
   "In the Gemini app: 'Add [product] from [store] to my cart and tell me if the price drops below [$] or if it's cheaper at another store.'",
   ["U.S. only for now.", "You can't check out from several stores at once (per The Verge)."],
   [UCART, VERGE_UC],
   None, source_date="2026-10-15", tags=["price drop", "holiday shopping", "google", "gemini"]),

uc("find-dead-conversations-to-follow-up", "Find the conversations you forgot to follow up on", "work",
   "A weekly automation reads your calendar, inbox and tasks and lists people still waiting to hear back, with drafted nudges.",
   ["Looks at recent meetings, email threads and tasks.", "Finds threads where you owe a reply or the other person went quiet.", "Drafts a short, friendly follow-up for each one.", "Puts it all in one morning brief."],
   "A list of dropped threads with a ready-to-send nudge for each.", "Medium",
   [T("n8n", "The source shares an 8-node workflow"), T("zapier"), T("gemini-spark"), T("grok-bot")],
   "Every Monday at 8am, look at my sent email, my calendar from the last 30 days and my task list. List conversations where (a) I promised something and haven't sent it, or (b) I asked something and got no reply in 7+ days. For each, draft a 2-sentence friendly follow-up. Don't send anything.",
   ["Read each draft. Some threads went quiet for a reason."],
   [xsrc("2102701286307119565", "an n8n automation found 19 dead conversations")],
   xpop("2102701286307119565"), tags=["follow up", "email", "networking", "n8n"]),

uc("build-a-lead-list-with-approval", "Build a list of local leads and approve every email", "business",
   "A workflow finds businesses in your niche and area, researches each one and drafts a personal email. Nothing goes out until you approve it.",
   ["Finds businesses by type and location.", "Identifies the decision maker and a public contact.", "Researches each business and drafts a personal note.", "Saves everything to a spreadsheet for you to review.", "Sends only approved emails, slowly."],
   "A spreadsheet of researched leads with drafted, approved outreach.", "Advanced",
   [T("n8n"), T("make"), T("zapier"), T("grok-bot")],
   "Find [20] [type of business] in [city] that might need [your service]. For each: name, website, decision maker if public, one specific detail about them, and a 3-sentence personal email draft. Put it all in a sheet. Do not send anything.",
   ["Follow anti-spam law (in the U.S., CAN-SPAM) and each platform's rules.", "Never send in bulk without reading each message."],
   [xsrc("2090800086477389964", "lead-finding workflow with human approval before sending")],
   xpop("2090800086477389964"), tags=["leads", "sales", "outreach", "small business"]),

uc("give-your-agent-its-own-email-address", "Give your agent its own email address", "inbox",
   "Give your agent an inbox of its own. Then you or anyone else can forward it jobs, like a meeting request it turns into a calendar invite with prep notes.",
   ["Gets its own email address.", "Reads whatever arrives there.", "Turns requests into actions, like adding a calendar invite.", "Researches the sender and adds prep notes."],
   "A forwarding address for chores. Forward it a request and it gets handled.", "Medium",
   [T("grok-bot"), T("gemini-spark", "Can be emailed at a dedicated Gmail address"), T("claude", "Via an email connector")],
   "When an email arrives at your address: if it's a meeting request, find a 30-minute slot in my calendar next week, create a draft invite and add 3 bullet points of research about the sender. If it's anything else, summarize it and ask me what to do. Never reply to the sender without my OK.",
   ["Anyone who knows the address can email it. Tell it to ignore instructions from strangers."],
   [xsrc("2110022751247556669", "gave an agent its own inbox; it turned an email into a prepped calendar invite")],
   xpop("2110022751247556669"), tags=["email", "calendar", "meetings", "forwarding"]),

uc("job-match-digest", "Get a daily digest of jobs that actually fit you", "work",
   "A scheduled workflow pulls new listings, scores them against your CV and emails you the best matches with draft notes. You still apply.",
   ["Reads your CV and preferences once.", "Twice a day, pulls new listings from job boards.", "Skips ones you've already seen.", "Scores each job for fit and keeps the good ones.", "Emails you a digest with a draft note for each."],
   "A short daily email of well-matched jobs, ready for you to apply.", "Advanced",
   [T("n8n", "Shared workflow on Reddit"), T("gemini-spark", "Its page shows “find and track” job searches"), T("grok-bot"), T("chatgpt", "Tailor one application at a time")],
   "Every weekday at 9am, find new [job title] roles in [location/remote] posted in the last 24 hours. Score each 1–10 against my CV below. For any 7 or above, give me: the link, why it fits, gaps to address, and a 3-sentence note to the hiring manager. Don't apply to anything.\n\nMy CV: [paste]",
   ["Don't auto-apply. Redditors report job sites block bots and can ban accounts; review every application yourself.", "Make sure tailored CVs don't invent experience."],
   [N8N_JOBS, N8N_JOBS2, xsrc("2104457847010693524", "Career Agent: evaluate jobs, tailor resumes, track applications")],
   {"platform": "reddit", "url": N8N_JOBS["url"], "author": "u/CoderOO7", "posted_at": "2026-04-22", "upvotes": 48, "comments": 40, "measured_at": MEASURED, "note": "Score as shown in a search-index copy on 2026-10-20; Reddit blocks direct reads from our server."},
   tags=["job search", "resume", "n8n", "career"]),
]
NEW += [
uc("school-email-digest", "Turn the flood of school emails into one weekly digest", "family",
   "Label school emails and let an agent read them weekly. It pulls out deadlines, forms, payments and events, without duplicates.",
   ["Reads emails with your “School” label, including linked newsletters.", "Pulls out deadlines, permission slips, payments and events.", "Ignores grades and activities that aren't your kids'.", "Removes duplicates and puts urgent things first.", "Can add events to your calendar and to-dos to your list."],
   "One digest a week with nothing important buried in a newsletter link.", "Medium",
   [T("claude-cowork", "Step-by-step setup in the source"), T("gemini-spark", "Google's own example: school updates digest"), T("meta-muse", "Meta's launch essay describes this"), T("grok-bot")],
   "Every Sunday at 6am, read all emails labeled 'School' that aren't labeled 'Processed'. Open any newsletter links. Extract permission slips, payments, deadlines, events and anything needing a reply. My kids: [initials, grades, schools]. Ignore other grades and [sports]. Put district-wide closures at the top, remove duplicates, and label each email 'Processed' when done. Draft replies for my approval; don't send.",
   ["Use initials instead of names if you prefer (the source author does).", "Have it draft, not send, replies to teachers."],
   [SCHOOL, MUSE_BLOG, SPARK_BLOG, xsrc("2108579992456327489", "school email manager prompt")],
   None, source_date="2026-09-08", tags=["school", "kids", "email", "deadlines", "permission slips"]),

uc("hidden-subscription-fee-finder", "Check every card statement for new or hidden fees", "money",
   "Each month a bot reads your card statement and flags new subscriptions, hidden fees and price creep.",
   ["Runs when your statement arrives each month.", "Lists every recurring charge.", "Flags anything new, any fees and any price increases.", "Drafts cancellations for the ones you choose."],
   "A monthly list of new, hidden or rising charges.", "Easy",
   [T("gemini-spark", "Google's own example task"), T("grok-bot"), T("claude-cowork"), T("chatgpt", "Upload a statement PDF")],
   "Each month when my [bank] statement email arrives, read it and list: every recurring charge, any new subscription since last month, any fee, and any charge that went up. Show the amount and the date. Draft a cancellation for any I mark CANCEL. Don't contact anyone without my OK.",
   ["Statements are sensitive. Prefer tools that say they don't train on your data, and remove account numbers if you upload PDFs."],
   [SPARK_BLOG, src("Engadget: Gemini Spark can spot hidden fees in credit card bills", "https://www.engadget.com/2176556/googles-gemini-spark-is-an-agentic-ai-assistant/")],
   None, source_date="2026-05-19", tags=["subscriptions", "fees", "statements", "budget"]),

uc("monday-inbox-recap-and-todo", "Get a Monday recap of your inbox and a to-do list", "inbox",
   "Every Monday a bot reviews last week's email, recaps what matters and suggests a ranked to-do list.",
   ["Reads the past week's email.", "Pulls out decisions, requests and deadlines.", "Writes a short recap.", "Suggests a ranked to-do list and blocks focus time."],
   "A 2-minute Monday briefing and a ranked to-do list.", "Easy",
   [T("gemini-spark", "Google's own example schedule"), T("grok-bot"), T("claude-cowork"), T("chatgpt-dots")],
   "Every Monday at 9:00 AM, scan my inbox and review my emails from the past week. Give me a quick recap of the most important updates and a suggested, prioritized to-do list for this week. Also suggest calendar blocks for focused work, but ask before adding them.",
   ["Start with summaries only, then let it draft replies once you trust it."],
   [SPARK_PAGE, xsrc("2108849705367327126", "beginner list of daily Grok Bot jobs")],
   None, source_date="2026-10-10", tags=["email", "to-do", "weekly", "productivity"]),

uc("flag-only-emails-that-need-a-reply", "Only see the emails that actually need a reply", "inbox",
   "A simple triage bot flags anything needing a reply within 24 hours and moves the noise out of the way.",
   ["Reads new email as it arrives.", "Flags messages that need a reply from you within a day.", "Labels newsletters, receipts and promos.", "Leaves everything else alone."],
   "An inbox where the flagged emails are the only ones you need to answer.", "Easy",
   [T("gemini-spark"), T("grok-bot"), T("zapier"), T("claude-cowork")],
   "Go through my new email every hour. If a message needs a reply from me within 24 hours, star it and add a one-line reason. Label newsletters 'Read later', receipts 'Receipts' and promotions 'Promos', and archive them. Never delete or reply.",
   ["Archive, don't delete, while you're testing. You can always undo an archive."],
   [RAI, RAI_LIVE],
   None, source_date="2026-08-18", tags=["email", "triage", "inbox zero"]),

uc("email-ghostwriter-style-guide", "Teach a bot to write emails that sound like you", "work",
   "Have the bot read your last 50 sent emails, write a style guide, then use it for every draft.",
   ["Reads a sample of your sent emails.", "Writes a short style guide: tone, length, greetings, sign-offs.", "Saves it as a reusable skill.", "Uses it whenever it drafts for you."],
   "Drafts that sound like you, so you edit less.", "Easy",
   [T("gemini-spark", "Google's own example skill"), T("grok-bot", "Save it as a skill"), T("claude")],
   "Read through the last 50 emails I wrote and turn them into a style guide for how I write emails. Turn that into a skill that gets used every time I ask you to draft an email. Call the skill 'ghostwriter'. Drafts only; never send.",
   ["Sent emails are private. Skip threads with other people's sensitive details."],
   [SPARK_PAGE, xsrc("2102768278812680522", "had Claude read 12 months of sent email so drafts sound like him")],
   None, source_date="2026-05-19", tags=["email", "writing", "drafts", "skills"]),

uc("log-new-client-inquiries", "Log every new client inquiry automatically", "business",
   "When an inquiry email arrives, the bot pulls out the client's name and requested date, logs it in your tracker and sets up a folder.",
   ["Watches for inquiry emails (“are you available on…”).", "Pulls out the name, date and what they want.", "Adds a row to your client tracker sheet.", "Creates a folder named after the client."],
   "A client tracker that fills itself in, so no inquiry slips.", "Easy",
   [T("gemini-spark", "Google's own example"), T("zapier"), T("make"), T("grok-bot")],
   "When I receive an email asking about my [service], extract the client's name, requested date and request, and log it in my 'Client Tracker' sheet. Then create a new folder named after the client. Draft a friendly reply with my availability, but don't send it.",
   ["Check the dates it pulls out. A wrong date costs you a booking."],
   [SPARK_PAGE],
   None, source_date="2026-05-19", tags=["clients", "freelance", "photography", "crm"]),

uc("replace-a-paid-app-with-a-shortcut", "Replace a paid app with a shortcut your agent helps you build", "money",
   "Ask your agent whether your phone can already do what a paid app does, and have it walk you through building it.",
   ["Asks what the app does for you.", "Checks whether your phone has built-in tools for it, like Apple Shortcuts.", "Walks you through building it step by step.", "Helps you test it before you cancel the subscription."],
   "A homemade tool and one less subscription.", "Easy",
   [T("chatgpt"), T("claude"), T("gemini"), T("grok")],
   "I pay [$/month] for [app] to do [job]. Can my [iPhone/Android/computer] do this with built-in tools? If yes, walk me through building it one step at a time. Wait for me to say 'done' before the next step. Then help me test it.",
   ["Test it for a week before cancelling the paid app."],
   [xsrc("2110401529882513728", "an agent walked him through an Apple Shortcut; he cancelled a $10/mo app")],
   xpop("2110401529882513728"), tags=["subscriptions", "apple shortcuts", "save money"]),

uc("morning-news-digest", "Get a 2-minute morning digest on topics you care about", "inbox",
   "A bot reads the news on your topics every morning and sends you a short plain-English digest, or even an audio version.",
   ["Checks news on your chosen topics every morning.", "Picks the few stories that matter.", "Explains each in plain English.", "Sends it as a message, a document or audio."],
   "A short daily briefing instead of doom-scrolling.", "Easy",
   [T("meta-muse", "“Morning news digest” is one of Muse's skills"), T("grok-bot"), T("gemini-spark"), T("chatgpt-dots")],
   "Every morning at 7am, send me the 5 most important stories about [topics] from the last 24 hours, in plain English, 2 sentences each, with a link to the original source. Skip anything that's just opinion.",
   ["Click through on anything important; summaries can be wrong."],
   [src("Meta Help Center: How Muse works with skills (morning news digest)", "https://www.meta.com/help/artificial-intelligence/2797651547267109/", "official"), xsrc("2108849705367327126", "“Every morning, send me the 5 biggest AI stories in plain English”")],
   None, source_date="2026-10-10", tags=["news", "briefing", "daily", "podcast"]),

uc("watch-for-one-important-letter", "Watch your email for one important letter or reply", "inbox",
   "Waiting on a visa decision, a refund or a reply from the landlord? Have a bot watch for it and ping you.",
   ["Takes who or what you're waiting for.", "Checks your inbox daily.", "Pings you when it arrives, with a summary.", "Tells you if a deadline is attached."],
   "A ping the moment it arrives, so you stop checking.", "Easy",
   [T("grok-bot"), T("gemini-spark"), T("zapier", "A simple email filter rule plus a text alert")],
   "Check my email daily for a message from [sender/organization] about [topic]. When it arrives, message me a 3-line summary and any deadline or action it asks for. Stop checking once it arrives.",
   ["Look in spam yourself too; some bots can't see it."],
   [RAI],
   None, source_date="2026-08-18", tags=["email", "alerts", "waiting"]),

uc("sell-on-marketplace-with-rules", "Sell on Marketplace with an agent, with safety rules set first", "business",
   "Agents can answer buyers and schedule pickups, but set rules first. One story tells of an agent sharing an address and booking a pickup when the seller was out.",
   ["Answers buyer questions using your listing details.", "Proposes pickup times from your calendar.", "Asks you before sharing any address or agreeing a price.", "Keeps a log of every buyer conversation."],
   "Buyer messages handled, with you in charge of price, address and timing.", "Medium",
   [T("meta-muse"), T("grok-bot"), T("chatgpt", "Write the listing and replies yourself")],
   "Help me sell [item] on [Marketplace]. You may answer questions about condition and size using this description: [details]. You may NOT: share my address, agree a price under [$], or schedule a pickup, without asking me first. Only offer pickup times from my calendar where I'm marked 'home'.",
   ["Never let a bot share your home address without your OK.", "Meet in a public place for higher-value items."],
   [xsrc("2104442538254123102", "a reported Muse Marketplace mix-up (address shared, pickup when seller was out)")],
   xpop("2104442538254123102"), tags=["marketplace", "selling", "safety"]),

uc("household-restock-list", "Keep a household essentials list and reorder on time", "shopping",
   "A bot keeps a running list of essentials, asks once a week what's low and builds the reorder.",
   ["Keeps a list of your usual essentials.", "Once a week, asks what's running low.", "Builds a reorder list or cart.", "Reminds you about anything you forgot last time."],
   "No more running out of toilet paper or lunchbox snacks.", "Easy",
   [T("grok-bot"), T("meta-muse"), T("chatgpt-work"), T("google-universal-cart", "Restock alerts on saved items")],
   "Maintain a list of our household essentials: [list]. Every Saturday morning, ask me what we're running low on. Build a cart with those items at [store] and stop before checkout. Remember what we bought and when, and remind me if something usually runs out by now.",
   ["Review the cart before paying."],
   [xsrc("2108579992456327489", "household restocking manager prompt")],
   None, source_date="2026-10-09", tags=["groceries", "household", "restock"]),

uc("weekend-family-activities", "Get 5 weekend activity ideas that fit your kids and the weather", "family",
   "Every Friday, get activity ideas matched to your kids' ages, the weather and your budget, with a rainy-day backup.",
   ["Checks the weekend forecast for your area.", "Finds activities that fit your kids' ages and interests.", "Adds costs and whether booking is needed.", "Includes a wet-weather alternative."],
   "A Friday list of 5 doable weekend plans.", "Easy",
   [T("grok-bot"), T("meta-muse"), T("gemini-spark"), T("chatgpt")],
   "Every Friday, suggest 5 family activities for this weekend based on our children's ages [ages], interests [interests], location [town], the weather and a budget of [$]. Include estimated costs, booking requirements and a wet-weather alternative.",
   ["Check opening hours before you go; listings go out of date."],
   [xsrc("2108579992456327489", "family activities planner prompt")],
   None, source_date="2026-10-09", tags=["kids", "weekend", "activities"]),

uc("medication-reminders-for-a-parent", "Set up medication and appointment reminders for a parent", "health",
   "Family agents can remind an older parent about medication and book routine appointments, with the family kept in the loop.",
   ["Sends medication reminders at set times.", "Asks for a quick “done” reply and tells the family if there's no reply.", "Books routine appointments, like the dentist, after a family member approves.", "Keeps a simple log."],
   "Reminders that actually reach Mum or Dad, and a family that knows they did.", "Easy",
   [T("meta-muse", "Reminders are built in"), T("grok-bot"), T("instinct")],
   "Remind [Mum] at [8am and 8pm] to take her [medication] by message. Ask her to reply 'done'. If she hasn't replied within 1 hour, message me. Once a month, ask me whether any appointments need booking. Never change medication instructions and never give medical advice.",
   ["Reminders only. Never let a bot change doses or give medical advice. Ask the pharmacist."],
   [xsrc("2109330165381910817", "family agent: “remind Grandma to take her meds”, book dentist appointments")],
   None, source_date="2026-10-11", tags=["aging parents", "medication", "reminders", "caregiving"]),

uc("pay-with-a-single-use-virtual-card", "Let your agent pay with a single-use virtual card", "money",
   "When an agent books or buys for you, give it a one-time virtual card so it can't be charged again.",
   ["You create a single-use or merchant-locked virtual card in your bank or card app.", "The agent uses that card for one booking.", "The card stops working after one use or past its limit."],
   "Agent purchases with a built-in spending limit.", "Easy",
   [T("chatgpt-work"), T("instinct"), T("grok-bot"), T("meta-muse")],
   "For this booking, use only the virtual card ending in [last 4]. Its limit is [$]. If the total is higher, stop and ask me. Never save this card to the site.",
   ["Check whether your bank offers single-use or merchant-locked cards before you start."],
   [xsrc("2105830877259346021", "agent booked a hotel with a one-time-use virtual card")],
   xpop("2105830877259346021"), tags=["payments", "safety", "virtual card", "booking"]),

uc("daily-ads-and-sales-report", "Get your ads and sales numbers every morning without logging in", "business",
   "A bot logs into your ad and sales dashboards (read-only) and sends a morning summary with what changed.",
   ["Checks your ad accounts and sales dashboard each morning.", "Compares yesterday with the past week.", "Highlights big changes and the likely reason.", "Sends one short report."],
   "A 1-minute morning report instead of 5 dashboards.", "Medium",
   [T("claude-cowork"), T("grok-bot"), T("zapier"), T("make")],
   "Every morning at 7am, pull yesterday's results from [ad platforms] and [store/sales platform]. Give me: spend, sales, cost per sale, and anything that changed more than 20% from the 7-day average, with a likely reason. Read-only: never change budgets or ads.",
   ["Read-only access first. Don't let it change budgets until you've watched it for weeks."],
   [xsrc("2108012315602034988", "Grok bot team sends an ads report every morning"), src("X post by @LorenHogueInc (2026-10-13): Apple and Meta ad reports every morning via Claude Cowork", "https://x.com/LorenHogueInc/status/2110083294792716367", "x")],
   xpop("2108012315602034988"), tags=["ads", "reports", "ecommerce", "small business"]),
]
CATMAP = {"paperwork": "inbox", "bookings": "travel", "health": "health", "money": "money", "family": "family", "time": "inbox", "work": "work", "side-hustles": "business", "small-business": "business"}
OLD_TOOL_SUGGEST = {"cancel-a-subscription": ["chatgpt-work", "meta-muse"], "book-an-appointment-with-an-ai-agent": ["instinct", "meta-muse"], "clean-up-your-email-inbox": ["gemini-spark", "grok-bot"], "weekly-meal-plan-and-grocery-list": ["grok-bot"], "plan-a-trip-itinerary": ["grok-bot"], "chase-an-unpaid-invoice": ["grok-bot", "zapier"], "reply-to-customer-reviews": ["zapier"]}
old = json.load(open(D("research", "use-cases.v1.json")))
migrated = []
for o in old:
    n = dict(o)
    n["category"] = CATMAP[o["category"]]
    n["date_added"] = "2026-10-19"
    n["source_date"] = None
    n["summary"] = o["problem"]
    n["what_the_bot_does"] = o["steps"]
    n["what_you_end_up_with"] = o["outcome"]
    n["setup"] = []
    for s in n["sources"]: s.setdefault("kind", "x" if "x.com" in s["url"] else "reddit" if "reddit.com" in s["url"] else "article")
    existing = {t["id"] for t in n["tools"]}
    for t in OLD_TOOL_SUGGEST.get(o["slug"], []):
        if t not in existing: n["tools"].append({"id": t})
    n["popularity"] = None
    if o["slug"] == "moving-checklist-and-change-of-address":
        n["popularity"] = xpop("2072663153532666045"); n["source_date"] = "2026-07-02"
    n["last_checked"] = o.get("last_checked", "2026-10-19")
    n["origin"] = "migrated-2026-10-19"
    migrated.append(n)

allu = NEW + migrated
slugs = [x["slug"] for x in allu]
assert len(slugs) == len(set(slugs)), "duplicate slug"
for x in allu: assert x["category"] in {c["slug"] for c in CATS}, x["slug"]
for x in allu:
    for t in x["tools"]: assert t["id"] in TOOLS, (x["slug"], t["id"])
json.dump(CATS, open(D("data", "categories.json"), "w"), indent=1, ensure_ascii=False)
json.dump(TOOLS, open(D("data", "tools.json"), "w"), indent=1, ensure_ascii=False)
json.dump(allu, open(D("data", "use-cases.json"), "w"), indent=1, ensure_ascii=False)
print(len(NEW), "new +", len(migrated), "migrated =", len(allu))
