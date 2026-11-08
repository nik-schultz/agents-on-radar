"""Stripe Billing decisions for saved setups. No network calls.

A browser return never changes an entitlement. Only a verified webhook does.
This module does not delete setups.
"""
import hashlib, hmac, json, string, time

PLANS = {
    "three": {"setups": 3, "price_usd": 9, "interval": "month"},
    "five": {"setups": 5, "price_usd": 14, "interval": "month"},
}
ACTIVE_STRIPE = {"active"}
PAST_DUE_STRIPE = {"past_due", "unpaid", "incomplete", "paused"}
CANCELED_STRIPE = {"canceled", "incomplete_expired"}


class BillingError(Exception):
    pass


def blank_entitlement(user_id):
    return {
        "user_id": user_id,
        "plan_code": "none",
        "setup_limit": 0,
        "status": "inactive",
        "stripe_customer_id": None,
        "stripe_subscription_id": None,
        "current_period_end": None,
        "last_event_created": 0,
    }


def access(entitlement, saved_count):
    """Read and export stay. New saves and edits require an active plan and room under the cap."""
    status = (entitlement or {}).get("status")
    limit = int((entitlement or {}).get("setup_limit") or 0)
    active = status == "active"
    return {
        "can_read": bool(entitlement),
        "can_export": bool(entitlement),
        "can_edit": active,
        "can_create": active and saved_count < limit,
        "can_delete": bool(entitlement),
    }


def entitlement_from_browser_return(query):
    """Success-page query strings do not grant a plan."""
    raise BillingError("browser return does not grant access")


def checkout_params(user_id, plan_code, prices, success_url, cancel_url, suffix):
    if plan_code not in PLANS:
        raise BillingError("unknown plan")
    if not user_id or not isinstance(user_id, str):
        raise BillingError("missing user")
    price = (prices or {}).get(plan_code) or ""
    if not price.startswith("price_"):
        raise BillingError("price not configured")
    if not suffix or len(suffix) != 8 or any(c not in string.ascii_lowercase for c in suffix):
        raise BillingError("integration suffix must be 8 letters")
    params = {
        "mode": "subscription",
        "client_reference_id": user_id,
        "line_items": [{"price": price, "quantity": 1}],
        "success_url": success_url,
        "cancel_url": cancel_url,
        "metadata": {"user_id": user_id, "plan_code": plan_code, "price_id": price},
        "subscription_data": {"metadata": {"user_id": user_id, "plan_code": plan_code}},
        "integration_identifier": "botsdothat_setups_" + suffix,
    }
    if "payment_method_types" in params or "automatic_tax" in params:
        raise BillingError("unexpected checkout field")
    idempotency_key = "setups-%s-%s-%s" % (user_id, plan_code, time.strftime("%Y%m%d%H", time.gmtime()))
    return params, idempotency_key


def portal_params(customer_id, return_url):
    if not customer_id or not str(customer_id).startswith("cus_"):
        raise BillingError("no customer")
    return {"customer": customer_id, "return_url": return_url}


def verify_signature(payload, header, secret, now, tolerance=300):
    if not isinstance(payload, (bytes, bytearray)):
        raise BillingError("payload must be bytes")
    parts = {}
    for item in (header or "").split(","):
        if "=" not in item:
            continue
        k, v = item.split("=", 1)
        parts.setdefault(k.strip(), []).append(v.strip())
    if "t" not in parts or "v1" not in parts:
        raise BillingError("missing signature")
    try:
        stamp = int(parts["t"][0])
    except ValueError as exc:
        raise BillingError("bad timestamp") from exc
    if abs(int(now) - stamp) > tolerance:
        raise BillingError("stale signature")
    mac = hmac.new(secret.encode("utf-8"), ("%d." % stamp).encode("utf-8") + bytes(payload), hashlib.sha256).hexdigest()
    if not any(hmac.compare_digest(mac, candidate) for candidate in parts["v1"]):
        raise BillingError("signature mismatch")
    return json.loads(payload.decode("utf-8"))


def _limit_for(plan_code):
    if plan_code not in PLANS:
        return 0
    return PLANS[plan_code]["setups"]


def _status_for_subscription(stripe_status):
    if stripe_status in ACTIVE_STRIPE:
        return "active"
    if stripe_status in PAST_DUE_STRIPE:
        return "past_due"
    if stripe_status in CANCELED_STRIPE:
        return "canceled"
    return "past_due"


def _price_id(subscription):
    items = ((subscription or {}).get("items") or {}).get("data") or []
    if not items:
        return ""
    price = items[0].get("price") or {}
    return price.get("id") or ""


def _bind_user(store, customer_id, subscription_id, metadata_user):
    existing = None
    if subscription_id:
        existing = store.get("by_subscription", {}).get(subscription_id)
    if not existing and customer_id:
        existing = store.get("by_customer", {}).get(customer_id)
    if existing:
        row = store["entitlements"].get(existing)
        if metadata_user and metadata_user != existing and row and row.get("stripe_customer_id") not in (None, customer_id):
            return None
        return existing
    if metadata_user:
        row = store["entitlements"].get(metadata_user)
        if row and row.get("stripe_customer_id") not in (None, "", customer_id):
            return None
        return metadata_user
    return None


def apply_event(store, event, prices):
    """Apply one verified event. `prices` maps plan code -> price id.

    Returns action: applied, duplicate, stale, ignored.
    Never returns a list of setups to delete.
    """
    event_id = event.get("id") or ""
    if not event_id:
        raise BillingError("missing event id")
    if event_id in store["events"]:
        return {"action": "duplicate", "event_id": event_id}
    created = int(event.get("created") or 0)
    kind = event.get("type") or ""
    obj = (event.get("data") or {}).get("object") or {}
    price_to_plan = {pid: code for code, pid in (prices or {}).items() if pid}
    user_id = None
    patch = None

    if kind in ("checkout.session.completed", "checkout.session.async_payment_succeeded"):
        if obj.get("mode") != "subscription":
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "not a subscription"}
        if obj.get("payment_status") not in ("paid", "no_payment_required"):
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "payment not paid"}
        meta = obj.get("metadata") or {}
        plan = meta.get("plan_code")
        price_id = meta.get("price_id")
        if plan not in PLANS or price_to_plan.get(price_id) != plan:
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "price not allowlisted"}
        user_id = meta.get("user_id") or obj.get("client_reference_id")
        if not user_id:
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "no user"}
        patch = {
            "plan_code": plan,
            "setup_limit": _limit_for(plan),
            "status": "active",
            "stripe_customer_id": obj.get("customer"),
            "stripe_subscription_id": obj.get("subscription"),
        }
    elif kind in ("customer.subscription.created", "customer.subscription.updated", "customer.subscription.deleted"):
        user_id = _bind_user(store, obj.get("customer"), obj.get("id"), (obj.get("metadata") or {}).get("user_id"))
        if not user_id:
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "no owned subscription"}
        if kind == "customer.subscription.deleted" or obj.get("status") in CANCELED_STRIPE:
            patch = {"plan_code": "none", "setup_limit": 0, "status": "canceled", "stripe_subscription_id": obj.get("id"), "stripe_customer_id": obj.get("customer"), "current_period_end": obj.get("current_period_end")}
        else:
            plan = price_to_plan.get(_price_id(obj))
            status = _status_for_subscription(obj.get("status"))
            if plan is None:
                patch = {"status": "past_due", "setup_limit": 0, "plan_code": "none", "stripe_subscription_id": obj.get("id"), "stripe_customer_id": obj.get("customer")}
            elif status != "active":
                current = store["entitlements"].get(user_id) or blank_entitlement(user_id)
                patch = {
                    "status": status,
                    "plan_code": plan,
                    "setup_limit": _limit_for(plan),
                    "stripe_subscription_id": obj.get("id"),
                    "stripe_customer_id": obj.get("customer"),
                    "current_period_end": obj.get("current_period_end"),
                }
                # Keep the recorded limit for display, but status blocks new saves.
                patch["setup_limit"] = current.get("setup_limit") if current.get("plan_code") == plan else _limit_for(plan)
            else:
                patch = {
                    "status": "active",
                    "plan_code": plan,
                    "setup_limit": _limit_for(plan),
                    "stripe_subscription_id": obj.get("id"),
                    "stripe_customer_id": obj.get("customer"),
                    "current_period_end": obj.get("current_period_end"),
                }
    elif kind in ("invoice.payment_failed",):
        user_id = _bind_user(store, obj.get("customer"), obj.get("subscription"), None)
        if not user_id:
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "unknown invoice"}
        patch = {"status": "past_due"}
    elif kind in ("charge.refunded", "charge.dispute.created", "radar.early_fraud_warning.created"):
        customer = obj.get("customer")
        user_id = store.get("by_customer", {}).get(customer)
        if not user_id:
            store["events"][event_id] = created
            return {"action": "ignored", "event_id": event_id, "reason": "unknown charge customer"}
        patch = {"status": "past_due"}
    else:
        store["events"][event_id] = created
        return {"action": "ignored", "event_id": event_id, "reason": "unhandled type"}

    row = dict(store["entitlements"].get(user_id) or blank_entitlement(user_id))
    if created < int(row.get("last_event_created") or 0):
        store["events"][event_id] = created
        return {"action": "stale", "event_id": event_id, "user_id": user_id}
    row.update(patch)
    row["user_id"] = user_id
    row["last_event_created"] = created
    store["entitlements"][user_id] = row
    if row.get("stripe_customer_id"):
        store.setdefault("by_customer", {})[row["stripe_customer_id"]] = user_id
    if row.get("stripe_subscription_id"):
        store.setdefault("by_subscription", {})[row["stripe_subscription_id"]] = user_id
    store["events"][event_id] = created
    return {"action": "applied", "event_id": event_id, "user_id": user_id, "entitlement": row}


def new_store():
    return {"events": {}, "entitlements": {}, "by_customer": {}, "by_subscription": {}}
