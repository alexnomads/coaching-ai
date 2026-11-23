#!/usr/bin/env python3
"""Indexing guardrail for aicoachalex.com.

Run before every push (and automatically on GitHub, see .github/workflows/seo-check.yml):

    python3 _tools/check_seo.py            # report problems, exit 1 if any
    python3 _tools/check_seo.py --fix      # also rewrite sitemap.xml lastmod from git history
                                           # and add any indexable page missing from the sitemap

Rules it enforces (each one maps to a Google Search Console "not indexed" reason):
  1. Every indexable page has exactly one <link rel="canonical"> pointing to itself on
     https://aicoachalex.com  -> prevents "Duplicate without user-selected canonical" and
     "Alternative page with proper canonical tag" caused by copy-paste canonicals.
  2. Pages with noindex or a meta-refresh redirect are NOT in sitemap.xml
     -> prevents "Excluded by noindex" / "Page with redirect" reports on URLs we asked Google to index.
  3. Every indexable page IS in sitemap.xml, and every sitemap URL exists as a file.
  4. ES/IT pages declare hreflang alternates.
  5. Every indexable page has at least one internal link pointing to it (no orphans).
"""
import collections
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://aicoachalex.com/"
SITEMAP = ROOT / "sitemap.xml"

# Pages that are deliberately not indexed. Keep this list short.
INTENTIONAL_NOINDEX = {"thank-you.html", "index-old.html", "index-old.es.html"}  # pre-redesign homepage backups


def url_of(rel: str) -> str:
    if rel == "index.html":
        return BASE
    if rel.endswith("/index.html"):
        return BASE + rel[: -len("index.html")]
    return BASE + rel


def public_pages():
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT).as_posix()
        if any(part.startswith((".", "_")) for part in rel.split("/")):
            continue
        yield rel, p


def head_of(html: str) -> str:
    return html.split("</head>", 1)[0]


def canonical_of(head: str):
    found = re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*>', head, re.I)
    hrefs = [re.search(r'href=["\']([^"\']+)', tag).group(1) for tag in found if "href=" in tag]
    return hrefs


def is_noindex(head: str) -> bool:
    return bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]*noindex', head, re.I))


def is_redirect(head: str) -> bool:
    return bool(re.search(r'http-equiv=["\']refresh', head, re.I))


def internal_targets(rel: str, html: str):
    body = html.split("</head>", 1)[-1]
    here = "/" + rel
    for href in re.findall(r'href=["\']([^"\'#?]+)', body):
        if href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        if href.startswith("http"):
            if "aicoachalex.com" not in href:
                continue
            href = re.sub(r"^https?://(www\.)?aicoachalex\.com", "", href)
        elif not href.startswith("/"):
            href = os.path.normpath(os.path.join(os.path.dirname(here), href))
        if href.endswith("/") or href == "":
            href = href.rstrip("/") + "/index.html"
        yield url_of(href.lstrip("/"))


def git_lastmod(path: Path):
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.strip()
    return out or None


def main():
    fix = "--fix" in sys.argv
    sitemap_xml = SITEMAP.read_text()
    in_sitemap = set(re.findall(r"<loc>(.*?)</loc>", sitemap_xml))

    pages = {}
    inbound = collections.Counter()
    for rel, p in public_pages():
        html = p.read_text(errors="ignore")
        pages[url_of(rel)] = (rel, p, html)
        for t in internal_targets(rel, html):
            if t != url_of(rel):
                inbound[t] += 1

    problems = []
    indexable = {}
    for url, (rel, p, html) in sorted(pages.items()):
        head = head_of(html)
        if "AW-18591414066" not in head and "</head>" in html:
            problems.append(f"{rel}: Google Ads tag (AW-18591414066) missing from <head>")
        canon = canonical_of(head)
        noindex, redirect = is_noindex(head), is_redirect(head)
        if noindex or redirect:
            if url in in_sitemap:
                problems.append(f"{rel}: noindex/redirect page is listed in sitemap.xml - remove it")
            if noindex and not redirect and rel not in INTENTIONAL_NOINDEX:
                problems.append(f"{rel}: has noindex but is not in INTENTIONAL_NOINDEX - remove the tag or allowlist it")
            continue
        indexable[url] = p
        if len(canon) != 1:
            problems.append(f"{rel}: expected 1 canonical tag, found {len(canon)}")
        elif canon[0] != url:
            problems.append(f"{rel}: canonical points to {canon[0]} - should be {url}")
        if url not in in_sitemap:
            problems.append(f"{rel}: indexable but missing from sitemap.xml")
        if re.search(r"\.(es|it)\.html$|^(es|it)/", rel) and "hreflang=" not in head:
            problems.append(f"{rel}: ES/IT page without hreflang alternates")
        if inbound[url] == 0 and url != BASE:
            problems.append(f"{rel}: orphan - no internal page links to it")

    for loc in sorted(in_sitemap):
        if loc not in pages:
            problems.append(f"sitemap.xml: {loc} has no matching file")

    if fix:
        missing = [u for u in indexable if u not in in_sitemap]
        entries = []
        for url, p in sorted(indexable.items()):
            lm = git_lastmod(p)
            entries.append(f"  <url><loc>{url}</loc>" + (f"<lastmod>{lm}</lastmod>" if lm else "") + "</url>")
        SITEMAP.write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(entries) + "\n</urlset>\n"
        )
        print(f"sitemap.xml rewritten: {len(entries)} URLs, lastmod from git, {len(missing)} added")
        problems = [x for x in problems if "sitemap.xml" not in x]

    if problems:
        print(f"{len(problems)} indexing problem(s):")
        for x in problems:
            print("  -", x)
        sys.exit(1)
    print(f"OK: {len(indexable)} indexable pages, all canonical, in sitemap, linked.")


if __name__ == "__main__":
    main()
