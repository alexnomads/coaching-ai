"""Build the client city in EN, ES and IT.

Run from the repo root:  python3 _tools/build_who_i_work_with.py
Copy: wiw_content.py (EN), wiw_es.py, wiw_it.py, wiw_wins.py, wiw_ui.py.
Drawings: wiw_buildings.py (bboxes.json = measured drawing bounds for centring).
"""
import html
import json
import os
import re

import wiw_buildings as B
import wiw_content as EN
import wiw_es
import wiw_it
from wiw_ui import UI, FOOTER_LINKS
from wiw_wins import WINS, WIN_LABEL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "_tools")
SITE = "https://aicoachalex.com"
BOOK = "https://alessandrocapezza.youcanbook.me/"
SHARE = SITE + "/ALEXAICOACH-SHAREv2.png"
TODAY = "2026-10-19"
CSS_V = "2"
LANGS = ["en", "es", "it"]
ORDER = EN.ORDER
BBOX = json.load(open(os.path.join(TOOLS, "bboxes.json")))


def read(name):
    with open(os.path.join(TOOLS, name), encoding="utf-8") as f:
        return f.read()


def esc(s):
    return html.escape(s, quote=True)


# ---------- data per language ----------
def personas(lang):
    out = {}
    for p in EN.P:
        q = dict(p)
        if lang != "en":
            q.update((wiw_es if lang == "es" else wiw_it).T[p["num"]])
        kind, wins = WINS[p["num"]]
        q["win"], q["win_label"] = wins[lang], WIN_LABEL[kind][lang]
        out[p["num"]] = q
    return out


def districts(lang):
    out = {}
    for d in EN.DISTRICTS:
        if lang == "en":
            out[d["id"]] = (d["name"], d["tag"], d["blurb"])
        else:
            out[d["id"]] = (wiw_es if lang == "es" else wiw_it).DISTRICTS[d["id"]]
    return out


DATA = {l: personas(l) for l in LANGS}
DIST = {l: districts(l) for l in LANGS}


def url(lang, p=None):
    return SITE + UI[lang]["base"] + (p["slug"] + "/" if p else "")


def path(lang, p=None):
    return UI[lang]["base"] + (p["slug"] + "/" if p else "")


def alternates(num=None):
    out = []
    for l in LANGS:
        out.append((l, url(l, DATA[l][num]) if num else url(l)))
    out.append(("x-default", url("en", DATA["en"][num]) if num else url("en")))
    return out


def win_badge(p, cls="win"):
    return f'<span class="{cls}"><small>{esc(p["win_label"])}</small>{esc(p["win"])}</span>'


def vb(kind, pad=10):
    x, y, w, h = BBOX[kind]
    return f"{x-pad:.0f} {y-pad:.0f} {w+2*pad:.0f} {h+2*pad:.0f}"


# ---------- chrome ----------
HEAD_TRACKING = read("_tracking_head.html")
BODY_NOSCRIPT = """<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T93CHX6Z"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2696345404134131&ev=PageView&noscript=1"
/></noscript>"""
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,700;0,9..144,900;1,9..144,400;1,9..144,700;1,9..144,900'
         '&family=Instrument+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">')
PERSON = {"@type": "Person", "@id": SITE + "/#alessandro", "name": "Alessandro Capezza",
          "alternateName": "AI Coach Alex", "jobTitle": "AI Coach", "url": SITE + "/",
          "address": {"@type": "PostalAddress", "addressLocality": "Barcelona", "addressCountry": "ES"},
          "sameAs": ["https://www.instagram.com/alexislimitless/", "https://www.youtube.com/@alexislimitless",
                     "https://www.linkedin.com/in/alessandrocapezza/", "https://x.com/alexNomads"]}
BOOKING = {"en": read("_booking_block.html"), "es": read("_booking_block_es.html"), "it": read("_booking_block_it.html")}
NAVJS = read("_navjs_block.html")
NAV_TPL = {"es": read("_nav_es.html"), "it": read("_nav_it.html")}


def lang_switch(lang, alts):
    hrefs = {l: h.replace(SITE, "") for l, h in alts if l in LANGS}
    parts = []
    for l in LANGS:
        on = ' class="on"' if l == lang else ""
        parts.append(f'<a href="{hrefs[l]}"{on} hreflang="{l}" onclick="try{{localStorage.setItem(\'preferred-lang\',\'{l}\')}}catch(e){{}}">{l.upper()}</a>')
    return '<div class="sn-lang">' + '<span class="sep">·</span>'.join(parts) + "</div>"


def nav(lang, alts):
    sw = lang_switch(lang, alts)
    if lang == "en":
        courses = ('<a href="/personal-ai-agent.html">Your Own AI</a><a href="/ai-video-course-booking.html">AI VideoGen</a>'
                   '<a href="/voice-ai-agents.html">Voice AI Agents</a><a href="/personal-ai-setup.html">Personal AI Setup</a><a href="/120-prompts.html">120 Prompts</a>')
        mob = courses.replace('<a href=', '<a class="sn-mob-course" href=')
        return f"""<div class="sn" id="siteNav" role="navigation" aria-label="Menu">
  <div class="sn-in">
    <a class="sn-logo" href="/" aria-label="AI Coach Alex"><img src="/assets/aicoachalex-mark-96.webp" alt="AI Coach Alex" width="38" height="38"></a>
    <div class="sn-links">
      <a href="/#method">Method</a>
      <a class="nav-quiz" href="/career-risk-assessment.html">Risk Quiz</a>
      <a href="/blog/">Blog</a>
      <a href="/openclaw-ai-agent-setup.html">Configure OpenClaw Agent</a>
      <div class="sn-dd"><a class="sn-dd-t" href="/courses.html" aria-haspopup="true" aria-expanded="false">Courses <span aria-hidden="true">&#9662;</span></a><div class="sn-dd-m">{courses}</div></div>
      <a href="{UI['en']['base']}" class="sn-cur">Who I Work With</a>
    </div>
    <div class="sn-right">
      {sw}
      <a class="nav-quiz sn-quiz-m" href="/career-risk-assessment.html">Risk Quiz</a>
      <a class="sn-cta" href="{BOOK}" target="_blank" rel="noopener">Book Diagnostic</a>
      <button class="sn-burger" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="sn-mob">
    <a href="/#method">Method</a>
    <a class="nav-quiz" href="/career-risk-assessment.html">Risk Quiz</a>
    <a href="/blog/">Blog</a>
    <a href="/openclaw-ai-agent-setup.html">Configure OpenClaw Agent</a>
    <a class="sn-mob-sub" href="/courses.html">Courses →</a>
    {mob}
    <a href="{UI['en']['base']}" class="sn-cur">Who I Work With</a>
    {sw}
    <a class="sn-cta-m sn-cta" href="{BOOK}" target="_blank" rel="noopener">Book Diagnostic</a>
  </div>
</div>"""
    t = NAV_TPL[lang].replace('class="sn sn-dark"', 'class="sn"').replace("/assets/aicoachalex-mark.png", "/assets/aicoachalex-mark-96.webp")
    t = t.replace(f'href="{UI[lang]["old_page"]}" class="sn-cur"', f'href="{UI[lang]["base"]}" class="sn-cur"')
    t = re.sub(r'<div class="sn-lang">.*?</div>', lambda m: sw, t, flags=re.S)
    return t


def footer(lang):
    u = UI[lang]
    links = [(u["base"], u["hub_name"])] + FOOTER_LINKS[lang] + [
        ("https://www.linkedin.com/in/alessandrocapezza/", "LinkedIn"), ("https://www.instagram.com/alexislimitless/", "Instagram"), ("https://x.com/alexNomads", "X")]
    a = "".join(f'<a href="{h}"' + (' target="_blank" rel="noopener"' if h.startswith("http") else "") + f'>{esc(t)}</a>' for h, t in links)
    return f"""<footer class="foot"><div class="wrap foot-in">
  <div class="foot-brand"><img src="/assets/aicoachalex-mark-96.webp" alt="" width="48" height="48" loading="lazy"><div><b>Alessandro Capezza</b><span>{u['footer_role']}</span></div></div>
  <nav aria-label="Footer">{a}</nav>
  <p class="copy">{esc(u['footer_note'])}</p>
</div></footer>"""


def page(lang, title, desc, canonical, alts, schema, body, extra_js=""):
    u = UI[lang]
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{h}">\n' for l, h in alts)
    og_alt = "".join(f'<meta property="og:locale:alternate" content="{UI[l]["locale"]}">\n' for l in LANGS if l != lang)
    return f"""<!DOCTYPE html>
<html lang="{u['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{alt}<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:site_name" content="AI Coach Alex">
<meta property="og:type" content="website">
<meta property="og:locale" content="{u['locale']}">
{og_alt}<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SHARE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SHARE}">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<meta name="theme-color" content="#f8f6f1">
{FONTS}
<link rel="stylesheet" href="/assets/wiw.css?v={CSS_V}">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
{HEAD_TRACKING}
</head>
<body>
{BODY_NOSCRIPT}
{nav(lang, alts)}
{body}
{footer(lang)}
{BOOKING[lang]}
{NAVJS}
{extra_js}
</body>
</html>
"""


def faq_html(items, heading):
    d = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in items)
    return f'<section class="faq wrap" id="faq"><h2 class="display">{esc(heading)}</h2>{d}</section>'


def faq_schema(items, page_url):
    return {"@type": "FAQPage", "@id": page_url + "#faq",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def mini(p):
    return f'<svg viewBox="{vb(p["building"])}" aria-hidden="true"><use href="#b-{p["building"]}" x="0" y="0" width="240" height="300"/></svg>'


def shop_card(lang, p):
    return f"""<a class="shop" href="{path(lang, p)}">
  <div class="art">{mini(p)}</div>
  {win_badge(p)}
  <span class="num">{p['num']}</span>
  <h3>{p['persona']}</h3>
  <p class="sec">{esc(p['sector'])} · {esc(p['country'])}</p>
  <span class="see">{esc(UI[lang]['visit'])}</span>
</a>"""


# ---------- living city ----------
POS = {"01": (0, 0), "07": (2.1, 0), "08": (0, 2.1), "12": (2.1, 2.1),
       "09": (4.3, 0), "02": (6.4, 0), "11": (4.3, 2.1), "13": (6.4, 2.1),
       "03": (0, 4.3), "04": (2.1, 4.3), "05": (0, 6.4), "10": (2.1, 6.4),
       "hq": (4.4, 4.4), "06": (6.4, 5.4)}
CELL, CX, CY, SCALE = 70, 520, 215, .84
W_SYM, H_SYM = 240 * SCALE, 300 * SCALE
LO, HI, R0, R1 = -1.2, 7.9, 3.15, 3.95
TREES = [(-0.8, 1.9), (1.9, -0.8), (5.3, -0.9), (7.6, 0.6), (7.6, 2.3), (-0.8, 4.4), (-0.6, 7.6), (1.6, 7.7), (4.3, 6.9), (5.6, 7.6), (7.7, 7.5), (2.95, 1.0), (4.3, 2.95)]


def gs(gx, gy, z=0):
    return (CX + (gx - gy) * CELL * B.C, CY + (gx + gy) * CELL * .5 - z * CELL)


def gpoly(cells, fill, extra=""):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (gs(*c) for c in cells))
    return f'<polygon points="{pts}" fill="{fill}"{extra}/>'


def car(axis, col):
    """Small iso car centred on (0,0); axis 'x' runs along gx, 'y' along gy."""
    L, Wd, H = (.55, .3, .17) if axis == "x" else (.3, .55, .17)
    x0, y0 = -L / 2, -Wd / 2
    x1, y1 = x0 + L, y0 + Wd

    def q(pts, f):
        s = " ".join(f"{gs(a, b, c)[0]-CX:.1f},{gs(a, b, c)[1]-CY:.1f}" for a, b, c in pts)
        return f'<polygon class="k" points="{s}" fill="{f}"/>'
    body = (q([(x0, y0, H), (x1, y0, H), (x1, y1, H), (x0, y1, H)], B.light(col, .25))
            + q([(x0, y1, 0), (x1, y1, 0), (x1, y1, H), (x0, y1, H)], col)
            + q([(x1, y0, 0), (x1, y1, 0), (x1, y1, H), (x1, y0, H)], B.dark(col, .2)))
    cx0, cx1 = (x0 + L * .3, x0 + L * .8) if axis == "x" else (x0, x1)
    cy0, cy1 = (y0, y1) if axis == "x" else (y0 + Wd * .3, y0 + Wd * .8)
    cab = (q([(cx0, cy0, H + .1), (cx1, cy0, H + .1), (cx1, cy1, H + .1), (cx0, cy1, H + .1)], B.light(col, .4))
           + q([(cx0, cy1, H), (cx1, cy1, H), (cx1, cy1, H + .1), (cx0, cy1, H + .1)], "#cfe6c0")
           + q([(cx1, cy0, H), (cx1, cy1, H), (cx1, cy1, H + .1), (cx1, cy0, H + .1)], B.dark("#cfe6c0", .2)))
    return body + cab


def person(col):
    return (f'<circle r="2.6" cy="-11" fill="#e9c9a7" class="k" stroke-width=".8"/>'
            f'<path d="M-2.6,-8 h5.2 v6 h-5.2z" fill="{col}" class="k" stroke-width=".8"/>'
            f'<path d="M-1.6,-2 v3 M1.6,-2 v3" stroke="#0d0c0a" stroke-width="1.1"/>')


def city_svg(lang, symbols):
    D, U = DATA[lang], UI[lang]
    o = []
    o.append(gpoly([(LO + .25, LO + .9), (HI + .25, LO + .9), (HI + .25, HI + .9), (LO + .25, HI + .9)], "#163300", ' opacity=".08"'))
    o.append(gpoly([(LO, LO), (HI, LO), (HI, HI), (LO, HI)], "#efeadf", ' class="ground" stroke="#0d0c0a" stroke-width="1.2"'))
    o.append(gpoly([(R0, LO), (R1, LO), (R1, HI), (R0, HI)], "#d6cdb8"))
    o.append(gpoly([(LO, R0), (HI, R0), (HI, R1), (LO, R1)], "#d6cdb8"))
    m = (R0 + R1) / 2
    for a, b in (((m, LO + .3), (m, HI - .3)), ((LO + .3, m), (HI - .3, m))):
        (ax, ay), (bx, by) = gs(*a), gs(*b)
        o.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#9fe870" stroke-width="2.5" stroke-dasharray="10 12"/>')
    # traffic, drawn under the buildings so nearer buildings hide the cars
    traffic = []
    lanes = [("x", R0 + .22, 1, 16, 0, "#163300"), ("x", R1 - .22, -1, 19, 6, "#e8b04b"), ("x", R0 + .22, 1, 16, 9, "#f8f6f1"),
             ("y", R1 - .22, 1, 17, 3, "#9fe870"), ("y", R0 + .22, -1, 21, 11, "#0d0c0a")]
    for axis, lane, d, dur, beg, col in lanes:
        a, b = (LO + .2, HI - .2) if d > 0 else (HI - .2, LO + .2)
        p0 = gs(a, lane) if axis == "x" else gs(lane, a)
        p1 = gs(b, lane) if axis == "x" else gs(lane, b)
        traffic.append(f'<g class="car">{car(axis, col)}<animateMotion dur="{dur}s" begin="-{beg}s" repeatCount="indefinite" '
                       f'path="M{p0[0]:.1f},{p0[1]:.1f} L{p1[0]:.1f},{p1[1]:.1f}"/></g>')
    o.append('<g class="traffic">' + "".join(traffic) + "</g>")
    # buildings and street trees, back to front
    tops = {}
    items = list(POS.items()) + [(f"t{i}", t) for i, t in enumerate(TREES)]
    for key, (gx, gy) in sorted(items, key=lambda kv: kv[1][0] + kv[1][1]):
        if key.startswith("t"):
            X, Y = gs(gx, gy)
            o.append(f'<g class="tree"><line x1="{X:.1f}" y1="{Y:.1f}" x2="{X:.1f}" y2="{Y-14:.1f}" stroke="#6b4f2e" stroke-width="3"/>'
                     f'<circle class="k" cx="{X:.1f}" cy="{Y-20:.1f}" r="10" fill="#3d6b22"/><circle cx="{X-3:.1f}" cy="{Y-23:.1f}" r="3.5" fill="#6f9a4f"/></g>')
            continue
        X, Y = gs(gx + .9, gy + .9)
        x, y = X - B.ANCHOR[0] * SCALE, Y - B.ANCHOR[1] * SCALE
        kind = "hq" if key == "hq" else D[key]["building"]
        tops[key] = (X, y + BBOX[kind][1] * SCALE)
        if key == "hq":
            o.append(f'<a class="bld" data-k="hq" href="#start" aria-label="{esc(U["studio_label"])}"><use href="#b-hq" x="{x:.1f}" y="{y:.1f}" width="{W_SYM:.1f}" height="{H_SYM:.1f}"/></a>')
            continue
        p = D[key]
        o.append(f'<a class="bld" data-k="{key}" href="{path(lang, p)}" aria-label="{esc(p["persona_plain"])}: {esc(p["sector"])}">'
                 f'<use href="#b-{p["building"]}" x="{x:.1f}" y="{y:.1f}" width="{W_SYM:.1f}" height="{H_SYM:.1f}"/></a>')
    # people walking into the workshops
    walkers, cols = [], ["#163300", "#e8b04b", "#3d6b22", "#0d0c0a", "#9fe870", "#cdbf9f", "#163300", "#e8b04b"]
    for i, key in enumerate(["07", "12", "11", "01", "09", "04", "10", "hq"]):
        gx, gy = POS[key]
        X, Y = gs(gx + .9, gy + .9)
        door, edge = (X - 36, Y + 3), (X - 41, Y + 19)
        start = gs(gx + .55, R0 - .05) if gy < 3 else gs(gx + .55, min(gy + 2.25, HI - .3))
        dur, beg = 7 + (i % 3) * 1.5, i * 1.7
        walkers.append(f'<g class="walker" opacity="0">{person(cols[i])}'
                       f'<animateMotion dur="{dur}s" begin="-{beg:.1f}s" repeatCount="indefinite" path="M{start[0]:.1f},{start[1]:.1f} L{edge[0]:.1f},{edge[1]:.1f} L{door[0]:.1f},{door[1]:.1f}"/>'
                       f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.08;.86;1" dur="{dur}s" begin="-{beg:.1f}s" repeatCount="indefinite"/></g>')
    for i, (a, b, dur) in enumerate([((R1 + .12, LO + .4), (R1 + .12, HI - .4), 46), ((HI - .4, R0 - .12), (LO + .4, R0 - .12), 52)]):
        p0, p1 = gs(*a), gs(*b)
        walkers.append(f'<g class="walker">{person(["#3d6b22", "#e8b04b"][i])}<animateMotion dur="{dur}s" begin="-{i*13}s" repeatCount="indefinite" '
                       f'path="M{p0[0]:.1f},{p0[1]:.1f} L{p1[0]:.1f},{p1[1]:.1f}"/></g>')
    o.append('<g class="people">' + "".join(walkers) + "</g>")
    # district signs
    for did, gx, gy in [("old-town", 1.0, -1.05), ("business-district", 5.4, -1.05), ("market-square", -1.05, 5.4), ("the-station", 7.6, 4.2)]:
        X, Y = gs(gx, gy)
        name = DIST[lang][did][0].upper()
        w = 9 * len(name) + 26
        o.append(f'<a class="dsign" href="#{did}"><rect x="{X-w/2:.1f}" y="{Y-15:.1f}" width="{w:.1f}" height="26" rx="13"/>'
                 f'<text x="{X:.1f}" y="{Y+2:.1f}" text-anchor="middle">{esc(name)}</text></a>')
    # sky: sun by day, moon and stars by night (switched by the visitor's local time)
    rays = "".join(f'<line x1="0" y1="-32" x2="0" y2="-42" stroke="#e8b04b" stroke-width="3" stroke-linecap="round" transform="rotate({a})"/>' for a in range(0, 360, 30))
    stars = "".join(f'<path d="M{x},{y} l2,5 l5,2 l-5,2 l-2,5 l-2,-5 l-5,-2 l5,-2z" fill="#163300"><animate attributeName="opacity" values=".15;.8;.15" dur="{d}s" repeatCount="indefinite"/></path>'
                    for x, y, d in [(-95, 10, 3), (70, -30, 4), (135, 40, 5), (-45, 75, 3.5), (195, -5, 4.5)])
    sky = (f'<g class="sun"><g>{rays}<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="60s" repeatCount="indefinite"/></g>'
           '<circle r="24" fill="#f3c55a" class="k"/><circle r="15" fill="#f8dc8a"/></g>'
           '<g class="moon"><circle r="24" fill="#ffffff" class="k"/><circle cx="-7" cy="-5" r="5" fill="#ecebe6"/><circle cx="8" cy="7" r="3.5" fill="#ecebe6"/><circle cx="6" cy="-10" r="2.5" fill="#ecebe6"/>'
           f'{stars}</g>')
    o.insert(0, f'<g class="sky" transform="translate(150,90)">{sky}</g>')
    birds = []
    for y, dur, beg, s in [(70, 34, 0, 1), (120, 41, 14, .8), (45, 29, 22, .9)]:
        flock = "".join(f'<g transform="translate({dx},{dy}) scale({s})"><path d="M0,0 q5,-6 10,0 q5,-6 10,0" fill="none" stroke="#0d0c0a" stroke-width="1.6" stroke-linecap="round">'
                        f'<animate attributeName="d" values="M0,0 q5,-6 10,0 q5,-6 10,0;M0,0 q5,3 10,0 q5,3 10,0;M0,0 q5,-6 10,0 q5,-6 10,0" dur=".8s" begin="{k*.25:.2f}s" repeatCount="indefinite"/></path></g>'
                        for k, (dx, dy) in enumerate([(0, 0), (24, 10), (-20, 12)]))
        birds.append(f'<g class="bird">{flock}<animateMotion dur="{dur}s" begin="-{beg}s" repeatCount="indefinite" path="M-80,{y} C300,{y-30} 700,{y+30} 1120,{y-10}"/></g>')
    o.append('<g class="birds" aria-hidden="true">' + "".join(birds) + "</g>")
    # hover labels, on top of everything
    labels = []
    for key, (X, Ytop) in tops.items():
        text = U["studio_label"] if key == "hq" else D[key]["persona_plain"]
        num = "" if key == "hq" else f'<tspan class="n">{key}</tspan>  '
        w = 8.2 * len(text) + (52 if num else 30)
        lx = min(max(X - w / 2, 8), 1032 - w)
        ly = max(Ytop - 44, 6)
        labels.append(f'<g class="lbl" data-for="{key}" data-cx="{X:.1f}"><rect x="{lx:.1f}" y="{ly:.1f}" width="{w:.1f}" height="30" rx="15"/>'
                      f'<path d="M{X-6:.1f},{ly+29:.1f} l6,7 l6,-7z"/>'
                      f'<text x="{lx+14:.1f}" y="{ly+19.5:.1f}">{num}{esc(text)}</text></g>')
    o.append('<g class="labels" aria-hidden="true">' + "".join(labels) + "</g>")
    return (f'<svg id="cityMap" viewBox="0 0 1040 780" role="img" aria-labelledby="cityTitle">'
            f'<title id="cityTitle">{esc(U["city_title"])}</title><defs>{symbols}</defs>{"".join(o)}</svg>')


CITY_JS = """<script>
(function(){var svg=document.getElementById('cityMap');if(!svg)return;
var city=svg.parentNode,h=new Date().getHours();if(h<7||h>=19)city.classList.add('night');
function fit(){svg.querySelectorAll('.lbl').forEach(function(g){var t=g.querySelector('text'),r=g.querySelector('rect');try{var w=t.getComputedTextLength()+28,c=+g.getAttribute('data-cx'),nx=Math.min(Math.max(c-w/2,8),1032-w);r.setAttribute('width',w.toFixed(1));r.setAttribute('x',nx.toFixed(1));t.setAttribute('x',(nx+14).toFixed(1));}catch(e){}});}
fit();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);
function show(k,on){var l=svg.querySelector('.lbl[data-for="'+k+'"]');if(l)l.classList.toggle('on',on);}
svg.querySelectorAll('.bld').forEach(function(a){var k=a.getAttribute('data-k');['mouseenter','focus'].forEach(function(e){a.addEventListener(e,function(){show(k,true)})});['mouseleave','blur'].forEach(function(e){a.addEventListener(e,function(){show(k,false)})});});
if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches){svg.pauseAnimations();city.classList.add('still');return;}
if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?svg.unpauseAnimations():svg.pauseAnimations()})}).observe(svg);}
document.addEventListener('visibilitychange',function(){document.hidden?svg.pauseAnimations():svg.unpauseAnimations()});
})();
</script>"""


# ---------- hub ----------
def build_hub(lang):
    D, U, DS = DATA[lang], UI[lang], DIST[lang]
    kinds = sorted({p["building"] for p in D.values()}) + ["hq"]
    symbols = "".join(B.symbol(k) for k in kinds)
    feat = D["07"]
    dnav = "".join(f'<li><a href="#{d["id"]}">{esc(DS[d["id"]][0])} <span>{esc(DS[d["id"]][1])}</span></a></li>' for d in EN.DISTRICTS)
    secs = ""
    for d in EN.DISTRICTS:
        ps = [D[n] for n in ORDER if D[n]["district"] == d["id"]]
        name, tag, blurb = DS[d["id"]]
        extra, ncls = "", ""
        if len(ps) == 1:
            ncls = " n1"
            extra = (f'<div class="station-note" id="start"><img src="/assets/aicoachalex-mark-160.webp" alt="AI Coach Alex" width="56" height="56" loading="lazy">'
                     f'<p>{U["station_note"]}</p><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(U["book_station"])}</a></div>')
        secs += f"""<section class="district wrap" id="{d['id']}" aria-labelledby="h-{d['id']}">
  <div class="district-head"><div><div class="eyebrow">{esc(tag)}</div><h2 class="display" id="h-{d['id']}">{esc(name)}</h2></div><p>{esc(blurb)}</p></div>
  <div class="shops{ncls}">{"".join(shop_card(lang, p) for p in ps)}{extra}</div>
</section>"""
    body = f"""<main>
<div class="wrap">
  <nav class="crumbs" aria-label="{esc(U['crumbs'])}"><ol><li><a href="{U['home']}">{esc(U['home_name'])}</a></li><li aria-current="page">{esc(U['hub_name'])}</li></ol></nav>
  <div class="hub-hero">
    <div class="hub-intro">
      <div class="eyebrow">{esc(U['hub_eyebrow'])}</div>
      <h1 class="display">{U['hub_h1']}</h1>
      <p>{esc(U['hub_intro'])}</p>
      <ul class="district-nav">{dnav}</ul>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(U['book'])}</a><a class="btn btn-line" href="{U['owners_href']}">{esc(U['owners'])}</a></div>
    </div>
    <div class="city">{city_svg(lang, symbols)}<p class="city-hint">{esc(U['city_hint'])}</p></div>
  </div>
  <a class="featured" href="{path(lang, feat)}">
    {mini(feat)}
    <div><span class="tag">{esc(U['featured_tag'])}</span><strong>{esc(feat['persona_plain'])}, {esc(feat['country'])}</strong><p>{esc(U['featured_text'])}</p></div>
    <span class="go">{esc(U['see_day'])}</span>
  </a>
</div>
{secs}
{faq_html(U['faq_hub'], U['faq_hub_h'])}
<div class="wrap"><section class="final"><div><h2 class="display">{U['final_h']}</h2><p>{esc(U['final_p'])}</p></div>
<div><a class="btn btn-lime" href="{BOOK}" target="_blank" rel="noopener">{esc(U['book'])} →</a><span class="note">{esc(U['final_note'])}</span></div></section></div>
</main>"""
    hub_url = url(lang)
    schema = {"@context": "https://schema.org", "@graph": [
        PERSON,
        {"@type": "CollectionPage", "@id": hub_url, "url": hub_url, "name": U["hub_name"], "description": U["hub_desc"],
         "inLanguage": lang, "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#alessandro"}, "dateModified": TODAY,
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(ORDER), "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": url(lang, D[n]), "name": f'{D[n]["persona_plain"]}: {D[n]["h1"]}'}
             for i, n in enumerate(ORDER)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": U["home_name"], "item": SITE + U["home"]},
            {"@type": "ListItem", "position": 2, "name": U["hub_name"], "item": hub_url}]},
        faq_schema(U["faq_hub"], hub_url)]}
    return page(lang, U["hub_title"], U["hub_desc"], hub_url, alternates(), schema, body, CITY_JS)


# ---------- workshop ----------
def build_workshop(lang, p):
    D, U, DS = DATA[lang], UI[lang], DIST[lang]
    dname = DS[p["district"]][0]
    nb = [D[n] for n in ORDER if D[n]["district"] == p["district"] and n != p["num"]]
    if len(nb) < 3:
        nb += [D[n] for n in ORDER if D[n]["district"] != p["district"] and D[n] not in nb][: 3 - len(nb)]
    nb = nb[:3]
    symbols = "".join(B.symbol(k) for k in sorted({p["building"]} | {n["building"] for n in nb}))
    page_url = url(lang, p)
    day = "".join(f'<li><time>{t}</time><p class="before">{esc(b)}</p><p class="after">{esc(a)}</p></li>' for t, b, a in p["day"])
    story = "".join(f"<p>{s}</p>" for s in p["story"])
    thoughts = "".join(f"<li>“{esc(s)}”</li>" for s in p["signals"])
    gets = "".join(f"<li>{esc(s)}</li>" for s in p["outcomes"])
    tools = "".join(f'<span class="chip">{esc(t)}</span>' for t in p["tools"])
    lis = "".join(f"<li>{esc(x)}</li>" for x in U["next_li"])
    body = f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{symbols}</defs></svg>
<main>
<div class="wrap">
  <nav class="crumbs" aria-label="{esc(U['crumbs'])}"><ol><li><a href="{U['home']}">{esc(U['home_name'])}</a></li><li><a href="{U['base']}">{esc(U['hub_name'])}</a></li><li><a href="{U['base']}#{p['district']}">{esc(dname)}</a></li><li aria-current="page">{esc(p['persona_plain'])}</li></ol></nav>
  <header class="ws-hero">
    <div>
      <div class="eyebrow">{esc(U['ws_eyebrow'].format(num=p['num'], district=dname))}</div>
      <p class="who">{p['persona']}</p>
      <h1 class="display">{esc(p['h1'])}</h1>
      <div class="ws-meta">{win_badge(p)}<span class="chip">{esc(p['sector'])}</span><span class="chip">{esc(p['country'])}</span></div>
      <p class="answer"><b>{esc(U['in_short'])}</b>{esc(p['answer'])}</p>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(U['book'])}</a><a class="btn btn-line" href="#day">{esc(U['see_day_btn'])}</a></div>
    </div>
    <div class="ws-art"><span class="plate">{esc(U['for_label'])}: {esc(', '.join(p['roles']))}</span><img class="brand" src="/assets/aicoachalex-mark-96.webp" alt="" width="40" height="40">
      <svg viewBox="{vb(p['building'], 14)}" role="img" aria-label="{esc(U['illus'].format(name=p['persona_plain']))}"><use href="#b-{p['building']}" x="0" y="0" width="240" height="300"/></svg></div>
  </header>
</div>

<section class="section wrap" id="day" aria-labelledby="h-day">
  <h2 class="display" id="h-day">{esc(U['day_h'])}</h2>
  <p class="lead">{esc(U['day_lead'])}</p>
  <div class="day"><div class="day-head" aria-hidden="true"><span>{esc(U['t_time'])}</span><span>{esc(U['t_before'])}</span><span>{esc(U['t_after'])}</span></div><ol>{day}</ol></div>
</section>

<section class="section wrap" aria-labelledby="h-story">
  <div class="story">
    <div><h2 class="display" id="h-story">{esc(U['story_h'])}</h2>{story}</div>
    <aside class="outcome" aria-label="{esc(p['win_label'])}"><span class="eyebrow">{esc(p['win_label'])}</span><strong class="big">{esc(p['win'])}</strong><p>{esc(p['result'])}</p><span class="country">{esc(U['based'])}: {esc(p['country'])}</span></aside>
  </div>
</section>

<section class="section wrap" aria-label="{esc(U['thinking'])}">
  <div class="twocol">
    <div><h3>{esc(U['thinking'])}</h3><ul class="thoughts">{thoughts}</ul></div>
    <div><h3>{esc(U['leave'])}</h3><ul class="gets">{gets}</ul></div>
  </div>
  <div class="tools"><b>{esc(U['tools'])}</b>{tools}</div>
</section>

<div class="wrap"><section class="book" aria-label="{esc(U['next_h'])}">
  <div><h2 class="display">{esc(U['next_h'])}</h2><p style="margin:0">{esc(U['next_p'])}</p><ul>{lis}</ul></div>
  <div><div class="price">49€<small>{esc(U['minutes'])}</small></div><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(U['book_btn'])}</a></div>
</section></div>

{faq_html(p['faq'], U['faq_ws_h'])}

<section class="section wrap" aria-labelledby="h-next">
  <h2 class="display" id="h-next">{esc(U['door_h'])}</h2>
  <p class="lead">{esc(U['door_lead'])}</p>
  <div class="next">{"".join(shop_card(lang, n) for n in nb)}<a class="back" href="{U['base']}"><span class="eyebrow">{esc(U['back_to'])}</span><strong>{esc(U['whole_city'])}</strong><span>{esc(U['whole_city_sub'])}</span></a></div>
</section>
</main>"""
    schema = {"@context": "https://schema.org", "@graph": [
        PERSON,
        {"@type": "WebPage", "@id": page_url, "url": page_url, "name": p["title"], "description": p["desc"], "inLanguage": lang,
         "isPartOf": {"@id": SITE + "/#website"}, "dateModified": TODAY, "breadcrumb": {"@id": page_url + "#breadcrumb"},
         "mainEntity": {"@id": page_url + "#service"}, "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer"]}},
        {"@type": "Service", "@id": page_url + "#service", "name": p["h1"], "serviceType": U["service_type"], "description": p["answer"],
         "provider": {"@id": SITE + "/#alessandro"}, "audience": {"@type": "BusinessAudience", "audienceType": f'{p["persona_plain"]} ({p["sector"]})'},
         "areaServed": "Worldwide", "availableLanguage": ["en", "es", "it"], "availableChannel": {"@type": "ServiceChannel", "serviceUrl": BOOK},
         "offers": {"@type": "Offer", "name": U["offer"], "price": "49", "priceCurrency": "EUR", "url": BOOK, "availability": "https://schema.org/InStock"}},
        {"@type": "BreadcrumbList", "@id": page_url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": U["home_name"], "item": SITE + U["home"]},
            {"@type": "ListItem", "position": 2, "name": U["hub_name"], "item": url(lang)},
            {"@type": "ListItem", "position": 3, "name": p["persona_plain"], "item": page_url}]},
        faq_schema(p["faq"], page_url)]}
    return page(lang, p["title"], p["desc"], page_url, alternates(p["num"]), schema, body)


def write(rel, content):
    full = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    write("/assets/wiw.css", read("_navcss.css") + "\n" + read("_page.css"))
    for lang in LANGS:
        write(UI[lang]["base"] + "index.html", build_hub(lang))
        for p in DATA[lang].values():
            write(path(lang, p) + "index.html", build_workshop(lang, p))
    print("built", len(LANGS), "languages x (hub +", len(ORDER), "workshops)")


if __name__ == "__main__":
    main()
