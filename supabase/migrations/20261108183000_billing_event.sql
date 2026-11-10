-- Apply a verified Stripe event. Do not run this on an unrelated project.
-- public.apply_billing_event is security invoker. It is not granted to anon or authenticated.
-- billing_writer can write entitlements and event ids. It cannot read or delete setups.
-- The function never deletes a setup and never reads editable JWT profile claims.

alter table public.entitlements
  add column if not exists cancel_at_period_end boolean not null default false;

do $$ begin
  create role billing_writer nologin bypassrls;
exception when duplicate_object then null;
end $$;

create or replace function public.apply_billing_event(p_event jsonb, p_prices jsonb)
returns jsonb
language plpgsql
security invoker
set search_path = ''
as $$
declare
  eid text := coalesce(p_event->>'id', '');
  created bigint := coalesce((p_event->>'created')::bigint, 0);
  kind text := coalesce(p_event->>'type', '');
  obj jsonb := coalesce(p_event->'data'->'object', '{}'::jsonb);
  meta jsonb := coalesce(obj->'metadata', '{}'::jsonb);
  inserted integer := 0;
  uid uuid;
  existing uuid;
  ent public.entitlements%rowtype;
  have boolean := false;
  plan text;
  price_id text;
  item_price text;
  sub_status text;
  customer text := obj->>'customer';
  sub_id text;
  new_status text;
  lim integer;
  period timestamptz;
  cancel_end boolean := false;
begin
  if eid = '' then
    raise exception 'missing event id';
  end if;
  insert into public.stripe_events (event_id, event_type, created_unix)
  values (eid, kind, created)
  on conflict (event_id) do nothing;
  get diagnostics inserted = row_count;
  if inserted = 0 then
    return jsonb_build_object('action', 'duplicate', 'event_id', eid);
  end if;

  if kind in ('checkout.session.completed', 'checkout.session.async_payment_succeeded') then
    if obj->>'mode' is distinct from 'subscription' then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'not a subscription');
    end if;
    if coalesce(obj->>'payment_status', '') not in ('paid', 'no_payment_required') then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'payment not paid');
    end if;
    plan := meta->>'plan_code';
    price_id := meta->>'price_id';
    if plan not in ('three', 'five') or p_prices->>plan is distinct from price_id then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'price not allowlisted');
    end if;
    begin
      uid := nullif(coalesce(meta->>'user_id', obj->>'client_reference_id'), '')::uuid;
    exception when invalid_text_representation then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'no user');
    end;
    if uid is null then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'no user');
    end if;
    lim := case plan when 'three' then 3 else 5 end;
    select * into ent from public.entitlements where user_id = uid for update;
    have := found;
    if have and created < ent.last_event_created then
      return jsonb_build_object('action', 'stale', 'event_id', eid, 'user_id', uid);
    end if;
    if not have then
      select uid, 'none'::text, 0, 'inactive'::text, null::text, null::text, null::timestamptz, 0::bigint, now(), false
      into ent;
    end if;
    ent.plan_code := plan;
    ent.setup_limit := lim;
    ent.status := 'active';
    ent.stripe_customer_id := customer;
    ent.stripe_subscription_id := obj->>'subscription';
    ent.cancel_at_period_end := false;
    ent.last_event_created := created;
  elsif kind in ('customer.subscription.created', 'customer.subscription.updated', 'customer.subscription.deleted') then
    sub_id := obj->>'id';
    select user_id into existing from public.entitlements where stripe_subscription_id = sub_id;
    if existing is null and customer is not null then
      select user_id into existing from public.entitlements where stripe_customer_id = customer;
    end if;
    if existing is not null then
      uid := existing;
    else
      begin
        uid := nullif(meta->>'user_id', '')::uuid;
      exception when invalid_text_representation then
        uid := null;
      end;
      if uid is not null then
        select * into ent from public.entitlements where user_id = uid;
        if found and ent.stripe_customer_id is not null and ent.stripe_customer_id is distinct from customer then
          uid := null;
        end if;
      end if;
    end if;
    if uid is null then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'no owned subscription');
    end if;
    select * into ent from public.entitlements where user_id = uid for update;
    have := found;
    if have and created < ent.last_event_created then
      return jsonb_build_object('action', 'stale', 'event_id', eid, 'user_id', uid);
    end if;
    if not have then
      select uid, 'none'::text, 0, 'inactive'::text, null::text, null::text, null::timestamptz, 0::bigint, now(), false
      into ent;
    end if;
    sub_status := coalesce(obj->>'status', '');
    cancel_end := coalesce(obj->>'cancel_at_period_end', '') = 'true';
    if obj ? 'current_period_end' and obj->>'current_period_end' ~ '^[0-9]+$' then
      period := to_timestamp((obj->>'current_period_end')::bigint);
    else
      period := ent.current_period_end;
    end if;
    item_price := obj#>>'{items,data,0,price,id}';
    plan := null;
    if item_price is not null and item_price = p_prices->>'three' then plan := 'three'; end if;
    if item_price is not null and item_price = p_prices->>'five' then plan := 'five'; end if;
    if sub_status = 'active' then new_status := 'active';
    elsif sub_status in ('past_due', 'unpaid', 'incomplete', 'paused') then new_status := 'past_due';
    elsif sub_status in ('canceled', 'incomplete_expired') then new_status := 'canceled';
    else new_status := 'past_due';
    end if;
    ent.stripe_customer_id := customer;
    ent.stripe_subscription_id := sub_id;
    ent.current_period_end := period;
    ent.last_event_created := created;
    if kind = 'customer.subscription.deleted' or sub_status in ('canceled', 'incomplete_expired') then
      ent.plan_code := 'none';
      ent.setup_limit := 0;
      ent.status := 'canceled';
      ent.cancel_at_period_end := false;
    elsif plan is null then
      ent.plan_code := 'none';
      ent.setup_limit := 0;
      ent.status := 'past_due';
      ent.cancel_at_period_end := cancel_end;
    elsif new_status = 'active' then
      ent.plan_code := plan;
      ent.setup_limit := case plan when 'three' then 3 else 5 end;
      ent.status := 'active';
      ent.cancel_at_period_end := cancel_end;
    else
      if ent.plan_code is distinct from plan then
        ent.setup_limit := case plan when 'three' then 3 else 5 end;
      end if;
      ent.plan_code := plan;
      ent.status := new_status;
      ent.cancel_at_period_end := cancel_end;
    end if;
  elsif kind = 'invoice.payment_failed' then
    sub_id := obj->>'subscription';
    select user_id into existing from public.entitlements where stripe_subscription_id = sub_id;
    if existing is null and customer is not null then
      select user_id into existing from public.entitlements where stripe_customer_id = customer;
    end if;
    uid := existing;
    if uid is null then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'unknown invoice');
    end if;
    select * into ent from public.entitlements where user_id = uid for update;
    have := found;
    if not have then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'unknown invoice');
    end if;
    if created < ent.last_event_created then
      return jsonb_build_object('action', 'stale', 'event_id', eid, 'user_id', uid);
    end if;
    ent.status := 'past_due';
    ent.last_event_created := created;
  elsif kind in ('charge.refunded', 'charge.dispute.created', 'radar.early_fraud_warning.created') then
    select user_id into uid from public.entitlements where stripe_customer_id = customer;
    if uid is null then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'unknown charge customer');
    end if;
    select * into ent from public.entitlements where user_id = uid for update;
    have := found;
    if not have then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'unknown charge customer');
    end if;
    if created < ent.last_event_created then
      return jsonb_build_object('action', 'stale', 'event_id', eid, 'user_id', uid);
    end if;
    ent.status := 'past_due';
    ent.last_event_created := created;
  else
    return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'unhandled type');
  end if;

  begin
    if have then
      update public.entitlements set
        plan_code = ent.plan_code,
        setup_limit = ent.setup_limit,
        status = ent.status,
        stripe_customer_id = ent.stripe_customer_id,
        stripe_subscription_id = ent.stripe_subscription_id,
        current_period_end = ent.current_period_end,
        last_event_created = ent.last_event_created,
        cancel_at_period_end = ent.cancel_at_period_end,
        updated_at = now()
      where user_id = uid;
    else
      insert into public.entitlements (
        user_id, plan_code, setup_limit, status, stripe_customer_id, stripe_subscription_id,
        current_period_end, last_event_created, cancel_at_period_end
      ) values (
        uid, ent.plan_code, ent.setup_limit, ent.status, ent.stripe_customer_id, ent.stripe_subscription_id,
        ent.current_period_end, ent.last_event_created, ent.cancel_at_period_end
      );
    end if;
  exception
    when unique_violation then
      return jsonb_build_object('action', 'ignored', 'event_id', eid, 'reason', 'customer already bound');
  end;
  return jsonb_build_object('action', 'applied', 'event_id', eid, 'user_id', uid, 'status', ent.status, 'setup_limit', ent.setup_limit, 'plan_code', ent.plan_code, 'cancel_at_period_end', ent.cancel_at_period_end);
end;
$$;

revoke all on function public.apply_billing_event(jsonb, jsonb) from public, anon, authenticated;
grant usage on schema public to billing_writer;
grant select, insert, update on public.entitlements to billing_writer;
grant select, insert on public.stripe_events to billing_writer;
grant execute on function public.apply_billing_event(jsonb, jsonb) to billing_writer;
revoke all on public.setups, public.setup_versions from billing_writer;
