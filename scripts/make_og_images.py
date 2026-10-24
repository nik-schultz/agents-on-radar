import json, csv, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
OUT = "/workspace/botsdothat/og-images"; ART = OUT + "/_art"
FD = "/usr/share/fonts/truetype/sand-box/google/Poppins/"
F = lambda w, s: ImageFont.truetype(FD + f"Poppins-{w}.ttf", s)
W, H = 1200, 630
BG = (5, 7, 15); TEAL = (80, 255, 200); WHITE = (242, 245, 255); MUTED = (150, 165, 210)
uc = {x["slug"]: x for x in json.load(open("/workspace/platform/data/use-cases.json"))}
cats = {c["slug"]: c["name"] for c in json.load(open("/workspace/platform/data/categories.json"))}
# Order and heat copied from the live https://botsdothat.com/trending/ "Full ranking" table, fetched 2026-10-24
RANK = [("build-a-second-brain-your-bot-reads",1209),("call-and-book-by-phone",1051),("family-meal-plan-and-grocery-order",417),
("hand-your-most-hated-chores-to-a-personal-agent",262),("sunday-family-calendar-check",251),("newsletter-daily-report",165),
("restaurant-reservations-by-agent",162),("give-your-agents-a-shared-apple-account",140),("email-scam-filter",139),
("proactive-next-moves-bot",126),("team-of-agents-with-roles",114),("send-a-long-video-or-thread-to-your-bot",108),
("log-meals-and-weight-by-voice",101),("make-a-customer-service-call",98),("run-family-logistics-from-the-group-chat",95)]
SECTIONS = [("use-cases","https://botsdothat.com/use-cases/","ALL USE CASES","AI agent use cases, in plain English","Real examples with sources and a prompt to copy"),
("trending","https://botsdothat.com/trending/","TRENDING NOW","What people are getting bots to do right now","Ranked by real likes and reposts, with dates"),
("blueprints","https://botsdothat.com/blueprints/","BUILD A BOT","Bot blueprints for beginners","Step-by-step plans you can copy, no coding needed")]

def wrap(d, text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def render(slug, eyebrow, title, footer):
    im = Image.new("RGB", (W, H), BG)
    art = Image.open(f"{ART}/{slug}.jpg").convert("RGB").resize((630, 630), Image.LANCZOS)
    im.paste(art, (W - 630, 0))
    # fade the art's left edge into the background so the text side stays clean
    mask = Image.new("L", (W, 1)); mask.putdata([255 if x < 560 else max(0, int(255 * (1 - (x - 560) / 260))) for x in range(W)])
    im = Image.composite(Image.new("RGB", (W, H), BG), im, mask.resize((W, H)))
    # soft glow behind text
    glow = Image.new("RGB", (W, H), (0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse((-260, 330, 380, 900), fill=(0, 90, 110)); glow = glow.filter(ImageFilter.GaussianBlur(140))
    im = Image.blend(im, Image.composite(glow, im, Image.new("L", (W, H), 255)), 0.0) if False else Image.fromarray(__import__("numpy").clip(__import__("numpy").asarray(im, dtype="int16") + __import__("numpy").asarray(glow, dtype="int16") // 2, 0, 255).astype("uint8"))
    d = ImageDraw.Draw(im)
    d.ellipse((68, 66, 86, 84), fill=TEAL)
    d.text((98, 55), "BotsDoThat", font=F("SemiBold", 30), fill=WHITE)
    d.text((70, 128), eyebrow.upper(), font=F("SemiBold", 22), fill=TEAL)
    maxw = 560
    for size in (64, 60, 56, 52, 48, 44):
        f = F("Bold", size); lines = wrap(d, title, f, maxw)
        if len(lines) <= 4: break
    lh = int(size * 1.18); y = 170
    for ln in lines: d.text((68, y), ln, font=f, fill=WHITE); y += lh
    d.text((70, 548), footer, font=F("Medium", 24), fill=MUTED)
    p = f"{OUT}/{slug}.png"; im.save(p, optimize=True)
    if os.path.getsize(p) > 1_000_000: im.convert("P", palette=Image.ADAPTIVE, colors=256).save(p, optimize=True)
    return p

rows = []
for i, (s, heat) in enumerate(RANK, 1):
    x = uc[s]; p = x["popularity"]
    render(s, cats.get(x["category"], x["category"]), x["title"], "botsdothat.com  ·  Use case with a prompt to copy")
    sig = (f"Live botsdothat.com/trending/ rank #{i} of 38 (heat {heat}, fetched 2026-10-24); "
           f"source X post {p['url']} by {p['author']}: {p['likes']} likes, {p['reposts']} reposts, measured {p['measured_at']}")
    rows.append((f"https://botsdothat.com/use-cases/{s}/", f"{s}.png", sig))
for s, url, eb, title, sub in SECTIONS:
    render(s, eb, title, "botsdothat.com  ·  " + sub)
    rows.append((url, f"{s}.png", "Section index image (not popularity-ranked)"))
with open(f"{OUT}/manifest.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page_url", "image_file", "popularity_signal"]); w.writerows(rows)
print(len(rows), "images")
