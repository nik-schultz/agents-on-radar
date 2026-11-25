#!/usr/bin/env python3
"""BotsDoThat Today: the daily front page (/), the dated archive (/today/<date>/) and the Today RSS feed.

Everything here is chosen from data the routines already write, so the page fills itself:
  * "3 things that changed": data/news.json items for the edition date, ranked by importance (impact), then by
    whether they touch an assistant people use (Bot Checkup match), then by measured X views. Weekend items roll
    into Monday's edition. Each weekday still gets its own edition when no news is dated that day: the newest
    older items fill in and keep their own date. Never invent items. Weekends show Friday's edition.
  * "Job of the day": a use case added on the previous weekday (easiest first), so the job is fixed from the morning
    build and doesn't change when the midday routine adds new ones; otherwise a fixed rotation through the Easy use
    cases, so every date always gets the same job.
  * Overrides: data/today.json "days" -> {"YYYY-MM-DD": {"picks": [news ids], "job": "use-case-slug", "note": "..."}}.
    The routines may set these; nothing else needs editing.
Stdlib only. Pure functions so scripts/test_today.py can test them without building the site.
"""
import datetime, hashlib, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMPACT_RANK = {"major": 0, "notable": 1, "minor": 2}
DIFF_RANK = {"Easy": 0, "Medium": 1, "Advanced": 2}

# Which everyday app a news item is about, from its company. Used for the "I use..." picker (stored in the browser only).
APP_BY_COMPANY = {"OpenAI": "chatgpt", "Anthropic": "claude", "Google": "gemini", "xAI": "grok", "Meta": "meta",
                  "Microsoft": "copilot", "Perplexity": "perplexity", "Apple": "apple", "Amazon": "alexa"}
APPS = [("chatgpt", "ChatGPT"), ("claude", "Claude"), ("gemini", "Gemini"), ("grok", "Grok"), ("meta", "Meta AI"),
        ("copilot", "Copilot"), ("perplexity", "Perplexity"), ("apple", "Apple"), ("alexa", "Alexa")]


def load(root=ROOT):
    p = os.path.join(root, "data", "today.json")
    d = json.load(open(p)) if os.path.exists(p) else {}
    d.setdefault("days", {})
    return d


def validate(cfg, news, ucs):
    """Errors for overrides that point at things that don't exist (so a routine typo fails the build, not the page)."""
    errs = []
    ids = {n["id"] for n in news}
    slugs = {x["slug"] for x in ucs}
    fe = cfg.get("first_edition")
    if fe:
        try:
            if datetime.date.fromisoformat(fe).weekday() > 4:
                errs.append("first_edition must be a weekday")
        except ValueError:
            errs.append("first_edition is not an ISO date")
    for day, o in cfg.get("days", {}).items():
        try:
            datetime.date.fromisoformat(day)
        except ValueError:
            errs.append(f"days: {day!r} is not an ISO date"); continue
        for pid in o.get("picks", []):
            if pid not in ids:
                errs.append(f"days[{day}].picks: unknown news id {pid!r}")
        if o.get("job") and o["job"] not in slugs:
            errs.append(f"days[{day}].job: unknown use case {o['job']!r}")
        if len(o.get("picks", [])) > 3:
            errs.append(f"days[{day}].picks: at most 3")
    return errs


def d(s):
    return datetime.date.fromisoformat(s[:10])


def edition_date_for(day):
    """The weekday edition a calendar day belongs to: weekdays are their own edition; Sat/Sun roll forward to Monday."""
    while day.weekday() > 4:
        day += datetime.timedelta(days=1)
    return day


def latest_edition(today):
    """The edition shown on a given build day: today on weekdays, Friday on weekends."""
    while today.weekday() > 4:
        today -= datetime.timedelta(days=1)
    return today


def prev_edition(day):
    day -= datetime.timedelta(days=1)
    while day.weekday() > 4:
        day -= datetime.timedelta(days=1)
    return day


def edition_number(day, first_edition):
    """1-based count of weekday editions since first_edition (a weekday). None before it, or when numbering is off."""
    if not first_edition:
        return None
    start = d(first_edition)
    if day < start:
        return None
    n, cur = 0, start
    while cur <= day:
        if cur.weekday() <= 4:
            n += 1
        cur += datetime.timedelta(days=1)
    return n


def edition_dates(news, today, limit=20, first_edition=None, days=None):
    """Weekday editions, newest first, up to `today`'s edition (weekends use Friday).

    The current weekday always gets an edition, even when no news is dated that day
    (pick_three fills in from earlier items; those items keep their own dates). Past
    editions are weekdays that have news, or a days[] override. Quiet weekdays before
    today are not created retroactively, unless first_edition is set, in which case
    every weekday from first_edition through today is included.
    """
    top = latest_edition(today)
    seen = {top}
    for n in news:
        nd = d(n["date"])
        if nd <= today:
            ed = edition_date_for(nd)
            if ed <= top:
                seen.add(ed)
    for key in (days or {}):
        try:
            nd = datetime.date.fromisoformat(key)
        except ValueError:
            continue
        if nd <= today and nd.weekday() <= 4:
            ed = edition_date_for(nd)
            if ed <= top:
                seen.add(ed)
    if first_edition:
        start = d(first_edition) if isinstance(first_edition, str) else first_edition
        cur = start
        while cur <= top:
            if cur.weekday() <= 4:
                seen.add(cur)
            cur += datetime.timedelta(days=1)
    return sorted(seen, reverse=True)[:limit]


def _assistant_hits(n, checkup):
    if not checkup:
        return []
    h = n.get("headline", "")
    return [a["id"] for a in checkup.get("assistants", []) if a.get("news_pattern") and re.search(a["news_pattern"], h)]


def rank_key(n, checkup=None):
    x = n.get("x") or {}
    return (IMPACT_RANK.get(n.get("impact"), 1), 0 if _assistant_hits(n, checkup) else 1, -(x.get("views") or 0), n["id"])


def items_for(news, ed):
    """News items that belong to edition `ed`: that weekday, plus the weekend before it when ed is a Monday."""
    return [n for n in news if edition_date_for(d(n["date"])) == ed]


def pick_three(news, ed, overrides=None, checkup=None):
    """(top3, also) for edition `ed`. top3 entries are news dicts; items dated before `ed` are fill-ins and keep their date."""
    overrides = overrides or {}
    by_id = {n["id"]: n for n in news}
    own = sorted(items_for(news, ed), key=lambda n: rank_key(n, checkup))
    chosen = [by_id[i] for i in overrides.get("picks", []) if i in by_id]
    for n in own:
        if len(chosen) >= 3:
            break
        if n not in chosen:
            chosen.append(n)
    if len(chosen) < 3:  # quiet day: fill with the newest earlier items, most important first within a day
        older = sorted([n for n in news if d(n["date"]) < ed and n not in chosen and edition_date_for(d(n["date"])) != ed],
                       key=lambda n: (-d(n["date"]).toordinal(), rank_key(n, checkup)))
        chosen += older[: 3 - len(chosen)]
    also = [n for n in own if n not in chosen]
    return chosen[:3], also


def _rotation(ucs):
    easy = [x for x in ucs if x.get("difficulty") == "Easy" and x.get("prompt")]
    return sorted(easy, key=lambda x: hashlib.sha1(x["slug"].encode()).hexdigest())  # stable, mixes categories


def pick_job(ucs, ed, overrides=None):
    """Job of the day for edition `ed`: override > a use case added the previous weekday (easiest first) > fixed rotation.
    Using the previous weekday's additions keeps the job stable all day: the midday routine's new use cases become
    tomorrow's job instead of swapping today's in the afternoon."""
    overrides = overrides or {}
    by_slug = {x["slug"]: x for x in ucs}
    if overrides.get("job") in by_slug:
        return by_slug[overrides["job"]], "picked"
    prev = prev_edition(ed)
    fresh = [x for x in ucs if x.get("prompt") and edition_date_for(d(x["date_added"])) == prev]
    if fresh:
        fresh.sort(key=lambda x: (DIFF_RANK.get(x.get("difficulty"), 1), x["date_added"], x["slug"]))
        return fresh[0], "new"
    rot = _rotation(ucs)
    if not rot:
        return None, ""
    return rot[ed.toordinal() % len(rot)], "rotation"


def apps_for(n):
    a = APP_BY_COMPANY.get(n.get("company", ""))
    return [a] if a else []
