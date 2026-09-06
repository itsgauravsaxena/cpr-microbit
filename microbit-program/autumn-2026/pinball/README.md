# The pinball project 🎯

> This term the **Pro** crew builds the **brain of a pinball machine**: the code that scores points, makes sounds and lights, and keeps the game going. Another group 3D-prints the body — we do the micro:bit. This page explains the whole plan; each **weekly page** then builds one piece.

New to the micro:bit and its pins? Start with **[Meet the gear](../gear/README.md)** 🔧.

## 🎮 The parts of a pinball

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
<text x="96" y="268" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🔴 Bumpers</text>
<line x1="98" y1="410" x2="148" y2="410" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="410" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎯 Targets</text>
<line x1="98" y1="560" x2="150" y2="558" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="560" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🕹️ Flippers</text>
<line x1="98" y1="584" x2="182" y2="584" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="584" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎱 Drain</text>
<text x="200" y="646" font-size="12.5" fill="var(--md-default-fg-color)" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif">↑ in a 3D-printed holder — the scoreboard + brain</text>
</svg>
</div>

- 🚀 **Plunger** — launches the ball onto the field.
- 🔴 **Bumpers** — the ball bounces off them and scores.
- 🎯 **Targets** — hit these to score (our metal **touch-pins**); thin wires run **up** to the micro:bit.
- 🕹️ **Flippers** — flick the ball back up so it doesn't fall.
- 🎱 **Drain** — the gap at the bottom; if the ball falls in, you lose it.
- 🧠 **micro:bit + shield** — the **brain**, in a **3D-printed holder at the top** (like a real pinball's backbox). Its LED screen is the **🔢 scoreboard**, buttons A/B are reset/new-game — and it's **out of the ball's way**.

That's the machine — now let's see how the micro:bit runs each part 👇

## 🎛️ Pinball features → micro:bit

Everything a pinball machine does, the micro:bit can do too:

| Pinball feature | We use the micro:bit's… |
|---|---|
| 🎯 Targets & bumpers score points | **touch pins** (P0, P1) |
| 🔢 Scoreboard | the **LED screen** |
| 🔊 "Ding!" and a game-over jingle | the **speaker** |
| 🎱 Ball drains → lose a life | a **drain pin** (P2) + a `balls` variable |
| 💥 TILT (shook too hard) | the **shake sensor** |
| 🕹️ Flippers (later) | **buttons A/B** → **servos** on pins |
| 🌈 Playfield lights (later) | a **NeoPixel** strip on a pin |
| 🏆 High score (later) | remember it in a **variable** |

New to the micro:bit and its pins? Start with **[Meet the gear](../gear/README.md)** 🔧.

## 🔭 Where we're headed

Over the term the machine keeps growing:

- 🕹️ **Flippers** — buttons A/B drive **servos** that flip
- 🚀 **Plunger / launch** — a button (later a servo) to fire the ball
- 🌈 **Playfield lights** — a **NeoPixel** strip that flashes on hits
- 🏆 **High score** — remember the best game
- ✨ **Bonus & multiball** — combos, multipliers, extra balls
- 😴 **Attract mode** — scroll "PLAY!" when the machine is idle

## 👉 Ready to build?

Head to your weekly page — that's where we write the code, one feature at a time. Week 2 starts the **scoreboard**.
