#!/usr/bin/env python3
"""Is the live Today edition current? Used by the routines after a deploy.
  python3 scripts/check_today.py                       # checks https://botsdothat.com/today/ and the Today box on https://botsdothat.com/
  python3 scripts/check_today.py --expect 2026-11-20   # check against a given edition date instead of today's (America/Chicago)
  python3 scripts/check_today.py --site site           # check a local build instead of the live site
Reads the <h1 class="td-date"> and data-edition on /today/, and data-edition on the home page's Today box.
Expected edition = today's date in America/Chicago, rolled back to Friday on weekends (scripts/today.py latest_edition).
Exit 0 = current, 1 = stale or missing (print says which)."""
import argparse, datetime, os, re, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import today as T

def fetch(base, path, local):
    if local:
        fp = os.path.join(base, path.strip("/"), "index.html")
        with open(fp, encoding="utf-8") as fh: return fh.read()
    req = urllib.request.Request(base.rstrip("/") + path + f"?check={datetime.datetime.now().timestamp():.0f}", headers={"User-Agent": "BotsDoThat-site-check", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r: return r.read().decode("utf-8")

def chicago_today():
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo("America/Chicago")).date()
    except Exception:
        return datetime.date.today()

def check(base, expect, local=False):
    problems, want = [], expect.isoformat()
    t = fetch(base, "/today/", local)
    h1 = re.search(r'<h1 class="td-date">([^<]+)</h1>', t)
    ed = re.search(r'<div class="td" data-edition="(\d{4}-\d{2}-\d{2})"', t)
    want_h1 = expect.strftime("%A, %b %-d")
    if not h1: problems.append("/today/: no <h1 class=\"td-date\"> heading")
    elif h1.group(1).strip() != want_h1: problems.append(f"/today/: td-date heading is {h1.group(1).strip()!r}, expected {want_h1!r}")
    if not ed or ed.group(1) != want: problems.append(f"/today/: data-edition is {ed.group(1) if ed else 'missing'}, expected {want}")
    h = fetch(base, "/", local)
    box = re.search(r'class="hb-today"[^>]*data-edition="(\d{4}-\d{2}-\d{2})"', h)
    if not box or box.group(1) != want: problems.append(f"home Today box: data-edition is {box.group(1) if box else 'missing'}, expected {want}")
    return problems

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="https://botsdothat.com")
    ap.add_argument("--site", help="local build folder (e.g. site) instead of --base")
    ap.add_argument("--expect", help="YYYY-MM-DD edition date (default: latest weekday edition in America/Chicago)")
    a = ap.parse_args()
    exp = datetime.date.fromisoformat(a.expect) if a.expect else T.latest_edition(chicago_today())
    probs = check(a.site or a.base, exp, local=bool(a.site))
    where = a.site or a.base
    if probs:
        print(f"STALE Today edition on {where} (expected {exp.strftime('%A, %b %-d')}):\n- " + "\n- ".join(probs)); sys.exit(1)
    print(f"OK: {where}/today/ and the home Today box show {exp.strftime('%A, %b %-d')} ({exp.isoformat()})")
