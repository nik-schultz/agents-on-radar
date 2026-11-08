#!/usr/bin/env python3
"""Billing decisions and the in-memory cap model. No Stripe account is contacted."""
import hashlib, hmac, json, os, sys, threading, unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from accounts.billing import (
    BillingError, access, apply_event, blank_entitlement, checkout_params,
    entitlement_from_browser_return, new_store, portal_params, verify_signature,
)
from accounts.library import CapError, Library

PRICES = {"three": "price_three_test", "five": "price_five_test"}
USER = "11111111-1111-1111-1111-111111111111"


def signed(payload, secret="whsec_test", stamp=1_700_000_000):
    body = json.dumps(payload).encode()
    mac = hmac.new(secret.encode(), ("%d." % stamp).encode() + body, hashlib.sha256).hexdigest()
    return body, "t=%d,v1=%s" % (stamp, mac), stamp


def event(event_id, created, kind, obj):
    return {"id": event_id, "created": created, "type": kind, "data": {"object": obj}}


class CheckoutTests(unittest.TestCase):
    def test_checkout_is_allowlisted_and_does_not_collect_tax_here(self):
        params, key = checkout_params(USER, "three", PRICES, "https://example.test/ok", "https://example.test/no", "abcdefgh")
        self.assertEqual(params["mode"], "subscription")
        self.assertEqual(params["line_items"], [{"price": "price_three_test", "quantity": 1}])
        self.assertNotIn("payment_method_types", params)
        self.assertNotIn("automatic_tax", params)
        self.assertEqual(params["metadata"]["plan_code"], "three")
        self.assertTrue(params["integration_identifier"].endswith("abcdefgh"))
        self.assertTrue(key.startswith("setups-"))
        with self.assertRaises(BillingError):
            checkout_params(USER, "three", {"three": ""}, "https://a", "https://b", "abcdefgh")
        with self.assertRaises(BillingError):
            checkout_params(USER, "unlimited", PRICES, "https://a", "https://b", "abcdefgh")

    def test_browser_return_does_not_grant_access(self):
        with self.assertRaises(BillingError):
            entitlement_from_browser_return({"session_id": "cs_test_123"})

    def test_portal_requires_our_customer_id(self):
        self.assertEqual(portal_params("cus_123", "https://example.test/back")["customer"], "cus_123")
        with self.assertRaises(BillingError):
            portal_params("user_123", "https://example.test/back")


class WebhookTests(unittest.TestCase):
    def test_signature_and_duplicate_and_stale_order(self):
        payload = event("evt_1", 100, "checkout.session.completed", {
            "mode": "subscription", "payment_status": "paid", "customer": "cus_1", "subscription": "sub_1",
            "client_reference_id": USER,
            "metadata": {"user_id": USER, "plan_code": "five", "price_id": "price_five_test"},
        })
        body, header, stamp = signed(payload, stamp=100)
        verified = verify_signature(body, header, "whsec_test", now=100)
        self.assertEqual(verified["id"], "evt_1")
        with self.assertRaises(BillingError):
            verify_signature(body, header, "whsec_test", now=100 + 10_000)
        with self.assertRaises(BillingError):
            verify_signature(body, "t=100,v1=deadbeef", "whsec_test", now=100)

        store = new_store()
        first = apply_event(store, verified, PRICES)
        self.assertEqual(first["action"], "applied")
        self.assertEqual(first["entitlement"]["setup_limit"], 5)
        self.assertEqual(first["entitlement"]["status"], "active")
        again = apply_event(store, verified, PRICES)
        self.assertEqual(again["action"], "duplicate")
        self.assertEqual(store["entitlements"][USER]["setup_limit"], 5)

        older = event("evt_old", 50, "customer.subscription.updated", {
            "id": "sub_1", "customer": "cus_1", "status": "active",
            "items": {"data": [{"price": {"id": "price_three_test"}}]},
            "metadata": {"user_id": USER},
        })
        stale = apply_event(store, older, PRICES)
        self.assertEqual(stale["action"], "stale")
        self.assertEqual(store["entitlements"][USER]["setup_limit"], 5)
        self.assertNotIn("delete_setups", first)

    def test_downgrade_and_cancel_keep_the_entitlement_row_only(self):
        store = new_store()
        apply_event(store, event("evt_a", 10, "checkout.session.completed", {
            "mode": "subscription", "payment_status": "paid", "customer": "cus_1", "subscription": "sub_1",
            "metadata": {"user_id": USER, "plan_code": "five", "price_id": "price_five_test"},
        }), PRICES)
        apply_event(store, event("evt_b", 20, "customer.subscription.updated", {
            "id": "sub_1", "customer": "cus_1", "status": "active",
            "items": {"data": [{"price": {"id": "price_three_test"}}]},
        }), PRICES)
        row = store["entitlements"][USER]
        self.assertEqual(row["setup_limit"], 3)
        self.assertEqual(row["status"], "active")
        rights = access(row, saved_count=4)
        self.assertFalse(rights["can_create"])
        self.assertTrue(rights["can_read"])
        self.assertTrue(rights["can_export"])
        self.assertTrue(rights["can_edit"])
        apply_event(store, event("evt_c", 30, "customer.subscription.deleted", {
            "id": "sub_1", "customer": "cus_1", "status": "canceled",
        }), PRICES)
        canceled = store["entitlements"][USER]
        self.assertEqual(canceled["status"], "canceled")
        self.assertEqual(canceled["setup_limit"], 0)
        after = access(canceled, saved_count=4)
        self.assertTrue(after["can_export"])
        self.assertFalse(after["can_create"])
        self.assertFalse(after["can_edit"])

    def test_failed_payment_and_unknown_price_do_not_raise_the_cap(self):
        store = new_store()
        apply_event(store, event("evt_a", 10, "checkout.session.completed", {
            "mode": "subscription", "payment_status": "paid", "customer": "cus_9", "subscription": "sub_9",
            "metadata": {"user_id": USER, "plan_code": "three", "price_id": "price_three_test"},
        }), PRICES)
        apply_event(store, event("evt_b", 11, "invoice.payment_failed", {
            "customer": "cus_9", "subscription": "sub_9",
        }), PRICES)
        self.assertEqual(store["entitlements"][USER]["status"], "past_due")
        self.assertFalse(access(store["entitlements"][USER], 0)["can_create"])
        apply_event(store, event("evt_c", 12, "customer.subscription.updated", {
            "id": "sub_9", "customer": "cus_9", "status": "active",
            "items": {"data": [{"price": {"id": "price_not_ours"}}]},
        }), PRICES)
        self.assertEqual(store["entitlements"][USER]["setup_limit"], 0)
        self.assertNotEqual(store["entitlements"][USER]["plan_code"], "five")

    def test_unpaid_checkout_is_ignored(self):
        store = new_store()
        result = apply_event(store, event("evt_wait", 5, "checkout.session.completed", {
            "mode": "subscription", "payment_status": "unpaid", "customer": "cus_1", "subscription": "sub_1",
            "metadata": {"user_id": USER, "plan_code": "three", "price_id": "price_three_test"},
        }), PRICES)
        self.assertEqual(result["action"], "ignored")
        self.assertNotIn(USER, store["entitlements"])


class ClientContractTests(unittest.TestCase):
    def test_browser_helper_matches_and_does_not_inject_html(self):
        source = open(os.path.join(os.path.dirname(__file__), "..", "static", "accounts.js"), encoding="utf-8").read()
        self.assertNotIn("innerHTML", source)
        raw = subprocess_run = __import__("subprocess").check_output(["node", "-e", """
          const a = require("./static/accounts.js");
          const row = {status: "active", setup_limit: 3};
          const over = a.accessFromRow(row, 3);
          const under = a.accessFromRow(row, 2);
          const dead = a.accessFromRow({status: "canceled", setup_limit: 0}, 2);
          process.stdout.write(JSON.stringify({over: over, under: under, dead: dead}));
        """], cwd=os.path.dirname(os.path.dirname(__file__)))
        got = json.loads(raw)
        self.assertFalse(got["over"]["can_create"])
        self.assertTrue(got["over"]["can_export"])
        self.assertTrue(got["under"]["can_create"])
        self.assertTrue(got["dead"]["can_export"])
        self.assertFalse(got["dead"]["can_edit"])


class LibraryTests(unittest.TestCase):
    def test_two_threads_cannot_both_pass_a_one_setup_cap(self):
        lib = Library()
        lib.set_entitlement("ada", "active", 1, "three")
        start = threading.Barrier(2)
        results = []

        def attempt():
            start.wait()
            try:
                results.append(("ok", lib.create("ada", "week")))
            except CapError as exc:
                results.append(("no", str(exc)))

        threads = [threading.Thread(target=attempt) for _ in range(2)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(sorted(r[0] for r in results), ["no", "ok"])
        self.assertEqual(lib.export_titles("ada"), ["week"])

    def test_downgrade_blocks_creates_and_keeps_export(self):
        lib = Library()
        lib.set_entitlement("ada", "active", 5, "five")
        for i in range(4):
            lib.create("ada", "setup %d" % i)
        lib.set_entitlement("ada", "active", 3, "three")
        self.assertEqual(len(lib.export_titles("ada")), 4)
        with self.assertRaises(CapError):
            lib.create("ada", "one more")
        self.assertEqual(lib.save("ada", 0, "renamed"), 2)
        lib.set_entitlement("ada", "canceled", 0, "none")
        self.assertEqual(lib.export_titles("ada")[0], "renamed")
        with self.assertRaises(CapError):
            lib.save("ada", 0, "again")


if __name__ == "__main__":
    unittest.main()
