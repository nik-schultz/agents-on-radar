# Subscriber-only extras: plan (DRAFT)

## The idea
Every BotsDoThat Weekly issue carries **one "Subscriber extra"** block that isn't on the site. It's something small and ready to use that builds on that week's topic. It gives people a reason to subscribe, and to stay subscribed, beyond reading the site.

## Rules for every extra
1. **Agentic, not just a chat prompt.** It should be a job the AI *does*: on a schedule, across email or calendar, or on a page. Keep the "asks before sending, buying or deleting" line.
2. **Sourced like the site.** Any feature claim must match an official help page, and any plan limit or price must be linked. No invented stats and no time-saved claims.
3. **New wording.** Don't paste an existing site page into the email.
4. **Small.** It fits in one email block: a prompt plus 3-6 steps or bullets. Bigger things become a PDF linked from the email.
5. **Labelled.** Heading: "🎁 Subscriber extra: [title]". Same position every week, right after the jobs and before the watch-out.

## Where it lives and how it stays exclusive
- **In the email body only.** /newsletter/ publishes a web copy of every issue (`nl_issue_html` in build.py). An extra that sits in the email body would also appear on the site. **Needs a build change, which needs Nik's approval:** add an `extra` field to issue data that goes into the Kit email but is left out of the web archive. The web version would show a line like "Subscribers got a bonus this week. [Subscribe]".
- **Bigger extras (PDF):** host them the same way as the Starter Pack. See kit-setup.md for the hosting choice.
- **Tracking:** Kit's Free plan includes tagging. Clicks on the extra can be tagged if Kit's link-click tagging is available on Free. That's **not verified**, so check in Kit before relying on it.

## The next 4 issues (Thursdays)

| Issue | Date | Extra | One-line description |
|---|---|---|---|
| #3 | Thu Nov 5, 2026 | **Calendar clash fixer, ask-first edition** | 3 prompts that find clashes in your calendar and draft the fix. Nothing moves until you reply "make the change." Matches #3's calendar features. |
| #4 | Thu Nov 12, 2026 | **The "ask first" card** | 6 copy-paste rule lines to add to any agent's standing instructions. They cover sending, buying, deleting, signing up, sharing files and sign-ins, with where to put them in ChatGPT, Claude, OpenClaw and Hermes. |
| #5 | Thu Nov 19, 2026 | **Holiday delivery tracker, upgraded** | Starter Pack setup #4 with two extra columns, "return window" and "gift for", run daily through December. It's still read-only, with no returns started by the bot. |
| #6 | Thu Nov 26, 2026 | **Test before you schedule: the 5-minute checklist** | How to try a new scheduled job safely before it runs on its own: one manual run, a paused or canary job (Hermes `--paused`), check where results go, then switch it on. |

Before each one goes out, check that week's feature claims against the help pages again (OpenAI, Anthropic, OpenClaw and Hermes docs change often).
