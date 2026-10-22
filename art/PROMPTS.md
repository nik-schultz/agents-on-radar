# Image slots and exact prompts

The site renders CSS "art slots" until real images exist. To add art: generate with these prompts,
save into `art/incoming/<slot>.png`, run `python3 scripts/optimize_images.py`, then `python3 scripts/build.py`.
WebP files land in `static/img/` and the build uses them automatically (hero 1280x720 plus a square `hero-radar` crop centred on its radar, og-bg 1200x630, others 640x640).

Style for all: dark navy background, glassy translucent 3D object, cyan (#5ef2d6) and violet (#c08bff) neon rim light, soft bloom, minimal, no text/letters/logos.

| Slot | Status | Prompt |
|---|---|---|
| hero | Live (2026-10-20 08:04 CDT): used as the homepage radar (square `hero-radar.webp` crop, 16 KB; full `hero.webp` 19 KB kept for reuse) | Wide cinematic hero artwork for a website about AI agents doing everyday tasks. Dark deep-navy to black background with a glowing circular radar scope in the center, concentric rings and a sweeping cyan-to-violet light beam. Small glassy translucent 3D icons float as blips on the radar: an envelope, a shopping cart, a calendar, a plane, a receipt, a house. Soft bloom, subtle grain, futuristic but friendly, lots of negative space on the left for headline text. No text, no letters, no logos. (16:9) |
| og-bg | Live (2026-10-20 08:04 CDT): background of the generated og.png (17 KB webp) | Social share card background, dark navy to black gradient with glowing cyan and violet aurora light, a minimal glassy radar ring on the right side with a few bright blips, faint grid lines, soft bloom, premium tech aesthetic, large empty space on the left half for text overlay. No text, no letters, no logos. (16:9) |
| cat-inbox | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (17 KB webp) | Square illustration, glassy translucent 3D isometric envelope stacked with paper documents and a small glowing checkmark, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |
| cat-money | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (15 KB webp) | Square illustration, glassy translucent 3D isometric wallet with a few coins and a paper bill with a glowing downward arrow, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no numbers, no logos. |
| cat-shopping | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (28 KB webp) | Square illustration, glassy translucent 3D isometric shopping cart filled with groceries like an apple, bread and a milk carton, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |
| cat-travel | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (18 KB webp) | Square illustration, glassy translucent 3D isometric paper plane and a small boarding pass with a glowing clock, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |
| cat-family | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (21 KB webp) | Square illustration, glassy translucent 3D isometric small house with a calendar page and a school backpack beside it, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |
| cat-health | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (23 KB webp) | Square illustration, glassy translucent 3D isometric medical clipboard with a heart pulse line and a pill bottle, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |
| cat-work | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (17 KB webp) | Square illustration, glassy translucent 3D isometric briefcase with a floating checklist and a small chat bubble, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |
| cat-business | Live (2026-10-20 08:04 CDT): category tiles, category page header, blueprint cards (16 KB webp) | Square illustration, glassy translucent 3D isometric small shop storefront with an awning, a receipt and a rising bar chart, floating on a dark navy background with cyan and violet neon rim light, soft bloom, minimal, premium tech style. No text, no letters, no logos. |

Blueprint cards reuse the category art of their area (field `art` in data/blueprints.json).
The og:image (`assets/og.png`, 1200x630) is generated at build time with Pillow and uses `og-bg.webp` as background when present.

## Notes (2026-10-20)
- The hero art has its own radar, so the homepage hides the CSS rings and sweep when `hero-radar.webp` exists, and draws only the live trending blips plus a soft "ping" ring over it. That way the two radars never stack. Without the image, the CSS radar comes back.
- The `hero-radar` crop centre is set in `scripts/optimize_images.py` (`HERO_RADAR`) and was measured on this artwork. Re-measure it if you replace `hero.png`.
- Below-the-fold images load lazily. The hero radar and the category/blueprint header art load eagerly.
