# Gruppe B — Avanceret: Mini-flippermaskine

Alder 8-10, allerede fortrolige med det grundlæggende i MakeCode. Sessioner på 1 time, fysiske micro:bits, Tinkercad til 3D-design.

Et 10-ugers afgangsprojekt, hvor der bygges en lille flippermaskine til bordet. Alt holdes på et simpelt blok-kodningsniveau — ikke noget indviklet, bare mange små sejre. Sæsonen kører i **tre nemme faser**:

1. **Uge 1–4 · Kod micro:bitten** — flippermaskinens "hjerne": pointtælling, en flipper-udløser, pointtælling med flere sensorer og game-over (med en valgfri radioresultattavle).
2. **Uge 5–8 · 3D-design delene** — start med en hel uge, hvor I *bare leger* i Tinkercad (perfekt til førstegangsdesignere), design derefter en bumper og en sensorholder, og færdiggør/print det hele.
3. **Uge 9–10 · Byg & afslut** — saml, playtest, finpuds, pynt, og slut af med en mini-turnering.

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
