#!/usr/bin/env python3
"""Assemble a daily AI-news blog post for aicoachalex.com.

Takes the site's reference post as the template (head, nav, footer, shared CSS/JS),
swaps in a new <article> fragment and metadata, then:
  - writes blog/<slug>.html
  - adds a card at the top of blog/index.html
  - adds the URL to sitemap.xml

Usage:
  python3 _tools/build_blog_post.py meta.json article.html

meta.json keys: slug, title, og_title, description, date (YYYY-MM-DD), tag,
read_min, excerpt, keywords, image (site path to og image), faq [[q,a],...]
"""
import json, re, sys, html, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "blog/claude-haiku-5-5-vs-sonnet-vs-opus.html"
TEMPLATE_SLUG = "claude-haiku-5-5-vs-sonnet-vs-opus"
LINKEDIN = "https://www.linkedin.com/in/alessandrocapezza/"

EXTRA_CSS = """
<style id="news-extra">
.byline{color:var(--black);text-decoration:underline;text-underline-offset:3px;}
.byline:hover{color:var(--green-deep);}
.post-figure{margin:0 0 2.5rem;}
.post-figure img{display:block;width:100%;height:auto;border-radius:8px;border:1px solid var(--border);}
.post-figure figcaption{font-size:0.85rem;color:var(--muted);margin-top:0.6rem;line-height:1.5;}
.hero-figure{margin-top:-1rem;}
.post-figure picture{display:block;}
.post-figure img.tall{max-width:460px;margin:0 auto;}
@media (max-width:640px){.post-figure img.tall{max-width:100%;}}
</style>"""


# Outbound links get UTM tags so the sites we cite see aicoachalex.com in their analytics.
# Own properties (site, booking page, author profiles) are left untouched.
NO_UTM = ("aicoachalex.com", "youcanbook.me", "linkedin.com/in/alessandrocapezza",
          "instagram.com/alexislimitless", "youtube.com/@alexislimitless", "x.com/alexnomads")


def add_utm(article, slug):
    from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

    def tag(match):
        url = html.unescape(match.group(2))
        if any(d in url.lower() for d in NO_UTM):
            return match.group(0)
        p = urlsplit(url)
        q = [kv for kv in parse_qsl(p.query, keep_blank_values=True) if not kv[0].startswith("utm_")]
        q += [("utm_source", "aicoachalex.com"), ("utm_medium", "referral"),
              ("utm_campaign", "blog"), ("utm_content", slug)]
        new = urlunsplit((p.scheme, p.netloc, p.path, urlencode(q), p.fragment))
        return f'{match.group(1)}{html.escape(new, quote=True)}"'

    out = re.sub(r'(<a\b[^>]*?\bhref=")(https?://[^"]+)"', tag, article)
    # keep the Referer header: never strip it with noreferrer on outbound links
    return out.replace('rel="noopener noreferrer"', 'rel="noopener"')


# ---- Booking CTAs -----------------------------------------------------------------------
# Every post carries two booking blocks: one right after the first section (so readers who
# land from search see a next step above the fold) and one at the end. Posts that already
# ship their own blocks are left alone.
BOOK_URL = "https://alessandrocapezza.youcanbook.me/"
CTA_TEXT = {
    "en": {"early_h": "Want your business to show up when people ask ChatGPT?",
           "early_p": "In a 49€ diagnostic call we check what ChatGPT and other AI assistants say about your business today, and what to fix first.",
           "early_b": "Book a 49€ diagnostic call →",
           "end_h": "Make sure AI describes your business the way you would.",
           "end_p": "One-to-one coaching: we write down how your business actually works, set up your AI workspace with your real files and rules, and build the first task that gives you hours back.",
           "end_b": "Book a 49€ diagnostic →", "end_2": "AI for Business Owners", "owners": "/ai-for-business-owners.html"},
    "es": {"early_h": "¿Quieres que tu negocio aparezca cuando la gente pregunta a ChatGPT?",
           "early_p": "En una llamada de diagnóstico de 49 € revisamos qué dicen hoy ChatGPT y otros asistentes de IA sobre tu negocio, y qué corregir primero.",
           "early_b": "Reservar llamada de diagnóstico de 49 € →",
           "end_h": "Asegúrate de que la IA describa tu negocio como lo harías tú.",
           "end_p": "Coaching individual: ponemos por escrito cómo funciona de verdad tu negocio, montamos tu espacio de IA con tus archivos y reglas reales y construimos la primera tarea que te devuelve horas.",
           "end_b": "Reservar diagnóstico de 49 € →", "end_2": "IA para dueños de negocio", "owners": "/ai-for-business-owners.es.html"},
    "it": {"early_h": "Vuoi che la tua attività compaia quando le persone lo chiedono a ChatGPT?",
           "early_p": "In una chiamata di diagnosi da 49 € controlliamo cosa dicono oggi ChatGPT e gli altri assistenti IA sulla tua attività, e cosa correggere per primo.",
           "early_b": "Prenota la chiamata di diagnosi da 49 € →",
           "end_h": "Fai in modo che l'IA descriva la tua attività come faresti tu.",
           "end_p": "Coaching individuale: mettiamo per iscritto come funziona davvero la tua attività, configuriamo il tuo spazio IA con i tuoi file e le tue regole reali e costruiamo il primo compito che ti restituisce ore.",
           "end_b": "Prenota la diagnosi da 49 € →", "end_2": "IA per titolari d'azienda", "owners": "/ai-for-business-owners.it.html"},
}


def cta_block(kind, lang, key):
    t = CTA_TEXT[lang]
    e = lambda x: html.escape(x, quote=False)
    if kind == "early":
        return (f'    <div class="article-cta inline">\n      <h3>{e(t["early_h"])}</h3>\n      <p>{e(t["early_p"])}</p>\n'
                f'      <a href="{BOOK_URL}" target="_blank" rel="noopener" data-cta="{key}-early-book">{e(t["early_b"])}</a>\n    </div>\n\n')
    return (f'    <div class="article-cta">\n      <h3>{e(t["end_h"])}</h3>\n      <p>{e(t["end_p"])}</p>\n'
            f'      <a href="{BOOK_URL}" target="_blank" rel="noopener" data-cta="{key}-end-book">{e(t["end_b"])}</a>\n'
            f'      <a href="{t["owners"]}" class="cta-secondary" data-cta="{key}-end-owners">{e(t["end_2"])}</a>\n    </div>\n\n')


def ensure_ctas(article, lang, key, early=True):
    """Add the early CTA (before the 2nd <h2>) and the end CTA (before sources/related) when missing."""
    if early and f'{key}-early-book' not in article:
        i = article.find("article-cta inline")
        if i == -1 or i > 0.35 * len(article):
            h2 = [mm.start() for mm in re.finditer(r"^[ \t]*<h2\b", article, re.M)]
            if len(h2) >= 2:
                article = article[:h2[1]] + cta_block("early", lang, key) + article[h2[1]:]
    if not re.search(r'<div class="article-cta">', article):
        marks = [mm.start() for pat in (r'^[ \t]*<p class="sources"', r'^[ \t]*<div class="related"')
                 for mm in re.finditer(pat, article, re.M)]
        if marks:
            at = min(marks)
            article = article[:at] + cta_block("end", lang, key) + article[at:]
    return article


TITLE_SUFFIX = " — AI Coach Alex"


def _shorten(text, limit):
    """Cut text to <= limit chars at a sentence/word boundary (used instead of failing the daily job)."""
    if len(text) <= limit:
        return text
    cut = text[:limit - 1]
    for sep in (". ", ": ", " — ", " - ", "; ", ", "):
        i = cut.rfind(sep)
        if i >= 30:
            return cut[:i].rstrip(" .:;,-—")
    return cut.rsplit(" ", 1)[0].rstrip(" .:;,-—") + "…"


def seo_meta(m):
    """Return the <title> text and validate lengths (Ahrefs/Google: title <= 70, description <= 160).

    Over-long values are auto-shortened with a WARNING (a daily job must never fail on length): shorten
    "title" (aim for <= 60 chars; "og_title" can stay long) or "description" (aim for <= 155) in meta.json.
    """
    core = re.sub(r"\s*\((?:AI news|Noticias IA|Notizie IA)?\s*\d{1,2} \w{3,4}\.? 20\d\d\)", "", m["title"]).strip()
    if len(core + TITLE_SUFFIX) <= 70:
        page_title = core + TITLE_SUFFIX
    elif len(core) <= 70:
        page_title = core
    else:
        page_title = _shorten(core, 70)
        print(f'WARNING: meta.json "title" is {len(core)} chars; <title> shortened to "{page_title}". Use <= 60 next time ("og_title" can stay long).')
    if len(m["description"]) > 160:
        m["description"] = _shorten(m["description"], 157)
        print(f'WARNING: meta.json "description" was over 160 chars; shortened. Keep it <= 155 next time.')
    return page_title

def main(meta_path, article_path):
    m = json.loads(pathlib.Path(meta_path).read_text())
    article = add_utm(pathlib.Path(article_path).read_text(), m["slug"])
    article = ensure_ctas(article, "en", f"news-{m['date']}-{m['slug']}")
    t = TEMPLATE.read_text()
    url = f"https://aicoachalex.com/blog/{m['slug']}.html"
    img = f"https://aicoachalex.com{m['image']}"
    esc = lambda s: html.escape(s, quote=True)

    head_end = t.index('<script type="application/ld+json">')
    head = t[:head_end]
    # template's article-specific style blocks (keep article-extra, drop the haiku widget css)
    styles = re.search(r'<style id="article-extra">.*?</style>', t, re.S).group(0)
    body_start = t.index("</head>")
    nav = t[body_start:t.index("<article>")]
    footer = t[t.index("<footer"):t.index('<script id="haiku-picker-js">')] + "</body>\n</html>\n"

    # --- metadata swaps in head ---
    head = head.replace(TEMPLATE_SLUG, m["slug"])
    head = re.sub(r"<title>.*?</title>", lambda _: f"<title>{esc(seo_meta(m))}</title>", head)
    for prop in ["og:title", "twitter:title"]:
        head = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*', rf"\g<1>{esc(m['og_title'])}", head)
    for prop in ["description", "og:description", "twitter:description"]:
        head = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*', rf"\g<1>{esc(m['description'])}", head)
    for prop in ["og:image", "twitter:image"]:
        head = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*', rf"\g<1>{img}", head)
    head = re.sub(r'(<meta property="article:published_time" content=")[^"]*', rf"\g<1>{m['date']}", head)
    head = head.replace('<meta name="author" content="Alessandro Capezza">',
                        f'<meta name="author" content="Alessandro Capezza">\n<link rel="author" href="{LINKEDIN}">')

    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "NewsArticle", "@id": url + "#article", "headline": m["og_title"],
         "description": m["description"], "image": img, "datePublished": m["date"],
         "dateModified": m["date"], "inLanguage": "en", "keywords": m["keywords"],
         "mainEntityOfPage": url,
         "author": {"@type": "Person", "name": "Alessandro Capezza", "url": LINKEDIN,
                    "jobTitle": "AI Coach", "sameAs": [LINKEDIN, "https://www.instagram.com/alexislimitless/",
                                                       "https://www.youtube.com/@alexislimitless"]},
         "publisher": {"@type": "Organization", "name": "AI Coach Alex", "url": "https://aicoachalex.com/",
                       "logo": {"@type": "ImageObject", "url": "https://aicoachalex.com/assets/aicoachalex-mark.png"}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "AI Coach Alex", "item": "https://aicoachalex.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://aicoachalex.com/blog/"},
            {"@type": "ListItem", "position": 3, "name": m["og_title"], "item": url}]},
    ]}
    if m.get("faq"):
        ld["@graph"].append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]})
    ldjson = '<script type="application/ld+json">\n' + json.dumps(ld, indent=1, ensure_ascii=False) + "\n</script>\n"

    nav = nav.replace(f"/blog/{TEMPLATE_SLUG}.html", f"/blog/{m['slug']}.html")
    page = head + ldjson + styles + EXTRA_CSS + "\n" + nav + article + "\n" + footer
    out = ROOT / "blog" / f"{m['slug']}.html"
    out.write_text(page)

    # --- blog index card ---
    idx = ROOT / "blog/index.html"
    s = idx.read_text()
    href = f"/blog/{m['slug']}.html"
    if href not in s:
        d = datetime.date.fromisoformat(m["date"])
        card = f"""
  <!-- NEW {m['date']} -->
  <a href="{href}" class="blog-card">
    <div class="blog-card-meta">
      <span class="blog-card-tag">{esc(m['tag'])}</span>
      <span>{m['read_min']} min read · {d.day} {d.strftime('%b %Y')}</span>
    </div>
    <h2 class="blog-card-title">{esc(m['og_title'])}</h2>
    <p class="blog-card-excerpt">{esc(m['excerpt'])}</p>
    <span class="blog-card-read">Read article</span>
  </a>
"""
        s = s.replace('<section class="blog-grid">\n', '<section class="blog-grid">\n' + card, 1)
        idx.write_text(s)

    # --- sitemap ---
    sm = ROOT / "sitemap.xml"
    x = sm.read_text()
    if url not in x:
        x = x.replace("</urlset>", f"  <url><loc>{url}</loc><lastmod>{m['date']}</lastmod></url>\n</urlset>")
        sm.write_text(x)

    # --- llms.txt (newest post first, under the Blog section, for AI answer engines) ---
    llms = ROOT / "llms.txt"
    if llms.exists():
        t = llms.read_text()
        head = "## Blog: AI news and guides for professionals and small businesses\n\n"
        if url not in t and head in t:
            i = t.index(head) + len(head)
            j = t.index("\n", i) + 1  # keep the blog-index line first
            t = t[:j] + f"- [{m['title']}]({url}): {m['description']}\n" + t[j:]
            llms.write_text(t)
    print("built", out)
    print("NEXT: build the ES and IT versions in this same run (build_blog_translation.py with meta.es.json / meta.it.json);\n"
          "      _tools/check_translations.py fails the next day if they are missing.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    # Indexing guardrail: fail loudly if this build left a bad canonical,
    # a page missing from sitemap.xml, or an orphan page.
    import subprocess
    sys.exit(subprocess.call([sys.executable, str(pathlib.Path(__file__).with_name("check_seo.py"))]))
