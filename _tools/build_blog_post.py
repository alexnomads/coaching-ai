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


def main(meta_path, article_path):
    m = json.loads(pathlib.Path(meta_path).read_text())
    article = add_utm(pathlib.Path(article_path).read_text(), m["slug"])
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
    head = re.sub(r"<title>.*?</title>", f"<title>{esc(m['title'])} — AI Coach Alex</title>", head)
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
    print("built", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
