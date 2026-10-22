#!/usr/bin/env python3
"""Validate data/*.json. Exit 1 on any error. Used by the build pipeline and add_use_cases.py."""
import json, os, re, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: json.load(open(os.path.join(ROOT, *p)))
DIFFS = {"Easy", "Medium", "Advanced"}
REQ = ["slug", "title", "category", "date_added", "summary", "what_the_bot_does", "what_you_end_up_with", "difficulty", "tools", "prompt", "sources"]

def is_date(s):
    try: datetime.date.fromisoformat(str(s)[:10]); return True
    except Exception: return False

def check_use_case(x, cats, tools):
    errs, s = [], x.get("slug", "?")
    for k in REQ:
        if not x.get(k): errs.append(f"{s}: missing {k}")
    if x.get("slug") and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", x["slug"]): errs.append(f"{s}: bad slug")
    if x.get("category") and x["category"] not in cats: errs.append(f"{s}: unknown category {x['category']}")
    if x.get("difficulty") and x["difficulty"] not in DIFFS: errs.append(f"{s}: difficulty must be one of {sorted(DIFFS)}")
    if x.get("date_added") and not is_date(x["date_added"]): errs.append(f"{s}: date_added not ISO")
    if x.get("source_date") and not is_date(x["source_date"]): errs.append(f"{s}: source_date not ISO")
    for t in x.get("tools", []):
        if t.get("id") not in tools: errs.append(f"{s}: unknown tool {t.get('id')} (add it to data/tools.json first)")
    if not isinstance(x.get("what_the_bot_does", []), list): errs.append(f"{s}: what_the_bot_does must be a list")
    for src in x.get("sources", []):
        if not str(src.get("url", "")).startswith("http"): errs.append(f"{s}: source without http url")
        if not src.get("label"): errs.append(f"{s}: source without label")
    p = x.get("popularity")
    if p is not None:
        if p.get("platform") not in ("x", "reddit"): errs.append(f"{s}: popularity.platform must be x or reddit")
        if not str(p.get("url", "")).startswith("http"): errs.append(f"{s}: popularity.url required")
        if not is_date(p.get("measured_at")): errs.append(f"{s}: popularity.measured_at required (ISO date)")
        if not is_date(p.get("posted_at")): errs.append(f"{s}: popularity.posted_at required (ISO date)")
        keys = ["likes", "reposts"] if p.get("platform") == "x" else ["upvotes"]
        for k in keys:
            if not isinstance(p.get(k), int) or p[k] < 0: errs.append(f"{s}: popularity.{k} must be a measured non-negative integer")
    return errs

def main():
    cats = {c["slug"] for c in J("data", "categories.json")}
    tools = J("data", "tools.json")
    ucs = J("data", "use-cases.json")
    errs = []
    seen = set()
    for x in ucs:
        if x.get("slug") in seen: errs.append(f"duplicate slug {x.get('slug')}")
        seen.add(x.get("slug"))
        errs += check_use_case(x, cats, tools)
    for b in J("data", "blueprints.json"):
        for k in ["slug", "title", "goal", "trigger", "watches", "steps", "tools", "instructions", "safety"]:
            if not b.get(k): errs.append(f"blueprint {b.get('slug')}: missing {k}")
        for r in b.get("related", []):
            if r not in seen: errs.append(f"blueprint {b['slug']}: related use case {r} not found")
        for t in b.get("tools", []):
            if t.get("id") not in tools: errs.append(f"blueprint {b['slug']}: unknown tool {t.get('id')}")
    # AI price table: every row needs a numeric price, an official source URL and a check date; warn when stale
    pr = J("data", "ai-pricing.json")
    for r in pr["api"]:
        if not (isinstance(r.get("input"), (int, float)) and isinstance(r.get("output"), (int, float))): errs.append(f"ai-pricing {r.get('model')}: non-numeric price")
        if not str(r.get("source_url", "")).startswith("https://") or not is_date(r.get("checked_on")): errs.append(f"ai-pricing {r.get('model')}: needs source_url + checked_on")
    for r in pr["consumer"] + pr["discounts"] + pr.get("voice", []):
        if not str(r.get("source_url", "")).startswith("https://") or not is_date(r.get("checked_on")): errs.append(f"ai-pricing {r.get('provider')}: needs source_url + checked_on")
    names = {r["model"] for r in pr["api"]}
    for m in pr["blueprint_models"]:
        if m not in names: errs.append(f"ai-pricing blueprint_models: {m} not in api rows")
    import datetime as _dt
    age = (_dt.date.today() - _dt.date.fromisoformat(pr["checked_on"])).days
    if age > 7: print(f"WARN ai-pricing.json last checked {age} days ago; re-check the official pages (weekly)")
    # Latest in AI: every item needs a date, headline, explainer, known category and an https source; flag a stale feed
    nw = J("data", "news.json"); ids = set()
    for n in nw["items"]:
        nid = n.get("id")
        if not nid or nid in ids: errs.append(f"news {nid}: missing or duplicate id")
        ids.add(nid)
        if not is_date(n.get("date")): errs.append(f"news {nid}: bad date")
        for k in ("headline", "explainer", "source_name"):
            if not n.get(k): errs.append(f"news {nid}: missing {k}")
        if n.get("category") not in nw["categories"]: errs.append(f"news {nid}: unknown category {n.get('category')}")
        if not str(n.get("source_url", "")).startswith("https://"): errs.append(f"news {nid}: needs an https source_url")
        x = n.get("x")
        if x and not (str(x.get("url", "")).startswith("https://x.com/") and isinstance(x.get("likes"), int) and isinstance(x.get("reposts"), int) and is_date(x.get("measured_at"))):
            errs.append(f"news {nid}: x needs url, integer likes/reposts and measured_at")
        if x and not (is_date(x.get("posted_at")) and x.get("author", "").startswith("@") and x.get("kind") in ("official", "coverage") and (x.get("views") is None or isinstance(x.get("views"), int))):
            errs.append(f"news {nid}: x needs posted_at, @author, kind official|coverage, integer views (or none)")
        if n.get("impact") not in nw.get("impact_levels", ["major", "notable", "minor"]): errs.append(f"news {nid}: impact must be major | notable | minor")
        if not n.get("company"): errs.append(f"news {nid}: missing company (used for the tile colour/monogram)")
    if nw["items"]:
        newest = max(n["date"] for n in nw["items"] if is_date(n.get("date")))
        nage = (_dt.date.today() - _dt.date.fromisoformat(newest)).days
        if nage > 3: print(f"WARN news.json newest item is {nage} days old ({newest}); run the news update (README)")
    _cfg = J("config.json") if os.path.exists(os.path.join(ROOT, "config.json")) else {}
    for k, v in ((_cfg.get("verification") or {}).items()):
        if k.startswith("_") or not v: continue
        if "<" in v or '"' in v or "content=" in v or not re.fullmatch(r"[A-Za-z0-9_\-]{8,100}", v):
            errs.append(f"config verification.{k}: paste only the content value (letters, digits, - and _), not the whole meta tag")
    sp = J("data", "sponsors.json")
    for slot, items in sp.items():
        if not isinstance(items, list): continue
        for it in items:
            for k in ("name", "url", "headline"):
                if not it.get(k): errs.append(f"sponsors {slot}: missing {k}")
            if it.get("url") and not str(it["url"]).startswith("https://"): errs.append(f"sponsors {slot}: url must be https")
    for e in errs: print("ERROR", e)
    print(f"validate: {len(ucs)} use cases, {len(J('data','blueprints.json'))} blueprints, {len(errs)} errors")
    return 1 if errs else 0

if __name__ == "__main__": sys.exit(main())
