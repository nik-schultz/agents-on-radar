/* Saved setups. The default build leaves sign-in and checkout disabled.
   A checkout return link never grants a plan. Rendering uses textContent only. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (typeof document !== "undefined") api.mount(document);
  root.SavedSetups = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";
  var SUPABASE_URL = "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.49.1/+esm";

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

  function download(text, filename) {
    var blob = new Blob([text], {type: "text/plain;charset=utf-8"});
    var link = document.createElement("a");
    var url = URL.createObjectURL(blob);
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  }

  function mount(doc) {
    var raw = doc.getElementById("bb-saved-config");
    var status = doc.getElementById("bb-account-status");
    var box = doc.getElementById("bb-account");
    var sign = doc.getElementById("bb-signin");
    var pay = doc.getElementById("bb-checkout-plan");
    if (!raw || !box) return;
    var config = JSON.parse(raw.textContent);
    if (sign) { sign.disabled = true; sign.setAttribute("aria-disabled", "true"); }
    if (pay) { pay.disabled = true; pay.setAttribute("aria-disabled", "true"); }
    if (typeof location !== "undefined" && /[?&]session_id=/.test(location.search) && status) {
      status.textContent = "A checkout return link does not turn on saving. This page does not grant a plan from that link.";
    }
    if (!config.sign_in && !config.billing) return;
    box.appendChild(el(doc, "p", config.live_launch
      ? "Accounts are configured for this build."
      : "Development configuration. This is not the live paid service. Do not enter a real card."));
    if (!config.sign_in || !config.supabase_url || !config.supabase_publishable_key) {
      if (status) status.textContent = "Sign-in is not configured. The free builder is still only in this tab.";
      return;
    }
    startClient(doc, box, status, config).catch(function (err) {
      if (status) status.textContent = "Sign-in did not load. " + (err && err.message ? err.message : "The account service did not answer.") + " Nothing was saved.";
    });
  }

  function startClient(doc, box, status, config) {
    return import(SUPABASE_URL).then(function (mod) {
      var client = mod.createClient(config.supabase_url, config.supabase_publishable_key);
      var catalog = JSON.parse(doc.getElementById("bb-catalog").textContent);
      var note = el(doc, "p", "");
      note.setAttribute("role", "status");
      box.appendChild(note);
      var form = doc.createElement("form");
      var label = el(doc, "label", "Email for the sign-in link");
      label.htmlFor = "bb-signin-email";
      var input = doc.createElement("input");
      input.type = "email";
      input.id = "bb-signin-email";
      input.autocomplete = "email";
      input.required = true;
      var submit = el(doc, "button", "Email me a sign-in link");
      submit.type = "submit";
      submit.className = "btn";
      form.appendChild(label);
      form.appendChild(input);
      form.appendChild(submit);
      box.appendChild(form);
      var library = doc.createElement("div");
      box.appendChild(library);
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
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
        if (!user) return;
        library.appendChild(el(doc, "p", "Signed in. A saved setup is instructions for your chat app, not a bot this site runs."));
        var outBtn = el(doc, "button", "Sign out");
        outBtn.type = "button";
        outBtn.className = "btn btn-ghost";
        outBtn.addEventListener("click", function () {
          client.auth.signOut().then(function () { note.textContent = "Signed out."; paint(null); });
        });
        library.appendChild(outBtn);
        client.from("entitlements").select("status,setup_limit,plan_code").eq("user_id", user.id).maybeSingle().then(function (entRes) {
          client.from("setups").select("id,title,task_id,instructions,updated_at,deleted_at").is("deleted_at", null).order("updated_at", {ascending: false}).then(function (listRes) {
            if (entRes.error || listRes.error) {
              note.textContent = (entRes.error || listRes.error).message;
              return;
            }
            var rows = listRes.data || [];
            var rights = accessFromRow(entRes.data, rows.length);
            library.appendChild(el(doc, "p", rights.can_create
              ? "You can save another setup."
              : "New saves are blocked. Existing setups stay here and can be exported."));
            if (rights.can_create || rights.can_edit) {
              var save = el(doc, "button", "Save the instructions in the box");
              save.type = "button";
              save.className = "btn";
              save.addEventListener("click", function () { saveCurrent(client, catalog, doc, note, rights, paint, user); });
              library.appendChild(save);
            }
            rows.forEach(function (row) {
              var block = doc.createElement("div");
              block.className = "glass bb-sample";
              block.appendChild(el(doc, "h3", row.title));
              block.appendChild(el(doc, "p", row.task_id));
              var exp = el(doc, "button", "Download this setup");
              exp.type = "button";
              exp.className = "btn btn-sm";
              exp.addEventListener("click", function () { download(row.instructions, row.task_id + "-setup.txt"); });
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
                    if (!res.error) paint(user);
                  });
                });
                block.appendChild(update);
              }
              var history = el(doc, "button", "Show version history");
              history.type = "button";
              history.className = "btn btn-sm btn-ghost";
              history.addEventListener("click", function () {
                client.from("setup_versions").select("version_no,title,created_at").eq("setup_id", row.id).order("version_no", {ascending: false}).then(function (res) {
                  if (res.error) { note.textContent = res.error.message; return; }
                  var list = el(doc, "ul", "");
                  (res.data || []).forEach(function (version) {
                    list.appendChild(el(doc, "li", "Version " + version.version_no + ": " + version.title));
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
                  client.rpc("soft_delete_setup", {p_setup_id: row.id}).then(function (res) {
                    note.textContent = res.error ? res.error.message : "Deleted from your library. It was not sent anywhere else.";
                    if (!res.error) paint(user);
                  });
                });
                block.appendChild(del);
              }
              library.appendChild(block);
            });
          });
        });
      }
      client.auth.getUser().then(function (res) {
        if (res.error) {
          note.textContent = "Your sign-in expired or was rejected. Sign in again. Nothing was granted from this page.";
          client.auth.signOut();
          return;
        }
        paint(res.data.user);
      });
      return client;
    });
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
    var title = task.title.slice(0, 120);
    if (!rights.can_create) {
      note.textContent = "This account cannot save another setup. You can still download the instructions.";
      return;
    }
    client.rpc("create_setup", {
      p_task_id: task.id,
      p_title: title,
      p_answers: built.answers,
      p_instructions: built.text
    }).then(function (res) {
      note.textContent = res.error ? res.error.message : "Saved in your account. This site will not run it.";
      if (!res.error) paint(user);
    });
  }

  return {accessFromRow: accessFromRow, mount: mount, collectAnswers: collectAnswers};
});
