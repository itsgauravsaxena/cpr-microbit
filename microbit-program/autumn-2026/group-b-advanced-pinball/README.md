# Group B — Advanced: Mini Pinball Machine

Ages 8-10, already comfortable with MakeCode basics. 1-hour sessions, physical micro:bits, Tinkercad for 3D design.

A 10-week capstone building a small tabletop pinball machine. Everything stays at a simple, block-coding level — nothing fancy, just lots of small wins. The term runs in **three easy phases**:

1. **Weeks 1–4 · Code the micro:bit** — the pinball "brain": scoring, a flipper trigger, multi-sensor scoring and game-over (with an optional radio scoreboard).
2. **Weeks 5–8 · 3D-design the parts** — start with a whole week *just playing* in Tinkercad (great for first-timers), then design a bumper and a sensor mount, and finish/print everything.
3. **Weeks 9–10 · Build & finish** — assemble, playtest, polish, decorate, and end with a mini tournament.

## What you’ll build

<div style="text-align:center;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 320 470" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif" role="img" aria-label="An animated mini pinball machine">
  <!-- cabinet -->
  <rect x="16" y="16" width="288" height="438" rx="24" fill="#33406b" stroke="#c8a24a" stroke-width="3"/>
  <!-- backbox / title -->
  <rect x="38" y="28" width="244" height="56" rx="10" fill="#0f1419"/>
  <text x="58" y="64" font-size="24" fill="#ffd24a" font-weight="800">PINBALL</text>
  <!-- micro:bit scoreboard with a pulsing heart -->
  <g transform="translate(232,36)">
    <rect x="0" y="0" width="42" height="40" rx="6" fill="#12191f" stroke="#c8a24a" stroke-width="1.5"/>
    <g fill="#3a2323">
      <rect x="6" y="6" width="5" height="5" rx="1"/><rect x="13" y="6" width="5" height="5" rx="1"/><rect x="20" y="6" width="5" height="5" rx="1"/><rect x="27" y="6" width="5" height="5" rx="1"/><rect x="34" y="6" width="5" height="5" rx="1"/>
      <rect x="6" y="13" width="5" height="5" rx="1"/><rect x="13" y="13" width="5" height="5" rx="1"/><rect x="20" y="13" width="5" height="5" rx="1"/><rect x="27" y="13" width="5" height="5" rx="1"/><rect x="34" y="13" width="5" height="5" rx="1"/>
      <rect x="6" y="20" width="5" height="5" rx="1"/><rect x="13" y="20" width="5" height="5" rx="1"/><rect x="20" y="20" width="5" height="5" rx="1"/><rect x="27" y="20" width="5" height="5" rx="1"/><rect x="34" y="20" width="5" height="5" rx="1"/>
      <rect x="6" y="27" width="5" height="5" rx="1"/><rect x="13" y="27" width="5" height="5" rx="1"/><rect x="20" y="27" width="5" height="5" rx="1"/><rect x="27" y="27" width="5" height="5" rx="1"/><rect x="34" y="27" width="5" height="5" rx="1"/>
    </g>
    <g fill="#ff4d4d">
      <animate attributeName="opacity" values="1;0.3;1" dur="1.1s" repeatCount="indefinite"/>
      <rect x="13" y="6" width="5" height="5" rx="1"/><rect x="27" y="6" width="5" height="5" rx="1"/>
      <rect x="6" y="13" width="5" height="5" rx="1"/><rect x="13" y="13" width="5" height="5" rx="1"/><rect x="20" y="13" width="5" height="5" rx="1"/><rect x="27" y="13" width="5" height="5" rx="1"/><rect x="34" y="13" width="5" height="5" rx="1"/>
      <rect x="13" y="20" width="5" height="5" rx="1"/><rect x="20" y="20" width="5" height="5" rx="1"/><rect x="27" y="20" width="5" height="5" rx="1"/>
      <rect x="20" y="27" width="5" height="5" rx="1"/>
    </g>
  </g>

  <!-- playfield -->
  <rect x="38" y="92" width="244" height="346" rx="14" fill="#123a24"/>
  <rect x="38" y="92" width="244" height="346" rx="14" fill="none" stroke="#1d5637" stroke-width="2"/>
  <!-- plunger lane -->
  <rect x="258" y="150" width="6" height="260" rx="3" fill="#0e2b1b"/>

  <!-- bumpers (pulsing) -->
  <g>
    <circle cx="96" cy="168" r="22" fill="#e5484d"/><circle cx="96" cy="168" r="12" fill="#ff8a8d">
      <animate attributeName="r" values="12;15;12" dur="1.3s" repeatCount="indefinite"/></circle>
  </g>
  <g>
    <circle cx="205" cy="152" r="22" fill="#3a7bd5"/><circle cx="205" cy="152" r="12" fill="#7fb2ff">
      <animate attributeName="r" values="12;15;12" dur="1.6s" repeatCount="indefinite"/></circle>
  </g>
  <g>
    <circle cx="150" cy="230" r="22" fill="#f2a03d"/><circle cx="150" cy="230" r="12" fill="#ffc987">
      <animate attributeName="r" values="12;15;12" dur="1.9s" repeatCount="indefinite"/></circle>
  </g>

  <!-- flippers (V-shape, flicking) -->
  <g transform="translate(92,406)">
    <rect x="0" y="-8" width="62" height="16" rx="8" fill="#ffd24a"/>
    <animateTransform attributeName="transform" type="rotate" values="-25;-48;-25" dur="1.1s" repeatCount="indefinite" additive="sum"/>
  </g>
  <g transform="translate(228,406)">
    <rect x="-62" y="-8" width="62" height="16" rx="8" fill="#ffd24a"/>
    <animateTransform attributeName="transform" type="rotate" values="25;48;25" dur="1.1s" repeatCount="indefinite" additive="sum"/>
  </g>

  <!-- the ball -->
  <circle r="8" fill="#eef3f7" stroke="#9fb0bd" stroke-width="1.5">
    <animateMotion dur="6s" repeatCount="indefinite" rotate="0"
      path="M261,405 L261,120 C232,104 175,120 160,150 C130,180 108,150 96,168 C118,205 185,178 205,152 C232,192 168,214 150,230 C150,300 150,360 158,398 L261,405 Z"/>
  </circle>
</svg>
</div>

*Your finished mini pinball machine — bumpers, flippers, a ball, and a micro:bit keeping score.*

## Reference builds
- ["3D Printed Pinball" by ctrl design](https://pinshape.com/items/24228-3d-printed-pinball) — micro:bit/Arduino-based, scalable difficulty, free STL files
- micro:bit + PinBox 3000 cardboard pinball (TechnoChic) — reference for driving lights, sound, and a scoreboard from a micro:bit on a simple frame

## Your 10-week build adventure

<div style="text-align:center;overflow-x:auto;" markdown="0">
<svg viewBox="0 0 960 290" width="100%" style="max-width:900px;height:auto;" role="img" aria-label="A map of the 10-week pinball build journey" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,sans-serif">
<path d="M100 72 H860 Q922 72 922 141 Q922 210 860 210 H100" fill="none" stroke="#9aa4d4" stroke-width="3" stroke-dasharray="7 7" stroke-linecap="round"/>
<circle cx="100" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="100" y="85" text-anchor="middle" font-size="34">🚀</text><text x="100" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="100" font-weight="700">Wk 1</tspan><tspan x="100" dy="15" font-size="11">Kickoff</tspan></text>
<circle cx="290" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="290" y="85" text-anchor="middle" font-size="34">💯</text><text x="290" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="290" font-weight="700">Wk 2</tspan><tspan x="290" dy="15" font-size="11">Scoring</tspan></text>
<circle cx="480" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="480" y="85" text-anchor="middle" font-size="34">🎯</text><text x="480" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="480" font-weight="700">Wk 3</tspan><tspan x="480" dy="15" font-size="11">Launcher</tspan></text>
<circle cx="670" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="670" y="85" text-anchor="middle" font-size="34">💡</text><text x="670" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="670" font-weight="700">Wk 4</tspan><tspan x="670" dy="15" font-size="11">Multi-sensor</tspan></text>
<circle cx="860" cy="72" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="860" y="85" text-anchor="middle" font-size="34">🧊</text><text x="860" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="860" font-weight="700">Wk 5</tspan><tspan x="860" dy="15" font-size="11">Tinkercad play</tspan></text>
<circle cx="860" cy="210" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="860" y="223" text-anchor="middle" font-size="34">🧩</text><text x="860" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="860" font-weight="700">Wk 6</tspan><tspan x="860" dy="15" font-size="11">Bumper</tspan></text>
<circle cx="670" cy="210" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="670" y="223" text-anchor="middle" font-size="34">🔧</text><text x="670" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="670" font-weight="700">Wk 7</tspan><tspan x="670" dy="15" font-size="11">Sensor Mount</tspan></text>
<circle cx="480" cy="210" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="480" y="223" text-anchor="middle" font-size="34">🖨️</text><text x="480" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="480" font-weight="700">Wk 8</tspan><tspan x="480" dy="15" font-size="11">Print prep</tspan></text>
<circle cx="290" cy="210" r="32" fill="#fff3d6" stroke="#f9a825" stroke-width="2.5"/><text x="290" y="223" text-anchor="middle" font-size="34">🛠️</text><text x="290" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="290" font-weight="700">Wk 9</tspan><tspan x="290" dy="15" font-size="11">Assemble</tspan></text>
<circle cx="100" cy="210" r="32" fill="#fff3d6" stroke="#f9a825" stroke-width="2.5"/><text x="100" y="223" text-anchor="middle" font-size="34">🏆</text><text x="100" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="100" font-weight="700">Wk 10</tspan><tspan x="100" dy="15" font-size="11">Showcase</tspan></text>
</svg>
</div>

*Phase 1 (weeks 1–4): micro:bit coding · Phase 2 (weeks 5–8): 3D design · Phase 3 (weeks 9–10): build & finish.*

## Weeks

### Phase 1 · Code the micro:bit
| Week | Focus |
|---|---|
| [1](./week-01-kickoff/README.md) | Kickoff & recap |
| [2](./week-02-scoring-basics/README.md) | Program scoring basics |
| [3](./week-03-launcher-trigger/README.md) | Program the launcher/flipper trigger |
| [4](./week-04-multi-sensor-scoring/README.md) | Multi-sensor scoring + game over |

### Phase 2 · 3D-design the parts
| Week | Focus |
|---|---|
| [5](./week-05-tinkercad-basics/README.md) | Tinkercad first steps (just play) |
| [6](./week-06-tinkercad-playfield/README.md) | Design a playfield bumper |
| [7](./week-07-sensor-mount/README.md) | Design a sensor mount |
| [8](./week-08-design-finish/README.md) | Finish & print prep |

### Phase 3 · Build & finish
| Week | Focus |
|---|---|
| [9](./week-09-assembly-playtest/README.md) | Assembly + first playtest |
| [10](./week-10-showcase-tournament/README.md) | Polish & showcase / tournament |

## Materials checklist
- Micro:bits (1-2 per kid if you try the radio scoreboard) + USB cables or battery packs
- Tinkercad accounts (needed from week 5)
- Switches or light sensors for scoring, buzzer/speaker (built into V2 boards), optional servos for a moving flipper
- 3D printer access from week 6 onward — queue the kids' parts as they are designed (weeks 6–8) so they are printed in time for assembly in week 9
- Pre-designed/precision cabinet and flipper mechanism files ready before week 6, so kids' own design time stays focused on their own simple parts
