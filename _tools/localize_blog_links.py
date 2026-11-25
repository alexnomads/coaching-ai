#!/usr/bin/env python3
"""Point internal blog links inside ES/IT articles at the ES/IT version of the target post, when one exists.

Only touches <article> bodies (never the language switcher / hreflang), and only
links of the form /blog/<english-slug>.html. Slug map: _tools/blog_slugs.json.

Usage: python3 _tools/localize_blog_links.py [--only slug1,slug2]   (limit to links that point at these English posts)
       python3 _tools/localize_blog_links.py --pages file1,file2    (limit to these ES/IT pages)
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
slugs = json.loads((ROOT / "_tools/blog_slugs.json").read_text())


def localized(slug, lang):
    ls = slugs.get(slug, {}).get(lang)
    if not ls:
        return None
    p = f"/blog/{ls}.{lang}.html"
    return p if (ROOT / p.lstrip("/")).exists() else None


def main(only=None, pages=None):
    changed = 0
    for lang in ("es", "it"):
        for f in sorted((ROOT / "blog").glob(f"*.{lang}.html")):
            if pages and f.name not in pages:
                continue
            s = f.read_text()
            if "<article>" not in s:
                continue
            a0, a1 = s.index("<article>"), s.index("</article>")
            art = s[a0:a1]

            def sub(m):
                slug = m.group(1)
                if only and slug not in only:
                    return m.group(0)
                new = localized(slug, lang)
                return f'href="{new}"' if new else m.group(0)

            new_art = re.sub(r'href="/blog/([a-z0-9-]+)\.html"', sub, art)
            if new_art != art:
                f.write_text(s[:a0] + new_art + s[a1:])
                changed += 1
    print("pages updated:", changed)


if __name__ == "__main__":
    only = pages = None
    for i, a in enumerate(sys.argv):
        if a == "--only":
            only = set(sys.argv[i + 1].split(","))
        if a == "--pages":
            pages = set(sys.argv[i + 1].split(","))
    main(only, pages)
