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

## 💡 Part 1 — Your first LED

### Switch it on and off

Press **A** to turn the LED **on**, **B** to turn it **off**. You're controlling a real light with code!

*🎓 Concept: **output** — `digital write pin P0 to 1` = on, `0` = off.*

??? example "👀 See the program"

    ```makecode
    auto:ledon
    ```

### Make it blink

No buttons this time — a `forever` loop flips the LED on, waits, flips it off, waits… forever. 🔁

??? example "👀 See the program"

    ```makecode
    auto:blink
    ```

    *Try it: change `500` to `100` for a fast blink, or `1000` for a slow one. Can you make an **SOS** (short-short-short, long-long-long)?*

## ✨ Part 2 — The screen's LEDs

The 25 lights on the front are LEDs too! Two tricks for the built-in screen:

??? example "💗 Fade — a breathing heart"

    `set brightness` goes from **0** (off) to **255** (full). Switching between bright and dim makes the heart pulse.

    ```makecode
    auto:fade
    ```

??? example "✨ Sparkle — random twinkles"

    `plot` turns on one LED at a random **x, y** spot, `unplot` turns another off — like a starry sky.

    ```makecode
    auto:sparkle
    ```

## 🎃 Halloween 👻

A spooky seasonal treat that teaches something **new** — the micro:bit's hidden **light sensor**! 🦇

??? example "🌑 Ghost in the Dark 🔦 — *learn the light sensor!*"

    **Something new:** the micro:bit can **feel how light or dark it is** — it has a hidden **light sensor**! Keep it in the light and it's calm 😀, but cover it or turn off the lights and a **ghost appears and wails** 👻. Spooky!

    ```makecode
    auto:ghost-in-dark
    ```

    *How: a `forever` loop checks **`light level`** (0–255 — the LEDs double as a light sensor). Below **50** (dark) → ghost + wail; otherwise calm. A brand-new **input** — the micro:bit's eyes! Drag the light slider in the simulator to test.*

??? example "🕯️ Ghost in the Dark — with a real LED 💡"

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

??? example "🤖 Tickle counter"

    Every touch on **P1** adds a point, plays a jingle and shows the score — a first taste of the Ticklebot! 😆

    ```makecode
    auto:tickle
    ```

    *How: a `score` **variable** goes up by 1 on each `on pin P1 pressed`. Try wiring foil or a crocodile clip to P1 to make a bigger "tickle pad".*

## ✅ I did it when…

- ☐ I wired an **LED** and switched it **on and off** with buttons. 💡
- ☐ I made my LED **blink** and changed its speed. 🔁
- ☐ *(Scientist!)* I used the **light sensor** to make a ghost appear in the dark — on screen and with my **real LED**. 🌑👻
- ☐ *(Legend!)* I built a **touch switch** or the **tickle counter**. 🤖

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
    - **LEDs** (1–2 each, a few spares) + jumper wires / crocodile clips
    - a way to **dim the room** (or hands/paper to cover the board) for the ghost
    - **V2** for the built-in speaker; V1 works otherwise

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 meet the LED (long leg +, short leg −) → 15 **wire + on/off** → 10 **blink** → 10 **fade / sparkle** → 15 🌑 **Ghost in the Dark** (screen) → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 10 🕯️ **ghost with the real LED** → lights-off ghost hunt 👻 → 10 level-up **touch switch / tickle counter** → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens in **Blocks**. Most "my LED doesn't work" problems are an LED **in backwards** or on the **wrong pin** — check P0 and flip it. The very first `light level` reading can be off while the sensor wakes up — give it a second. Touch pins need the kid to also touch **GND** to close the circuit. The ghost programs moved here from Week 6 so they land on **Halloween week**. 🎃
