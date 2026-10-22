#!/usr/bin/env python3
"""Append new use cases from data/incoming/*.json to data/use-cases.json.

Each incoming file holds one use case object or a list of them, in the same shape as
data/use-cases.json (see data/incoming/_template.json.example). Rules:
  * popularity must be real (measured counts + url + measured_at) or null. Never estimate.
  * date_added defaults to today; origin defaults to "pipeline".
  * duplicates (same slug, or a popularity/source URL already used as the primary source) are skipped.
Processed files move to data/incoming/processed/. Rejected ones to data/incoming/rejected/ with a .err note.
Usage: python3 scripts/add_use_cases.py [--dry-run]"""
import json, os, sys, glob, shutil, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate import check_use_case
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *p: os.path.join(ROOT, *p)
dry = "--dry-run" in sys.argv
today = datetime.date.today().isoformat()
cats = {c["slug"] for c in json.load(open(P("data", "categories.json")))}
tools = json.load(open(P("data", "tools.json")))
ucs = json.load(open(P("data", "use-cases.json")))
slugs = {x["slug"] for x in ucs}
urls = {(x.get("popularity") or {}).get("url") for x in ucs} | {x["sources"][0]["url"] for x in ucs if x.get("sources")}
added, rejected = 0, 0
for f in sorted(glob.glob(P("data", "incoming", "*.json"))):
    data = json.load(open(f)); items = data if isinstance(data, list) else [data]
    errs_all = []
    for x in items:
        x.setdefault("date_added", today); x.setdefault("origin", "pipeline"); x.setdefault("last_checked", today)
        x.setdefault("setup", []); x.setdefault("watch_out", []); x.setdefault("tags", []); x.setdefault("popularity", None)
        x.setdefault("source_date", (x.get("popularity") or {}).get("posted_at"))
        errs = check_use_case(x, cats, tools)
        if x.get("slug") in slugs: errs.append(f"{x.get('slug')}: slug already exists")
        pu = (x.get("popularity") or {}).get("url")
        if pu and pu in urls: errs.append(f"{x.get('slug')}: popularity source already used by another entry")
        if errs: errs_all += errs; rejected += 1; continue
        ucs.insert(0, x); slugs.add(x["slug"]); urls.add(pu); added += 1
        print("added", x["slug"])
    if not dry:
        dest = "processed" if not errs_all else "rejected"
        os.makedirs(P("data", "incoming", dest), exist_ok=True)
        shutil.move(f, P("data", "incoming", dest, os.path.basename(f)))
        if errs_all: open(P("data", "incoming", dest, os.path.basename(f) + ".err"), "w").write("\n".join(errs_all) + "\n")
    for e in errs_all: print("REJECT", e)
if not dry and added: json.dump(ucs, open(P("data", "use-cases.json"), "w"), indent=1, ensure_ascii=False)
print(f"add_use_cases: {added} added, {rejected} rejected{' (dry run)' if dry else ''}")
