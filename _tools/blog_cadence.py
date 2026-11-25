#!/usr/bin/env python3
"""Should a NEW English AI-news post be written today?

Reads _content/blog-cadence.json (key ai_news_posts_per_week, default 7 = every day).
Override without editing the file: BLOG_AI_NEWS_POSTS_PER_WEEK=2 python3 _tools/blog_cadence.py

Usage:  python3 _tools/blog_cadence.py [YYYY-MM-DD]   (date defaults to today, Europe/Madrid)
Prints "POST <n>/week <weekday>" and exits 0 when today is a posting day, or
"SKIP <n>/week <weekday>" and exits 1 when it is not.
ES/IT translations of an English post that already exists are never skipped by this.
Any config problem falls back to 7/week (post every day) so a typo can't silence the blog.
"""
import json, os, sys, pathlib, datetime
from zoneinfo import ZoneInfo

CFG = pathlib.Path(__file__).resolve().parent.parent / "_content/blog-cadence.json"
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def main(argv):
    try:
        cfg = json.loads(CFG.read_text())
        n = int(os.environ.get("BLOG_AI_NEWS_POSTS_PER_WEEK") or cfg.get("ai_news_posts_per_week", 7))
        days = cfg["post_days_by_count"][str(n)]
    except Exception:
        n, days = 7, DAYS
    d = (datetime.date.fromisoformat(argv[1]) if len(argv) > 1
         else datetime.datetime.now(ZoneInfo("Europe/Madrid")).date())
    wd = DAYS[d.weekday()]
    ok = wd in days
    print(f"{'POST' if ok else 'SKIP'} {n}/week {wd}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
