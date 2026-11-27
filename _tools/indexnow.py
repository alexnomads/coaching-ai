#!/usr/bin/env python3
"""Submit URLs to IndexNow (Bing, Yandex, etc.). Key file: /<key>.txt in the site root.

Usage: python3 _tools/indexnow.py            # every URL in sitemap.xml
       python3 _tools/indexnow.py URL [URL…] # only these URLs
"""
import json, re, sys, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "aicoachalex.com"
KEY = next(p.stem for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem))
urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text())
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls[:10000]}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow:", r.status, f"{len(urls)} URLs submitted")
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:200]); sys.exit(1)
