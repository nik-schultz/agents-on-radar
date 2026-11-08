"""In-memory model of the setup cap. The database lock is FOR UPDATE in the migration.

This is not a Postgres run. tests/test_rls.py runs the SQL when local Postgres is up.
"""
import threading


class CapError(Exception):
    pass


class Library:
    def __init__(self):
        self._guard = threading.Lock()
        self._user_locks = {}
        self.rows = {}
        self.entitlements = {}

    def _lock(self, user_id):
        with self._guard:
            lock = self._user_locks.get(user_id)
            if lock is None:
                lock = threading.Lock()
                self._user_locks[user_id] = lock
        return lock

    def set_entitlement(self, user_id, status, setup_limit, plan_code):
        self.entitlements[user_id] = {"status": status, "setup_limit": setup_limit, "plan_code": plan_code}

    def create(self, user_id, title):
        with self._lock(user_id):
            ent = self.entitlements.get(user_id)
            if not ent or ent["status"] != "active":
                raise CapError("saves are not available on this account")
            rows = self.rows.setdefault(user_id, [])
            live = [r for r in rows if not r["deleted"]]
            if len(live) >= ent["setup_limit"]:
                raise CapError("setup limit reached")
            rows.append({"title": title, "deleted": False, "versions": [title]})
            return len(live) + 1

    def save(self, user_id, index, title):
        with self._lock(user_id):
            ent = self.entitlements.get(user_id)
            if not ent or ent["status"] != "active":
                raise CapError("editing is not available on this account")
            live = [r for r in self.rows.get(user_id, []) if not r["deleted"]]
            row = live[index]
            row["title"] = title
            row["versions"].append(title)
            return len(row["versions"])

    def export_titles(self, user_id):
        return [r["title"] for r in self.rows.get(user_id, []) if not r["deleted"]]
