#!/usr/bin/env python3
"""Check every internal link/src in site/ resolves to a file. --external also HEAD-checks outside links (report only;
many sites block scripts with 403/429, which is not proof a page is gone)."""
import os, re, sys, urllib.request, urllib.parse, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
CFG = json.load(open(os.path.join(ROOT, "config.json")))
_bu = urllib.parse.urlparse(CFG.get("base_url") or "https://" + re.sub(r"[^a-z0-9]", "", CFG["site_name"].lower()) + ".com")
SELF = f"{_bu.scheme}://{_bu.netloc}"  # origin; links to it are checked as internal
BP = (CFG.get("base_path") or _bu.path).rstrip("/")
bad, ext, n = [], set(), 0
for d, _, fs in os.walk(SITE):
    for f in fs:
        if not f.endswith(".html"): continue
        s = open(os.path.join(d, f)).read()
        for m in re.finditer(r'(?:href|src)="([^"]+)"', s):
            l = m.group(1); n += 1
            if l.startswith(SELF + "/") or l == SELF: l = l[len(SELF):] or "/"  # canonical/og/feed links to our own site: check the file exists
            if l.startswith(("http://", "https://")): ext.add(l); continue
            if l.startswith(("mailto:", "#", "data:")): continue
            path = urllib.parse.urlparse(l).path
            if BP and path.startswith("/"):
                if not (path == BP or path.startswith(BP + "/")): bad.append((os.path.relpath(os.path.join(d, f), SITE), l + "  (missing base path " + BP + ")")); continue
                path = path[len(BP):] or "/"
            t = os.path.join(SITE, path.lstrip("/"))
            if path.endswith("/"): t = os.path.join(t, "index.html")
            if not os.path.exists(t): bad.append((os.path.relpath(os.path.join(d, f), SITE), l))
for b in bad: print("BROKEN", *b)
print(f"check_links: {n} links scanned, {len(bad)} broken internal, {len(ext)} unique external")
if "--external" in sys.argv:
    fails = []
    for l in sorted(ext):
        try:
            r = urllib.request.urlopen(urllib.request.Request(l, method="HEAD", headers={"User-Agent": "Mozilla/5.0 linkcheck"}), timeout=12); code = r.status
        except urllib.error.HTTPError as e: code = e.code
        except Exception as e: code = type(e).__name__
        if code != 200: fails.append((code, l))
    for c, l in fails: print("EXTERNAL", c, l)
    print(f"external: {len(ext)-len(fails)} OK, {len(fails)} not-200 (often bot-blocking; verify by hand)")
sys.exit(1 if bad else 0)
