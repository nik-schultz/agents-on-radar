/* Saved setups. The default build leaves sign-in and checkout disabled.
   A checkout return link never grants a plan. Rendering uses textContent only.
   Customer sign-in email stays off until auth_email_ready is true, which this repo rejects. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (typeof document !== "undefined") {
    api.mount(document, root.__SAVED_SETUPS_TEST__ || null);
  }
  root.SavedSetups = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";
  var SUPABASE_URL = "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.49.1/+esm";
  var LOCAL_KEY = "botsdothat.weeklyCheckin.v1";

  function accessFromRow(entitlement, savedCount) {
    var status = entitlement && entitlement.status;
    var limit = entitlement ? (entitlement.setup_limit || 0) : 0;
    var active = status === "active";
    return {
      can_read: !!entitlement,
      can_export: !!entitlement,
      can_edit: active,
      can_create: active && savedCount < limit,
      can_delete: !!entitlement
    };
  }

  function importCandidate(raw) {
    if (raw == null || raw === "") return {ok: false, reason: "empty"};
    var data;
    try { data = JSON.parse(raw); }
    catch (err) { return {ok: false, reason: "unreadable"}; }
    if (!data || !Array.isArray(data.versions) || typeof data.index !== "number" || data.index < 0 || data.index >= data.versions.length) {
      return {ok: false, reason: "unreadable"};
    }
    var text = data.versions[data.index];
    if (typeof text !== "string" || !text) return {ok: false, reason: "unreadable"};
    return {
      ok: true,
      task_id: "weekly-plan",
      title: "Weekly setup from this device",
      instructions: text,
      answers: {source: "device-import"}
    };
  }

  function el(doc, tag, text) {
    var node = doc.createElement(tag);
    if (text != null) node.textContent = text;
    return node;
  }

  function currentTaskId(doc) {
    var picked = doc.querySelector('input[name="bb-task"]:checked');
    return picked ? picked.value : "";
  }

  function collectAnswers(doc, task) {
    var answers = {};
    task.questions.forEach(function (q) {
      if (q.type === "choice") {
        var choice = doc.querySelector('input[name="bb-q-' + q.id + '"]:checked');
        answers[q.id] = choice ? choice.value : "";
      } else if (q.type === "check") {
        var box = doc.getElementById("bb-q-" + q.id);
        answers[q.id] = !!(box && box.checked);
      } else {
        var field = doc.getElementById("bb-q-" + q.id);
        answers[q.id] = field ? field.value : "";
      }
    });
    return answers;
  }

  function download(text, filename, doc) {
    var blob = new Blob([text], {type: "text/plain;charset=utf-8"});
    var link = doc.createElement("a");
    var url = URL.createObjectURL(blob);
    link.href = url;
    link.download = filename;
    doc.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  }

  function returnNote(search) {
    if (/[?&](session_id=|billing=return|billing=cancel)/.test(search || "")) {
      return "A checkout return link does not turn on saving. This page does not grant a plan from that link.";
    }
    return "";
  }

  function mount(doc, testHooks) {
    var raw = doc.getElementById("bb-saved-config");
    var status = doc.getElementById("bb-account-status");
    var box = doc.getElementById("bb-account");
    var sign = doc.getElementById("bb-signin");
    var pay = doc.getElementById("bb-checkout-plan");
    if (!raw || !box) return;
    var config = JSON.parse(raw.textContent);
    if (sign) { sign.disabled = true; sign.setAttribute("aria-disabled", "true"); }
    if (pay) { pay.disabled = true; pay.setAttribute("aria-disabled", "true"); }
    var returned = returnNote(typeof location !== "undefined" ? location.search : "");
    if (returned && status) status.textContent = returned;
    if (!config.sign_in && !config.billing) return;
    box.appendChild(el(doc, "p", config.live_launch
      ? "Accounts are configured for this build."
      : "Development configuration. This is not the live paid service. Do not enter a real card."));
    if (!config.sign_in || !config.supabase_url || !config.supabase_publishable_key) {
      if (status) status.textContent = "Sign-in is not configured. The free builder is still only in this tab.";
      return;
    }
    var hooks = testHooks || {};
    return startClient(doc, box, status, config, hooks).catch(function (err) {
      if (status) status.textContent = "Sign-in did not load. " + (err && err.message ? err.message : "The account service did not answer.") + " Nothing was saved.";
    });
  }

  function startClient(doc, box, status, config, hooks) {
    var ready = hooks.client ? Promise.resolve({createClient: function () { return hooks.client; }}) : import(SUPABASE_URL);
    return ready.then(function (mod) {
      var client = hooks.client || mod.createClient(config.supabase_url, config.supabase_publishable_key);
      var catalog = JSON.parse(doc.getElementById("bb-catalog").textContent);
      var storage = hooks.storage || (typeof localStorage !== "undefined" ? localStorage : null);
      var note = el(doc, "p", "Loading your library…");
      note.setAttribute("role", "status");
      box.appendChild(note);
      var form = doc.createElement("form");
      var label = el(doc, "label", "Email for a sign-in link");
      label.htmlFor = "bb-signin-email";
      var input = doc.createElement("input");
      input.type = "email";
      input.id = "bb-signin-email";
      input.autocomplete = "email";
      input.required = true;
      var submit = el(doc, "button", "Email me a sign-in link");
      submit.type = "submit";
      submit.className = "btn";
      if (!config.auth_email_ready) {
        submit.disabled = true;
        submit.setAttribute("aria-disabled", "true");
        submit.style.opacity = "0.55";
        input.disabled = true;
      }
      form.appendChild(label);
      form.appendChild(input);
      form.appendChild(submit);
      var emailNote = el(doc, "p", config.auth_email_ready
        ? "The sign-in link goes only to the address you type. No password is stored."
        : "Customer sign-in email is not available. The built-in mail service is limited to organization team members and about 2 messages an hour, so it cannot sign up or recover a customer. Nothing is sent.");
      form.appendChild(emailNote);
      box.appendChild(form);
      var library = doc.createElement("div");
      library.id = "bb-library";
      box.appendChild(library);
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        if (!config.auth_email_ready) {
          note.textContent = "No sign-in email was sent. Customer email delivery is not approved.";
          return;
        }
        note.textContent = "Sending a sign-in link…";
        client.auth.signInWithOtp({
          email: input.value,
          options: {emailRedirectTo: location.origin + location.pathname}
        }).then(function (res) {
          if (res.error) note.textContent = res.error.message;
          else note.textContent = "Check that inbox for the sign-in link. This page did not store a password.";
        });
      });
      function paint(user) {
        library.textContent = "";
        if (!user) {
          library.appendChild(el(doc, "p", "Not signed in. The free builder on this page still works."));
          return Promise.resolve();
        }
        note.textContent = "Loading your library…";
        library.appendChild(el(doc, "p", "Signed in. A saved setup is instructions for your chat app, not a bot this site runs."));
        var outBtn = el(doc, "button", "Sign out");
        outBtn.type = "button";
        outBtn.className = "btn btn-ghost";
        outBtn.addEventListener("click", function () {
          client.auth.signOut().then(function () { note.textContent = "Signed out."; paint(null); });
        });
        library.appendChild(outBtn);
        return client.from("entitlements").select("status,setup_limit,plan_code,stripe_customer_id,cancel_at_period_end,current_period_end").eq("user_id", user.id).maybeSingle().then(function (entRes) {
          return client.from("setups").select("id,title,task_id,instructions,updated_at,deleted_at").is("deleted_at", null).order("updated_at", {ascending: false}).then(function (listRes) {
            if (entRes.error || listRes.error) {
              note.textContent = "The library did not load. " + (entRes.error || listRes.error).message + " Nothing new was saved.";
              return;
            }
            var rows = listRes.data || [];
            var rights = accessFromRow(entRes.data, rows.length);
            note.textContent = rows.length ? "Your saved setups are listed below." : "No saved setups yet. The free builder on this page still works.";
            if (entRes.data && entRes.data.cancel_at_period_end && entRes.data.status === "active") {
              library.appendChild(el(doc, "p", "This subscription is scheduled to stop at the end of the current period. Saving stays available until then. This page does not promise a refund."));
            }
            library.appendChild(el(doc, "p", rights.can_create
              ? "You can save another setup."
              : "New saves are blocked. Existing setups stay here and can be exported."));
            addCheckout(doc, library, note, client, config, entRes.data);
            addImport(doc, library, note, client, storage, rights, function () { paint(user); });
            if (rights.can_create || rights.can_edit) {
              var save = el(doc, "button", "Save the instructions in the box");
              save.type = "button";
              save.className = "btn";
              save.addEventListener("click", function () { saveCurrent(client, catalog, doc, note, rights, paint, user); });
              library.appendChild(save);
            }
            if (!rows.length) library.appendChild(el(doc, "p", "No saved setups yet."));
            rows.forEach(function (row) {
              library.appendChild(setupBlock(doc, client, catalog, row, rights, note, function () { paint(user); }));
            });
          });
        }).catch(function (err) {
          note.textContent = "The library did not load. " + (err && err.message ? err.message : "The account service did not answer.");
        });
      }
      return client.auth.getUser().then(function (res) {
        if (res.error || !res.data || !res.data.user) {
          note.textContent = "Your sign-in expired or was rejected. Sign in again. Nothing was granted from this page.";
          if (res.error) client.auth.signOut();
          return paint(null);
        }
        return paint(res.data.user);
      }).catch(function () {
        note.textContent = "Your sign-in expired or was rejected. Sign in again. Nothing was granted from this page.";
        return paint(null);
      }).then(function () { return client; });
    });
  }

  function addCheckout(doc, library, note, client, config, entitlement) {
    var open = !!(config.billing && config.live_launch);
    ["three", "five"].forEach(function (plan) {
      var button = el(doc, "button", plan === "three" ? "Checkout for 3 setups" : "Checkout for 5 setups");
      button.type = "button";
      button.className = "btn btn-sm";
      button.disabled = !open;
      if (!open) {
        button.setAttribute("aria-disabled", "true");
        button.style.opacity = "0.55";
      }
      button.addEventListener("click", function () {
        if (!open) {
          note.textContent = "Checkout is closed until the payment flow is verified. No plan was granted.";
          return;
        }
        note.textContent = "Opening checkout…";
        client.functions.invoke("billing", {body: {action: "checkout", plan_code: plan}}).then(function (res) {
          if (res.error || !res.data || !res.data.url) {
            note.textContent = "Checkout did not open. No plan was granted.";
            return;
          }
          location.assign(res.data.url);
        });
      });
      library.appendChild(button);
    });
    var portal = el(doc, "button", "Open the billing portal");
    portal.type = "button";
    portal.className = "btn btn-sm btn-ghost";
    var portalOpen = open && entitlement && entitlement.stripe_customer_id;
    portal.disabled = !portalOpen;
    if (!portalOpen) {
      portal.setAttribute("aria-disabled", "true");
      portal.style.opacity = "0.55";
    }
    portal.addEventListener("click", function () {
      if (!portalOpen) {
        note.textContent = "The billing portal is closed. No plan was granted.";
        return;
      }
      client.functions.invoke("billing", {body: {action: "portal"}}).then(function (res) {
        if (res.error || !res.data || !res.data.url) {
          note.textContent = "The billing portal did not open.";
          return;
        }
        location.assign(res.data.url);
      });
    });
    library.appendChild(portal);
  }

  function addImport(doc, library, note, client, storage, rights, done) {
    var raw = "";
    try { raw = storage ? storage.getItem(LOCAL_KEY) : ""; }
    catch (err) { raw = ""; }
    var candidate = importCandidate(raw);
    if (!candidate.ok) return;
    var button = el(doc, "button", "Import the weekly setup saved on this device");
    button.type = "button";
    button.className = "btn btn-sm";
    button.addEventListener("click", function () {
      if (!rights.can_create) {
        note.textContent = "This account cannot save another setup. The copy on this device was left where it is.";
        return;
      }
      client.rpc("create_setup", {
        p_task_id: candidate.task_id,
        p_title: candidate.title,
        p_answers: candidate.answers,
        p_instructions: candidate.instructions
      }).then(function (res) {
        note.textContent = res.error ? res.error.message : "Imported into your account. The copy on this device is still there. This site will not run it.";
        if (!res.error) done();
      });
    });
    library.appendChild(button);
  }

  function setupBlock(doc, client, catalog, row, rights, note, done) {
    var block = doc.createElement("article");
    block.className = "glass bb-sample";
    block.appendChild(el(doc, "h3", row.title));
    block.appendChild(el(doc, "p", row.task_id));
    var exp = el(doc, "button", "Download this setup");
    exp.type = "button";
    exp.className = "btn btn-sm";
    exp.addEventListener("click", function () { download(row.instructions, row.task_id + "-setup.txt", doc); });
    block.appendChild(exp);
    if (rights.can_edit) {
      var update = el(doc, "button", "Replace with the instructions in the box");
      update.type = "button";
      update.className = "btn btn-sm";
      update.addEventListener("click", function () {
        var task = null;
        catalog.tasks.forEach(function (item) { if (item.id === currentTaskId(doc)) task = item; });
        if (!task || !root.BotBuilder) { note.textContent = "Choose the same kind of task and write instructions first."; return; }
        var built = root.BotBuilder.generate(task.id, collectAnswers(doc, task));
        if (!built.ok) { note.textContent = "Fix the builder fields before saving a new version."; return; }
        client.rpc("save_setup", {p_setup_id: row.id, p_title: task.title.slice(0, 120), p_answers: built.answers, p_instructions: built.text}).then(function (res) {
          note.textContent = res.error ? res.error.message : "Saved a new version in your account. Older versions stay in the history.";
          if (!res.error) done();
        });
      });
      block.appendChild(update);
    }
    var history = el(doc, "button", "Show version history");
    history.type = "button";
    history.className = "btn btn-sm btn-ghost";
    history.addEventListener("click", function () {
      client.from("setup_versions").select("version_no,title,instructions,created_at").eq("setup_id", row.id).order("version_no", {ascending: false}).then(function (res) {
        if (res.error) { note.textContent = res.error.message; return; }
        var list = el(doc, "ul", "");
        (res.data || []).forEach(function (version) {
          var item = el(doc, "li", "Version " + version.version_no + ": " + version.title);
          var older = el(doc, "button", "Download version " + version.version_no);
          older.type = "button";
          older.className = "btn btn-sm btn-ghost";
          older.addEventListener("click", function () { download(version.instructions, "setup-v" + version.version_no + ".txt", doc); });
          item.appendChild(older);
          list.appendChild(item);
        });
        block.appendChild(list);
      });
    });
    block.appendChild(history);
    if (rights.can_delete) {
      var del = el(doc, "button", "Delete");
      del.type = "button";
      del.className = "btn btn-sm btn-ghost";
      del.addEventListener("click", function () {
        var confirm = el(doc, "button", "Confirm delete");
        confirm.type = "button";
        confirm.className = "btn btn-sm";
        confirm.addEventListener("click", function () {
          client.rpc("soft_delete_setup", {p_setup_id: row.id}).then(function (res) {
            note.textContent = res.error ? res.error.message : "Deleted from your library. It was not sent anywhere else.";
            if (!res.error) done();
          });
        });
        block.appendChild(confirm);
      });
      block.appendChild(del);
    }
    return block;
  }

  function saveCurrent(client, catalog, doc, note, rights, paint, user) {
    var taskId = currentTaskId(doc);
    var task = null;
    catalog.tasks.forEach(function (item) { if (item.id === taskId) task = item; });
    if (!task || !root.BotBuilder) {
      note.textContent = "Choose a task and write instructions before saving.";
      return;
    }
    var built = root.BotBuilder.generate(task.id, collectAnswers(doc, task));
    if (!built.ok) {
      note.textContent = "Fix the builder fields before saving. Nothing was stored.";
      return;
    }
    if (!rights.can_create) {
      note.textContent = "This account cannot save another setup. You can still download the instructions.";
      return;
    }
    client.rpc("create_setup", {
      p_task_id: task.id,
      p_title: task.title.slice(0, 120),
      p_answers: built.answers,
      p_instructions: built.text
    }).then(function (res) {
      note.textContent = res.error ? res.error.message : "Saved in your account. This site will not run it.";
      if (!res.error) paint(user);
    });
  }

  return {accessFromRow: accessFromRow, importCandidate: importCandidate, returnNote: returnNote, mount: mount, collectAnswers: collectAnswers};
});
