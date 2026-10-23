"""Render brand-book blog images (AI Coach Alex) from HTML templates with headless Chromium.
Usage: python3 render.py <out_dir>
"""
import sys, os, base64, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FP = HERE / "fontpkg/node_modules"
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
FONTS = f"""
@font-face{{font-family:'Fraunces';font-style:normal;font-weight:100 900;src:url(data:font/woff2;base64,{b64(FP/'@fontsource-variable/fraunces/files/fraunces-latin-wght-normal.woff2')}) format('woff2');}}
@font-face{{font-family:'Fraunces';font-style:italic;font-weight:100 900;src:url(data:font/woff2;base64,{b64(FP/'@fontsource-variable/fraunces/files/fraunces-latin-wght-italic.woff2')}) format('woff2');}}
@font-face{{font-family:'Instrument Sans';font-weight:400;src:url(data:font/woff2;base64,{b64(FP/'@fontsource/instrument-sans/files/instrument-sans-latin-400-normal.woff2')}) format('woff2');}}
@font-face{{font-family:'Instrument Sans';font-weight:500;src:url(data:font/woff2;base64,{b64(FP/'@fontsource/instrument-sans/files/instrument-sans-latin-500-normal.woff2')}) format('woff2');}}
"""
BASE = """
:root{--white:#f8f6f1;--black:#0d0c0a;--green:#9fe870;--green-deep:#163300;--muted:#7a7670;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Instrument Sans',sans-serif;-webkit-font-smoothing:antialiased}
.f{font-family:'Fraunces',serif}
.lbl{font-size:22px;letter-spacing:.16em;text-transform:uppercase;font-weight:500}
"""

def hero(w, h, scale):
    s = scale
    return f"""<div style="width:{w}px;height:{h}px;background:#0d0c0a;color:#f8f6f1;padding:{70*s}px {84*s}px;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden">
<div style="position:absolute;right:-{120*s}px;top:-{120*s}px;width:{520*s}px;height:{520*s}px;border-radius:50%;border:{2*s}px solid rgba(159,232,112,.25)"></div>
<div style="position:absolute;right:-{40*s}px;top:-{40*s}px;width:{360*s}px;height:{360*s}px;border-radius:50%;border:{2*s}px solid rgba(159,232,112,.18)"></div>
<div style="display:flex;gap:{18*s}px;align-items:center"><span class="lbl" style="font-size:{20*s}px;background:#9fe870;color:#0d0c0a;padding:{6*s}px {14*s}px">AI News</span><span class="lbl" style="font-size:{20*s}px;color:#7a7670">23 Oct 2026 · AI Coach Alex</span></div>
<h1 class="f" style="font-size:{104*s}px;font-weight:900;line-height:.98;letter-spacing:-.035em;max-width:{1180*s}px">Write your AI playbook once.<br><em style="color:#9fe870;font-weight:700">Run it everywhere.</em></h1>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:{14*s}px">
{''.join(f'<div style="border:{1.5*s}px solid rgba(248,246,241,.22);border-radius:{10*s}px;padding:{18*s}px {20*s}px"><div class="f" style="font-size:{30*s}px;font-weight:700;letter-spacing:-.02em">{a}</div><div style="font-size:{19*s}px;color:#9fe870;margin-top:{6*s}px">from {b}</div></div>' for a,b in [("Agent Skills","Anthropic"),("Open Responses","OpenAI"),("OpenEnv","Hugging Face"),("OpenSandbox","Alibaba")])}
</div></div>"""

def anatomy():
    rows = [("my-weekly-report/", "the skill = one folder", True),
            ("├─ SKILL.md", "name, when to use it, the steps", False),
            ("├─ references/", "your examples, tone, checklists", False),
            ("├─ scripts/", "optional: code it can run", False),
            ("└─ assets/", "templates, logos, files", False)]
    tree = "".join(f'<div style="display:flex;justify-content:space-between;gap:24px;padding:14px 0;border-bottom:1px solid rgba(13,12,10,.1)"><span style="font-family:ui-monospace,Menlo,monospace;font-size:30px;font-weight:{700 if b else 500};color:{"#163300" if b else "#0d0c0a"}">{a}</span><span style="font-size:24px;color:#7a7670">{c}</span></div>' for a,c,b in rows)
    stages = [("1","At start","Only the name + description (~100 tokens)"),("2","When needed","The SKILL.md instructions load"),("3","If required","Files and scripts open on demand")]
    st = "".join(f'<div style="flex:1;background:#0d0c0a;color:#f8f6f1;border-radius:12px;padding:22px 24px"><div class="f" style="font-size:44px;font-weight:900;color:#9fe870;line-height:1">{n}</div><div style="font-size:20px;letter-spacing:.12em;text-transform:uppercase;margin:10px 0 6px;font-weight:500">{t}</div><div style="font-size:22px;color:rgba(248,246,241,.75);line-height:1.35">{d}</div></div>' for n,t,d in stages)
    return f"""<div style="width:1600px;height:900px;background:#f8f6f1;color:#0d0c0a;padding:64px 84px;display:flex;flex-direction:column;gap:30px">
<div class="lbl" style="color:#163300">Anatomy of an Agent Skill</div>
<h2 class="f" style="font-size:66px;font-weight:900;letter-spacing:-.03em;line-height:1">A folder your AI <em style="color:#163300;font-weight:700">reads when it needs it.</em></h2>
<div style="display:grid;grid-template-columns:1.15fr 1fr;gap:56px;align-items:start;margin-top:6px">
<div style="border-top:2px solid #0d0c0a">{tree}</div>
<div style="display:flex;flex-direction:column;gap:14px">{st}</div>
</div>
<div style="margin-top:auto;font-size:22px;color:#7a7670">Same folder works in Claude, Codex, Gemini CLI, Cursor, GitHub Copilot and 30+ other tools · aicoachalex.com</div>
</div>"""

def today():
    cards = [("100–180ms","OpenAI Decisions API, now open to every developer","down from 1–3 seconds",False),
             ("~$15B","DeepSeek's new funding round, led by Tencent and CATL","One of China's largest AI rounds",False),
             ("10","Open agent projects now under the Linux Foundation","up from 3 in Dec 2025",True)]
    c = "".join(f'<div style="background:{"#9fe870" if hi else "#0d0c0a"};color:{"#0d0c0a" if hi else "#f8f6f1"};border-radius:14px;padding:34px 32px;display:flex;flex-direction:column;gap:14px"><div class="f" style="font-size:96px;font-weight:900;letter-spacing:-.04em;line-height:1;color:{"#163300" if hi else "#9fe870"}">{n}</div><div style="font-size:30px;line-height:1.3;font-weight:500">{t}</div><div style="font-size:22px;opacity:.65;margin-top:auto">{s}</div></div>' for n,t,s,hi in cards)
    return f"""<div style="width:1600px;height:900px;background:#f8f6f1;color:#0d0c0a;padding:64px 84px;display:flex;flex-direction:column;gap:40px">
<div class="lbl" style="color:#163300">Also today · 22–23 Oct 2026</div>
<h2 class="f" style="font-size:72px;font-weight:900;letter-spacing:-.03em;line-height:1">Three numbers <em style="color:#163300;font-weight:700">worth knowing.</em></h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;flex:1">{c}</div>
<div style="font-size:22px;color:#7a7670">aicoachalex.com/blog</div></div>"""

def main(out):
    os.makedirs(out, exist_ok=True)
    jobs = {"hero.png": (hero(1600, 900, 1), 1600, 900),
            "og.png": (hero(1200, 630, .74), 1200, 630),
            "skill-anatomy.png": (anatomy(), 1600, 900),
            "also-today.png": (today(), 1600, 900)}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1243/chrome-linux64/chrome")
        for name, (body, w, h) in jobs.items():
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.set_content(f"<html><head><style>{FONTS}{BASE}</style></head><body>{body}</body></html>")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(out, name), type="png")
        b.close()

if __name__ == "__main__":
    main(sys.argv[1])
