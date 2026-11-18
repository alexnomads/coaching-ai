/* AI Coach Alex — pinned scroll scenes (homepage, shared by all languages).
 *
 * Markup contract (see index.html):
 *   <section class="scene" style="--len:260" data-wall="ink|forest|lime|cream" data-nav="dark|light">
 *     <div class="stage"> ... </div>
 *   </section>
 * Scroll progress p (0..1) of each scene drives elements inside it:
 *   data-words="a b"      word-by-word reveal between a and b
 *   data-letters="a b"    letter-by-letter reveal (giant words)
 *   data-show="a b"       fade + rise
 *   data-on="a b"         fade only
 *   data-swap="a b c d"   fade in a..b, out c..d
 *   data-count="a b"      count up to data-to (data-pre / data-suf)
 *   data-scale="a b from to"  scale (transform) between from and to
 *   .laptop[data-type="a b"]  lines type onto the screen, keys press, Enter at each line end
 *   .laptop[data-keys="a b"]  keys press while a<p<b; data-enters="x y z" press Enter around those points
 *   data-nav-steps="0:dark 0.66:light"  nav colour changes inside one scene
 * Normal (non-pinned) sections can carry data-wall / data-nav too.
 * Everything reverses on scroll-up. prefers-reduced-motion: every scene renders its final state, no pinning.
 */
(function () {
  'use strict';
  var root = document.documentElement;
  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
  if (reduce) root.classList.add('scenes-still');

  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function seg(p, a, b) { return clamp((p - a) / (b - a)); }
  function ease(t) { return 1 - Math.pow(1 - t, 3); }
  function nums(s) { return (s || '').trim().split(/\s+/).map(Number); }

  /* ---------- split helpers: text stays in the DOM, only wrapped in spans ---------- */
  function splitText(el, mode) {
    var out = [];
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var parts = mode === 'letters' ? n.nodeValue.split('') : n.nodeValue.split(/(\s+)/);
          var frag = document.createDocumentFragment();
          parts.forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(t)); return; }
            var s = document.createElement('span');
            s.className = mode === 'letters' ? 'rl' : 'rw';
            s.textContent = t;
            frag.appendChild(s); out.push(s);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && !n.classList.contains('dotmark')) { walk(n); }
      });
    })(el);
    return out;
  }

  /* ---------- laptop keyboard ---------- */
  var LAYOUT = [[1,1,1,1,1,1,1,1,1,1,1,1,1.6],[1.4,1,1,1,1,1,1,1,1,1,1,1,1.2],[1.7,1,1,1,1,1,1,1,1,1,1,1.9],[2.2,1,1,1,1,1,1,1,1,1,2.2],[1.2,1.2,1.2,6,1.2,1.2,1.2]];
  function buildKeyboard(lap) {
    var kb = lap.querySelector('.lap-kb');
    if (!kb) return null;
    var keys = [], enter = null, space = null;
    var rows = document.createElement('div'); rows.className = 'lap-rows';
    LAYOUT.forEach(function (r, ri) {
      var row = document.createElement('div'); row.className = 'lap-row';
      r.forEach(function (w, ki) {
        var k = document.createElement('span'); k.className = 'key'; k.style.flexGrow = w;
        row.appendChild(k); keys.push(k);
        if (ri === 2 && ki === r.length - 1) enter = k;
        if (ri === 4 && ki === 3) space = k;
      });
      rows.appendChild(row);
    });
    var pad = document.createElement('div'); pad.className = 'lap-pad';
    kb.appendChild(rows); kb.appendChild(pad);
    return { keys: keys, enter: enter, space: space, last: [] };
  }
  function pressKeys(kb, p, enterOn) {
    if (!kb) return;
    var on = [];
    if (p >= 0) {
      var n = kb.keys.length;
      on.push(kb.keys[Math.floor(p * 211) % n]);
      var s = kb.keys[Math.floor(p * 211 + 7) % n];
      if (s === kb.space) on.push(s);
    }
    if (enterOn) on.push(kb.enter);
    kb.last.forEach(function (k) { if (on.indexOf(k) < 0) k.classList.remove('down'); });
    on.forEach(function (k) { if (k) k.classList.add('down'); });
    kb.last = on;
  }

  /* ---------- per-scene controllers ---------- */
  var scenes = [];
  function setup(sec) {
    var S = { el: sec, items: [], p: -1 };
    sec.querySelectorAll('[data-words]').forEach(function (el) {
      var r = nums(el.getAttribute('data-words'));
      S.items.push({ t: 'seq', parts: splitText(el, 'words'), a: r[0], b: r[1], k: 'w' });
    });
    sec.querySelectorAll('[data-letters]').forEach(function (el) {
      var r = nums(el.getAttribute('data-letters'));
      S.items.push({ t: 'seq', parts: splitText(el, 'letters'), a: r[0], b: r[1], k: 'l' });
    });
    [['data-show', 'show'], ['data-on', 'on'], ['data-swap', 'swap'], ['data-count', 'count'], ['data-scale', 'scale']].forEach(function (d) {
      sec.querySelectorAll('[' + d[0] + ']').forEach(function (el) {
        var it = { t: d[1], el: el, r: nums(el.getAttribute(d[0])) };
        if (d[1] === 'count') { it.to = parseFloat(el.getAttribute('data-to')); it.pre = el.getAttribute('data-pre') || ''; it.suf = el.getAttribute('data-suf') || ''; it.v = null; }
        S.items.push(it);
      });
    });
    sec.querySelectorAll('.laptop').forEach(function (lap) {
      var it = { t: 'lap', el: lap, kb: buildKeyboard(lap), lines: [], scroll: lap.querySelector('.lap-scroll') };
      if (lap.hasAttribute('data-type')) {
        it.r = nums(lap.getAttribute('data-type'));
        it.maxvis = parseInt(lap.getAttribute('data-maxvis') || '8', 10);
        lap.querySelectorAll('.ln').forEach(function (ln) {
          var chars = splitText(ln, 'letters'); ln.classList.add('typed');
          it.lines.push({ el: ln, chars: chars, shown: -1 });
        });
      }
      if (lap.hasAttribute('data-keys')) { it.keys = nums(lap.getAttribute('data-keys')); it.enters = nums(lap.getAttribute('data-enters')); }
      S.items.push(it);
    });
    var steps = sec.getAttribute('data-nav-steps');
    if (steps) S.navSteps = steps.trim().split(/\s+/).map(function (x) { var q = x.split(':'); return [parseFloat(q[0]), q[1]]; });
    var wallSteps = sec.getAttribute('data-wall-steps');
    if (wallSteps) S.wallSteps = wallSteps.trim().split(/\s+/).map(function (x) { var q = x.split(':'); return [parseFloat(q[0]), q[1]]; });
    return S;
  }

  function fadeStyle(el, o, dy) {
    el.style.opacity = o.toFixed(3);
    el.style.transform = 'translateY(' + ((1 - o) * (dy || 30)).toFixed(1) + 'px)';
  }

  function render(S, p) {
    S.items.forEach(function (it) {
      if (it.t === 'seq') {
        var n = it.parts.length;
        it.parts.forEach(function (s, i) {
          var o, tr;
          if (it.k === 'w') {
            o = ease(seg(p, it.a + (it.b - it.a) * i / n, it.a + (it.b - it.a) * (i + 1) / n));
            tr = 'translateY(' + ((1 - o) * 0.45).toFixed(3) + 'em) rotate(' + ((((i * 37) % 11) - 5) * 1.4 * (1 - o)).toFixed(2) + 'deg)';
          } else {
            o = ease(seg(p, it.a + (it.b - it.a) * i / n * 0.7, it.a + (it.b - it.a) * (i / n * 0.7 + 0.3)));
            var dy = (((i * 53) % 7) - 3) * 0.08 * (1 - o) + (1 - o) * 0.5;
            tr = 'translateY(' + dy.toFixed(3) + 'em) rotate(' + ((((i * 29) % 9) - 4) * 3 * (1 - o)).toFixed(2) + 'deg)';
          }
          s.style.opacity = o.toFixed(3); s.style.transform = tr;
        });
      } else if (it.t === 'show') {
        fadeStyle(it.el, ease(seg(p, it.r[0], it.r[1])));
      } else if (it.t === 'on') {
        it.el.style.opacity = ease(seg(p, it.r[0], it.r[1])).toFixed(3);
      } else if (it.t === 'swap') {
        var o2 = ease(seg(p, it.r[0], it.r[1])) * (1 - ease(seg(p, it.r[2], it.r[3])));
        it.el.style.opacity = o2.toFixed(3);
        it.el.style.transform = 'translateY(' + ((1 - o2) * 24).toFixed(1) + 'px)';
        it.el.style.visibility = o2 < 0.01 ? 'hidden' : 'visible';
      } else if (it.t === 'count') {
        var v = Math.round(it.to * ease(seg(p, it.r[0], it.r[1])));
        if (v !== it.v) { it.v = v; it.el.textContent = it.pre + v + it.suf; }
      } else if (it.t === 'scale') {
        var sc = it.r[2] + (it.r[3] - it.r[2]) * ease(seg(p, it.r[0], it.r[1]));
        it.el.style.transform = 'scale(' + sc.toFixed(4) + ')';
      } else if (it.t === 'lap') {
        renderLaptop(it, p);
      }
    });
    if (S.navSteps) S.nav = pick(S.navSteps, p);
    if (S.wallSteps) S.wall = pick(S.wallSteps, p);
  }
  function pick(steps, p) { var v = steps[0][1]; steps.forEach(function (s) { if (p >= s[0]) v = s[1]; }); return v; }

  function renderLaptop(it, p) {
    if (it.r) {
      var a = it.r[0], b = it.r[1], n = it.lines.length, started = 0, typing = false, enter = false, caretLine = -1;
      it.lines.forEach(function (ln, i) {
        var lo = a + (b - a) * i / n, hi = a + (b - a) * (i + 1) / n, f = seg(p, lo, hi);
        var count = f >= 1 ? ln.chars.length : Math.floor(ln.chars.length * Math.min(1, f / 0.8));
        if (f > 0) started = i + 1;
        if (f > 0 && (f < 1 || i === n - 1)) caretLine = i;
        if (f > 0 && f < 0.8) typing = true;
        if (f >= 0.8 && f < 1) enter = true;
        if (count !== ln.shown) {
          ln.chars.forEach(function (c, j) { c.classList.toggle('on', j < count); });
          ln.shown = count;
        }
        ln.el.classList.toggle('vis', f > 0);
      });
      it.lines.forEach(function (ln, i) {
        ln.el.classList.toggle('caret', i === caretLine);
        var lastOn = ln.chars[Math.max(0, ln.shown - 1)];
        ln.chars.forEach(function (c) { c.classList.remove('cur'); });
        if (i === caretLine && ln.shown > 0 && lastOn) lastOn.classList.add('cur');
        ln.el.classList.toggle('caret0', i === caretLine && ln.shown === 0);
      });
      if (it.scroll && started !== it.started) {
        // keep the newest line in view; measured, so wrapped lines scroll correctly
        it.started = started;
        var view = it.scroll.parentNode, last = started ? it.lines[started - 1].el : null;
        var shift = last ? Math.max(0, last.offsetTop + last.offsetHeight - view.clientHeight) : 0;
        it.scroll.style.transform = 'translateY(' + (-shift) + 'px)';
      }
      pressKeys(it.kb, typing ? p : -1, enter);
    } else if (it.keys) {
      var on = p > it.keys[0] && p < it.keys[1];
      var ent = (it.enters || []).some(function (x) { return Math.abs(p - x) < 0.02; });
      pressKeys(it.kb, on ? p : -1, ent);
    } else {
      pressKeys(it.kb, p > 0 && p < 1 ? p : -1, false);
    }
  }

  /* ---------- loop ---------- */
  var navTargets = [];
  var raf = 0;
  function frame() {
    raf = 0;
    var vh = window.innerHeight || 900;
    scenes.forEach(function (S) {
      var r = S.el.getBoundingClientRect();
      if (r.bottom < -vh || r.top > vh * 2) return;           // far away: skip work
      var span = r.height - vh;
      var p = span > 0 ? clamp(-r.top / span) : (r.top < vh ? 1 : 0);
      if (Math.abs(p - S.p) < 0.0005) return;
      S.p = p; render(S, p);
    });
    // nav colour + wall: whatever sits under the nav bar (y = 48px)
    var nav = 'dark', wall = 'ink';
    for (var i = 0; i < navTargets.length; i++) {
      var t = navTargets[i], rr = t.el.getBoundingClientRect();
      if (rr.top <= 48 && rr.bottom > 48) {
        nav = (t.S && t.S.nav) || t.el.getAttribute('data-nav') || nav;
        wall = (t.S && t.S.wall) || t.el.getAttribute('data-wall') || wall;
        break;
      }
    }
    if (root.getAttribute('data-nav') !== nav) root.setAttribute('data-nav', nav);
    if (root.getAttribute('data-wall') !== wall) root.setAttribute('data-wall', wall);
  }
  function onScroll() { if (!raf) raf = requestAnimationFrame(frame); }

  /* ---------- case videos: load and play only when visible ---------- */
  function lazyVideos() {
    var vids = document.querySelectorAll('video[data-lazy-play]');
    if (!('IntersectionObserver' in window)) { vids.forEach(function (v) { v.preload = 'auto'; }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) { if (v.preload !== 'auto') v.preload = 'auto'; var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
        else if (!v.paused) v.pause();
      });
    }, { threshold: 0.25 });
    vids.forEach(function (v) { io.observe(v); });
  }

  function init() {
    document.querySelectorAll('.scene').forEach(function (sec) { var S = setup(sec); scenes.push(S); sec._S = S; });
    document.querySelectorAll('[data-nav]').forEach(function (el) { navTargets.push({ el: el, S: el._S }); });
    if (reduce) {
      scenes.forEach(function (S) { render(S, 1); S.p = 1; });
      // in still mode every scene sits in normal flow, so only the nav colour needs to follow scrolling
      scenes.length = 0;
    }
    frame();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    lazyVideos();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
