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

    Every program lights a **real LED** — the **💡** tag shows which pin(s). Most need just **one LED on P0**; Part 2 uses **two or three** (ask a helper for more).

!!! failure "🔧 My LED doesn't light — check these, in order"
    1. **Turn the LED round.** The **long leg (+) → S**, the **short leg (−) → G**. Legs cut the same length? The **flat edge** on the LED's rim is the short (−) side. Backwards does no harm — it just stays dark.
    2. **S and G — never V.** Read the little letters on the board: the three rows aren't always in the same order. A plain LED never needs **V**.
    3. **Is the micro:bit pushed all the way in, straight?** If it's crooked or half in, **some pins work and others don't**. Pull it out and push it firmly back in.
    4. **Same pin in the code and on the board?** LED in P1 but the code says P0 = dark. Stick to **P0, P1, P2** — some other pins are busy inside the micro:bit (**P3, P4, P6, P7, P10** run the screen, **P5 / P11** are buttons A / B).
    5. **Wiggle the wire.** If the LED flickers, the connector is loose — swap the wire or bend the LED leg a tiny bit so it grips.
    6. **Blue or white LED?** They can be too dim at 3 V — try a **red** one.
    7. **Did you download** the newest program to the micro:bit?

??? example "🔧 Pin tester — find the broken LED in seconds · 💡 P0 + P1 + P2"

    Plug your LEDs into **P0, P1, P2** and run this. The screen shows **0**, **1**, **2** in turn and lights **that** pin's LED. The number shows but its LED stays dark? That's the one to fix — or move the LED to another pin to see whether it's the **LED** or the **socket**.

    ```makecode
    auto:pin-test
    ```

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

## 🌈 Part 2 — More LEDs

Grab **one or two more LEDs** (ask a helper!) and plug them into **P1** and **P2** — long legs to S, short legs to G, just like P0. Same blocks as Part 1 — `digital write` and `pause` — but now you control a whole light show! 🎆

??? example "🚓 Police lights · 💡 P0 + P1"

    **Two LEDs** take turns: one on, the other off, swap — *wee-woo!* Blue and red LEDs look best.

    ```makecode
    auto:police
    ```

    *Try it: make it faster with `pause 100`, or flash each LED **twice** before swapping.*

??? example "🙋 Quiz buzzer · 💡 P0 + P1"

    Two players! **A** lights the **P0** LED and shows **A**, **B** lights the **P1** LED and shows **B** — who presses first? ⏱️

    ```makecode
    auto:buzzer
    ```

    *Try it: play a different sound for each player, or keep the winner's light on longer.*

??? example "🏃 Running light · 💡 P0 + P1 + P2"

    Three LEDs light up **one after another**: P0 → P1 → P2 → again… like a light racing along a line.

    ```makecode
    auto:chaser
    ```

    *Try it: can you make it run **back** too (P2 → P1 → P0)? Or light up two at a time?*

??? example "🚦 Traffic light · 💡 P0 + P1 + P2"

    Use **red → P0**, **yellow → P1**, **green → P2** for a real Danish traffic light: red → red + yellow → green → yellow → red again… just like at the crossroads.

    ```makecode
    auto:traffic-light
    ```

    *How: it's just `digital write` and `pause` in the right order. Try adding a **pedestrian button**: press A to switch to red early!*

??? example "✨ Twinkle · 💡 P0 + P1 + P2"

    Three LEDs flick on and off **at random** — like fairy lights. ✨

    ```makecode
    auto:led-twinkle
    ```

    *How: `pick random 0 to 1` gives each pin either **0** (off) or **1** (on) every 150 ms. Change the pause for calmer or crazier twinkling.*

??? example "🚀 Rocket launch · 💡 P0 + P1 + P2"

    Press **A** for a countdown: **3** 💡 … **2** 💡💡 … **1** 💡💡💡 … **LIFT-OFF!** All the lights flash and the rocket blasts off with a sound. 🚀

    ```makecode
    auto:rocket
    ```

    *How: one LED turns on for each number, then a `repeat 4 times` loop flashes all three. Try a countdown from **5** — where would the extra LEDs go?*

## ✨ Part 3 — Bright and dim

`digital write` can only do **on (1)** or **off (0)**. `analog write pin` can do everything **in between**: **0** = off, **1023** = full brightness. Now your LED can glow softly! 🌗

??? example "🌙 Breathing LED · 💡 P0"

    The LED slowly **fades up** and **down again** — like it's breathing.

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

## 🧠 Part 4 — A light that remembers

So far the micro:bit forgets everything between presses. Now it will **remember** — and make a choice with `if / else`, just like the ghost will next.

### 🔦 One-button torch · 💡 P0

Just **one** button this time: press **A** once → on, press again → off. The micro:bit has to **remember** whether the light is on.

??? example "👀 See the program"

    ```makecode
    auto:led-toggle
    ```

    *How: the variable `on` is **true** or **false**. `set on to not on` flips it on every press, and `if` picks on or off. A light switch that remembers!*

## 🎃 Halloween 👻

A spooky seasonal treat that teaches something **new** — the micro:bit's hidden **light sensor**! 🦇

??? example "🕯️ Ghost in the Dark · 💡 P0 — *learn the light sensor!*"

    **Something new:** the micro:bit can **feel how light or dark it is** — the screen's LEDs double as a hidden **light sensor**! 👀 **Where is it?** It *is* the **25-light screen** on the front — so the screen must see the room, and you cover the **screen** with your hand. In the light it's calm 😀 and your LED is off. Cover the screen or turn off the lights and a **ghost appears** 👻 while your LED **flickers** like a haunted candle 🕯️. Spooky!

    Keep your LED on pin **P0** from Part 1. **Start it in the normal room light** — when it starts, it measures how bright your room is.

    - **Hold A** → see the light number (0–255). Cover the screen and watch it drop!
    - **Press B** → measure the room again (✓), e.g. after someone switches the lights.

    ```makecode
    auto:ghost-in-dark-led
    ```

    *How: at the start the program reads `light level` twice (the first reading just wakes the sensor) and sets `dark` to **half** the room's light — so it works in a dim classroom and a sunny one. A `forever` loop then checks: `light level` below `dark` → ghost, and `digital write pin P0` flips the LED **on/off at random** (the candle flicker); otherwise calm and off. It reads a sensor **and** drives a real circuit! Drag the light slider in the simulator to test.*

## 🚀 Level up — touch switches

Pins can be **inputs** too! Touching a pin (while you hold **GND**) closes a circuit — a homemade **switch**. This is how the **Ticklebot** and the pinball targets will work. Keep your LED on **P0** — touch **P1** *(unplug any LED from P1 first)*.

??? example "🔔 Doorbell light · 💡 P0"

    Touch **P1** (and hold **GND** with your other hand) → your LED lights for half a second + a ding. Input on one pin, output on another!

    ```makecode
    auto:led-touch
    ```

??? example "🤖 Tickle counter · 💡 P0"

    Every touch on **P1** adds a point: the LED flashes, a jingle plays and the score shows — a first taste of the Ticklebot! 😆

    ```makecode
    auto:tickle
    ```

    *How: a `score` **variable** goes up by 1 on each `on pin P1 pressed`, and the LED stays on while the score shows. Try wiring foil or a crocodile clip to P1 to make a bigger "tickle pad".*

## ✅ I did it when…

- ☐ I wired an **LED** and switched it **on and off** with buttons. 💡
- ☐ I made my LED **blink** and changed its speed. 🔁
- ☐ I wired **two or three LEDs** and made a light show (police lights, running light, traffic light or rocket). 🌈
- ☐ I made my LED **glow softly** with `analog write` (breathing LED or dimmer). 🌙
- ☐ I built a **one-button torch** that remembers if it's on. 🔦
- ☐ *(Scientist!)* I used the **light sensor** to make my LED flicker when it's dark. 🌑👻
- ☐ *(Legend!)* I built the **doorbell light** or the **tickle counter**. 🤖

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
    - for Part 2: **2 extra LEDs** per kid — ideally **red, yellow and green** (traffic light) and a **blue** one (police lights)
    - **no bulbs** — torch/filament bulbs draw too much current for a micro:bit pin
    - a way to **dim the room** (or hands/paper to cover the board) for the ghost
    - **V2** for the built-in speaker; V1 works otherwise

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 meet the LED (long leg +, short leg −) → 15 **wire + on/off** → 5 **blink** → 15 🌈 **more LEDs** (police → buzzer → running light → traffic light → twinkle → rocket; each kid picks 2–3) → 10 **breathing LED → dimmer** → 5 🔦 **torch** (variable + `if / else`, the warm-up for the ghost) → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 10 🕯️ **Ghost in the Dark** + lights-off ghost hunt 👻 → 10 level-up **doorbell light → tickle counter** → 5 showcase (🚀 rocket launches!) → 5 Kahoot.

    **Notes:** every embed opens in **Blocks**. For "my LED doesn't work", go through the **🔧 checklist** at the top of the page and run the **pin tester** — most cases are an LED **in backwards**, plugged into **V instead of G**, a micro:bit **not pushed fully into the shield** (exactly the "some pins work, some don't" symptom), or the **wrong pin**. On a **V2**, sound also comes out of **P0** by default, which makes a P0 LED buzz or blink at odd moments — so the programs that play sound (buzzer, rocket, doorbell, tickle) start with `set audio pin enabled false`; sound still plays on the built-in speaker (on a V1 these are silent). A dim blue/white LED isn't broken — swap it for red. `analog write` takes **0–1023** (not 0–255 like screen brightness). Part 2 puts LEDs on **P1** and **P2**; the touch programs use **P1** as an input — remind kids to unplug the P1 LED first. Ghost always blinking? The **screen** is the light sensor, so it must face the room (not be covered by the shield or a hand). Classroom light often reads only **10–60**, so the ghost measures the room at start-up instead of using a fixed number — make sure kids **start it in normal light**, and press **B** to re-measure if the lights change. Hold **A** to see the actual reading. Touch pins need the kid to also touch **GND** to close the circuit. The ghost program moved here from Week 6 so it lands on **Halloween week**. 🎃
