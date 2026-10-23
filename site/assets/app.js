/* Vanilla JS: entry animation, reveals, card glow, copy, search/filter/sort. No dependencies. */
(function () {
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var norm = function (s) { return (s || '').toLowerCase().replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim(); };

  // ---- entry animation: max ~2.1s, skippable by click/key/scroll, never blocks content afterwards
  var intro = d.getElementById('intro');
  if (intro && root.classList.contains('intro-on')) {
    var done = function () { if (!intro.classList.contains('gone')) { intro.classList.add('gone'); root.classList.remove('intro-on'); } };
    var btn = intro.querySelector('.intro-skip'); if (btn) { btn.tabIndex = 0; btn.addEventListener('click', done); }
    intro.addEventListener('click', done);
    ['keydown', 'wheel', 'touchstart'].forEach(function (ev) { window.addEventListener(ev, done, { once: true, passive: true }); });
    setTimeout(done, 2100);
  }

  // ---- scroll reveals
  var rev = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }); }, { rootMargin: '0px 0px -8% 0px' });
    rev.forEach(function (el) { io.observe(el); });
  } else { rev.forEach(function (el) { el.classList.add('in'); }); }

  // ---- pointer glow on cards
  if (!reduce) d.addEventListener('pointermove', function (ev) {
    var c = ev.target.closest && ev.target.closest('.card'); if (!c) return;
    var r = c.getBoundingClientRect(); c.style.setProperty('--mx', (ev.clientX - r.left) + 'px'); c.style.setProperty('--my', (ev.clientY - r.top) + 'px');
  });

  // ---- copy buttons
  d.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var el = d.querySelector(b.getAttribute('data-copy')); if (!el) return;
      var text = el.innerText, ok = function () { b.textContent = 'Copied ✓'; b.classList.add('done'); setTimeout(function () { b.textContent = 'Copy'; b.classList.remove('done'); }, 1800); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(ok, fallback); else fallback();
      function fallback() { var r = d.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); try { d.execCommand('copy'); ok(); } catch (e) { b.textContent = 'Press Ctrl/⌘+C'; } }
    });
  });

  // ---- index: search + chips + sort
  var list = d.getElementById('cards');
  if (list) {
    var cards = Array.prototype.slice.call(list.children), qIn = d.getElementById('q2'), sortSel = d.getElementById('sort'), count = d.getElementById('count'), empty = d.querySelector('.empty');
    var params = new URLSearchParams(location.search), cat = params.get('cat') || 'all';
    if (params.get('q') && qIn) qIn.value = params.get('q');
    if (params.get('sort') && sortSel) sortSel.value = params.get('sort');
    var chipsEl = d.querySelectorAll('.chip[data-filter]');
    function apply() {
      var words = norm(qIn ? qIn.value : '').split(' ').filter(Boolean), shown = 0;
      cards.forEach(function (c) {
        var okCat = cat === 'all' || c.dataset.cat === cat, s = c.dataset.search;
        var okQ = words.every(function (w) { return s.indexOf(w) > -1 || (w.length > 3 && s.indexOf(w.replace(/s$/, '')) > -1); });
        c.hidden = !(okCat && okQ); if (!c.hidden) shown++;
      });
      chipsEl.forEach(function (ch) { var on = ch.dataset.filter === cat; ch.classList.toggle('on', on); ch.setAttribute('aria-pressed', on); });
      if (count) count.textContent = shown + ' of ' + cards.length + ' use cases';
      if (empty) empty.hidden = shown > 0;
    }
    function sort() {
      var m = sortSel ? sortSel.value : 'heat';
      cards.sort(function (a, b) {
        if (m === 'new') return a.dataset.added < b.dataset.added ? 1 : -1;
        if (m === 'easy') return (a.dataset.diff - b.dataset.diff) || (b.dataset.heat - a.dataset.heat);
        return b.dataset.heat - a.dataset.heat || (a.dataset.added < b.dataset.added ? 1 : -1);
      }).forEach(function (c) { list.appendChild(c); });
    }
    chipsEl.forEach(function (ch) { ch.addEventListener('click', function () { cat = ch.dataset.filter; apply(); }); });
    if (qIn) { qIn.addEventListener('input', apply); qIn.form.addEventListener('submit', function (e) { e.preventDefault(); apply(); }); }
    if (sortSel) sortSel.addEventListener('change', function () { sort(); apply(); });
    sort(); apply();
  }

  // ---- homepage instant search
  var hs = d.querySelector('[data-home-search]');
  if (hs) {
    var out = d.querySelector('.home-results'), idx = null;
    var load = function () { if (idx) return Promise.resolve(idx); var base = (d.querySelector('link[rel=stylesheet]').getAttribute('href') || '').replace(/assets\/style\.css$/, ''); return fetch(base + 'assets/search-index.json').then(function (r) { return r.json(); }).then(function (j) { idx = j; return j; }); };
    hs.addEventListener('focus', load, { once: true });
    hs.addEventListener('input', function () {
      var words = norm(hs.value).split(' ').filter(Boolean);
      if (!words.length) { out.innerHTML = ''; return; }
      load().then(function (ix) {
        var hits = ix.filter(function (it) { return words.every(function (w) { return it.s.indexOf(w) > -1 || (w.length > 3 && it.s.indexOf(w.replace(/s$/, '')) > -1); }); })
          .sort(function (a, b) { return b.h - a.h; }).slice(0, 6);
        var esc = function (s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
        out.innerHTML = hits.length ? '<ul class="glass">' + hits.map(function (h) { return '<li><a href="' + esc(h.u) + '"><span aria-hidden="true">' + h.i + '</span><span>' + esc(h.t) + '</span><span class="hr-cat">' + esc(h.c) + '</span></a></li>'; }).join('') + '</ul>'
          : '<p class="small muted">No match yet. Press Enter to search everything.</p>';
      });
    });
  }

  // ---- /news/ filter chips: All keeps the bento; other filters show a flat grid (Trending sorted by heat)
  var nb = d.getElementById('news-bento'), nr = d.getElementById('news-results');
  if (nb && nr) {
    var nchips = d.querySelector('.news-chips'), ne = d.getElementById('news-empty');
    var tiles = Array.prototype.slice.call(nb.querySelectorAll('.nt'));
    if (nchips) nchips.hidden = false;
    var setF = function (f) {
      nchips.querySelectorAll('.chip').forEach(function (c) { var on = c.dataset.nf === f; c.classList.toggle('on', on); c.setAttribute('aria-pressed', on); });
      if (f === 'all') { nb.hidden = false; nr.hidden = true; ne.hidden = true; return; }
      var pick = tiles.filter(function (t) { return f === 'trending' ? +t.dataset.heat > 0 : t.dataset.cat === f; });
      pick.sort(function (a, b) { return f === 'trending' ? b.dataset.heat - a.dataset.heat : (a.dataset.date < b.dataset.date ? 1 : -1); });
      nr.innerHTML = '';
      pick.forEach(function (t, i) { var c = t.cloneNode(true); c.removeAttribute('id'); c.style.setProperty('--i', i); nr.appendChild(c); });
      nb.hidden = true; nr.hidden = !pick.length; ne.hidden = !!pick.length;
    };
    nchips.addEventListener('click', function (ev) { var c = ev.target.closest('.chip'); if (c) setF(c.dataset.nf); });
  }

  // ---- "What will my bot cost?" calculator (full on /run-your-bots-for-less/, mini on the homepage)
  var RANK = { small: 0, mid: 1, flagship: 2 };
  var money = function (v) { if (v < 0.005) return 'under 1¢'; if (v >= 100) return '$' + Math.round(v).toLocaleString('en-US'); return '$' + v.toFixed(2); };
  var esc2 = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  d.querySelectorAll('[data-calc]').forEach(function (f) {
    var D = JSON.parse(f.querySelector('.calc-data').textContent), full = f.dataset.calc === 'full', out = f.querySelector('.calc-out');
    var el = function (n) { return f.elements[n]; };
    var preset = function (slug) { return D.presets.filter(function (p) { return p.slug === slug; })[0]; };
    function fill(p) {
      if (!p || !full) return;
      el('n').value = p.n; el('unit').value = p.unit; el('in').value = p['in']; el('out').value = p.out; el('size').value = 'custom';
      var w = f.querySelector('.calc-why'); if (w) w.textContent = p.why;
    }
    function nums() {
      if (!full) { var p = preset(el('bot').value) || D.presets[0]; return { rpm: p.n * D.units[p.unit], tin: p['in'], tout: p.out }; }
      var n = Math.max(0, parseFloat(el('n').value) || 0);
      return { rpm: n * (D.units[el('unit').value] || 1), tin: Math.max(0, parseFloat(el('in').value) || 0), tout: Math.max(0, parseFloat(el('out').value) || 0) };
    }
    function render() {
      var x = nums(), need = el('tier').value, batch = full && el('batch').checked;
      var on = full ? Array.prototype.map.call(f.querySelectorAll('input[name=m]:checked'), function (c) { return +c.value; }) : null;
      var rows = D.models.map(function (m, k) { return { m: m, k: k }; }).filter(function (r) {
        return RANK[r.m.t] >= RANK[need] && (!on || on.indexOf(r.k) > -1);
      }).map(function (r) {
        var disc = batch && D.batch.indexOf(r.m.p) > -1 ? 0.5 : 1;
        r.v = x.rpm * (x.tin * r.m.i + x.tout * r.m.o) / 1e6 * disc; r.b = disc < 1; return r;
      }).sort(function (a, b) { return a.v - b.v; });
      if (!rows.length) { out.innerHTML = '<p class="calc-empty">No model in this group. Tick more models or lower what the bot needs.</p>'; return; }
      var lo = rows[0], hi = rows[rows.length - 1], top = hi.v || 1;
      var tier = function (t) { return '<span class="calc-tier t-' + t + '">' + t + '</span>'; };
      var html = '<div class="calc-best"><p class="calc-best-k">Cheapest option that fits</p><p class="calc-best-v"><b>' + money(lo.v) + '</b><span>/month</span></p>' +
        '<p class="calc-best-m">' + esc2(lo.m.p) + ' · ' + esc2(lo.m.m) + ' ' + tier(lo.m.t) + (lo.b ? ' <span class="calc-tier">batch</span>' : '') + '</p>' +
        (rows.length > 1 ? '<p class="small muted">The priciest fit, ' + esc2(hi.m.p) + ' ' + esc2(hi.m.m) + ', would be ' + money(hi.v) + '/month' + (lo.v > 0 && hi.v / lo.v >= 2 ? ' (' + Math.round(hi.v / lo.v) + '× more)' : '') + '.</p>' : '') +
        (full ? '<p class="small muted">' + Math.round(x.rpm * 10) / 10 + ' runs a month · about ' + Math.round(x.rpm * x.tin).toLocaleString('en-US') + ' tokens in and ' + Math.round(x.rpm * x.tout).toLocaleString('en-US') + ' out.</p>' : '') + '</div>';
      var list = full ? rows : [lo].concat(rows.length > 2 ? [rows[Math.floor(rows.length / 2)]] : []).concat(rows.length > 1 ? [hi] : []);
      html += '<ol class="calc-list" aria-label="Monthly cost by model, cheapest first">' + list.map(function (r, i) {
        return '<li class="' + (r === lo ? 'is-best' : '') + '"><span class="calc-name"><b>' + esc2(r.m.p) + '</b> ' + esc2(r.m.m) + ' ' + tier(r.m.t) + '</span>' +
          '<span class="calc-bar" aria-hidden="true"><i style="width:' + Math.max(1.5, r.v / top * 100).toFixed(1) + '%"></i></span><span class="calc-v">' + money(r.v) + '</span></li>';
      }).join('') + '</ol>';
      out.innerHTML = html;
    }
    if (full) {
      var q = new URLSearchParams(location.search);
      if (q.get('bot') && preset(q.get('bot'))) { el('bot').value = q.get('bot'); fill(preset(q.get('bot'))); }
      var own = false;
      ['n', 'unit', 'in', 'out'].forEach(function (k) { if (q.get(k) !== null && el(k)) { el(k).value = q.get(k); own = true; } });
      if (own && !q.get('bot')) { el('bot').value = ''; el('size').value = 'custom'; var w0 = f.querySelector('.calc-why'); if (w0) w0.textContent = 'Your own numbers, from the link you opened.'; }
      if (q.get('tier') && RANK[q.get('tier')] !== undefined) el('tier').value = q.get('tier');
      if (q.get('batch') === '1') el('batch').checked = true;
      el('bot').addEventListener('change', function () { var p = preset(el('bot').value); if (p) fill(p); else { var w = f.querySelector('.calc-why'); if (w) w.textContent = 'Enter how often your bot runs and roughly how much it reads and writes each time.'; } render(); });
      el('size').addEventListener('change', function () { var z = D.sizes[el('size').value]; if (z) { el('in').value = z[0]; el('out').value = z[1]; el('bot').value = ''; } render(); });
      ['n', 'in', 'out'].forEach(function (k) { el(k).addEventListener('input', function () { if (k !== 'n') el('size').value = 'custom'; el('bot').value = el('bot').value && k === 'n' ? el('bot').value : (k === 'n' ? el('bot').value : ''); render(); }); });
    }
    f.addEventListener('change', render);
    render();
  });
  // ---- newsletter (Kit, double opt-in): submit in place with JSON; fall back to a normal POST if fetch is unavailable
  Array.prototype.forEach.call(d.querySelectorAll('form[data-nl]'), function (f) {
    if (!window.fetch || !window.FormData) return;
    var st = f.parentNode.querySelector('.nl-status'), btn = f.querySelector('button');
    var say = function (msg, bad) { if (!st) return; st.textContent = msg; st.hidden = false; st.classList.toggle('nl-bad', !!bad); };
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (btn) btn.disabled = true;
      fetch(f.action, { method: 'POST', body: new FormData(f), headers: { Accept: 'application/json' } })
        .then(function (r) { return r.json().catch(function () { return { status: r.ok ? 'success' : 'failed' }; }); })
        .then(function (j) {
          if (j && j.status === 'success') { f.hidden = true; say('Almost done. Check your email to confirm your subscription.'); }
          else { if (btn) btn.disabled = false; var m = j && j.errors && j.errors.messages; say((m && m.length ? m.join(' ') : 'That didn\u2019t work.') + ' Please check the address and try again.', true); }
        })
        .catch(function () { f.removeAttribute('data-nl'); HTMLFormElement.prototype.submit.call(f); });
    });
  });
})();
