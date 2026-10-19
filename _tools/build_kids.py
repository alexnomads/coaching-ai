"""Build the AI lessons for kids pages (EN/ES/IT): a pixel-art island hub for parents + 6 track pages.

Run from the repo root:  python3 _tools/build_kids.py
Copy: _tools/kids_content.py. Map and sprites: assets/kids-island.js (icons in assets/kids/).
Shares page chrome with build_who_i_work_with.py.
"""
import os
import re

import build_who_i_work_with as G
from kids_content import K, PRICE, TRACK_ORDER

ROOT, SITE, BOOK, LANGS, esc = G.ROOT, G.SITE, G.BOOK, G.LANGS, G.esc
TODAY = "2026-10-19"
JS_V = "2"
SHARE = SITE + "/assets/kids/ai-island.png"
SPRITE = {"lab": "lab", "market": "market", "court": "court", "studio": "studio", "time": "time", "light": "light"}
ICON_SIZE = {"lab": (240, 216), "time": (128, 264), "market": (248, 224), "court": (240, 176), "studio": (288, 208), "light": (104, 248), "hq": (184, 168)}
# hotspot boxes on the 384x240 map: door position + sprite box (see kids-island.js)
DOORS = {"lab": (88, 80), "time": (192, 62), "market": (300, 80), "court": (88, 186), "studio": (300, 186), "light": (346, 128), "hq": (44, 128)}
BOX = {"lab": (-30, -48, 60, 54), "time": (-16, -62, 32, 66), "market": (-30, -52, 62, 56), "court": (-30, -38, 60, 44),
       "studio": (-30, -46, 72, 52), "light": (-12, -58, 26, 62), "hq": (-22, -38, 46, 42)}
KIDS_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@500;700&family=Nunito:wght@400;600;800&display=swap" rel="stylesheet">'


def money(s):
    return s.format(**PRICE)


def url(lang, t=None):
    return SITE + K[lang]["base"] + (K[lang]["tracks"][t]["slug"] + "/" if t else "")


def path(lang, t=None):
    return K[lang]["base"] + (K[lang]["tracks"][t]["slug"] + "/" if t else "")


def alts(t=None):
    return [(l, url(l, t)) for l in LANGS] + [("x-default", url("en", t))]


def icon(t, cls="px", lazy=True):
    w, h = ICON_SIZE[SPRITE[t]]
    return f'<img class="{cls}" src="/assets/kids/{SPRITE[t]}.png" alt="" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else ""}>'


def track_card(lang, t):
    tr, k = K[lang]["tracks"][t], K[lang]
    return f"""<a class="kcard k-{t}" href="{path(lang, t)}">
  <div class="kart">{icon(t)}</div>
  <span class="kages">{esc(k['for_ages'])} {esc(tr['ages'])}</span>
  <h3>{esc(tr['name'])}</h3>
  <p>{esc(tr['h1'])}</p>
  <span class="kgo">→</span>
</a>"""


def course_schema(lang, t):
    tr = K[lang]["tracks"][t]
    lo, hi = tr["ages"].replace("–", "-").split("-")
    return {"@type": "Course", "@id": url(lang, t) + "#course", "url": url(lang, t), "name": tr["h1"], "description": tr["answer"],
            "inLanguage": lang, "provider": {"@id": SITE + "/#alessandro"}, "image": SITE + f"/assets/kids/{SPRITE[t]}.png",
            "audience": {"@type": "EducationalAudience", "educationalRole": "student", "audienceType": f"Kids and teenagers {tr['ages']}"},
            "typicalAgeRange": f"{lo}-{hi}", "educationalLevel": "Beginner",
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online", "courseWorkload": "PT50M", "instructor": {"@id": SITE + "/#alessandro"}},
            "offers": [{"@type": "Offer", "name": "Single lesson", "price": "65", "priceCurrency": "EUR", "category": "Paid", "url": BOOK},
                       {"@type": "Offer", "name": "Pack of 8 (price per lesson)", "price": "60", "priceCurrency": "EUR", "category": "Paid", "url": BOOK}]}


def island(lang):
    k = K[lang]
    spots = ""
    for key in ["time", "lab", "market", "hq", "light", "court", "studio"]:
        dx, dy = DOORS[key]
        bx, by, bw, bh = BOX[key]
        st = f'left:{(dx+bx)/3.84:.2f}%;top:{(dy+by)/2.40:.2f}%;width:{bw/3.84:.2f}%;height:{bh/2.40:.2f}%'
        if key == "hq":
            spots += f'<a class="spot hq" href="#book" style="{st}"><span>AI Coach Alex</span></a>'
        else:
            tr = k["tracks"][key]
            spots += f'<a class="spot{" below" if key == "light" else ""}" href="{path(lang, key)}" style="{st}" aria-label="{esc(tr["name"])}: {esc(tr["h1"])}"><span>{esc(tr["name"])}</span></a>'
    return (f'<div class="island-map" role="group" aria-label="{esc(k["island_title"])}">'
            f'<canvas width="384" height="240" aria-hidden="true"></canvas><div class="tags" aria-hidden="true"></div>{spots}'
            f'<noscript><img src="/assets/kids/ai-island.png" alt="{esc(k["island_title"])}" width="1152" height="720"></noscript></div>')


# ---------- the Word Machine, embedded inline ----------
def prefix_css(css, scope=".wmx"):
    out, i, n = [], 0, len(css)
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    n = len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        head = css[i:j].strip()
        depth, k = 1, j + 1
        while depth and k < n:
            depth += css[k] == "{"
            depth -= css[k] == "}"
            k += 1
        body = css[j + 1:k - 1]
        if head.startswith("@media"):
            if "prefers-color-scheme" in head:
                pass
            else:
                out.append(f"{head}{{{prefix_css(body, scope)}}}")
        elif head.startswith("@keyframes"):
            out.append(f"{head.replace('@keyframes ', '@keyframes wm-')}{{{body}}}")
        elif "data-theme" in head:
            pass
        else:
            sels = []
            for sel in head.split(","):
                sel = sel.strip()
                if sel in (":root", "body", "html"):
                    sels.append(scope)
                elif sel.startswith(":root"):
                    continue
                else:
                    sels.append(f"{scope} {sel}")
            if sels:
                body = re.sub(r"animation:\s*([a-z]+)", lambda m: f"animation:wm-{m.group(1)}", body)
                out.append(f"{','.join(sels)}{{{body}}}")
        i = k
    return "".join(out)


def word_machine():
    s = open(os.path.join(ROOT, "_tools", "word-machine.src.html"), encoding="utf-8").read()
    css = s[s.index("<style>") + 7:s.index("</style>")]
    css = prefix_css(css)
    css = css.replace('"Bricolage Grotesque", "Avenir Next", system-ui, sans-serif', "'Pixelify Sans',system-ui,sans-serif")
    css = css.replace('"Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif', "'Nunito',system-ui,sans-serif")
    css = css.replace('"JetBrains Mono", ui-monospace', "'IBM Plex Mono', ui-monospace")
    fig = s[s.index('<div class="figure">'):s.index("  <section>")]
    lesson = s[s.index("  <section>"):s.index("    <div class=\"habits\">")] + "  </section>"
    lesson = lesson.replace("<h2>The lesson</h2>", "<h3 class=\"wm-h\">Play it in five steps</h3>")
    lesson = lesson.replace("<p class=\"lead\">The student drives. Before every click they say out loud what they think will happen. The step cards tick off as they go.</p>",
                            "<p class=\"lead\">Before every click, guess out loud what will happen. The cards tick off as you go.</p>")
    js = s[s.index("<script>") + 8:s.index("</script>")]
    js = js.replace("document.getElementById('bCopy').addEventListener(", "document.getElementById('bCopy')?.addEventListener(")
    return f'<style>{css}</style>\n<div class="wmx">{fig}{lesson}</div>\n<script>{js}</script>'


WM = None


def plans_html(lang):
    k, cards = K[lang], ""
    for i, (name, price, sub, items) in enumerate(k["plans"]):
        lis = "".join(f"<li>{esc(x)}</li>" for x in items)
        badge = '<span class="kbadge">-8%</span>' if i == 1 else ""
        cards += f'<div class="plan p{i}">{badge}<h3>{esc(name)}</h3><div class="pp">{esc(money(price))}</div><p class="ps">{esc(money(sub))}</p><ul>{lis}</ul></div>'
    return cards


def hub(lang):
    global WM
    WM = WM or word_machine()
    k = K[lang]
    promises = "".join(f'<div class="promise c{i}"><span class="pn">{i+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for i, (a, b) in enumerate(k["promises"]))
    cards = "".join(track_card(lang, t) for t in TRACK_ORDER)
    lesson = "".join(f'<li><time>{a}′</time><div><b>{esc(b)}</b><p>{esc(c)}</p></div></li>' for a, b, c in k["lesson"])
    recap = "".join(f"<li>{esc(r)}</li>" for r in k["recap"])
    projects = "".join(f'<article class="project c{i}"><img src="/assets/kids/{["market", "court"][i]}.png" alt="" width="120" height="100" loading="lazy"><span class="eyebrow">{esc(a)}</span><h3>{esc(b)}</h3><p>{esc(c)}</p></article>'
                       for i, (a, b, c) in enumerate(k["projects"]))
    safety = "".join(f'<div class="rule"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in k["safety"])
    body = f"""<main>
<div class="wrap">
  <nav class="crumbs" aria-label="{esc(k['crumbs'])}"><ol><li><a href="{k['home']}">{esc(k['home_name'])}</a></li><li aria-current="page">{esc(k['hub_name'])}</li></ol></nav>
  <div class="kids-hero">
    <div class="hub-intro">
      <div class="eyebrow">{esc(k['eyebrow'])}</div>
      <h1 class="display">{k['h1']}</h1>
      <p>{esc(k['intro'])}</p>
      <p class="price-line">{esc(money(k['price_line']))}</p>
      <div class="hub-ctas"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(k['cta'])}</a><a class="btn btn-line" href="#tracks">{esc(k['cta2'])}</a></div>
    </div>
    <div class="map-frame">{island(lang)}<p class="city-hint">{esc(k['island_hint'])}</p></div>
  </div>
</div>
<div class="rainbow" aria-hidden="true"></div>
<section class="section wrap" aria-labelledby="h-prom"><h2 class="display" id="h-prom">{esc(k['promises_h'])}</h2><div class="promises">{promises}</div></section>
<section class="section wrap" id="tracks" aria-labelledby="h-tracks"><h2 class="display" id="h-tracks">{esc(k['tracks_h'])}</h2><p class="lead">{esc(k['tracks_lead'])}</p><div class="kcards">{cards}</div></section>
<section class="section wrap" aria-labelledby="h-lesson"><div class="story">
  <div><h2 class="display" id="h-lesson">{esc(k['lesson_h'])}</h2><p class="lead">{esc(k['lesson_lead'])}</p><ol class="ksteps">{lesson}</ol></div>
  <aside class="outcome"><span class="eyebrow">{esc(k['recap_h'])}</span><ul class="recap">{recap}</ul></aside>
</div></section>
<section class="section wrap" id="try" aria-labelledby="h-try"><h2 class="display" id="h-try">{esc(k['try_h'])}</h2><p class="lead">{esc(k['try_p'])}</p>
  {WM}
</section>
<section class="section wrap" aria-labelledby="h-proj"><h2 class="display" id="h-proj">{esc(k['projects_h'])}</h2><p class="lead">{esc(k['projects_note'])}</p><div class="projects">{projects}</div></section>
<section class="section wrap" aria-labelledby="h-safe"><h2 class="display" id="h-safe">{esc(k['safety_h'])}</h2><div class="rules">{safety}</div></section>
<section class="section wrap" id="book" aria-labelledby="h-price"><h2 class="display" id="h-price">{esc(k['pricing_h'])}</h2><div class="plans">{plans_html(lang)}</div><p class="lead small">{esc(k['plans_note'])}</p>
  <p class="book-row"><a class="btn btn-dark" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])} →</a> <span class="eyebrow">{esc(k['call_note'])}</span></p></section>
{G.faq_html(k['faq'], k['faq_h'])}
<div class="wrap"><section class="final"><div><h2 class="display">{k['final_h']}</h2><p>{esc(k['final_p'])}</p></div>
<div><a class="btn btn-lime" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])} →</a><span class="note">{esc(k['call_note'])}</span></div></section></div>
</main>
<script src="/assets/kids-island.js?v={JS_V}" defer></script>"""
    u = url(lang)
    schema = {"@context": "https://schema.org", "@graph": [
        G.PERSON,
        {"@type": "CollectionPage", "@id": u, "url": u, "name": k["hub_name"], "description": k["desc"], "inLanguage": lang,
         "isPartOf": {"@id": SITE + "/#website"}, "dateModified": TODAY, "primaryImageOfPage": SHARE,
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(TRACK_ORDER), "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "item": course_schema(lang, t)} for i, t in enumerate(TRACK_ORDER)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": k["home_name"], "item": SITE + k["home"]},
            {"@type": "ListItem", "position": 2, "name": k["hub_name"], "item": u}]},
        G.faq_schema(k["faq"], u)]}
    return finish(lang, G.page(lang, k["title"], k["desc"], u, alts(), schema, body))


def track(lang, t):
    k, tr = K[lang], K[lang]["tracks"][t]
    others = [x for x in TRACK_ORDER if x != t][:3]
    builds = "".join(f"<li>{esc(b)}</li>" for b in tr["builds"])
    steps = "".join(f'<li><time>{i+1}</time><div><p>{esc(s)}</p></div></li>' for i, s in enumerate(tr["lesson"]))
    single, pack = k["plans"][0], k["plans"][1]
    body = f"""<main>
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
    <div class="track-art k-{t}">{icon(t, 'px big', lazy=False)}</div>
  </header>
</div>
<div class="rainbow" aria-hidden="true"></div>
<section class="section wrap"><div class="twocol">
  <div><h2 class="display">{esc(k['tr_builds'])}</h2><ul class="gets">{builds}</ul></div>
  <div><h2 class="display">{esc(k['tr_lesson'])}</h2><ol class="ksteps">{steps}</ol></div>
</div></section>
<section class="section wrap"><div class="story">
  <div><h2 class="display">{esc(k['tr_parents'])}</h2><p>{esc(k['tr_parents_p'])}</p><div class="rules two">{"".join(f'<div class="rule"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in k['safety'][:2])}</div></div>
  <aside class="outcome"><span class="eyebrow">{esc(single[0])} · {esc(pack[0])}</span><strong class="big">{esc(money(single[1]))} · {esc(money(pack[1]))}</strong><p>{esc(money(pack[2]))}</p><a class="btn btn-lime" href="{BOOK}" target="_blank" rel="noopener">{esc(k['book_call'])} →</a></aside>
</div></section>
{G.faq_html(tr['faq'], k['faq_h'])}
<section class="section wrap"><h2 class="display">{esc(k['tr_other'])}</h2><div class="kcards">{"".join(track_card(lang, x) for x in others)}</div><p><a class="btn btn-line" href="{k['base']}">↩ {esc(k['tr_back'])}</a></p></section>
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
    html = html.replace(' class="sn-cur"', "")
    kb = K[lang]["base"]
    html = re.sub(r'(<a href="%s")(>)' % re.escape(kb), r'\1 class="sn-cur"\2', html, count=2)
    html = html.replace(G.esc(G.UI[lang]["footer_note"]), esc(K[lang]["footer_note"]))
    html = html.replace(G.SHARE, SHARE).replace("<body>", '<body class="kids">', 1)
    html = html.replace('<link rel="stylesheet" href="/assets/wiw.css', KIDS_FONTS + '\n<link rel="stylesheet" href="/assets/wiw.css', 1)
    return html


def main():
    for lang in LANGS:
        G.write(K[lang]["base"] + "index.html", hub(lang))
        for t in TRACK_ORDER:
            G.write(path(lang, t) + "index.html", track(lang, t))
    print("built kids pages:", len(LANGS), "x (hub + 6 tracks)")


if __name__ == "__main__":
    main()
