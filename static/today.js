/* BotsDoThat Today: daily streak, "tried it" check-offs and "which apps do you use" flags.
   Everything stays in this browser (localStorage). No accounts, no network calls.
   Keys: bdt-days = {"YYYY-MM-DD": ["read" | "tried:<slug>", ...]}  (date = the weekday edition: Sat/Sun count toward Friday)
         bdt-apps = ["chatgpt", "claude", ...] */
(function () {
  'use strict';
  var d = document, LS = null;
  try { LS = window.localStorage; LS.setItem('bdt-t', '1'); LS.removeItem('bdt-t'); } catch (e) { LS = null; }
  if (!LS) return; // no storage: buttons stay hidden, the page still reads fine

  function iso(dt) { var m = dt.getMonth() + 1, a = dt.getDate(); return dt.getFullYear() + '-' + (m < 10 ? '0' : '') + m + '-' + (a < 10 ? '0' : '') + a; }
  function weekdayOf(dt) { var x = new Date(dt.getFullYear(), dt.getMonth(), dt.getDate()); while (x.getDay() === 0 || x.getDay() === 6) x.setDate(x.getDate() - 1); return x; }
  function prevWeekday(dt) { var x = new Date(dt.getFullYear(), dt.getMonth(), dt.getDate() - 1); while (x.getDay() === 0 || x.getDay() === 6) x.setDate(x.getDate() - 1); return x; }
  function load(k, def) { try { var v = JSON.parse(LS.getItem(k)); return v == null ? def : v; } catch (e) { return def; } }
  function save(k, v) { try { LS.setItem(k, JSON.stringify(v)); } catch (e) {} }

  var BDT = window.BDT = {
    today: function () { return weekdayOf(window.BDT_NOW ? new Date(window.BDT_NOW) : new Date()); },
    days: function () { return load('bdt-days', {}); },
    mark: function (what) {
      var days = BDT.days(), k = iso(BDT.today()), list = days[k] || [];
      if (list.indexOf(what) < 0) list.push(what);
      days[k] = list;
      var keys = Object.keys(days).sort(); while (keys.length > 120) delete days[keys.shift()]; // keep it small
      save('bdt-days', days); render();
    },
    has: function (what) { var l = BDT.days()[iso(BDT.today())] || []; return l.indexOf(what) >= 0; },
    streak: function () {
      // consecutive weekday editions with any check-off; today not done yet doesn't break it
      var days = BDT.days(), cur = BDT.today(), n = 0;
      if (!(days[iso(cur)] || []).length) cur = prevWeekday(cur);
      while ((days[iso(cur)] || []).length) { n++; cur = prevWeekday(cur); }
      return n;
    }
  };

  function render() {
    var done = (BDT.days()[iso(BDT.today())] || []);
    d.querySelectorAll('[data-mark]').forEach(function (b) {
      var what = b.getAttribute('data-mark') === 'tried' ? 'tried:' + b.getAttribute('data-slug') : 'read';
      b.hidden = false;
      var on = done.indexOf(what) >= 0;
      b.classList.toggle('is-done', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    d.querySelectorAll('.tried-note').forEach(function (x) { x.hidden = false; });
    var box = d.querySelector('.td-streak');
    if (box) {
      var n = BDT.streak();
      box.hidden = false;
      d.getElementById('streak-n').textContent = n;
      d.getElementById('streak-n').hidden = !n;
      d.getElementById('streak-lbl').textContent = n ? 'day streak' : 'Start a streak';
      var msg = d.getElementById('streak-msg');
      if (done.length) msg.textContent = 'Done for today. Come back tomorrow to keep it going. Weekends don\'t break it.';
      else if (n) msg.textContent = 'Read today\'s 3 or try the job to keep your streak.';
      else msg.textContent = 'Read today\'s 3 or try the job to start a streak. Weekends don\'t break it.';
      var sh = d.getElementById('streak-share'); if (sh) sh.hidden = !done.length;
    }
  }

  d.addEventListener('click', function (ev) {
    var b = ev.target.closest('[data-mark]');
    if (b) { BDT.mark(b.getAttribute('data-mark') === 'tried' ? 'tried:' + b.getAttribute('data-slug') : 'read'); return; }
    if (ev.target.id === 'streak-share') {
      var done = BDT.days()[iso(BDT.today())] || [];
      var txt = 'BotsDoThat Today, ' + BDT.today().toDateString().slice(4, 10) + '\n' +
        (done.indexOf('read') >= 0 ? '✅ Caught up on the 3 changes\n' : '') +
        (done.some(function (x) { return x.indexOf('tried:') === 0; }) ? '✅ Tried the job of the day\n' : '') +
        '🔥 ' + BDT.streak() + '-day streak\n' + location.origin + '/';
      var ok = function () { var s = d.getElementById('streak-copied'); if (s) s.textContent = ' Copied. Paste it anywhere.'; };
      if (navigator.clipboard) navigator.clipboard.writeText(txt).then(ok, function () {}); else ok();
    }
  });

  // "Which AI apps do you use?": flag items about those apps
  function applyApps() {
    var mine = load('bdt-apps', []), hits = 0;
    d.querySelectorAll('[data-app]').forEach(function (c) { var on = mine.indexOf(c.getAttribute('data-app')) >= 0; c.classList.toggle('on', on); c.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    d.querySelectorAll('[data-apps]').forEach(function (it) {
      var apps = (it.getAttribute('data-apps') || '').split(' '), you = apps.some(function (a) { return a && mine.indexOf(a) >= 0; });
      var badge = it.querySelector('.td-you'); if (badge) badge.hidden = !you;
      it.classList.toggle('is-yours', you);
      if (you && it.classList.contains('td-item')) hits++;
    });
    var yc = d.getElementById('you-count');
    if (yc) yc.textContent = mine.length ? (hits ? hits + ' affect apps you use' : 'none about apps you use') : '';
  }
  d.querySelectorAll('[data-app]').forEach(function (c) {
    c.addEventListener('click', function () {
      var mine = load('bdt-apps', []), a = c.getAttribute('data-app'), i = mine.indexOf(a);
      if (i >= 0) mine.splice(i, 1); else mine.push(a);
      save('bdt-apps', mine); applyApps();
    });
  });

  render(); applyApps();
})();
