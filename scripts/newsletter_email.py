#!/usr/bin/env python3
"""Render one BotsDoThat Weekly issue as email HTML for Kit (inline CSS, table layout, dark site palette).
  python3 scripts/newsletter_email.py 2            -> ops/newsletter/issue-2-email.html, issue-2-email-body.html, issue-2-meta.txt
Sends nothing. Paste the body file into Kit's HTML block (or use the full file)."""
import json, os, sys, html
from urllib.parse import urlencode
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: json.load(open(os.path.join(ROOT, *p)))
cfg = J("config.json"); BASE = cfg.get("base_url", "https://botsdothat.com").rstrip("/")
NUM = int(sys.argv[1]) if len(sys.argv) > 1 else max(i["number"] for i in J("data", "newsletter.json")["issues"])
iss = next(i for i in J("data", "newsletter.json")["issues"] if i["number"] == NUM)
UC = {u["slug"]: u for u in J("data", "use-cases.json")}
NEWS = {n["id"]: n for n in J("data", "news.json")["items"]}
PROMO = ((cfg.get("sponsor_checkout") or {}).get("newsletter_promo_code") or "").strip()
e = lambda s: html.escape(str(s), quote=True)
def link(path, content="item"):
    return f"{BASE}{path}?" + urlencode({"utm_source": "newsletter", "utm_medium": "email", "utm_campaign": f"weekly-{NUM}", "utm_content": content})
# palette from static/style.css
BG, BG2, CARD, LINE, INK, MUTED, C1, C2, C3, WARN = "#05070f", "#0a0f1f", "#111834", "#232c52", "#eef1ff", "#a3acc9", "#5ef2d6", "#7c8cff", "#c08bff", "#ffcf6e"
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Inter,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Courier New',monospace"
def nice(d):
    import datetime; x = datetime.date.fromisoformat(d); return x.strftime("%B ") + str(x.day) + x.strftime(", %Y")
def btn(href, label, solid=True):
    bg = C2 if solid else BG2; fg = "#04121a" if solid else INK; bd = C2
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{bg}" style="border-radius:999px;background:{bg};border:1px solid {bd};">'
            f'<a href="{e(href)}" style="display:inline-block;padding:11px 20px;font-family:{FONT};font-size:15px;font-weight:700;line-height:1.2;color:{fg};text-decoration:none;border-radius:999px;">{e(label)}</a></td></tr></table>')
def eyebrow(t, color=C1):
    return f'<p style="margin:0 0 8px;font-family:{FONT};font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{color};">{e(t)}</p>'
def card(inner, border=LINE, bg=CARD):
    return (f'<tr><td style="padding:0 24px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="background:{bg};border:1px solid {border};border-radius:16px;">'
            f'<tr><td style="padding:22px 22px 20px;">{inner}</td></tr></table></td></tr>')
P = f"font-family:{FONT};font-size:16px;line-height:1.6;color:{INK};margin:0 0 14px;"
PM = f"font-family:{FONT};font-size:13px;line-height:1.55;color:{MUTED};margin:0;"
web = link(f"/newsletter/{iss['slug']}/", "web-version")
rows = []
# header image
rows.append(f'<tr><td style="padding:0;"><a href="{e(link("/", "header"))}" style="text-decoration:none;"><img src="{BASE}/assets/img/email-header.png" width="600" alt="BotsDoThat: what AI agents can do for real people" style="display:block;width:100%;max-width:600px;height:auto;border:0;border-radius:16px 16px 0 0;"></a></td></tr>')
rows.append(f'<tr><td style="padding:14px 24px 0;text-align:right;"><a href="{e(web)}" style="font-family:{FONT};font-size:13px;color:{MUTED};text-decoration:underline;">View in your browser</a></td></tr>')
rows.append(f'<tr><td style="padding:12px 24px 6px;">{eyebrow(f"BotsDoThat Weekly · Issue {NUM} · {nice(iss[chr(100)+"ate"])}")}'
            f'<h1 style="margin:0 0 14px;font-family:{FONT};font-size:28px;line-height:1.2;font-weight:800;letter-spacing:-0.5px;color:#ffffff;">{e(iss["subject"])}</h1>'
            f'<p style="{P}color:#cfd6f3;font-size:17px;">{e(iss["intro"])}</p></td></tr>')
for k, it in enumerate(iss["items"], 1):
    x = UC[it["slug"]]; href = link(f"/use-cases/{x['slug']}/", f"item-{k}")
    prompt = e(x["prompt"]).replace("\n", "<br>")
    inner = (eyebrow(f"Job {k} of {len(iss['items'])}", C2)
             + f'<h2 style="margin:0 0 10px;font-family:{FONT};font-size:21px;line-height:1.25;font-weight:800;color:#ffffff;"><a href="{e(href)}" style="color:#ffffff;text-decoration:none;">{e(x["title"])}</a></h2>'
             + f'<p style="{P}">{e(it["why"])}</p>'
             + f'<p style="{P}"><strong style="color:{C1};">You end up with:</strong> {e(x["what_you_end_up_with"])}</p>'
             + f'<p style="margin:0 0 6px;font-family:{FONT};font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};">Prompt to copy</p>'
             + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG2}" style="background:{BG2};border:1px solid {LINE};border-left:4px solid {C2};border-radius:10px;margin:0 0 16px;"><tr><td style="padding:14px 16px;font-family:{MONO};font-size:14px;line-height:1.6;color:#dfe4ff;">{prompt}</td></tr></table>'
             + f'<p style="{PM}margin:0 0 14px;">Difficulty: {e(x["difficulty"])} · Fill in the [brackets] first.</p>'
             + btn(href, "Full guide with watch-outs"))
    rows.append(card(inner))
np_ = iss.get("new_page")
if np_:
    x = UC.get(np_["slug"]); href = link(f"/use-cases/{np_['slug']}/" if x else np_.get("path", "/"), "new-page")
    title = x["title"] if x else np_.get("title", "")
    rows.append(card(eyebrow("New on the site", C1) + f'<h2 style="margin:0 0 10px;font-family:{FONT};font-size:20px;line-height:1.25;font-weight:800;color:#ffffff;"><a href="{e(href)}" style="color:#ffffff;text-decoration:none;">{e(title)}</a></h2><p style="{P}">{e(np_["note"])}</p>' + btn(href, "Read the guide"), border=C2))
w = NEWS.get(iss.get("watch_out") or "")
if w:
    rows.append(card(eyebrow(iss.get("watch_out_label") or "One thing that went wrong", WARN) + f'<h2 style="margin:0 0 10px;font-family:{FONT};font-size:19px;line-height:1.3;font-weight:800;color:#ffffff;">{e(w["headline"])}</h2><p style="{P}">{e(w["explainer"])}</p><p style="{PM}">Source: <a href="{e(w["source_url"])}" style="color:{C1};">{e(w["source_name"])}</a>, {nice(w["date"])}</p>'))
s = iss.get("sponsor")
if s:
    rows.append(card(eyebrow("Sponsored", WARN) + f'<h2 style="margin:0 0 8px;font-family:{FONT};font-size:19px;font-weight:800;color:#ffffff;">{e(s["headline"])}</h2><p style="{P}">{e(s.get("body", ""))}</p>' + btn(s["url"], s.get("cta", "Learn more")) + f'<p style="{PM}margin-top:12px;">Paid placement by {e(s["name"])}. It doesn\'t change what we pick.</p>', border=WARN))
else:
    code = (f' The first 2 newsletter slots are free: use code <strong style="color:{C1};font-family:{MONO};">{e(PROMO)}</strong> at checkout.' if PROMO else " Your first 2 issues are free.")
    rows.append(card(eyebrow("Your spot here · Sponsor this newsletter", WARN) + f'<h2 style="margin:0 0 8px;font-family:{FONT};font-size:19px;font-weight:800;color:#ffffff;">Sponsor the BotsDoThat Weekly</h2><p style="{P}">One short, clearly labeled sponsor block that matches the week\'s topic. Book and pay online, no back-and-forth.{code}</p>' + btn(link("/advertise/", "house-ad"), "See sponsor options", solid=False), border=LINE, bg=BG2))
rows.append(f'<tr><td style="padding:6px 24px 22px;"><p style="{P}">That\'s it for this week. Try one, and if something worked or broke, tell us at hello@botsdothat.com.</p><p style="{P}margin:0;">See you next Thursday,<br>BotsDoThat</p></td></tr>')
rows.append(f'<tr><td style="padding:20px 24px 26px;border-top:1px solid {LINE};text-align:center;">'
            f'<p style="{PM}margin:0 0 8px;"><a href="{e(web)}" style="color:{C1};">Read this issue on the web</a> · <a href="{e(link("/newsletter/", "footer"))}" style="color:{C1};">All issues</a> · <a href="{e(link("/", "footer"))}" style="color:{C1};">botsdothat.com</a></p>'
            f'<p style="{PM}margin:0 0 8px;">Questions or tips: <a href="mailto:hello@botsdothat.com" style="color:{C1};">hello@botsdothat.com</a></p>'
            f'<p style="{PM}">You\'re getting this because you signed up at botsdothat.com. The unsubscribe link and our mailing address are added below by Kit, our email provider.</p></td></tr>')
pre = iss.get("preview", "")
body = (f'<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{BG};opacity:0;">{e(pre)}' + "&#847; &zwnj; &nbsp; " * 30 + '</div>\n'
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};width:100%;"><tr><td align="center" style="padding:24px 10px;">\n'
        f'<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="width:100%;max-width:600px;background:{BG};border:1px solid {LINE};border-radius:16px;">\n'
        + "\n".join(rows) + "\n</table>\n</td></tr></table>\n")
full = (f'<!DOCTYPE html>\n<html lang="en" xmlns="http://www.w3.org/1999/xhtml"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<meta name="color-scheme" content="dark"><meta name="supported-color-schemes" content="dark"><title>{e(iss["subject"])}</title></head>\n'
        f'<body style="margin:0;padding:0;background:{BG};color:{INK};-webkit-text-size-adjust:100%;">\n{body}</body></html>\n')
out = os.path.join(ROOT, "ops", "newsletter"); os.makedirs(out, exist_ok=True)
open(os.path.join(out, f"issue-{NUM}-email.html"), "w").write(full)
open(os.path.join(out, f"issue-{NUM}-email-body.html"), "w").write(body)
open(os.path.join(out, f"issue-{NUM}-meta.txt"), "w").write(f"Subject: {iss['subject']}\nPreview text: {pre}\nWeb version: {BASE}/newsletter/{iss['slug']}/\nSender: hello@botsdothat.com (set in Kit)\n")
print("wrote", out, f"issue-{NUM}-*")
