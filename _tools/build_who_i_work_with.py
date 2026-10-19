"""Build /who-i-work-with/ (the client city) and one page per workshop.

Run from the repo root:  python3 _tools/build_who_i_work_with.py
Edit copy in _tools/wiw_content.py, drawings in _tools/wiw_buildings.py.
"""
import html
import json
import math
import os

import wiw_buildings as B
from wiw_content import DISTRICTS, ORDER, P

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "_tools")
SITE = "https://aicoachalex.com"
BASE = "/who-i-work-with/"
BOOK = "https://alessandrocapezza.youcanbook.me/"
SHARE = SITE + "/ALEXAICOACH-SHAREv2.png"
TODAY = "2026-10-19"
CSS_V = "1"

BY_NUM = {p["num"]: p for p in P}
DNAME = {d["id"]: d for d in DISTRICTS}
STATUS = {"Result": ("result", "Result"), "In progress": ("progress", "In progress"),
          "Getting started": ("start", "Getting started"), "Target": ("goal", "Goal set")}


def read(name):
    with open(os.path.join(TOOLS, name), encoding="utf-8") as f:
        return f.read()


def esc(s):
    return html.escape(s, quote=True)


def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def url(p=None):
    return SITE + BASE + (p["slug"] + "/" if p else "")


def chip(status):
    c, label = STATUS[status]
    return f'<span class="chip {c}">{label}</span>'


# ---------------- shared chrome ----------------
HEAD_TRACKING = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-T93CHX6Z');</script>
<!-- End Google Tag Manager -->
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2696345404134131');
fbq('track', 'PageView');
</script>
<!-- End Meta Pixel Code -->"""

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
DIAG_OFFER = {"@type": "Offer", "name": "AI diagnostic (50 minutes, 1:1)", "price": "49",
              "priceCurrency": "EUR", "url": BOOK, "availability": "https://schema.org/InStock"}


def nav(es_href, it_href):
    lang = (f'<div class="sn-lang"><a href="{BASE}" class="on" onclick="try{{localStorage.setItem(\'preferred-lang\',\'en\')}}catch(e){{}}">EN</a>'
            f'<span class="sep">·</span><a href="{es_href}" onclick="try{{localStorage.setItem(\'preferred-lang\',\'es\')}}catch(e){{}}">ES</a>'
            f'<span class="sep">·</span><a href="{it_href}" onclick="try{{localStorage.setItem(\'preferred-lang\',\'it\')}}catch(e){{}}">IT</a></div>')
    courses = ('<a href="/personal-ai-agent.html">Your Own AI</a><a href="/ai-video-course-booking.html">AI VideoGen</a>'
               '<a href="/voice-ai-agents.html">Voice AI Agents</a><a href="/personal-ai-setup.html">Personal AI Setup</a><a href="/120-prompts.html">120 Prompts</a>')
    mob_courses = courses.replace('<a href=', '<a class="sn-mob-course" href=')
    return f"""<div class="sn" id="siteNav" role="navigation" aria-label="Menu">
  <div class="sn-in">
    <a class="sn-logo" href="/" aria-label="AI Coach Alex"><img src="/assets/aicoachalex-mark-96.webp" alt="AI Coach Alex" width="38" height="38"></a>
    <div class="sn-links">
      <a href="/#method">Method</a>
      <a class="nav-quiz" href="/career-risk-assessment.html">Risk Quiz</a>
      <a href="/blog/">Blog</a>
      <a href="/openclaw-ai-agent-setup.html">Configure OpenClaw Agent</a>
      <div class="sn-dd"><a class="sn-dd-t" href="/courses.html" aria-haspopup="true" aria-expanded="false">Courses <span aria-hidden="true">&#9662;</span></a><div class="sn-dd-m">{courses}</div></div>
      <a href="{BASE}" class="sn-cur">Who I Work With</a>
    </div>
    <div class="sn-right">
      {lang}
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
    {mob_courses}
    <a href="{BASE}" class="sn-cur">Who I Work With</a>
    {lang}
    <a class="sn-cta-m sn-cta" href="{BOOK}" target="_blank" rel="noopener">Book Diagnostic</a>
  </div>
</div>"""


def footer():
    links = [(BASE, "Who I Work With"), ("/ai-for-business-owners.html", "AI for Business Owners"),
             ("/personal-ai-agent.html", "Your Own AI"), ("/ai-video-course-booking.html", "AI VideoGen"),
             ("/voice-ai-agents.html", "Voice AI Agents"), ("/personal-ai-setup.html", "Personal AI Setup"),
             ("/120-prompts.html", "120 Prompts"), ("/openclaw-ai-agent-setup.html", "OpenClaw Agent Setup"),
             ("/blog/", "Blog"), ("https://www.linkedin.com/in/alessandrocapezza/", "LinkedIn"),
             ("https://www.instagram.com/alexislimitless/", "Instagram"), ("https://x.com/alexNomads", "X")]
    a = "".join(f'<a href="{h}"' + (' target="_blank" rel="noopener"' if h.startswith("http") else "") + f'>{t}</a>' for h, t in links)
    return f"""<footer class="foot"><div class="wrap foot-in">
  <div class="foot-brand"><img src="/assets/aicoachalex-mark-96.webp" alt="" width="48" height="48" loading="lazy"><div><b>Alessandro Capezza</b><span>AI Coach · Barcelona</span></div></div>
  <nav aria-label="Footer">{a}</nav>
  <p class="copy">Every workshop in this city is a real coaching engagement. Names, cities and identifying figures are removed. Contact: aicoachalex@gmail.com</p>
</div></footer>"""


def page(title, desc, canonical, alternates, schema, body, es_href, it_href, og_type="website"):
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{h}">\n' for l, h in alternates)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{alt}<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:site_name" content="AI Coach Alex">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
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
{nav(es_href, it_href)}
{body}
{footer()}
{BOOKING}
{NAVJS}
</body>
</html>
"""


BOOKING = read("_booking_block.html")
NAVJS = read("_navjs_block.html")


# ---------------- city map (hub hero) ----------------
POS = {"01": (0, 0), "07": (2.1, 0), "08": (0, 2.1), "12": (2.1, 2.1),
       "09": (4.3, 0), "02": (6.4, 0), "11": (4.3, 2.1), "13": (6.4, 2.1),
       "03": (0, 4.3), "04": (2.1, 4.3), "05": (0, 6.4), "10": (2.1, 6.4),
       "hq": (4.4, 4.4), "06": (6.4, 5.4)}
CELL, CX, CY, SCALE = 70, 520, 205, .84
W_SYM, H_SYM = 240 * SCALE, 300 * SCALE


def gs(gx, gy):
    return (CX + (gx - gy) * CELL * B.C, CY + (gx + gy) * CELL * .5)


def gpoly(cells, cls="", fill=None, extra=""):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (gs(*c) for c in cells))
    f = f' fill="{fill}"' if fill else ""
    c = f' class="{cls}"' if cls else ""
    return f'<polygon{c}{f} points="{pts}"{extra}/>'


def city_svg(symbols):
    o = []
    lo, hi = -1.2, 7.9
    o.append(gpoly([(lo + .25, lo + .9), (hi + .25, lo + .9), (hi + .25, hi + .9), (lo + .25, hi + .9)], fill="#163300", extra=' opacity=".08"'))
    o.append(gpoly([(lo, lo), (hi, lo), (hi, hi), (lo, hi)], cls="ground", extra=' stroke="#0d0c0a" stroke-width="1.2"'))
    # roads
    r0, r1 = 3.15, 3.95
    o.append(gpoly([(r0, lo), (r1, lo), (r1, hi), (r0, hi)], fill="#d6cdb8"))
    o.append(gpoly([(lo, r0), (hi, r0), (hi, r1), (lo, r1)], fill="#d6cdb8"))
    m = (r0 + r1) / 2
    (ax, ay), (bx, by) = gs(m, lo + .3), gs(m, hi - .3)
    o.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#9fe870" stroke-width="2.5" stroke-dasharray="10 12"/>')
    (ax, ay), (bx, by) = gs(lo + .3, m), gs(hi - .3, m)
    o.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#9fe870" stroke-width="2.5" stroke-dasharray="10 12"/>')
    # buildings, back to front
    items = sorted(POS.items(), key=lambda kv: kv[1][0] + kv[1][1])
    for key, (gx, gy) in items:
        X, Y = gs(gx + .9, gy + .9)
        x, y = X - B.ANCHOR[0] * SCALE, Y - B.ANCHOR[1] * SCALE
        if key == "hq":
            o.append(f'<a class="bld" href="#start" aria-label="AI Coach Alex studio: start here"><use href="#b-hq" x="{x:.1f}" y="{y:.1f}" width="{W_SYM:.1f}" height="{H_SYM:.1f}"/>'
                     f'<g class="lbl"><rect x="{X-78:.1f}" y="{Y+22:.1f}" width="156" height="30" rx="15"/><text x="{X:.1f}" y="{Y+41:.1f}" text-anchor="middle">Start here: the studio</text></g></a>')
            continue
        p = BY_NUM[key]
        name = p["persona_plain"]
        w = max(150, 7.2 * len(name) + 46)
        o.append(f'<a class="bld" href="{BASE}{p["slug"]}/" aria-label="Workshop {p["num"]}: {esc(name)}, {esc(p["sector"])}">'
                 f'<title>{esc(name)}: {esc(p["sector"])}</title>'
                 f'<use href="#b-{p["building"]}" x="{x:.1f}" y="{y:.1f}" width="{W_SYM:.1f}" height="{H_SYM:.1f}"/>'
                 f'<g class="lbl"><rect x="{X-w/2:.1f}" y="{Y+22:.1f}" width="{w:.1f}" height="30" rx="15"/>'
                 f'<text x="{X-w/2+14:.1f}" y="{Y+41:.1f}"><tspan class="n">{p["num"]}</tspan>  {esc(name)}</text></g></a>')
    # district signs
    signs = [("old-town", 1.0, -1.05), ("business-district", 5.4, -1.05), ("market-square", -1.05, 5.4), ("the-station", 7.6, 4.2)]
    for did, gx, gy in signs:
        X, Y = gs(gx, gy)
        name = DNAME[did]["name"].upper()
        w = 9 * len(name) + 26
        o.append(f'<a class="dsign" href="#{did}"><rect x="{X-w/2:.1f}" y="{Y-15:.1f}" width="{w:.1f}" height="26" rx="13"/>'
                 f'<text x="{X:.1f}" y="{Y+2:.1f}" text-anchor="middle">{name}</text></a>')
    return (f'<svg viewBox="0 0 1040 760" role="img" aria-labelledby="cityTitle">'
            f'<title id="cityTitle">Map of the client city: 13 workshops in four districts around the AI Coach Alex studio</title>'
            f'<defs>{symbols}</defs>{"".join(o)}</svg>')


def mini(p, cls=""):
    return f'<svg viewBox="0 0 240 300" aria-hidden="true"{cls}><use href="#b-{p["building"]}"/></svg>'


def shop_card(p, tag="h3"):
    one = strip(p["result"]).split(". ")[0].rstrip(".") + "."
    return f"""<a class="shop" href="{BASE}{p['slug']}/">
  <div class="art">{mini(p)}</div>
  <div class="meta"><span class="num">{p['num']}</span>{chip(p['status'])}</div>
  <{tag}>{p['persona']}</{tag}>
  <p class="sec">{esc(p['sector'])} · {esc(p['country'])}</p>
  <p class="one">{esc(one)}</p>
  <span class="see">Visit the workshop →</span>
</a>"""


# ---------------- hub ----------------
HUB_FAQ = [
    ("Who does AI Coach Alex work with?", "Owners, operators, leaders and professionals who want AI as a working tool: event companies, electricians, construction firms, clinics, accountants, CEOs, real estate agents, marketers and salespeople, plus individuals changing career. Each workshop in this city is a real, anonymised engagement."),
    ("Are these real clients?", "Yes. Names, cities and identifying figures are removed; the country, or continent, is kept. Each workshop is marked Result, In progress or Getting started, so you can see where it stands."),
    ("Do I need to be technical?", "No. Most clients start non-technical. Lessons are 50 minutes, one to one, and built around your own files, tools and daily work."),
    ("How do we start?", "With a 50-minute diagnostic for 49€. We map where AI fits your work and decide what to build first. You leave with that map whether or not we continue."),
]


def faq_html(items, heading):
    d = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in items)
    return f'<section class="faq wrap" id="faq"><h2 class="display">{heading}</h2>{d}</section>'


def faq_schema(items, page_url):
    return {"@type": "FAQPage", "@id": page_url + "#faq",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def build_hub():
    kinds = sorted({p["building"] for p in P}) + ["hq"]
    symbols = "".join(B.symbol(k) for k in kinds)
    feat = BY_NUM["07"]
    dnav = "".join(f'<li><a href="#{d["id"]}">{d["name"]} <span>{d["tag"]}</span></a></li>' for d in DISTRICTS)
    districts = ""
    for d in DISTRICTS:
        ps = [BY_NUM[n] for n in ORDER if BY_NUM[n]["district"] == d["id"]]
        cards = "".join(shop_card(p) for p in ps)
        extra, ncls = "", ""
        if len(ps) == 1:
            ncls = " n1"
            extra = (f'<div class="station-note" id="start"><img src="/assets/aicoachalex-mark-160.webp" alt="AI Coach Alex" width="56" height="56" loading="lazy">'
                     f'<p><strong>Every journey starts at the studio.</strong> Not sure which workshop is yours? The 50-minute diagnostic maps where AI fits your work and what to build first.</p>'
                     f'<a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">Book the diagnostic — 49€</a></div>')
        districts += f"""<section class="district wrap" id="{d['id']}" aria-labelledby="h-{d['id']}">
  <div class="district-head"><div><div class="eyebrow">{d['tag']}</div><h2 class="display" id="h-{d['id']}">{d['name']}</h2></div><p>{d['blurb']}</p></div>
  <div class="shops{ncls}">{cards}{extra}</div>
</section>"""
    body = f"""<main>
<div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Who I work with</li></ol></nav>
  <div class="hub-hero">
    <div class="hub-intro">
      <div class="eyebrow">13 workshops · 4 districts · real engagements</div>
      <h1 class="display">Who I work <em>with</em></h1>
      <p>A small city of real businesses, each with its own AI workshop. Walk in to see a day in the life of that business, what we built with AI, and where it stands today.</p>
      <ul class="district-nav">{dnav}</ul>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">Book a diagnostic — 49€</a><a class="btn btn-line" href="/ai-for-business-owners.html">For business owners</a></div>
    </div>
    <div class="city">{city_svg(symbols)}<p class="city-hint">Click a building to walk into its workshop.</p></div>
  </div>
  <a class="featured" href="{BASE}{feat['slug']}/">
    {mini(feat)}
    <div><span class="tag">New in the city</span><strong>{strip(feat['persona'])}, {esc(feat['country'])}</strong><p>The first test of the AI workspace caught an overdue payment the owner didn't know about.</p></div>
    <span class="go">See a day in the life →</span>
  </a>
</div>
{districts}
{faq_html(HUB_FAQ, "Questions about who I work with")}
<div class="wrap"><section class="final"><div><h2 class="display">Don't see your business? <em>That's the call.</em></h2><p>In 50 minutes we map where you are, what's at stake and what to build first. You leave with a clear plan, whether we keep working together or not.</p></div>
<div><a class="btn btn-lime" href="{BOOK}" target="_blank" rel="noopener">Book Diagnostic — 49€ →</a><span class="note">50 min · 1:1 · not a sales pitch</span></div></section></div>
</main>"""
    hub_url = url()
    schema = {"@context": "https://schema.org", "@graph": [
        PERSON,
        {"@type": "CollectionPage", "@id": hub_url, "url": hub_url, "name": "Who I work with",
         "description": HUB_DESC, "inLanguage": "en", "isPartOf": {"@id": SITE + "/#website"},
         "about": {"@id": SITE + "/#alessandro"}, "dateModified": TODAY,
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(P), "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": url(BY_NUM[n]), "name": f'{BY_NUM[n]["persona_plain"]}: {BY_NUM[n]["h1"]}'}
             for i, n in enumerate(ORDER)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Who I work with", "item": hub_url}]},
        faq_schema(HUB_FAQ, hub_url)]}
    alts = [("en", hub_url), ("es", SITE + "/who-i-work-with.es.html"), ("it", SITE + "/who-i-work-with.it.html"), ("x-default", hub_url)]
    return page(HUB_TITLE, HUB_DESC, hub_url, alts, schema, body, "/who-i-work-with.es.html", "/who-i-work-with.it.html")


HUB_TITLE = "Who I Work With: AI Coaching Clients by Industry | AI Coach Alex"
HUB_DESC = ("Real, anonymised AI coaching clients: event companies, electricians, construction, clinics, CEOs, "
            "real estate agents and more. A day in the life of each.")


# ---------------- workshop page ----------------
def build_workshop(p):
    d = DNAME[p["district"]]
    neighbours = [BY_NUM[n] for n in ORDER if BY_NUM[n]["district"] == p["district"] and n != p["num"]]
    if len(neighbours) < 3:
        neighbours += [BY_NUM[n] for n in ORDER if BY_NUM[n]["district"] != p["district"] and BY_NUM[n] not in neighbours][: 3 - len(neighbours)]
    kinds = sorted({p["building"]} | {n["building"] for n in neighbours})
    symbols = "".join(B.symbol(k) for k in kinds)
    page_url = url(p)
    day = "".join(f'<li><time>{t}</time><p class="before">{esc(b)}</p><p class="after">{esc(a)}</p></li>' for t, b, a in p["day"])
    story = "".join(f"<p>{s}</p>" for s in p["story"])
    thoughts = "".join(f"<li>“{esc(s)}”</li>" for s in p["signals"])
    gets = "".join(f"<li>{esc(s)}</li>" for s in p["outcomes"])
    tools = "".join(f'<span class="chip">{esc(t)}</span>' for t in p["tools"])
    roles = ", ".join(p["roles"])
    next_cards = "".join(shop_card(n, tag="h3") for n in neighbours[:3])
    body = f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{symbols}</defs></svg>
<main>
<div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="{BASE}">Who I work with</a></li><li><a href="{BASE}#{d['id']}">{d['name']}</a></li><li aria-current="page">{esc(p['persona_plain'])}</li></ol></nav>
  <header class="ws-hero">
    <div>
      <div class="eyebrow">Workshop {p['num']} · {d['name']}</div>
      <p class="who">{p['persona']}</p>
      <h1 class="display">{esc(p['h1'])}</h1>
      <div class="ws-meta">{chip(p['status'])}<span class="chip">{esc(p['sector'])}</span><span class="chip">{esc(p['country'])}</span></div>
      <p class="answer"><b>In short</b>{esc(p['answer'])}</p>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">Book a diagnostic — 49€</a><a class="btn btn-line" href="#day">See a day in the life ↓</a></div>
    </div>
    <div class="ws-art"><span class="plate">For: {esc(roles)}</span><img class="brand" src="/assets/aicoachalex-mark-96.webp" alt="" width="40" height="40">
      <svg viewBox="{'0 0 240 300' if p['building'] in ('tower','crane') else '0 50 240 250'}" role="img" aria-label="Illustration of the {esc(p['persona_plain'])} workshop"><use href="#b-{p['building']}"/></svg></div>
  </header>
</div>

<section class="section wrap" id="day" aria-labelledby="h-day">
  <h2 class="display" id="h-day">A day in the life</h2>
  <p class="lead">The same working day, before and after AI joined the team. Hours are typical, not exact.</p>
  <div class="day"><div class="day-head" aria-hidden="true"><span>Time</span><span>Before</span><span>With AI</span></div><ol>{day}</ol></div>
</section>

<section class="section wrap" aria-labelledby="h-story">
  <div class="story">
    <div><h2 class="display" id="h-story">The real engagement</h2>{story}</div>
    <aside class="outcome" aria-label="Where it stands">{chip(p['status'])}<p>{esc(p['result'])}</p><span class="country">Client based in: {esc(p['country'])}</span></aside>
  </div>
</section>

<section class="section wrap" aria-label="Is this you?">
  <div class="twocol">
    <div><h3>You find yourself thinking…</h3><ul class="thoughts">{thoughts}</ul></div>
    <div><h3>What you'll leave with</h3><ul class="gets">{gets}</ul></div>
  </div>
  <div class="tools"><b>Tools in this workshop</b>{tools}</div>
</section>

<div class="wrap"><section class="book" aria-label="Book a diagnostic">
  <div><h2 class="display">Your next step</h2><p style="margin:0">A 50-minute diagnostic on your own business. We map where AI fits and what to build first.</p>
  <ul><li>1:1, online</li><li>Your files, your tools</li><li>A written plan after the call</li></ul></div>
  <div><div class="price">49€<small>50 minutes</small></div><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">Book Diagnostic →</a></div>
</section></div>

{faq_html(p['faq'], "Questions from this workshop")}

<section class="section wrap" aria-labelledby="h-next">
  <h2 class="display" id="h-next">Next door</h2>
  <p class="lead">Other workshops nearby in the city.</p>
  <div class="next">{next_cards}<a class="back" href="{BASE}"><span class="eyebrow">Back to</span><strong>The whole city →</strong><span>13 workshops in four districts</span></a></div>
</section>
</main>"""
    schema = {"@context": "https://schema.org", "@graph": [
        PERSON,
        {"@type": "WebPage", "@id": page_url, "url": page_url, "name": p["title"], "description": p["desc"],
         "inLanguage": "en", "isPartOf": {"@id": SITE + "/#website"}, "dateModified": TODAY,
         "breadcrumb": {"@id": page_url + "#breadcrumb"}, "mainEntity": {"@id": page_url + "#service"},
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer"]}},
        {"@type": "Service", "@id": page_url + "#service", "name": p["h1"], "serviceType": "AI coaching",
         "description": p["answer"], "provider": {"@id": SITE + "/#alessandro"},
         "audience": {"@type": "BusinessAudience", "audienceType": f'{p["persona_plain"]} ({p["sector"]})'},
         "areaServed": "Worldwide", "availableChannel": {"@type": "ServiceChannel", "serviceUrl": BOOK},
         "offers": DIAG_OFFER},
        {"@type": "BreadcrumbList", "@id": page_url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Who I work with", "item": url()},
            {"@type": "ListItem", "position": 3, "name": p["persona_plain"], "item": page_url}]},
        faq_schema(p["faq"], page_url)]}
    alts = [("en", page_url), ("x-default", page_url)]
    return page(p["title"], p["desc"], page_url, alts, schema, body, "/who-i-work-with.es.html", "/who-i-work-with.it.html")


def main():
    css = read("_navcss.css") + "\n" + read("_page.css")
    with open(os.path.join(ROOT, "assets", "wiw.css"), "w", encoding="utf-8") as f:
        f.write(css)
    out = os.path.join(ROOT, "who-i-work-with")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_hub())
    for p in P:
        d = os.path.join(out, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(build_workshop(p))
    print("built hub +", len(P), "workshops")


if __name__ == "__main__":
    main()
