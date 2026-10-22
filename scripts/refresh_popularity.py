#!/usr/bin/env python3
"""Refresh popularity numbers from REAL measurements only.

  python3 scripts/refresh_popularity.py --export-ids
      Prints the X post ids we track, in batches of 100 (one line per batch), for the daily agent
      to pass to the X API tool `get_posts_by_ids` (post.fields=public_metrics,created_at).
  python3 scripts/refresh_popularity.py --from-x FILE [FILE ...]
      Merges saved get_posts_by_ids / search_posts_all responses (raw tool output is fine; text before
      the first "{" is ignored). Updates likes, reposts, replies, bookmarks, views and measured_at.
  python3 scripts/refresh_popularity.py --from-reddit FILE
      FILE is JSON lines: {"url": ..., "upvotes": int, "comments": int, "measured_at": "YYYY-MM-DD"}.

Posts missing from the response keep their old numbers and are reported as stale. Nothing is ever
estimated. Every update is appended to data/popularity-history.jsonl."""
import json, os, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UCP = os.path.join(ROOT, "data", "use-cases.json")
HIST = os.path.join(ROOT, "data", "popularity-history.jsonl")
today = datetime.date.today().isoformat()
ucs = json.load(open(UCP))

def load_json_loose(path):
    s = open(path).read(); i = s.find("{"); j = s.rfind("}")
    return json.loads(s[i:j + 1])

def log(rec):
    with open(HIST, "a") as h: h.write(json.dumps(rec) + "\n")

args = sys.argv[1:]
if not args or args[0] == "--export-ids":
    ids = [x["popularity"]["post_id"] for x in ucs if (x.get("popularity") or {}).get("platform") == "x" and x["popularity"].get("post_id")]
    for i in range(0, len(ids), 100): print(",".join(ids[i:i + 100]))
    sys.exit(0)

updated, stale = 0, []
if args[0] == "--from-x":
    metrics = {}
    for f in args[1:]:
        d = load_json_loose(f)
        for p in d.get("data", []):
            if "public_metrics" in p: metrics[p["id"]] = p["public_metrics"]
    for x in ucs:
        p = x.get("popularity")
        if not p or p.get("platform") != "x": continue
        m = metrics.get(p.get("post_id"))
        if not m: stale.append(x["slug"]); continue
        p.update({"likes": m.get("like_count", 0), "reposts": m.get("repost_count", m.get("retweet_count", 0)), "replies": m.get("reply_count"),
                  "bookmarks": m.get("bookmark_count"), "views": m.get("impression_count"), "measured_at": today})
        log({"slug": x["slug"], "platform": "x", "post_id": p["post_id"], "likes": p["likes"], "reposts": p["reposts"], "measured_at": today}); updated += 1
elif args[0] == "--from-reddit":
    rows = {}
    for line in open(args[1]):
        if line.strip(): r = json.loads(line); rows[r["url"].rstrip("/")] = r
    for x in ucs:
        p = x.get("popularity")
        if not p or p.get("platform") != "reddit": continue
        r = rows.get(p["url"].rstrip("/"))
        if not r: stale.append(x["slug"]); continue
        if not isinstance(r.get("upvotes"), int): continue
        p.update({"upvotes": r["upvotes"], "comments": r.get("comments"), "measured_at": r.get("measured_at", today)}); p.pop("note", None)
        log({"slug": x["slug"], "platform": "reddit", "url": p["url"], "upvotes": p["upvotes"], "measured_at": p["measured_at"]}); updated += 1
else:
    print(__doc__); sys.exit(2)
json.dump(ucs, open(UCP, "w"), indent=1, ensure_ascii=False)
print(f"refresh_popularity: {updated} updated, {len(stale)} not in this batch (kept old numbers): {', '.join(stale) if stale else '-'}")
