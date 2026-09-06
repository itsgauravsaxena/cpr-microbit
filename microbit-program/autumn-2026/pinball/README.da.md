# Flipperprojektet 🎯

> Dette semester bygger **Pro**-holdet **hjernen i en flippermaskine**: koden, der giver point, laver lyd og lys, og holder spillet i gang. En anden gruppe 3D-printer kroppen — vi laver micro:bit'en. Denne side forklarer hele planen; hver **ugeside** bygger så én del.

Ny til micro:bit'en og dens pins? Start med **[Mød dit udstyr](../gear/README.md)** 🔧.

## 🎮 Flipperens dele

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg viewBox="0 0 400 660" width="100%" style="max-width:340px;height:auto;display:block;margin:0 auto;" role="img" aria-label="Pinball parts with the micro:bit in a top backbox holder" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="112" y="26" width="176" height="94" rx="12" fill="#2b3038" stroke="#c8a24a" stroke-width="2"/>
<rect x="140" y="38" width="120" height="66" rx="8" fill="#0f1419" stroke="#c8a24a" stroke-width="1.5"/>
<rect x="176" y="46" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="186" y="46" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="196" y="46" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="206" y="46" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="216" y="46" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="176" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="186" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="196" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="206" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="216" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="176" y="66" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="186" y="66" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="196" y="66" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="206" y="66" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="216" y="66" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="176" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="186" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="196" y="76" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="206" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="216" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<circle cx="152" cy="72" r="6" fill="#2b3038" stroke="#c8a24a"/><circle cx="248" cy="72" r="6" fill="#2b3038" stroke="#c8a24a"/>
<rect x="180" y="99" width="10" height="5" rx="1" fill="#ffd23f"/>
<rect x="196" y="99" width="10" height="5" rx="1" fill="#ffd23f"/>
<rect x="212" y="99" width="10" height="5" rx="1" fill="#ffd23f"/>
<rect x="176" y="118" width="48" height="20" fill="#2b3038"/>
<rect x="105" y="135" width="190" height="470" rx="18" fill="#20486e" stroke="#c8a24a" stroke-width="3"/>
<path d="M112 215 Q200 158 288 215" fill="none" stroke="#3d6a95" stroke-width="4"/>
<line x1="262" y1="215" x2="262" y2="590" stroke="#3d6a95" stroke-width="3"/>
<circle cx="278" cy="185" r="7" fill="#d7dbe1" stroke="#9aa0aa"/>
<rect x="271" y="571" width="14" height="18" rx="3" fill="#c0c4cc" stroke="#8a8f98"/>
<path d="M278 589 l-7 5 l14 5 l-14 5" fill="none" stroke="#8a8f98" stroke-width="2"/>
<circle cx="152" cy="268" r="21" fill="#e63946"/><circle cx="152" cy="268" r="8" fill="#fff"/>
<circle cx="222" cy="236" r="21" fill="#e63946"/><circle cx="222" cy="236" r="8" fill="#fff"/>
<circle cx="188" cy="338" r="21" fill="#e63946"/><circle cx="188" cy="338" r="8" fill="#fff"/>
<rect x="150" y="405" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="184" y="405" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="218" y="405" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<circle cx="168" cy="472" r="9" fill="#d7dbe1" stroke="#9aa0aa"/><circle cx="165" cy="469" r="2.5" fill="#fff"/>
<rect x="145" y="552" width="46" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(-26 145 560)"/>
<rect x="209" y="552" width="46" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(26 255 560)"/>
<rect x="182" y="578" width="36" height="14" rx="3" fill="#0a1a2a"/>
<path d="M200 561 l-8 12 l16 0 z" fill="#0a1a2a" opacity="0.55"/>
<path d="M150 405 C 118 330, 118 190, 176 132" fill="none" stroke="#ffd23f" stroke-width="2" stroke-dasharray="4 4"/>
<line x1="288" y1="72" x2="302" y2="72" stroke="#c8a24a" stroke-width="1.5"/>
<text x="304" y="72" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🧠 micro:bit</text>
<line x1="288" y1="185" x2="302" y2="185" stroke="#c8a24a" stroke-width="1.5"/>
<text x="304" y="185" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🚀 Plunger</text>
<line x1="98" y1="268" x2="131" y2="268" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="268" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🔴 Bumpere</text>
<line x1="98" y1="410" x2="148" y2="410" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="410" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎯 Mål</text>
<line x1="98" y1="560" x2="150" y2="558" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="560" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🕹️ Flippere</text>
<line x1="98" y1="584" x2="182" y2="584" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="584" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎱 Drain</text>
<text x="200" y="646" font-size="12.5" fill="var(--md-default-fg-color)" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif">↑ i en 3D-printet holder — scoreboard + hjerne</text>
</svg>
</div>

- 🚀 **Plunger** — skyder kuglen ind på banen.
- 🔴 **Bumpere** — kuglen hopper af dem og scorer.
- 🎯 **Mål** — ram dem for at score (vores metal-**touch-pins**); tynde ledninger går **op** til micro:bit'en.
- 🕹️ **Flippere** — slår kuglen op igen, så den ikke falder ned.
- 🎱 **Drain** — hullet i bunden; falder kuglen i, mister du den.
- 🧠 **micro:bit + shield** — **hjernen**, i en **3D-printet holder øverst** (som en rigtig flippers backbox). Dens LED-skærm er **🔢 scoreboardet**, knapperne A/B er nulstil/nyt spil — og den er **væk fra kuglens vej**.

Det er maskinen — lad os se, hvordan micro:bit'en styrer hver del 👇

## 🎛️ Flipper-funktioner → micro:bit

Alt hvad en flippermaskine kan, kan micro:bit'en også:

| Flipper-funktion | Vi bruger micro:bit'ens… |
|---|---|
| 🎯 Mål & bumpere giver point | **touch-pins** (P0, P1) |
| 🔢 Scoreboard | **LED-skærmen** |
| 🔊 "Ding!" og en game-over-melodi | **højtaleren** |
| 🎱 Kuglen ryger ud → mist et liv | en **drain-pin** (P2) + en `balls`-variabel |
| 💥 TILT (rystet for hårdt) | **ryste-sensoren** |
| 🕹️ Flippere (senere) | **knapperne A/B** → **servoer** på pins |
| 🌈 Banelys (senere) | en **NeoPixel**-strip på en pin |
| 🏆 Highscore (senere) | husk den i en **variabel** |

Ny til micro:bit'en og dens pins? Start med **[Mød dit udstyr](../gear/README.md)** 🔧.

## 🔭 Hvor vi er på vej hen

Henover semesteret vokser maskinen:

- 🕹️ **Flippere** — knapperne A/B styrer **servoer**, der flipper
- 🚀 **Plunger / affyring** — en knap (senere en servo) til at skyde kuglen
- 🌈 **Banelys** — en **NeoPixel**-strip, der blinker ved ramt
- 🏆 **Highscore** — husk det bedste spil
- ✨ **Bonus & multibold** — combos, multiplikatorer, ekstra kugler
- 😴 **Attract-mode** — scroll "PLAY!", når maskinen står stille

## 👉 Klar til at bygge?

Gå til din ugeside — det er der, vi skriver koden, én funktion ad gangen. Uge 2 starter **scoreboardet**.
