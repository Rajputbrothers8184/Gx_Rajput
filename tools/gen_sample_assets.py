#!/usr/bin/env python3
"""Builds the hand-crafted SVG sample designs used in the Gx_Rajput portfolio.

Run from the repo root:   python3 tools/gen_sample_assets.py
Everything is written to assets/svg/. These are *sample* pieces used to fill the
portfolio grid - swap any of them for real client work by dropping a file with
the same name (or editing the card in index.html).
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "svg")
os.makedirs(OUT, exist_ok=True)

BG = "#080c14"
PANEL = "#0d131f"
BLUE = "#2f7bff"
BLUE_D = "#10306e"
ORANGE = "#ff8a1f"
ORANGE_D = "#ff5f0f"
WHITE = "#f3f7ff"
MUTED = "#8ea2c0"
FONT = "Arial, Helvetica, sans-serif"


def grad(gid, a, b, angle=45):
    x2, y2 = (1, 1) if angle == 45 else (1, 0)
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
        f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'
    )


def radial(gid, color, opacity=0.55):
    return (
        f'<radialGradient id="{gid}" cx="50%" cy="45%" r="60%">'
        f'<stop offset="0" stop-color="{color}" stop-opacity="{opacity}"/>'
        f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>'
    )


def svg(w, h, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" font-family="{FONT}">\n<defs>\n{defs}\n</defs>\n{body}\n</svg>\n'
    )


def base(w, h, accent=BLUE, glow=True):
    """Dark panel + grid + optional corner glow."""
    d = grad("bg", PANEL, "#070a11", 45)
    d += f'<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">' \
         f'<path d="M28 0H0V28" fill="none" stroke="#ffffff" stroke-opacity="0.035" stroke-width="1"/></pattern>'
    if glow:
        d += radial("glow", accent, 0.30)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += f'<rect width="{w}" height="{h}" fill="url(#grid)"/>'
    if glow:
        b += f'<rect width="{w}" height="{h}" fill="url(#glow)"/>'
    return d, b


def label(x, y, text, size=15, color=MUTED, ls=4, anchor="middle", weight="bold"):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" '
        f'letter-spacing="{ls}" text-anchor="{anchor}">{text}</text>'
    )


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)


# --------------------------------------------------------------------------
# 1. LOGO DESIGN  (400 x 300)
# --------------------------------------------------------------------------
def logo(name, mark, brand, tag, defs_extra=""):
    d, b = base(400, 300, BLUE)
    d += grad("mg", BLUE, ORANGE) + defs_extra
    b += f'<g>{mark}</g>'
    b += label(200, 232, brand, 21, WHITE, 6)
    b += label(200, 254, tag, 10, MUTED, 5)
    return svg(400, 300, b, d)


LOGOS = [
    ("logo-01.svg",
     '<rect x="142" y="52" width="116" height="116" rx="30" fill="url(#mg)"/>'
     '<rect x="154" y="64" width="92" height="92" rx="22" fill="none" stroke="#ffffff" '
     'stroke-opacity="0.35" stroke-width="2"/>'
     '<text x="200" y="142" font-size="62" font-weight="bold" fill="#ffffff" '
     'text-anchor="middle">N</text>'
     '<circle cx="200" cy="110" r="86" fill="none" stroke="url(#mg)" stroke-opacity="0.45" '
     'stroke-width="2" stroke-dasharray="4 8"/>',
     "NOOR STUDIO", "CREATIVE • BRANDING"),
    ("logo-02.svg",
     '<path d="M200 48 L252 70 L252 128 Q252 176 200 202 Q148 176 148 128 L148 70 Z" fill="url(#mg)"/>'
     '<path d="M200 62 L240 79 L240 127 Q240 165 200 187 Q160 165 160 127 L160 79 Z" fill="#0a0e18"/>'
     '<text x="200" y="132" font-size="46" font-weight="bold" fill="#ffffff" '
     'text-anchor="middle">GX</text>'
     '<circle cx="200" cy="30" r="7" fill="' + ORANGE + '"/>'
     '<circle cx="176" cy="38" r="5" fill="' + ORANGE + '" fill-opacity="0.7"/>'
     '<circle cx="224" cy="38" r="5" fill="' + ORANGE + '" fill-opacity="0.7"/>'
     '<rect x="168" y="150" width="64" height="4" rx="2" fill="' + ORANGE + '"/>',
     "GX RAJPUT", "DESIGN • CODE • FILM"),
    ("logo-03.svg",
     '<circle cx="200" cy="110" r="72" fill="none" stroke="url(#mg)" stroke-width="12"/>'
     '<path d="M208 56 L166 118 H196 L184 164 L236 100 H204 Z" fill="url(#mg)"/>'
     '<circle cx="200" cy="110" r="86" fill="none" stroke="#ffffff" stroke-opacity="0.12" '
     'stroke-width="1"/>',
     "BOLTFIT", "STRENGTH ACADEMY"),
    ("logo-04.svg",
     '<circle cx="200" cy="110" r="74" fill="none" stroke="url(#mg)" stroke-width="10"/>'
     '<path d="M200 66 C214 90 226 98 226 118 A26 26 0 1 1 174 118 C174 98 188 88 200 66 Z" '
     'fill="url(#mg)"/>'
     '<path d="M170 152 Q200 176 230 152" fill="none" stroke="' + ORANGE + '" stroke-width="7" '
     'stroke-linecap="round"/>'
     '<circle cx="200" cy="110" r="88" fill="none" stroke="' + ORANGE + '" stroke-opacity="0.35" '
     'stroke-width="2" stroke-dasharray="2 9"/>',
     "SPICE ROUTE", "FINE DESI CUISINE"),
    ("logo-05.svg",
     '<path d="M158 148 L200 74 L242 148" fill="none" stroke="url(#mg)" stroke-width="8" '
     'stroke-linecap="round"/>'
     '<path d="M158 148 H242" stroke="url(#mg)" stroke-width="8" stroke-linecap="round"/>'
     '<circle cx="200" cy="74" r="17" fill="' + ORANGE + '"/>'
     '<circle cx="158" cy="148" r="13" fill="' + BLUE + '"/>'
     '<circle cx="242" cy="148" r="13" fill="' + BLUE + '"/>'
     '<circle cx="200" cy="110" r="96" fill="none" stroke="#ffffff" stroke-opacity="0.08" '
     'stroke-width="1"/>',
     "NEXUS TECH", "SOFTWARE • NETWORKS"),
    ("logo-06.svg",
     '<circle cx="200" cy="110" r="76" fill="none" stroke="url(#mg)" stroke-width="9"/>'
     '<path d="M156 76 L244 144 M244 76 L156 144" stroke="#ffffff" stroke-width="7" '
     'stroke-linecap="round"/>'
     '<circle cx="150" cy="152" r="13" fill="none" stroke="' + ORANGE + '" stroke-width="6"/>'
     '<circle cx="250" cy="152" r="13" fill="none" stroke="' + ORANGE + '" stroke-width="6"/>'
     '<path d="M178 172 Q200 158 222 172 Q200 190 178 172 Z" fill="' + ORANGE + '"/>',
     "KING BARBER", "GENTS SALON • SINCE 2016"),
]

for fname, mark, brand, tag in LOGOS:
    write(fname, logo(fname, mark, brand, tag))


# --------------------------------------------------------------------------
# 2. BUSINESS CARDS  (440 x 260)
# --------------------------------------------------------------------------
def card(name, body, defs_extra=""):
    d, b = base(440, 260, BLUE)
    d += grad("mg", BLUE, ORANGE) + grad("mg2", ORANGE, BLUE_D) + defs_extra
    b += '<rect x="32" y="34" width="376" height="204" rx="16" fill="#05070c" fill-opacity="0.55"/>'
    b += body
    return svg(440, 260, b, d)


def c_icon(cx, cy, kind):
    if kind == "phone":
        return (f'<path d="M{cx-5} {cy-6}h4l3 6-3 2a20 20 0 0 0 9 9l2-3 6 3v4a3 3 0 0 1-3 3'
                f'A26 26 0 0 1 {cx-21} {cy+8}a3 3 0 0 1 3-3z" fill="{ORANGE}"/>')
    if kind == "mail":
        return (f'<rect x="{cx-9}" y="{cy-7}" width="18" height="14" rx="2" fill="none" '
                f'stroke="{ORANGE}" stroke-width="2"/><path d="M{cx-9} {cy-7}l9 7 9-7" fill="none" '
                f'stroke="{ORANGE}" stroke-width="2"/>')
    if kind == "pin":
        return (f'<path d="M{cx} {cy+8}c-6-6-9-10-9-14a9 9 0 0 1 18 0c0 4-3 8-9 14z" '
                f'fill="{ORANGE}"/><circle cx="{cx}" cy="{cy-6}" r="3" fill="{PANEL}"/>')
    return (f'<circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="{ORANGE}" stroke-width="2"/>'
            f'<path d="M{cx} {cy-4}v8M{cx-4} {cy}h8" stroke="{ORANGE}" stroke-width="2"/>')


def c_line(x, y, kind, text, color=WHITE, size=11):
    return (f'<g>{c_icon(x + 9, y - 4, kind)}'
            f'<text x="{x + 26}" y="{y}" font-size="{size}" fill="{color}">{text}</text></g>')


CARDS = [
    ("card-01.svg",
     '<rect x="32" y="34" width="10" height="204" rx="5" fill="url(#mg)"/>'
     '<text x="66" y="80" font-size="26" font-weight="bold" fill="#ffffff">ZAHID</text>'
     '<text x="66" y="106" font-size="26" font-weight="bold" fill="' + ORANGE + '">ELECTRONICS</text>'
     '<text x="66" y="126" font-size="10" fill="' + MUTED + '" letter-spacing="3">MOBILES • REPAIR • ACCESSORIES</text>'
     '<line x1="66" y1="142" x2="380" y2="142" stroke="#ffffff" stroke-opacity="0.12"/>'
     + c_line(66, 168, "phone", "0300-1234567")
     + c_line(66, 192, "mail", "info@zahidelectronics.pk")
     + c_line(66, 216, "pin", "Main Bazar, Layyah")),
    ("card-02.svg",
     '<rect x="32" y="34" width="376" height="204" rx="16" fill="url(#mg2)" fill-opacity="0.22"/>'
     '<path d="M32 200 L120 118 L408 34 L408 238 Z" fill="url(#mg)" fill-opacity="0.35"/>'
     '<circle cx="200" cy="96" r="34" fill="none" stroke="#ffffff" stroke-width="3"/>'
     '<path d="M182 108 L218 72 M182 84 h26 v26" stroke="#ffffff" stroke-width="3" fill="none"/>'
     '<text x="200" y="164" font-size="22" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'AL-MADINA TRAVELS</text>'
     '<text x="200" y="184" font-size="10" fill="' + WHITE + '" fill-opacity="0.75" '
     'letter-spacing="3" text-anchor="middle">VISA • TICKETING • TOURS</text>'
     '<text x="200" y="216" font-size="11" fill="' + WHITE + '" text-anchor="middle">'
     '0321-9876543   |   almadina.travels</text>'),
    ("card-03.svg",
     '<rect x="32" y="34" width="376" height="204" rx="16" fill="#05070c" fill-opacity="0.6"/>'
     '<rect x="52" y="54" width="66" height="66" rx="18" fill="url(#mg)"/>'
     '<text x="85" y="98" font-size="30" font-weight="bold" fill="#ffffff" text-anchor="middle">F</text>'
     '<text x="140" y="82" font-size="24" font-weight="bold" fill="#ffffff">FITZONE</text>'
     '<text x="140" y="104" font-size="24" font-weight="bold" fill="' + ORANGE + '">GYM</text>'
     '<text x="140" y="122" font-size="9" fill="' + MUTED + '" letter-spacing="2">TRAIN HARD • STAY HUMBLE</text>'
     '<g><rect x="52" y="150" width="330" height="1" fill="#ffffff" fill-opacity="0.12"/></g>'
     + c_line(52, 178, "phone", "0345-5566778")
     + c_line(52, 200, "pin", "Chowk Azam Road, Layyah")
     + c_line(52, 222, "globe", "fitzonegym.pk")),
    ("card-04.svg",
     '<rect x="52" y="54" width="336" height="164" rx="14" fill="none" stroke="url(#mg)" stroke-width="2"/>'
     '<text x="220" y="106" font-size="30" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'NOOR CONSTRUCTION</text>'
     '<text x="220" y="128" font-size="9" fill="' + ORANGE + '" letter-spacing="4" text-anchor="middle">'
     'BUILDERS &amp; DEVELOPERS</text>'
     '<text x="220" y="164" font-size="12" fill="' + WHITE + '" text-anchor="middle">'
     'Hassan Ali  •  Chief Engineer</text>'
     '<text x="220" y="196" font-size="11" fill="' + MUTED + '" text-anchor="middle">'
     '0346-1122334   •   noor.builders@gmail.com</text>'),
    ("card-05.svg",
     '<path d="M32 34h376v74H32z" fill="url(#mg)"/>'
     '<text x="220" y="86" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'SPICE ROUTE</text>'
     '<text x="220" y="104" font-size="9" fill="#ffffff" fill-opacity="0.85" letter-spacing="4" '
     'text-anchor="middle">FINE DESI CUISINE</text>'
     + c_line(66, 156, "phone", "0300-4455667")
     + c_line(66, 180, "mail", "hello@spiceroute.pk")
     + c_line(66, 204, "pin", "Food Street, Layyah")
     + '<circle cx="352" cy="180" r="34" fill="none" stroke="' + ORANGE + '" stroke-width="2"/>'
     '<text x="352" y="186" font-size="9" fill="' + ORANGE + '" text-anchor="middle">SCAN</text>'
     '<g fill="' + ORANGE + '"><rect x="336" y="150" width="6" height="6"/><rect x="348" y="150" '
     'width="6" height="6"/><rect x="360" y="150" width="6" height="6"/><rect x="336" y="162" '
     'width="6" height="6"/><rect x="360" y="162" width="6" height="6"/><rect x="336" y="174" '
     'width="6" height="6"/><rect x="348" y="174" width="6" height="6"/><rect x="360" y="174" '
     'width="6" height="6"/></g>'),
    ("card-06.svg",
     '<text x="352" y="212" font-size="120" font-weight="bold" fill="#ffffff" fill-opacity="0.05" '
     'text-anchor="middle">GX</text>'
     '<rect x="52" y="70" width="52" height="52" rx="14" fill="url(#mg)"/>'
     '<text x="78" y="104" font-size="22" font-weight="bold" fill="#ffffff" text-anchor="middle">GX</text>'
     '<text x="120" y="92" font-size="20" font-weight="bold" fill="#ffffff">GX STUDIO</text>'
     '<text x="120" y="110" font-size="9" fill="' + MUTED + '" letter-spacing="3">DESIGN • VIDEO • CODE</text>'
     '<rect x="52" y="140" width="330" height="1" fill="#ffffff" fill-opacity="0.14"/>'
     + c_line(52, 168, "phone", "+92 311 0682944")
     + c_line(52, 192, "mail", "n88908410@gmail.com")
     + c_line(52, 216, "pin", "Layyah, Punjab, Pakistan")),
]

for fname, body in CARDS:
    write(fname, card(fname, body))


# --------------------------------------------------------------------------
# 3. BANNERS & COVERS  (640 x 360)
# --------------------------------------------------------------------------
def banner(name, body, defs_extra=""):
    d, b = base(640, 360, BLUE)
    d += grad("mg", BLUE, ORANGE) + grad("mg2", ORANGE, BLUE_D) + grad("mgv", BLUE_D, "#05070c", 0)
    d += defs_extra
    b += body
    return svg(640, 360, b, d)


BANNERS = [
    ("banner-01.svg",  # YouTube channel art
     '<rect y="0" width="640" height="360" fill="url(#mgv)"/>'
     '<circle cx="548" cy="86" r="150" fill="url(#mg)" fill-opacity="0.35"/>'
     '<circle cx="120" cy="330" r="120" fill="url(#mg2)" fill-opacity="0.25"/>'
     '<g transform="translate(52 150)">'
     '<text x="0" y="0" font-size="60" font-weight="bold" fill="#ffffff">GX RAJPUT</text>'
     '<text x="0" y="34" font-size="15" fill="' + ORANGE + '" letter-spacing="7">'
     'GRAPHICS  •  VIDEO  •  CODE</text>'
     '<rect x="0" y="56" width="190" height="40" rx="20" fill="url(#mg)"/>'
     '<text x="95" y="82" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'SUBSCRIBE</text></g>'),
    ("banner-02.svg",  # Facebook cover
     '<rect width="640" height="360" fill="#06122e"/>'
     '<path d="M0 250 Q160 190 320 250 T640 250 V360 H0 Z" fill="url(#mg)" fill-opacity="0.55"/>'
     '<path d="M0 286 Q160 232 320 286 T640 286 V360 H0 Z" fill="' + ORANGE + '" fill-opacity="0.5"/>'
     '<circle cx="556" cy="76" r="46" fill="url(#mg)"/>'
     '<text x="556" y="88" font-size="34" font-weight="bold" fill="#ffffff" text-anchor="middle">GX</text>'
     '<text x="46" y="170" font-size="46" font-weight="bold" fill="#ffffff">Gx Rajput Studio</text>'
     '<text x="46" y="202" font-size="14" fill="' + WHITE + '" fill-opacity="0.8" letter-spacing="4">'
     'DESIGN • EDITING • DEVELOPMENT</text>'
     '<text x="46" y="230" font-size="12" fill="' + ORANGE + '" letter-spacing="3">'
     '@gx_rajput  •  Layyah, Punjab</text>'),
    ("banner-03.svg",  # LinkedIn banner
     '<rect width="640" height="360" fill="#070b13"/>'
     '<g stroke="' + BLUE + '" stroke-opacity="0.35" fill="none">'
     + "".join(f'<path d="M{x} 0 V360"/>' for x in range(40, 641, 60))
     + "".join(f'<path d="M0 {y} H640"/>' for y in range(40, 361, 60))
     + '</g>'
     '<rect x="0" y="150" width="640" height="70" fill="url(#mg)" fill-opacity="0.9"/>'
     '<text x="320" y="196" font-size="38" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'BUILDING BRANDS THAT SELL</text>'
     '<text x="320" y="252" font-size="13" fill="' + MUTED + '" letter-spacing="6" text-anchor="middle">'
     '7+ YEARS  •  LAYYAH, PAKISTAN</text>'
     '<circle cx="86" cy="290" r="10" fill="' + ORANGE + '"/>'
     '<text x="108" y="296" font-size="13" fill="' + WHITE + '">Freelance — open for work</text>'),
    ("banner-04.svg",  # Twitch / gaming banner
     '<rect width="640" height="360" fill="#08070f"/>'
     + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="10" fill="{c}" fill-opacity="{o}"/>'
               for x, y, w, c, o in [(60, 90, 180, BLUE, 0.9), (300, 90, 260, ORANGE, 0.8),
                                     (120, 130, 320, BLUE, 0.5), (90, 250, 220, ORANGE, 0.75),
                                     (360, 250, 190, BLUE, 0.85)])
     + '<text x="320" y="186" font-size="64" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'GX_RAJPUT</text>'
     '<text x="320" y="216" font-size="14" fill="' + ORANGE + '" letter-spacing="8" text-anchor="middle">'
     'LIVE • EDITING • GAMING</text>'),
    ("banner-05.svg",  # X / Twitter header
     '<rect width="640" height="360" fill="#060a12"/>'
     '<path d="M0 360 L200 0 H420 L640 360 Z" fill="url(#mg)" fill-opacity="0.28"/>'
     '<circle cx="320" cy="180" r="96" fill="none" stroke="url(#mg)" stroke-width="3"/>'
     '<circle cx="320" cy="180" r="130" fill="none" stroke="' + ORANGE + '" stroke-opacity="0.4" '
     'stroke-width="1" stroke-dasharray="6 10"/>'
     '<text x="320" y="188" font-size="42" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     '@gx_rajput</text>'
     '<text x="320" y="216" font-size="12" fill="' + MUTED + '" letter-spacing="5" text-anchor="middle">'
     'GRAPHIC DESIGNER &amp; DEVELOPER</text>'),
    ("banner-06.svg",  # Sale / event banner
     '<rect width="640" height="360" fill="#0a0509"/>'
     + "".join(f'<path d="M320 180 L{x1} {y1} L{x2} {y2} Z" fill="{c}" fill-opacity="{o}"/>'
               for x1, y1, x2, y2, c, o in [(320, 0, 0, 60, BLUE, 0.30), (640, 60, 320, 0, ORANGE, 0.22),
                                            (0, 300, 320, 360, ORANGE, 0.25), (320, 360, 640, 300, BLUE, 0.30)])
     + '<rect x="120" y="118" width="400" height="124" rx="18" fill="#05070c" fill-opacity="0.72" '
     'stroke="url(#mg)" stroke-width="2"/>'
     '<text x="320" y="172" font-size="52" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'MEGA SALE</text>'
     '<text x="320" y="206" font-size="26" font-weight="bold" fill="' + ORANGE + '" text-anchor="middle">'
     'UPTO 50% OFF</text>'
     '<text x="320" y="230" font-size="11" fill="' + MUTED + '" letter-spacing="4" text-anchor="middle">'
     'LIMITED TIME  •  ORDER ON WHATSAPP</text>'),
]

for fname, body in BANNERS:
    write(fname, banner(fname, body))


# --------------------------------------------------------------------------
# 4. PRINT & PACKAGING  (600 x 420)
# --------------------------------------------------------------------------
def printshot(name, body, defs_extra=""):
    d, b = base(600, 420, ORANGE)
    d += grad("mg", BLUE, ORANGE) + grad("mg2", ORANGE, BLUE_D) + defs_extra
    b += body
    return svg(600, 420, b, d)


PRINTS = [
    ("print-01.svg",  # Billboard
     '<rect y="0" width="600" height="420" fill="url(#mgv)"/>'
     '<rect y="300" width="600" height="120" fill="#0b0f18"/>'
     + "".join(f'<rect x="{x}" y="358" width="46" height="6" rx="3" fill="#ffffff" fill-opacity="0.5"/>'
               for x in range(20, 600, 90))
     + '<rect x="180" y="330" width="14" height="76" fill="#141a26"/>'
     '<rect x="406" y="330" width="14" height="76" fill="#141a26"/>'
     '<rect x="80" y="60" width="440" height="230" rx="6" fill="#05070c" stroke="#1b2333" stroke-width="6"/>'
     '<rect x="92" y="72" width="416" height="206" rx="4" fill="url(#mg)" fill-opacity="0.9"/>'
     '<text x="300" y="150" font-size="46" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'AL-NOOR MOTORS</text>'
     '<text x="300" y="186" font-size="16" fill="#ffffff" fill-opacity="0.9" letter-spacing="5" '
     'text-anchor="middle">BOOK YOUR TEST DRIVE TODAY</text>'
     '<rect x="228" y="204" width="144" height="38" rx="19" fill="#05070c" fill-opacity="0.85"/>'
     '<text x="300" y="229" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     '0300-1234567</text>'
     '<circle cx="300" cy="330" r="0" fill="none"/>'),
    ("print-02.svg",  # Packaging box
     '<g transform="translate(150 96)">'
     '<path d="M0 40 L110 0 L220 40 L110 82 Z" fill="url(#mg2)"/>'
     '<path d="M0 40 L110 82 V250 L0 208 Z" fill="#101828"/>'
     '<path d="M220 40 L110 82 V250 L220 208 Z" fill="#0a0f1a"/>'
     '<text x="112" y="146" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle" '
     'transform="rotate(-20 112 146)">SPICE</text>'
     '<text x="112" y="176" font-size="18" font-weight="bold" fill="' + ORANGE + '" text-anchor="middle" '
     'transform="rotate(-20 112 176)">ROUTE</text>'
     '<path d="M28 96 L84 118 V196 L28 174 Z" fill="#0d1424"/>'
     '<text x="56" y="150" font-size="11" fill="' + MUTED + '" text-anchor="middle" '
     'transform="rotate(-20 56 150)">250g</text>'
     '</g>'
     '<ellipse cx="260" cy="356" rx="150" ry="18" fill="#000000" fill-opacity="0.55"/>'),
    ("print-03.svg",  # Flyer
     '<g transform="rotate(-8 300 210)">'
     '<rect x="150" y="46" width="300" height="330" rx="4" fill="#0b1019" stroke="#1c2436" stroke-width="2"/>'
     '<rect x="150" y="46" width="300" height="96" fill="url(#mg)"/>'
     '<text x="300" y="104" font-size="30" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'GRAND OPENING</text>'
     '<text x="300" y="128" font-size="11" fill="#ffffff" fill-opacity="0.9" letter-spacing="3" '
     'text-anchor="middle">FITZONE GYM • LAYYAH</text>'
     '<text x="300" y="196" font-size="56" font-weight="bold" fill="' + ORANGE + '" text-anchor="middle">'
     '50% OFF</text>'
     '<text x="300" y="222" font-size="13" fill="' + WHITE + '" letter-spacing="3" text-anchor="middle">'
     'ON ALL MEMBERSHIPS</text>'
     '<rect x="196" y="246" width="208" height="1" fill="#ffffff" fill-opacity="0.18"/>'
     '<text x="300" y="278" font-size="11" fill="' + MUTED + '" text-anchor="middle">'
     'Cardio • Weights • CrossFit • Sauna</text>'
     '<text x="300" y="300" font-size="11" fill="' + MUTED + '" text-anchor="middle">'
     'Chowk Azam Road, Layyah</text>'
     '<rect x="222" y="322" width="156" height="34" rx="17" fill="url(#mg)"/>'
     '<text x="300" y="344" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     '0300-5566778</text></g>'),
    ("print-04.svg",  # Letterhead + envelope
     '<rect x="70" y="60" width="330" height="290" rx="4" fill="#f4f7ff"/>'
     '<rect x="70" y="60" width="330" height="64" fill="url(#mg)"/>'
     '<text x="98" y="102" font-size="22" font-weight="bold" fill="#ffffff">GX STUDIO</text>'
     '<text x="98" y="118" font-size="8" fill="#ffffff" fill-opacity="0.85" letter-spacing="3">'
     'DESIGN • VIDEO • CODE</text>'
     + "".join(f'<rect x="98" y="{y}" width="{w}" height="5" rx="2" fill="#c6d2e8"/>'
               for y, w in [(168, 274), (188, 250), (208, 268), (228, 210), (248, 262), (268, 180)])
     + '<rect x="98" y="300" width="90" height="30" rx="4" fill="url(#mg)"/>'
     '<rect x="330" y="60" width="12" height="290" fill="' + ORANGE + '" fill-opacity="0.9"/>'
     '<g transform="rotate(12 430 250)">'
     '<rect x="380" y="196" width="176" height="112" rx="4" fill="#e8eefb" stroke="#c9d6ee" stroke-width="2"/>'
     '<path d="M380 198 L468 268 L556 198" fill="none" stroke="#b7c6e2" stroke-width="2"/></g>'),
    ("print-05.svg",  # Tri-fold brochure
     '<g>'
     '<rect x="52" y="72" width="172" height="290" rx="4" fill="#0c121d" stroke="#1c2436"/>'
     '<rect x="214" y="60" width="172" height="290" rx="4" fill="#101828" stroke="#1c2436"/>'
     '<rect x="376" y="72" width="172" height="290" rx="4" fill="#0c121d" stroke="#1c2436"/>'
     '<text x="300" y="120" font-size="26" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'NOOR</text>'
     '<text x="300" y="150" font-size="26" font-weight="bold" fill="' + ORANGE + '" text-anchor="middle">'
     'CONSTRUCTION</text>'
     '<text x="300" y="176" font-size="9" fill="' + MUTED + '" letter-spacing="4" text-anchor="middle">'
     'BUILDERS &amp; DEVELOPERS</text>'
     + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2" fill="#22304a"/>'
               for x, y, w in [(76, 122, 124), (76, 142, 108), (76, 162, 130), (76, 182, 96),
                               (400, 122, 124), (400, 142, 112), (400, 162, 128), (400, 182, 100)])
     + '<circle cx="138" cy="250" r="36" fill="url(#mg)" fill-opacity="0.85"/>'
     '<text x="138" y="258" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">PLAN</text>'
     '<circle cx="462" cy="250" r="36" fill="url(#mg2)" fill-opacity="0.85"/>'
     '<text x="462" y="258" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">BUILD</text>'
     '<text x="300" y="326" font-size="11" fill="' + MUTED + '" text-anchor="middle">'
     '0346-1122334  •  Layyah, Punjab</text></g>'),
    ("print-06.svg",  # Menu card
     '<g transform="rotate(-3 300 210)">'
     '<rect x="176" y="40" width="248" height="350" rx="10" fill="#0a0f19" stroke="#202a3d" stroke-width="2"/>'
     '<text x="300" y="92" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'SPICE ROUTE</text>'
     '<text x="300" y="112" font-size="9" fill="' + ORANGE + '" letter-spacing="4" text-anchor="middle">'
     'MENU</text>'
     '<path d="M232 124 H368" stroke="url(#mg)" stroke-width="2"/>'
     + "".join(
        f'<text x="204" y="{y}" font-size="12" font-weight="bold" fill="#eaf0ff">{n}</text>'
        f'<text x="396" y="{y}" font-size="12" fill="{ORANGE}" text-anchor="end">{p}</text>'
        f'<text x="204" y="{y + 15}" font-size="8" fill="{MUTED}">{d}</text>'
        for y, n, p, d in [(156, "Chicken Karahi", "1,450", "Boneless • Desi Ghee • Spicy"),
                           (200, "Beef Seekh Kebab", "1,250", "Charcoal grilled • 6 pcs"),
                           (244, "Mutton Pulao", "1,100", "Basmati • Slow cooked"),
                           (288, "Zinger Burger", "850", "Double patty • Fries")])
     + '<text x="300" y="360" font-size="9" fill="' + MUTED + '" text-anchor="middle">'
     'Food Street, Layyah  •  0300-4455667</text></g>'),
]

for fname, body in PRINTS:
    write(fname, printshot(fname, body, radial("mgv", BLUE, 0.35) if fname == "print-01.svg" else ""))


# --------------------------------------------------------------------------
# 5. WEB & APP UI  (600 x 400)
# --------------------------------------------------------------------------
def uishot(name, body, defs_extra=""):
    d, b = base(600, 400, BLUE)
    d += grad("mg", BLUE, ORANGE) + grad("mg2", ORANGE, BLUE_D) + defs_extra
    b += body
    return svg(600, 400, b, d)


def browser_frame(x, y, w, h, inner):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#0d1421" stroke="#1d2740"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="10" fill="#141c2c"/>'
        f'<rect x="{x}" y="{y + 16}" width="{w}" height="10" fill="#141c2c"/>'
        f'<circle cx="{x + 16}" cy="{y + 13}" r="4" fill="' + ORANGE + '"/>'
        f'<circle cx="{x + 30}" cy="{y + 13}" r="4" fill="' + BLUE + '"/>'
        f'<circle cx="{x + 44}" cy="{y + 13}" r="4" fill="#2b3752"/>'
        f'<rect x="{x + 62}" y="{y + 7}" width="{w - 100}" height="12" rx="6" fill="#0a0f19"/>'
        f'{inner}'
    )


def phone_frame(x, y, w, h, inner):
    return (
        f'<rect x="{x - 6}" y="{y - 6}" width="{w + 12}" height="{h + 12}" rx="26" fill="#05070c" '
        f'stroke="#1d2740" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="#0b1019"/>'
        f'<rect x="{x + w / 2 - 22}" y="{y + 6}" width="44" height="6" rx="3" fill="#1d2740"/>'
        f'{inner}'
        f'<rect x="{x + w / 2 - 26}" y="{y + h - 14}" width="52" height="4" rx="2" fill="#2b3752"/>'
    )


UIS = [
    ("ui-01.svg",  # eCommerce dashboard
     browser_frame(40, 46, 520, 310,
                   '<rect x="40" y="72" width="110" height="284" fill="#0a0f19"/>'
                   '<rect x="56" y="92" width="70" height="10" rx="5" fill="url(#mg)"/>'
                   + "".join(f'<rect x="56" y="{y}" width="{w}" height="9" rx="4" fill="#1e293f"/>'
                             for y, w in [(120, 70), (144, 56), (168, 64), (192, 48), (216, 60)])
                   + '<rect x="164" y="92" width="150" height="76" rx="8" fill="#101a2c" stroke="#1d2740"/>'
                   '<text x="180" y="122" font-size="10" fill="' + MUTED + '">REVENUE</text>'
                   '<text x="180" y="150" font-size="22" font-weight="bold" fill="#ffffff">Rs 842K</text>'
                   '<rect x="330" y="92" width="150" height="76" rx="8" fill="#101a2c" stroke="#1d2740"/>'
                   '<text x="346" y="122" font-size="10" fill="' + MUTED + '">ORDERS</text>'
                   '<text x="346" y="150" font-size="22" font-weight="bold" fill="' + ORANGE + '">1,284</text>'
                   '<rect x="496" y="92" width="48" height="76" rx="8" fill="url(#mg)" fill-opacity="0.9"/>'
                   '<rect x="164" y="182" width="380" height="120" rx="8" fill="#101a2c" stroke="#1d2740"/>'
                   + "".join(f'<rect x="{190 + i * 46}" y="{252 - h}" width="26" height="{h}" rx="4" '
                             f'fill="url(#mg)" fill-opacity="{0.5 + i * 0.06}"/>'
                             for i, h in enumerate([34, 56, 42, 74, 60, 88, 70]))
                   + '<text x="180" y="206" font-size="10" fill="' + MUTED + '" letter-spacing="2">'
                   'SALES OVERVIEW</text>'
                   '<rect x="164" y="316" width="380" height="50" rx="8" fill="#101a2c" stroke="#1d2740"/>'
                   + "".join(f'<rect x="{182 + i * 118}" y="332" width="{w}" height="8" rx="4" fill="#1e293f"/>'
                             for i, w in enumerate([96, 84, 100]))
                   )),
    ("ui-02.svg",  # food delivery app
     phone_frame(210, 50, 180, 320,
                 '<rect x="210" y="70" width="180" height="26" fill="#0a0f19"/>'
                 '<text x="226" y="88" font-size="9" fill="' + MUTED + '" letter-spacing="2">'
                 'DELIVER TO</text>'
                 '<text x="226" y="118" font-size="13" font-weight="bold" fill="#ffffff">'
                 'Layyah, Punjab</text>'
                 '<rect x="224" y="132" width="152" height="26" rx="13" fill="#131c2d"/>'
                 '<text x="238" y="149" font-size="9" fill="' + MUTED + '">Search biryani...</text>'
                 + "".join(
                     f'<rect x="224" y="{166 + i * 58}" width="152" height="50" rx="10" fill="#101a2c"/>'
                     f'<rect x="232" y="{174 + i * 58}" width="40" height="34" rx="8" fill="url(#mg)" '
                     f'fill-opacity="{0.9 - i * 0.12}"/>'
                     f'<rect x="280" y="{178 + i * 58}" width="{80 - i * 8}" height="8" rx="4" fill="#22304a"/>'
                     f'<rect x="280" y="{192 + i * 58}" width="{58 - i * 5}" height="7" rx="3" fill="#1a2438"/>'
                     for i in range(4))
                 + '<rect x="224" y="332" width="152" height="26" rx="13" fill="url(#mg)"/>'
                 '<text x="300" y="349" font-size="10" font-weight="bold" fill="#ffffff" '
                 'text-anchor="middle">TRACK ORDER</text>')),
    ("ui-03.svg",  # fitness app
     phone_frame(210, 50, 180, 320,
                 '<text x="226" y="86" font-size="12" font-weight="bold" fill="#ffffff">'
                 'Today\'s Activity</text>'
                 '<g transform="translate(300 156)">'
                 '<circle r="46" fill="none" stroke="#16203300" stroke-width="10"/>'
                 '<circle r="46" fill="none" stroke="#1b2540" stroke-width="10"/>'
                 '<circle r="46" fill="none" stroke="url(#mg)" stroke-width="10" '
                 'stroke-linecap="round" stroke-dasharray="220 290" transform="rotate(-90)"/>'
                 '<text y="6" font-size="22" font-weight="bold" fill="#ffffff" text-anchor="middle">'
                 '78%</text>'
                 '<text y="22" font-size="8" fill="' + MUTED + '" text-anchor="middle">GOAL</text></g>'
                 + "".join(
                     f'<rect x="{224 + (i % 2) * 80}" y="{228 + (i // 2) * 50}" width="70" height="42" '
                     f'rx="8" fill="#101a2c"/>'
                     f'<text x="{236 + (i % 2) * 80}" y="{246 + (i // 2) * 50}" font-size="12" '
                     f'font-weight="bold" fill="#ffffff">{v}</text>'
                     f'<text x="{236 + (i % 2) * 80}" y="{260 + (i // 2) * 50}" font-size="8" '
                     f'fill="{MUTED}">{k}</text>'
                     for i, (v, k) in enumerate([("8.4k", "STEPS"), ("420", "KCAL"), ("62", "BPM"), ("7h", "SLEEP")]))
                 + '<rect x="224" y="330" width="152" height="26" rx="13" fill="url(#mg)"/>'
                 '<text x="300" y="347" font-size="10" font-weight="bold" fill="#ffffff" '
                 'text-anchor="middle">START WORKOUT</text>')),
    ("ui-04.svg",  # chat app
     phone_frame(210, 50, 180, 320,
                 '<rect x="210" y="70" width="180" height="40" fill="#0a0f19"/>'
                 '<circle cx="234" cy="90" r="13" fill="url(#mg)"/>'
                 '<rect x="256" y="82" width="60" height="7" rx="3" fill="#22304a"/>'
                 '<rect x="256" y="94" width="40" height="6" rx="3" fill="#1a2438"/>'
                 + "".join(
                     f'<rect x="{x}" y="{100 + i * 56}" width="{w}" height="34" rx="10" fill="{c}"/>'
                     for i, (x, w, c) in enumerate([(224, 96, "#16233c"), (286, 96, "url(#mg)"),
                                                    (224, 118, "#16233c"), (262, 120, "url(#mg)"),
                                                    (224, 88, "#16233c")]))
                 + '<rect x="224" y="330" width="120" height="26" rx="13" fill="#131c2d"/>'
                 '<circle cx="360" cy="343" r="13" fill="url(#mg)"/>')),
    ("ui-05.svg",  # analytics web app
     browser_frame(40, 46, 520, 310,
                   '<rect x="40" y="72" width="520" height="34" fill="#0a0f19"/>'
                   '<text x="60" y="94" font-size="11" font-weight="bold" fill="#ffffff">NEXUS ANALYTICS</text>'
                   + "".join(f'<rect x="{x}" y="86" width="{w}" height="7" rx="3" fill="#1e293f"/>'
                             for x, w in [(200, 40), (254, 52), (320, 36), (372, 46)])
                   + '<circle cx="536" cy="89" r="11" fill="url(#mg)"/>'
                   '<rect x="56" y="122" width="200" height="220" rx="10" fill="#101a2c" stroke="#1d2740"/>'
                   + "".join(f'<rect x="76" y="{150 + i * 30}" width="{w}" height="9" rx="4" fill="#1e293f"/>'
                             for i, w in enumerate([150, 120, 140, 100, 130, 90]))
                   + '<rect x="272" y="122" width="272" height="130" rx="10" fill="#101a2c" stroke="#1d2740"/>'
                   + "".join(f'<rect x="{292 + i * 34}" y="{212 - h}" width="18" height="{h}" rx="4" '
                             f'fill="url(#mg)" fill-opacity="{0.45 + i * 0.07}"/>'
                             for i, h in enumerate([22, 40, 30, 56, 46, 68, 52]))
                   + '<rect x="272" y="268" width="130" height="74" rx="10" fill="#101a2c" stroke="#1d2740"/>'
                   '<text x="288" y="294" font-size="9" fill="' + MUTED + '">CONVERSION</text>'
                   '<text x="288" y="320" font-size="20" font-weight="bold" fill="' + ORANGE + '">4.8%</text>'
                   '<rect x="414" y="268" width="130" height="74" rx="10" fill="#101a2c" stroke="#1d2740"/>'
                   '<text x="430" y="294" font-size="9" fill="' + MUTED + '">SESSIONS</text>'
                   '<text x="430" y="320" font-size="20" font-weight="bold" fill="#ffffff">32.1K</text>')),
    ("ui-06.svg",  # portfolio site mock
     browser_frame(40, 46, 520, 310,
                   '<rect x="40" y="72" width="520" height="284" fill="#070b13"/>'
                   '<circle cx="420" cy="220" r="120" fill="url(#mg)" fill-opacity="0.30"/>'
                   '<text x="76" y="150" font-size="30" font-weight="bold" fill="#ffffff">Gx_Rajput</text>'
                   '<text x="76" y="178" font-size="11" fill="' + ORANGE + '" letter-spacing="5">'
                   'GRAPHICS • VIDEO • CODE</text>'
                   '<text x="76" y="212" font-size="11" fill="' + MUTED + '">Designing brands, editing</text>'
                   '<text x="76" y="230" font-size="11" fill="' + MUTED + '">stories and shipping software.</text>'
                   '<rect x="76" y="250" width="104" height="30" rx="15" fill="url(#mg)"/>'
                   '<text x="128" y="270" font-size="10" font-weight="bold" fill="#ffffff" '
                   'text-anchor="middle">HIRE ME</text>'
                   '<rect x="192" y="250" width="104" height="30" rx="15" fill="none" stroke="#253150"/>'
                   '<text x="244" y="270" font-size="10" font-weight="bold" fill="#ffffff" '
                   'text-anchor="middle">PORTFOLIO</text>'
                   + "".join(f'<rect x="{76 + i * 74}" y="308" width="60" height="34" rx="6" '
                             f'fill="#101a2c" stroke="#1d2740"/>' for i in range(6))
                   )),
]

for fname, body in UIS:
    write(fname, uishot(fname, body))


# --------------------------------------------------------------------------
# 6. YOUTUBE THUMBNAILS (SVG fallbacks) (SVG fallbacks)  (640 x 360)
# --------------------------------------------------------------------------
def thumb(name, body, defs_extra=""):
    d, b = base(640, 360, BLUE)
    d += grad("mg", BLUE, ORANGE) + grad("mg2", ORANGE, BLUE_D) + defs_extra
    b += body
    return svg(640, 360, b, d)


THUMBS = [
    ("thumb-02.svg",
     '<rect width="640" height="360" fill="#06080f"/>'
     '<circle cx="470" cy="180" r="150" fill="url(#mg)" fill-opacity="0.28"/>'
     + "".join(f'<rect x="{60 + i * 92}" y="{90 + (i % 2) * 40}" width="70" height="70" rx="14" '
               f'fill="#101a2c" stroke="url(#mg)" stroke-width="2"/>' for i in range(5))
     + '<text x="52" y="322" font-size="46" font-weight="bold" fill="#ffffff">TOP 5 GADGETS</text>'
     '<text x="52" y="348" font-size="16" font-weight="bold" fill="' + ORANGE + '">UNDER RS 20,000</text>'
     '<path d="M420 300 h150 l-30 -26 h-120z" fill="' + ORANGE + '"/>'
     '<text x="495" y="292" font-size="20" font-weight="bold" fill="#05070c" text-anchor="middle">WOW</text>'),
    ("thumb-03.svg",
     '<rect width="640" height="360" fill="#070a13"/>'
     + "".join(f'<rect x="330" y="{70 + i * 46}" width="{w}" height="26" rx="6" fill="{c}" '
               f'fill-opacity="{o}"/>' for i, (w, c, o) in enumerate([(240, BLUE, 0.85), (190, ORANGE, 0.8),
                                                                      (270, BLUE, 0.6), (150, ORANGE, 0.7),
                                                                      (220, BLUE, 0.5)]))
     + '<text x="52" y="150" font-size="52" font-weight="bold" fill="#ffffff">HOW I EDIT</text>'
     '<text x="52" y="192" font-size="52" font-weight="bold" fill="' + ORANGE + '">REELS FAST</text>'
     '<rect x="52" y="220" width="176" height="42" rx="21" fill="url(#mg)"/>'
     '<text x="140" y="248" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'PREMIERE PRO</text>'
     '<text x="248" y="248" font-size="15" font-weight="bold" fill="#ffffff">+ CAPCUT</text>'),
    ("thumb-04.svg",
     '<rect width="640" height="360" fill="#0b0709"/>'
     + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{ORANGE}" fill-opacity="{o}"/>'
               for x, y, r, o in [(500, 110, 90, 0.30), (560, 210, 60, 0.22), (420, 250, 44, 0.25)])
     + '<text x="52" y="140" font-size="50" font-weight="bold" fill="#ffffff">STREET FOOD</text>'
     '<text x="52" y="184" font-size="50" font-weight="bold" fill="' + ORANGE + '">TOUR LAYYAH</text>'
     '<text x="52" y="220" font-size="16" fill="' + WHITE + '" fill-opacity="0.85">'
     'We tried 7 stalls in one night</text>'
     '<circle cx="520" cy="250" r="52" fill="url(#mg)"/>'
     '<text x="520" y="262" font-size="30" font-weight="bold" fill="#ffffff" text-anchor="middle">7</text>'),
    ("thumb-05.svg",
     '<rect width="640" height="360" fill="#05070e"/>'
     '<text x="52" y="150" font-size="46" font-weight="bold" fill="#ffffff">BUILD AN APP</text>'
     '<text x="52" y="196" font-size="46" font-weight="bold" fill="' + BLUE + '">IN 10 MINUTES</text>'
     '<rect x="52" y="222" width="230" height="44" rx="22" fill="url(#mg)"/>'
     '<text x="167" y="251" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">'
     'FLUTTER TUTORIAL</text>'
     + "".join(f'<rect x="{430 + (i % 2) * 60}" y="{80 + i * 52}" width="{90 - (i % 3) * 16}" '
               f'height="34" rx="8" fill="#101a2c" stroke="#1d2740"/>' for i in range(6))
     + '<path d="M356 320 h108 l-24 -22 h-84z" fill="' + ORANGE + '"/>'
     '<text x="410" y="313" font-size="16" font-weight="bold" fill="#05070c" text-anchor="middle">'
     'EASY</text>'),
    ("thumb-06.svg",
     '<rect width="640" height="360" fill="#06090f"/>'
     '<circle cx="320" cy="180" r="130" fill="none" stroke="url(#mg)" stroke-width="3" '
     'stroke-dasharray="10 12"/>'
     '<text x="52" y="164" font-size="48" font-weight="bold" fill="#ffffff">HIDDEN PHONE</text>'
     '<text x="52" y="210" font-size="48" font-weight="bold" fill="' + ORANGE + '">SETTINGS</text>'
     '<text x="52" y="244" font-size="16" fill="' + WHITE + '" fill-opacity="0.85">'
     '99% people never change these</text>'
     '<circle cx="520" cy="230" r="58" fill="url(#mg)"/>'
     '<path d="M492 230 l20 20 l40 -44" fill="none" stroke="#ffffff" stroke-width="8" '
     'stroke-linecap="round"/>'),
]

for fname, body in THUMBS:
    write(fname, thumb(fname, body))

print(f"Generated {len(LOGOS) + len(CARDS) + len(BANNERS) + len(PRINTS) + len(UIS) + len(THUMBS)} SVG designs -> {OUT}")
