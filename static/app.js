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
    var chipsEl = d.querySelectorAll('.chip');
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
})();
