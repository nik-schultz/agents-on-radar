#!/usr/bin/env python3
"""Tests for BotsDoThat Today (/today/ daily edition, /today/archive/, feed, the home overview + Today box, /guides/, nav and streak).
  python3 scripts/build.py && python3 scripts/test_today.py
Unit tests use small fixtures. Page tests read the built site/. Browser tests use Playwright (skip when missing)."""
import datetime, json, os, re, sys, threading, unittest, warnings, xml.dom.minidom
warnings.simplefilter("ignore", ResourceWarning)
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import today as T

D = datetime.date
def item(i, date, impact="notable", company="OpenAI", headline=None, views=0):
    n = {"id": i, "date": date, "impact": impact, "company": company, "category": "feature", "headline": headline or i,
         "explainer": "x.", "source_url": "https://example.com/" + i, "source_name": "Ex"}
    if views: n["x"] = {"views": views}
    return n
def uc(slug, added, diff="Easy"):
    return {"slug": slug, "date_added": added, "difficulty": diff, "prompt": "p", "title": slug}
CK = {"assistants": [{"id": "grok", "news_pattern": "Grok Bot"}]}

def built(path):
    fp = os.path.join(SITE, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(SITE, path.lstrip("/"))
    with open(fp, encoding="utf-8") as fh: return fh.read()


class EditionDates(unittest.TestCase):
    def test_weekend_rolls_forward_and_latest_rolls_back(self):
        self.assertEqual(T.edition_date_for(D(2026, 11, 21)), D(2026, 11, 23))  # Sat -> Mon
        self.assertEqual(T.edition_date_for(D(2026, 11, 19)), D(2026, 11, 19))
        self.assertEqual(T.latest_edition(D(2026, 11, 22)), D(2026, 11, 20))     # Sun -> Fri
        self.assertEqual(T.prev_edition(D(2026, 11, 23)), D(2026, 11, 20))       # Mon -> Fri

    def test_numbering_is_off_until_launch_and_counts_weekdays(self):
        self.assertIsNone(T.edition_number(D(2026, 11, 19), None))
        self.assertIsNone(T.edition_number(D(2026, 11, 19), "2026-11-20"))
        self.assertEqual(T.edition_number(D(2026, 11, 20), "2026-11-20"), 1)
        self.assertEqual(T.edition_number(D(2026, 11, 23), "2026-11-20"), 2)    # weekend skipped
        self.assertEqual(T.edition_number(D(2026, 11, 27), "2026-11-20"), 6)

    def test_edition_list_includes_today_skips_future_and_past_quiet_days(self):
        news = [item("a", "2026-11-19"), item("b", "2026-11-21"), item("c", "2026-11-17")]
        # Fri Nov 20 has no items but is still today's edition; Sat Nov 21 rolls to Mon Nov 23 (future);
        # Wed Nov 18 has no items and is not invented after the fact.
        self.assertEqual(T.edition_dates(news, D(2026, 11, 20)), [D(2026, 11, 20), D(2026, 11, 19), D(2026, 11, 17)])

    def test_quiet_weekday_still_gets_an_edition_filled_from_earlier_items(self):
        news = [item("tue", "2026-11-24", "major"), item("mon", "2026-11-23"), item("fri", "2026-11-20")]
        eds = T.edition_dates(news, D(2026, 11, 25))  # Wed, no items dated today
        self.assertEqual(eds[0], D(2026, 11, 25))
        self.assertEqual(eds[1:], [D(2026, 11, 24), D(2026, 11, 23), D(2026, 11, 20)])
        top, also = T.pick_three(news, D(2026, 11, 25))
        self.assertEqual([n["id"] for n in top], ["tue", "mon", "fri"])
        self.assertEqual([n["date"] for n in top], ["2026-11-24", "2026-11-23", "2026-11-20"])
        self.assertEqual(also, [])

    def test_weekend_uses_friday_even_when_friday_had_no_items(self):
        news = [item("thu", "2026-11-19")]
        self.assertEqual(T.edition_dates(news, D(2026, 11, 21))[0], D(2026, 11, 20))  # Sat -> Fri
        self.assertEqual(T.edition_dates(news, D(2026, 11, 22))[0], D(2026, 11, 20))  # Sun -> Fri
        top, _ = T.pick_three(news, D(2026, 11, 20))
        self.assertEqual(top[0]["id"], "thu")
        self.assertEqual(top[0]["date"], "2026-11-19")

    def test_override_day_is_kept_even_without_news(self):
        news = [item("a", "2026-11-17")]
        eds = T.edition_dates(news, D(2026, 11, 20), days={"2026-11-19": {"picks": ["a"]}})
        self.assertEqual(eds, [D(2026, 11, 20), D(2026, 11, 19), D(2026, 11, 17)])

    def test_first_edition_fills_quiet_weekdays_from_launch(self):
        news = [item("a", "2026-11-20")]
        eds = T.edition_dates(news, D(2026, 11, 25), first_edition="2026-11-20")
        self.assertEqual(eds, [D(2026, 11, 25), D(2026, 11, 24), D(2026, 11, 23), D(2026, 11, 20)])


class Picks(unittest.TestCase):
    def test_importance_then_assistant_then_views(self):
        news = [item("minor", "2026-11-19", "minor", views=99999), item("plain", "2026-11-19", views=50),
                item("grok", "2026-11-19", headline="Grok Bot can book flights"), item("major", "2026-11-19", "major")]
        top, also = T.pick_three(news, D(2026, 11, 19), {}, CK)
        self.assertEqual([n["id"] for n in top], ["major", "grok", "plain"])
        self.assertEqual([n["id"] for n in also], ["minor"])

    def test_override_order_wins(self):
        news = [item("a", "2026-11-19", "major"), item("b", "2026-11-19"), item("c", "2026-11-19")]
        top, _ = T.pick_three(news, D(2026, 11, 19), {"picks": ["c"]})
        self.assertEqual(top[0]["id"], "c")

    def test_quiet_day_fills_from_newest_older_items(self):
        news = [item("today", "2026-11-19"), item("old", "2026-11-10"), item("yday", "2026-11-18")]
        top, also = T.pick_three(news, D(2026, 11, 19))
        self.assertEqual([n["id"] for n in top], ["today", "yday", "old"])
        self.assertEqual(also, [])

    def test_monday_includes_weekend_items(self):
        news = [item("sat", "2026-11-21"), item("mon", "2026-11-23")]
        top, _ = T.pick_three(news, D(2026, 11, 23))
        self.assertEqual({n["id"] for n in top[:2]}, {"sat", "mon"})

    def test_job_override_then_fresh_then_stable_rotation(self):
        # added Wed 11-18 -> Thursday's job; added Thu 11-19 (midday) must NOT change Thursday's job
        ucs = [uc("hard-new", "2026-11-18", "Advanced"), uc("easy-new", "2026-11-18"), uc("old1", "2026-10-01"), uc("old2", "2026-10-02"), uc("midday", "2026-11-19")]
        self.assertEqual(T.pick_job(ucs, D(2026, 11, 19), {"job": "old2"})[0]["slug"], "old2")
        self.assertEqual(T.pick_job(ucs, D(2026, 11, 19)), (ucs[1], "new"))
        self.assertEqual(T.pick_job(ucs, D(2026, 11, 20)), (ucs[4], "new"))  # Thursday's midday add is Friday's job
        a = T.pick_job(ucs, D(2026, 11, 12)); b = T.pick_job(ucs, D(2026, 11, 12))
        self.assertEqual(a, b); self.assertEqual(a[1], "rotation")

    def test_validator_catches_bad_overrides(self):
        errs = T.validate({"first_edition": "2026-11-21", "days": {"2026-11-19": {"picks": ["nope"], "job": "nope"}, "bad": {}}},
                          [item("a", "2026-11-19")], [uc("x", "2026-11-19")])
        self.assertEqual(len(errs), 4, errs)

    def test_real_data_validates(self):
        news = json.load(open(os.path.join(ROOT, "data", "news.json")))["items"]
        ucs = json.load(open(os.path.join(ROOT, "data", "use-cases.json")))
        self.assertEqual(T.validate(T.load(ROOT), news, ucs), [])


@unittest.skipUnless(os.path.exists(os.path.join(SITE, "index.html")), "run scripts/build.py first")
class Pages(unittest.TestCase):
    def test_today_url_is_the_daily_page(self):
        h = built("/today/")
        self.assertIn('data-page="today"', h)
        self.assertRegex(h, r'<h1 class="td-date">[A-Z][a-z]+day, [A-Z][a-z]{2} \d{1,2}</h1>')  # the routines check this heading
        self.assertIn("3 things that changed", h)
        self.assertEqual(h.count('class="td-item glass"'), 3)
        self.assertIn("Job of the day", h)
        self.assertIn('id="job-prompt"', h)
        self.assertIn('data-mark="tried"', h)
        self.assertIn('data-mark="read"', h)
        self.assertIn("What it means for you:", h)
        self.assertEqual(len(re.findall(r'<li class="td-item[^"]*"[^>]*>.*?Source: <a href="https?://', h, re.S)), 3)  # every item is sourced
        self.assertNotIn("radar-stage", h)  # old hero is gone

    def test_home_is_a_short_overview_with_a_today_box(self):
        h = built("/")
        self.assertIn('data-page="home"', h)
        self.assertNotIn('class="td-item glass"', h)  # the full edition is not on the home page
        box = re.search(r'<a class="hb-today" href="/today/"[^>]*data-edition="(\d{4}-\d{2}-\d{2})">(.*?)</a></section>', h, re.S)
        self.assertTrue(box, "Today box linking to /today/ near the top")
        self.assertLess(h.index('class="hb-today"'), h.index('class="hf-grid"'))
        t = built("/today/")
        ed = re.search(r'<div class="td" data-edition="([\d-]+)" data-job="([^"]*)"', t)
        self.assertEqual(box.group(1), ed.group(1))  # same edition as /today/
        top1 = re.search(r'<h3 class="td-h">(.*?)</h3>', t).group(1)
        self.assertIn(top1, box.group(2))  # teaser = the #1 change on /today/
        job_title = re.search(r'<h2 id="job-h"><a [^>]*>(.*?)</a></h2>', t).group(1)
        self.assertIn(job_title, box.group(2))  # same job of the day
        self.assertIn(re.search(r'<h1 class="td-date">(.*?)</h1>', t).group(1), box.group(2))
        for p in ("/bot-checkup/", "/use-cases/", "/news/", "/guides/", "/bot-instructions/", "/ai-pricing/"):
            self.assertIn(f'<a href="{p}">', re.search(r'class="hf-grid">(.*?)</ul>', h, re.S).group(1), p)
        main = re.search(r'<main id="main">(.*?)</main>', h, re.S).group(1)
        self.assertEqual(main.count('class="nl-form"'), 1)  # one signup form
        self.assertIn('href="/advertise/"', h.split('<footer', 1)[1])  # advertise stays in the footer
        self.assertNotIn('/advertise/', main)
        n_ucs = len(json.load(open(os.path.join(ROOT, "data", "use-cases.json"))))
        self.assertIn(f"{n_ucs} jobs", h)  # counts come from the data, never typed in

    def test_news_header_is_compact(self):
        h = built("/news/")
        head = re.search(r'<div class="wrap page-head news-head">(.*?)<div class="wrap news-wrap">', h, re.S).group(1)
        self.assertNotIn("td-band", head)  # old "Short on time?" box is gone
        info = re.search(r'<details class="ni" id="news-info"><summary class="ni-btn">About this page.*?</details>', head, re.S)
        self.assertTrue(info, "no-JS fallback: a <details> holds the page info")
        outside = head.replace(info.group(0), "")
        for moved in ("New to AI agents?", "How we measure", "with measured X numbers", "/news/feed.xml"):
            self.assertIn(moved, info.group(0), moved)
            self.assertNotIn(moved, outside, moved)
        news = json.load(open(os.path.join(ROOT, "data", "news.json")))["items"]
        self.assertIn(f"{len(news)} stories", info.group(0))  # counts come from the data
        self.assertIn(f"{sum(1 for n in news if n.get('x'))} with measured X numbers", info.group(0))
        pill = re.search(r'<p class="nh-pill" id="news-pill">(.*?)</p>', outside, re.S).group(1)
        self.assertIn('href="/today/"', pill); self.assertIn('href="/bot-checkup/"', pill); self.assertIn('class="nh-x"', pill)
        self.assertLess(outside.index("news-pill"), outside.index("news-chips"))

    def test_live_check_script_reads_the_build(self):
        import check_today
        ed = datetime.date.fromisoformat(re.search(r'<div class="td" data-edition="([\d-]+)"', built("/today/")).group(1))
        self.assertEqual(check_today.check(SITE, ed, local=True), [])
        self.assertEqual(len(check_today.check(SITE, ed - datetime.timedelta(days=7), local=True)), 3)

    def test_built_today_is_the_current_weekday_edition(self):
        cfg = json.load(open(os.path.join(ROOT, "config.json")))
        build_day = datetime.date.fromisoformat(cfg.get("as_of") or datetime.date.today().isoformat())
        want = T.latest_edition(build_day)
        h = built("/today/")
        self.assertIn(f'data-edition="{want.isoformat()}"', h)
        self.assertIn(f'<h1 class="td-date">{want.strftime("%A, %b %-d")}</h1>', h)
        self.assertNotIn("isn't in yet", h)
        self.assertTrue(os.path.isdir(os.path.join(SITE, "today", want.isoformat())))
        box = built("/")
        self.assertIn(f'data-edition="{want.isoformat()}"', box)
        news_dates = {n["date"][:10] for n in json.load(open(os.path.join(ROOT, "data", "news.json")))["items"]}
        if want.isoformat() not in news_dates:  # quiet day: fill-ins keep their own date labels
            self.assertIn("td-older", h)

    def test_nav_is_five_items_in_order(self):
        h = built("/news/")
        nav = re.search(r'<nav aria-label="Main" class="menu" id="site-menu">(.*?)</nav>', h, re.S).group(1)
        self.assertEqual(re.findall(r">([^<]+)</a>", nav), ["Today", "Jobs to try", "Bot Checkup", "AI news", "Guides"])
        self.assertIn('href="/today/" aria-current=page', built("/today/"))
        self.assertIn('href="/today/" aria-current=page', built("/today/archive/"))
        self.assertNotIn("aria-current=page", re.search(r'<nav aria-label="Main".*?</nav>', built("/"), re.S).group(0))

    def test_archive_pages_feed_and_canonical(self):
        arch = built("/today/archive/")
        dates = re.findall(r'href="/today/(\d{4}-\d{2}-\d{2})/"', arch)
        self.assertGreaterEqual(len(dates), 5)
        latest = built(f"/today/{dates[0]}/")
        self.assertIn('<link rel="canonical" href="https://botsdothat.com/today/">', latest)  # no duplicate of /today/
        self.assertIn('<link rel="canonical" href="https://botsdothat.com/today/">', built("/today/"))
        older = built(f"/today/{dates[1]}/")
        self.assertIn(f'<link rel="canonical" href="https://botsdothat.com/today/{dates[1]}/">', older)
        self.assertIn("Go to today", older)
        sm = open(os.path.join(SITE, "sitemap.xml")).read()
        self.assertNotIn(f"/today/{dates[0]}/", sm)
        self.assertIn(f"/today/{dates[1]}/", sm)
        feed = open(os.path.join(SITE, "today", "feed.xml"), encoding="utf-8").read()
        xml.dom.minidom.parseString(feed.encode("utf-8"))
        self.assertGreaterEqual(feed.count("<item>"), 5)
        self.assertIn("<link>https://botsdothat.com/today/</link>", feed)
        self.assertIn("https://botsdothat.com/today/</loc>", sm)
        self.assertIn("https://botsdothat.com/today/archive/</loc>", sm)

    def test_guides_hub_links_every_guide(self):
        g = built("/guides/")
        for p in ("/what-can-bots-do/", "/bot-checkup/", "/chatgpt-dots-vs-grok-bot-vs-meta-muse/", "/ai-pricing/", "/run-your-bots-for-less/", "/blueprints/", "/trending/", "/bot-instructions/"):
            self.assertIn(f'href="{p}"', g, p)

    def test_every_old_url_still_exists(self):
        missing = []
        lines = []
        for f in ("urls-before-overhaul.txt", "urls-before-home-overview.txt"):
            lines += open(os.path.join(ROOT, "scripts", "fixtures", f)).read().split()
        for line in lines:
            p = line.strip()
            if not p: continue
            fp = os.path.join(SITE, p.lstrip("/"), "index.html") if p.endswith("/") else os.path.join(SITE, p.lstrip("/"))
            if not os.path.exists(fp): missing.append(p)
        self.assertEqual(missing, [])

    def test_use_case_pages_offer_tried_it(self):
        any_uc = sorted(os.listdir(os.path.join(SITE, "use-cases")))
        any_uc = [x for x in any_uc if os.path.isdir(os.path.join(SITE, "use-cases", x))][0]
        h = built(f"/use-cases/{any_uc}/")
        self.assertIn(f'data-mark="tried" data-slug="{any_uc}"', h)
        self.assertIn("/assets/today.js", h)

    def test_no_network_calls_in_today_js(self):
        js = open(os.path.join(ROOT, "static", "today.js")).read()
        for bad in ("fetch(", "XMLHttpRequest", "sendBeacon", "document.cookie"):
            self.assertNotIn(bad, js)


class _Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

@unittest.skipUnless(os.path.exists(os.path.join(SITE, "index.html")), "run scripts/build.py first")
class Browser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise unittest.SkipTest("playwright not installed")
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), partial(_Quiet, directory=SITE))
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_address[1]}"
        cls.pw = sync_playwright().start()
        try: cls.b = cls.pw.chromium.launch()
        except Exception: cls.b = cls.pw.chromium.launch(channel="chrome")

    @classmethod
    def tearDownClass(cls):
        cls.b.close(); cls.pw.stop(); cls.srv.shutdown()

    def _page(self, now="2026-11-19T09:00:00"):
        ctx = self.b.new_context()
        ctx.add_init_script(f"window.BDT_NOW = '{now}';")
        ctx.set_default_timeout(60000)  # the shared box is sometimes slow to start Chrome
        return ctx, ctx.new_page()

    def test_streak_counts_weekdays_and_survives_weekends(self):
        ctx, pg = self._page("2026-11-23T09:00:00")  # a Monday
        pg.goto(self.base + "/today/")
        self.assertEqual(pg.inner_text("#streak-lbl"), "Start a streak")
        # seed Thu + Fri done; the weekend in between must not break it
        pg.evaluate("localStorage.setItem('bdt-days', JSON.stringify({'2026-11-19':['read'],'2026-11-20':['read']}))")
        pg.reload()
        self.assertEqual(pg.inner_text("#streak-n"), "2")  # today not done yet: streak still alive
        pg.click("[data-mark=read]")
        self.assertEqual(pg.inner_text("#streak-n"), "3")
        self.assertEqual(pg.get_attribute("[data-mark=read]", "aria-pressed"), "true")
        self.assertTrue(pg.is_visible("#streak-share"))
        pg.reload()
        self.assertEqual(pg.inner_text("#streak-n"), "3")  # persisted in this browser
        ctx.close()

    def test_tried_on_a_use_case_page_counts_on_today(self):
        ctx, pg = self._page()
        pg.goto(self.base + "/today/")
        slug = pg.get_attribute(".td", "data-job")
        pg.goto(self.base + f"/use-cases/{slug}/")
        pg.click("[data-mark=tried]")
        pg.goto(self.base + "/today/")
        self.assertEqual(pg.inner_text("#streak-n"), "1")
        self.assertEqual(pg.get_attribute(".td-job [data-mark=tried]", "aria-pressed"), "true")
        ctx.close()

    def test_app_picker_flags_matching_items(self):
        ctx, pg = self._page()
        pg.goto(self.base + "/today/")
        apps = pg.eval_on_selector_all(".td-item", "els => els.map(e => e.dataset.apps).filter(Boolean)")
        self.assertTrue(apps, "expected at least one item about a known app")
        app = apps[0].split()[0]
        pg.click("summary")
        pg.click(f"[data-app={app}]")
        self.assertGreaterEqual(pg.locator(".td-item.is-yours").count(), 1)
        self.assertIn("affect apps you use", pg.inner_text("#you-count"))
        pg.reload()
        self.assertGreaterEqual(pg.locator(".td-item.is-yours").count(), 1)
        ctx.close()

    def test_home_box_shows_streak_and_opens_today(self):
        ctx, pg = self._page("2026-11-20T09:00:00")
        pg.goto(self.base + "/")
        self.assertFalse(pg.is_visible(".hb-streak"))  # nothing until you start
        pg.evaluate("localStorage.setItem('bdt-days', JSON.stringify({'2026-11-18':['read'],'2026-11-19':['read']}))")
        pg.reload()
        self.assertIn("2-day streak", pg.inner_text(".hb-streak"))
        pg.click(".hb-today")
        pg.wait_for_url("**/today/")
        self.assertTrue(pg.is_visible("h1.td-date"))
        ctx.close()

    def test_home_is_short_on_mobile(self):
        ctx = self.b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
        pg = ctx.new_page()
        pg.goto(self.base + "/")
        box_top = pg.evaluate("document.querySelector('.hb-today').getBoundingClientRect().top")
        self.assertLess(box_top, 844)  # the Today box is on the first phone screen
        main_h = pg.evaluate("document.getElementById('main').scrollHeight")
        pg.goto(self.base + "/today/")
        self.assertLess(main_h, pg.evaluate("document.getElementById('main').scrollHeight"))
        ctx.close()

    def test_news_popover_and_pill(self):
        ctx = self.b.new_context(viewport={"width": 1280, "height": 800}); ctx.set_default_timeout(60000)
        pg = ctx.new_page()
        pg.goto(self.base + "/news/")
        btn = "button.ni-btn"
        self.assertEqual(pg.get_attribute(btn, "aria-expanded"), "false")
        self.assertEqual(pg.get_attribute(btn, "aria-controls"), "ni-panel")
        self.assertFalse(pg.is_visible("#ni-panel"))
        pg.click(btn)
        self.assertTrue(pg.is_visible("#ni-panel")); self.assertEqual(pg.get_attribute(btn, "aria-expanded"), "true")
        pg.keyboard.press("Escape")
        self.assertFalse(pg.is_visible("#ni-panel")); self.assertEqual(pg.get_attribute(btn, "aria-expanded"), "false")
        pg.click(btn); pg.mouse.click(20, 780)  # click outside
        self.assertFalse(pg.is_visible("#ni-panel"))
        # chips and the top story / trending cards are on the first screen
        for sel in (".news-chips", ".nb--top .nt--xl", ".nb--top .nb-side .nt"):
            self.assertLess(pg.evaluate(f"document.querySelector('{sel}').getBoundingClientRect().top"), 800, sel)
        pg.click("#news-pill .nh-x")
        self.assertFalse(pg.is_visible("#news-pill"))
        pg.reload()
        self.assertFalse(pg.is_visible("#news-pill"))  # remembered in this browser
        ctx.close()

    def test_news_works_without_js(self):
        ctx = self.b.new_context(java_script_enabled=False); ctx.set_default_timeout(60000)
        pg = ctx.new_page()
        pg.goto(self.base + "/news/")
        self.assertFalse(pg.is_visible("#ni-panel"))
        pg.click("summary.ni-btn")
        self.assertTrue(pg.is_visible("#ni-panel"))
        self.assertFalse(pg.is_visible("#news-pill .nh-x"))  # no dead dismiss button without JS
        ctx.close()

    def test_mobile_has_no_horizontal_scroll(self):
        ctx = self.b.new_context(viewport={"width": 360, "height": 740}, is_mobile=True)
        pg = ctx.new_page()
        for p in ("/", "/today/", "/today/archive/", "/guides/", "/news/"):
            pg.goto(self.base + p)
            self.assertLessEqual(pg.evaluate("document.documentElement.scrollWidth"), 361, p)
        ctx.close()


if __name__ == "__main__":
    unittest.main(verbosity=1)
