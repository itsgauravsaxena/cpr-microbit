# Week 7 — Light It Up 💡🎃

> Our first **real circuits**! Wire up an LED and make it switch, blink and flicker — then use the micro:bit's hidden **light sensor** for a spooky **Halloween** ghost that only comes out in the dark. 👻

!!! abstract "🎓 What you'll learn today"
    - **outputs** — `digital write pin` turns a real LED **on (1)** and **off (0)**
    - **wiring** — an LED has a **long leg (+)** and a **short leg (−)**
    - the **light sensor** — a brand-new **input** (`light level`, 0–255)
    - **inputs → outputs** — read a sensor, then drive a circuit

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a flickering ghost on the LED screen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="17" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="153" width="26" height="26" rx="6" fill="#2b3038"/><g fill="#ff8c1a"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0;0.15;0.25;0.4;0.55;0.6" values="1;0.25;1;0.5;1;0.2"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

!!! tip "Wiring an LED 🔌"
    Plug the micro:bit into the **[sensor shield](../gear/README.md)** and connect an **LED** to pin **P0**: **long leg → S (signal)**, **short leg → G (ground)**. No shield? Use crocodile clips on **P0** and **GND**. LED stays dark? Flip it round — LEDs only work one way! 🔄

!!! warning "Which lights can I use? 💡"
    - ✅ **LED modules** (little boards with S / V / G) — easiest: plug straight into the shield, resistor built in.
    - ✅ **Loose LEDs** — red, yellow and green are brightest. Blue and white may be dim (the pins only give ~3 V). A **100–220 Ω resistor** in series is kindest to the pin.
    - ❌ **Bulbs** (torch / filament bulbs) — they need far more power than a pin gives. They won't light and can damage the micro:bit.

    Every program marked **💡 P0** lights your real LED. **🖥️ screen** programs use the built-in lights and need no wiring.

## 💡 Part 1 — Your first LED

### Switch it on and off · 💡 P0

Press **A** to turn the LED **on**, **B** to turn it **off**. You're controlling a real light with code!

*🎓 Concept: **output** — `digital write pin P0 to 1` = on, `0` = off.*

??? example "👀 See the program"

    ```makecode
    auto:ledon
    ```

### Make it blink · 💡 P0

No buttons this time — a `forever` loop flips the LED on, waits, flips it off, waits… forever. 🔁

??? example "👀 See the program"

    ```makecode
    auto:blink
    ```

    *Try it: change `500` to `100` for a fast blink, or `1000` for a slow one. Can you make an **SOS** (short-short-short, long-long-long)?*

### 🔦 One-button torch · 💡 P0

Just **one** button this time: press **A** once → on, press again → off. The micro:bit has to **remember** whether the light is on.

??? example "👀 See the program"

    ```makecode
    auto:led-toggle
    ```

    *How: the variable `on` is **true** or **false**. `set on to not on` flips it on every press, and `if` picks on or off. A light switch that remembers!*

## ✨ Part 2 — Bright and dim

`digital write` can only do **on (1)** or **off (0)**. `analog write pin` can do everything **in between**: **0** = off, **1023** = full brightness. Now your LED can glow softly! 🌗

??? example "🌙 Breathing LED · 💡 P0"

    The real LED slowly **fades up** and **down again** — like it's breathing.

    ```makecode
    auto:led-fade
    ```

    *How: a `for` loop counts 0 → 20 and writes `index × 50` (0 → 1000); a second loop counts back down. Change `pause 40` to make it breathe faster or slower.*

??? example "🎚️ Dimmer · 💡 P0"

    **B** = brighter, **A** = dimmer. The screen shows the level **0–10**.

    ```makecode
    auto:led-dimmer
    ```

    *How: the variable `level` goes from 0 to 10, and `analog write pin P0` gets `level × 100`. `min` / `max` stop it from going past 10 or below 0.*

### 🖥️ On the screen

The 25 lights on the front are LEDs too! Two tricks for the built-in screen — no wiring needed:

??? example "💗 Fade — a breathing heart · 🖥️ screen"

    `set brightness` goes from **0** (off) to **255** (full). Switching between bright and dim makes the heart pulse.

    ```makecode
    auto:fade
    ```

??? example "✨ Sparkle — random twinkles · 🖥️ screen"

    `plot` turns on one LED at a random **x, y** spot, `unplot` turns another off — like a starry sky.

    ```makecode
    auto:sparkle
    ```

## 🎃 Halloween 👻

A spooky seasonal treat that teaches something **new** — the micro:bit's hidden **light sensor**! 🦇

??? example "🌑 Ghost in the Dark 🔦 — *learn the light sensor!* · 🖥️ screen"

    **Something new:** the micro:bit can **feel how light or dark it is** — it has a hidden **light sensor**! Keep it in the light and it's calm 😀, but cover it or turn off the lights and a **ghost appears and wails** 👻. Spooky!

    ```makecode
    auto:ghost-in-dark
    ```

    *How: a `forever` loop checks **`light level`** (0–255 — the LEDs double as a light sensor). Below **50** (dark) → ghost + wail; otherwise calm. A brand-new **input** — the micro:bit's eyes! Drag the light slider in the simulator to test.*

??? example "🕯️ Ghost in the Dark — with a real LED · 💡 P0"

    Same idea, now with the **LED you wired up**: in the dark, it **flickers** like a haunted candle; in the light it's off. 🕯️👻

    Keep your LED on pin **P0** from Part 1.

    ```makecode
    auto:ghost-in-dark-led
    ```

    *How: when `light level` is low, `digital write pin P0` flips the LED **on/off at random** (a candle flicker); in the light it stays off. Now it reads a sensor **and** drives a real circuit. No LED? Watch the **P0** pin in the simulator.*

## 🚀 Level up — touch switches

Pins can be **inputs** too! Touching a pin (while you hold **GND**) closes a circuit — a homemade **switch**. This is how the **Ticklebot** and the pinball targets will work.

??? example "👆 Touch switch"

    Touch **P1** (and hold **GND** with your other hand) → ✓ and a beep.

    ```makecode
    auto:switch
    ```

??? example "🔔 Doorbell light · 💡 P0"

    Same touch switch, but now your **LED** flashes too: touch **P1** → the LED on **P0** lights for half a second + a ding. Input on one pin, output on another!

    ```makecode
    auto:led-touch
    ```

??? example "🤖 Tickle counter"

    Every touch on **P1** adds a point, plays a jingle and shows the score — a first taste of the Ticklebot! 😆

    ```makecode
    auto:tickle
    ```

    *How: a `score` **variable** goes up by 1 on each `on pin P1 pressed`. Try wiring foil or a crocodile clip to P1 to make a bigger "tickle pad".*

## 🚦 Super level — traffic light

Got **three LEDs**? Build a real Danish traffic light! **Red → P0**, **yellow → P1**, **green → P2** (long legs to S, short legs to G).

??? example "🚦 Traffic light · 💡 P0 + P1 + P2"

    Red → red + yellow → green → yellow → red again… just like at the crossroads.

    ```makecode
    auto:traffic-light
    ```

    *How: it's just `digital write` and `pause` in the right order. Try adding a **pedestrian button**: press A to switch to red early!*

## ✅ I did it when…

- ☐ I wired an **LED** and switched it **on and off** with buttons. 💡
- ☐ I made my LED **blink** and changed its speed. 🔁
- ☐ I made my LED **glow softly** with `analog write` (breathing LED or dimmer). 🌙
- ☐ *(Scientist!)* I used the **light sensor** to make a ghost appear in the dark — on screen and with my **real LED**. 🌑👻
- ☐ *(Legend!)* I built a **touch switch**, the **doorbell light** or the **tickle counter**. 🤖
- ☐ *(Super legend!)* I wired **three LEDs** into a **traffic light**. 🚦

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-7
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** everyone wires **one LED** and controls it from code, then combines an **input** (light sensor) with that **output** for the Halloween ghost. Fast finishers move on to **touch switches** (toward the Ticklebot / pinball).

    **Materials**

    - micro:bits + USB + **sensor shields** — **1 per kid** (this week works solo)
    - **LEDs** (1–2 each, a few spares; LED modules are easiest) + jumper wires / crocodile clips
    - for the traffic light: **red, yellow and green** LEDs (3 per kid who gets there)
    - **no bulbs** — torch/filament bulbs draw too much current for a micro:bit pin
    - a way to **dim the room** (or hands/paper to cover the board) for the ghost
    - **V2** for the built-in speaker; V1 works otherwise

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 meet the LED (long leg +, short leg −) → 15 **wire + on/off** → 10 **blink / torch** → 10 **breathing LED / dimmer** (screen fade / sparkle for anyone without an LED) → 15 🌑 **Ghost in the Dark** (screen) → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 10 🕯️ **ghost with the real LED** → lights-off ghost hunt 👻 → 10 level-up **touch switch / doorbell light / tickle counter** (🚦 traffic light for fast finishers) → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens in **Blocks**. Most "my LED doesn't work" problems are an LED **in backwards** or on the **wrong pin** — check P0 and flip it. A dim blue/white LED isn't broken — swap it for red. `analog write` takes **0–1023** (not 0–255 like screen brightness). The doorbell light uses **P1** for touch, so the traffic light (which needs P1 for yellow) is a separate program. The very first `light level` reading can be off while the sensor wakes up — give it a second. Touch pins need the kid to also touch **GND** to close the circuit. The ghost programs moved here from Week 6 so they land on **Halloween week**. 🎃
