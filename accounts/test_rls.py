#!/usr/bin/env python3
"""Apply the saved-setup migration to local Postgres and check isolation.

This is a local database named bots_setups_test. It is not a Supabase project
and it is not production. auth.uid() is a test stub, not Supabase Auth.
"""
import os, threading, unittest, uuid

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIGRATION = os.path.join(ROOT, "supabase", "migrations", "20261108160000_saved_setups.sql")
DB = "bots_setups_test"

STUB = """
create schema if not exists auth;
create table if not exists auth.users (id uuid primary key);
create or replace function auth.uid() returns uuid
language sql stable as $$
  select nullif(current_setting('request.jwt.claim.sub', true), '')::uuid;
$$;
do $$ begin create role anon nologin; exception when duplicate_object then null; end $$;
do $$ begin create role authenticated nologin; exception when duplicate_object then null; end $$;
"""


def admin():
    conn = psycopg2.connect(dbname="postgres", user="postgres", host="/var/run/postgresql")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return conn


def connect():
    return psycopg2.connect(dbname=DB, user="postgres", host="/var/run/postgresql")


class RlsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        adm = admin()
        cur = adm.cursor()
        cur.execute("select pg_terminate_backend(pid) from pg_stat_activity where datname = %s and pid <> pg_backend_pid()", (DB,))
        cur.execute("drop database if exists %s" % DB)
        cur.execute("create database %s" % DB)
        adm.close()
        conn = connect()
        cur = conn.cursor()
        cur.execute(STUB)
        cur.execute("do $$ begin create role authenticated nologin; exception when duplicate_object then null; end $$;")
        cur.execute("grant authenticated to postgres")
        cur.execute("grant usage on schema auth to authenticated")
        cur.execute("grant execute on function auth.uid() to authenticated")
        sql = open(MIGRATION, encoding="utf-8").read()
        cur.execute(sql)
        conn.commit()
        cls.conn = conn
        cls.ada = str(uuid.uuid4())
        cls.bea = str(uuid.uuid4())
        cur.execute("insert into auth.users (id) values (%s), (%s)", (cls.ada, cls.bea))
        cur.execute(
            "insert into public.entitlements (user_id, plan_code, setup_limit, status, stripe_customer_id) values (%s, 'three', 3, 'active', 'cus_ada'), (%s, 'three', 3, 'active', 'cus_bea')",
            (cls.ada, cls.bea),
        )
        conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        adm = admin()
        cur = adm.cursor()
        cur.execute("select pg_terminate_backend(pid) from pg_stat_activity where datname = %s and pid <> pg_backend_pid()", (DB,))
        cur.execute("drop database if exists %s" % DB)
        adm.close()

    def as_user(self, user_id):
        cur = self.conn.cursor()
        cur.execute("reset role")
        cur.execute("select set_config('request.jwt.claim.sub', %s, false)", (user_id,))
        cur.execute("set role authenticated")
        return cur

    def reset_role(self):
        cur = self.conn.cursor()
        cur.execute("reset role")
        return cur

    def test_migration_text_rejects_user_metadata(self):
        sql = open(MIGRATION, encoding="utf-8").read().lower()
        self.assertNotIn("user_metadata", sql)
        self.assertNotIn("raw_user_meta_data", sql)
        self.assertIn("enable row level security", sql)
        self.assertIn("force row level security", sql)

    def test_two_users_cannot_read_or_change_each_other(self):
        cur = self.as_user(self.ada)
        cur.execute(
            "select public.create_setup('weekly-plan', 'Ada week', '{\"week_start\": \"Monday 9 November 2026\"}'::jsonb, 'instructions for ada')",
        )
        ada_id = cur.fetchone()[0]
        self.conn.commit()
        cur = self.as_user(self.bea)
        cur.execute("select title from public.setups")
        self.assertNotIn("Ada week", [row[0] for row in cur.fetchall()])
        with self.assertRaises(psycopg2.Error):
            cur.execute("select public.soft_delete_setup(%s)", (ada_id,))
            self.conn.commit()
        self.conn.rollback()
        self.reset_role()
        cur = self.conn.cursor()
        cur.execute("select count(*) from public.setups where user_id = %s and title = 'Ada week' and deleted_at is null", (self.ada,))
        self.assertEqual(cur.fetchone()[0], 1)

    def test_cap_versions_downgrade_and_past_due(self):
        cur = self.as_user(self.bea)
        ids = []
        for i in range(3):
            cur.execute(
                "select public.create_setup('email-draft', %s, '{}'::jsonb, 'draft text')",
                ("Draft %d" % i,),
            )
            ids.append(cur.fetchone()[0])
        self.conn.commit()
        with self.assertRaises(psycopg2.Error):
            cur.execute("select public.create_setup('compare-quotes', 'Fourth', '{}'::jsonb, 'quotes')")
            self.conn.commit()
        self.conn.rollback()
        cur = self.as_user(self.bea)
        cur.execute("select public.save_setup(%s, 'Draft renamed', '{\"tone\": \"direct\"}'::jsonb, 'draft text revised')", (ids[0],))
        version = cur.fetchone()[0]
        self.assertEqual(version, 2)
        self.conn.commit()
        cur.execute("select version_no, title from public.setup_versions where setup_id = %s order by version_no", (ids[0],))
        self.assertEqual([row[1] for row in cur.fetchall()], ["Draft 0", "Draft renamed"])
        self.reset_role()
        cur = self.conn.cursor()
        cur.execute("update public.entitlements set setup_limit = 3, plan_code = 'three', status = 'active' where user_id = %s", (self.bea,))
        self.conn.commit()
        cur = self.as_user(self.bea)
        cur.execute("select title from public.setups where deleted_at is null order by title")
        self.assertEqual(len(cur.fetchall()), 3)
        with self.assertRaises(psycopg2.Error):
            cur.execute("select public.create_setup('weekly-plan', 'Extra', '{}'::jsonb, 'more')")
            self.conn.commit()
        self.conn.rollback()
        self.reset_role()
        cur = self.conn.cursor()
        cur.execute("update public.entitlements set status = 'past_due' where user_id = %s", (self.bea,))
        self.conn.commit()
        cur = self.as_user(self.bea)
        cur.execute("select count(*) from public.setups where deleted_at is null")
        self.assertEqual(cur.fetchone()[0], 3)
        with self.assertRaises(psycopg2.Error):
            cur.execute("select public.save_setup(%s, 'Nope', '{}'::jsonb, 'nope')", (ids[0],))
            self.conn.commit()
        self.conn.rollback()
        cur = self.as_user(self.bea)
        cur.execute("select public.soft_delete_setup(%s)", (ids[2],))
        self.conn.commit()
        cur.execute("select title from public.setups where deleted_at is null")
        self.assertEqual(len(cur.fetchall()), 2)

    def test_authenticated_cannot_write_entitlements_or_events(self):
        cur = self.as_user(self.ada)
        with self.assertRaises(psycopg2.Error):
            cur.execute("update public.entitlements set setup_limit = 5 where user_id = %s", (self.ada,))
            self.conn.commit()
        self.conn.rollback()
        cur = self.as_user(self.ada)
        with self.assertRaises(psycopg2.Error):
            cur.execute("insert into public.stripe_events (event_id, event_type, created_unix) values ('evt_fake', 'checkout.session.completed', 1)")
            self.conn.commit()
        self.conn.rollback()
        with self.assertRaises(psycopg2.Error):
            cur = self.as_user(self.ada)
            cur.execute("select count(*) from public.stripe_events")
            self.conn.commit()
        self.conn.rollback()

    def test_two_connections_cannot_both_pass_a_one_setup_cap(self):
        uid = str(uuid.uuid4())
        cur = self.conn.cursor()
        cur.execute("reset role")
        cur.execute("insert into auth.users (id) values (%s)", (uid,))
        cur.execute(
            "insert into public.entitlements (user_id, plan_code, setup_limit, status) values (%s, 'three', 3, 'active')",
            (uid,),
        )
        self.conn.commit()
        cur.execute("select set_config('request.jwt.claim.sub', %s, false)", (uid,))
        cur.execute("set role authenticated")
        for n in range(2):
            cur.execute(
                "select public.create_setup('weekly-plan', %s, '{}'::jsonb, 'seed text')",
                ("Seed %d" % n,),
            )
        self.conn.commit()
        cur.execute("reset role")
        results = []

        def worker():
            conn = connect()
            c = conn.cursor()
            try:
                c.execute("select set_config('request.jwt.claim.sub', %s, false)", (uid,))
                c.execute("set role authenticated")
                c.execute("select public.create_setup('weekly-plan', 'Race', '{}'::jsonb, 'race text that is long enough')")
                conn.commit()
                results.append("ok")
            except Exception:
                conn.rollback()
                results.append("no")
            finally:
                conn.close()

        threads = [threading.Thread(target=worker) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(sorted(results), ["no", "ok"])
        cur.execute("reset role")
        cur.execute("select count(*) from public.setups where user_id = %s and deleted_at is null", (uid,))
        self.assertEqual(cur.fetchone()[0], 3)

    def test_malicious_text_is_stored_as_text_for_the_owner_only(self):
        cur = self.as_user(self.ada)
        nasty = '<script>alert(1)</script>'
        cur.execute(
            "select public.create_setup('weekly-plan', 'Quoted', %s::jsonb, %s)",
            ('{"fixed": "<img src=x onerror=alert(1)>"}', nasty),
        )
        self.conn.commit()
        cur.execute("select instructions from public.setups where title = 'Quoted'")
        self.assertEqual(cur.fetchone()[0], nasty)
        cur = self.as_user(self.bea)
        cur.execute("select count(*) from public.setups where instructions like %s", ('%<script>%',))
        self.assertEqual(cur.fetchone()[0], 0)


if __name__ == "__main__":
    unittest.main()
