/* AI Island: a cozy pixel-art map for the AI lessons for kids page.
   Everything is drawn in code on a 384x240 canvas, scaled up with crisp pixels.
   Buildings link to the track pages through HTML hotspots laid over the canvas. */
(function () {
  var W = 384, H = 240, OL = '#2b2a3a';
  var C = {
    water: '#3fc1ec', waterL: '#8fdcf7', waterD: '#2aa6d6', sand: '#f3d98f', sandD: '#dfbe68',
    grass: '#7ccd5d', grassD: '#68b94b', grassL: '#97dc78', cob: '#c5cbd3', cobL: '#e0e4e9', cobD: '#a2aab5',
    wood: '#b07a45', woodD: '#83562a', win: '#bdeeff', white: '#ffffff', skin: '#f6c9a0', skinD: '#e2a87c'
  };
  var DOORS = { lab: [88, 80], time: [192, 62], market: [300, 80], court: [88, 186], studio: [300, 186], light: [346, 128], hq: [44, 128] };
  var CENTER = [192, 128];

  function rng(seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }
  function R(c, x, y, w, h, col) { c.fillStyle = col; c.fillRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h)); }

  // ---------- terrain ----------
  function land(x, y) { var a = (x - 192) / 172, b = (y - 120) / 106; return Math.pow(Math.abs(a), 4) + Math.pow(Math.abs(b), 4); }
  function onPath(x, y) {
    if (Math.abs(y - 128) <= 5 && x >= 40 && x <= 346) return true;
    if (Math.abs(x - 192) <= 5 && y >= 60 && y <= 228) return true;
    if (Math.abs(x - 88) <= 4 && ((y >= 80 && y <= 128) || (y >= 128 && y <= 186))) return true;
    if (Math.abs(x - 300) <= 4 && ((y >= 80 && y <= 128) || (y >= 128 && y <= 186))) return true;
    var dx = x - 192, dy = y - 128; return dx * dx + dy * dy <= 30 * 30;
  }

  function terrain(c) {
    var r = rng(7), x, y, v;
    for (y = 0; y < H; y++) for (x = 0; x < W; x++) {
      v = land(x, y);
      if (v > 1) { R(c, x, y, 1, 1, ((x * 7 + y * 13) % 29 === 0) ? C.waterD : C.water); continue; }
      if (v > .8) { R(c, x, y, 1, 1, r() < .12 ? C.sandD : C.sand); continue; }
      if (onPath(x, y)) {
        var sx = (x + (y >> 2) * 3) % 6, sy = y % 4;
        R(c, x, y, 1, 1, (sx === 0 || sy === 0) ? C.cobD : (r() < .25 ? C.cobL : C.cob)); continue;
      }
      var t = r(); R(c, x, y, 1, 1, t < .07 ? C.grassD : t > .95 ? C.grassL : C.grass);
    }
    // shoreline outline + foam
    for (y = 1; y < H - 1; y++) for (x = 1; x < W - 1; x++) {
      if (land(x, y) <= 1 && (land(x + 1, y) > 1 || land(x - 1, y) > 1 || land(x, y + 1) > 1 || land(x, y - 1) > 1)) R(c, x, y, 1, 1, C.white);
    }
    // grass tufts
    for (var i = 0; i < 140; i++) {
      x = 20 + r() * 344 | 0; y = 20 + r() * 200 | 0;
      if (land(x, y) < .75 && !onPath(x, y) && !onPath(x + 3, y)) { R(c, x, y, 1, 2, C.grassD); R(c, x + 2, y - 1, 1, 3, C.grassD); }
    }
    // rainbow wheel in the plaza
    for (y = -10; y <= 10; y++) for (x = -10; x <= 10; x++) {
      var d = x * x + y * y; if (d > 100) continue;
      var a = (Math.atan2(y, x) / Math.PI + 1) * 180;
      R(c, 192 + x, 128 + y, 1, 1, d > 81 ? OL : 'hsl(' + Math.round(a) + ',90%,62%)');
    }
    R(c, 190, 126, 4, 4, C.white);
  }

  // ---------- props ----------
  function shadow(c, x, y, w) { c.fillStyle = 'rgba(30,40,60,.22)'; c.fillRect(x - w / 2 | 0, y, w | 0, 3); }
  function tree(c, x, y, col) {
    shadow(c, x, y, 14); R(c, x - 1, y - 5, 3, 6, C.woodD);
    var g = col || '#4faa49', gl = '#74c95f', gd = '#3c8d3a';
    R(c, x - 6, y - 15, 13, 9, g); R(c, x - 4, y - 18, 9, 3, g); R(c, x - 5, y - 6, 11, 2, gd);
    R(c, x - 3, y - 16, 4, 3, gl); R(c, x - 7, y - 13, 1, 6, OL); R(c, x + 7, y - 13, 1, 6, OL); R(c, x - 4, y - 19, 9, 1, OL);
  }
  function palm(c, x, y) {
    shadow(c, x + 2, y, 14);
    for (var i = 0; i < 14; i++) R(c, x + (i > 8 ? 1 : 0), y - i, 2, 1, i % 3 ? '#b8834b' : '#8c5c2c');
    var fy = y - 15, g = '#3fb35a', gl = '#6fd27f';
    R(c, x - 8, fy, 7, 2, g); R(c, x + 3, fy, 7, 2, g); R(c, x - 10, fy + 2, 3, 2, g); R(c, x + 9, fy + 2, 3, 2, g);
    R(c, x - 4, fy - 3, 10, 3, g); R(c, x - 2, fy - 5, 6, 2, gl); R(c, x - 6, fy - 1, 2, 1, gl); R(c, x + 6, fy - 1, 2, 1, gl);
    R(c, x - 1, fy, 2, 2, '#8c5c2c');
  }
  function flowers(c, x, y, col) {
    [[0, 0], [3, 1], [1, 3], [5, 3]].forEach(function (p) { R(c, x + p[0], y + p[1], 2, 2, col); R(c, x + p[0], y + p[1], 1, 1, '#fff3a6'); });
    R(c, x + 2, y + 2, 1, 2, C.grassD);
  }
  function bench(c, x, y) { R(c, x, y, 14, 3, C.wood); R(c, x, y + 3, 14, 1, C.woodD); R(c, x + 1, y + 4, 2, 2, C.woodD); R(c, x + 11, y + 4, 2, 2, C.woodD); R(c, x, y - 3, 14, 2, C.wood); }
  function lamp(c, x, y) { shadow(c, x, y, 6); R(c, x, y - 12, 2, 12, OL); R(c, x - 2, y - 15, 6, 3, OL); R(c, x - 1, y - 14, 4, 1, '#ffe27a'); }
  function bush(c, x, y) { R(c, x - 5, y - 4, 10, 5, '#58b14a'); R(c, x - 3, y - 6, 6, 2, '#58b14a'); R(c, x - 2, y - 5, 2, 1, '#86d470'); R(c, x - 1, y - 3, 2, 2, '#ff7eb6'); R(c, x + 3, y - 2, 2, 2, '#ffd23f'); }

  // ---------- buildings (door at bottom centre) ----------
  function walls(c, cx, by, w, h, col, shade) {
    var x0 = cx - w / 2 | 0, y0 = by - h;
    shadow(c, cx + 3, by, w + 4);
    R(c, x0, y0, w, h, col); R(c, x0, by - 3, w, 3, shade);
    R(c, x0 - 1, y0, 1, h + 1, OL); R(c, x0 + w, y0, 1, h + 1, OL); R(c, x0 - 1, by, w + 2, 1, OL);
    return [x0, y0];
  }
  function roof(c, cx, y0, w, h, col, shade, over) {
    over = over == null ? 3 : over;
    var x0 = (cx - w / 2 | 0) - over, ww = w + over * 2;
    R(c, x0, y0 - h, ww, h, col);
    for (var i = 2; i < h; i += 3) R(c, x0, y0 - h + i, ww, 1, shade);
    R(c, x0, y0 - h, ww, 1, OL); R(c, x0 - 1, y0 - h, 1, h + 1, OL); R(c, x0 + ww, y0 - h, 1, h + 1, OL); R(c, x0, y0, ww, 1, OL);
    R(c, x0 + 1, y0 - h + 1, ww - 2, 1, 'rgba(255,255,255,.35)');
  }
  function door(c, cx, by, col) { R(c, cx - 3, by - 10, 7, 10, OL); R(c, cx - 2, by - 9, 5, 9, col || C.wood); R(c, cx + 1, by - 5, 1, 1, '#ffe27a'); }
  function win(c, x, y, lit) { R(c, x - 1, y - 1, 7, 7, OL); R(c, x, y, 5, 5, lit ? '#ffe9a0' : C.win); R(c, x + 2, y, 1, 5, C.white); R(c, x, y + 2, 5, 1, C.white); }

  function bLab(c, n) {
    var d = DOORS.lab, p = walls(c, d[0], d[1], 46, 22, '#f4f7fb', '#d6dde6');
    roof(c, d[0], p[1], 46, 12, '#2fb7a8', '#239789');
    door(c, d[0], d[1], '#2fb7a8'); win(c, p[0] + 5, p[1] + 6, n); win(c, p[0] + 34, p[1] + 6, n);
    // flask on the roof
    var fx = d[0] - 4, fy = p[1] - 22; R(c, fx + 2, fy, 4, 5, '#cfe9ff'); R(c, fx, fy + 5, 8, 6, '#9fe870'); R(c, fx - 1, fy + 4, 10, 1, OL); R(c, fx + 1, fy + 7, 2, 2, C.white);
    R(c, fx + 9, fy - 2, 2, 2, '#9fe870'); R(c, fx + 12, fy - 5, 1, 1, '#9fe870');
    // dish
    R(c, d[0] + 12, p[1] - 18, 8, 3, '#e0e4e9'); R(c, d[0] + 15, p[1] - 15, 2, 4, OL);
  }
  function bTime(c, n) {
    var d = DOORS.time, p = walls(c, d[0], d[1], 22, 30, '#f2d6a2', '#d9b97d');
    for (var i = 0; i < 9; i++) R(c, d[0] - 12 + i - 0, p[1] - 1 - i * 1.4, 24 - i * 2.4, 1.4, i % 2 ? '#e55a4e' : '#cc463c');
    R(c, d[0] - 1, p[1] - 17, 2, 4, OL);
    // clock
    var cx = d[0], cy = p[1] + 9;
    for (var y = -5; y <= 5; y++) for (var x = -5; x <= 5; x++) { var q = x * x + y * y; if (q <= 25) R(c, cx + x, cy + y, 1, 1, q > 18 ? OL : C.white); }
    R(c, cx, cy - 3, 1, 4, OL); R(c, cx, cy, 3, 1, OL);
    door(c, d[0], d[1], C.woodD); win(c, d[0] - 9, d[1] - 14, n);
  }
  function bMarket(c, n) {
    var d = DOORS.market, x0 = d[0] - 24;
    shadow(c, d[0] + 3, d[1], 52);
    R(c, x0, d[1] - 10, 48, 10, C.wood); R(c, x0, d[1] - 10, 48, 2, '#cf9a60'); R(c, x0 - 1, d[1], 50, 1, OL);
    var fruit = ['#ff5a5a', '#ffd23f', '#9fe870', '#ff9f43', '#b57bff'];
    for (var i = 0; i < 5; i++) { R(c, x0 + 3 + i * 9, d[1] - 14, 7, 4, C.woodD); R(c, x0 + 4 + i * 9, d[1] - 16, 5, 3, fruit[i]); R(c, x0 + 5 + i * 9, d[1] - 16, 1, 1, C.white); }
    R(c, x0 + 1, d[1] - 34, 2, 24, C.woodD); R(c, x0 + 45, d[1] - 34, 2, 24, C.woodD);
    for (i = 0; i < 8; i++) R(c, x0 - 2 + i * 6.5, d[1] - 40, 6.5, 8, i % 2 ? C.white : '#ff7eb6');
    for (i = 0; i < 8; i++) R(c, x0 - 2 + i * 6.5, d[1] - 32, 6.5, 2, i % 2 ? '#e8e8f0' : '#e2559a');
    R(c, x0 - 2, d[1] - 41, 52, 1, OL);
    R(c, d[0] - 10, d[1] - 48, 20, 7, OL); R(c, d[0] - 9, d[1] - 47, 18, 5, '#ffd23f'); R(c, d[0] - 6, d[1] - 45, 12, 1, OL);
  }
  function bCourt(c, n) {
    var d = DOORS.court, p = walls(c, d[0], d[1], 46, 22, '#e7e3dc', '#cdc6b9');
    for (var i = 0; i < 5; i++) { R(c, p[0] + 3 + i * 9, p[1] + 3, 4, 17, C.white); R(c, p[0] + 6 + i * 9, p[1] + 3, 1, 17, '#cdc6b9'); }
    for (i = 0; i < 9; i++) R(c, d[0] - 26 + i * 2.6, p[1] - 1 - i * 1.3, 52 - i * 5.2, 1.3, i === 0 ? OL : '#d8cfbe');
    R(c, d[0] - 26, p[1], 52, 1, OL);
    // scales
    R(c, d[0], p[1] - 9, 1, 6, OL); R(c, d[0] - 5, p[1] - 9, 11, 1, OL); R(c, d[0] - 6, p[1] - 7, 3, 1, '#ffd23f'); R(c, d[0] + 4, p[1] - 7, 3, 1, '#ffd23f');
    R(c, p[0] - 3, d[1], 52, 2, '#cdc6b9');
    door(c, d[0], d[1], C.woodD);
  }
  function bStudio(c, n) {
    var d = DOORS.studio, p = walls(c, d[0], d[1], 44, 22, '#ffd0e4', '#f3aecd');
    roof(c, d[0], p[1], 44, 12, '#9b7bff', '#7d5ee0');
    door(c, d[0], d[1], '#9b7bff'); win(c, p[0] + 5, p[1] + 6, n); win(c, p[0] + 33, p[1] + 6, n);
    // palette sign
    var sx = d[0] - 8, sy = p[1] - 20;
    R(c, sx, sy, 16, 9, OL); R(c, sx + 1, sy + 1, 14, 7, '#fff3d6');
    [['#ff5a5a', 2, 2], ['#ffd23f', 6, 2], ['#3fc1ec', 10, 2], ['#9fe870', 4, 5]].forEach(function (k) { R(c, sx + k[1], sy + k[2], 2, 2, k[0]); });
    // easel
    R(c, d[0] + 26, d[1] - 14, 10, 8, C.white); R(c, d[0] + 27, d[1] - 13, 3, 3, '#ff7eb6'); R(c, d[0] + 31, d[1] - 11, 3, 3, '#3fc1ec');
    R(c, d[0] + 27, d[1] - 6, 1, 6, C.woodD); R(c, d[0] + 34, d[1] - 6, 1, 6, C.woodD);
  }
  function bLight(c, n, t) {
    var d = DOORS.light; shadow(c, d[0] + 3, d[1], 18);
    for (var i = 0; i < 40; i++) { var w = 14 - Math.floor(i / 10); R(c, d[0] - w / 2, d[1] - 1 - i, w, 1, Math.floor(i / 8) % 2 ? C.white : '#e5484d'); }
    R(c, d[0] - 8, d[1] - 1, 1, 1, OL);
    R(c, d[0] - 6, d[1] - 47, 12, 7, OL); R(c, d[0] - 5, d[1] - 46, 10, 5, '#ffe27a');
    R(c, d[0] - 6, d[1] - 52, 12, 5, '#e5484d'); R(c, d[0] - 4, d[1] - 54, 8, 2, '#e5484d'); R(c, d[0] - 1, d[1] - 56, 2, 2, OL);
    door(c, d[0], d[1], C.woodD);
  }
  function bHq(c, n, logo) {
    var d = DOORS.hq, p = walls(c, d[0], d[1], 34, 22, '#1b1a17', '#0d0c0a');
    roof(c, d[0], p[1], 34, 9, '#9fe870', '#7ccb52');
    door(c, d[0], d[1], '#9fe870'); win(c, p[0] + 3, p[1] + 5, true); win(c, p[0] + 26, p[1] + 5, true);
    if (logo && logo.complete && logo.naturalWidth) { c.imageSmoothingEnabled = true; c.drawImage(logo, d[0] - 8, p[1] - 26, 16, 16); c.imageSmoothingEnabled = false; R(c, d[0] - 9, p[1] - 27, 18, 1, OL); }
  }

  var BUILD = { lab: bLab, time: bTime, market: bMarket, court: bCourt, studio: bStudio, light: bLight, hq: bHq };

  function decor(c) {
    [[128, 60], [250, 56], [26, 98], [358, 82], [148, 210], [238, 214], [30, 162], [360, 172], [120, 98], [262, 160]].forEach(function (p) { palm(c, p[0], p[1]); });
    [[146, 166], [240, 92], [56, 60], [330, 210], [52, 206], [338, 46], [210, 30], [168, 30]].forEach(function (p) { tree(c, p[0], p[1]); });
    var r = rng(31), cols = ['#ff7eb6', '#ffd23f', '#ffffff', '#b57bff', '#ff9f43'];
    for (var i = 0; i < 70; i++) {
      var x = 24 + r() * 336 | 0, y = 24 + r() * 196 | 0;
      if (land(x, y) < .7 && !onPath(x, y) && !onPath(x + 6, y + 4) && !near(x, y)) flowers(c, x, y, cols[i % cols.length]);
    }
    [[110, 150], [272, 104], [60, 150], [326, 150], [120, 200], [262, 206]].forEach(function (p) { bush(c, p[0], p[1]); });
    bench(c, 160, 100); bench(c, 214, 154);
    [[166, 112], [218, 112], [166, 150], [218, 150]].forEach(function (p) { lamp(c, p[0], p[1]); });
    // dock
    for (var k = 0; k < 6; k++) { R(c, 186, 218 + k * 4, 12, 3, C.wood); R(c, 186, 221 + k * 4, 12, 1, C.woodD); }
    R(c, 185, 218, 1, 24, OL); R(c, 198, 218, 1, 24, OL);
  }
  function near(x, y) {
    for (var k in DOORS) { var d = DOORS[k]; if (Math.abs(x - d[0]) < 32 && y > d[1] - 56 && y < d[1] + 6) return true; }
    return false;
  }

  // ---------- characters ----------
  var KIDS = [
    { name: 'MIA', hair: '#5a3a1e', shirt: '#ff7eb6', pants: '#3b4a8c' }, { name: 'LEO', hair: '#f2c14e', shirt: '#3fc1ec', pants: '#2b2a3a' },
    { name: 'ZOE', hair: '#2b2a3a', shirt: '#9fe870', pants: '#7d5ee0' }, { name: 'KAI', hair: '#c4572e', shirt: '#ffd23f', pants: '#3b4a8c' },
    { name: 'NOOR', hair: '#1b1a17', shirt: '#b57bff', pants: '#2b2a3a', scarf: '#ff9f43' }, { name: 'SAM', hair: '#8b5a2b', shirt: '#ff9f43', pants: '#2fb7a8' },
    { name: 'GIZMO', robot: true }
  ];
  function drawKid(c, k, x, y, f, dir) {
    x = Math.round(x); y = Math.round(y);
    c.fillStyle = 'rgba(30,40,60,.25)'; c.fillRect(x - 4, y - 1, 9, 2);
    if (k.robot) {
      var bob = f % 2;
      R(c, x - 4, y - 14 - bob, 9, 8, '#d9dee7'); R(c, x - 4, y - 14 - bob, 9, 1, OL); R(c, x - 5, y - 13 - bob, 1, 6, OL); R(c, x + 5, y - 13 - bob, 1, 6, OL);
      R(c, x - 3, y - 12 - bob, 7, 3, '#2b2a3a'); R(c, x - 2, y - 11 - bob, 2, 1, '#5ff0ff'); R(c, x + 1, y - 11 - bob, 2, 1, '#5ff0ff');
      R(c, x, y - 17 - bob, 1, 3, OL); R(c, x - 1, y - 18 - bob, 3, 1, '#9fe870');
      R(c, x - 3, y - 6 - bob, 7, 4, '#c3cad6'); R(c, x - 3, y - 6 - bob, 7, 1, '#9fe870'); R(c, x - 2, y - 2, 2, 2, OL); R(c, x + 1, y - 2, 2, 2, OL);
      return;
    }
    var step = f % 2;
    R(c, x - 2, y - 3, 2, 3 - step, k.pants); R(c, x + 1, y - 3, 2, 2 + step, k.pants);
    R(c, x - 2, y - 1 + (step ? 0 : 0), 2, 1, OL); R(c, x + 1, y - 1, 2, 1, OL);
    R(c, x - 3, y - 8, 7, 5, k.shirt); R(c, x - 4, y - 7, 1, 3, C.skin); R(c, x + 4, y - 7, 1, 3, C.skin);
    if (k.scarf) R(c, x - 3, y - 8, 7, 1, k.scarf);
    R(c, x - 3, y - 14, 7, 6, C.skin); R(c, x - 3, y - 15, 7, 2, k.hair); R(c, x - 4, y - 14, 1, 4, k.hair); R(c, x + 4, y - 14, 1, 4, k.hair);
    if (dir !== 'up') { R(c, x - 2, y - 11, 1, 1, OL); R(c, x + 2, y - 11, 1, 1, OL); R(c, x, y - 9, 1, 1, C.skinD); }
    else R(c, x - 3, y - 13, 7, 3, k.hair);
  }

  // routes between plaza centre and doors along the avenues
  function route(to) {
    var d = DOORS[to], pts = [[192, 132]];
    if (to === 'time') pts.push([192, d[1] + 2]);
    else if (to === 'hq' || to === 'light') pts.push([d[0] + (to === 'hq' ? 4 : -4), 132]);
    else { pts.push([d[0], 132]); pts.push([d[0], d[1] + 2]); }
    return pts;
  }

  // ---------- app ----------
  function Island(root) {
    var cv = root.querySelector('canvas'), c = cv.getContext('2d');
    c.imageSmoothingEnabled = false;
    var base = document.createElement('canvas'); base.width = W; base.height = H;
    var bc = base.getContext('2d'); bc.imageSmoothingEnabled = false;
    var logo = new Image(); logo.src = '/assets/aicoachalex-mark-96.webp';
    var hr = new Date().getHours(), night = hr < 7 || hr >= 19;
    if (night) root.classList.add('night');
    function paintBase() {
      terrain(bc); decor(bc);
      ['time', 'lab', 'market', 'hq', 'light', 'court', 'studio'].forEach(function (k) { BUILD[k](bc, night, logo); });
    }
    paintBase(); logo.onload = function () { BUILD.hq(bc, night, logo); };
    var tags = root.querySelector('.tags'), walkers = [], targets = ['lab', 'market', 'court', 'studio', 'time', 'light', 'hq'];
    var r = rng(11);
    KIDS.forEach(function (k, i) {
      var el = document.createElement('span'); el.className = 'tag' + (k.robot ? ' bot' : ''); el.textContent = k.name; tags.appendChild(el);
      var rt = route(targets[i % targets.length]), end = rt[rt.length - 1];
      var w = { k: k, el: el, path: rt.slice(0, -1).reverse(), x: end[0], y: end[1], wait: i * 25, f: 0, dir: 'down' };
      walkers.push(w);
    });
    var coach = document.createElement('span'); coach.className = 'tag coach'; coach.textContent = 'COACH ALEX'; tags.appendChild(coach);
    function plan(w) {
      var to = targets[(r() * targets.length) | 0], out = route(to);
      w.path = out.slice(1).concat(out.slice(0, -1).reverse());
      w.wait = 0;
    }
    var boatX = 230, t = 0, clouds = [[40, 30], [220, 190], [320, 60]];
    function frame() {
      t++;
      c.drawImage(base, 0, 0);
      // water sparkles
      for (var i = 0; i < 46; i++) {
        var sx = (i * 53 + (t >> 1) * (1 + i % 3)) % W, sy = (i * 37 + (i % 5) * 11) % H;
        if (land(sx, sy) > 1.08) R(c, sx, sy, 3, 1, (t + i) % 16 < 8 ? C.waterL : C.white);
      }
      // boat
      boatX += .15; if (boatX > 380) boatX = -20;
      var by = 234 + (t % 30 < 15 ? 0 : 1);
      R(c, boatX - 8, by, 18, 3, '#e5484d'); R(c, boatX - 6, by + 3, 14, 1, OL); R(c, boatX, by - 12, 1, 12, OL); R(c, boatX + 1, by - 11, 7, 9, C.white); R(c, boatX - 6, by - 8, 6, 6, '#ffd23f');
      // lighthouse beam
      var ang = t * .04, d = DOORS.light;
      c.save(); c.globalAlpha = night ? .35 : .18; c.fillStyle = '#fff3a6'; c.beginPath(); c.moveTo(d[0], d[1] - 44);
      c.lineTo(d[0] + Math.cos(ang - .18) * 90, d[1] - 44 + Math.sin(ang - .18) * 50); c.lineTo(d[0] + Math.cos(ang + .18) * 90, d[1] - 44 + Math.sin(ang + .18) * 50); c.fill(); c.restore();
      // walkers sorted by y
      walkers.forEach(function (w) {
        if (w.wait > 0) { w.wait--; return; }
        if (!w.path.length) { plan(w); w.wait = 30 + (r() * 60 | 0); return; }
        var p = w.path[0], dx = p[0] - w.x, dy = p[1] - w.y, sp = .55;
        if (Math.abs(dx) < sp && Math.abs(dy) < sp) { w.x = p[0]; w.y = p[1]; w.path.shift(); if (!w.path.length) w.wait = 40; return; }
        if (Math.abs(dx) >= sp) { w.x += Math.sign(dx) * sp; w.dir = dx > 0 ? 'right' : 'left'; } else { w.y += Math.sign(dy) * sp; w.dir = dy > 0 ? 'down' : 'up'; }
        if (t % 6 === 0) w.f++;
      });
      walkers.slice().sort(function (a, b) { return a.y - b.y; }).forEach(function (w) { drawKid(c, w.k, w.x, w.y, w.f, w.dir); });
      drawKid(c, { hair: '#2b2a3a', shirt: '#0d0c0a', pants: '#163300', scarf: '#9fe870' }, 176, 130, (t >> 5) % 2 ? 0 : 0, 'down');
      // clouds
      clouds.forEach(function (cl, i) {
        cl[0] += .08 + i * .03; if (cl[0] > W + 40) cl[0] = -60;
        c.fillStyle = 'rgba(255,255,255,.55)'; c.fillRect(cl[0], cl[1], 34, 6); c.fillRect(cl[0] + 6, cl[1] - 4, 20, 4); c.fillRect(cl[0] + 4, cl[1] + 6, 26, 2);
      });
      if (night) {
        c.fillStyle = 'rgba(25,30,80,.42)'; c.fillRect(0, 0, W, H);
        c.globalCompositeOperation = 'lighter';
        [[166, 98], [218, 98], [166, 136], [218, 136]].forEach(function (p) { c.fillStyle = 'rgba(255,220,120,.18)'; c.fillRect(p[0] - 6, p[1] - 4, 14, 14); });
        c.globalCompositeOperation = 'source-over';
        for (var s = 0; s < 18; s++) { var stx = (s * 97) % W, sty = (s * 41) % 60; if (land(stx, sty) > 1.1 && (t + s * 7) % 40 < 30) R(c, stx, sty, 1, 1, '#ffffff'); }
      }
      // name tags follow walkers
      var scale = cv.clientWidth / W;
      walkers.forEach(function (w) { w.el.style.transform = 'translate(' + (w.x * scale) + 'px,' + ((w.y - 19) * scale) + 'px) translate(-50%,-100%)'; });
      coach.style.transform = 'translate(' + (176 * scale) + 'px,' + (111 * scale) + 'px) translate(-50%,-100%)';
    }
    var running = true, last = 0;
    function loop(ts) { if (running && ts - last > 55) { last = ts; frame(); } requestAnimationFrame(loop); }
    frame();
    var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!still) {
      requestAnimationFrame(loop);
      if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { running = es[0].isIntersecting; }).observe(cv);
      document.addEventListener('visibilitychange', function () { running = !document.hidden; });
    }
    window.addEventListener('resize', frame);
  }

  // sprite export used at build time for track icons
  function sprite(kind, scale) {
    var cv = document.createElement('canvas'); cv.width = W; cv.height = H; var c = cv.getContext('2d'); c.imageSmoothingEnabled = false;
    BUILD[kind](c, false, null);
    var d = DOORS[kind], box = { lab: [-30, -48, 60, 54], time: [-16, -62, 32, 66], market: [-30, -52, 62, 56], court: [-30, -38, 60, 44], studio: [-30, -46, 72, 52], light: [-12, -58, 26, 62], hq: [-22, -38, 46, 42] }[kind];
    var out = document.createElement('canvas'); out.width = box[2] * scale; out.height = box[3] * scale;
    var o = out.getContext('2d'); o.imageSmoothingEnabled = false;
    o.drawImage(cv, d[0] + box[0], d[1] + box[1], box[2], box[3], 0, 0, out.width, out.height);
    return out.toDataURL('image/png');
  }
  function mapPng(scale) {
    var div = document.createElement('div'); div.innerHTML = '<canvas width="' + W + '" height="' + H + '"></canvas><div class="tags"></div>';
    var cv = div.querySelector('canvas'), c = cv.getContext('2d'); c.imageSmoothingEnabled = false;
    terrain(c); decor(c); ['time', 'lab', 'market', 'hq', 'light', 'court', 'studio'].forEach(function (k) { BUILD[k](c, false, null); });
    KIDS.forEach(function (k, i) { drawKid(c, k, 150 + i * 14, 134 + (i % 2) * 6, i, 'down'); });
    var out = document.createElement('canvas'); out.width = W * scale; out.height = H * scale; var o = out.getContext('2d'); o.imageSmoothingEnabled = false;
    o.drawImage(cv, 0, 0, out.width, out.height); return out.toDataURL('image/png');
  }
  window.AIIsland = { sprite: sprite, mapPng: mapPng, W: W, H: H, DOORS: DOORS };
  document.querySelectorAll('.island-map').forEach(function (el) { Island(el); });
})();
