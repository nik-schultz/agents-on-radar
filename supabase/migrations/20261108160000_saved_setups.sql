-- Saved instruction setups. Apply only to a Supabase project created for this product.
-- Do not run this against an unrelated project.
-- `private` must stay out of the Data API exposed schemas.
-- Webhook writes use the service role (BYPASSRLS). Browser writes go through the functions below.

create schema if not exists private;
revoke all on schema private from public, anon, authenticated;

create table public.entitlements (
  user_id uuid primary key references auth.users (id) on delete cascade,
  plan_code text not null default 'none' check (plan_code in ('none', 'three', 'five')),
  setup_limit integer not null default 0 check (setup_limit in (0, 3, 5)),
  status text not null default 'inactive' check (status in ('inactive', 'active', 'past_due', 'canceled')),
  stripe_customer_id text unique,
  stripe_subscription_id text unique,
  current_period_end timestamptz,
  last_event_created bigint not null default 0,
  updated_at timestamptz not null default now()
);

create table public.setups (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users (id) on delete cascade,
  task_id text not null check (task_id in ('weekly-plan', 'email-draft', 'compare-quotes')),
  title text not null check (char_length(btrim(title)) between 1 and 120),
  answers jsonb not null,
  instructions text not null check (char_length(instructions) between 1 and 20000),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz
);

create table public.setup_versions (
  id uuid primary key default gen_random_uuid(),
  setup_id uuid not null references public.setups (id) on delete cascade,
  user_id uuid not null references auth.users (id) on delete cascade,
  version_no integer not null check (version_no > 0),
  title text not null,
  answers jsonb not null,
  instructions text not null,
  created_at timestamptz not null default now(),
  unique (setup_id, version_no)
);

create table public.stripe_events (
  event_id text primary key,
  event_type text not null,
  created_unix bigint not null,
  received_at timestamptz not null default now()
);

create index setups_user_active_idx on public.setups (user_id) where deleted_at is null;
create index setup_versions_setup_idx on public.setup_versions (setup_id, version_no desc);
create index entitlements_customer_idx on public.entitlements (stripe_customer_id);

alter table public.entitlements enable row level security;
alter table public.setups enable row level security;
alter table public.setup_versions enable row level security;
alter table public.stripe_events enable row level security;
alter table public.entitlements force row level security;
alter table public.setups force row level security;
alter table public.setup_versions force row level security;
alter table public.stripe_events force row level security;

revoke all on public.entitlements, public.setups, public.setup_versions, public.stripe_events from public, anon, authenticated;
grant select on public.entitlements, public.setups, public.setup_versions to authenticated;

create policy entitlements_select_own on public.entitlements
  for select to authenticated
  using ((select auth.uid()) = user_id);

create policy setups_select_own on public.setups
  for select to authenticated
  using ((select auth.uid()) = user_id);

create policy setup_versions_select_own on public.setup_versions
  for select to authenticated
  using ((select auth.uid()) = user_id);

-- No policies on stripe_events: signed-in users cannot read webhook ids.

create or replace function private.create_setup(p_task_id text, p_title text, p_answers jsonb, p_instructions text)
returns uuid
language plpgsql
security definer
set search_path = ''
as $$
declare
  uid uuid := auth.uid();
  lim integer;
  st text;
  n integer;
  sid uuid;
begin
  if uid is null then
    raise exception 'not signed in';
  end if;
  if p_task_id not in ('weekly-plan', 'email-draft', 'compare-quotes') then
    raise exception 'unknown task';
  end if;
  if p_title is null or char_length(btrim(p_title)) < 1 or char_length(p_title) > 120 then
    raise exception 'title length';
  end if;
  if p_instructions is null or char_length(p_instructions) < 1 or char_length(p_instructions) > 20000 then
    raise exception 'instructions length';
  end if;
  if jsonb_typeof(p_answers) is distinct from 'object' or octet_length(p_answers::text) > 20000 then
    raise exception 'answers must be a small object';
  end if;
  select e.setup_limit, e.status into lim, st
  from public.entitlements e
  where e.user_id = uid
  for update;
  if not found or st is distinct from 'active' then
    raise exception 'saves are not available on this account';
  end if;
  select count(*)::integer into n
  from public.setups s
  where s.user_id = uid and s.deleted_at is null;
  if n >= lim then
    raise exception 'setup limit reached';
  end if;
  insert into public.setups (user_id, task_id, title, answers, instructions)
  values (uid, p_task_id, btrim(p_title), p_answers, p_instructions)
  returning id into sid;
  insert into public.setup_versions (setup_id, user_id, version_no, title, answers, instructions)
  values (sid, uid, 1, btrim(p_title), p_answers, p_instructions);
  return sid;
end;
$$;

create or replace function private.save_setup(p_setup_id uuid, p_title text, p_answers jsonb, p_instructions text)
returns integer
language plpgsql
security definer
set search_path = ''
as $$
declare
  uid uuid := auth.uid();
  st text;
  next_no integer;
begin
  if uid is null then
    raise exception 'not signed in';
  end if;
  if p_title is null or char_length(btrim(p_title)) < 1 or char_length(p_title) > 120 then
    raise exception 'title length';
  end if;
  if p_instructions is null or char_length(p_instructions) < 1 or char_length(p_instructions) > 20000 then
    raise exception 'instructions length';
  end if;
  if jsonb_typeof(p_answers) is distinct from 'object' or octet_length(p_answers::text) > 20000 then
    raise exception 'answers must be a small object';
  end if;
  select e.status into st
  from public.entitlements e
  where e.user_id = uid
  for update;
  if st is distinct from 'active' then
    raise exception 'editing is not available on this account';
  end if;
  if not exists (
    select 1 from public.setups s
    where s.id = p_setup_id and s.user_id = uid and s.deleted_at is null
  ) then
    raise exception 'setup not found';
  end if;
  update public.setups
  set title = btrim(p_title), answers = p_answers, instructions = p_instructions, updated_at = now()
  where id = p_setup_id and user_id = uid and deleted_at is null;
  select coalesce(max(version_no), 0) + 1 into next_no
  from public.setup_versions
  where setup_id = p_setup_id;
  insert into public.setup_versions (setup_id, user_id, version_no, title, answers, instructions)
  values (p_setup_id, uid, next_no, btrim(p_title), p_answers, p_instructions);
  return next_no;
end;
$$;

create or replace function private.soft_delete_setup(p_setup_id uuid)
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare
  uid uuid := auth.uid();
begin
  if uid is null then
    raise exception 'not signed in';
  end if;
  update public.setups
  set deleted_at = now(), updated_at = now()
  where id = p_setup_id and user_id = uid and deleted_at is null;
  if not found then
    raise exception 'setup not found';
  end if;
end;
$$;

revoke all on function private.create_setup(text, text, jsonb, text) from public, anon, authenticated;
revoke all on function private.save_setup(uuid, text, jsonb, text) from public, anon, authenticated;
revoke all on function private.soft_delete_setup(uuid) from public, anon, authenticated;

create or replace function public.create_setup(p_task_id text, p_title text, p_answers jsonb, p_instructions text)
returns uuid
language plpgsql
security invoker
set search_path = ''
as $$
begin
  return private.create_setup(p_task_id, p_title, p_answers, p_instructions);
end;
$$;

create or replace function public.save_setup(p_setup_id uuid, p_title text, p_answers jsonb, p_instructions text)
returns integer
language plpgsql
security invoker
set search_path = ''
as $$
begin
  return private.save_setup(p_setup_id, p_title, p_answers, p_instructions);
end;
$$;

create or replace function public.soft_delete_setup(p_setup_id uuid)
returns void
language plpgsql
security invoker
set search_path = ''
as $$
begin
  perform private.soft_delete_setup(p_setup_id);
end;
$$;

revoke all on function public.create_setup(text, text, jsonb, text) from public, anon;
revoke all on function public.save_setup(uuid, text, jsonb, text) from public, anon;
revoke all on function public.soft_delete_setup(uuid) from public, anon;
grant execute on function public.create_setup(text, text, jsonb, text) to authenticated;
grant execute on function public.save_setup(uuid, text, jsonb, text) to authenticated;
grant execute on function public.soft_delete_setup(uuid) to authenticated;
grant execute on function private.create_setup(text, text, jsonb, text) to authenticated;
grant execute on function private.save_setup(uuid, text, jsonb, text) to authenticated;
grant execute on function private.soft_delete_setup(uuid) to authenticated;
grant usage on schema private to authenticated;
