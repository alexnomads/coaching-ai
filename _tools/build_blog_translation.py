#!/usr/bin/env python3
"""Build the Spanish or Italian version of an existing English blog post on aicoachalex.com.

The English page blog/<slug>.html must already exist (built with build_blog_post.py).
This script reuses it as the base, swaps in the translated <article> fragment, localised
metadata, nav and footer (taken from an existing ES/IT post), then:
  - writes blog/<slug>.<lang>.html
  - links EN/ES/IT versions to each other (hreflang + the EN·ES·IT switcher) on every version
  - adds a card at the top of blog/index.<lang>.html
  - adds the URL to sitemap.xml

Usage:
  python3 _tools/build_blog_translation.py meta.<lang>.json article.<lang>.html

meta keys: slug (the English slug), lang (es|it), title, og_title, description, date,
tag, read_min, excerpt, keywords, image, faq [[q,a],...]
"""
import json, re, sys, html, pathlib, datetime

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_blog_post import add_utm, ROOT  # noqa: E402

LOCALE_TEMPLATE_SLUG = "how-to-stay-relevant-ai-era"   # existing post with EN/ES/IT versions
L10N = {
    "es": {"copied": "Copiado", "copy": "Copiar", "read": "Leer artículo", "min": "min de lectura",
           "months": "ene feb mar abr may jun jul ago sep oct nov dic"},
    "it": {"copied": "Copiato", "copy": "Copia", "read": "Leggi l'articolo", "min": "min di lettura",
           "months": "gen feb mar apr mag giu lug ago set ott nov dic"},
}
BASE = "https://aicoachalex.com/blog/"


def page_url(slug, lang):
    return f"{BASE}{slug}.html" if lang == "en" else f"{BASE}{slug}.{lang}.html"


def link_versions(slug):
    """Give every existing language version of <slug> the full hreflang set and a working switcher."""
    langs = ["en"] + [l for l in ("es", "it") if (ROOT / f"blog/{slug}.{l}.html").exists()]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{page_url(slug, l)}">\n' for l in langs)
    alts += f'<link rel="alternate" hreflang="x-default" href="{page_url(slug, "en")}">\n'
    for l in langs:
        p = ROOT / (f"blog/{slug}.html" if l == "en" else f"blog/{slug}.{l}.html")
        s = p.read_text()
        s = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n)+', alts, s, count=1)
        # language switcher: point each code at that version of this post
        for code in langs:
            target = f"/blog/{slug}.html" if code == "en" else f"/blog/{slug}.{code}.html"
            s = re.sub(rf'<a href="[^"]*"((?: class="on")?) onclick="try{{localStorage.setItem\(\'preferred-lang\',\'{code}\'\)',
                       rf'<a href="{target}"\1 onclick="try{{localStorage.setItem(\'preferred-lang\',\'{code}\')', s)
        p.write_text(s)


def main(meta_path, article_path):
    m = json.loads(pathlib.Path(meta_path).read_text())
    slug, lang = m["slug"], m["lang"]
    L = L10N[lang]
    esc = lambda s: html.escape(s, quote=True)
    en_url, url = page_url(slug, "en"), page_url(slug, lang)
    img = f"https://aicoachalex.com{m['image']}"

    base = (ROOT / f"blog/{slug}.html").read_text()
    loc = (ROOT / f"blog/{LOCALE_TEMPLATE_SLUG}.{lang}.html").read_text()
    article = add_utm(pathlib.Path(article_path).read_text(), f"{slug}-{lang}").strip()

    s = base
    s = s.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    s = s[:s.index("<article>")] + article + s[s.index("</article>") + len("</article>"):]
    # nav and footer from the localised template
    loc_nav = loc[loc.index("<body>"):loc.index("<article>")].replace(LOCALE_TEMPLATE_SLUG, slug)
    s = s[:s.index("<body>")] + loc_nav + s[s.index("<article>"):]
    loc_footer = loc[loc.index("<footer"):loc.index("</footer>") + len("</footer>")]
    s = s[:s.index("<footer")] + loc_footer + s[s.index("</footer>") + len("</footer>"):]
    s = s.replace("b.textContent='Copied';setTimeout(function(){b.textContent='Copy'}",
                  f"b.textContent='{L['copied']}';setTimeout(function(){{b.textContent='{L['copy']}'}}")

    # head metadata
    s = re.sub(r"<title>.*?</title>", f"<title>{esc(m['title'])} — AI Coach Alex</title>", s, count=1)
    for prop in ["og:title", "twitter:title"]:
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*', rf"\g<1>{esc(m['og_title'])}", s)
    for prop in ["description", "og:description", "twitter:description"]:
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*', lambda x: x.group(1) + esc(m["description"]), s)
    for prop in ["og:image", "twitter:image"]:
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*', rf"\g<1>{img}", s)
    s = s.replace(f'<link rel="canonical" href="{en_url}">', f'<link rel="canonical" href="{url}">')
    s = s.replace(f'<meta property="og:url" content="{en_url}">', f'<meta property="og:url" content="{url}">')

    # JSON-LD
    def fix_ld(match):
        ld = json.loads(match.group(1))
        for node in ld["@graph"]:
            if node["@type"] == "NewsArticle":
                node.update({"@id": url + "#article", "headline": m["og_title"], "description": m["description"],
                             "image": img, "inLanguage": lang, "keywords": m["keywords"], "mainEntityOfPage": url})
            elif node["@type"] == "BreadcrumbList":
                node["itemListElement"][1]["item"] = f"{BASE}index.{lang}.html"
                node["itemListElement"][2].update({"name": m["og_title"], "item": url})
        ld["@graph"] = [n for n in ld["@graph"] if n["@type"] != "FAQPage"]
        if m.get("faq"):
            ld["@graph"].append({"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]})
        return '<script type="application/ld+json">\n' + json.dumps(ld, indent=1, ensure_ascii=False) + "\n</script>"
    s = re.sub(r'<script type="application/ld\+json">\n(.*?)\n</script>', fix_ld, s, count=1, flags=re.S)

    out = ROOT / f"blog/{slug}.{lang}.html"
    out.write_text(s)
    link_versions(slug)

    # blog index card
    idx = ROOT / f"blog/index.{lang}.html"
    t = idx.read_text()
    href = f"/blog/{slug}.{lang}.html"
    if href not in t:
        d = datetime.date.fromisoformat(m["date"])
        mon = L["months"].split()[d.month - 1]
        card = f"""
  <!-- NEW {m['date']} -->
  <a href="{href}" class="blog-card">
    <div class="blog-card-meta">
      <span class="blog-card-tag">{esc(m['tag'])}</span>
      <span>{m['read_min']} {L['min']} · {d.day} {mon} {d.year}</span>
    </div>
    <h2 class="blog-card-title">{esc(m['og_title'])}</h2>
    <p class="blog-card-excerpt">{esc(m['excerpt'])}</p>
    <span class="blog-card-read">{L['read']}</span>
  </a>
"""
        t = t.replace('<section class="blog-grid">\n', '<section class="blog-grid">\n' + card, 1)
        idx.write_text(t)

    sm = ROOT / "sitemap.xml"
    x = sm.read_text()
    if url not in x:
        x = x.replace("</urlset>", f"  <url><loc>{url}</loc><lastmod>{m['date']}</lastmod></url>\n</urlset>")
        sm.write_text(x)
    print("built", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
