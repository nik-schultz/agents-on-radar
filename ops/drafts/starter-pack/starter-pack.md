# BotsDoThat Starter Pack

**7 ready-to-paste AI agent setups for beginners. Each one is a real job your AI does on a schedule, and it asks you before it sends, buys or deletes anything.**

*For BotsDoThat Weekly subscribers. Version 1, November 2026. Every feature below was checked against the tool's own help pages; see Sources at the end.*

---

## How to use this pack

1. **Pick one setup.** Start with #1 or #2. They only read, so nothing can go wrong in your inbox.
2. **Paste the prompt and fill in the [brackets].**
3. **Run it once by hand first.** Paste it into a normal chat and check the answer looks right.
4. **Then put it on a schedule** using the steps for your tool.
5. **Keep the safety line in.** Every prompt ends with a "don't" line. Leave it there.

### The safety rule (it's in every prompt)

> Read and report only. Don't send, reply, buy, pay, sign up, cancel, or delete anything. If you think something should happen, tell me what and why, and wait for me to say yes.

Some tools also have their own guardrails. On ChatGPT, a scheduled task that tries to send a message or change data in a connected app may pause and ask for your approval. Claude's Gmail connector asks for approval before it sends, replies or forwards, unless you change that. The prompt line is your backup either way. More on this: [Is it safe to give an AI agent your email?](https://botsdothat.com/is-it-safe-to-give-an-ai-agent-your-email/)

### Which tool can do what (as of November 2026)

| | Runs on a schedule? | Reads your email and calendar? | Where results show up |
|---|---|---|---|
| **ChatGPT** | Yes, with **scheduled tasks**, on every plan including Free. Free runs at most once a day, in a morning, afternoon or night window. Paid plans can pick exact times and run hourly. | Gmail and Google Calendar are plugins under **Settings > Plugins**. OpenAI's scheduled-tasks page names Gmail, Slack and GitHub as apps a task can use. | Push and/or email notification (**Settings > Notifications**), plus the **Scheduled** page |
| **Claude** | Yes, with **scheduled tasks in Cowork**, on **paid plans only** (Pro, Max, Ultra, Team, Enterprise). They run even if your computer is asleep. | Gmail, Google Calendar and Drive connectors work for **all users**, including Free: **+ > Connectors**. | The task's results in Cowork |
| **OpenClaw** | Yes, with the built-in scheduler, `openclaw automations` (also called `openclaw cron`). | Through the `gog` skill. It needs a one-time Google Cloud sign-in setup, so it's more technical. | A chat channel you pick (Telegram, Slack and so on), a webhook, or nowhere |
| **Hermes Agent** | Yes, with **cron**: plain words, `/cron add`, or `hermes cron create`. The gateway has to be running. | Through the bundled **Google Workspace** skill. It also needs a one-time Google Cloud sign-in setup. | A place you pick: Telegram, Discord, Slack, WhatsApp, Signal, email, SMS and more |

**Things worth knowing before you start:**

- **ChatGPT plan limits.** You can have 3 active tasks on Free and Go, 5 on Plus, 10 on Business and Edu, and 15 on Pro and Enterprise. On Free, pick your favourite 3 of these 7.
- **ChatGPT usage.** A task that runs counts against your plan's usage even when it has nothing to report (OpenAI).
- **Claude on the Free plan** can still do every setup here by hand: paste the prompt when you want it. Only the schedule needs a paid plan.
- **Hermes starts each run fresh**, so a prompt can't say "since last time." All 7 prompts are written to work without memory: they look at a fixed window, like "the last 24 hours."
- **Quiet runs.** In Hermes, a reply of exactly `[SILENT]` means nothing gets delivered. In OpenClaw, the quiet reply is `NO_REPLY`. Some prompts below use these so you only hear from your bot when something matters.
- **Running OpenClaw or Hermes yourself?** You pay the AI model provider you connect. Our guide explains how that adds up: [How much does it cost to run an AI agent?](https://botsdothat.com/how-much-does-it-cost-to-run-an-ai-agent/) To pick between the two, see [OpenClaw vs Hermes Agent](https://botsdothat.com/openclaw-vs-hermes-agent/).

### One-time setup per tool

- **ChatGPT:** Go to **Settings > Plugins**, choose Gmail (and Google Calendar if you want it), and connect your Google account. Then go to **Settings > Notifications** and turn on push or email for tasks. Walkthrough: [Set up ChatGPT scheduled tasks](https://botsdothat.com/use-cases/set-up-chatgpt-scheduled-tasks/).
- **Claude:** In a chat, click **+ > Connectors** and connect Gmail and Google Calendar. To schedule (paid plans), open **Scheduled** in Cowork, click **New task**, then **Set up manually**. Enter a name, the prompt, the approval mode, the cadence (hourly, daily, weekly, weekdays or manual) and, optionally, a model.
- **OpenClaw:** Install the `gog` skill. Authorize only what you need, e.g. `gog auth add you@gmail.com --services gmail,calendar`. Tell the agent to use `gog --readonly` for these jobs. Schedule with `openclaw automations create`, as shown in each setup.
- **Hermes Agent:** Run `hermes gateway install` so scheduled jobs can run. Then ask Hermes to "set up Google Workspace", and it walks you through the Google sign-in. Schedule in plain words, e.g. "Every morning at 7am, … send it to me on Telegram", or with `/cron add`. Tip: Hermes can create a job paused (`--paused`), so you can check it before it goes live.

---

## 1. The 7am inbox summary

**What it does:** Every weekday morning it reads yesterday's email and gives you a short list. It covers what needs you today, what has a deadline this week, and a count of everything else. It never touches your inbox.

**Runs:** weekdays, early morning.

```
Read the emails that arrived in my inbox in the last 24 hours.
Give me:
1. Up to 5 emails that need me today: sender, subject, and one line on why.
2. Anything that mentions a date or deadline in the next 7 days, with the date.
3. One line counting the rest by type (newsletters, receipts, notifications, other).
Ignore emails from: [senders or lists to skip].
Put anything urgent at the very top. If nothing needs me, just say "Nothing needs you this morning."
Read and report only. Don't reply, archive, label, delete or unsubscribe from anything.
```

- **ChatGPT:** In a new chat, type "Every weekday at 7am:" and paste the prompt. ChatGPT creates a task, which you can edit on the **Scheduled** page. On Free it runs in the morning window instead of exactly at 7.
- **Claude:** Cowork > **Scheduled** > **New task** > **Set up manually**. Paste the prompt and choose **Weekdays**. On Free, paste it by hand each morning.
- **OpenClaw:** `openclaw automations create "0 7 * * 1-5" "<prompt>" --name "Morning inbox" --tz "<Your/Timezone>" --session isolated --announce --channel telegram --to "<your chat id>"`
- **Hermes Agent:** Tell Hermes: "Every weekday at 7am, <prompt>. Send it to me on Telegram."

**Safety:** read-only. Nothing gets sent or changed.

**Go further:** [Morning inbox briefing blueprint](https://botsdothat.com/blueprints/morning-inbox-briefing/) · [Monday inbox recap and to-do](https://botsdothat.com/use-cases/monday-inbox-recap-and-todo/)

---

## 2. The Sunday family week-ahead

**What it does:** Every Sunday evening it reads the coming week on your calendar, including shared family calendars. It flags clashes, tight gaps, early starts and anything you need to prepare. It doesn't move anything.

**Runs:** weekly, Sunday evening.

```
Look at my calendar [and the shared calendar called "____"] for next Monday through Sunday.
Give me:
1. Each day's events in order, with times and who's involved.
2. Clashes: events that overlap, or are less than [30] minutes apart when one of them needs travel.
3. Anything before [8am] or after [7pm], and any event with no location.
4. Up to 3 things to get ready this week (forms, payments, gifts, packing), based on event names and notes.
If an event looks like it should move, list it under "Suggested changes" with your reason.
Read and report only. Don't create, move or delete events, and don't message or invite anyone.
```

- **Claude (best fit):** The Google Calendar connector can read shared calendars. In Cowork, go to **Scheduled** > **New task**, paste the prompt and choose **Weekly**.
- **ChatGPT:** Connect Google Calendar under **Settings > Plugins**, then ask: "Every Sunday at 6pm:" plus the prompt. OpenAI's scheduled-tasks page names only Gmail, Slack and GitHub as task apps. So check the first run: if the task says it can't see your calendar, use this as a chat prompt you paste on Sundays.
- **OpenClaw:** Authorize the calendar with `gog` (read-only). Then run `openclaw automations create "0 18 * * 0" "<prompt>" --name "Week ahead" --tz "<Your/Timezone>" --session isolated --announce --channel telegram --to "<your chat id>"`.
- **Hermes Agent:** With the Google Workspace skill set up, say: "Every Sunday at 6pm, <prompt>. Send it to me on Telegram."

**Safety:** it suggests changes, and you make them.

**Go further:** [Family calendar guardian blueprint](https://botsdothat.com/blueprints/family-calendar-guardian/) · [Sunday family calendar check](https://botsdothat.com/use-cases/sunday-family-calendar-check/)

---

## 3. Bills coming due

**What it does:** Twice a week it finds bills and payment reminders in your email. It lists who you owe, how much and by when, with the next 5 days at the top. It never pays anything or clicks a "pay now" link.

**Runs:** Monday and Thursday mornings.

```
Search my email from the last 14 days for bills, invoices and payment reminders
(for example utilities, phone, internet, credit cards, insurance, rent, school or medical).
For each one, list: who it's from, amount due, due date, and whether the email says it's on autopay.
Sort by due date and put anything due in the next 5 days at the top.
Skip ads and receipts for things already paid.
If the amount or due date isn't clearly written in the email, write "check the bill" instead of guessing.
Read and report only. Don't pay anything, don't open "pay now" links, don't sign in to any account, and don't reply.
```

- **ChatGPT:** "Every Monday and Thursday at 8am:" plus the prompt. On Free, note that a task runs at most once a day.
- **Claude:** Make a **Weekly** task for Monday. Make a second one for Thursday, or run Thursday's by hand.
- **OpenClaw:** `openclaw automations create "0 8 * * 1,4" "<prompt>" --name "Bills due" --tz "<Your/Timezone>" --session isolated --announce --channel telegram --to "<your chat id>"`
- **Hermes Agent:** "Every Monday and Thursday at 8am, <prompt>. Send it to me by email." Email is one of Hermes' delivery options.

**Want calendar reminders too?** Add this line: "Then propose a calendar reminder for each bill due in the next 14 days, and only add them after I reply 'add them'."

**Safety:** it never pays. Any reminder it adds waits for your "add them."

---

## 4. Where are my packages?

**What it does:** Every evening it collects shipping and delivery emails into one small table: store, item, carrier, status, expected date and tracking link. Problems go at the top.

**Runs:** daily, evening.

```
Check my email from the last 24 hours for order confirmations and shipping or delivery updates.
Make a short table: store, item, carrier, latest status, expected delivery date, and the tracking link from the email.
Put "delivered", "delayed", "delivery attempted" and "action needed" at the top.
If there are no new shipping emails, reply with exactly: No package news today.
Read and report only. Don't contact any store or carrier, don't start a return, and don't buy anything.
```

- **ChatGPT:** "Every day at 6pm:" plus the prompt. A one-off task also works. OpenAI's own example task is "Let me know when my package is delivered." **On paid plans** (Plus, Pro, Business, Enterprise, Edu) you can set up an **event-triggered task** instead. In **Work**, describe the trigger, such as "When a new Gmail message arrives with 'shipped' or 'out for delivery' in the subject", and it runs when that email lands. Event triggers aren't available on Free or Go.
- **Claude:** **Daily** scheduled task (paid plans).
- **OpenClaw:** Use `openclaw automations create "0 18 * * *" …` like the setups above, and change the last prompt line to "If there are no new shipping emails, reply NO_REPLY." That makes quiet days silent. OpenClaw also has Gmail Pub/Sub triggers that react to new mail as it arrives. Setting those up is an advanced job.
- **Hermes Agent:** Change the quiet line to "reply with exactly [SILENT]", then say: "Every day at 6pm, <prompt>. Send it to me on Telegram."

**Safety:** read-only. Returns and complaints stay with you.

---

## 5. Renewals and free trials ending

**What it does:** Once a week it finds subscription receipts, renewal notices, price-change emails and "your trial ends" emails. It lists what's renewing or ending soon. It never cancels anything by itself.

**Runs:** weekly.

```
Search my email from the last 45 days for subscription receipts, renewal notices,
price-change notices and "your free trial ends" emails.
For each subscription, list: the service, the price and billing period exactly as the email says,
the next renewal or trial-end date, and the date of the email you got it from.
Put anything renewing or ending in the next 10 days at the top, and mark any price increase the email mentions.
If a price or date isn't in the email, write "not in the email".
Read and report only. Don't cancel, change, or sign in to anything, and don't reply to any email.
```

- **ChatGPT:** "Every Saturday morning:" plus the prompt.
- **Claude:** **Weekly** scheduled task. On Free, run it by hand once a week.
- **OpenClaw:** `openclaw automations create "0 9 * * 6" "<prompt>" --name "Renewals" --tz "<Your/Timezone>" --session isolated --announce --channel telegram --to "<your chat id>"`
- **Hermes Agent:** "Every Saturday at 9am, <prompt>. Send it to me on Telegram."

**Next step, still safe:** When you decide to cancel one, ask in a normal chat: "Walk me through cancelling [service]. Show me each step before you do it." Cancelling stays your call.

---

## 6. Tell me when this page changes

**What it does:** It checks one web page every day and stays quiet until the thing you're waiting for shows up. That might be registration opening, a new date, an appointment slot, or "back on sale" turning into "available."

**Runs:** daily, or hourly on paid ChatGPT plans.

```
Open [page URL] and look at [the part you care about, e.g. "the registration section" / "appointment dates"].
Tell me only if this is true: [what you're waiting for, e.g. "registration for spring is open" /
"a date after March 1 is listed" / "the status no longer says Full"].
If it's true, quote the exact text that shows it and give me the link.
If I can't be sure (the page didn't load, or needs a login), tell me that instead.
If it's not true yet, [quiet line: see your tool below].
Don't fill in forms, sign up, sign in, book, or buy anything.
```

- **ChatGPT:** For the quiet line, write "say nothing new". Then ask "Check this every morning and stop once it's true:" plus the prompt. ChatGPT's monitoring tasks check for changes, tell you when something happens, and can stop when a condition is met.
- **Claude:** Make a **Daily** scheduled task. Scheduled tasks can run web research. Claude still writes a short result each run, so for the quiet line use "reply in one line: Not yet."
- **OpenClaw:** Quiet line: "reply NO_REPLY". Then `openclaw automations create "0 9 * * *" "<prompt>" --name "Page watch" …`, same as the others.
- **Hermes Agent:** Quiet line: "reply with exactly [SILENT]". Then "Every day at 9am, <prompt>. Send it to me on Telegram." If the page needs a login, Hermes says to set that up before the job runs.

**Safety:** it watches and tells you. Signing up or booking stays with you.

**Go further:** [Web page watcher blueprint](https://botsdothat.com/blueprints/web-page-watcher/) · [Watch a web page for changes](https://botsdothat.com/use-cases/watch-a-web-page-for-changes/) · [Schedule bots without burning tokens](https://botsdothat.com/use-cases/schedule-bots-without-burning-tokens/)

---

## 7. Friday "what's waiting on me"

**What it does:** Every Friday afternoon it finds the emails where someone is still waiting on you. It also collects promises you made ("I'll send it Monday") and deadlines coming up next week. It writes a suggested reply for each, which you can copy. It doesn't send them.

**Runs:** weekly, Friday afternoon.

```
Look at my email from the last 7 days and find:
1. Messages where someone asked me a question or asked me for something, and I haven't replied.
   Show the sender, what they asked, and the date.
2. Things I said I would do ("I'll send", "I'll check", "I'll get back to you") that I haven't done yet, as far as you can tell.
3. Deadlines, meetings or appointments next week that are mentioned in email.
Show at most 10 items, most important first.
For each one in group 1, write a suggested reply of 2-3 sentences that I can copy.
Don't send or save any replies, and don't archive or delete anything. If I want a draft saved, I'll say "draft it".
```

- **ChatGPT:** "Every Friday at 3pm:" plus the prompt. If a later step tries to send, ChatGPT may pause the task and ask for your approval.
- **Claude:** Make a **Weekly** scheduled task. Claude's Gmail connector can save drafts, and it asks before sending by default.
- **OpenClaw:** `openclaw automations create "0 15 * * 5" "<prompt>" --name "Friday catch-up" --tz "<Your/Timezone>" --session isolated --announce --channel telegram --to "<your chat id>"`. Keep `gog --readonly`.
- **Hermes Agent:** "Every Friday at 3pm, <prompt>. Send it to me on Telegram." Hermes delivers the job's final answer to you. The job doesn't send messages to anyone else.

**Safety:** you get suggestions, not sent emails. More: [Flag only the emails that need a reply](https://botsdothat.com/use-cases/flag-only-emails-that-need-a-reply/) · [Let AI send emails for you, safely](https://botsdothat.com/use-cases/let-ai-send-emails-for-you/)

---

## Where to go next

- More things bots can do: [botsdothat.com/what-can-bots-do](https://botsdothat.com/what-can-bots-do/)
- New jobs every week, with one subscriber-only extra in each email: [BotsDoThat Weekly](https://botsdothat.com/newsletter/)
- Stuck, or did a setup break? Reply to any BotsDoThat email. We read them.

## Sources (checked November 3, 2026)

- OpenAI, Scheduled tasks in ChatGPT: https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
- OpenAI, Connected apps in ChatGPT: https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt
- OpenAI, Connecting and managing app accounts in ChatGPT: https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt
- Anthropic, Schedule recurring tasks in Claude Cowork: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
- Anthropic, Use Google Workspace connectors: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- OpenClaw, Automations: https://docs.openclaw.ai/automation/cron-jobs (and /managing-jobs, /delivery, /payloads, /gmail)
- OpenClaw, gog skill: https://github.com/openclaw/openclaw/blob/main/skills/gog/SKILL.md and https://github.com/openclaw/gogcli
- Hermes Agent, Scheduled tasks (cron): https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/
- Hermes Agent, Google Workspace skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/google-workspace

*Features change. If a step doesn't match what you see, the tool's own help page wins. Tell us, and we'll fix the pack.*

BotsDoThat · botsdothat.com · hello@botsdothat.com
