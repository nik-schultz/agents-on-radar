import json
D = "2026-10-19"
AC = lambda q: {"label": f"Google search suggestions for “{q}” (checked {D})", "url": "https://www.google.com/search?q=" + q.replace(" ", "+")}
MENLO25 = {"label": "Menlo Ventures, 2025 State of Consumer AI (survey of 5,000+ US adults)", "url": "https://menlovc.com/perspective/2025-the-state-of-consumer-ai/"}
MENLO26 = {"label": "Menlo Ventures, 2026 State of Consumer AI", "url": "https://menlovc.com/wp-content/uploads/2026/09/menlo_ventures_consumer_ai_report-2026.pdf"}
EY = {"label": "EY AI Sentiment Study, wave 4 (2026)", "url": "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/ai/documents/ey-gl-ai-sentiment-study-wave-04-2026.pdf"}
CHANNELV = {"label": "Search Engine Watch on Channel V Media's AI Barometer (June 2026 survey, 7,675 US adults)", "url": "https://searchenginewatch.com/four-in-ten-americans-would-hand-ai-a-chore-survey-finds/"}
OAI_CB = {"label": "OpenAI Help: Using cloud browser in ChatGPT", "url": "https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt"}
OAI_DC = {"label": "OpenAI Help: Data controls in ChatGPT", "url": "https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt"}
HC_INT = {"label": "HealthCare.gov: Internal appeals", "url": "https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/"}
HC_EXT = {"label": "HealthCare.gov: External review", "url": "https://www.healthcare.gov/appeal-insurance-company-decision/external-review/"}
KFF = {"label": "KFF: Claims Denials and Appeals in ACA Marketplace Plans in 2024 (Mar 2026)", "url": "https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/"}
CHAT4 = [{"id": "chatgpt"}, {"id": "claude"}, {"id": "gemini"}, {"id": "grok"}]
PRIV = "Remove Social Security numbers, account numbers, member IDs and birth dates before you paste or upload anything. In ChatGPT you can use Temporary Chat or turn off “Improve the model for everyone” under Settings › Data controls."

U = []

# ---------- FLAGSHIP 1 ----------
U.append(dict(
 slug="appeal-a-health-insurance-denial", category="health", flagship=True,
 title="Appeal a health insurance denial with AI",
 problem="Your health insurance said no to a treatment, test or medicine, and the letter is full of codes and jargon.",
 outcome="A clear, polite appeal letter that answers the insurer's exact reason for saying no, a checklist of documents to attach, and your deadlines on a calendar.",
 prompt="""You are helping me appeal a health insurance denial. I am not a lawyer or doctor, so explain things simply.

Here is the denial letter (personal details removed):
[PASTE DENIAL LETTER OR EXPLANATION OF BENEFITS]

My situation in plain words:
[WHAT TREATMENT, WHY MY DOCTOR ORDERED IT, WHAT I'VE ALREADY TRIED]

Please:
1. Tell me in 3 bullet points why they said no, quoting the exact reason from the letter.
2. List my deadline to appeal and any other dates mentioned in the letter. If no date is in the letter, say so.
3. Make a checklist of documents I should gather (for example a letter from my doctor, medical records, the plan's coverage policy).
4. Write a one-page appeal letter that answers each stated reason, asks for a written decision, and leaves [BLANKS] for anything I need to fill in. Do not invent medical facts, studies or policy wording. If you are unsure, say so.
5. List 3 questions I should ask my doctor's office to make the appeal stronger.""",
 tools=[{"id": "chatgpt"}, {"id": "claude"}, {"id": "gemini"}, {"id": "grok"}],
 time_saved="Editor's estimate: a first draft in about 30 minutes instead of an evening of research",
 difficulty="Medium",
 steps=[
  "Find the denial letter or Explanation of Benefits (EOB) and your plan's appeal instructions.",
  "Remove personal details, then paste the letter and your situation into the prompt below.",
  "Ask your doctor's office for a letter supporting the treatment and any records the AI's checklist mentions.",
  "Read the draft line by line. Fix anything that isn't true, then send it the way your plan asks (portal, mail or fax) and keep copies.",
  "Put the decision deadline on your calendar. If the internal appeal fails, ask for an external review."],
 watch_out=[
  "AI can invent studies, policy quotes or facts. Never send anything you haven't checked against your own papers.",
  PRIV,
  "This is help with paperwork, not medical or legal advice. Your state's Consumer Assistance Program can help for free."],
 faq=[
  {"q": "How long do I have to appeal?", "a": "Under the federal rules described on HealthCare.gov, you must file an internal appeal within 180 days (6 months) of getting the denial notice. Your letter should list your exact deadline."},
  {"q": "How fast does the insurer have to answer?", "a": "HealthCare.gov says an internal appeal must be decided within 30 days for a service you haven't had yet and within 60 days for one you already received. Urgent cases can move much faster."},
  {"q": "What if they still say no?", "a": "You can usually ask for an external review by an independent reviewer. HealthCare.gov says to request it in writing within 4 months of the final denial, and the insurer must accept the reviewer's decision."},
  {"q": "Does this work for Medicare, Medicaid or my employer plan?", "a": "Those plans have their own appeal steps. The steps in this guide still help, but follow the instructions and deadlines printed in your own denial letter."}],
 sources=[HC_INT, HC_EXT, KFF,
  {"label": "Reddit r/AgingParents: discharge appeal written with ChatGPT help (Feb 2026)", "url": "https://www.reddit.com/r/AgingParents/comments/1r1eimf/"},
  {"label": "Hacker News comment: parent used ChatGPT to work through an external appeal", "url": "https://news.ycombinator.com/item?id=45734582"},
  AC("using ai to appeal insurance denial")],
 real_examples=[
  {"text": "A user in r/AgingParents says ChatGPT helped word an appeal of their 90-year-old mother's rehab discharge, and the appeal was approved.", "source": "Reddit r/AgingParents, Feb 2026", "url": "https://www.reddit.com/r/AgingParents/comments/1r1eimf/", "verification": "Self-reported; not independently verified"},
  {"text": "A parent on Hacker News says ChatGPT guided them through an external appeal for their child's surgery, and the procedure was approved 10 days after the denial.", "source": "Hacker News comment", "url": "https://news.ycombinator.com/item?id=45734582", "verification": "Self-reported; not independently verified"}],
 tags=["insurance", "denied claim", "prior authorization", "EOB", "appeal letter", "external review"],
 guide=dict(
  intro="Getting a “denied” letter from your health insurer feels final. It usually isn't. You have a legal right to appeal, and an AI chatbot is very good at the hardest part: turning a confusing letter into a clear, organized reply. You still make the decisions and check every word.",
  sections=[
   {"h": "Why bother appealing?", "p": ["Very few people appeal. KFF looked at federal data for HealthCare.gov plans in 2024: insurers denied 19% of in-network claims, but people appealed fewer than 1% of those denials. Insurers upheld about two-thirds (66%) of the internal appeals that were filed, which means some did go the other way. You can't know which group you're in unless you ask."]},
   {"h": "What you need before you start", "li": ["The denial letter or Explanation of Benefits (EOB).", "Your plan's appeal instructions (often on the back of the letter or in your online account).", "Your member ID and claim number (keep these out of the chatbot; add them to the final letter yourself).", "A rough timeline: when you saw the doctor, what was ordered, what you've already tried."]},
   {"h": "Step 1: Have the AI decode the letter", "p": ["Paste the letter with personal details removed and ask: “Explain why this was denied in plain English, and quote the exact reason.” Denials often come down to one of a few reasons: the plan says it isn't medically necessary, it needed prior approval, the provider was out of network, or it's treated as experimental. HealthCare.gov lists these as reasons you can appeal."]},
   {"h": "Step 2: Get your deadlines straight", "p": ["Ask the AI to pull every date out of the letter. Then check them yourself. Under the federal rules HealthCare.gov describes, you have 180 days to file an internal appeal. The insurer then has 30 days to decide if you haven't had the care yet, or 60 days if you have. If your health is at serious risk, you can ask for an expedited (fast) appeal and an external review at the same time."]},
   {"h": "Step 3: Build the evidence list", "p": ["The strongest appeals usually include a letter from your doctor explaining why you need this treatment. Ask the AI: “What should my doctor's letter say to answer this specific denial reason?” Then send that list to your doctor's office. It saves them time and makes it more likely they'll write it."]},
   {"h": "Step 4: Draft the appeal letter", "p": ["Use the prompt on this page. A good appeal letter is short, polite and specific: it names the claim, quotes the reason for denial, answers it point by point, lists what's attached, and asks for a written decision. Tell the AI not to invent studies or policy wording. If it cites something, find it yourself before you keep it."]},
   {"h": "Step 5: Send it and keep records", "p": ["Send the appeal exactly the way your plan says (portal, mail or fax). HealthCare.gov recommends keeping copies of everything and notes from every phone call: the date, time, the person's name and what they said. You can ask the AI to make you a simple call-log template."]},
   {"h": "If they still say no: external review", "p": ["If the insurer upholds the denial, you can usually ask for an external review by an independent reviewer. HealthCare.gov says to file within 4 months of the final denial. Standard reviews are decided within 45 days, urgent ones within 72 hours, and the insurer must accept the reviewer's decision. It costs nothing under the federal process and no more than $25 in other processes."]},
   {"h": "Where to get free human help", "p": ["Every state has a Consumer Assistance Program or Department of Insurance that can explain your rights, and HealthCare.gov says the Consumer Assistance Program can even file an appeal for you. Your doctor's billing office has also seen many denials and can tell you what usually works with your insurer."]}]),
 last_checked=D))

# ---------- FLAGSHIP 2 ----------
U.append(dict(
 slug="understand-a-confusing-letter", category="paperwork", flagship=True,
 title="Understand a confusing letter or notice (and know what to do next)",
 problem="A letter from a government office, insurer, bank or landlord landed in your mailbox and you can't tell if it's important, a bill, a scam, or nothing.",
 outcome="A plain-English summary, the action you need to take (if any), the deadline, a scam check, and a ready-to-send reply if one is needed.",
 prompt="""I got this letter and I don't fully understand it. Personal details are removed.

[PASTE THE LETTER TEXT, OR UPLOAD A PHOTO WITH PERSONAL DETAILS COVERED]

Please answer in plain English, at about an 8th-grade reading level:
1. Who is this from and what is it about, in 2 sentences?
2. Do I need to do anything? If yes, what exactly, and by what date?
3. What happens if I do nothing?
4. Are there signs this could be a scam (pressure, threats, odd payment methods, strange links)? Tell me how to check it using the organization's official website, not the contact details in the letter.
5. If a reply is needed, write a short, polite reply I can send, with [BLANKS] for anything you don't know.
If anything is unclear or you are guessing, say so.""",
 tools=CHAT4,
 time_saved="Editor's estimate: about 5–10 minutes to understand a letter that might otherwise sit in a pile for weeks",
 difficulty="Easy",
 steps=[
  "Cover or remove personal numbers (Social Security, account, case numbers) before taking a photo or pasting text.",
  "Paste the letter into the prompt and read the summary.",
  "Look up the sender's official website or phone number yourself, and confirm the letter is real before you pay or share anything.",
  "Put any deadline on your calendar right away.",
  "If a reply is needed, edit the AI's draft so every detail is true, then send it the way the letter asks."],
 watch_out=[
  "Scammers send official-looking letters too. The IRS warns that impersonators demand payment “now or else”, threaten arrest, and use odd links.",
  PRIV,
  "For anything with legal consequences (court papers, eviction, immigration, debt lawsuits), use the AI to understand it, then talk to a legal aid office or a lawyer."],
 faq=[
  {"q": "Can I just upload a photo of the letter?", "a": "Yes, most chat AIs read photos. Cover your account numbers, ID numbers and signature first."},
  {"q": "Which AI is best for this?", "a": "Any of the big free chat apps (ChatGPT, Claude, Gemini, Grok) can do this well. Use the one you already have."},
  {"q": "How do I know the AI got it right?", "a": "Ask it to quote the exact sentence each answer comes from. Then check those sentences in the letter yourself."}],
 sources=[{"label": "IRS: Recognize tax scams and fraud", "url": "https://www.irs.gov/help/tax-scams/recognize-tax-scams-and-fraud"}, OAI_DC, AC("ai to read my pdf"), AC("use ai to write a letter")],
 real_examples=[],
 tags=["letter", "notice", "mail", "government", "IRS", "scam check", "explain", "reply"],
 guide=dict(
  intro="Most of us have a pile of letters we've been meaning to deal with. AI chatbots are excellent translators of official-speak. In a few minutes you'll know whether a letter matters, what it wants, and how to reply, without guessing.",
  sections=[
   {"h": "Step 1: Protect your personal information", "p": ["Before anything goes into a chatbot, cover or delete: Social Security numbers, account and policy numbers, case numbers, dates of birth and signatures. The AI doesn't need them to explain the letter. " + "If you use ChatGPT, Temporary Chat isn't used to train models (OpenAI says it may keep it up to 30 days for safety checks), and you can switch off “Improve the model for everyone” in Settings › Data controls."]},
   {"h": "Step 2: Ask for the four things that matter", "li": ["Who sent it and what it's about.", "Whether you need to act, and by when.", "What happens if you don't.", "Whether anything looks like a scam."]},
   {"h": "Step 3: Check it's real, using your own lookup", "p": ["Don't call the phone number printed in a suspicious letter. Look up the organization's official website or the number on your card or account, and confirm there. The IRS's own scam page lists the warning signs: demands to pay “now or else”, threats of arrest or deportation, and odd or misspelled links. Ask the AI to point out any of those in your letter."]},
   {"h": "Step 4: Make the deadline impossible to miss", "p": ["Ask: “Turn the action and deadline into a calendar reminder with a one-line note.” Then add it to your phone's calendar. Many problems with letters come from missing a date, not from the letter itself."]},
   {"h": "Step 5: Reply in two minutes", "p": ["If the letter asks for a response, ask the AI for a short, polite reply that includes your reference number (add it yourself after), what you're sending, and a request for written confirmation. Read it and fix anything that isn't exactly true before you send."]},
   {"h": "When to get a human", "p": ["Court papers, eviction notices, immigration letters and lawsuits about debt can have strict deadlines and serious consequences. Use the AI to understand what the paper says, then contact your local legal aid office or a lawyer the same week."]}]),
 last_checked=D))

# ---------- FLAGSHIP 3 ----------
U.append(dict(
 slug="book-an-appointment-with-an-ai-agent", category="bookings", flagship=True,
 title="Have an AI agent find and book an appointment for you",
 problem="You need a DMV slot, a restaurant table or a service appointment, and you don't have time to click through booking sites or keep checking for openings.",
 outcome="The agent finds options that fit your times and rules, shows you its pick, and books it only after you say yes.",
 prompt="""Find and book an appointment for me. Ask me before you confirm anything or pay.

What: [E.G. DMV LICENSE RENEWAL / DINNER FOR 4 / OIL CHANGE]
Where: [CITY OR NEIGHBORHOOD, MAX DISTANCE]
When I can go: [DAYS AND TIME WINDOWS]
Must-haves: [E.G. WHEELCHAIR ACCESS, KID-FRIENDLY, UNDER $X]
Website to use, if I have a preference: [SITE OR 'YOUR CHOICE']

Rules:
- Show me your top 3 options with date, time, address and any fees before booking.
- Stop at the final confirmation screen and wait for my OK.
- Don't add paid extras, insurance or memberships.
- If a site needs me to sign in, pause and let me do it through the secure sign-in.
- If you can't finish, tell me exactly where you stopped and give me the link.""",
 tools=[{"id": "chatgpt-work", "note": "Can use websites for you, including ones you sign in to; asks before bookings or payments."},
        {"id": "gemini-opentable", "note": "Can check, book and cancel OpenTable restaurant reservations."},
        {"id": "claude"}, {"id": "grok"}],
 time_saved="Editor's estimate: 10–30 minutes of clicking per booking, more if you'd otherwise keep checking for openings",
 difficulty="Easy",
 steps=[
  "Pick an agent that can actually use websites (see the tools list). Chat-only AIs can find options but you'll book yourself.",
  "Copy the prompt and fill in what, where, when and your must-haves.",
  "If the agent asks you to sign in, use its secure sign-in form. Never type passwords or card numbers into the chat.",
  "Review its top options and the exact details on the confirmation screen.",
  "Say yes, then check the confirmation email and add it to your calendar."],
 watch_out=[
  "OpenAI says some websites block automated agents. If that happens, the agent should hand the task back to you.",
  "Double-check the date, time, location and total price before you approve. Agents can misread a page.",
  "Never paste passwords, security codes or payment details into the conversation. OpenAI's own guidance says the same."],
 faq=[
  {"q": "Can a free AI book things for me?", "a": "Usually not end to end. OpenAI says ChatGPT's cloud browser is on paid plans only (not Free or Go). Gemini can book OpenTable restaurant reservations through the app. Free chat AIs can still find options and give you the link."},
  {"q": "Will it book something without asking me?", "a": "OpenAI says ChatGPT is designed to ask before actions like confirming a booking or making a payment. Our prompt also tells the agent to stop at the final screen. Always read what you're approving."},
  {"q": "What can't Gemini do with OpenTable?", "a": "Google says Gemini can't modify an existing reservation (it gives you a link instead), process payments, show reviews or read menus."},
  {"q": "Is it safe to let an agent sign in to my accounts?", "a": "OpenAI says credentials typed into its secure sign-in form go to the remote browser and aren't visible to the model or stored by ChatGPT. You can clear saved site data in Settings › Cloud browser. Only connect accounts you're comfortable with."}],
 sources=[OAI_CB, {"label": "Google Gemini Help: Find, book & manage reservations on OpenTable", "url": "https://support.google.com/gemini/answer/17090712"}, CHANNELV, EY, AC("ai agent to book appointments")],
 real_examples=[],
 tags=["appointment", "reservation", "restaurant", "DMV", "booking", "agent", "schedule"],
 guide=dict(
  intro="This is one of the first everyday jobs AI agents can really do, not just talk about. In a June 2026 survey reported by Search Engine Watch, booking a restaurant was the most popular task people would hand to an AI agent (12.1% chose it). EY's 2026 study found 21% would prefer an AI assistant that books doctor's appointments for them. Here's how to do it safely.",
  sections=[
   {"h": "Know which kind of AI you're using", "p": ["A chat AI (free ChatGPT, Claude, Gemini or Grok) can search, compare and hand you links. An agent can open websites, fill in forms and click through for you. Two options we checked:"], "li": ["ChatGPT Work with cloud browser: OpenAI says it can find a DMV appointment and prepare the booking for your approval, check restaurant availability and request quotes. Paid ChatGPT plans only.", "Gemini with OpenTable: Google says Gemini can check availability, book and cancel OpenTable reservations, and check the ones you have."]},
   {"h": "Step 1: Give clear rules, not just a wish", "p": ["“Book me a table Friday” leaves too much to guess. Our prompt covers what, where, when, must-haves and rules, including “stop at the final confirmation and wait for my OK” and “no paid extras.”"]},
   {"h": "Step 2: Handle sign-ins the safe way", "p": ["If a site needs your account, the agent should pause and ask you to sign in. In ChatGPT that's a secure sign-in form; OpenAI says the username and password you enter there aren't visible to the model and aren't stored. Never type a password, security code or card number into the chat itself."]},
   {"h": "Step 3: Review before you approve", "p": ["OpenAI says ChatGPT asks for confirmation before consequential actions like confirming a booking or paying. Read the date, time, address, number of people and total cost. If anything is off, tell it to go back."]},
   {"h": "Step 4: If it gets stuck", "p": ["Some websites block automated agents. OpenAI says you can take over the cloud browser yourself, or open the page in your own browser. Our prompt asks the agent to tell you exactly where it stopped so you can finish in a minute."]},
   {"h": "Good first tasks to try", "li": ["A restaurant reservation for a specific night.", "A DMV or passport appointment window.", "An oil change or haircut at a place you already use.", "Rescheduling a delivery (ask it to check with you before confirming)."]}]),
 last_checked=D))

def add(**k):
    k.setdefault("flagship", False); k.setdefault("real_examples", []); k.setdefault("last_checked", D); U.append(k)

add(slug="question-a-medical-bill", category="money", title="Question a medical bill that looks wrong",
 problem="A doctor or hospital bill is higher than you expected and you can't tell what you're paying for.",
 outcome="A plain-English breakdown of every line, a list of charges worth questioning, and a polite request for a corrected bill.",
 prompt="""Help me understand and question a medical bill. Personal details are removed.

Itemized bill (codes, descriptions, amounts): [PASTE]
What my insurance paid / my EOB says: [PASTE OR 'NO INSURANCE']

1. Explain each line in plain English.
2. Flag anything that looks like a duplicate, a service I may not have received, or a charge that doesn't match my EOB.
3. List questions to ask the billing office.
4. Draft a short, polite letter asking for a review and a corrected bill, and asking them to hold the bill from collections while it's reviewed.
Mark anything you're unsure about.""",
 tools=CHAT4, time_saved="Editor's estimate: about 30 minutes to go through a long bill line by line", difficulty="Medium",
 steps=["Call the billing office and ask for a fully itemized bill with billing codes.", "Remove personal details and paste the bill and your EOB into the prompt.", "Check each flagged line against your own records and your insurer's EOB.", "Send the letter, and write down who you talked to and when.", "If you were uninsured or got a surprise out-of-network bill, read the federal No Surprises rules at CMS."],
 watch_out=["AI can be wrong about billing rules. Treat its flags as questions to ask, not facts.", PRIV],
 faq=[{"q": "What's an itemized bill?", "a": "A bill that lists each service, supply and medicine separately, usually with billing codes. Summary bills often hide mistakes, so ask for the itemized version."}],
 sources=[{"label": "CMS: No Surprises Act protections", "url": "https://www.cms.gov/nosurprises"}, {"label": "Hacker News: Using AI to negotiate a $195k hospital bill down to $33k", "url": "https://news.ycombinator.com/item?id=45734582"}, AC("ai to negotiate medical bills")],
 real_examples=[{"text": "A widely shared post describes a family using Claude to go through itemized hospital codes and dispute charges; the poster says a $195,000 bill was settled at about $33,000.", "source": "Hacker News discussion", "url": "https://news.ycombinator.com/item?id=45734582", "verification": "Self-reported; not independently verified"}],
 tags=["medical bill", "hospital", "itemized", "EOB", "billing error", "dispute"])

add(slug="cancel-a-subscription", category="money", title="Find and cancel subscriptions you forgot about",
 problem="You're paying for apps and memberships you don't use, and cancelling each one is a maze.",
 outcome="A list of every recurring charge, which ones to cancel, and either the cancellation done by an agent or exact steps for each.",
 prompt="""Here are my last 2–3 months of card/bank transactions (account numbers removed):
[PASTE TRANSACTIONS]

1. List every recurring charge: name, amount, how often, and yearly cost.
2. Mark which look like subscriptions I might not use.
3. For each one I choose to cancel: [LIST], give me the exact cancellation steps (website path or phone), or if you can use websites, go to the official site and cancel it, asking me before the final click.
4. Remind me to check for a confirmation email for each.""",
 tools=[{"id": "chatgpt-work", "note": "Can go through a cancellation flow on the website and ask before the final step."}, {"id": "chatgpt"}, {"id": "claude"}, {"id": "gemini"}, {"id": "grok"}],
 time_saved="Editor's estimate: 15–30 minutes to audit a few months of statements", difficulty="Easy",
 steps=["Download or copy 2–3 months of transactions. Remove account numbers.", "Paste them into the prompt and review the recurring list.", "Decide what to cancel. Watch for annual plans that just renewed.", "Cancel through the official site or app store, or let an agent do it with your approval.", "Save each confirmation email until the next statement shows no charge."],
 watch_out=["Cancel only through the company's real site or your app store, never through a link in an unexpected email.", "Never paste card numbers or passwords into a chat."],
 faq=[{"q": "What about subscriptions billed through my phone?", "a": "Those are managed in your Apple or Google account settings, not on the company's website. Ask the AI for the exact menu path for your phone."}],
 sources=[OAI_CB, AC("use ai to cancel subscription"), MENLO25],
 tags=["subscription", "cancel", "recurring charge", "membership", "free trial"])

add(slug="write-a-complaint-that-gets-fixed", category="money", title="Write a complaint that actually gets a problem fixed",
 problem="A company messed up (late delivery, broken product, wrong charge, bad repair) and customer service keeps going in circles.",
 outcome="A short, firm, factual complaint with a clear ask and a deadline, plus where to escalate if they ignore it.",
 prompt="""Help me write a complaint to [COMPANY].

What happened, with dates: [TIMELINE]
What I already tried: [CALLS, CHATS, TICKET NUMBERS]
What I want: [REFUND / REPLACEMENT / REPAIR / CREDIT]

Write a calm, factual complaint under 200 words with a clear request and a reasonable deadline. Then tell me: the best channel to send it (email, web form, executive contact), and where I can escalate if they don't respond (for example a regulator or my card issuer), with official links I can check.""",
 tools=CHAT4, time_saved="Editor's estimate: about 10 minutes for a clear complaint", difficulty="Easy",
 steps=["Write down the timeline: dates, order numbers, who you talked to.", "Fill in the prompt and read the draft.", "Remove anything emotional or untrue; keep it factual.", "Send it through the channel the AI suggests and note the date.", "If the deadline passes, escalate using the official route."],
 watch_out=["Don't make threats you won't follow through on. Calm and specific works better.", "Check any regulator or escalation link the AI gives you; it may be out of date."],
 faq=[{"q": "Can an AI agent contact customer service for me?", "a": "Some agents can fill in a web form or chat window for you. EY's 2026 study found 34% of people would prefer an AI that contacts customer service to fix issues. Read what it sends before it sends it."}],
 sources=[EY, AC("use ai to write a letter of complaint")],
 tags=["complaint", "customer service", "refund", "broken", "escalate"])

add(slug="fill-out-a-long-form", category="paperwork", title="Get through a long form without the headache",
 problem="A long application or government form is confusing, and you're not sure what each question is really asking.",
 outcome="A question-by-question explanation, a list of documents to have ready, and draft answers for you to check and enter yourself.",
 prompt="""I need to fill out this form: [FORM NAME AND WHO IT'S FOR]
Here are the questions or a copy of the form (personal info removed): [PASTE OR UPLOAD]

1. Explain what each question is asking in plain English.
2. List every document or number I'll need before I start.
3. Point out questions where a wrong answer could cause problems or delays.
4. Where I give you my details, draft an answer, but never guess. If you don't know, write [ASK ME].
My details: [ONLY THE FACTS NEEDED, NO ID NUMBERS]""",
 tools=CHAT4, time_saved="Editor's estimate: 20–40 minutes on a long form", difficulty="Medium",
 steps=["Get the official form and its official instructions.", "Use the prompt to understand each question and gather documents.", "Enter your answers yourself on the official site or paper form.", "Ask the AI to double-check your answers for consistency (without ID numbers).", "Keep a copy of what you submitted."],
 watch_out=["You're responsible for every answer on an official form. Don't let an AI guess.", "Read the official instructions too; the AI may not know the latest version of the form.", PRIV],
 faq=[{"q": "Can AI fill out the form for me?", "a": "It can draft answers and some agents can type into web forms, but for government, tax, immigration or legal forms you should enter and review every answer yourself."}],
 sources=[AC("can ai fill out forms for me"), AC("can ai fill out pdf forms")],
 tags=["form", "application", "government", "PDF", "paperwork"])

add(slug="review-a-lease-before-signing", category="paperwork", title="Review a rental lease before you sign",
 problem="The lease is long, the landlord wants it signed this week, and you're worried about what's buried in it.",
 outcome="A plain-English summary, a list of unusual or one-sided clauses, and polite questions to ask before you sign.",
 prompt="""Review this residential lease for me as a renter in [CITY, STATE]. Personal info removed.
[PASTE LEASE]

1. Summarize rent, deposit, fees, term, renewal and move-out rules.
2. List clauses that are unusual, one-sided, or could cost me money (for example automatic renewal, repair duties, penalties, entry rules).
3. Tell me which points may depend on my state's or city's tenant laws, so I can check them.
4. Write 5 polite questions or change requests for the landlord.
This is not legal advice; flag anything I should ask a tenant-rights group about.""",
 tools=CHAT4, time_saved="Editor's estimate: about 20 minutes for a first read of a long lease", difficulty="Medium",
 steps=["Get the full lease, including any addenda.", "Remove names and addresses and paste it into the prompt.", "Check any 'depends on your state' points with your state or local tenant resources.", "Send your questions to the landlord in writing.", "Keep a signed copy and photos of the unit on move-in day."],
 watch_out=["AI isn't a lawyer and may not know your local rules. Confirm anything important.", "Don't sign under pressure if key questions are unanswered."],
 faq=[{"q": "Where do I check my tenant rights?", "a": "HUD keeps a page with tenant-rights resources by state, and many cities have free tenant hotlines."}],
 sources=[{"label": "HUD: Tenant rights, laws and protections", "url": "https://www.hud.gov/topics/rental_assistance/tenantrights"}, AC("chatgpt lease review")],
 tags=["lease", "rent", "landlord", "apartment", "contract", "tenant"])

add(slug="moving-checklist-and-change-of-address", category="paperwork", title="Make a moving checklist and change your address everywhere",
 problem="Moving means telling dozens of companies and offices your new address, and something always gets missed.",
 outcome="A personal moving checklist by week, a list of everyone to notify, and the official USPS change of address done for the official fee.",
 prompt="""I'm moving from [CITY/STATE] to [CITY/STATE] on [DATE]. My household: [WHO, PETS, CAR?]
Here are my recurring bills/accounts (no account numbers): [LIST OR PASTE A STATEMENT]

1. Make a week-by-week moving checklist starting today.
2. List every organization I should give my new address to, grouped (government, money, utilities, health, subscriptions, work/school).
3. Tell me which utilities to stop or transfer and when.
4. Write a short, reusable message I can send to update my address.""",
 tools=CHAT4, time_saved="Editor's estimate: an hour or more of list-making", difficulty="Easy",
 steps=["Fill in the prompt with your move date and accounts.", "Do the USPS change of address on the official USPS site only.", "Work through the AI's list, ticking off each organization.", "Set reminders for utility stop/start dates.", "A month after the move, ask the AI which items are still open."],
 watch_out=["USPS warns that some third-party sites charge $40 or more to file a change of address. The official online fee is $1.25 for identity verification.", "Never give an AI your account numbers; just the company names."],
 faq=[{"q": "When can I file the USPS change of address?", "a": "USPS says you can submit it up to 90 days before your move and up to 30 days after."}],
 sources=[{"label": "USPS: Standard Forward Mail & Change of Address", "url": "https://www.usps.com/manage/forward.htm"}, {"label": "USPS FAQ: Change of Address – The Basics", "url": "https://faq.usps.com/articles/Knowledge/Change-of-Address-The-Basics"}, {"label": "X post: using an AI agent for moving-out admin", "url": "https://x.com/tomchris/status/2072663153532666045"}],
 real_examples=[{"text": "A person moving out of Lisbon says he gave Claude his contracts and emails to cancel utility contracts, and that it recovered €770 in unfair charges along the way.", "source": "X post by @tomchris, Jul 2026", "url": "https://x.com/tomchris/status/2072663153532666045", "verification": "Self-reported; not independently verified"}],
 tags=["moving", "change of address", "USPS", "utilities", "checklist"])

add(slug="plan-a-trip-itinerary", category="bookings", title="Plan a trip itinerary that fits your budget and pace",
 problem="Planning a trip means 30 open tabs, and you still aren't sure the days fit together.",
 outcome="A day-by-day plan with realistic travel times, a budget estimate, and a booking checklist with links to verify.",
 prompt="""Plan a [NUMBER]-day trip to [PLACE] for [WHO, AGES] in [MONTH].
Budget: [TOTAL OR PER DAY]. Pace: [RELAXED / BUSY]. We like: [INTERESTS]. Avoid: [THINGS].
Getting there from: [CITY].

1. Day-by-day plan with morning/afternoon/evening, grouped by neighborhood to cut travel time.
2. Rough costs per day, marked as estimates.
3. What to book ahead, in order of urgency.
4. A rainy-day backup for each day.
Tell me what I should double-check (opening hours, prices, closures) because it may be out of date.""",
 tools=[{"id": "chatgpt"}, {"id": "claude"}, {"id": "gemini"}, {"id": "grok"}, {"id": "chatgpt-work", "note": "Can check flights and availability on websites."}],
 time_saved="Editor's estimate: a few hours of research down to about 30 minutes", difficulty="Easy",
 steps=["Fill in the prompt with dates, people, budget and interests.", "Ask follow-ups: “make day 2 less walking”, “swap in a kid-friendly lunch”.", "Check opening hours and prices on official sites.", "Book the urgent items first.", "Save the final plan to your phone or a shared doc."],
 watch_out=["AI can list places that have closed or changed hours. Verify before you go.", "Prices are estimates. Check the real price at booking."],
 faq=[{"q": "Can the AI book the flights and hotel?", "a": "Agents like ChatGPT Work can search and prepare bookings on websites and ask before paying. Many people still prefer to book the final step themselves."}],
 sources=[AC("use chatgpt to plan a trip"), {"label": "Use.AI survey of 2,400 US/UK adults (press release)", "url": "https://cooperative-agency.prowly.com/447243-why-more-people-are-outsourcing-their-thinking-to-ai"}, OAI_CB],
 tags=["travel", "trip", "itinerary", "vacation", "plan", "budget"])

add(slug="prepare-for-a-doctor-visit", category="health", title="Prepare for a doctor's appointment in 10 minutes",
 problem="Appointments are short, and you forget half your questions or can't explain your symptoms clearly.",
 outcome="A one-page summary of symptoms, medicines and questions to bring, plus a way to capture what the doctor said afterwards.",
 prompt="""Help me prepare for a doctor's appointment. This is to organize my thoughts, not to diagnose me.

Reason for visit: [WHAT'S GOING ON]
Symptoms, when they started, what makes them better/worse: [DETAILS]
Medicines and supplements I take: [LIST]
What I'm worried about: [CONCERNS]

1. Turn this into a clear one-page summary I can hand to the doctor.
2. Suggest the 5 most useful questions to ask, in priority order.
3. Make a short template for writing down what the doctor tells me and any next steps.""",
 tools=CHAT4, time_saved="Editor's estimate: about 10 minutes, and a more useful appointment", difficulty="Easy",
 steps=["Jot down symptoms and medicines as you notice them.", "Run the prompt the day before the appointment.", "Print or save the summary and bring it.", "Fill in the template right after the visit.", "Ask the AI to explain any terms from your visit summary in plain English."],
 watch_out=["AI can't examine you and may be wrong. Use it to prepare, not to replace your doctor.", "Leave your name, birth date and insurance ID out of the chat."],
 faq=[{"q": "Is it okay to ask an AI health questions?", "a": "Many people do; Menlo Ventures' 2025 survey found 14% of US adults used AI to research health questions. Treat the answers as a starting point for a conversation with your clinician."}],
 sources=[MENLO25, {"label": "AHRQ: Questions to ask your doctor", "url": "https://www.ahrq.gov/questions/index.html"}],
 tags=["doctor", "appointment", "symptoms", "questions", "health"])

add(slug="organize-a-parents-care-paperwork", category="health", title="Organize an aging parent's care and paperwork",
 problem="You're helping a parent with doctors, insurance, medicines and bills, and the details live in a dozen places.",
 outcome="One organized care binder: contacts, medicines, appointments, insurance details, and a running log of calls and decisions.",
 prompt="""I'm helping my [MOM/DAD], age [AGE], with their care. Here's what I know so far (no ID numbers):
[DOCTORS, MEDICINES, INSURANCE TYPE, UPCOMING APPOINTMENTS, OPEN ISSUES]

1. Organize this into a care binder with sections: contacts, medicines (dose, time, prescriber), appointments, insurance, open issues.
2. List what's missing that I should collect.
3. Make a call-log template (date, who, what was said, next step).
4. Suggest questions to ask at the next appointment or care meeting.""",
 tools=CHAT4, time_saved="Editor's estimate: an afternoon of organizing down to under an hour", difficulty="Medium",
 steps=["Collect what you have: pill bottles, insurance cards, recent letters.", "Run the prompt without ID numbers.", "Fill in the gaps it lists.", "Keep the binder in a shared doc with siblings or caregivers.", "Log every call; it helps a lot if you ever need to appeal a decision."],
 watch_out=["Double-check medicine names and doses against the labels. Errors here matter.", "Get your parent's permission and any required forms (like a HIPAA authorization) before talking to their providers."],
 faq=[{"q": "Can AI help if insurance wants to discharge them too early?", "a": "It can help you write an appeal. See our guide to appealing a health insurance denial, and ask the facility how to file a discharge appeal."}],
 sources=[{"label": "Reddit r/AgingParents: ChatGPT helped with an insurance discharge appeal", "url": "https://www.reddit.com/r/AgingParents/comments/1r1eimf/"}],
 real_examples=[{"text": "A user says they used ChatGPT to word an appeal of their mother's rehab discharge, which was approved, and then fed in the paperwork to prepare a second appeal.", "source": "Reddit r/AgingParents, Feb 2026", "url": "https://www.reddit.com/r/AgingParents/comments/1r1eimf/", "verification": "Self-reported; not independently verified"}],
 tags=["caregiving", "aging parent", "eldercare", "medicines", "binder"])

add(slug="weekly-meal-plan-and-grocery-list", category="family", title="Make a weekly meal plan and grocery list in 5 minutes",
 problem="Deciding what's for dinner every night is exhausting, and you keep buying food that goes to waste.",
 outcome="Seven dinners your household will actually eat, using what you already have, plus one grocery list sorted by store aisle.",
 prompt="""Plan [NUMBER] dinners for [NUMBER] people this week.
Likes: [FOODS]. Dislikes/allergies: [LIST]. Weeknight cooking time: [MINUTES].
Already in my fridge/pantry: [LIST].
Budget: [AMOUNT OR 'KEEP IT CHEAP'].

1. Give me the plan, reusing ingredients across meals so nothing goes to waste.
2. Make one grocery list grouped by store section, minus what I already have.
3. Note which meals make good leftovers for lunch.""",
 tools=CHAT4, time_saved="Editor's estimate: 20–30 minutes of planning each week", difficulty="Easy",
 steps=["List what's in your fridge and pantry.", "Fill in the prompt and swap any meals you don't like.", "Copy the grocery list to your phone or a grocery app.", "Save the prompt and reuse it every week."],
 watch_out=["Double-check anything allergy-related yourself. AI can miss hidden ingredients."],
 faq=[{"q": "How common is this?", "a": "Menlo Ventures' 2025 survey found 16% of US adults used AI for meal planning, one of its top everyday uses."}],
 sources=[MENLO25, AC("use ai to plan meals")],
 tags=["meal plan", "dinner", "grocery list", "recipes", "family"])

add(slug="homework-help-that-teaches", category="family", title="Use AI for homework help that teaches instead of cheats",
 problem="Your kid is stuck on homework, you don't remember how to do it, and you don't want the AI to just hand over answers.",
 outcome="A patient, step-by-step tutor that asks your child questions and explains the idea, without doing the work for them.",
 prompt="""Act as a patient tutor for my [GRADE]-grade child. Topic: [SUBJECT/TOPIC].
Here is the problem they're stuck on: [PASTE OR PHOTO]

Rules:
- Do NOT give the final answer.
- Ask one question at a time to help them figure out the next step.
- If they're stuck twice, give a hint or a similar example with different numbers.
- Use simple words and short sentences.
- At the end, give them one practice problem to try on their own.""",
 tools=CHAT4, time_saved="Editor's estimate: less time stuck and fewer evening battles", difficulty="Easy",
 steps=["Check your child's school rules on AI use first.", "Paste the prompt and the problem.", "Sit with your child for the first few sessions.", "Ask the AI to explain the idea to you too, so you can help next time."],
 watch_out=["AI can make math and fact mistakes. Check the final work.", "Many schools have AI rules. Follow your child's school policy."],
 faq=[{"q": "Will it just give my kid the answer?", "a": "Not if you set the rules in the prompt like the one above. Remind it if it slips."}],
 sources=[AC("ai to help with homework"), MENLO26],
 tags=["homework", "kids", "school", "tutor", "parents"])

add(slug="clean-up-your-email-inbox", category="time", title="Get your email inbox under control",
 problem="Thousands of unread emails, and the important ones get buried under newsletters and promos.",
 outcome="A simple folder or label system, a list of senders to unsubscribe from, and short replies drafted for the emails that matter.",
 prompt="""Help me get my inbox under control. Here's a list of my most frequent senders and some recent subject lines (no personal details):
[PASTE LIST]

1. Group senders into: must read, nice to read, unsubscribe, and archive.
2. Suggest 4–6 labels or folders and simple rules/filters to sort new mail automatically, with steps for [GMAIL / OUTLOOK / APPLE MAIL].
3. For these emails I need to answer: [PASTE], draft short, friendly replies.""",
 tools=CHAT4, time_saved="Editor's estimate: an hour or two of sorting, then minutes a day", difficulty="Easy",
 steps=["Export or copy your top senders (most email apps can sort by sender).", "Run the prompt and set up the suggested filters.", "Unsubscribe from the senders on the list.", "Use the AI for drafts; read every reply before sending."],
 watch_out=["If you connect an AI to your email account, check what it can read and do, and require it to ask before sending.", "Don't paste emails that contain passwords, codes or financial details."],
 faq=[{"q": "Can an AI read and sort my email for me?", "a": "Some assistants can connect to Gmail or Outlook and draft or organize messages. Check what your plan allows, and keep sending in your own hands."}],
 sources=[MENLO25, MENLO26, AC("use ai to organize gmail")],
 tags=["email", "inbox", "Gmail", "Outlook", "unsubscribe", "productivity"])

add(slug="tailor-your-resume-to-a-job", category="work", title="Tailor your resume and cover letter to a job in 15 minutes",
 problem="Every job wants a slightly different resume, and rewriting yours each time takes forever.",
 outcome="A resume version that matches the job's key words using only your real experience, plus a short cover letter.",
 prompt="""Here's a job posting: [PASTE]
Here's my current resume (contact details removed): [PASTE]

1. List the 8 most important skills and keywords in the posting.
2. Show which ones my resume already proves and which are missing.
3. Rewrite my bullet points to match the posting using ONLY true experience from my resume. Don't invent jobs, numbers or skills. Where a number would help, write [ADD NUMBER].
4. Write a cover letter under 200 words.
5. Give me 3 likely interview questions for this job.""",
 tools=CHAT4, time_saved="Editor's estimate: 30–60 minutes per application", difficulty="Easy",
 steps=["Copy the job posting and your resume.", "Run the prompt and fill in any [ADD NUMBER] spots with real figures.", "Read every line; remove anything that isn't true.", "Save each version with the company name.", "Practice the interview questions out loud."],
 watch_out=["Never let AI add skills or results you don't have. It can cost you the job later.", "Remove your phone, email and address before pasting."],
 faq=[{"q": "Can AI fill out job applications for me?", "a": "Agents can fill some online forms, but review every field yourself. Many people use AI for drafts and do the submitting themselves."}],
 sources=[AC("ai to help with resume"), AC("can ai fill out job applications for me")],
 tags=["resume", "cover letter", "job application", "career", "interview"])

add(slug="sell-your-stuff-online", category="side-hustles", title="Write listings that sell your stuff faster",
 problem="You have things to sell, but writing listings, pricing them and answering buyers is a chore.",
 outcome="A clear title, honest description and price range for each item, plus ready replies for common buyer messages.",
 prompt="""Help me sell this on [FACEBOOK MARKETPLACE / EBAY / ETSY / OTHER].
Item: [WHAT IT IS, BRAND, MODEL, AGE, CONDITION, FLAWS]
Photos: [UPLOAD IF YOU CAN]
Pickup/shipping: [DETAILS]

1. Write a searchable title and an honest description (mention flaws).
2. Suggest a price range and tell me how to check it against sold listings on the site.
3. Write short replies to: 'Is this still available?', lowball offers, and 'Can you hold it?'
4. List safety tips for meeting buyers and getting paid.""",
 tools=CHAT4, time_saved="Editor's estimate: about 10 minutes per listing", difficulty="Easy",
 steps=["Take clear photos in good light.", "Run the prompt for each item.", "Check real sold prices on the marketplace before you set the price.", "Post, then use the saved replies for messages."],
 watch_out=["AI price guesses can be way off. Check sold listings.", "Be honest about flaws; it avoids returns and bad reviews.", "Watch for buyer scams like overpayment or fake payment screenshots."],
 faq=[{"q": "Can AI tell what my item is from a photo?", "a": "Often yes. Ask it to identify the item and model, then confirm with any labels or serial numbers."}],
 sources=[AC("use ai to sell on facebook marketplace"), AC("ai to write listing description")],
 tags=["sell", "marketplace", "eBay", "listing", "declutter", "side hustle"])

add(slug="test-a-side-hustle-idea", category="side-hustles", title="Test a side hustle idea before you spend money",
 problem="You have an idea to earn extra money, but you don't know if anyone will pay, and ads promise 'easy AI income'.",
 outcome="A one-page reality check: who would pay, what it really costs, a cheap 2-week test, and a list of red flags to avoid.",
 prompt="""I'm thinking about this side hustle: [IDEA]
My skills/time/budget: [DETAILS]

Be honest, not encouraging. Please:
1. Who exactly would pay for this, and how would I reach them?
2. Realistic costs and time per week. Mark guesses as guesses.
3. Design a 2-week test that costs under [AMOUNT] to see if anyone will pay.
4. What would make me stop?
5. Red flags if someone is selling me a course, 'done-for-you store' or 'AI income' system for this.""",
 tools=CHAT4, time_saved="Editor's estimate: saves you from spending before you know", difficulty="Medium",
 steps=["Write the idea in one sentence.", "Run the prompt and push back on anything vague.", "Run the cheap test before buying tools or courses.", "Decide using real results, not hype."],
 watch_out=["The FTC has sued several schemes that promised big passive income from 'AI-powered' online stores. Be very wary of anyone guaranteeing earnings.", "AI can't know your local market. Treat its numbers as guesses."],
 faq=[{"q": "Is 'make money with AI' legit?", "a": "AI can help you do real work faster. But the FTC's Operation AI Comply targeted businesses that sold AI-powered income opportunities with false earnings claims. Guaranteed income is a red flag."}],
 sources=[{"label": "FTC: Crackdown on deceptive AI claims and schemes (Operation AI Comply, Sep 2024)", "url": "https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes"}, {"label": "FTC: Air AI banned from marketing business opportunities (Mar 2026)", "url": "https://www.ftc.gov/news-events/news/press-releases/2026/03/air-ai-its-owners-will-be-banned-marketing-business-opportunities-settle-ftc-charges-company-misled"}, AC("use ai to start a side hustle")],
 tags=["side hustle", "extra income", "business idea", "scam", "validate"])

add(slug="reply-to-customer-reviews", category="small-business", title="Reply to customer reviews (even the angry ones)",
 problem="Reviews pile up on Google and you don't have time to answer, or a harsh review has you stuck on what to say.",
 outcome="Short, personal replies for each review, including a calm, professional reply to a negative one.",
 prompt="""I run [BUSINESS TYPE] called [NAME]. Write replies to these reviews:
[PASTE REVIEWS]

Rules:
- Under 60 words each, warm and specific to what the customer said.
- For negative reviews: thank them, acknowledge the issue without arguing, say what we're doing about it, and invite them to contact [EMAIL/PHONE] offline.
- No discounts or incentives, no customer private details.
- Vary the wording so replies don't look copy-pasted.""",
 tools=CHAT4, time_saved="Editor's estimate: about 2 minutes per review instead of 10", difficulty="Easy",
 steps=["Copy new reviews from your Google Business Profile (or other site).", "Run the prompt and edit each reply so it sounds like you.", "Post replies from your verified Business Profile.", "Do it weekly so it never piles up."],
 watch_out=["Google checks replies against its content policies before posting. Keep replies polite and free of private information.", "Don't let AI invent facts about what happened."],
 faq=[{"q": "Do I need anything to reply on Google?", "a": "Google says your business must be verified before you can reply to reviews. Replies show as a response from the business, and the reviewer gets notified."}],
 sources=[{"label": "Google Business Profile Help: Manage customer reviews", "url": "https://support.google.com/business/answer/3474050?hl=en"}, AC("ai to respond to google reviews")],
 tags=["reviews", "Google", "small business", "customer service", "reputation"])

add(slug="chase-an-unpaid-invoice", category="small-business", title="Chase an unpaid invoice without burning the relationship",
 problem="A client is late paying and you're not sure how firm to be.",
 outcome="A sequence of three reminders (friendly, firm, final) and a clean invoice template for next time.",
 prompt="""A client owes me [AMOUNT] for [WORK], invoice [NUMBER] dated [DATE], due [DATE]. Our relationship: [GOOD / NEW / TENSE].
Payment terms we agreed: [TERMS, IF ANY].

1. Write 3 short emails: a friendly reminder, a firm follow-up a week later, and a final notice that states next steps.
2. Keep them professional and factual; include invoice number, amount and how to pay.
3. Suggest clearer payment terms for my future invoices.
4. Give me a simple invoice template with the fields I should always include.""",
 tools=CHAT4, time_saved="Editor's estimate: about 15 minutes, plus less stress", difficulty="Easy",
 steps=["Gather the invoice, agreed terms and any emails about the work.", "Run the prompt and send the first reminder.", "Put the follow-up dates on your calendar.", "Update your invoice template for future clients."],
 watch_out=["Only state next steps (late fees, collections) that your agreement and local law allow.", "Keep client names and bank details out of the chat; add them yourself."],
 faq=[{"q": "Can AI make the invoice too?", "a": "Yes, it can draft an invoice layout. Many accounting and payment apps also generate invoices; use whichever your clients can pay most easily."}],
 sources=[AC("use ai to make invoices")],
 tags=["invoice", "late payment", "freelance", "small business", "email"])

for u in U:
    assert len(u["steps"]) >= 3
json.dump(U, open("/workspace/platform/data/use-cases.json", "w"), indent=1, ensure_ascii=False)
print(len(U), "use cases")
