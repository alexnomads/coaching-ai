"""Shareable images for the 'AI agents are your next customers' post: horizontal (desktop) + vertical 4:5 (mobile/Instagram)."""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
SITE = pathlib.Path("/home/claude/coaching-ai")
FP = HERE / "fontpkg/node_modules"
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
FONTS = f"""
@font-face{{font-family:'Fraunces';font-style:normal;font-weight:100 900;src:url(data:font/woff2;base64,{b64(FP/'@fontsource-variable/fraunces/files/fraunces-latin-wght-normal.woff2')})}}
@font-face{{font-family:'Fraunces';font-style:italic;font-weight:100 900;src:url(data:font/woff2;base64,{b64(FP/'@fontsource-variable/fraunces/files/fraunces-latin-wght-italic.woff2')})}}
@font-face{{font-family:'IS';font-weight:400;src:url(data:font/woff2;base64,{b64(FP/'@fontsource/instrument-sans/files/instrument-sans-latin-400-normal.woff2')})}}
@font-face{{font-family:'IS';font-weight:500;src:url(data:font/woff2;base64,{b64(FP/'@fontsource/instrument-sans/files/instrument-sans-latin-500-normal.woff2')})}}
"""
MARK = b64(SITE / "assets/aicoachalex-mark.png")
CSS = """*{box-sizing:border-box;margin:0;padding:0}body{font-family:'IS',sans-serif;-webkit-font-smoothing:antialiased;overflow:hidden}
.f{font-family:'Fraunces',serif}.c{display:flex;flex-direction:column;position:relative;overflow:hidden}
.dark{background:#0d0c0a;color:#f8f6f1}.light{background:#f8f6f1;color:#0d0c0a}.lime{background:#9fe870;color:#0d0c0a}
.dark em{color:#9fe870}.light em,.lime em{color:#163300}em{font-weight:700}
.lbl{letter-spacing:.16em;text-transform:uppercase;font-weight:500}
.brand{display:flex;align-items:center;gap:.6em;letter-spacing:.14em;text-transform:uppercase;font-weight:500}
.brand img{border-radius:6px}.mut{color:#7a7670}
"""

def brand(px, theme):
    col = "#163300" if theme == "lime" else "#7a7670"
    return f'<div class="brand" style="font-size:{px}px;color:{col}"><img src="data:image/png;base64,{MARK}" style="width:{px*2.2}px;height:{px*2.2}px">AI Coach Alex · aicoachalex.com</div>'

# ---------- 1. HERO ----------
def hero(w, h):
    v = h > w
    s = w / 1600 if not v else w / 1080
    rungs = [("Research", "OK"), ("Prepare", "Contested"), ("Pay", "The fight")]
    chips = "".join(f'<div style="flex:1;border:{2*s}px solid rgba(248,246,241,.22);border-radius:{12*s}px;padding:{18*s}px {22*s}px"><div class="f" style="font-size:{(34 if not v else 44)*s}px;font-weight:700">{a}</div><div style="font-size:{(20 if not v else 28)*s}px;color:#9fe870;margin-top:{6*s}px">{b}</div></div>' for a, b in rungs)
    title_px = (96 if not v else 100) * s
    return f"""<div class="c dark" style="width:{w}px;height:{h}px;padding:{(70 if not v else 90)*s}px {84*s}px;justify-content:space-between">
<div style="position:absolute;right:-{140*s}px;top:-{140*s}px;width:{560*s}px;height:{560*s}px;border-radius:50%;border:{2*s}px solid rgba(159,232,112,.22)"></div>
<div style="display:flex;gap:{16*s}px;align-items:center"><span class="lbl" style="font-size:{(20 if not v else 26)*s}px;background:#9fe870;color:#0d0c0a;padding:{6*s}px {14*s}px">From the coaching room</span></div>
<div><div class="f" style="font-size:{title_px}px;font-weight:900;line-height:.98;letter-spacing:-.035em">Your next customer won't look at your website.<br><em style="font-style:italic">It will read it.</em></div>
<div style="font-size:{(28 if not v else 38)*s}px;line-height:1.35;color:rgba(248,246,241,.72);margin-top:{(28 if not v else 44)*s}px;max-width:{1150*s}px">AI agents are starting to research, compare and buy for people. Is your business ready for them?</div></div>
<div><div style="display:flex;gap:{14*s}px">{chips}</div><div style="margin-top:{(26 if not v else 40)*s}px">{brand((18 if not v else 24)*s, 'dark')}</div></div></div>"""

# ---------- 2. LADDER ----------
LADDER = [
    ("3", "Pay", "The agent places the order or booking.", "Where the fight is. Big platforms block here to protect ads and upsells.", "Keep a human check: deposit link or your final OK."),
    ("2", "Prepare", "The agent builds the quote or basket.", "Needs real prices, rules and availability it can read.", "Publish price ranges and your rules in plain text."),
    ("1", "Research", "The agent finds and compares options.", "Most companies already allow this. It works like search.", "Let every agent in. Make your facts easy to read."),
]
def ladder(w, h):
    v = h > w
    s = w / 1600 if not v else w / 1080
    rows = ""
    for n, name, what, fight, you in LADDER:
        hi = name == "Pay"
        bg = "#0d0c0a" if hi else "#ffffff"
        fg = "#f8f6f1" if hi else "#0d0c0a"
        sub = "rgba(248,246,241,.7)" if hi else "#7a7670"
        youc = "#9fe870" if hi else "#163300"
        if not v:
            rows += f'''<div style="display:grid;grid-template-columns:{90*s}px {220*s}px 1fr 1fr;gap:{24*s}px;align-items:center;background:{bg};color:{fg};border:{2*s}px solid #0d0c0a;border-radius:{14*s}px;padding:{22*s}px {28*s}px">
<div class="f" style="font-size:{72*s}px;font-weight:900;color:{youc};line-height:1">{n}</div>
<div><div class="f" style="font-size:{40*s}px;font-weight:700">{name}</div><div style="font-size:{19*s}px;color:{sub};margin-top:{4*s}px;line-height:1.3">{what}</div></div>
<div style="font-size:{22*s}px;color:{sub};line-height:1.4">{fight}</div>
<div style="font-size:{22*s}px;line-height:1.4;font-weight:500;color:{youc}">→ {you}</div></div>'''
        else:
            rows += f'''<div style="background:{bg};color:{fg};border:{2*s}px solid #0d0c0a;border-radius:{18*s}px;padding:{26*s}px {32*s}px">
<div style="display:flex;align-items:baseline;gap:{18*s}px"><span class="f" style="font-size:{64*s}px;font-weight:900;color:{youc};line-height:1">{n}</span><span class="f" style="font-size:{50*s}px;font-weight:700">{name}</span></div>
<div style="font-size:{27*s}px;color:{sub};margin-top:{8*s}px;line-height:1.35">{fight}</div>
<div style="font-size:{29*s}px;line-height:1.35;font-weight:500;color:{youc};margin-top:{10*s}px">→ {you}</div></div>'''
    return f"""<div class="c light" style="width:{w}px;height:{h}px;padding:{(56 if not v else 80)*s}px {(84 if not v else 70)*s}px;gap:{(18 if not v else 22)*s}px">
<div class="lbl" style="font-size:{(20 if not v else 26)*s}px;color:#163300">The ladder of trust</div>
<div class="f" style="font-size:{(58 if not v else 74)*s}px;font-weight:900;letter-spacing:-.03em;line-height:1.02;margin-bottom:{(10 if not v else 14)*s}px">How far will you let <em style="font-style:italic">an agent</em> go?</div>
{rows}
<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:20px">{brand((18 if not v else 22)*s,'light')}<span class="mut" style="font-size:{(16 if not v else 20)*s}px">Framework: Greg Isenberg</span></div></div>"""

# ---------- 3. TEST SCORECARD ----------
STATS = [("0/3", "found the business on their own"), ("3/3", "ranked it well when asked by name"), ("0/3", "quoted the real price"), ("0/3", "could book it")]
def score(w, h):
    v = h > w
    s = w / 1600 if not v else w / 1080
    cols = 4 if not v else 2
    cards = "".join(f'<div style="background:{"#9fe870" if n=="3/3" else "#1a1917"};color:{"#0d0c0a" if n=="3/3" else "#f8f6f1"};border-radius:{16*s}px;padding:{(30 if not v else 34)*s}px;display:flex;flex-direction:column;gap:{12*s}px"><div class="f" style="font-size:{(104 if not v else 116)*s}px;font-weight:900;letter-spacing:-.04em;line-height:1;color:{"#163300" if n=="3/3" else "#9fe870"}">{n}</div><div style="font-size:{(26 if not v else 32)*s}px;line-height:1.3">{t}</div></div>' for n, t in STATS)
    return f"""<div class="c dark" style="width:{w}px;height:{h}px;padding:{(60 if not v else 84)*s}px {(84 if not v else 70)*s}px;gap:{(30 if not v else 40)*s}px">
<div class="lbl" style="font-size:{(20 if not v else 26)*s}px;color:#9fe870">One owner ran the test</div>
<div class="f" style="font-size:{(62 if not v else 80)*s}px;font-weight:900;letter-spacing:-.03em;line-height:1.02">3 AI agents. 1 real booking request. <em style="font-style:italic">Zero bookings.</em></div>
<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:{18*s}px;flex:1">{cards}</div>
<div style="font-size:{(20 if not v else 24)*s}px;line-height:1.4;color:#7a7670">Claude, ChatGPT and Perplexity asked to plan a 150-guest company party in Manhattan. Test by an events business owner, Oct 2026.</div>
{brand((18 if not v else 22)*s,'dark')}</div>"""

# ---------- 4. CHECKLIST ----------
CHECK = [("Run the agent test", "Ask 3 AIs to find, price and book you."),
         ("Write your prices and rules down", "If they live in your head, agents guess."),
         ("Put the facts in plain text", "Not in images, PDFs or Instagram stories."),
         ("Give agents one next step", "A booking link, a quote form, a WhatsApp link."),
         ("Choose where a human steps in", "Usually at the pay rung, for now.")]
def check(w, h):
    v = h > w
    s = w / 1600 if not v else w / 1080
    rows = "".join(f'<div style="display:flex;gap:{(24 if not v else 28)*s}px;align-items:flex-start;padding:{(26 if not v else 34)*s}px 0;border-top:{2*s}px solid rgba(13,12,10,.14)"><div style="flex:0 0 auto;width:{(50 if not v else 62)*s}px;height:{(50 if not v else 62)*s}px;border-radius:{10*s}px;background:#0d0c0a;color:#9fe870;display:flex;align-items:center;justify-content:center" class="f"><span style="font-size:{(28 if not v else 36)*s}px;font-weight:900">{i+1}</span></div><div><div class="f" style="font-size:{(34 if not v else 44)*s}px;font-weight:700;line-height:1.1;letter-spacing:-.01em">{a}</div><div style="font-size:{(22 if not v else 29)*s}px;color:#3d4a2a;margin-top:{6*s}px;line-height:1.3">{b}</div></div></div>' for i, (a, b) in enumerate(CHECK))
    head = f'<div class="lbl" style="font-size:{(20 if not v else 26)*s}px;color:#163300">Agent-ready in a week</div><div class="f" style="font-size:{(60 if not v else 78)*s}px;font-weight:900;letter-spacing:-.03em;line-height:1.02;margin:{14*s}px 0 {(20 if not v else 30)*s}px">5 moves for <em style="font-style:italic">small businesses</em></div>'
    if not v:
        inner = f'<div style="display:grid;grid-template-columns:.8fr 1.2fr;gap:{60*s}px;flex:1"><div style="display:flex;flex-direction:column">{head}<div style="font-size:{24*s}px;line-height:1.45;color:#3d4a2a">You don\'t have ad revenue to protect. Being easy for agents to read and book is pure upside.</div><div style="margin-top:auto">{brand(18*s,"lime")}</div></div><div>{rows}</div></div>'
    else:
        inner = f'{head}{rows}<div style="margin-top:auto">{brand(22*s,"lime")}</div>'
    return f'<div class="c lime" style="width:{w}px;height:{h}px;padding:{(60 if not v else 84)*s}px {(84 if not v else 70)*s}px">{inner}</div>'

# ---------- 5. CAROUSEL EXTRAS (vertical only) ----------
def camps(w, h):
    s = w / 1080
    data = [("Block", "Amazon, Delta, Yelp (paid access only)", "#1a1917", "#f8f6f1"),
            ("In the middle", "Zillow, Walmart", "#2a2925", "#f8f6f1"),
            ("Welcome", "Meta + Walmart + Stripe on an open standard, Shopify, Visa, Mastercard", "#9fe870", "#0d0c0a")]
    rows = "".join(f'<div style="background:{bg};color:{fg};border-radius:{18*s}px;padding:{42*s}px {38*s}px"><div class="f" style="font-size:{58*s}px;font-weight:900">{a}</div><div style="font-size:{33*s}px;line-height:1.35;margin-top:{10*s}px;opacity:.85">{b}</div></div>' for a, b, bg, fg in data)
    return f"""<div class="c dark" style="width:{w}px;height:{h}px;padding:{84*s}px {70*s}px;gap:{24*s}px">
<div class="lbl" style="font-size:{26*s}px;color:#9fe870">Big companies have picked sides</div>
<div class="f" style="font-size:{76*s}px;font-weight:900;letter-spacing:-.03em;line-height:1.02;margin-bottom:{10*s}px">Who lets AI agents <em style="font-style:italic">in?</em></div>
{rows}
<div style="font-size:{29*s}px;line-height:1.4;color:rgba(248,246,241,.75);margin-top:{8*s}px">Agents skip ads, banners and upsells. That's why the giants block them. You probably have nothing to lose.</div>
<div style="margin-top:auto">{brand(22*s,'dark')}</div></div>"""

def cta(w, h):
    s = w / 1080
    return f"""<div class="c dark" style="width:{w}px;height:{h}px;padding:{90*s}px {70*s}px;justify-content:center;gap:{40*s}px">
<div class="lbl" style="font-size:{26*s}px;color:#9fe870">Full guide + 2 copy-paste prompts</div>
<div class="f" style="font-size:{104*s}px;font-weight:900;letter-spacing:-.035em;line-height:1">Make your business <em style="font-style:italic">agent-ready.</em></div>
<div style="font-size:{36*s}px;line-height:1.4;color:rgba(248,246,241,.8)">Read it on aicoachalex.com/blog, or book a 49€ diagnostic and we'll run the test on your business together.</div>
<div style="align-self:flex-start;background:#9fe870;color:#0d0c0a;font-size:{38*s}px;font-weight:500;padding:{22*s}px {40*s}px;border-radius:999px">Link in bio →</div>
<div style="position:absolute;bottom:{70*s}px;left:{70*s}px">{brand(22*s,'dark')}</div></div>"""

JOBS = {
    "hero": (hero, [(1600, 900), (1080, 1350)]),
    "ladder": (ladder, [(1600, 900), (1080, 1350)]),
    "test": (score, [(1600, 900), (1080, 1350)]),
    "checklist": (check, [(1600, 900), (1080, 1350)]),
    "camps": (camps, [(1080, 1350)]),
    "cta": (cta, [(1080, 1350)]),
    "og": (hero, [(1200, 675)]),
}

def main(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    chrome = next(pathlib.Path("/opt/pw-browsers").glob("chromium-*/chrome-linux64/chrome"))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=str(chrome))
        for name, (fn, sizes) in JOBS.items():
            for w, h in sizes:
                pg = b.new_page(viewport={"width": w, "height": h})
                pg.set_content(f"<html><head><style>{FONTS}{CSS}</style></head><body>{fn(w, h)}</body></html>")
                pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(250)
                ov = pg.evaluate("[...document.querySelectorAll('.c *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>innerWidth+1||r.bottom>innerHeight+1}).length")
                suffix = "" if name == "og" else ("-v" if h > w else "-h")
                f = out / f"{name}{suffix}.png"
                pg.screenshot(path=str(f)); pg.close()
                print(f.name, w, h, "overflow" if ov else "ok")
        b.close()

if __name__ == "__main__":
    main(sys.argv[1])
