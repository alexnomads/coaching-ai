#!/usr/bin/env python3
"""Build the scroll-scene homepage from the previous homepage.

    python3 _tools/build_home_scenes.py            # builds index.html and index.es.html
    python3 _tools/build_home_scenes.py it         # another language, once COPY["it"] exists

Source of truth for everything that already existed (head, tracking, nav, logo,
dropdown, mobile menu, video phone, marquee, all section copy, cases, pricing
cards, coach section, footer, interstitial and scripts) is index-old[.xx].html.
Only the copy of the new scenes lives in COPY below. Shared CSS/JS:
assets/scenes.css and assets/scenes.js.
"""
import html as H
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_V = "1"

COPY = {
    "en": {
        "hero_lap_title": "chat",
        "hero_lap": ["> is my career going in the right direction?", "  let's find out."],
        "comfort_a": "You've built a solid career.",
        "comfort_b": "Then you got",
        "comfort_big": "comfort-able",
        "mach_a": "and now the",
        "mach_big": "machines",
        "mach_b": "are good at it too.",
        "term_title": "terminal — your job, automated",
        "term": [
            ("> draft the quarterly report", "c-cmd"), ("  done. 12 seconds.", "c-out"),
            ("> clear my inbox", "c-cmd"), ("  done. 214 emails sorted.", "c-out"),
            ("> analyse the sales data", "c-cmd"), ("  done. 3 insights, 1 chart.", "c-out"),
            ("> write the landing page", "c-cmd"), ("  done.", "c-out"),
            ("> build the board deck", "c-cmd"), ("  done. 18 slides.", "c-out"),
            ("> so what do I do now?", "c-cmd"), ("orchestrate. don't compete.", "c-big"),
        ],
        "late_a": "Too late?",
        "late_b": "No.",
        "method_lap_title": "diagnostic.md",
        "method_head": "## the method",
        "method_last": "> run diagnostic --you",
        "pricing_lap_title": "aicoachalex.com/pricing",
    },
    "es": {
        "hero_lap_title": "chat",
        "hero_lap": ["> ¿va mi carrera en la dirección correcta?", "  vamos a averiguarlo."],
        "comfort_a": "Has construido una carrera sólida.",
        "comfort_b": "Y luego te",
        "comfort_big": "acomo-daste",
        "mach_a": "y ahora las",
        "mach_big": "máquinas",
        "mach_b": "también lo hacen bien.",
        "term_title": "terminal — tu trabajo, automatizado",
        "term": [
            ("> redacta el informe trimestral", "c-cmd"), ("  hecho. 12 segundos.", "c-out"),
            ("> vacía mi bandeja de entrada", "c-cmd"), ("  hecho. 214 emails ordenados.", "c-out"),
            ("> analiza los datos de ventas", "c-cmd"), ("  hecho. 3 conclusiones, 1 gráfico.", "c-out"),
            ("> escribe la landing page", "c-cmd"), ("  hecho.", "c-out"),
            ("> monta la presentación para el consejo", "c-cmd"), ("  hecho. 18 diapositivas.", "c-out"),
            ("> ¿y ahora qué hago yo?", "c-cmd"), ("orquesta. no compitas.", "c-big"),
        ],
        "late_a": "¿Demasiado tarde?",
        "late_b": "No.",
        "method_lap_title": "diagnostico.md",
        "method_head": "## el método",
        "method_last": "> ejecutar diagnóstico --tú",
        "pricing_lap_title": "aicoachalex.com/precios",
        # the Spanish page never had the Replit/Lovable badges: reuse the English block, translated
        "badges_tr": [
            ("Software Development Agents", "Agentes de desarrollo de software"),
            ("🏆 Top 10% of Replit Agent users", "🏆 Top 10% de usuarios de Replit Agent"),
            ("Directs the Replit AI Agent to generate and refine substantial production code across multi-step build sessions.",
             "Dirige al agente de IA de Replit para generar y perfeccionar código de producción en sesiones de desarrollo de varios pasos."),
            ("Conversational AI Software", "Software de IA conversacional"),
            ("🏆 Top 10% of Lovable users", "🏆 Top 10% de usuarios de Lovable"),
            ("Builds web platforms, networks, and marketplaces in Lovable.", "Construye plataformas web, redes y marketplaces en Lovable."),
        ],
    },
}


def grab(pat, s, what, flags=re.S):
    m = re.search(pat, s, flags)
    assert m, f"not found: {what}"
    return m


def between(s, a, b, what):
    i = s.find(a); assert i >= 0, f"start marker missing: {what}"
    j = s.find(b, i); assert j >= 0, f"end marker missing: {what}"
    return s[i:j]


def text(fragment):
    return H.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def esc(t):
    return H.escape(t, quote=False)


def laptop(title, lines_html, attrs="", screen_extra=""):
    return f'''<div class="laptop" {attrs}>
        <div class="lap-lid"><div class="lap-screen">
          <div class="lap-bar" aria-hidden="true"><i></i><i></i><i></i><span>{esc(title)}</span></div>
          {screen_extra or f'<div class="lap-view"><div class="lap-scroll">{lines_html}</div></div>'}
        </div></div>
        <div class="lap-base" aria-hidden="true"><div class="lap-kb"></div></div>
      </div>'''


def build(lang):
    sfx = "" if lang == "en" else f".{lang}"
    src = open(os.path.join(ROOT, f"index-old{sfx}.html"), encoding="utf-8").read()
    # the backups are noindexed; never carry that into the live homepage
    src = src.replace('<meta name="robots" content="noindex, nofollow">\n', "")
    C = COPY[lang]

    # ---------- preserved blocks ----------
    head_end = src.index("</head>")
    head = src[:head_end] + f'<link rel="stylesheet" href="/assets/scenes.css?v={ASSET_V}">\n'
    hero_start = src.index('<section class="hero" id="heroSection">')
    prefix = src[head_end:hero_start]          # </head><body> nav, cursor, quiz pill, logo, dropdown, mobile menu
    phone = between(src, "<!-- PHONE MOCKUP -->", "<!-- Scroll Hint -->", "phone")
    marquee = between(src, "<!-- Marquee Strip -->", "<!-- Quiz Section -->", "marquee")
    tail = src[src.index("<!-- FOOTER WITH SOCIAL LINKS -->"):]
    # the era hover script and the old card-deck carousel go: their sections are now scroll scenes
    a = tail.index("// Era Cards"); b = tail.index("</script>", a)
    tail = tail[:a] + tail[b:]
    k = tail.rindex("</body>")   # the real closing tag (a comment above also mentions </body>)
    tail = tail[:k] + f'<script src="/assets/scenes.js?v={ASSET_V}" defer></script>\n' + tail[k:]

    hero = between(src, '<section class="hero" id="heroSection">', "<!-- Marquee Strip -->", "hero")
    h1 = grab(r"<h1 class=\"hero-type\">.*?</h1>", hero, "h1").group(0)
    hero_p = grab(r'<div class="hero-aside">\s*<p>(.*?)</p>', hero, "hero paragraph").group(1)
    btn_hero = grab(r'<a href="#pricing" class="btn-hero">.*?</a>', hero, "hero button").group(0)
    btn_tg = grab(r'<a href="https://t\.me/alexnomads" class="btn-telegram-mobile">.*?</a>', hero, "telegram button").group(0)
    tg_text = text(btn_tg)
    scroll_hint = text(grab(r'<div class="hero-scroll">(.*?)</div>', hero, "scroll hint").group(1))
    assert C["comfort_a"] in text(hero_p), "comfort line must come from the hero paragraph"

    quiz = between(src, "<!-- Quiz Section -->", "<!-- Era Section -->", "quiz")
    quiz_title = grab(r'<h2 class="quiz-title">(.*?)</h2>', quiz, "quiz title").group(1)
    quiz_desc = grab(r'<p class="quiz-desc">(.*?)</p>', quiz, "quiz desc").group(1)
    quiz_cta = grab(r'<a href="(career-risk-assessment\.html)" class="quiz-cta">(.*?)</a>', quiz, "quiz cta")
    qstats = re.findall(r'<div class="quiz-stat-num">(.*?)</div>\s*<div class="quiz-stat-label">(.*?)</div>', quiz, re.S)
    assert len(qstats) == 3

    eras_src = between(src, "<!-- Era Section -->", "<!-- Problem Statement -->", "eras")
    eras = re.findall(r'<span class="era-num">(.*?)</span>.*?<h2 class="era-name">(.*?)</h2>\s*<p class="era-body">(.*?)</p>\s*<span class="era-tag">(.*?)</span>', eras_src, re.S)
    assert len(eras) == 3

    stmt = between(src, "<!-- Problem Statement -->", "<!-- THE METHOD", "statement")
    stmt_label = grab(r'<span class="stmt-label">.*?</span>', stmt, "stmt label").group(0)
    stmt_h2 = grab(r'<h2 class="statement-text">.*?</h2>', stmt, "stmt h2").group(0)
    stmt_ps = re.findall(r"<p style=.*?</p>", stmt, re.S)
    assert len(stmt_ps) == 2

    meth = between(src, "<!-- THE METHOD", "<!-- Cases Section -->", "method")
    m_label = text(grab(r'<span class="method-label">(.*?)</span>', meth, "method label").group(1))
    m_title = grab(r'<h2 class="method-title">(.*?)</h2>', meth, "method title").group(1)
    m_sub = grab(r'<p class="method-subtitle">(.*?)</p>', meth, "method sub").group(1)
    cards = []
    for c in re.findall(r'<div class="method-card[^"]*" data-card="\d">(.*?)<button class="card-expand"', meth, re.S):
        cards.append(dict(
            n=text(grab(r'<div class="card-number">(.*?)</div>', c, "card n").group(1)),
            title=text(grab(r'<h3 class="card-title">(.*?)</h3>', c, "card title").group(1)),
            pre=grab(r'<p class="card-preview">(.*?)</p>', c, "card preview").group(1).strip(),
            full=grab(r'<div class="card-full">\s*<p>(.*?)</p>', c, "card full").group(1).strip(),
            items=re.findall(r"<li>(.*?)</li>", c, re.S),
            cta=re.search(r'<a href="([^"]+)" class="card-cta">(.*?)</a>', c, re.S),
            featured="card-featured" in c))
    assert len(cards) == 4 and all(len(c["items"]) == 3 for c in cards)

    cases = between(src, "<!-- Cases Section -->", "<!-- Pricing Section -->", "cases")
    c_label = text(grab(r'<span class="cases-label">(.*?)</span>', cases, "cases label").group(1))
    c_title = grab(r'<h2 class="cases-title">(.*?)</h2>', cases, "cases title").group(1)
    c_sub = grab(r'<p class="cases-subtitle">.*?</p>', cases, "cases sub").group(0)
    if '<div class="trust-badges">' in cases:
        badges = between(cases, '<div class="trust-badges">', '<div class="cases-grid">', "badges")
    else:
        en = open(os.path.join(ROOT, "index-old.html"), encoding="utf-8").read()
        badges = between(en, '<div class="trust-badges">', '<div class="cases-grid">', "badges (en)")
        for a, b in C["badges_tr"]:
            assert a in badges, a
            badges = badges.replace(a, b)
    grid = grab(r'<div class="cases-grid">.*</div>\s*(?=</section>)', cases, "cases grid").group(0)
    n_vid = grid.count("<video autoplay muted loop playsinline>")
    assert n_vid == 6, n_vid
    grid = grid.replace("<video autoplay muted loop playsinline>", '<video muted loop playsinline preload="none" data-lazy-play>')
    case_stats = re.findall(r'<h3 class="case-title">(.*?)</h3>.*?<div class="case-stat">(.*?)<span>(.*?)</span></div>', grid, re.S)
    assert len(case_stats) == 6

    pricing = between(src, "<!-- Pricing Section -->", "<!-- Coach Section -->", "pricing")
    p_label = text(grab(r'<span class="pricing-label">(.*?)</span>', pricing, "pricing label").group(1))
    p_title = grab(r'<h2 class="pricing-title">(.*?)</h2>', pricing, "pricing title").group(1)
    p_sub = grab(r'<p class="pricing-subtitle">(.*?)</p>', pricing, "pricing sub").group(1)
    p_grid = grab(r'<div class="pricing-grid">.*</div>\s*(?=</section>)', pricing, "pricing grid").group(0)
    plans = re.findall(r'<div class="pricing-tier">(.*?)</div>\s*<div class="pricing-price">(.*?)<span>(.*?)</span></div>.*?<a (href="[^"]+"[^>]*?) class="pricing-cta">(.*?)</a>', p_grid, re.S)
    assert len(plans) == 3

    coach = between(src, "<!-- Coach Section -->", "<!-- Final CTA -->", "coach")
    coach = coach.replace('<section class="coach-section">', '<section class="coach-section flow" data-wall="forest" data-nav="dark">', 1)

    cta = between(src, "<!-- Final CTA -->", "<!-- FOOTER WITH SOCIAL LINKS -->", "cta")
    cta_label = text(grab(r'<span class="cta-label">(.*?)</span>', cta, "cta label").group(1))
    cta_title = grab(r'<h2 class="cta-title">(.*?)</h2>', cta, "cta title").group(1)
    cta_btn = grab(r'<a href="(https://alessandrocapezza\.youcanbook\.me/)"[^>]*class="cta-btn">(.*?)</a>', cta, "cta btn")
    cta_note = text(grab(r'<p class="cta-note">(.*?)</p>', cta, "cta note").group(1))
    t_main, t_em = grab(r"^(.*?)\s*<em>(.*?)</em>\s*$", cta_title, "cta title parts").groups()

    # ---------- new markup ----------
    hero_lines = (f'<p class="ln c-cmd">{esc(C["hero_lap"][0])}</p>'
                  f'<p class="ln">{esc(C["hero_lap"][1])}<span class="caret-static"></span></p>')
    out = [head, prefix]

    out.append(f'''<section class="scene s-hero" id="heroSection" style="--len:140" data-wall="ink" data-nav="dark">
  <div class="stage wall-ink">
    <div class="floor floor-forest"></div>
    <div class="hero-copy">
      {h1}
      <div class="hero-aside">
        <p>{hero_p}</p>
        {btn_hero}
        {btn_tg}
      </div>
    </div>
    <div class="hero-desk" aria-hidden="true">
      {laptop(C["hero_lap_title"], hero_lines)}
      <div class="desk"></div>
    </div>
    {phone.strip()}
    <p class="hero-scroll">{esc(scroll_hint)} ↓</p>
  </div>
</section>

{marquee.strip()}
''')

    out.append(f'''<!-- 3 · comfort-able -->
<section class="scene s-comfort" style="--len:260" data-wall="ink" data-nav="dark">
  <div class="stage wall-ink">
    <p class="say" data-words="0.02 0.3">{esc(C["comfort_a"])}</p>
    <p class="say" data-words="0.32 0.45">{esc(C["comfort_b"])}</p>
    <p class="giant" aria-label="{esc(C["comfort_big"])}."><span data-letters="0.45 0.85">{esc(C["comfort_big"])}</span><span class="dotmark" data-on="0.85 0.9"></span></p>
  </div>
</section>
''')

    term = "".join(f'<p class="ln {c}">{esc(t)}</p>' for t, c in C["term"])
    out.append(f'''<!-- 4 · machines -->
<section class="scene s-machines" style="--len:340" data-wall="lime" data-nav="light">
  <div class="stage wall-lime">
    <div class="floor floor-cloth"></div>
    <p class="say say-row"><span data-words="0 0.1">{esc(C["mach_a"])}</span> <span class="giant-mach" data-letters="0.1 0.3">{esc(C["mach_big"])}</span></p>
    <p class="say" data-words="0.3 0.42">{esc(C["mach_b"])}</p>
    {laptop(C["term_title"], term, 'data-type="0.4 0.97"')}
  </div>
</section>
''')

    era_html = ""
    ranges = ["-1 0 0.28 0.34", "0.34 0.40 0.61 0.67"]
    for i, (num, name, body, tag) in enumerate(eras):
        attr = f'data-swap="{ranges[i]}"' if i < 2 else 'data-show="0.67 0.73"'
        era_html += f'''
      <div class="era era-{i+1}" {attr}>
        <span class="era-num" aria-hidden="true">{num}</span>
        <h2 class="era-name">{name}</h2>
        <p class="era-body">{body}</p>
        <span class="era-tag">{tag}</span>
      </div>'''
    out.append(f'''<!-- 5 · eras -->
<section class="scene s-eras" style="--len:360" data-wall="ink" data-nav="dark" data-wall-steps="0:ink 0.34:forest 0.67:lime" data-nav-steps="0:dark 0.67:light">
  <div class="stage">
    <div class="walls" aria-hidden="true"><i class="w1"></i><i class="w2" data-on="0.30 0.38"></i><i class="w3" data-on="0.63 0.71"></i></div>
    <div class="eras">{era_html}
    </div>
  </div>
</section>
''')

    out.append(f'''<!-- 6 · too late -->
<section class="scene s-late" style="--len:280" data-wall="ink" data-nav="dark">
  <div class="stage wall-ink">
    <p class="late" data-swap="0 0.12 0.28 0.36">{esc(C["late_a"])}</p>
    <p class="late late-no" data-swap="0.38 0.46 0.56 0.62">{esc(C["late_b"])}</p>
    <div class="late-wrap" data-show="0.64 0.76">{stmt_h2}</div>
  </div>
</section>
<section class="statement flow" data-wall="cream" data-nav="light">
  <div>{stmt_label}</div>
  <div>
    {stmt_ps[0]}
    {stmt_ps[1]}
  </div>
</section>
''')

    stats_html = "".join(
        f'<div class="qstat" data-show="{a} {b}"><b data-count="{a} {b2}" data-to="{text(n)}">{text(n)}</b><span>{l}</span></div>'
        for (n, l), (a, b, b2) in zip(qstats, [(0.30, 0.40, 0.45), (0.42, 0.52, 0.56), (0.54, 0.64, 0.66)]))
    out.append(f'''<!-- 7 · quiz -->
<section class="scene s-quiz" style="--len:300" data-wall="forest" data-nav="dark">
  <div class="stage wall-forest">
    <div class="floor floor-cloth"></div>
    <h2 class="quiz-title" data-words="0 0.2">{quiz_title}</h2>
    <p class="lede" data-show="0.18 0.3">{quiz_desc}</p>
    <div class="qstats">{stats_html}</div>
    <div class="quiz-go" data-show="0.72 0.84"><a href="{quiz_cta.group(1)}" class="btn-lime quiz-cta">{quiz_cta.group(2)}</a></div>
  </div>
</section>
''')

    m_lines = f'<p class="ln c-head">{esc(C["method_head"])}</p>'
    for c in cards:
        m_lines += f'<p class="ln c-title">{esc(c["n"])}  {esc(c["title"])}</p><p class="ln c-out">    {esc(text(c["pre"]))}</p>'
    m_lines += f'<p class="ln c-cmd">{esc(C["method_last"])}</p>'
    steps = ""
    for c in cards:
        cta_html = f'<a href="{c["cta"].group(1)}" class="card-cta">{c["cta"].group(2)}</a>' if c["cta"] else ""
        items = "".join(f"<li>{x}</li>" for x in c["items"])
        steps += f'''
      <article class="step{' featured' if c['featured'] else ''}">
        <span class="step-n">{esc(c["n"])}</span>
        <h3>{esc(c["title"])}</h3>
        <p class="step-pre">{c["pre"]}</p>
        <p>{c["full"]}</p>
        <ul>{items}</ul>
        {cta_html}
      </article>'''
    out.append(f'''<!-- 8 · method -->
<section class="scene s-method" id="method" style="--len:380" data-wall="cream" data-nav="light">
  <div class="stage wall-cream">
    <div class="floor floor-cloth-dim"></div>
    <div class="m-head">
      <p class="kicker">{esc(m_label)}</p>
      <h2 class="big-h" data-words="0 0.15">{m_title}</h2>
      <p class="lede" data-show="0.12 0.22">{m_sub}</p>
    </div>
    {laptop(C["method_lap_title"], m_lines, 'data-type="0.22 0.97"')}
  </div>
</section>
<section class="steps flow" data-wall="cream" data-nav="light">
  <div class="flow-inner steps-grid">{steps}
  </div>
</section>
''')

    rec = [0, 1, 3, 4]   # The Sandbox, LandVault, BlueStacks + Game.tv, GenLayer
    rstats = ""
    for k, i in enumerate(rec):
        title, val, cap = case_stats[i]
        m = grab(r"^(\D*)([\d.,]+)(.*)$", val.strip(), "stat value")
        company = text(title).split(" — ")[0]
        cap_txt = " · ".join(text(cap).split(" · ")[:2]) + " · " + company
        a = 0.33 + 0.1 * k
        rstats += f'<div class="rstat" data-show="{a:.2f} {a + 0.07:.2f}"><b data-count="{a + 0.02:.2f} {a + 0.25:.2f}" data-to="{m.group(2)}" data-pre="{esc(m.group(1))}" data-suf="{esc(m.group(3))}">{esc(val.strip())}</b><span>{esc(cap_txt)}</span></div>'
    out.append(f'''<!-- 9 · track record -->
<section class="scene s-record" style="--len:300" data-wall="forest" data-nav="dark">
  <div class="stage wall-forest">
    <p class="kicker">{esc(c_label)}</p>
    <h2 class="big-h cases-title" data-words="0 0.3">{c_title}</h2>
    <div class="bar" data-show="0.28 0.34"></div>
    <div class="rstats">{rstats}</div>
  </div>
</section>
<section class="cases-section flow" data-wall="ink" data-nav="dark">
  <div class="cases-section-header">
    {c_sub}
  </div>
  {badges.strip()}
  {grid.strip()}
</section>
''')

    rows = ""
    for k, (tier, price, sub, attrs, ctatext) in enumerate(plans):
        a = 0.25 + 0.2 * k
        rows += f'''<div class="plan-row" data-show="{a:.2f} {a + 0.15:.2f}"><p class="pp">{esc(text(price))}</p><div class="pt"><b>{esc(text(tier))}</b><span>{esc(text(sub).lstrip("· ").strip())}</span></div><a {attrs}>{ctatext}</a></div>'''
    screen = f'<div class="plans-screen">{rows}</div>'
    out.append(f'''<!-- 10 · pricing -->
<section class="scene s-pricing" id="pricing" style="--len:320" data-wall="lime" data-nav="light">
  <div class="stage wall-lime">
    <div class="floor floor-cloth"></div>
    <p class="kicker">{esc(p_label)}</p>
    <h2 class="big-h" data-words="0 0.16">{p_title}</h2>
    <p class="lede" data-show="0.12 0.22">{p_sub}</p>
    {laptop(C["pricing_lap_title"], "", 'data-keys="0.2 0.82" data-enters="0.4 0.6 0.8"', screen)}
  </div>
</section>
<section class="plans flow" data-wall="cream" data-nav="light">
  {p_grid.strip()}
</section>

{coach.strip()}
''')

    tg_href = "https://t.me/alexnomads"
    b_txt = text(cta_btn.group(2))
    b_main, b_price = (b_txt.split(" — ", 1) + [""])[:2]
    out.append(f'''<!-- 12 · book -->
<section class="scene s-book" style="--len:280" data-wall="ink" data-nav="dark">
  <div class="stage wall-ink">
    <div class="b-head">
      <p class="kicker">{esc(cta_label)}</p>
      <h2 class="big-h" data-words="0 0.22">{esc(text(t_main))}</h2>
      <p class="today" data-show="0.25 0.38">{esc(text(t_em))}</p>
      <div class="b-notes" data-show="0.4 0.5">
        <p>{esc(cta_note)}</p>
        <a href="{tg_href}">{esc(tg_text)} →</a>
      </div>
    </div>
    <div class="dot-wrap">
      <a href="{cta_btn.group(1)}" target="_blank" rel="noopener" class="book-dot" data-scale="0.45 0.8 0.035 1"><span class="bl" data-on="0.75 0.88">{esc(b_main)}<b>{esc(b_price)}</b></span></a>
    </div>
  </div>
</section>

''')

    out.append(tail.replace('<footer class="footer">', '<footer class="footer" data-wall="ink" data-nav="dark">', 1))
    page = "".join(out)
    open(os.path.join(ROOT, f"index{sfx}.html"), "w", encoding="utf-8").write(page)
    print(f"index{sfx}.html: {len(page):,} bytes")


if __name__ == "__main__":
    for lang in (sys.argv[1:] or ["en", "es"]):
        build(lang)
