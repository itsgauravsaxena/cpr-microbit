# Week 3 — Pinball switches ⚡ (part 2)

> Part 2 of the pinball build. Last week your targets were the 3 touch pins — this week you **wire and read your own switches**, so the machine can grow as big as you want. 🔌

!!! abstract "🎓 What you'll learn today"
    - **digital input** — read a real switch
    - **loops** (`forever`) — watch a pin all the time
    - **state** — the machine remembers what you did

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="a bumper hit rippling out across the screen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ffd23f"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

!!! info "🎯 New to the pinball project?"
    See **[The pinball project](../../pinball/README.md)** for the big picture, and **[Week 2 — Pinball scoreboard](../week-02-data-sensors/README.md)** for the score-on-touch build this continues.

## ⚡ Wire up more targets

**Why?** So far your targets are the **3 touch pins** (P0/P1/P2). A real pinball has *loads* of targets, bumpers and lanes — and every one is just a tiny **switch the ball closes**. This week is how you **wire and read your own switches**, so your machine can grow as big as you want. This is the real electronics the lights and flippers plug into later. 🔌

Build it up **one small step at a time** — each step adds just a little. 🌱

*🎓 Concept: **digital input** + **loops** (`forever`) + **state**.*

??? note "How it works"

    **Purpose.** Teach how a *real* switch is read, and the one trick — **edge detection** — behind every button, bumper and lane in the world. This is the input electronics the lights and flippers plug into later.

    **Think of it like a turnstile:** it should count each person **once** as they push through — not keep counting while someone leans on it. That "count on the change" is the `wasClosed` trick; in the machine a bumper scores once per hit, not while the ball rests against it.

    **How the code works (the key steps):**

    - `set pull pin P0 up` makes the pin rest at **1** when the switch is open; closing it (a wire to **GND**) pulls it to **0**. A `forever` loop reads `digital read P0` over and over.
    - **② is a deliberate bug:** adding points *inside* the loop makes the score rocket, because the loop runs hundreds of times a second while the switch is held.
    - **③ is the fix — the big idea:** a `wasClosed` variable (a **flag**) so it scores only when the pin *becomes* 0 (and `wasClosed` was still false), then sets the flag; opening the switch clears it. "Only on the change" = **edge detection** → one hit, one point.
    - **⑤ rollover lanes** keep a `leftArmed` flag: hitting P0 arms it, hitting P1 *while armed* pays the BONUS. The machine now remembers what happened first — that's **state**.

    **Watch for:** steps ①–⑤ run in the simulator (click P0/P1). Step ⑥ moves the extra switches to spare pins **P8/P9**, which the sim can't click — test that one on hardware (or temporarily read P0/P1).

!!! tip "Which pin? P0 now, spare pins later"
    We practise on **P0** because you can **press it in the simulator**. On the real table your touch targets stay on P0–P2 and each *extra* switch goes on a spare pin (**P8, P9, …**) — read with the **exact same blocks**, just a different pin number. The **Keyestudio shield** gives every pin its own socket — that's how you reach **P8/P9** (a bare micro:bit only clips onto P0/P1/P2).

**① Read a switch** 🔌 — the whole idea in three blocks: **`set pull pin P0 up`**, then a **`forever`** loop that shows a ✓ while the switch is closed (**`digital read pin P0` = 0**) and clears it otherwise. Press **P0** in the sim — ✓ on, ✓ off.

??? example "👀 See the blocks"

    ```makecode
    auto:adv-1
    ```

**② Make it score** 🔢 — now add points when it closes. Press P0 and watch… the score races up **crazy fast** while you hold it! That's a real problem — the `forever` loop counts *every* pass. We fix it next.

??? example "👀 See the blocks"

    ```makecode
    auto:adv-2
    ```

**③ One hit = one point** 🎯 — add a **`wasClosed`** flag so a hit only scores **once**, when the switch *first* closes. This "only on the change" trick is how every real button and bumper works.

??? example "👀 See the blocks"

    ```makecode
    auto:adv-3
    ```

**④ A second target** ➕ — copy the same idea onto **P1** for a second switch, worth more points. Two targets! On the real board this is just another wire to another pin.

??? example "👀 See the blocks"

    ```makecode
    auto:adv-4
    ```

**⑤ Rollover lanes** 🛣️ — a proper pinball combo: hit the **left lane (P0)** to *arm* it, then the **right lane (P1)** for a big **BONUS**. Miss the order and no bonus. Now the machine remembers what you did — that's **state**.

??? example "👀 See the blocks"

    ```makecode
    auto:adv-5
    ```

**⑥ Put it in your machine** 🕹️ — drop your new switches into the full game: touch targets on **P0/P1/P2** *and* two wired switches on **P8/P9** (a **100** bumper and a **500** jackpot), all with the one-hit-one-point trick. A real table with real switches.

??? example "👀 See the blocks — run or edit"

    ```makecode
    auto:adv-6
    ```

### 🔭 Coming next — lights & flippers

Now the machine *reads* lots of switches, it's ready for the parts that make it move and glow (coming weeks):

- 🌈 **Playfield lights** — a **NeoPixel** strip that flashes on every switch hit.
- 🕹️ **Flippers** — **servos** on buttons **A/B** that flick the ball back up the table.

## 🎮 Bonus — tilt maze (brain break)

Need a change of pace from wiring? Tilt the board and a dot rolls across the screen — like a marble in a tray. Same accelerometer you've used before, now steering a sprite. 🎮

??? note "How it works"

    **Purpose.** A no-wiring brain break that reuses the accelerometer to steer an on-screen **sprite** (a movable LED).

    **Think of it like a wooden ball-in-a-maze toy:** tilt the tray and the marble rolls whichever way you lean it.

    **How the code works:** `create sprite` makes the player dot and a target. A `forever` loop reads `acceleration (X)` and `(Y)` — each roughly −1023…1023 — **divides by 300** to get a small step, and `change x/y by` nudges the dot. When the player `is touching` the target, `score +1` and the target jumps to a random spot. The **`/ 300`** is the speed dial: smaller = faster and twitchier. Dot flies off? Raise it to 500.

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 218" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set player to create sprite at 2,2</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set target to create sprite at 4,4</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">player change x by (acceleration X / 300)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">player change y by (acceleration Y / 300)</text>
<rect x="322" y="125" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if player touching target → score +1</text>
<rect x="322" y="160" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 100 ms</text>
</svg>
</div>

```javascript
let player = game.createSprite(2, 2)
let target = game.createSprite(4, 4)
basic.forever(function () {
    player.change(LedSpriteProperty.X, input.acceleration(Dimension.X) / 300)
    player.change(LedSpriteProperty.Y, input.acceleration(Dimension.Y) / 300)
    if (player.isTouching(target)) {
        game.addScore(1)
        target.set(LedSpriteProperty.X, randint(0, 4))
        target.set(LedSpriteProperty.Y, randint(0, 4))
    }
    basic.pause(100)
})
```

!!! tip "▶️ Try it in MakeCode (30 seconds)"
    1. Open <https://makecode.microbit.org> → **New Project**
    2. Click the **`{ } JavaScript`** button at the top
    3. Select everything in the editor and **delete it**, then **paste the code above**
    4. Click **Blocks** to switch back — the real blocks appear, ready to explore
    5. **Download** to put it on a board, or press ▶️ to run it in the simulator

    `acceleration (X)` is roughly −1023…1023. Dividing by 300 turns that into a small step like −3…3 — that division is your **speed control**. Smaller number = faster and twitchier. Dot flies off instantly? Increase the divisor (try 500). Extra: add **walls** (flash and reset on the edge), a **30-second countdown**, or a second target worth 5.

## ✅ I did it when…

- ☐ I **read my own switch** and saw ✓ on / ✓ off.
- ☐ I fixed it to **one hit = one point** (the `wasClosed` flag).
- ☐ I added a **second target** on another pin.
- ☐ *(Boss!)* **Rollover lanes** give a **BONUS** only in the right order.

## 🎉 Kahoot time!

Finish with this week's quiz — **both groups play together**.

```kahoot
week-3
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** the **electronics-first** half of the pinball build — *reading a switch*, built up one small step at a time (each embed adds only the new bit, so kids see it grow). Still **no new parts** beyond Week 2, just wires and the shield. It carries straight on from **[Week 2](../week-02-data-sensors/README.md)**.

    **The concept:** a switch is two wires the ball closes; `set pull pin … up` makes the pin read **1** open / **0** closed, and a `forever` loop watches it. The big teaching moment is **② → ③**: without an edge flag the score races while held; the **`wasClosed`** flag ("only on the change") fixes it — the same trick behind every button and bumper. Steps ①–⑤ practise on **P0/P1** so kids can **press the pads in the simulator**; ⑥ moves the extra switches to spare pins **P8/P9** exactly as on the real board (same blocks, different pin — the sim can't click those, so test ⑥ on hardware or by temporarily reading P0/P1). ⑤ (rollover lanes) adds **ordered state** for a combo.

    **Materials**

    - micro:bit (**V2** recommended) + USB, **Keyestudio sensor shield**
    - a couple of extra wires (and foil/a button) to make **switch targets** — practise on P0/P1, then real switches on **P8/P9**
    - Laptop/Chromebook — the **simulator is enough** for steps ①–⑤ (click the pins)

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap the scoreboard → 15 ① read a switch + ② make it score → 20 ③ one-hit-one-point (the key idea) → 15 ④ second target → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 15 ⑤ rollover lanes / ⑥ full machine for fast finishers → 5 **tilt-maze** brain break → 5 showcase → 5 Kahoot.

    **Notes:** blocks are shown; **JavaScript/Python** are one click away via **Open & run**. This is the input half of the pinball electronics — it sets up the hardware weeks: 🌈 NeoPixels and 🕹️ servos. The **🎮 tilt maze** is an optional brain break (the accelerometer they've already met) — no wiring, pure sim fun.
