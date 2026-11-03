# Welcome email: delivers the Starter Pack (DRAFT, not in Kit)

From: BotsDoThat <hello@botsdothat.com>

## Important: which Kit email this is

On Kit's Free plan the pack has to ride on the **confirmation (incentive) email**. That email goes out right after someone signs up. Its button confirms the subscription and then downloads the PDF or opens a URL. Kit's Free plan help page lists **email sequences and visual automations as paid features**. So a separate "you're confirmed, here's your pack" email that sends *after* confirmation isn't available on Free. Details are in kit-setup.md.

That gives two versions:

- **Version A (use now, works on Free):** this text replaces the body of the form's confirmation email. Keep Kit's confirm button and its link exactly as Kit sets them, and only change the button's words. Then set "After confirming, redirect to" to the PDF (Download) or to the PDF's URL.
- **Version B (only if Nik upgrades to a paid plan later):** a one-email welcome sequence, triggered by a basic automation ("joins form 10088120" > "add to sequence").

Note from Kit's help: personalization code doesn't work in the confirmation email's *subject line*. So the subject lines below have no {{ first_name }}.

---

## Version A: confirmation email that delivers the pack (Free plan)

**Subject line options**
1. Confirm, and your Starter Pack is yours
2. One click to get your 7 AI agent setups
3. Your BotsDoThat Starter Pack is one click away

**Preview text:** Tap the button to confirm your email. The Starter Pack PDF opens right after.

**Body**

Hi there,

Thanks for signing up for BotsDoThat Weekly.

Tap the button below to confirm your email, and your **BotsDoThat Starter Pack** opens straight away. It's 7 ready-to-paste setups that put an AI on a regular schedule: a 7am inbox summary, a Sunday week-ahead check of your calendar, a bills-due list, a package tracker, a renewals watch, a page watcher that only pings you when something changes, and a Friday "what's waiting on me."

Each one has the exact prompt, the steps for ChatGPT, Claude, OpenClaw and Hermes Agent, and a safety line. Your AI reads and reports, and it asks you before it sends, buys or deletes anything.

[ Button: **Confirm and get the Starter Pack** ] ← keep Kit's own confirm link on this button

Didn't sign up? Just ignore this email, and you won't hear from us.

From Thursday, you'll get one email a week. Each has a few jobs you can hand to AI, plus one extra that's only in the email.

The BotsDoThat team
hello@botsdothat.com · botsdothat.com

*(If Nik picks the URL option instead of Kit's Download option, the button still confirms, and Kit then sends people to: [PDF LINK].)*

---

## Version B: welcome email after confirmation (paid plan only)

**Subject line options**
1. Here's your BotsDoThat Starter Pack
2. Your 7 AI agent setups are inside
3. Start here: your first scheduled AI job

**Preview text:** 7 ready-to-paste setups, and the one we'd try first.

**Body**

Hi {{ subscriber.first_name | default: "there" }},   ← check this personalization tag in Kit's editor before using; it wasn't checked against a Kit help page

You're in. Here's your Starter Pack:

**[Download the BotsDoThat Starter Pack (PDF)]([PDF LINK])**

If you only try one, start with **#1, the 7am inbox summary**. It only reads, so nothing in your inbox changes. Run the prompt once by hand, check the answer, then put it on a schedule with the steps for your tool.

A few things to know:
- Every setup ends with a "don't" line. Keep it in.
- ChatGPT's Free plan allows 3 active scheduled tasks, so pick your favourite 3.
- On Claude, scheduling needs a paid plan, but you can run any of the 7 by hand on Free.

Every Thursday you'll get a few new jobs to hand to AI, plus a subscriber-only extra.

Reply and tell us which setup you tried, or where you got stuck. We read every reply.

The BotsDoThat team
hello@botsdothat.com · botsdothat.com
