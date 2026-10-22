#!/usr/bin/env python3
"""Convert generated art in art/incoming/ (png/jpg/webp) into optimized WebP in static/img/.
File names decide the slot: hero.*, og-bg.*, cat-<category>.* (see art/PROMPTS.md). Needs Pillow."""
import os, glob
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZES = {"hero": (1280, 720), "og-bg": (1200, 630)}
# hero-radar: square crop of the hero art centred on its radar, used inside the homepage radar.
# Centre/half-size are fractions of the hero image (measured on the 2026-10-20 art; re-measure if hero changes).
HERO_RADAR = {"cx": 885 / 1280, "cy": 360 / 720, "half": 330 / 720, "size": 640}
os.makedirs(os.path.join(ROOT, "static", "img"), exist_ok=True)
for f in sorted(glob.glob(os.path.join(ROOT, "art", "incoming", "*"))):
    name, ext = os.path.splitext(os.path.basename(f))
    if ext.lower() not in (".png", ".jpg", ".jpeg", ".webp"): continue
    im = Image.open(f).convert("RGB")
    w, h = SIZES.get(name, (640, 640))
    sr, tr = im.width / im.height, w / h  # center-crop to target ratio, then resize
    if sr > tr: nw = int(im.height * tr); im = im.crop(((im.width - nw) // 2, 0, (im.width + nw) // 2, im.height))
    elif sr < tr: nh = int(im.width / tr); im = im.crop((0, (im.height - nh) // 2, im.width, (im.height + nh) // 2))
    im = im.resize((w, h), Image.LANCZOS)
    out = os.path.join(ROOT, "static", "img", name + ".webp"); im.save(out, "WEBP", quality=80, method=6)
    print(f"{name}: {w}x{h} -> {os.path.getsize(out)//1024} KB")
    if name == "hero":
        src = Image.open(f).convert("RGB"); W, H = src.size; c = HERO_RADAR
        hs = int(c["half"] * H); cx, cy = int(c["cx"] * W), int(c["cy"] * H)
        sq = src.crop((cx - hs, cy - hs, cx + hs, cy + hs)).resize((c["size"], c["size"]), Image.LANCZOS)
        o2 = os.path.join(ROOT, "static", "img", "hero-radar.webp"); sq.save(o2, "WEBP", quality=80, method=6)
        print(f"hero-radar: {c['size']}x{c['size']} -> {os.path.getsize(o2)//1024} KB")
