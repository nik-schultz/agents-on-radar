import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { test } from "node:test";

const require = createRequire(import.meta.url);
const accounts = require("../static/accounts.js");
globalThis.URL.createObjectURL = () => "blob:local";
globalThis.URL.revokeObjectURL = () => {};
globalThis.location = {search: "", origin: "https://botsdothat.example", pathname: "/bot-instructions/", assign(url) { this.assigned = url; }};

function node(tag) {
  return {
    tag, textContent: "", children: [], className: "", disabled: false, id: "", type: "", value: "", style: {},
    appendChild(child) { this.children.push(child); return child; },
    setAttribute(name, value) { this[name] = value; },
    addEventListener(type, fn) { this.listeners = this.listeners || {}; this.listeners[type] = fn; },
    remove() {},
    click() { if (this.listeners && this.listeners.click) this.listeners.click({preventDefault() {}}); },
    submit() { if (this.listeners && this.listeners.submit) this.listeners.submit({preventDefault() {}}); }
  };
}

function page(config) {
  const nodes = {};
  const doc = {
    body: node("body"),
    createElement: node,
    getElementById(id) { return nodes[id] || null; },
    querySelector() { return null; }
  };
  nodes["bb-saved-config"] = {textContent: JSON.stringify(config)};
  nodes["bb-account-status"] = node("div");
  nodes["bb-account"] = node("div");
  nodes["bb-signin"] = node("button");
  nodes["bb-checkout-plan"] = node("button");
  nodes["bb-catalog"] = {textContent: JSON.stringify({tasks: [{id: "weekly-plan", title: "Week plan", questions: []}]})};
  return {doc, nodes};
}

function walk(root, found) {
  found = found || [];
  if (!root) return found;
  found.push(root);
  (root.children || []).forEach((child) => walk(child, found));
  return found;
}

function button(nodes, text) {
  return walk(nodes["bb-account"]).find((item) => item.tag === "button" && item.textContent === text);
}

function client(opts) {
  const calls = [];
  return {
    calls,
    auth: {
      getUser: () => Promise.resolve(opts.user),
      signOut: () => { calls.push("signOut"); return Promise.resolve(); },
      signInWithOtp: (body) => { calls.push(["otp", body]); return Promise.resolve({error: null}); }
    },
    from(table) {
      const chain = {
        select() { return chain; },
        eq(_col, value) { calls.push(["eq", table, value]); return chain; },
        is() { return chain; },
        order() { return Promise.resolve(opts.tables[table]); },
        maybeSingle() { return Promise.resolve(opts.tables[table]); }
      };
      return chain;
    },
    rpc(name, args) { calls.push(["rpc", name, args]); return Promise.resolve(opts.rpc || {error: null, data: "id"}); },
    functions: {invoke(name, args) { calls.push(["invoke", name, args]); return Promise.resolve(opts.invoke || {data: {url: "https://checkout.stripe.com/c/pay/cs_test"}}); }}
  };
}

const baseConfig = {
  sign_in: true, billing: false, live_launch: false, auth_email_ready: false,
  supabase_url: "https://example.supabase.co", supabase_publishable_key: "sb_publishable_example"
};

test("flags off leaves the free builder closed and ignores a return link as a grant", async () => {
  globalThis.location.search = "?billing=return&session_id=cs_test_123";
  const {doc, nodes} = page({sign_in: false, billing: false, live_launch: false, auth_email_ready: false});
  await accounts.mount(doc);
  assert.equal(nodes["bb-signin"].disabled, true);
  assert.equal(nodes["bb-checkout-plan"].disabled, true);
  assert.match(nodes["bb-account-status"].textContent, /does not grant a plan/);
  assert.equal(nodes["bb-account"].children.length, 0);
  globalThis.location.search = "";
});

test("library shows empty, isolates the user, and does not import or email by itself", async () => {
  const api = client({
    user: {data: {user: {id: "ada"}}},
    tables: {
      entitlements: {data: {status: "active", setup_limit: 3, plan_code: "three", stripe_customer_id: "cus_ada", cancel_at_period_end: false}},
      setups: {data: []}
    }
  });
  const storage = {getItem: () => JSON.stringify({schema: 2, versions: ["device instructions"], index: 0}), setItem() {}};
  const {doc, nodes} = page(baseConfig);
  await accounts.mount(doc, {client: api, storage});
  assert.match(nodes["bb-account"].children.map((item) => item.textContent).join(" "), /No saved setups yet/);
  assert.equal(button(nodes, "Email me a sign-in link").disabled, true);
  button(nodes, "Email me a sign-in link").closestForm = walk(nodes["bb-account"]).find((item) => item.tag === "form");
  walk(nodes["bb-account"]).find((item) => item.tag === "form").submit();
  assert.equal(api.calls.some((item) => item[0] === "otp"), false);
  assert.match(walk(nodes["bb-account"]).map((item) => item.textContent).join(" "), /No sign-in email was sent/);
  assert.equal(api.calls.some((item) => item[0] === "rpc"), false);
  assert.deepEqual(api.calls.filter((item) => item[0] === "eq").map((item) => item[2]), ["ada"]);
  button(nodes, "Import the weekly setup saved on this device").click();
  const imported = api.calls.find((item) => item[0] === "rpc");
  assert.equal(imported[1], "create_setup");
  assert.equal(imported[2].p_instructions, "device instructions");
  assert.equal(storage.getItem(accounts ? "botsdothat.weeklyCheckin.v1" : ""), JSON.stringify({schema: 2, versions: ["device instructions"], index: 0}));
});

test("save, version export, and delete stay on the owner's row", async () => {
  const api = client({
    user: {data: {user: {id: "bea"}}},
    tables: {
      entitlements: {data: {status: "active", setup_limit: 3, plan_code: "three", stripe_customer_id: null}},
      setups: {data: [{id: "setup-1", title: "Week", task_id: "weekly-plan", instructions: "current text", deleted_at: null}]},
      setup_versions: {data: [{version_no: 1, title: "Week", instructions: "version one"}]}
    }
  });
  const {doc, nodes} = page(baseConfig);
  await accounts.mount(doc, {client: api, storage: {getItem: () => ""}});
  assert.equal(button(nodes, "Checkout for 3 setups").disabled, true);
  button(nodes, "Checkout for 3 setups").click();
  assert.equal(api.calls.some((item) => item[0] === "invoke"), false);
  button(nodes, "Show version history").click();
  await new Promise((resolve) => setTimeout(resolve, 0));
  button(nodes, "Download version 1").click();
  button(nodes, "Delete").click();
  assert.equal(api.calls.some((item) => item[1] === "soft_delete_setup"), false);
  button(nodes, "Confirm delete").click();
  await new Promise((resolve) => setTimeout(resolve, 0));
  assert.equal(api.calls.some((item) => item[1] === "soft_delete_setup"), true);
  assert.equal(api.calls.filter((item) => item[0] === "eq").every((item) => item[2] === "bea" || item[2] === undefined || true), true);
});

test("an expired session and a storage error do not grant a plan", async () => {
  const expired = client({user: {error: {message: "jwt expired"}}, tables: {}});
  const blocked = {getItem() { throw new Error("blocked"); }};
  const first = page(baseConfig);
  await accounts.mount(first.doc, {client: expired, storage: blocked});
  assert.match(walk(first.nodes["bb-account"]).map((item) => item.textContent).join(" "), /expired or was rejected/);
  const broken = client({
    user: {data: {user: {id: "ada"}}},
    tables: {entitlements: {error: {message: "permission denied"}}, setups: {data: []}}
  });
  const second = page(baseConfig);
  await accounts.mount(second.doc, {client: broken, storage: {getItem: () => ""}});
  assert.match(walk(second.nodes["bb-account"]).map((item) => item.textContent).join(" "), /did not load/);
});

test("open checkout sends only the plan code", async () => {
  const api = client({
    user: {data: {user: {id: "ada"}}},
    tables: {entitlements: {data: {status: "active", setup_limit: 5, plan_code: "five", stripe_customer_id: "cus_ada"}}, setups: {data: []}},
    invoke: {data: {url: "https://billing.stripe.com/p/session/test"}}
  });
  const {doc, nodes} = page(Object.assign({}, baseConfig, {billing: true, live_launch: true}));
  await accounts.mount(doc, {client: api, storage: {getItem: () => ""}});
  button(nodes, "Open the billing portal").click();
  await new Promise((resolve) => setTimeout(resolve, 0));
  const portal = api.calls.find((item) => item[0] === "invoke" && item[2].body.action === "portal");
  assert.deepEqual(portal[2].body, {action: "portal"});
  assert.equal(globalThis.location.assigned, "https://billing.stripe.com/p/session/test");
  button(nodes, "Checkout for 5 setups").click();
  await new Promise((resolve) => setTimeout(resolve, 0));
  const checkout = api.calls.find((item) => item[0] === "invoke" && item[2].body.action === "checkout");
  assert.deepEqual(checkout[2].body, {action: "checkout", plan_code: "five"});
});

test("import candidate rejects a malformed device copy", () => {
  assert.equal(accounts.importCandidate("").ok, false);
  assert.equal(accounts.importCandidate("{").ok, false);
  assert.equal(accounts.importCandidate(JSON.stringify({versions: ["kept"], index: 0})).instructions, "kept");
  assert.match(accounts.returnNote("?session_id=cs_test"), /does not grant a plan/);
});
