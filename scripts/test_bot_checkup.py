#!/usr/bin/env python3
"""Tests for Bot Checkup: settings data honesty, house-rules Python/JS parity, news matching and the built page.
Run python3 scripts/build.py first for the page tests (they skip if site/ is missing)."""
import datetime, json, os, re, shutil, subprocess, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bot_checkup as ck

D = ck.load()
with open(os.path.join(ROOT, "config.json"), encoding="utf-8") as _fh:
    CFG = json.load(_fh)
PAGE = os.path.join(ROOT, "site", "bot-checkup", "index.html")
JS = os.path.join(ROOT, "static", "bot-checkup.js")


def built(path):
    fp = os.path.join(ROOT, "site", path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "site", "index.html")
    if not os.path.exists(fp):
        raise unittest.SkipTest("site not built")
    with open(fp, encoding="utf-8") as fh:
        return fh.read()


class DataTests(unittest.TestCase):
    def test_data_validates(self):
        self.assertEqual(ck.validate(D), [])

    def test_five_assistants_in_order(self):
        self.assertEqual([a["name"] for a in D["assistants"]], ["Grok Bot", "ChatGPT dots", "Claude Duet", "Meta Muse", "Gemini Tasks"])

    def test_every_source_is_an_official_vendor_page(self):
        for k, s in D["sources"].items():
            host = re.match(r"https://([^/]+)/", s["url"]).group(1)
            self.assertIn(host, ck.VENDOR_HOSTS, k)

    def test_every_fix_has_a_path_or_says_it_is_unverified(self):
        n_paths = n_unverified = 0
        for a in D["assistants"]:
            for f in a["fixes"]:
                self.assertTrue(bool(f.get("path")) != bool(f.get("unverified")), f["id"])
                self.assertIn(f["source"], D["sources"])
                n_paths += bool(f.get("path")); n_unverified += bool(f.get("unverified"))
        self.assertGreater(n_paths, 15)
        self.assertGreater(n_unverified, 0)  # we say so where a vendor doesn't document steps

    def test_validator_catches_a_made_up_path_source(self):
        bad = json.loads(json.dumps(D))
        bad["assistants"][0]["fixes"][0]["source"] = "nope"
        bad["sources"]["blog"] = {"label": "x", "url": "https://example.com/post"}
        bad["assistants"][1]["fixes"][0].pop("path")
        errs = ck.validate(bad)
        self.assertTrue(any("unknown source nope" in x for x in errs))
        self.assertTrue(any("not an official vendor URL" in x for x in errs))
        self.assertTrue(any("no path and no 'unverified'" in x for x in errs))

    def test_no_mockup_placeholders_or_grades(self):
        blob = json.dumps({k: v for k, v in D.items() if k != "_help"}).lower()
        for w in ("fictional", "placeholder", "lorem", "score", "grade", "100% safe"):
            self.assertNotIn(w, blob)


class RulesTests(unittest.TestCase):
    CASES = [({}, False, ""), ({}, True, ""), ({"send": "fine", "buy": "never"}, False, ""), ({"delete": "never"}, True, "my son Alex"),
             ({a["id"]: "fine" for a in D["actions"]}, False, ""), ({a["id"]: "never" for a in D["actions"]}, True, "  ")]

    def test_defaults_ask_first_and_parent_mode_is_stricter(self):
        normal, parent = ck.house_rules(D), ck.house_rules(D, parent=True)
        self.assertNotIn("Never do these", normal)
        self.assertIn("Never do these", parent)
        self.assertIn("Scam protection", parent)
        self.assertNotIn("Scam protection", normal)
        self.assertIn("gift cards", parent)

    def test_helper_name_is_used(self):
        self.assertIn("Tell me and my son Alex first.", ck.house_rules(D, parent=True, helper="my son Alex"))
        self.assertIn("[name of someone I trust]", ck.house_rules(D, parent=True, helper=" "))

    def test_python_and_js_rules_match(self):
        if not shutil.which("node"):
            self.skipTest("node not installed")
        script = ("require(process.argv[1]); const d=JSON.parse(process.argv[2]); const cases=JSON.parse(process.argv[3]);"
                  "console.log(JSON.stringify(cases.map(c=>globalThis.BotCheckup.houseRules(d.actions,c[0],c[1],c[2]))));")
        out = subprocess.check_output(["node", "-e", script, JS, json.dumps(D), json.dumps(self.CASES)], text=True)
        js = json.loads(out)
        for (ans, parent, helper), got in zip(self.CASES, js):
            self.assertEqual(got, ck.house_rules(D, ans, parent, helper))

    def test_script_makes_no_network_calls_and_stores_nothing(self):
        with open(JS, encoding="utf-8") as fh:
            src = fh.read()
        for w in ("fetch(", "XMLHttpRequest", "localStorage", "sessionStorage", "sendBeacon", "document.cookie"):
            self.assertNotIn(w, src)


class NewsTests(unittest.TestCase):
    def test_match_news_window_categories_and_headline_match(self):
        items = [
            {"date": "2026-11-18", "category": "feature", "headline": "Grok Bot adds per-tool permissions", "explainer": "Set send email to Needs approval.", "source_url": "https://x.ai/changelog/bot", "source_name": "xAI"},
            {"date": "2026-11-18", "category": "model release", "headline": "Muse Wonder 2 model", "explainer": "", "source_url": "https://about.fb.com/"},
            {"date": "2026-08-01", "category": "feature", "headline": "Old Grok Bot thing", "explainer": "", "source_url": "https://x.ai/"},
            {"date": "2026-11-17", "category": "feature", "headline": "Spotify DJ gets voices", "explainer": "dots", "source_url": "https://spotify.com/"},
            {"date": "2026-11-13", "category": "feature", "headline": "ChatGPT Wallet lets your dot buy things", "explainer": "approve each purchase", "source_url": "https://openai.com/"},
            {"date": "2026-11-12", "category": "feature", "headline": "No source Gemini task", "explainer": "", "source_url": ""},
        ]
        got = ck.match_news(items, D, datetime.date(2026, 11, 19))
        self.assertEqual([g["headline"] for g in got], ["Grok Bot adds per-tool permissions", "ChatGPT Wallet lets your dot buy things"])
        self.assertEqual(got[0]["assistants"], ["grok"])
        self.assertIn("email", got[0]["connections"])
        self.assertIn("payments", got[1]["connections"])


class PageTests(unittest.TestCase):
    def test_page_has_flow_sources_and_honest_watch_pricing(self):
        h = built("/bot-checkup/")
        for name in ("Grok Bot", "ChatGPT dots", "Claude Duet", "Meta Muse", "Gemini Tasks"):
            self.assertIn(name, h)
        for s in D["sources"].values():
            self.assertIn(f'href="{s["url"]}"', h)
        for w in ("Fictional", "Paths are placeholders", "MOCKUP", "Tested handoffs"):
            self.assertNotIn(w, h)
        self.assertIn('id="ck-parent"', h)
        self.assertIn("Exact steps not documented.", h)
        self.assertIn("$5<small>/month</small>", h)
        self.assertIn("$9<small>/month</small>", h)
        self.assertGreaterEqual(h.count("Coming soon · no charge today"), 3)
        self.assertIn('/assets/bot-checkup.js', h)
        self.assertIn('href="/bot-instructions/"', h)

    def test_interest_list_uses_the_free_kit_form_and_no_checkout(self):
        h = built("/bot-checkup/")
        self.assertFalse(CFG["checkup_watch"]["charging"])
        self.assertIn("forms/10088120/subscriptions", CFG["newsletter"]["form_action"])
        form = h[h.index('class="nl-form ck-int-form"'):]
        form = form[:form.index("</form>")]
        self.assertIn('action="https://app.kit.com/forms/10088120/subscriptions"', form)
        self.assertIn(f'name="fields[{CFG["checkup_watch"]["plan_field"]}]" value="watch"', form)
        self.assertIn('value="household"', form)
        self.assertIn('name="email_address"', form)
        self.assertIn("data-nl", form)
        for w in ("buy.stripe.com", "checkout.stripe.com", "accounts.js", "supabase", "card number"):
            self.assertNotIn(w, h.lower() if w == "card number" else h)
        self.assertFalse(CFG["saved_setups"]["sign_in"])
        self.assertFalse(CFG["saved_setups"]["billing"])

    def test_bot_checkup_is_the_top_action_and_builder_links_up(self):
        for path in ("/", "/news/", "/bot-instructions/", "/how-to-use-tasks-in-gemini/"):
            h = built(path)
            self.assertIn('class="btn btn-sm nav-build" href="/bot-checkup/"', h, path)
            self.assertIn('href="/bot-checkup/">Bot Checkup</a>', h, path)
        bi = built("/bot-instructions/")
        self.assertIn('class="ck-upsell', bi)
        self.assertIn('id="bb-form"' if 'id="bb-form"' in bi else "bot-builder.js", bi)  # builder still renders
        self.assertIn(">Start the free Bot Checkup</a>", built("/"))


class BrowserTests(unittest.TestCase):
    """Drives the built page in headless Chrome (skips when Playwright or the build is missing)."""
    def test_flow_filters_results_and_parent_mode_changes_rules(self):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            self.skipTest("playwright not installed")
        if not os.path.exists(PAGE):
            self.skipTest("site not built")
        import http.server, threading, functools
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(http.server.SimpleHTTPRequestHandler, directory=os.path.join(ROOT, "site")))
        srv.RequestHandlerClass.log_message = lambda *a: None
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        try:
            with sync_playwright() as p:
                try:
                    b = p.chromium.launch()
                except Exception as ex:  # no bundled browser
                    try:
                        b = p.chromium.launch(channel="chrome")
                    except Exception:
                        self.skipTest(f"no browser: {ex}")
                pg = b.new_page()
                requests = []
                pg.on("request", lambda r: requests.append(r.url))
                pg.goto(f"http://127.0.0.1:{srv.server_port}/bot-checkup/")
                pg.wait_for_function("document.getElementById('ck-count').textContent.indexOf('Pick') === 0")
                self.assertEqual(pg.locator(".ck-assistant:visible").count(), 5)
                pg.click("label.ck-chip:has(input[value=muse])")
                self.assertEqual(pg.locator(".ck-assistant:visible").count(), 1)
                self.assertIn("Meta Muse", pg.locator(".ck-assistant:visible h3").inner_text())
                before = pg.locator(".ck-fix:visible").count()
                pg.click("label.ck-chip:has(input[value=browser])")
                self.assertGreater(pg.locator(".ck-fix:visible").count(), before)
                self.assertTrue(pg.locator(".ck-tab[data-tab=muse]").is_visible())
                self.assertFalse(pg.locator(".ck-tab[data-tab=grok]").is_visible())
                self.assertNotIn("Scam protection", pg.input_value("#ck-rules"))
                pg.click("a[data-parent-mode]")
                self.assertTrue(pg.is_checked("#ck-parent"))
                self.assertIn("Scam protection", pg.input_value("#ck-rules"))
                pg.fill("#ck-helper", "my son Alex")
                self.assertIn("my son Alex", pg.input_value("#ck-rules"))
                self.assertTrue(pg.is_checked("input[name=act-buy][value=never]"))
                pg.click("label:has(input[name=act-send][value=fine])")
                self.assertIn("You may do these without asking", pg.input_value("#ck-rules"))
                outside = [u for u in requests if not u.startswith(f"http://127.0.0.1:{srv.server_port}/") and "cloudflareinsights" not in u]
                self.assertEqual(outside, [])  # nothing about the checkup leaves the browser
                b.close()
        finally:
            srv.shutdown()


if __name__ == "__main__":
    unittest.main(verbosity=1)
