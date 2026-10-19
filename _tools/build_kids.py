"""Build the AI lessons for kids pages (EN/ES/IT): an island hub for parents + 6 track pages.

Run from the repo root:  python3 _tools/build_kids.py
Copy: _tools/kids_content.py. Shares chrome with build_who_i_work_with.py.
"""
import json
import os
import re

import build_who_i_work_with as G
import wiw_buildings as B
from kids_content import K, PRICE, TRACK_ORDER, BUILDING

ROOT, SITE, BOOK, LANGS, esc = G.ROOT, G.SITE, G.BOOK, G.LANGS, G.esc
TODAY = "2026-10-19"


def money(s):
    return s.format(**PRICE)


def url(lang, t=None):
    return SITE + K[lang]["base"] + (K[lang]["tracks"][t]["slug"] + "/" if t else "")


def path(lang, t=None):
    return K[lang]["base"] + (K[lang]["tracks"][t]["slug"] + "/" if t else "")


def alts(t=None):
    out = [(l, url(l, t)) for l in LANGS]
    return out + [("x-default", url("en", t))]


def vb(kind, pad=10):
    return G.vb(kind, pad)


def art(kind, cls=""):
    return f'<svg viewBox="{vb(kind)}" aria-hidden="true"{cls}><use href="#b-{kind}" x="0" y="0" width="240" height="300"/></svg>'


def mark_current(html, lang):
    html = html.replace(' class="sn-cur"', "")
    kb = K[lang]["base"]
    html = re.sub(r'(<a href="%s")(>)' % re.escape(kb), r'\1 class="sn-cur"\2', html, count=2)
    return html


def track_card(lang, t):
    tr, k = K[lang]["tracks"][t], K[lang]
    return f"""<a class="shop" href="{path(lang, t)}">
  <div class="art">{art(BUILDING[t])}</div>
  <span class="win"><small>{esc(k['for_ages'])}</small>{esc(tr['ages'])}</span>
  <h3>{esc(tr['name'])}</h3>
  <p class="sec">{esc(tr['h1'])}</p>
</a>"""


def course_schema(lang, t):
    k, tr = K[lang], K[lang]["tracks"][t]
    lo, hi = tr["ages"].replace("–", "-").split("-")
    return {"@type": "Course", "@id": url(lang, t) + "#course", "url": url(lang, t), "name": tr["h1"], "description": tr["answer"],
            "inLanguage": lang, "provider": {"@id": SITE + "/#alessandro"},
            "audience": {"@type": "EducationalAudience", "educationalRole": "student", "audienceType": f"Kids and teenagers {tr['ages']}"},
            "typicalAgeRange": f"{lo}-{hi}", "educationalLevel": "Beginner",
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": "PT50M",
                                  "instructor": {"@id": SITE + "/#alessandro"}},
            "offers": {"@type": "Offer", "price": "65", "priceCurrency": "EUR", "category": "Paid", "url": BOOK}}


# ---------- the island ----------
CELL, CX, CY, SC = 66, 520, 165, .84
W_SYM, H_SYM = 240 * SC, 300 * SC
POS = {"lab": (0.0, 1.9), "time": (1.9, 0.0), "market": (3.8, 0.4), "court": (0.4, 3.8), "studio": (2.4, 2.4), "hq": (4.3, 2.5), "light": (2.6, 4.5)}


def gs(gx, gy):
    return (CX + (gx - gy) * CELL * B.C, CY + (gx + gy) * CELL * .5)


def gpoly(cells, fill, extra=""):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in (gs(*c) for c in cells))}" fill="{fill}"{extra}/>'


def island(lang):
    k = K[lang]
    o = []
    wlo, whi, lo, hi = -1.75, 7.15, -0.9, 6.3
    o.append(gpoly([(wlo, wlo), (whi, wlo), (whi, whi), (wlo, whi)], "#d4e8e2", ' stroke="#0d0c0a" stroke-width="1.2"'))
    # waves
    for i, (a, b) in enumerate([((wlo + .6, -1.6), (whi - .6, -1.6)), ((7.2, wlo + .6), (7.2, whi - .6)), ((-1.7, wlo + .8), (-1.7, whi - .8)), ((wlo + .8, 7.3), (whi - .8, 7.3))]):
        (ax, ay), (bx, by) = gs(*a), gs(*b)
        o.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#ffffff" stroke-width="2" stroke-dasharray="14 22" stroke-linecap="round" opacity=".9">'
                 f'<animate attributeName="stroke-dashoffset" from="0" to="-72" dur="{6+i}s" repeatCount="indefinite"/></line>')
    # boats
    for i, (a, b, dur, beg) in enumerate([((wlo + .5, 7.0), (whi - .5, 7.0), 40, 0), ((7.0, whi - .5), (7.0, wlo + .5), 48, 18)]):
        (ax, ay), (bx, by) = gs(*a), gs(*b)
        boat = ('<path class="k" d="M-12,0 L12,0 L8,6 L-8,6 Z" fill="#163300"/><path d="M0,0 V-22" stroke="#0d0c0a" stroke-width="1.6"/>'
                f'<path class="k" d="M1,-21 L14,-3 L1,-3 Z" fill="{["#f8f6f1", "#9fe870"][i]}"/>')
        o.append(f'<g class="boat">{boat}<animateMotion dur="{dur}s" begin="-{beg}s" repeatCount="indefinite" path="M{ax:.1f},{ay:.1f} L{bx:.1f},{by:.1f}"/></g>')
    # island: sand rim + grass
    o.append(gpoly([(lo - .35, lo - .35), (hi + .35, lo - .35), (hi + .35, hi + .35), (lo - .35, hi + .35)], "#e9dcb8", ' stroke="#0d0c0a" stroke-width="1.1"'))
    o.append(gpoly([(lo, lo), (hi, lo), (hi, hi), (lo, hi)], "#dfe9c9", ' class="ground" stroke="#0d0c0a" stroke-width="1.1"'))
    # footpath loop between the buildings
    loop = [(1.2, 3.3), (1.6, 1.6), (3.4, 1.4), (4.2, 2.0), (4.2, 4.0), (3.4, 4.3), (1.6, 4.2), (1.2, 3.3)]
    d = "M" + " L".join(f"{gs(*p)[0]:.1f},{gs(*p)[1]:.1f}" for p in loop)
    o.append(f'<path d="{d}" fill="none" stroke="#e9dcb8" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>')
    o.append(f'<path d="{d}" fill="none" stroke="#d6c79f" stroke-width="2" stroke-dasharray="3 9" stroke-linecap="round"/>')
    # buildings, trees and kids back to front
    trees = [(-0.5, 0.3), (0.9, -0.6), (5.6, -0.4), (6.1, 1.5), (-0.6, 5.6), (5.9, 4.3), (4.9, 6.0), (1.3, 6.0), (3.2, 3.15)]
    items = [(k_, p) for k_, p in POS.items()] + [(f"t{i}", t) for i, t in enumerate(trees)]
    tops = {}
    for key, (gx, gy) in sorted(items, key=lambda kv: kv[1][0] + kv[1][1]):
        if key.startswith("t"):
            X, Y = gs(gx, gy)
            o.append(f'<g><line x1="{X:.1f}" y1="{Y:.1f}" x2="{X:.1f}" y2="{Y-14:.1f}" stroke="#6b4f2e" stroke-width="3"/><circle class="k" cx="{X:.1f}" cy="{Y-21:.1f}" r="11" fill="#3d6b22"/><circle cx="{X-3.5:.1f}" cy="{Y-24.5:.1f}" r="3.8" fill="#6f9a4f"/></g>')
            continue
        kind = "hq" if key == "hq" else BUILDING[key]
        X, Y = gs(gx + .68, gy + .68)
        x, y = X - B.ANCHOR[0] * SC, Y - B.ANCHOR[1] * SC
        tops[key] = (X, y + G.BBOX[kind][1] * SC)
        if key == "hq":
            o.append(f'<a class="bld" data-k="hq" href="#book" aria-label="AI Coach Alex"><use href="#b-hq" x="{x:.1f}" y="{y:.1f}" width="{W_SYM:.1f}" height="{H_SYM:.1f}"/></a>')
        else:
            tr = k["tracks"][key]
            o.append(f'<a class="bld" data-k="{key}" href="{path(lang, key)}" aria-label="{esc(tr["name"])}: {esc(tr["h1"])}"><use href="#b-{kind}" x="{x:.1f}" y="{y:.1f}" width="{W_SYM:.1f}" height="{H_SYM:.1f}"/></a>')
    kids = []
    cols = ["#e8b04b", "#9fe870", "#163300", "#e88b8b", "#3d6b22", "#f8f6f1"]
    for i in range(6):
        dur, beg = 38 + i * 3, i * 7
        kids.append(f'<g class="walker"><circle r="2.4" cy="-10" fill="#e9c9a7" class="k" stroke-width=".8"/>'
                    f'<path d="M-2.4,-7.4 h4.8 v5.4 h-4.8z" fill="{cols[i]}" class="k" stroke-width=".8"/><path d="M-1.5,-2 v2.6 M1.5,-2 v2.6" stroke="#0d0c0a" stroke-width="1"/>'
                    f'<animateMotion dur="{dur}s" begin="-{beg}s" repeatCount="indefinite" path="{d}"/></g>')
    o.append("".join(kids))
    # sky
    rays = "".join(f'<line x1="0" y1="-32" x2="0" y2="-42" stroke="#e8b04b" stroke-width="3" stroke-linecap="round" transform="rotate({a})"/>' for a in range(0, 360, 30))
    stars = "".join(f'<path d="M{x},{y} l2,5 l5,2 l-5,2 l-2,5 l-2,-5 l-5,-2 l5,-2z" fill="#163300"><animate attributeName="opacity" values=".15;.8;.15" dur="{dd}s" repeatCount="indefinite"/></path>'
                    for x, y, dd in [(-95, 10, 3), (70, -30, 4), (135, 40, 5), (-45, 75, 3.5)])
    o.insert(0, f'<g class="sky" transform="translate(120,70)"><g class="sun"><g>{rays}<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="60s" repeatCount="indefinite"/></g>'
                '<circle r="24" fill="#f3c55a" class="k"/><circle r="15" fill="#f8dc8a"/></g>'
                f'<g class="moon"><circle r="24" fill="#ffffff" class="k"/><circle cx="-7" cy="-5" r="5" fill="#ecebe6"/><circle cx="8" cy="7" r="3.5" fill="#ecebe6"/>{stars}</g></g>')
    birds = "".join(f'<g class="bird"><path d="M0,0 q5,-6 10,0 q5,-6 10,0" fill="none" stroke="#0d0c0a" stroke-width="1.6" stroke-linecap="round">'
                    f'<animate attributeName="d" values="M0,0 q5,-6 10,0 q5,-6 10,0;M0,0 q5,3 10,0 q5,3 10,0;M0,0 q5,-6 10,0 q5,-6 10,0" dur=".8s" repeatCount="indefinite"/></path>'
                    f'<animateMotion dur="{dur}s" begin="-{beg}s" repeatCount="indefinite" path="M-60,{y} C300,{y-30} 700,{y+30} 1100,{y-10}"/></g>'
                    for y, dur, beg in [(60, 30, 0), (110, 37, 15), (40, 26, 8)])
    o.append(birds)
    labels = []
    for key, (X, Ytop) in tops.items():
        text = "AI Coach Alex" if key == "hq" else k["tracks"][key]["name"]
        w = 8.2 * len(text) + 30
        lx, ly = min(max(X - w / 2, 8), 1032 - w), max(Ytop - 44, 6)
        labels.append(f'<g class="lbl" data-for="{key}" data-cx="{X:.1f}"><rect x="{lx:.1f}" y="{ly:.1f}" width="{w:.1f}" height="30" rx="15"/>'
                      f'<path d="M{X-6:.1f},{ly+29:.1f} l6,7 l6,-7z"/><text x="{lx+14:.1f}" y="{ly+19.5:.1f}">{esc(text)}</text></g>')
    o.append('<g class="labels" aria-hidden="true">' + "".join(labels) + "</g>")
    symbols = "".join(B.symbol(s) for s in sorted(set(BUILDING.values()) | {"hq"}))
    return (f'<svg id="cityMap" viewBox="0 0 1040 760" role="img" aria-labelledby="islandTitle"><title id="islandTitle">{esc(k["island_title"])}</title>'
            f'<defs>{symbols}</defs>{"".join(o)}</svg>')


# ---------- pages ----------
def plans_html(lang):
    k = K[lang]
    cards = ""
    for name, price, sub, items in k["plans"]:
        lis = "".join(f"<li>{esc(i)}</li>" for i in items)
        cards += f'<div class="plan"><h3>{esc(name)}</h3><div class="pp">{esc(money(price))}</div><p class="ps">{esc(money(sub))}</p><ul>{lis}</ul></div>'
    return cards


def hub(lang):
    k = K[lang]
    promises = "".join(f'<div class="promise"><span class="pn">{i+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for i, (a, b) in enumerate(k["promises"]))
    cards = "".join(track_card(lang, t) for t in TRACK_ORDER)
    lesson = "".join(f'<li><time>{a}′</time><div><b>{esc(b)}</b><p>{esc(c)}</p></div></li>' for a, b, c in k["lesson"])
    recap = "".join(f"<li>{esc(r)}</li>" for r in k["recap"])
    projects = "".join(f'<article class="project"><span class="eyebrow">{esc(a)}</span><h3>{esc(b)}</h3><p>{esc(c)}</p></article>' for a, b, c in k["projects"])
    safety = "".join(f'<div class="rule"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in k["safety"])
    body = f"""<main>
<div class="wrap">
  <nav class="crumbs" aria-label="{esc(k['crumbs'])}"><ol><li><a href="{k['home']}">{esc(k['home_name'])}</a></li><li aria-current="page">{esc(k['hub_name'])}</li></ol></nav>
  <div class="hub-hero kids-hero">
    <div class="hub-intro">
      <div class="eyebrow">{esc(k['eyebrow'])}</div>
      <h1 class="display">{k['h1']}</h1>
      <p>{esc(k['intro'])}</p>
      <p class="price-line">{esc(money(k['price_line']))}</p>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(k['cta'])}</a><a class="btn btn-line" href="#tracks">{esc(k['cta2'])}</a></div>
    </div>
    <div class="city island">{island(lang)}<p class="city-hint">{esc(k['island_hint'])}</p></div>
  </div>
</div>
<section class="section wrap" aria-labelledby="h-prom"><h2 class="display" id="h-prom">{esc(k['promises_h'])}</h2><div class="promises">{promises}</div></section>
<section class="section wrap" id="tracks" aria-labelledby="h-tracks"><h2 class="display" id="h-tracks">{esc(k['tracks_h'])}</h2><p class="lead">{esc(k['tracks_lead'])}</p><div class="shops tracks">{cards}</div></section>
<section class="section wrap" aria-labelledby="h-lesson"><div class="story">
  <div><h2 class="display" id="h-lesson">{esc(k['lesson_h'])}</h2><p class="lead">{esc(k['lesson_lead'])}</p><ol class="steps">{lesson}</ol></div>
  <aside class="outcome"><span class="eyebrow">{esc(k['recap_h'])}</span><ul class="recap">{recap}</ul></aside>
</div></section>
<section class="section wrap" aria-labelledby="h-proj"><h2 class="display" id="h-proj">{esc(k['projects_h'])}</h2><p class="lead">{esc(k['projects_note'])}</p><div class="projects">{projects}</div></section>
<section class="section wrap" id="try" aria-labelledby="h-try"><h2 class="display" id="h-try">{esc(k['try_h'])}</h2><p class="lead">{esc(k['try_p'])}</p>
  <div class="wm"><iframe src="{k['wm_path']}" title="{esc(k['wm_title'])}" loading="lazy"></iframe></div>
  <p><a class="btn btn-line" href="{k['wm_path']}">{esc(k['try_btn'])} ↗</a></p></section>
<section class="section wrap" aria-labelledby="h-safe"><h2 class="display" id="h-safe">{esc(k['safety_h'])}</h2><div class="rules">{safety}</div></section>
<section class="section wrap" id="book" aria-labelledby="h-price"><h2 class="display" id="h-price">{esc(k['pricing_h'])}</h2><div class="plans">{plans_html(lang)}</div><p class="lead small">{esc(k['plans_note'])}</p>
  <p><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])} →</a> <span class="eyebrow">{esc(k['call_note'])}</span></p></section>
{G.faq_html(k['faq'], k['faq_h'])}
<div class="wrap"><section class="final"><div><h2 class="display">{k['final_h']}</h2><p>{esc(k['final_p'])}</p></div>
<div><a class="btn btn-lime" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])} →</a><span class="note">{esc(k['call_note'])}</span></div></section></div>
</main>"""
    u = url(lang)
    schema = {"@context": "https://schema.org", "@graph": [
        G.PERSON,
        {"@type": "CollectionPage", "@id": u, "url": u, "name": k["hub_name"], "description": k["desc"], "inLanguage": lang,
         "isPartOf": {"@id": SITE + "/#website"}, "dateModified": TODAY,
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(TRACK_ORDER), "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "item": course_schema(lang, t)} for i, t in enumerate(TRACK_ORDER)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": k["home_name"], "item": SITE + k["home"]},
            {"@type": "ListItem", "position": 2, "name": k["hub_name"], "item": u}]},
        G.faq_schema(k["faq"], u)]}
    return finish(lang, G.page(lang, k["title"], k["desc"], u, alts(), schema, body, G.CITY_JS))


def track(lang, t):
    k, tr = K[lang], K[lang]["tracks"][t]
    kind = BUILDING[t]
    others = [x for x in TRACK_ORDER if x != t][:3]
    symbols = "".join(B.symbol(s) for s in sorted({kind} | {BUILDING[x] for x in others}))
    builds = "".join(f"<li>{esc(b)}</li>" for b in tr["builds"])
    steps = "".join(f'<li><time>{i+1}</time><div><p>{esc(s)}</p></div></li>' for i, s in enumerate(tr["lesson"]))
    plan = k["plans"][0]
    body = f"""<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{symbols}</defs></svg>
<main>
<div class="wrap">
  <nav class="crumbs" aria-label="{esc(k['crumbs'])}"><ol><li><a href="{k['home']}">{esc(k['home_name'])}</a></li><li><a href="{k['base']}">{esc(k['hub_name'])}</a></li><li aria-current="page">{esc(tr['name'])}</li></ol></nav>
  <header class="ws-hero">
    <div>
      <div class="eyebrow">{esc(k['tr_eyebrow'].format(ages=tr['ages']))}</div>
      <p class="who">{esc(tr['name'])}</p>
      <h1 class="display">{esc(tr['h1'])}</h1>
      <p class="answer"><b>{esc(k['in_short'])}</b>{esc(tr['answer'])}</p>
      <p class="price-line">{esc(money(k['price_line']))}</p>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])}</a><a class="btn btn-line" href="{k['base']}">{esc(k['tr_back'])}</a></div>
    </div>
    <div class="ws-art kids-art"><img class="brand" src="/assets/aicoachalex-mark-96.webp" alt="" width="40" height="40">
      <svg viewBox="{vb(kind, 14)}" role="img" aria-label="{esc(tr['name'])}"><use href="#b-{kind}" x="0" y="0" width="240" height="300"/></svg></div>
  </header>
</div>
<section class="section wrap"><div class="twocol">
  <div><h2 class="display">{esc(k['tr_builds'])}</h2><ul class="gets">{builds}</ul></div>
  <div><h2 class="display">{esc(k['tr_lesson'])}</h2><ol class="steps">{steps}</ol></div>
</div></section>
<section class="section wrap"><div class="story">
  <div><h2 class="display">{esc(k['tr_parents'])}</h2><p>{esc(k['tr_parents_p'])}</p><div class="rules two">{"".join(f'<div class="rule"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in k['safety'][:2])}</div></div>
  <aside class="outcome"><span class="eyebrow">{esc(plan[0])}</span><strong class="big">{esc(money(plan[1]))}</strong><p>{esc(money(plan[2]))}</p><a class="btn btn-lime" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])} →</a></aside>
</div></section>
{G.faq_html(tr['faq'], k['faq_h'])}
<section class="section wrap"><h2 class="display">{esc(k['tr_other'])}</h2><div class="next">{"".join(track_card(lang, x) for x in others)}<a class="back" href="{k['base']}"><span class="eyebrow">↩</span><strong>{esc(k['tr_back'])} →</strong></a></div></section>
</main>"""
    u = url(lang, t)
    schema = {"@context": "https://schema.org", "@graph": [
        G.PERSON, course_schema(lang, t),
        {"@type": "WebPage", "@id": u, "url": u, "name": tr["title"], "description": tr["desc"], "inLanguage": lang,
         "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": u + "#course"}, "dateModified": TODAY,
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer"]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": k["home_name"], "item": SITE + k["home"]},
            {"@type": "ListItem", "position": 2, "name": k["hub_name"], "item": url(lang)},
            {"@type": "ListItem", "position": 3, "name": tr["name"], "item": u}]},
        G.faq_schema(tr["faq"], u)]}
    return finish(lang, G.page(lang, tr["title"], tr["desc"], u, alts(t), schema, body))


def finish(lang, html):
    html = mark_current(html, lang)
    k = K[lang]
    return html.replace(G.esc(G.UI[lang]["footer_note"]), esc(k["footer_note"]))


WM_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="description" content="An interactive model that shows kids and adults how a chatbot writes its answer: tokens, next-word odds, temperature, memory and made-up facts.">
<link rel="canonical" href="https://aicoachalex.com/ai-lessons-for-kids/word-machine/">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<style>:root{padding:env(safe-area-inset-top,0) 0 env(safe-area-inset-bottom,0)}body{margin:0;font:14px system-ui,sans-serif}[hidden]{display:none!important}img{max-width:100%}</style>
"""


def word_machine():
    src = os.path.join(ROOT, "_tools", "word-machine.src.html")
    with open(src, encoding="utf-8") as f:
        s = f.read()
    m = s.index("<style>")
    head, rest = s[:m], s[m:]
    st_end = rest.index("</style>") + len("</style>")
    return WM_HEAD + head + rest[:st_end] + "\n</head>\n<body>\n" + rest[st_end:] + "\n</body>\n</html>\n"


def main():
    for lang in LANGS:
        G.write(K[lang]["base"] + "index.html", hub(lang))
        for t in TRACK_ORDER:
            G.write(path(lang, t) + "index.html", track(lang, t))
    G.write("/ai-lessons-for-kids/word-machine/index.html", word_machine())
    print("built kids pages:", len(LANGS), "x (hub + 6 tracks) + word machine")


if __name__ == "__main__":
    main()
