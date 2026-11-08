# Builder path comparison, 8 November 2026

Bounded check of two paths that are already on the branch. This is not a user study, not an A/B test, and not evidence of what a person would prefer or pay. No model was asked to produce a weekly plan. Sign-in, checkout, and live launch stayed off. Nothing was merged or deployed.

The pages were the built site at `http://127.0.0.1:8090/`. There is no public preview. The browser was headless Chrome 156. Safari was not available.

## How counts were made

- A click is one pointer activation, including a radio or a checkbox.
- A field entry is one field set to its final fictional value, not one keystroke.
- A navigation is one URL change or reload.
- A step is one named intention in the log.
- Seconds are the automated script's wall clock on this machine. They are not a human completion time. Path B's script finished in less time because it skipped the replacement prompts. That does not mean the from-scratch form is easier.

Shared fictional week, used by both paths for the instructions: Monday 9 November 2026, America/Puerto_Rico, fixed line "Tuesday afternoon is unavailable.", tasks of 4, 3, 2, and 1 hours, 8 hours already free after fixed time and buffers. No private data.

## Minimum path, excluding the extra probes

Path A, homepage "Try a weekly-planning example":

- 1 navigation to `/bot-instructions/#weekly-sample`
- The hour card is already filled with the overloaded week
- 1 click, Make it mine
- 1 click, Write instructions
- 0 typed fields if the fictional numbers are kept

Path B, header "Build your bot":

- 1 navigation to `/bot-instructions/` with no sample hash
- Weekly fields are absent until the task is chosen
- 1 click to choose weekly planning
- 7 text fields plus 1 required shape choice to match the same week
- 1 click, Write instructions

The full script also ran the hour checks, the replacement prompts, the clipboard refusal, the review, and the storage cases. Those totals were: path A, 20 clicks, 28 field entries, 4 navigations, 17 steps, 4.93 seconds; path B, 14 clicks, 34 field entries, 2 navigations, 13 steps, 3.69 seconds.

## Results

Both paths produced instructions of 8,237 characters that quoted "Tuesday afternoon is unavailable." and did not contain the cancelled text "KEEP THIS". The arithmetic on the sample card matched for both paths.

| Check | Path A | Path B | 320px |
|---|---|---|---|
| Overloaded week, 8 available and 10 of tasks, 2 hours to move | Pass | Pass | Pass, summary visible |
| Missing estimate does not say the week fits | Pass | Pass | Not separately repeated |
| 8 available and 7 of tasks stays "within the hours entered" | Pass | Pass | Not separately repeated |
| Deferring the 1 hour reading still leaves 1 hour | Pass | Pass | Not separately repeated |
| No clock time added by the hour summary or the check-in block | Pass | Pass | Not separately repeated |
| Make it mine / from-scratch reaches copy-ready instructions | Pass | Pass | Pass, write control is 53px tall and the page does not scroll sideways |
| Second fill asks, and Cancel keeps the exact sentence | Pass | Not on this path | Not repeated |
| Changing the hour card does not fill the form by itself | Not the A route | Pass | Not repeated |
| Checks start on Not checked | Pass | Pass | Not repeated |
| Forced clipboard refusal names select-or-download and does not mark Pass | Pass | Pass | Not repeated |
| Editing facts after a Fail sets Needs recheck | Pass | Pass | Not repeated |
| "Nothing to change" adds no patch | Pass | Pass | Not repeated |
| Apply then Undo restores the exact text; version goes to v2 and back | Pass | Pass | Not repeated |
| Reload after a successful save says a copy was loaded | Pass, 8,237 characters | Not repeated | Not repeated |
| Malformed saved text is not applied | Pass | Not repeated | Not repeated |
| A newer tab is announced and not applied by itself | Pass | Not repeated | Not repeated |
| Sign-in, checkout, and live launch stay off; My bots hidden | Pass | Pass | Header still shows Build your bot |
| Local-only privacy sentence is on the page | Pass | Pass | Visible in the 320 path A shot |
| Reduced motion stops the radar float | Pass, shared | Pass, shared | Not repeated |
| Keyboard can focus the Build your bot link | Pass, shared | Pass, shared | Not a full tab walk |

Not tested: a real clipboard permission prompt, Safari or Firefox, two operating-system windows (the newer-tab case was a `storage` event in the same page), byte-for-byte equality of the reloaded instructions (the length and the loaded status matched), and any reply from ChatGPT or another app.

## Defect

Major, trust, not a blocker to copying instructions.

The version line says the text was saved when the browser refused to store it.

1. Open `/bot-instructions/` and clear this site's local storage.
2. Choose "Show a made-up example" so a save succeeds. The status is "Saved on this device only. Not an account."
3. Make `localStorage.setItem` throw.
4. Click "Write instructions" again.

Observed: the save line correctly says "Not saved. This browser refused to store it. You can still copy or download." The version line still says "Version v1. Saved on this device only. Not sent to BotsDoThat."

The first automated attempt did not hit this. A newer-tab conflict fired first and also begins with "Not saved", so that attempt is not evidence about a thrown write. The steps above were run separately.

Suggested fix, not applied: the version line should not say Saved unless the write succeeded.

## Obstacle, not a broken control

After writing the sample instructions, the weekly check-in starts about 7,520 pixels from the top of the builder page. At a 900 pixel window that is several screens below the form. The script could still activate the controls. A person has to scroll past the instruction text to reach Apply and Undo. Suggested fix, not applied: keep the check-in next to the handoff, or shorten the on-page instruction preview.

## Which path should lead

Lead with path A, the fictional example. A person can reach copy-ready instructions for the shared week without typing, can see the overload before the form, and Cancel protected a sentence they had typed. Path B is the right route when they want their own notes first: the weekly fields stay hidden until they choose the task, and editing the hour card does not overwrite those fields. This is a judgment about steps and required fields in this script, not a claim about conversion or about which path people would like.

## Logs and screenshots

- Machine log: `/opt/cursor/artifacts/qa-path-log.json`
- Path A, desktop, after a refused copy: `/opt/cursor/artifacts/screenshot_path_a_desktop.png`
- Path B, desktop, form filled from scratch: `/opt/cursor/artifacts/screenshot_path_b_desktop.png`
- Path A at 320px, privacy copy and header: `/opt/cursor/artifacts/screenshot_path_a_320.png`
- Path B at 320px, fictional week and the 8 / 10 / 2 line: `/opt/cursor/artifacts/screenshot_path_b_320.png`
- Homepage at 320px: `/opt/cursor/artifacts/screenshot_path_mobile_home.png`
