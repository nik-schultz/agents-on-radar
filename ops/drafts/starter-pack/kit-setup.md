# Kit setup: delivering the Starter Pack (DRAFT, nothing changed in Kit)

Checked on Kit's official help center on Nov 3, 2026. Form: **10088120** (uid e874d57257), double opt-in (config.json).

## Short answer
- **Yes, Kit can deliver the pack automatically on the Free plan,** but only through the **form's confirmation email** (Kit also calls it the "incentive email"). That's the double opt-in email Kit sends right after someone signs up. Its "After confirming redirect to" setting can be **Download**, a file uploaded to Kit, or a **URL**. When the subscriber clicks confirm, they get the file or the URL.
- **No, Kit can't send a separate welcome or delivery email *after* confirmation on Free.** Kit's current Free plan help page (dated Sep 23, 2026) lists **"Visual automations and the automation template library"** and **"Email sequences"** under *What needs a paid plan*.
- **Kit's help center contradicts itself.** An older article, "Visual Automations on the Newsletter Plan" (dated Sep 6, 2026), says the Newsletter plan includes one email sequence and one basic visual automation. The newer Free plan page says both are paid. Plan around the newer page. Don't build the delivery on a sequence.
- **Timing risk:** ops/content-calendar.md says the Kit trial ends about Nov 6, and the account then drops to Free. Kit's Free plan page says "Visual automations and sequences stop running while you're on the Free plan." Anything built on a sequence during the trial would quietly stop. The confirmation email approach doesn't have this problem.

### Was what we told Nik right?
"Kit can send the starter pack automatically on its free plan" is **mostly right, with one correction.** It's sent automatically **as part of the confirmation email** (click confirm, get the PDF), not as a separate welcome email after confirmation. People who never click confirm never get it. People who subscribed before the change won't get it either. To reach them, send one free broadcast (broadcasts are unlimited on Free) with a link, and that needs a URL-hosted copy (see hosting below).

## Sources (Kit help center)
- The Kit Free plan: https://help.kit.com/en/articles/16627071-the-kit-free-plan
  - Included: up to 10,000 subscribers, unlimited forms and landing pages, unlimited broadcasts, tagging and segmentation.
  - Paid: visual automations, email sequences, rules and RSS, AI Connectors, paid apps.
- The Confirmation Email: https://help.kit.com/en/articles/2502655-the-confirmation-email
  - Settings > Confirmation Email.
  - "After confirming redirect to": "upload a file for them to download (such as a freebie or lead magnet), or send them to a URL."
  - Steps: Select Download > Choose a file > save. To replace the file, upload a new one and save.
  - Supported files: "PDFs, Word documents, and images", within file size and type limits that the page doesn't spell out.
  - Personalization doesn't work in the subject line.
- Troubleshooting: Confirmation downloads: https://help.kit.com/en/articles/4296218-troubleshooting-confirmation-downloads
  - In the Form builder: Settings > **Incentive** > Download, then publish.
  - If downloads fail, use a filename **under 20 characters, with no spaces, underscores or accented letters**.
- Grow your list with content upgrades: https://help.kit.com/en/articles/2502644-grow-your-list-with-content-upgrades
  - For a file: turn on Send confirmation email, then choose Download under "After confirming redirect to".
  - Auto-confirm still sends the email and the file.
- Visual Automations on the Newsletter Plan (older, contradicts the page above): https://help.kit.com/en/articles/9053626-visual-automations-on-the-newsletter-plan
- Kit features page FAQ (marketing page): https://kit.com/features says "Email sequences, Visual Automations, and the Kit App Store start on the Creator plan."

## Where to host the PDF: recommendation

**Recommended: both, each for its own job.**

1. **New subscribers: use Kit's Download upload** on form 10088120.
   - The file never sits on botsdothat.com, so it can't end up in the sitemap, llms.txt, search results or the site search index.
   - Nothing to build or deploy.
   - It updates by re-uploading.
   - Filename: `StarterPack.pdf`, which is short with no spaces or underscores, per Kit's troubleshooting page.
2. **Existing subscribers, and the resend link in future issues: an unlisted URL on botsdothat.com,** e.g. `/subscribers/starter-pack-<random>/StarterPack.pdf`.
   - Keep it out of the sitemap, llms.txt and search-index.json (build.py generates those, so it needs a small exclusion).
   - Caveats:
     - The site is on **GitHub Pages**, which can't send a `noindex` header for a PDF. "Unlisted" just means unlinked: anyone with the link can open it, and search engines could find it if someone posts the link publicly.
     - Don't add it to robots.txt either. A Disallow line publishes the path.
   - This needs a deploy, so it needs Nik's approval.

If Nik wants just one option, use **Kit Download only**, and skip resending to the existing list. That way nothing touches the live site.

## Steps for Nik (or for us, after approval)
1. Kit > Grow > Landing Pages & Forms > form 10088120 > **Settings > Incentive** (the Form builder's name for the Confirmation Email tab).
2. Keep "Send incentive/confirmation email" **on** and "Auto-confirm new subscribers" **off**, so double opt-in stays as it is today.
3. **Edit Email Contents.** Paste Version A from welcome-email.md: a subject line, the preview text and the body. Change only the button *text*, and leave Kit's confirm link alone.
4. Under **After confirming redirect to**, choose **Download** and upload `StarterPack.pdf`. (Or choose URL and paste the unlisted link, if option 2 is chosen.)
5. Save, then **Publish** the form. Kit's troubleshooting page says to check the file is still listed after publishing.
6. Test with your own address, e.g. a plus alias: sign up on botsdothat.com, confirm, and check the PDF downloads on phone and desktop.
7. Only then update the site signup copy (signup-copy.md). That step is a deploy, so it needs approval.

## Not verified (check in Kit before relying on it)
- The exact upload file size limit. Kit says only "provided they meet the platform's file size and type requirements." Our PDF is about 0.26 MB.
- Whether link-click tagging in broadcasts is available on Free.
- The exact current names of the Kit menus. Kit's own articles use both "Confirmation Email" and "Incentive".
