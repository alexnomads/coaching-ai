"""Isometric workshop illustrations for /who-i-work-with/.

Each building is an SVG <symbol> (viewBox 0 0 240 300) drawn from simple
boxes, so the pages stay light: no images, no libraries.
Anchor: plot centre (3.5, 3.5, 0) sits at (120, 236) in symbol space.
"""
import math

C, S, SC = math.cos(math.pi / 6), 0.5, 16
OX, OY = 120, 180

INK = "#0d0c0a"; CREAM = "#f8f6f1"; PAPER = "#ece6d8"; STONE = "#ddd5c3"
SAND = "#cdbf9f"; LIME = "#9fe870"; DEEP = "#163300"; MOSS = "#3d6b22"
SAGE = "#b7d39a"; GLASS = "#cfe6c0"; WARM = "#e8b04b"


def _mix(h, t, k):
    a = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(t[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * k):02x}" for x, y in zip(a, b))


def light(h, k=.16): return _mix(h, "#ffffff", k)
def dark(h, k=.16): return _mix(h, "#000000", k)


def P(x, y, z):
    return (OX + (x - y) * C * SC, OY + (x + y) * S * SC - z * SC)


def pts(a):
    return " ".join(f"{X:.1f},{Y:.1f}" for X, Y in (P(*p) for p in a))


def poly(a, fill, stroke=True, extra=""):
    st = ' class="k"' if stroke else ""
    return f'<polygon{st} points="{pts(a)}" fill="{fill}"{extra}/>'


def box(x, y, z, dx, dy, dz, col, top=None, right=None, stroke=True):
    x1, y1, z1 = x + dx, y + dy, z + dz
    return (poly([(x, y, z1), (x1, y, z1), (x1, y1, z1), (x, y1, z1)], top or light(col), stroke)
            + poly([(x, y1, z), (x1, y1, z), (x1, y1, z1), (x, y1, z1)], col, stroke)
            + poly([(x1, y, z), (x1, y1, z), (x1, y1, z1), (x1, y, z1)], right or dark(col), stroke))


def mY(x, y, z):  # draw on a face whose normal is +y (front-left), text runs along +x
    X, Y = P(x, y, z); return f"matrix({C:.4f},{S},0,1,{X:.1f},{Y:.1f})"


def mX(x, y, z):  # draw on a face whose normal is +x (front-right), text runs along -y
    X, Y = P(x, y, z); return f"matrix({C:.4f},{-S},0,1,{X:.1f},{Y:.1f})"


def onY(x, y, z, inner): return f'<g transform="{mY(x, y, z)}">{inner}</g>'
def onX(x, y, z, inner): return f'<g transform="{mX(x, y, z)}">{inner}</g>'


def winY(x0, y, z0, n, w=0.9, h=1.1, gap=0.5, col=INK, glow=None):
    out = ""
    for i in range(n):
        x = x0 + i * (w + gap)
        out += poly([(x, y, z0), (x + w, y, z0), (x + w, y, z0 + h), (x, y, z0 + h)], glow or col)
    return out


def winX(x, y0, z0, n, w=0.9, h=1.1, gap=0.5, col=INK, glow=None):
    out = ""
    for i in range(n):
        y = y0 + i * (w + gap)
        out += poly([(x, y, z0), (x, y + w, z0), (x, y + w, z0 + h), (x, y, z0 + h)], glow or col)
    return out


def gable(x0, y0, z, dx, dy, rh, col):
    x1, y1, ym = x0 + dx, y0 + dy, y0 + dy / 2
    return (poly([(x0, y1, z), (x1, y1, z), (x1, ym, z + rh), (x0, ym, z + rh)], col)
            + poly([(x1, y0, z), (x1, y1, z), (x1, ym, z + rh)], dark(col, .22)))


def sign_y(x, y, z, w, h, text, bg=INK, fg=LIME, size=9):
    """A flat sign on a +y face: w,h in units; text centred."""
    W, H = w * SC, h * SC
    return onY(x, y, z + h, f'<rect class="k" width="{W:.1f}" height="{H:.1f}" rx="2" fill="{bg}"/>'
               f'<text x="{W/2:.1f}" y="{H/2+size*0.36:.1f}" font-size="{size}" text-anchor="middle" fill="{fg}" class="sg">{text}</text>')


def sign_x(x, y, z, w, h, text, bg=INK, fg=LIME, size=9):
    W, H = w * SC, h * SC
    return onX(x, y, z + h, f'<rect class="k" width="{W:.1f}" height="{H:.1f}" rx="2" fill="{bg}"/>'
               f'<text x="{W/2:.1f}" y="{H/2+size*0.36:.1f}" font-size="{size}" text-anchor="middle" fill="{fg}" class="sg">{text}</text>')


def plot():
    sh = f'<polygon points="{pts([(0.2,0.6,0),(7.4,0.6,0),(7.4,7.8,0),(0.2,7.8,0)])}" fill="{DEEP}" opacity=".12"/>'
    return sh + box(0.2, 0.2, 0, 6.8, 6.8, 0.35, PAPER, top=light(PAPER, .35), right=dark(PAPER, .12))


def tree(x, y, z=0.35, r=0.75, col=MOSS):
    bx, by = P(x, y, z)
    return (box(x - .12, y - .12, z, .24, .24, .8, "#6b4f2e")
            + f'<circle class="k" cx="{bx:.1f}" cy="{by - 1.6*SC:.1f}" r="{r*SC:.1f}" fill="{col}"/>'
            + f'<circle cx="{bx - r*SC*.35:.1f}" cy="{by - 1.6*SC - r*SC*.35:.1f}" r="{r*SC*.32:.1f}" fill="{light(col,.35)}"/>')


def lamp(x, y, z=0.35, banner=True):
    out = box(x - .07, y - .07, z, .14, .14, 3.2, INK)
    bx, by = P(x, y, z + 3.3)
    out += f'<circle class="k" cx="{bx:.1f}" cy="{by:.1f}" r="3.2" fill="{WARM}"/>'
    if banner:
        out += onY(x + .1, y, z + 2.9, f'<rect class="k" width="13" height="18" fill="{LIME}"/>'
                   f'<rect x="3" y="4" width="1.6" height="10" fill="{INK}"/><text x="8.6" y="9" font-size="4.3" text-anchor="middle" fill="#0d0c0a" class="sg">AI</text><text x="8.6" y="14" font-size="3.6" text-anchor="middle" fill="#0d0c0a" class="sg">CA</text>')
    return out


def icon(name):
    """Small icons drawn in a 20x20 local box (used inside face groups)."""
    return {
        "bolt": f'<path d="M11 1 L4 11 h5 l-2 8 l8-11 h-5 z" fill="{LIME}"/>',
        "tooth": f'<path d="M4 4 q6-5 12 0 q1 5-2 9 l-1 6 q-2 1-2-4 q-1-3-2 0 q0 5-2 4 l-1-6 q-3-4-2-9z" fill="{CREAM}" class="k"/>',
        "house": f'<path d="M3 10 L10 3 L17 10 V18 H3 Z" fill="{LIME}"/><rect x="8" y="12" width="4" height="6" fill="{INK}"/>',
        "chart": f'<path d="M3 17 V3 M3 17 H18" stroke="{LIME}" stroke-width="2" fill="none"/><path d="M5 14 L9 10 L12 12 L17 5" stroke="{LIME}" stroke-width="2.2" fill="none"/>',
        "play": f'<circle cx="10" cy="10" r="8" fill="{LIME}"/><path d="M8 6 L14 10 L8 14 Z" fill="{INK}"/>',
        "ledger": f'<rect x="4" y="3" width="12" height="14" fill="{CREAM}" class="k"/><path d="M6 7 h8 M6 10 h8 M6 13 h5" stroke="{INK}" stroke-width="1.3"/>',
        "glass": f'<path d="M5 3 H15 L10 10 Z" fill="{LIME}"/><path d="M10 10 V16 M6.5 17 H13.5" stroke="{LIME}" stroke-width="1.8"/>',
        "hat": f'<path d="M3 13 Q3 5 10 5 Q17 5 17 13 Z" fill="{WARM}" class="k"/><rect x="1.5" y="12.5" width="17" height="3" fill="{WARM}" class="k"/>',
        "spark": f'<path d="M10 1 L12 8 L19 10 L12 12 L10 19 L8 12 L1 10 L8 8 Z" fill="{LIME}"/>',
        "laptop": f'<rect x="4" y="4" width="12" height="8" fill="{LIME}" class="k"/><path d="M2 14 H18 L16 16 H4 Z" fill="{CREAM}" class="k"/>',
        "clock": f'<circle cx="10" cy="10" r="8" fill="{CREAM}" class="k"/><path d="M10 5 V10 L13 12" stroke="{INK}" stroke-width="1.6" fill="none"/>',
        "speaker": f'<rect x="5" y="2" width="10" height="16" rx="1" fill="{INK}" class="k"/><circle cx="10" cy="7" r="2" fill="{LIME}"/><circle cx="10" cy="13" r="3" fill="{LIME}"/>',
    }[name]


def icon_y(x, y, z, name, scale=1.0):
    return onY(x, y, z, f'<g transform="scale({scale})">{icon(name)}</g>')


def icon_x(x, y, z, name, scale=1.0):
    return onX(x, y, z, f'<g transform="scale({scale})">{icon(name)}</g>')


# ---------------- buildings ----------------

def b_stage():
    o = plot()
    o += box(1, 1.4, .35, 5, 4.2, 3.4, DEEP)
    o += poly([(2, 5.6, .35), (4.6, 5.6, .35), (4.6, 5.6, 2.6), (2, 5.6, 2.6)], INK)
    for i in range(6):
        z = .6 + i * .35
        o += poly([(2.1, 5.6, z), (4.5, 5.6, z), (4.5, 5.6, z + .12), (2.1, 5.6, z + .12)], dark(STONE, .5), stroke=False)
    o += winX(6, 2, 1.6, 2, w=1.1, h=1, gap=.6, glow=WARM)
    # roof truss
    o += box(1.2, 1.6, 3.75, .2, .2, 1.8, LIME) + box(5.6, 1.6, 3.75, .2, .2, 1.8, LIME)
    o += box(1.2, 5.0, 3.75, .2, .2, 1.8, LIME) + box(5.6, 5.0, 3.75, .2, .2, 1.8, LIME)
    o += box(1.2, 5.0, 5.55, 4.6, .2, .2, LIME) + box(5.6, 1.6, 5.55, .2, 3.6, .2, LIME)
    o += sign_y(1.3, 5.6, 2.75, 1.9, .8, "LIVE", size=8)
    o += box(5.4, 5.9, .35, .9, .7, 1.8, INK) + icon_y(5.45, 6.6, 2.0, "speaker", .7)
    o += tree(.9, 6.3)
    return o


def b_trades():
    o = plot()
    o += box(1, 1, .35, 4.6, 4.2, 3.2, SAND)
    o += box(.9, .9, 3.55, 4.8, 4.4, .35, DEEP)
    o += poly([(1.6, 5.2, .35), (2.8, 5.2, .35), (2.8, 5.2, 2.3), (1.6, 5.2, 2.3)], INK)
    o += winY(3.3, 5.2, 1.0, 1, w=1.8, h=1.3, glow=GLASS)
    o += sign_y(1.4, 5.3, 2.55, 3.6, .85, "ELECTRICAL", size=7.5)
    o += icon_x(5.6, 5.0, 3.0, "bolt", 1.0)
    o += winX(5.6, 1.6, 1.0, 1, w=1.6, h=1.2, glow=GLASS)
    # van
    o += box(5.95, 1.4, .35, 1.0, 3.2, 1.25, CREAM) + box(5.95, 4.6, .35, 1.0, .9, .9, CREAM)
    o += poly([(6.95, 1.6, .9), (6.95, 4.4, .9), (6.95, 4.4, 1.05), (6.95, 1.6, 1.05)], LIME)
    o += winX(6.95, 4.65, .95, 1, w=.8, h=.5, glow=GLASS)
    return o


def b_facade():
    o = plot()
    o += box(1.2, 1.2, .35, 4.2, 4.2, 5.4, STONE)
    for r in range(4):
        for c in range(3):
            x = 1.45 + c * 1.35; z = .7 + r * 1.25
            col = (LIME if (r + c) % 2 == 0 else MOSS) if r < 3 else STONE
            o += poly([(x, 5.4, z), (x + 1.15, 5.4, z), (x + 1.15, 5.4, z + 1.05), (x, 5.4, z + 1.05)], col)
    # scaffolding on +x face
    for i in range(4):
        y = 1.4 + i * 1.3
        o += box(5.75, y, .35, .1, .1, 5.6, INK, stroke=False)
    for k in range(4):
        o += box(5.75, 1.4, .35 + 1.4 * (k + 1), .1, 4.0, .1, WARM, stroke=False)
    o += icon_x(5.4, 4.9, 6.6, "hat", .9)
    o += box(1.2, 5.9, .35, 1.4, .8, .6, INK) + box(1.3, 6.0, .95, 1.2, .6, .25, LIME)
    return o


def b_bar():
    o = plot()
    o += box(1, 1.2, .35, 5, 4.2, 3.3, DEEP)
    o += box(.95, 1.15, 3.65, 5.1, 4.3, .3, INK)
    o += winY(1.4, 5.4, .9, 2, w=1.5, h=1.5, gap=.5, glow=WARM)
    o += poly([(4.9, 5.4, .35), (5.8, 5.4, .35), (5.8, 5.4, 2.3), (4.9, 5.4, 2.3)], INK)
    # striped awning
    for i in range(5):
        x = 1.2 + i * .92; col = LIME if i % 2 == 0 else CREAM
        o += poly([(x, 5.4, 2.85), (x + .92, 5.4, 2.85), (x + .92, 6.2, 2.4), (x, 6.2, 2.4)], col)
    o += icon_y(4.95, 5.4, 3.45, "glass", .6)
    # screen with chart on +x face (the software)
    o += onX(6, 4.9, 3.0, f'<rect class="k" width="44" height="30" rx="2" fill="{INK}"/><g transform="translate(12,5)">{icon("chart")}</g>')
    o += box(1.6, 6.1, .35, .5, .5, .7, SAND) + box(3.0, 6.1, .35, .5, .5, .7, SAND)
    return o


def b_tower():
    o = plot()
    o += box(1.7, 1.7, .35, 3.6, 3.6, 9.2, INK, top=MOSS, right="#1e1d1a")
    for r in range(8):
        z = 1.0 + r * 1.05
        o += poly([(2.0, 5.3, z), (5.0, 5.3, z), (5.0, 5.3, z + .45), (2.0, 5.3, z + .45)], GLASS if r % 3 else LIME, stroke=False)
        o += poly([(5.3, 2.0, z), (5.3, 5.0, z), (5.3, 5.0, z + .45), (5.3, 2.0, z + .45)], dark(GLASS, .25), stroke=False)
    o += box(2.4, 2.4, 9.55, 2.2, 2.2, .7, LIME)
    o += box(3.45, 3.45, 10.25, .1, .1, 1.6, INK)
    fx, fy = P(3.5, 3.5, 11.8)
    o += f'<path class="k" d="M{fx:.1f},{fy:.1f} l14,4 l-14,4 z" fill="{LIME}"/>'
    o += sign_y(2.2, 5.3, .5, 2.6, .55, "HQ", size=7)
    o += tree(6.1, 6.0) + tree(.9, 6.2, r=.6)
    return o


def b_crane():
    o = plot()
    o += box(1, 3.2, .35, 3.4, 2.8, 2.2, SAND)
    o += winY(1.4, 6.0, 1.0, 2, w=.9, h=.8, gap=.6, glow=GLASS)
    o += sign_y(1.3, 6.0, 1.95, 2.8, .5, "PERMITS", size=6.5)
    o += box(5.2, 1.2, .35, .35, .35, 8.6, WARM)
    o += box(1.2, 1.15, 8.95, 5.6, .45, .35, LIME)
    o += box(5.5, 1.05, 8.6, 1.3, .65, .5, INK)
    hx, hy = P(2.2, 1.35, 8.95); hx2, hy2 = P(2.2, 1.35, 5.6)
    o += f'<line class="k" x1="{hx:.1f}" y1="{hy:.1f}" x2="{hx2:.1f}" y2="{hy2:.1f}"/>'
    o += box(1.95, 1.1, 4.9, .5, .5, .7, MOSS)
    for i in range(4):
        x = 4.6 + i * .55
        o += poly([(x, 6.6, .35), (x + .3, 6.6, .35), (x + .3, 6.6, .9), (x, 6.6, .9)], INK if i % 2 else WARM)
    return o


def b_clinic():
    o = plot()
    o += box(1, 1.2, .35, 5, 4.4, 3.6, CREAM, top=STONE)
    o += box(.95, 1.15, 3.95, 5.1, 4.5, .3, MOSS)
    o += winY(1.4, 5.6, 1.2, 2, w=1.2, h=1.3, gap=.5, glow=GLASS)
    o += poly([(4.6, 5.6, .35), (5.6, 5.6, .35), (5.6, 5.6, 2.4), (4.6, 5.6, 2.4)], DEEP)
    o += poly([(4.4, 5.6, 2.55), (5.8, 5.6, 2.55), (5.8, 6.4, 2.25), (4.4, 6.4, 2.25)], LIME)
    o += onY(1.6, 5.6, 3.6, f'<rect class="k" width="30" height="16" rx="3" fill="{DEEP}"/><g transform="translate(9,1) scale(.7)">{icon("tooth")}</g>')
    o += winX(6, 1.8, 1.2, 2, w=1.2, h=1.3, gap=.6, glow=GLASS)
    o += tree(6.4, 6.3, r=.6, col=MOSS)
    return o


def b_bank():
    o = plot()
    o += box(1.1, 1.3, .35, 4.8, 3.6, 3.4, STONE)
    o += box(.8, 4.9, .35, 5.4, .9, .3, light(STONE)) + box(.95, 5.0, .65, 5.1, .6, .25, light(STONE))
    for i in range(5):
        x = 1.35 + i * 1.08
        o += box(x, 4.95, .9, .35, .3, 2.85, CREAM, stroke=True)
    o += box(1.0, 1.2, 3.75, 5.0, 4.1, .35, SAND)
    x0, x1 = 1.0, 6.0
    o += poly([(x0, 5.3, 4.1), (x1, 5.3, 4.1), ((x0 + x1) / 2, 5.3, 5.4)], DEEP)
    o += icon_y(3.05, 5.3, 4.95, "ledger", .55)
    o += sign_x(5.9, 4.6, 2.3, 2.6, .55, "AUDIT", size=6.5)
    return o


def b_studio():
    o = plot()
    o += box(1, 1.3, .35, 5, 4.2, 3.4, CREAM, top=STONE)
    o += poly([(1.4, 5.5, .8), (4.6, 5.5, .8), (4.6, 5.5, 3.1), (1.4, 5.5, 3.1)], INK)
    o += poly([(1.6, 5.5, 1.0), (4.4, 5.5, 1.0), (4.4, 5.5, 2.9), (1.6, 5.5, 2.9)], MOSS)
    o += icon_y(2.5, 5.5, 2.6, "play", .9)
    o += box(.95, 1.25, 3.75, 5.1, 4.3, .3, INK)
    # rooftop camera on tripod
    o += box(3.0, 2.8, 4.05, .15, .15, 1.2, INK) + box(2.5, 2.5, 5.25, 1.3, .9, .8, LIME) + box(3.8, 2.75, 5.45, .5, .4, .4, INK)
    o += sign_x(6, 4.9, 2.1, 3, .6, "STUDIO", size=7)
    return o


def b_cottage():
    o = plot()
    o += box(1.5, 1.6, .35, 4, 3.6, 2.6, SAGE)
    o += gable(1.3, 1.4, 2.95, 4.4, 4.0, 1.7, DEEP)
    o += winY(1.9, 5.2, 1.0, 1, w=1.3, h=1.1, glow=WARM)
    o += icon_y(1.95, 5.2, 2.0, "laptop", .55)
    o += poly([(3.9, 5.2, .35), (4.8, 5.2, .35), (4.8, 5.2, 2.0), (3.9, 5.2, 2.0)], INK)
    o += winX(5.5, 2.2, 1.0, 1, w=1.2, h=1.0, glow=WARM)
    o += box(5.6, 6.0, .35, .1, .1, 1.1, INK) + box(5.4, 5.9, 1.45, .5, .35, .35, LIME)
    o += tree(1.0, 6.3, r=.65)
    return o


def b_kiosk():
    o = plot()
    o += box(1.6, 1.6, .35, 3.6, 3.6, 4.2, SAND)
    o += box(1.5, 1.5, 4.55, 3.8, 3.8, .3, INK)
    o += onY(1.9, 5.2, 4.25, f'<rect class="k" width="46" height="26" rx="2" fill="{INK}"/><g transform="translate(13,3)">{icon("chart")}</g>')
    o += winY(1.9, 5.2, .9, 1, w=2.2, h=1.6, glow=GLASS)
    for i in range(4):
        x = 1.7 + i * .85; col = LIME if i % 2 == 0 else INK
        o += poly([(x, 5.2, 2.9), (x + .85, 5.2, 2.9), (x + .85, 6.0, 2.5), (x, 6.0, 2.5)], col)
    o += poly([(4.4, 5.2, .35), (5.0, 5.2, .35), (5.0, 5.2, 2.1), (4.4, 5.2, 2.1)], INK)
    o += sign_x(5.2, 4.8, 2.6, 2.6, .55, "SALES", size=7)
    o += lamp(6.2, 6.2, banner=True)
    return o


def b_agency():
    o = plot()
    o += box(1.2, 1.4, .35, 4.6, 3.8, 3.0, CREAM, top=STONE)
    o += gable(1.0, 1.2, 3.35, 5.0, 4.2, 1.6, MOSS)
    for i in range(3):
        x = 1.5 + i * 1.3
        o += onY(x, 5.2, 2.2, f'<rect class="k" width="17" height="19" fill="{GLASS}"/><g transform="translate(2,2) scale(.65)">{icon("house")}</g>')
    o += poly([(1.5, 5.2, .35), (2.4, 5.2, .35), (2.4, 5.2, 1.6), (1.5, 5.2, 1.6)], INK)
    o += box(6.3, 5.9, .35, .12, .12, 2.0, INK)
    o += onY(5.6, 6.02, 2.3, f'<rect class="k" width="22" height="13" fill="{LIME}"/><text x="11" y="9" font-size="5.4" text-anchor="middle" fill="#0d0c0a" class="sg">SOLD</text>')
    o += tree(.9, 6.3, r=.6)
    return o


def b_station():
    o = plot()
    o += box(.8, 1.8, .35, 5.8, 3.0, 2.6, SAND)
    o += gable(.6, 1.6, 2.95, 6.2, 3.4, 1.2, DEEP)
    o += winY(1.2, 4.8, .9, 3, w=.9, h=1.1, gap=.65, glow=WARM)
    o += poly([(5.0, 4.8, .35), (6.0, 4.8, .35), (6.0, 4.8, 2.0), (5.0, 4.8, 2.0)], INK)
    o += icon_y(3.2, 4.8, 4.2, "clock", .75)
    o += sign_y(1.0, 4.8, 2.15, 2.4, .5, "STATION", size=6.5)
    for y in (5.7, 6.4):
        o += box(.4, y, .35, 6.6, .12, .08, INK, stroke=False)
    for i in range(7):
        o += box(.6 + i * .95, 5.6, .3, .2, 1.0, .06, "#6b4f2e", stroke=False)
    return o


def b_hq(logo_href):
    o = plot()
    o += box(1, 1, .35, 5, 5, 4.6, INK, top="#2a2925", right="#1a1917")
    # logo on the front face
    o += onY(1.35, 6, 3.95, f'<rect width="46" height="46" rx="3" fill="{INK}" stroke="{LIME}" stroke-width="1.5"/>'
            f'<image href="{logo_href}" x="1.5" y="1.5" width="43" height="43"/>')
    o += poly([(4.5, 6, .35), (5.6, 6, .35), (5.6, 6, 2.4), (4.5, 6, 2.4)], LIME)
    o += winX(6, 1.6, 1.4, 2, w=1.4, h=1.4, gap=.8, glow=LIME)
    o += box(.95, .95, 4.95, 5.1, 5.1, .25, LIME)
    o += onY(4.45, 6, 3.2, f'<rect width="19" height="8" rx="1.5" fill="{CREAM}"/><text x="9.5" y="5.8" font-size="4.4" text-anchor="middle" fill="{INK}" class="sg">OPEN</text>')
    o += lamp(.7, 6.6) + tree(6.6, 6.5, r=.6)
    return o


def pyramid(x0, y0, z, dx, dy, h, col):
    x1, y1 = x0 + dx, y0 + dy
    ap = (x0 + dx / 2, y0 + dy / 2, z + h)
    return poly([(x0, y1, z), (x1, y1, z), ap], col) + poly([(x1, y0, z), (x1, y1, z), ap], dark(col, .22))


def b_lab():
    o = plot()
    o += box(1.2, 1.4, .35, 4.6, 4.0, 3.2, CREAM, top=STONE)
    o += box(1.1, 1.3, 3.55, 4.8, 4.2, .3, DEEP)
    o += winY(1.6, 5.4, 1.1, 2, w=1.3, h=1.2, gap=.6, glow=GLASS)
    o += poly([(4.7, 5.4, .35), (5.5, 5.4, .35), (5.5, 5.4, 2.1), (4.7, 5.4, 2.1)], INK)
    o += onY(4.0, 5.4, 3.2, f'<rect class="k" width="26" height="12" rx="2" fill="{INK}"/><text x="13" y="8.6" font-size="7" text-anchor="middle" fill="{LIME}" class="sg">LAB</text>')
    # flask on the roof
    o += box(3.0, 2.9, 3.85, .5, .5, 1.0, GLASS)
    bx, by = P(3.25, 3.15, 4.85)
    o += f'<circle class="k" cx="{bx:.1f}" cy="{by+8:.1f}" r="13" fill="{LIME}"/><circle cx="{bx-4:.1f}" cy="{by+4:.1f}" r="3" fill="#ffffff" opacity=".7"/>'
    o += winX(5.8, 2.0, 1.1, 2, w=1.1, h=1.2, gap=.6, glow=GLASS)
    o += tree(6.4, 6.3, r=.6)
    return o


def b_market():
    o = plot()
    o += box(1.3, 2.4, .35, 4.6, 2.4, 1.3, SAND)
    o += box(1.2, 2.3, 1.65, 4.8, 2.6, .15, light(SAND, .3))
    for x in (1.4, 5.6):
        o += box(x, 4.5, .35, .15, .15, 3.0, INK)
        o += box(x, 2.5, 1.8, .15, .15, 1.55, INK)
    for i in range(6):
        x = 1.2 + i * .82; col = LIME if i % 2 == 0 else CREAM
        o += poly([(x, 2.2, 3.4), (x + .82, 2.2, 3.4), (x + .82, 5.1, 3.0), (x, 5.1, 3.0)], col)
    o += box(1.6, 2.6, 1.8, .9, .7, .6, WARM) + box(2.8, 2.6, 1.8, .9, .7, .6, MOSS) + box(4.0, 2.6, 1.8, .9, .7, .6, "#e88b8b")
    o += onY(2.2, 4.8, 1.25, f'<rect class="k" width="44" height="11" rx="2" fill="{INK}"/><text x="22" y="8" font-size="6.4" text-anchor="middle" fill="{LIME}" class="sg">MARKET</text>')
    o += box(5.6, 5.6, .35, .7, .7, .55, SAND) + box(5.7, 5.7, .9, .5, .5, .4, LIME)
    return o


def b_court():
    o = b_bank()
    o = o.replace(">AUDIT<", ">COURT<")
    return o


def b_clocktower():
    o = plot()
    o += box(2.3, 2.3, .35, 2.6, 2.6, 6.8, STONE)
    for z in (1.4, 3.2):
        o += winY(2.8, 4.9, z, 1, w=.8, h=1.1, glow=GLASS) + winX(4.9, 2.8, z, 1, w=.8, h=1.1, glow=GLASS)
    o += icon_y(2.95, 4.9, 6.75, "clock", 1.15) + icon_x(4.9, 4.1, 6.75, "clock", 1.15)
    o += box(2.15, 2.15, 7.15, 2.9, 2.9, .3, DEEP)
    o += pyramid(2.15, 2.15, 7.45, 2.9, 2.9, 2.2, DEEP)
    o += poly([(2.8, 4.9, .35), (3.6, 4.9, .35), (3.6, 4.9, 1.0), (2.8, 4.9, 1.0)], INK)
    o += tree(1.0, 6.2, r=.6) + tree(6.2, 1.3, r=.55)
    return o


def b_lighthouse():
    o = plot()
    o += box(1.0, 4.4, .35, 2.4, 2.2, 1.6, CREAM, top=STONE) + gable(.9, 4.3, 1.95, 2.6, 2.4, .9, MOSS)
    segs = [(2.7, 2.3, 2.0, 1.6, CREAM), (2.85, 2.45, 1.7, 1.6, INK), (3.0, 2.6, 1.4, 1.6, CREAM), (3.1, 2.7, 1.2, 1.5, INK)]
    z = .35
    for x, y, w, h, c in segs:
        o += box(x, y, .35 if False else z, w, w, h, c) if False else box(x, y, z, w, w, h, c)
        z += h
    o += box(3.0, 2.6, z, 1.4, 1.4, .15, INK)
    o += box(3.15, 2.75, z + .15, 1.1, 1.1, 1.0, LIME, top=light(LIME, .4))
    o += pyramid(3.0, 2.6, z + 1.15, 1.4, 1.4, .9, INK)
    o += f'<g class="beam"><polygon points="{pts([(3.7, 3.3, z + .65), (8.5, 1.0, z + 1.2), (8.5, 2.6, z + .2)])}" fill="{WARM}" opacity=".35"/></g>'
    return o


BUILDERS = {
    "stage": b_stage, "trades": b_trades, "facade": b_facade, "bar": b_bar, "tower": b_tower,
    "crane": b_crane, "clinic": b_clinic, "bank": b_bank, "studio": b_studio, "cottage": b_cottage,
    "kiosk": b_kiosk, "agency": b_agency, "station": b_station,
    "lab": b_lab, "market": b_market, "court": b_court, "clocktower": b_clocktower, "lighthouse": b_lighthouse,
}


def symbol(kind, logo_href="/assets/aicoachalex-mark-160.webp"):
    body = b_hq(logo_href) if kind == "hq" else BUILDERS[kind]()
    return f'<symbol id="b-{kind}" viewBox="0 0 240 300">{body}</symbol>'


ANCHOR = (120, 236)  # plot centre in symbol space
