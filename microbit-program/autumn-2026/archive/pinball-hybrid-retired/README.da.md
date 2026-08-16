# Gruppe B — Avanceret: Mini-flippermaskine

!!! warning "Arkiveret — kører ikke i efteråret 2026"
    Dette var et hybridforløb med micro:bit + 3D-design (flippermaskine). Efterårssæsonen 2026
    kører nu i stedet to rene micro:bit-hold ([Beginners](../../microbit-beginners/README.md) og
    [Pro](../../microbit-pro/README.md)). Materialet gemmes her til reference og genbrug.


Alder 8-10, allerede fortrolige med det grundlæggende i MakeCode. Sessioner på 1 time, fysiske micro:bits, Tinkercad til 3D-design.

Et 10-ugers afgangsprojekt, hvor der bygges en lille flippermaskine til bordet. Alt holdes på et simpelt blok-kodningsniveau — ikke noget indviklet, bare mange små sejre. Sæsonen kører i **tre nemme faser**:

1. **Uge 1–4 · Kod micro:bitten** — flippermaskinens "hjerne": pointtælling, en flipper-udløser, pointtælling med flere sensorer og game-over (med en valgfri radioresultattavle).
2. **Uge 5–8 · 3D-design delene** — start med en hel uge, hvor I *bare leger* i Tinkercad (perfekt til førstegangsdesignere), design derefter en bumper og en sensorholder, og færdiggør/print det hele.
3. **Uge 9–10 · Byg & afslut** — saml, playtest, finpuds, pynt, og slut af med en mini-turnering.

## Hvad I bygger

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

*Jeres færdige mini-flippermaskine — bumpere, flippere, en bold og en micro:bit, der holder styr på pointene.*

## Maskinens dele (navne)

Brug disse navne, så alle mener det samme:

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 730 500" width="100%" style="max-width:660px;height:auto;" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif" role="img" aria-label="Labeled diagram of the pinball machine parts">
  <!-- ===== machine (static), shifted right to leave room for labels ===== -->
  <g transform="translate(160,20)">
    <rect x="16" y="16" width="288" height="438" rx="24" fill="#33406b" stroke="#c8a24a" stroke-width="3"/>
    <rect x="38" y="28" width="244" height="56" rx="10" fill="#0f1419"/>
    <text x="58" y="64" font-size="24" fill="#ffd24a" font-weight="800">PINBALL</text>
    <!-- micro:bit scoreboard, static heart -->
    <g transform="translate(232,36)">
      <rect x="0" y="0" width="42" height="40" rx="6" fill="#12191f" stroke="#c8a24a" stroke-width="1.5"/>
      <g fill="#ff4d4d">
        <rect x="13" y="6" width="5" height="5" rx="1"/><rect x="27" y="6" width="5" height="5" rx="1"/>
        <rect x="6" y="13" width="5" height="5" rx="1"/><rect x="13" y="13" width="5" height="5" rx="1"/><rect x="20" y="13" width="5" height="5" rx="1"/><rect x="27" y="13" width="5" height="5" rx="1"/><rect x="34" y="13" width="5" height="5" rx="1"/>
        <rect x="13" y="20" width="5" height="5" rx="1"/><rect x="20" y="20" width="5" height="5" rx="1"/><rect x="27" y="20" width="5" height="5" rx="1"/>
        <rect x="20" y="27" width="5" height="5" rx="1"/>
      </g>
    </g>
    <rect x="38" y="92" width="244" height="346" rx="14" fill="#123a24"/>
    <rect x="38" y="92" width="244" height="346" rx="14" fill="none" stroke="#1d5637" stroke-width="2"/>
    <rect x="258" y="150" width="6" height="260" rx="3" fill="#0e2b1b"/>
    <!-- bumpers -->
    <circle cx="96" cy="168" r="22" fill="#e5484d"/><circle cx="96" cy="168" r="13" fill="#ff8a8d"/>
    <circle cx="205" cy="152" r="22" fill="#3a7bd5"/><circle cx="205" cy="152" r="13" fill="#7fb2ff"/>
    <circle cx="150" cy="230" r="22" fill="#f2a03d"/><circle cx="150" cy="230" r="13" fill="#ffc987"/>
    <!-- flippers (static V) -->
    <g transform="translate(92,406) rotate(-25)"><rect x="0" y="-8" width="62" height="16" rx="8" fill="#ffd24a"/></g>
    <g transform="translate(228,406) rotate(25)"><rect x="-62" y="-8" width="62" height="16" rx="8" fill="#ffd24a"/></g>
    <!-- ball (static) -->
    <circle cx="232" cy="120" r="8" fill="#eef3f7" stroke="#9fb0bd" stroke-width="1.5"/>
  </g>

  <!-- ===== labels + leader lines (absolute coords) ===== -->
  <g stroke="#8a94a6" stroke-width="1.5" fill="none">
    <polyline points="150,58 176,52"/>            <!-- Cabinet -->
    <polyline points="150,278 224,278"/>          <!-- Playfield -->
    <polyline points="150,196 250,196"/>          <!-- Bumpers -->
    <polyline points="150,432 252,428"/>          <!-- Flippers -->
    <polyline points="470,72 428,72"/>            <!-- Scoreboard -->
    <polyline points="470,140 402,140"/>          <!-- Ball -->
    <polyline points="470,300 426,320"/>          <!-- Launch lane -->
    <polyline points="470,432 312,442"/>          <!-- Drain -->
  </g>
  <g fill="#8a94a6">
    <circle cx="176" cy="52" r="3"/><circle cx="224" cy="278" r="3"/><circle cx="250" cy="196" r="3"/><circle cx="252" cy="428" r="3"/>
    <circle cx="428" cy="72" r="3"/><circle cx="402" cy="140" r="3"/><circle cx="426" cy="320" r="3"/><circle cx="312" cy="442" r="3"/>
  </g>
  <g font-size="16" font-weight="600" fill="currentColor">
    <text x="142" y="62" text-anchor="end">Cabinet</text>
    <text x="142" y="283" text-anchor="end">Playfield</text>
    <text x="142" y="201" text-anchor="end">Bumpers</text>
    <text x="142" y="437" text-anchor="end">Flippers</text>
    <text x="478" y="77">Scoreboard (micro:bit)</text>
    <text x="478" y="145">Ball</text>
    <text x="478" y="305">Launch lane (plunger)</text>
    <text x="478" y="437">Drain</text>
  </g>
</svg>
</div>

## Referencebyg
- ["3D Printed Pinball" af ctrl design](https://pinshape.com/items/24228-3d-printed-pinball) — micro:bit/Arduino-baseret, skalerbar sværhedsgrad, gratis STL-filer
- micro:bit + PinBox 3000 pap-flippermaskine (TechnoChic) — reference til at styre lys, lyd og en resultattavle fra en micro:bit på et enkelt stel

## Jeres 10-ugers byggeeventyr

<div style="text-align:center;overflow-x:auto;" markdown="0">
<svg viewBox="0 0 960 290" width="100%" style="max-width:900px;height:auto;" role="img" aria-label="A map of the 10-week pinball build journey" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,sans-serif">
<path d="M100 72 H860 Q922 72 922 141 Q922 210 860 210 H100" fill="none" stroke="#9aa4d4" stroke-width="3" stroke-dasharray="7 7" stroke-linecap="round"/>
<circle cx="100" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="100" y="85" text-anchor="middle" font-size="34">🚀</text><text x="100" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="100" font-weight="700">Uge 1</tspan><tspan x="100" dy="15" font-size="11">Kickoff</tspan></text>
<circle cx="290" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="290" y="85" text-anchor="middle" font-size="34">💯</text><text x="290" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="290" font-weight="700">Uge 2</tspan><tspan x="290" dy="15" font-size="11">Pointtælling</tspan></text>
<circle cx="480" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="480" y="85" text-anchor="middle" font-size="34">🎯</text><text x="480" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="480" font-weight="700">Uge 3</tspan><tspan x="480" dy="15" font-size="11">Udløser</tspan></text>
<circle cx="670" cy="72" r="32" fill="#e8eaf6" stroke="#5c6bc0" stroke-width="2.5"/><text x="670" y="85" text-anchor="middle" font-size="34">💡</text><text x="670" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="670" font-weight="700">Uge 4</tspan><tspan x="670" dy="15" font-size="11">Multi-sensor</tspan></text>
<circle cx="860" cy="72" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="860" y="85" text-anchor="middle" font-size="34">🧊</text><text x="860" y="124" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="860" font-weight="700">Uge 5</tspan><tspan x="860" dy="15" font-size="11">Tinkercad-leg</tspan></text>
<circle cx="860" cy="210" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="860" y="223" text-anchor="middle" font-size="34">🧩</text><text x="860" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="860" font-weight="700">Uge 6</tspan><tspan x="860" dy="15" font-size="11">Bumper</tspan></text>
<circle cx="670" cy="210" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="670" y="223" text-anchor="middle" font-size="34">🔧</text><text x="670" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="670" font-weight="700">Uge 7</tspan><tspan x="670" dy="15" font-size="11">Sensorholder</tspan></text>
<circle cx="480" cy="210" r="32" fill="#d8f3ef" stroke="#26a69a" stroke-width="2.5"/><text x="480" y="223" text-anchor="middle" font-size="34">🖨️</text><text x="480" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="480" font-weight="700">Uge 8</tspan><tspan x="480" dy="15" font-size="11">Print-klar</tspan></text>
<circle cx="290" cy="210" r="32" fill="#fff3d6" stroke="#f9a825" stroke-width="2.5"/><text x="290" y="223" text-anchor="middle" font-size="34">🛠️</text><text x="290" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="290" font-weight="700">Uge 9</tspan><tspan x="290" dy="15" font-size="11">Saml</tspan></text>
<circle cx="100" cy="210" r="32" fill="#fff3d6" stroke="#f9a825" stroke-width="2.5"/><text x="100" y="223" text-anchor="middle" font-size="34">🏆</text><text x="100" y="262" text-anchor="middle" fill="currentColor" font-size="13"><tspan x="100" font-weight="700">Uge 10</tspan><tspan x="100" dy="15" font-size="11">Fremvisning</tspan></text>
</svg>
</div>

*Fase 1 (uge 1–4): micro:bit-kodning · Fase 2 (uge 5–8): 3D-design · Fase 3 (uge 9–10): byg & afslut.*

## Uger

### Fase 1 · Kod micro:bitten
| Uge | Fokus |
|---|---|
| [1](./week-01-kickoff/README.md) | Kickoff & opsummering |
| [2](./week-02-scoring-basics/README.md) | Programmér grundlæggende pointtælling |
| [3](./week-03-launcher-trigger/README.md) | Programmér udløseren til affyring/flipper |
| [4](./week-04-multi-sensor-scoring/README.md) | Pointtælling med flere sensorer + game over |

### Fase 2 · 3D-design delene
| Uge | Fokus |
|---|---|
| [5](./week-05-tinkercad-basics/README.md) | Første skridt i Tinkercad (bare leg) |
| [6](./week-06-tinkercad-playfield/README.md) | Design en bumper til spillepladen |
| [7](./week-07-sensor-mount/README.md) | Design en sensorholder |
| [8](./week-08-design-finish/README.md) | Færdiggør & klargør print |

### Fase 3 · Byg & afslut
| Uge | Fokus |
|---|---|
| [9](./week-09-assembly-playtest/README.md) | Samling + første playtest |
| [10](./week-10-showcase-tournament/README.md) | Finpudsning & fremvisning / turnering |

## Tjekliste over materialer
- Micro:bits (1-2 pr. barn, hvis I prøver radioresultattavlen) + USB-kabler eller batteripakker
- Tinkercad-konti (skal bruges fra uge 5)
- Kontakter eller lyssensorer til pointtælling, buzzer/højttaler (indbygget i V2-boards), valgfri servoer til en bevægelig flipper
- Adgang til 3D-printer fra uge 6 og frem — sæt børnenes dele i kø, efterhånden som de designes (uge 6–8), så de er printet i tide til samlingen i uge 9
- Færdigdesignede/præcisionsfiler til kabinet og flippermekanisme klar inden uge 6, så børnenes egen designtid holdes fokuseret på deres egne simple dele
