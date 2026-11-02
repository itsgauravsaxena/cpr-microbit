"""Robot orchestra: printable A4 paper-robot template, IKEA-style (parts A-H + picture steps).

    python3 make_template.py da|en   ->  template-<lang>.html  (6 A4 pages; print to PDF with Chrome)
"""
import math
import pathlib
import sys

LANG = sys.argv[1] if len(sys.argv) > 1 else "da"
OUT = pathlib.Path(__file__).with_name(f"template-{LANG}.html")
PAGES = 7

EN = {
    "klip": "cut", "fold": "fold",
    "Kroppen": "The body",
    "Klip langs den hele streg. Fold siderne BAGUD langs de stiplede streger — så kan robotten stå.":
        "Cut along the solid line. Fold the sides BACKWARDS along the dashed lines so the robot can stand.",
    "FOLD BAGUD": "FOLD BACK", "servo 2 · hoved": "servo 2 · head", "servo 1 · arm": "servo 1 · arm",
    "↑ tape servoerne her, akslen fremad": "↑ tape the servos here, shaft facing forward",
    "NAVN:": "NAME:", "MIN TONE": "MY NOTE", "lim G her": "glue G here",
    "Tip: lim kroppen på et stykke karton (fx fra en cornflakespakke) hvis papiret er for blødt.":
        "Tip: glue the body onto thin card (e.g. a cereal box) if the paper is too floppy.",
    "Hoved, arme og tromme": "Head, arms and drum",
    "Klip alle dele ud. Armene foldes på midten og limes sammen — så bliver de stive.":
        "Cut out all the parts. Fold the arms in half and glue them together so they get stiff.",
    "prik et hul i hver prik med en blyant": "poke a hole in each dot with a pencil",
    "servo 2 bagpå her": "servo 2 behind here", "TROMMESTIK": "DRUMSTICK",
    "fold på midten · lim sammen": "fold in half · glue together", "servo 1": "servo 1",
    "PYNT-ARM": "DECORATION ARM", "valgfri · tape på venstre skulder": "optional · tape onto the left shoulder", "valgfri": "optional", "foldet:": "folded:", "lim": "glue",
    "pynt-arm (valgfri)": "deco arm (optional)",
    "TROMME · rul til et rør, tape fliken indeni": "DRUM · roll into a tube, tape the tab inside",
    "Tone-badge, trommeskind og pynt": "Note badge, drum top and decorations",
    "Klip KUN din egen tone-badge ud, og lim den på robottens bryst. Farvelæg pynten, og klip den ud.":
        "Cut out ONLY your own note badge and glue it on the robot's chest. Colour the decorations and cut them out.",
    "dyb": "low", "trommer": "drums", "tone-badges · en til hver robot": "note badges · one for each robot",
    "TROMMESKIND": "DRUM TOP", "klip fligene ud, fold dem ned, lim på E": "cut out the tabs, fold them down, glue onto E",
    "PYNT": "DECORATIONS", "Tegn også selv: hår, ører, en hat, en kappe… det er DIN robot!":
        "Draw your own too: hair, ears, a hat, a cape… it's YOUR robot!",
    "Dele og værktøj": "Parts and tools", "Tjek, at du har det hele, før du starter.": "Check that you have everything before you start.",
    "Papirdele": "Paper parts", "Elektronik": "Electronics", "Værktøj": "Tools",
    "krop": "body", "hoved": "head", "trommestik": "drumstick", "pynt-arm": "deco arm", "tromme": "drum",
    "trommeskind": "drum top", "din tone": "your note", "pynt": "decorations",
    "servo SG90": "servo SG90", "LED": "LED", "micro:bit + shield": "micro:bit + shield", "ledninger": "wires",
    "batteripakke": "battery pack", "saks": "scissors", "tape": "tape", "limstift": "glue stick",
    "blyant": "pencil", "viskelæder": "eraser", "farver": "colour pens",
    "Ledninger til sensor-shieldet": "Wiring on the sensor shield", "Servo 1 · arm": "Servo 1 · arm",
    "Servo 2 · hoved": "Servo 2 · head", "LED-øje venstre": "LED eye, left", "LED-øje højre": "LED eye, right",
    "brun → G · rød → V · orange → S": "brown → G · red → V · orange → S",
    "langt ben → S · kort ben → G": "long leg → S · short leg → G",
    "Printtjek: denne streg skal være præcis 5 cm. Print i 100 % / \"faktisk størrelse\".":
        "Print check: this line must be exactly 5 cm. Print at 100% / \"actual size\".",
    "Sådan sidder servoerne": "How the servos sit", "Servoen ligger fladt på papiret, og akslen peger mod dig.": "The servo lies flat on the paper, and the shaft points at you.",
    "Servoens dele": "The servo's parts", "horn": "horn", "aksel (drejer)": "shaft (turns)", "øre": "ear", "kabel → shield": "cable → shield",
    "Set fra siden": "Seen from the side", "A · papir": "A · paper", "servo": "servo", "forfra": "front", "du kigger herfra": "you look from here",
    "Arm: C hænger ned og svinger": "Arm: C hangs down and swings", "90° = lige ned": "90° = straight down", "slag": "hit",
    "Hoved: B tapes på hornet og vipper": "Head: B is taped on the horn and tilts", "bagsiden af B": "back of B",
    "1 servo fladt · 2 servo-center · 3 tape C og B på hornet": "1 servo flat · 2 servo-center · 3 tape C and B on the horn",
    "Byg din robot": "Build your robot", "Følg billederne, trin for trin.": "Follow the pictures, step by step.",
    "Klip delene A–H ud": "Cut out parts A–H", "Fold A bagud · fold og lim C + D": "Fold A backwards · fold and glue C + D",
    "Prik huller i B · LED'er ind bagfra": "Poke holes in B · LEDs in from behind",
    "Kør servo-center → begge servoer på 90°": "Run servo-center → both servos at 90°",
    "Servo på halsen · B på servo-armen": "Servo on the neck · B on the servo arm",
    "Servo på skulderen · C peger skråt ned": "Servo on the shoulder · C points down at an angle",
    "Rul E · lim F på · stil den ved benet": "Roll E · glue F on · place it by the leg",
    "Forbind · tænd · spil!": "Connect · switch on · play!",
    "langt": "long", "kort": "short", "+ langt": "+ long", "− kort": "− short",
    "Vakler robotten, eller genstarter micro:bit'en? Brug en batteripakke.":
        "Robot shaky, or the micro:bit restarts? Use a battery pack.",
}


def tr(s):
    if LANG != "en":
        return s
    if s not in EN and any(c in s for c in "æøåÆØÅ"):
        raise SystemExit(f"missing EN for: {s}")
    return EN.get(s, s)


INK = "#111"
CUT = f'fill="none" stroke="{INK}" stroke-width="0.6"'
FOLD = 'fill="none" stroke="#555" stroke-width="0.5" stroke-dasharray="3 2"'
THIN = 'fill="none" stroke="#777" stroke-width="0.35"'
PAPER = "#f6efe2"
BLUE = "#2f7de1"
FONT = 'font-family="Arial, Helvetica, sans-serif"'
LINE = f'fill="#fff" stroke="{INK}" stroke-width="0.5" stroke-linejoin="round"'


def t(x, y, s, size=4, anchor="start", weight="normal", fill="#222", rot=None):
    r = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return (f'<text x="{x}" y="{y}" {FONT} font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}"{r}>{tr(s)}</text>')


def header(sheet, title, sub):
    top = f"ROBOT ORCHESTRA · SHEET {sheet}/{PAGES}" if LANG == "en" else f"ROBOT-ORKESTER · ARK {sheet}/{PAGES}"
    return (t(12, 14, top, 3.6, weight="bold", fill="#7a5530")
            + t(12, 23, title, 7, weight="bold")
            + t(12, 30, sub, 3.6, fill="#444")
            + f'<line x1="150" y1="13" x2="162" y2="13" {CUT}/>' + t(164, 14.2, "klip", 3.4)
            + f'<line x1="150" y1="20" x2="162" y2="20" {FOLD}/>' + t(164, 21.2, "fold", 3.4))


def tag(x, y, letter, r=5.5):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>'
            + f'<text x="{x}" y="{y + r * 0.38}" {FONT} font-size="{r * 1.15}" text-anchor="middle" '
              f'font-weight="bold" fill="#fff">{letter}</text>')


def g(inner, x=0, y=0, s=1, rot=0):
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">{inner}</g>'


def _head(x2, y2, a, color):
    hx1, hy1 = x2 - 3 * math.cos(a - 0.45), y2 - 3 * math.sin(a - 0.45)
    hx2, hy2 = x2 - 3 * math.cos(a + 0.45), y2 - 3 * math.sin(a + 0.45)
    return f'<polygon points="{x2},{y2} {hx1:.2f},{hy1:.2f} {hx2:.2f},{hy2:.2f}" fill="{color}"/>'


def arrow(x1, y1, x2, y2, w=0.7, color=INK):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>'
            + _head(x2, y2, math.atan2(y2 - y1, x2 - x1), color))


def curved_arrow(x1, y1, cx, cy, x2, y2, w=0.7, color=INK):
    return (f'<path d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" fill="none" stroke="{color}" stroke-width="{w}"/>'
            + _head(x2, y2, math.atan2(y2 - cy, x2 - cx), color))


BODY_PATH = ("M92,46 H118 V58 H156 Q164,58 164,66 V70 H196 V186 H164 V196 H154 V256 H160 V272 H110 V256 H116 V196 "
             "H94 V256 H100 V272 H50 V256 H56 V196 H46 V186 H14 V70 H46 V66 Q46,58 54,58 H92 Z")
TORSO_PATH = ("M92,46 H118 V58 H156 Q164,58 164,66 V196 H154 V256 H160 V272 H110 V256 H116 V196 "
              "H94 V256 H100 V272 H50 V256 H56 V196 H46 V66 Q46,58 54,58 H92 Z")


def body_icon(x, y, s, flaps=True):
    p = BODY_PATH if flaps else TORSO_PATH
    return (f'<g transform="translate({x},{y}) scale({s}) translate(-105,-159)">'
            f'<path d="{p}" fill="#fff" stroke="{INK}" stroke-width="{0.5 / s:.2f}"/>'
            f'<circle cx="105" cy="136" r="24" fill="none" stroke="#999" stroke-width="{0.35 / s:.2f}"/></g>')


def head_icon(x, y, s, eyes="dot"):
    w = lambda v: f"{v / s:.2f}"
    inner = (f'<rect x="-60" y="-42" width="120" height="85" rx="10" fill="#fff" stroke="{INK}" stroke-width="{w(0.5)}"/>'
             f'<line x1="0" y1="-42" x2="0" y2="-54" stroke="{INK}" stroke-width="{w(0.5)}"/>'
             f'<circle cx="0" cy="-57" r="5" fill="#fff" stroke="{INK}" stroke-width="{w(0.5)}"/>'
             f'<rect x="-27" y="12" width="54" height="13" rx="2" fill="none" stroke="{INK}" stroke-width="{w(0.4)}"/>')
    for ex in (-25, 25):
        inner += f'<circle cx="{ex}" cy="-12" r="10" fill="#fff" stroke="{INK}" stroke-width="{w(0.4)}"/>'
        inner += (f'<circle cx="{ex}" cy="-12" r="3.5" fill="#e53935"/>' if eyes == "led"
                  else f'<circle cx="{ex}" cy="-12" r="{1.6 / s * 0.3:.2f}" fill="{INK}"/>')
    return g(inner, x, y, s)


def servo_icon(x, y, s=1, horn_rot=0, tabs=True):
    w = lambda v: f"{v / s:.2f}"
    inner = ""
    if tabs:
        inner += f'<rect x="-9.5" y="-6.2" width="32" height="12.4" rx="1" fill="#dbe9fb" stroke="{BLUE}" stroke-width="{w(0.5)}"/>'
    inner += f'<rect x="-5.5" y="-6.2" width="23" height="12.4" rx="1" fill="#9cc3f5" stroke="{BLUE}" stroke-width="{w(0.5)}"/>'
    inner += (f'<g transform="rotate({horn_rot})"><path d="M-2.6,0 L-1.6,-14 A1.6,1.6 0 0,1 1.6,-14 L2.6,0 Z" fill="#fff" '
              f'stroke="{INK}" stroke-width="{w(0.45)}"/></g>')
    inner += f'<circle cx="0" cy="0" r="2.8" fill="#fff" stroke="{INK}" stroke-width="{w(0.45)}"/>'
    return g(inner, x, y, s)


def tape(x, y, w=16, h=5, rot=-20):
    return (f'<rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" fill="#f5e7b8" fill-opacity="0.85" '
            f'stroke="#c9a85a" stroke-width="0.3" transform="translate({x},{y}) rotate({rot})"/>')


def scissors(x, y, s=1, rot=0):
    inner = (f'<circle cx="-7" cy="-3" r="2.6" {LINE}/><circle cx="-7" cy="3" r="2.6" {LINE}/>'
             f'<path d="M-4.6,-2 L9,2.2 L-1,0 Z" fill="#ddd" stroke="{INK}" stroke-width="0.4"/>'
             f'<path d="M-4.6,2 L9,-2.2 L-1,0 Z" fill="#ddd" stroke="{INK}" stroke-width="0.4"/>'
             f'<circle cx="-1" cy="0" r="0.7" fill="{INK}"/>')
    return g(inner, x, y, s, rot)


def pencil(x, y, s=1, rot=0):
    inner = (f'<rect x="0" y="-2" width="26" height="4" fill="#ffd54f" stroke="{INK}" stroke-width="0.4"/>'
             f'<polygon points="0,-2 -6,0 0,2" fill="#f3d9b1" stroke="{INK}" stroke-width="0.4"/>'
             f'<polygon points="-4.5,-0.6 -6,0 -4.5,0.6" fill="{INK}"/>'
             f'<rect x="26" y="-2" width="4" height="4" fill="#f48fb1" stroke="{INK}" stroke-width="0.4"/>')
    return g(inner, x, y, s, rot)


def eraser(x, y, s=1):
    return g(f'<rect x="-8" y="-3.5" width="16" height="7" rx="1" fill="#fff" stroke="{INK}" stroke-width="0.45"/>'
             f'<rect x="-8" y="-3.5" width="6" height="7" rx="1" fill="#90caf9" stroke="{INK}" stroke-width="0.45"/>', x, y, s)


def glue_stick(x, y, s=1, rot=0):
    return g(f'<rect x="-3" y="-6" width="6" height="16" rx="1" fill="#fff" stroke="{INK}" stroke-width="0.45"/>'
             f'<rect x="-3.2" y="-10" width="6.4" height="5" rx="1" fill="#7e57c2" stroke="{INK}" stroke-width="0.45"/>', x, y, s, rot)


def tape_roll(x, y, s=1):
    return g(f'<circle cx="0" cy="0" r="7" fill="#f5e7b8" stroke="{INK}" stroke-width="0.45"/>'
             f'<circle cx="0" cy="0" r="3.8" fill="#fff" stroke="{INK}" stroke-width="0.45"/>', x, y, s)


def led_icon(x, y, s=1, rot=0, labels=False):
    inner = (f'<path d="M-3,0 V-5 A3,3 0 0,1 3,-5 V0 Z" fill="#ef9a9a" stroke="{INK}" stroke-width="0.4"/>'
             f'<rect x="-3.6" y="0" width="7.2" height="1.4" fill="#e57373" stroke="{INK}" stroke-width="0.35"/>'
             f'<line x1="-1.3" y1="1.4" x2="-1.3" y2="13" stroke="{INK}" stroke-width="0.5"/>'
             f'<line x1="1.3" y1="1.4" x2="1.3" y2="9.5" stroke="{INK}" stroke-width="0.5"/>')
    if labels:
        inner += t(-2.2, 16.5, "+", 3.4, "middle", "bold") + t(2.6, 13, "−", 3.4, "middle", "bold")
    return g(inner, x, y, s, rot)


def microbit_icon(x, y, s=1, pattern=None):
    inner = (f'<rect x="-13" y="-10" width="26" height="20" rx="2" fill="#2b2f36" stroke="{INK}" stroke-width="0.45"/>'
             f'<circle cx="-10" cy="0" r="1.5" fill="#bbb"/><circle cx="10" cy="0" r="1.5" fill="#bbb"/>')
    for r in range(5):
        for c in range(5):
            on = pattern is not None and (r, c) in pattern
            inner += f'<rect x="{-5.4 + c * 2.4}" y="{-6.4 + r * 2.4}" width="1.3" height="1.3" fill="{"#ff5252" if on else "#5a5f68"}"/>'
    return g(inner, x, y, s)


def shield_icon(x, y, s=1, pins=("P1", "P2", "P8", "P13")):
    inner = f'<rect x="-30" y="-14" width="60" height="30" rx="2" fill="#e3f2fd" stroke="{INK}" stroke-width="0.45"/>'
    inner += f'<rect x="-14" y="-24" width="28" height="11" rx="1.5" fill="#2b2f36" stroke="{INK}" stroke-width="0.45"/>'
    for i, p in enumerate(pins):
        cx = -21 + i * 14
        for k, lab in enumerate(("S", "V", "G")):
            inner += f'<rect x="{cx - 1.6}" y="{-6 + k * 5}" width="3.2" height="3.2" fill="#ffd54f" stroke="{INK}" stroke-width="0.3"/>'
            inner += t(cx + 3.2, -3.6 + k * 5, lab, 2.2)
        inner += t(cx + 1, 14, p, 3.2, "middle", "bold", BLUE)
    return g(inner, x, y, s)


def battery_icon(x, y, s=1):
    return g(f'<rect x="-11" y="-6" width="22" height="12" rx="1.5" fill="#fff" stroke="{INK}" stroke-width="0.45"/>'
             f'<rect x="-9" y="-4" width="8" height="8" rx="1" fill="#ffcc80" stroke="{INK}" stroke-width="0.35"/>'
             f'<rect x="1" y="-4" width="8" height="8" rx="1" fill="#ffcc80" stroke="{INK}" stroke-width="0.35"/>', x, y, s)


def wire_icon(x, y, s=1, color="#e53935"):
    return g(f'<path d="M-12,0 C-4,-6 4,6 12,0" fill="none" stroke="{color}" stroke-width="1.1"/>'
             f'<rect x="-15" y="-1.6" width="4" height="3.2" fill="#333"/><rect x="11" y="-1.6" width="4" height="3.2" fill="#333"/>', x, y, s)


def arm_path(w, half):
    """Two mirrored arm halves joined at the fold (y=0): a strip of length w with a round end on each half.
    Each round end touches the fold at one point, so folding puts the two halves exactly on top of each other."""
    r, o = half * 2 / 3, half / 3
    cx = w + o
    xa = cx - math.sqrt(r * r - (r - half) ** 2)
    yb = -r + math.sqrt(r * r - o * o)
    full = (f"M0,{-half} H{xa:.2f} A{r:.2f},{r:.2f} 0 1,1 {w},{yb:.2f} V{-yb:.2f} "
            f"A{r:.2f},{r:.2f} 0 1,1 {xa:.2f},{half} H0 Z")
    one = f"M0,0 V{-half} H{xa:.2f} A{r:.2f},{r:.2f} 0 1,1 {w},{yb:.2f} V0 Z"
    return full, one


def strip(x, y, w, h, s=1, fold=True, folded=False):
    """Small arm picture: h = total height of both halves (or of the folded arm when folded=True)."""
    half = h if folded else h / 2
    full, one = arm_path(w, half)
    inner = f'<path d="{one if folded else full}" fill="#fff" stroke="{INK}" stroke-width="{0.5 / s:.2f}"/>'
    if fold and not folded:
        inner += f'<line x1="0" y1="0" x2="{w}" y2="0" stroke="#555" stroke-width="{0.4 / s:.2f}" stroke-dasharray="1.6 1.2"/>'
    return g(inner, x, y + (h if folded else h / 2), s)


def drum_icon(x, y, s=1, skin=True):
    w = lambda v: f"{v / s:.2f}"
    inner = (f'<rect x="-14" y="-10" width="28" height="20" fill="#fff" stroke="none"/>'
             f'<path d="M-14,10 A14,4 0 0,0 14,10" fill="none" stroke="{INK}" stroke-width="{w(0.5)}"/>'
             f'<line x1="-14" y1="-10" x2="-14" y2="10" stroke="{INK}" stroke-width="{w(0.5)}"/>'
             f'<line x1="14" y1="-10" x2="14" y2="10" stroke="{INK}" stroke-width="{w(0.5)}"/>'
             f'<polyline points="-14,-3 -9,5 -4,-3 1,5 6,-3 11,5 14,0" fill="none" stroke="#c99a5b" stroke-width="{w(0.9)}"/>'
             f'<ellipse cx="0" cy="-10" rx="14" ry="4" fill="{PAPER if skin else "#fff"}" stroke="{INK}" stroke-width="{w(0.5)}"/>')
    return g(inner, x, y, s)


def ok_mark(x, y, good=True):
    if good:
        return (f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" stroke="#2e7d32" stroke-width="0.8"/>'
                f'<polyline points="{x - 2},{y} {x - 0.5},{y + 1.8} {x + 2.3},{y - 1.8}" fill="none" stroke="#2e7d32" stroke-width="0.9"/>')
    return (f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" stroke="#c62828" stroke-width="0.8"/>'
            f'<line x1="{x - 2}" y1="{y - 2}" x2="{x + 2}" y2="{y + 2}" stroke="#c62828" stroke-width="0.9"/>'
            f'<line x1="{x + 2}" y1="{y - 2}" x2="{x - 2}" y2="{y + 2}" stroke="#c62828" stroke-width="0.9"/>')


def page(svg):
    return f'<section class="page"><svg viewBox="0 0 210 297" width="210mm" height="297mm" xmlns="http://www.w3.org/2000/svg">{svg}</svg></section>'


def servo_box(x, y, label):
    return (f'<rect x="{x}" y="{y}" width="32" height="12.5" rx="1" fill="#dbe9fb" stroke="{BLUE}" stroke-width="0.5" stroke-dasharray="1.5 1"/>'
            + f'<circle cx="{x + 4.5}" cy="{y + 6.25}" r="2" fill="#fff" stroke="{BLUE}" stroke-width="0.4"/>'
            + t(x + 19, y + 7.4, label, 2.6, "middle", "bold", "#1f5fae"))


# ================= sheet 1: A body =================
s1 = header(1, "Kroppen", "Klip langs den hele streg. Fold siderne BAGUD langs de stiplede streger — så kan robotten stå.")
s1 += f'<path d="{BODY_PATH}" fill="{PAPER}" stroke="{INK}" stroke-width="0.6"/>'
s1 += f'<line x1="46" y1="70" x2="46" y2="186" {FOLD}/><line x1="164" y1="70" x2="164" y2="186" {FOLD}/>'
s1 += t(30, 128, "FOLD BAGUD", 4, "middle", "bold", "#888", rot=-90) + t(180, 128, "FOLD BAGUD", 4, "middle", "bold", "#888", rot=90)
s1 += servo_box(89, 46, "servo 2 · hoved") + servo_box(130, 62, "servo 1 · arm")
s1 += t(146, 81, "↑ tape servoerne her, akslen fremad", 2.6, "middle", fill="#1f5fae")
s1 += tag(62, 72, "A", 6.5)
s1 += f'<rect x="60" y="86" width="90" height="15" rx="2" fill="#fff" stroke="#333" stroke-width="0.4"/>' + t(64, 96, "NAVN:", 4.5, weight="bold")
s1 += f'<circle cx="105" cy="136" r="24" fill="#fff" stroke="#333" stroke-width="0.5"/>' + t(105, 120, "MIN TONE", 3, "middle", "bold", "#666")
s1 += t(105, 140, "lim G her", 2.8, "middle", fill="#999")
for x in (85, 105, 125):
    s1 += f'<circle cx="{x}" cy="176" r="5" fill="#fff" stroke="#333" stroke-width="0.4"/>'
for (x, y) in ((53, 189), (157, 189)):
    s1 += f'<circle cx="{x}" cy="{y}" r="1.6" fill="#999"/>'
s1 += f'<line x1="56" y1="226" x2="94" y2="226" {THIN}/><line x1="116" y1="226" x2="154" y2="226" {THIN}/>'
s1 += t(105, 284, "Tip: lim kroppen på et stykke karton (fx fra en cornflakespakke) hvis papiret er for blødt.", 3, "middle", fill="#555")

# ================= sheet 2: B head, C/D arms, E drum =================
s2 = header(2, "Hoved, arme og tromme", "Klip alle dele ud. Armene foldes på midten og limes sammen — så bliver de stive.")
head_path = ("M55,54 H101 V45 A6,6 0 1,1 109,45 V54 H155 Q165,54 165,64 V129 Q165,139 155,139 H55 "
             "Q45,139 45,129 V64 Q45,54 55,54 Z")
s2 += f'<path d="{head_path}" fill="{PAPER}" stroke="{INK}" stroke-width="0.6"/>'
for x in (80, 130):
    s2 += (f'<circle cx="{x}" cy="84" r="10" fill="#fff" stroke="#333" stroke-width="0.5"/>'
           f'<circle cx="{x}" cy="84" r="1.6" fill="#e53935"/>')
s2 += t(105, 70, "prik et hul i hver prik med en blyant", 2.8, "middle", fill="#c62828")
s2 += f'<rect x="78" y="106" width="54" height="14" rx="2" fill="#fff" stroke="#333" stroke-width="0.5"/>'
for x in range(84, 132, 6):
    s2 += f'<line x1="{x}" y1="106" x2="{x}" y2="120" {THIN}/>'
s2 += f'<circle cx="105" cy="130" r="3" fill="none" stroke="{BLUE}" stroke-width="0.5" stroke-dasharray="1 0.8"/>' + t(110, 131.2, "servo 2 bagpå her", 2.5, fill="#1f5fae")
s2 += tag(56, 65, "B", 6.5)
FULL_C, _ = arm_path(150, 12)
s2 += f'<g transform="translate(20,160)"><path d="{FULL_C}" fill="{PAPER}" stroke="{INK}" stroke-width="0.6"/></g>'
s2 += f'<line x1="20" y1="160" x2="170" y2="160" {FOLD}/>'
s2 += t(96, 155.6, "TROMMESTIK", 3.6, "middle", "bold") + t(96, 167.6, "fold på midten · lim sammen", 3, "middle", fill="#555")
s2 += f'<circle cx="27" cy="154" r="3" fill="none" stroke="{BLUE}" stroke-width="0.5" stroke-dasharray="1 0.8"/>' + t(32, 155.2, "servo 1", 2.5, fill="#1f5fae")
s2 += tag(193, 160, "C", 6)
FULL_D, _ = arm_path(84, 12)
s2 += f'<g transform="translate(20,192)"><path d="{FULL_D}" fill="{PAPER}" stroke="{INK}" stroke-width="0.6" stroke-dasharray="none"/></g>'
s2 += f'<line x1="20" y1="192" x2="104" y2="192" {FOLD}/>'
s2 += t(62, 187.6, "PYNT-ARM", 3.6, "middle", "bold") + t(62, 199.6, "valgfri · tape på venstre skulder", 3, "middle", fill="#555")
s2 += tag(126, 192, "D", 6) + t(134, 193.2, "valgfri", 3.2, weight="bold", fill="#777")
s2 += t(150, 186, "foldet:", 2.8, fill="#555") + strip(150, 189, 34, 6, folded=True) + tag(190, 192, "C", 3)
s2 += f'<path d="M192,214 H200 V260 H192" {CUT}/>'
s2 += f'<path d="M12,214 H192 V260 H12 Z" fill="{PAPER}" stroke="{INK}" stroke-width="0.6"/><line x1="192" y1="214" x2="192" y2="260" {FOLD}/>'
zig = " ".join(f"{12 + i * 10},{224 if i % 2 == 0 else 250}" for i in range(19))
s2 += f'<polyline points="{zig}" fill="none" stroke="#c99a5b" stroke-width="1.2"/>'
s2 += f'<line x1="12" y1="219" x2="192" y2="219" {THIN}/><line x1="12" y1="255" x2="192" y2="255" {THIN}/>'
s2 += t(196, 237, "lim", 2.8, "middle", fill="#777", rot=90)
s2 += f'<circle cx="24" cy="237" r="7.5" fill="{PAPER}"/>' + tag(24, 237, "E", 6)
s2 += t(102, 270, "TROMME · rul til et rør, tape fliken indeni", 3.6, "middle", "bold")

# ================= sheet 3: F drum top, G badges, H decorations =================
s3 = header(3, "Tone-badge, trommeskind og pynt", "Klip KUN din egen tone-badge ud, og lim den på robottens bryst. Farvelæg pynten, og klip den ud.")
pastel = ["#ffe0b2", "#ffcdd2", "#f8bbd0", "#e1bee7", "#c5cae9", "#b3e5fc", "#c8e6c9", "#fff9c4"]
badges = [("G", "dyb"), ("C", ""), ("D", ""), ("E", ""), ("F", ""), ("G", ""), ("A", ""), ("♩", "trommer")]
for i, (n, sub) in enumerate(badges):
    cx, cy = 34 + (i % 4) * 47, 64 + (i // 4) * 50
    s3 += f'<circle cx="{cx}" cy="{cy}" r="20" fill="{pastel[i]}" stroke="{INK}" stroke-width="0.6"/>'
    s3 += t(cx, cy + (5 if not sub else 3.5), n, 16 if n != "♩" else 15, "middle", "bold")
    if sub:
        s3 += t(cx, cy + 12, sub, 3.4, "middle", "bold", "#444")
s3 += tag(66, 146, "G", 5.5) + t(74, 147.4, "tone-badges · en til hver robot", 3.2, fill="#555")
s3 += f'<circle cx="50" cy="197" r="29" fill="{PAPER}" stroke="{INK}" stroke-width="0.6"/>'
for k in range(8):
    a = k * math.pi / 4
    pts = [(29, -0.18), (35, -0.12), (35, 0.12), (29, 0.18)]
    d = " L".join(f"{50 + r * math.cos(a + o):.1f},{197 + r * math.sin(a + o):.1f}" for r, o in pts)
    s3 += f'<path d="M{d}" {CUT}/>'
s3 += f'<circle cx="50" cy="197" r="29" {FOLD}/>' + t(50, 206, "TROMMESKIND", 3.4, "middle", "bold") + tag(50, 192, "F", 6)
s3 += t(50, 242, "klip fligene ud, fold dem ned, lim på E", 2.8, "middle", fill="#555")
s3 += tag(136, 157, "H", 5.5) + t(144, 158.4, "PYNT", 4, weight="bold")
s3 += f'<path d="M120,180 C120,170 134,170 134,180 C134,170 148,170 148,180 C148,192 134,198 134,204 C134,198 120,192 120,180 Z" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
star = " ".join(f"{176 + (12 if k % 2 == 0 else 5) * math.sin(k * math.pi / 5):.1f},{186 - (12 if k % 2 == 0 else 5) * math.cos(k * math.pi / 5):.1f}" for k in range(10))
s3 += f'<polygon points="{star}" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
s3 += f'<polygon points="118,214 134,222 118,230" fill="#fff" stroke="{INK}" stroke-width="0.6"/><polygon points="150,214 134,222 150,230" fill="#fff" stroke="{INK}" stroke-width="0.6"/><circle cx="134" cy="222" r="3" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
s3 += f'<polygon points="178,208 168,226 175,226 170,242 186,220 178,220 184,208" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
s3 += f'<rect x="116" y="248" width="40" height="22" rx="3" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
for x in (124, 136, 148):
    s3 += f'<circle cx="{x}" cy="259" r="3.5" fill="none" stroke="#333" stroke-width="0.4"/>'
s3 += f'<path d="M166,258 C170,250 178,250 182,258 C186,250 194,250 198,258 C194,264 186,262 182,258 C178,262 170,264 166,258 Z" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
s3 += t(105, 286, "Tegn også selv: hår, ører, en hat, en kappe… det er DIN robot!", 3.2, "middle", fill="#555")

# ================= sheet 4: parts & tools =================
s4 = header(4, "Dele og værktøj", "Tjek, at du har det hele, før du starter.")


def cell(x, y, w, h, art, qty, label, letter=None):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="#fff" stroke="#bbb" stroke-width="0.4"/>'
    out += art
    if qty:
        out += t(x + w - 3, y + 7, qty, 4.6, "end", "bold")
    out += t(x + w / 2, y + h - 3.5, label, 3, "middle", fill="#444")
    if letter:
        out += tag(x + 6.5, y + 6.5, letter, 4.5)
    return out


s4 += t(12, 44, "Papirdele", 5, weight="bold")
W, H = 44, 40
heart = '<path d="M-9,-2 C-9,-8 -1,-8 -1,-2 C-1,-8 7,-8 7,-2 C7,4 -1,7 -1,10 C-1,7 -9,4 -9,-2 Z" fill="#fff" stroke="#111" stroke-width="0.5" transform="translate(-5,-1) scale(0.8)"/>'
star_small = '<polygon points="12,-9 14,-3 20,-3 15,1 17,7 12,3 7,7 9,1 4,-3 10,-3" fill="#fff" stroke="#111" stroke-width="0.5" transform="translate(-6,0) scale(0.9)"/>'
paper = [
    ("A", body_icon(0, -1, 0.13), "krop"),
    ("B", head_icon(0, 2, 0.2), "hoved"),
    ("C", strip(-17, -4, 30, 6), "trommestik"),
    ("D", strip(-12, -4, 20, 6), "pynt-arm (valgfri)"),
    ("E", f'<rect x="-17" y="-6" width="34" height="10" fill="#fff" stroke="{INK}" stroke-width="0.5"/><polyline points="-17,-3 -13,2 -9,-3 -5,2 -1,-3 3,2 7,-3 11,2 15,-3 17,-1" fill="none" stroke="#c99a5b" stroke-width="0.8"/>', "tromme"),
    ("F", f'<circle cx="0" cy="-1" r="10" fill="#fff" stroke="{INK}" stroke-width="0.5"/>', "trommeskind"),
    ("G", f'<circle cx="0" cy="-1" r="10" fill="#c8e6c9" stroke="{INK}" stroke-width="0.5"/>' + t(0, 2.6, "C", 10, "middle", "bold"), "din tone"),
    ("H", heart + star_small, "pynt"),
]
for i, (L, art, label) in enumerate(paper):
    x, y = 12 + (i % 4) * (W + 2.7), 48 + (i // 4) * (H + 3)
    s4 += cell(x, y, W, H, g(art, x + W / 2, y + H / 2 - 1), "1×", label, L)

s4 += t(12, 146, "Elektronik", 5, weight="bold")
EW = 36.4
elec = [
    (servo_icon(-4, 2, 1.0), "2×", "servo SG90"),
    (led_icon(-5, -4, 1.2) + led_icon(5, -4, 1.2), "2×", "LED"),
    (microbit_icon(0, -6, 0.75, {(1, 1), (1, 3), (3, 0), (3, 4), (4, 1), (4, 2), (4, 3)}) + f'<rect x="-14" y="2" width="28" height="8" rx="1.5" fill="#e3f2fd" stroke="{INK}" stroke-width="0.45"/>', "1×", "micro:bit + shield"),
    (wire_icon(0, -4, 1, "#e53935") + wire_icon(0, 4, 1, "#43a047"), "2×", "ledninger"),
    (battery_icon(0, 0, 1.1), "1×", "batteripakke"),
]
for i, (art, q, label) in enumerate(elec):
    x, y = 12 + i * (EW + 1.0), 150
    s4 += cell(x, y, EW, H, g(art, x + EW / 2, y + H / 2 - 1), q, label)

s4 += t(12, 206, "Værktøj", 5, weight="bold")
TW = 29.8
pens = "".join(f'<rect x="{-8 + k * 4.5}" y="-8" width="3" height="16" rx="1" fill="{c}" stroke="{INK}" stroke-width="0.35"/>' for k, c in enumerate(("#e53935", "#fdd835", "#43a047", "#1e88e5")))
tools = [(scissors(0, 0, 1.3), "saks"), (tape_roll(0, 0, 1.2), "tape"), (glue_stick(0, 2, 1), "limstift"),
         (pencil(-12, 0, 0.85), "blyant"), (eraser(0, 0, 1.2), "viskelæder"), (pens, "farver")]
for i, (art, label) in enumerate(tools):
    x, y = 12 + i * (TW + 1.44), 210
    s4 += cell(x, y, TW, 30, g(art, x + TW / 2, y + 12), "", label)

ty = 252
s4 += t(12, ty, "Ledninger til sensor-shieldet", 4.4, weight="bold")
rows = [("Servo 1 · arm", "P1", "brun → G · rød → V · orange → S"), ("Servo 2 · hoved", "P2", "brun → G · rød → V · orange → S"),
        ("LED-øje venstre", "P8", "langt ben → S · kort ben → G"), ("LED-øje højre", "P13", "langt ben → S · kort ben → G")]
for k, (a, p, c) in enumerate(rows):
    y = ty + 6.5 + k * 6.6
    s4 += f'<rect x="12" y="{y - 4.6}" width="186" height="6.4" fill="{"#f3ece0" if k % 2 == 0 else "#fff"}"/>'
    s4 += t(15, y, a, 3.3, weight="bold") + t(66, y, p, 3.5, weight="bold", fill="#1f5fae") + t(84, y, c, 3.2, fill="#333")
s4 += f'<line x1="12" y1="290" x2="62" y2="290" stroke="{INK}" stroke-width="0.8"/>' + "".join(
    f'<line x1="{12 + k * 10}" y1="287.5" x2="{12 + k * 10}" y2="292.5" stroke="{INK}" stroke-width="0.5"/>' for k in range(6))
s4 += t(66, 291.2, "Printtjek: denne streg skal være præcis 5 cm. Print i 100 % / \"faktisk størrelse\".", 3, fill="#333")

# ================= sheets 5-6: picture steps =================
BW, BH = 91, 119
POS = [(12, 38), (107, 38), (12, 162), (107, 162)]


def step_box(i, n, caption, art):
    bx, by = POS[i]
    out = f'<rect x="{bx}" y="{by}" width="{BW}" height="{BH}" rx="3" fill="#fff" stroke="#c99a5b" stroke-width="0.6"/>'
    out += f'<text x="{bx + 5}" y="{by + 15}" {FONT} font-size="15" font-weight="bold" fill="{INK}">{n}</text>'
    out += f'<line x1="{bx + 4}" y1="{by + BH - 14}" x2="{bx + BW - 4}" y2="{by + BH - 14}" stroke="#eee" stroke-width="0.4"/>'
    out += t(bx + BW / 2, by + BH - 6, caption, 3.3, "middle", "bold", "#333")
    out += f'<g transform="translate({bx},{by})">{art}</g>'
    return out


# 1 cut
a1 = f'<rect x="5" y="24" width="30" height="44" fill="#fff" stroke="#bbb" stroke-width="0.4"/>'
a1 += body_icon(20, 47, 0.145) + tag(9.5, 28.5, "A", 3)
a1 += scissors(40, 44, 1.0, 180)
thumbs = [("A", body_icon(0, 0, 0.08)), ("B", head_icon(0, 1, 0.11)), ("C", strip(-8, -2, 12, 4)), ("D", strip(-6, -2, 8, 4)),
          ("E", f'<rect x="-10" y="-3" width="20" height="6" fill="#fff" stroke="{INK}" stroke-width="0.45"/>'),
          ("F", f'<circle r="5" fill="#fff" stroke="{INK}" stroke-width="0.45"/>'),
          ("G", f'<circle r="5" fill="#c8e6c9" stroke="{INK}" stroke-width="0.45"/>'),
          ("H", f'<polygon points="0,-5 1.5,-1.5 5,-1.5 2.2,0.8 3.2,4.5 0,2.3 -3.2,4.5 -2.2,0.8 -5,-1.5 -1.5,-1.5" fill="#fff" stroke="{INK}" stroke-width="0.4"/>')]
for k, (L, art) in enumerate(thumbs):
    cx, cy = 64 + (k % 2) * 19, 28 + (k // 2) * 20
    a1 += g(art, cx, cy + 3) + tag(cx - 8, cy - 4, L, 2.8)
# 2 fold
a2 = body_icon(26, 46, 0.17)
a2 += curved_arrow(10, 36, 2, 28, 10, 23) + curved_arrow(42, 36, 50, 28, 42, 23)
a2 += f'<polyline points="13,92 19,84 33,84 39,92" fill="none" stroke="{INK}" stroke-width="0.9"/>' + t(26, 99, "90°", 3.5, "middle", "bold")
a2 += f'<path d="M15,90 A6,6 0 0,1 19,84" fill="none" stroke="{BLUE}" stroke-width="0.5"/>'
a2 += t(70, 25, "C · D", 3.2, "middle", "bold")
a2 += strip(56, 30, 26, 8) + curved_arrow(60, 42, 52, 48, 60, 53)
a2 += strip(56, 56, 26, 4, folded=True) + glue_stick(80, 76, 0.9, 30) + ok_mark(66, 90)
# 3 eyes
a3 = head_icon(25, 50, 0.3)
a3 += pencil(20, 44, 0.9, -40)
a3 += eraser(17.5, 72, 0.7)
a3 += f'<line x1="66" y1="26" x2="66" y2="66" stroke="{INK}" stroke-width="1.2"/>' + tag(66, 72, "B", 3)
a3 += led_icon(72, 42, 1.3, -90, False) + arrow(90, 33, 76, 33)
a3 += led_icon(34, 78, 1.5, 0, False)
a3 += t(30, 101, "+ langt", 2.9, "end", "bold", "#333") + t(38, 95, "− kort", 2.9, "start", "bold", "#333")
a3 += t(78, 96, "2×", 6, "middle", "bold")
# 4 servo-center
a4 = f'<path d="M10,24 H42 V44 H10 Z" fill="#fff" stroke="{INK}" stroke-width="0.6"/><path d="M6,46 H46 L43,50 H9 Z" fill="#ddd" stroke="{INK}" stroke-width="0.5"/>'
a4 += t(26, 36, "servo-center", 3.1, "middle", "bold", BLUE)
a4 += f'<path d="M46,40 C54,40 52,48 60,48" fill="none" stroke="#333" stroke-width="0.8"/>'
a4 += microbit_icon(72, 46, 0.9, {(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (0, 2), (1, 2), (3, 2), (4, 2)})
a4 += arrow(46, 60, 46, 68)
a4 += servo_icon(26, 88, 1.1) + servo_icon(62, 88, 1.1)
for cx in (26, 62):
    a4 += f'<path d="M{cx - 11},88 A11,11 0 0,1 {cx},77" fill="none" stroke="{BLUE}" stroke-width="0.5" stroke-dasharray="1 0.8"/>' + t(cx - 10, 78.5, "90°", 2.8, "middle", "bold", BLUE)
a4 += ok_mark(84, 74)
# 5 head
a5 = (f'<path d="M28,100 V88 Q28,82 34,82 H38 V76 H58 V82 H62 Q68,82 68,88 V100" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
      f'<rect x="32" y="73" width="32" height="12.4" rx="1" fill="#dbe9fb" stroke="{BLUE}" stroke-width="0.4" stroke-dasharray="1.2 0.8"/>')
a5 += servo_icon(41.5, 79.2, 1) + tape(38, 81, 13, 4, -25) + tape(58, 81, 13, 4, 25)
a5 += head_icon(48, 40, 0.26)
a5 += arrow(41.5, 54, 41.5, 63)
a5 += tag(16, 30, "B", 3.2) + tag(20, 94, "A", 3.2)
# 6 arm
a6 = (f'<path d="M10,100 V40 Q10,32 18,32 H50 Q58,32 58,40 V100" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
      f'<rect x="31" y="36" width="32" height="12.4" rx="1" fill="#dbe9fb" stroke="{BLUE}" stroke-width="0.4" stroke-dasharray="1.2 0.8"/>')
a6 += g(f'<path d="M0,-3 H40 A4,4 0 1,1 40,3 H0 Z" fill="#fff" stroke="{INK}" stroke-width="0.6"/>', 40.5, 42.2, 1, 60)
a6 += servo_icon(40.5, 42.2, 1, 150, tabs=False)
a6 += tape(48, 36.5, 16, 4, -8) + tape(48, 48, 16, 4, 8)
a6 += f'<path d="M54,42.2 A13.5,13.5 0 0,1 47.2,53.9" fill="none" stroke="{BLUE}" stroke-width="0.6"/>'
a6 += tag(20, 46, "A", 3.2) + tag(68, 84, "C", 3.2) + ok_mark(82, 98)
# 7 drum
a7 = f'<rect x="8" y="26" width="34" height="10" fill="#fff" stroke="{INK}" stroke-width="0.5"/>' + tag(8, 24, "E", 3)
a7 += curved_arrow(26, 40, 14, 48, 22, 53)
a7 += drum_icon(26, 70, 0.75, skin=False)
a7 += f'<ellipse cx="44" cy="52" rx="8" ry="3" fill="{PAPER}" stroke="{INK}" stroke-width="0.45"/>' + tag(52, 48, "F", 3) + arrow(40, 55.5, 32, 61)
a7 += body_icon(68, 66, 0.15, flaps=False)
a7 += f'<line x1="78" y1="54" x2="81" y2="82" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"/>'
a7 += drum_icon(83, 90, 0.36)
a7 += t(88, 74, "♪", 6, "middle", "bold", BLUE)
# 8 connect
a8 = shield_icon(46, 54, 1.05)
a8 += servo_icon(24, 22, 0.55)
a8 += (f'<path d="M23,26 C23,32 24,34 24,43" fill="none" stroke="#6d4c41" stroke-width="0.8"/>'
       f'<path d="M25,26 C25,32 26,36 26,38" fill="none" stroke="#e53935" stroke-width="0.8"/>'
       f'<path d="M27,26 C28,30 28,32 25.5,33" fill="none" stroke="#fb8c00" stroke-width="0.8"/>')
a8 += led_icon(72, 22, 1.0) + f'<path d="M70.7,36 C70,40 70,41 70.8,44" fill="none" stroke="#333" stroke-width="0.6"/><path d="M73.3,32 C76,36 76,46 71.5,54" fill="none" stroke="#333" stroke-width="0.6"/>'
a8 += battery_icon(78, 90, 0.9) + f'<path d="M70,90 C60,90 62,74 56,72" fill="none" stroke="#333" stroke-width="0.7"/>'
a8 += microbit_icon(26, 90, 0.8, {(0, 1), (0, 3), (2, 0), (2, 4), (3, 1), (3, 2), (3, 3)}) + t(41, 93, "♪ ♫", 6, "start", "bold", BLUE)
a8 += ok_mark(86, 18)

# ================= sheet 5: servo close-up =================
sv = header(5, "Sådan sidder servoerne", "Servoen ligger fladt på papiret, og akslen peger mod dig.")
# box 1: parts
b1 = servo_icon(36, 58, 2.4)
b1 += f'<path d="M58,73 V92 M61,73 V92 M64,73 V92" stroke="#6d4c41" stroke-width="0" fill="none"/>'
b1 += '<path d="M56,73 C56,82 54,86 54,92" fill="none" stroke="#6d4c41" stroke-width="1"/><path d="M59,73 C59,82 57,86 57,92" fill="none" stroke="#e53935" stroke-width="1"/><path d="M62,73 C62,82 60,86 60,92" fill="none" stroke="#fb8c00" stroke-width="1"/>'
b1 += f'<line x1="44" y1="26" x2="39" y2="31" stroke="{INK}" stroke-width="0.35"/>' + t(45, 25.5, "horn", 3.4, weight="bold")
b1 += f'<line x1="56" y1="46" x2="42" y2="56" stroke="{INK}" stroke-width="0.35"/>' + t(57, 45, "aksel (drejer)", 3.4, weight="bold")
b1 += f'<line x1="12" y1="78" x2="16" y2="62" stroke="{INK}" stroke-width="0.35"/>' + t(6, 82, "øre", 3.4, weight="bold")
b1 += t(63, 96, "kabel → shield", 3, fill="#555")
# box 2: side view
b2 = f'<rect x="18" y="24" width="3" height="78" fill="{PAPER}" stroke="{INK}" stroke-width="0.5"/>' + t(19.5, 108, "A · papir", 3, "middle", "bold")
b2 += f'<rect x="21" y="44" width="34" height="19" rx="1.5" fill="#9cc3f5" stroke="{BLUE}" stroke-width="0.6"/>' + t(38, 55, "servo", 3.2, "middle", "bold", "#1f5fae")
b2 += f'<rect x="55" y="47" width="5" height="6" fill="#fff" stroke="{INK}" stroke-width="0.5"/>'
b2 += f'<rect x="60" y="36" width="2.5" height="24" rx="1" fill="#fff" stroke="{INK}" stroke-width="0.5"/>' + t(61, 33, "horn", 3, "middle", "bold")
b2 += f'<rect x="62.5" y="44" width="2.5" height="56" fill="{PAPER}" stroke="{INK}" stroke-width="0.5"/>' + tag(70, 92, "C", 3.2)
b2 += tape(21, 44.5, 10, 3, -50) + tape(21, 62.5, 10, 3, 50)
b2 += arrow(88, 70, 72, 70) + t(86, 78, "du kigger herfra", 2.6, "end", fill="#555")
# box 3: arm front view
b3 = (f'<path d="M8,104 V40 Q8,30 18,30 H52 Q62,30 62,40 V104" fill="#fff" stroke="{INK}" stroke-width="0.6"/>'
      f'<rect x="31" y="35" width="32" height="12.4" rx="1" fill="#dbe9fb" stroke="{BLUE}" stroke-width="0.4" stroke-dasharray="1.2 0.8"/>')
ghost, _ = arm_path(46, 3)
b3 += g(f'<path d="{ghost}" fill="none" stroke="#999" stroke-width="0.5" stroke-dasharray="1.5 1"/>', 40.5, 41.2, 1, 60)
b3 += g(f'<path d="{ghost}" fill="#fff" stroke="{INK}" stroke-width="0.6"/>', 40.5, 41.2, 1, 90)
b3 += servo_icon(40.5, 41.2, 1, 180, tabs=False) + tape(48, 35.5, 16, 4, -8) + tape(48, 47, 16, 4, 8)
b3 += curved_arrow(42, 80, 54, 84, 62, 78, color=BLUE) + t(66, 76, "slag", 3, fill="#1f5fae", weight="bold")
b3 += drum_icon(76, 92, 0.42)
b3 += t(44, 106, "90° = lige ned", 3, "middle", "bold") + tag(36, 92, "C", 3.2)
# box 4: head front view
b4 = (f'<path d="M24,104 V92 Q24,86 30,86 H36 V80 H56 V86 H62 Q68,86 68,92 V104" fill="#fff" stroke="{INK}" stroke-width="0.6"/>')
b4 += servo_icon(41.5, 82, 1) + tape(38, 84, 13, 4, -25) + tape(58, 84, 13, 4, 25)
b4 += f'<g opacity="0.8">{head_icon(44, 56, 0.3)}</g>'
b4 += f'<circle cx="41.5" cy="67" r="3" fill="none" stroke="{BLUE}" stroke-width="0.7" stroke-dasharray="1 0.8"/>'
b4 += f'<line x1="44.5" y1="68" x2="66" y2="76" stroke="{BLUE}" stroke-width="0.35"/>' + t(67, 77.5, "bagsiden af B", 2.6, fill="#1f5fae")
b4 += curved_arrow(22, 30, 16, 40, 20, 50) + curved_arrow(70, 30, 76, 40, 72, 50) + tag(80, 60, "B", 3.2)
sv += step_box(0, "", "Servoens dele", b1) + step_box(1, "", "Set fra siden", b2)
sv += step_box(2, "", "Arm: C hænger ned og svinger", b3) + step_box(3, "", "Hoved: B tapes på hornet og vipper", b4)
sv += f'<rect x="12" y="284" width="186" height="9" rx="2" fill="#f3ece0"/>' + t(105, 290, "1 servo fladt · 2 servo-center · 3 tape C og B på hornet", 3.4, "middle", "bold")

s5 = header(6, "Byg din robot", "Følg billederne, trin for trin.")
s5 += step_box(0, 1, "Klip delene A–H ud", a1) + step_box(1, 2, "Fold A bagud · fold og lim C + D", a2)
s5 += step_box(2, 3, "Prik huller i B · LED'er ind bagfra", a3) + step_box(3, 4, "Kør servo-center → begge servoer på 90°", a4)
s6 = header(7, "Byg din robot", "Følg billederne, trin for trin.")
s6 += step_box(0, 5, "Servo på halsen · B på servo-armen", a5) + step_box(1, 6, "Servo på skulderen · C peger skråt ned", a6)
s6 += step_box(2, 7, "Rul E · lim F på · stil den ved benet", a7) + step_box(3, 8, "Forbind · tænd · spil!", a8)
s6 += t(105, 290, "Vakler robotten, eller genstarter micro:bit'en? Brug en batteripakke.", 3.2, "middle", fill="#555")

title = "Robot orchestra template A4" if LANG == "en" else "Robot-orkester skabelon A4"
html = f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>@page {{ size: A4; margin: 0; }} html,body {{ margin:0; padding:0; }}
.page {{ width:210mm; height:297mm; page-break-after: always; break-after: page; overflow:hidden; }}
.page:last-child {{ page-break-after: auto; break-after: auto; }} svg {{ display:block; }}</style></head>
<body>{page(s1)}{page(s2)}{page(s3)}{page(s4)}{page(sv)}{page(s5)}{page(s6)}</body></html>"""
OUT.write_text(html, encoding="utf-8")
print("wrote", OUT)
