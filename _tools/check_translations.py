#!/usr/bin/env python3
"""Fail if a recent English blog post has no Spanish and/or Italian version.

The daily blog job must build EN + ES + IT in the same run (build_blog_post.py, then
build_blog_translation.py for es and it). This catches a run that skipped them.

  python3 _tools/check_translations.py            # list every EN post missing ES/IT; exit 1 only
                                                  # for posts dated ENFORCE_FROM or later and at
                                                  # least GRACE_DAYS old (so a same-day run in
                                                  # progress is not flagged)
  python3 _tools/check_translations.py --all      # also exit 1 for the older backlog
"""
import datetime, json, os, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENFORCE_FROM = datetime.date(2026, 11, 26)   # posts before this are a known backlog (listed, not failing)
GRACE_DAYS = 1

slugs = json.loads((ROOT / "_tools/blog_slugs.json").read_text())
today = datetime.date.today()
rows = []
for f in sorted((ROOT / "blog").glob("*.html")):
    n = f.name
    if re.search(r"\.(es|it)\.html$", n) or n.startswith("index"):
        continue
    slug = f.stem
    m = re.search(r'article:published_time" content="(\d{4}-\d{2}-\d{2})', f.read_text())
    d = datetime.date.fromisoformat(m.group(1)) if m else None
    miss = [l for l in ("es", "it") if not (ROOT / f"blog/{slugs.get(slug, {}).get(l, slug)}.{l}.html").exists()]
    if miss:
        rows.append((d, slug, miss))

fail = 0
for d, slug, miss in sorted(rows, key=lambda r: (r[0] or datetime.date.min), reverse=True):
    enforced = sys.argv.count("--all") or (d and d >= ENFORCE_FROM and (today - d).days >= GRACE_DAYS)
    print(("FAIL " if enforced else "backlog ") + f"{d} {slug}: missing {', '.join(miss)}")
    fail += bool(enforced)
if not rows:
    print("OK: every English post has ES and IT versions")
elif not fail:
    print(f"OK: {len(rows)} older post(s) still untranslated (backlog), none newer than {ENFORCE_FROM}")
sys.exit(1 if fail else 0)
