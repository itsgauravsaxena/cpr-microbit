# Week 6 — Team Games 🎮

> Two playground classics, now **over radio**: **Red Light, Green Light** 🚦 and **Rock-Paper-Scissors** ✊✋✌️ — each with a level-up for fast finishers.

!!! abstract "🎓 What you'll learn today"
    - **transmitter & receiver** — one caller, many players
    - the **accelerometer** — catching movement
    - **random** + **variables** — fair throws and keeping score

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a red light turning green" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g><animate attributeName="fill" calcMode="discrete" dur="2s" repeatCount="indefinite" keyTimes="0;0.5" values="#ff4d4d;#59b04a"/><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

## 🎮 Pick a game

Both games use **two or more micro:bits** on the same **group**. Flash a program onto each board, then play! New to radio? Start with **[Week 4 — Game Lab](../week-04-game-lab/README.md)**. 🌱

### 🚦 Red Light, Green Light

The playground classic — on the micro:bit! One board is the **caller** (the traffic light); everyone else holds a **player** board. Move on green ✓, freeze on red ✗ — get caught moving on red and you're **out**! 🚦

*🎓 Concept: **transmitter & receiver** + the **accelerometer** (it feels you move).*

!!! tip "One caller, lots of players — same group"
    Flash **`LIGHT`** (the caller) onto one board and **`PLAYER`** onto everyone else's, all on the **same group**. The caller presses **A = green**, **B = red**.

??? example "👀 See the two programs"

    **🚦 Caller (the traffic light)** — press A for green, B for red:

    ```makecode
    auto:rlgl-light
    ```

    **🏃 Player** — ✓ green = go, ✗ red = freeze. Move on red → 💀 out!

    ```makecode
    auto:rlgl-player
    ```

??? note "How it works"

    **Think of it like the real game — the micro:bit is a referee that never blinks.**

    - The **caller** is a *transmitter*: **A** sends `1` (green ✓), **B** sends `2` (red ✗).
    - Each **player** is a *receiver*: it remembers the light in a variable. `on shake` = "you moved" — if the light is **red** right then, it shows a 💀 and calls **game over**.

    **Watch for:** needs **2+ boards on the same group**. In the simulator, shake the player while the light is red to see the game-over; on real boards the *accelerometer* catches real movement.

??? example "🚀 Level up — automatic caller"

    No more button-pressing — the light flips **red/green on its own** at random times, so no one can predict it. Sneaky! Players keep the same **`PLAYER`** program.

    **🚦 Auto-caller** — random green, then random red, forever:

    ```makecode
    auto:rlgl-auto
    ```

    *How: a `forever` loop sends green, waits a **random** `1–4 s`, sends red, waits a random `1–3 s`, and repeats — `pick random` makes the timing impossible to guess.*

### ✊✋✌️ Rock, Paper, Scissors

Shake to throw ✊✋✌️. Play it **solo**, then **duel a friend over the radio** — the boards judge the winner for you!

*🎓 Concept: **random** to throw, **radio** to duel.*

??? example "👀 Solo — one board"

    Shake to throw rock, paper or scissors:

    ```makecode
    auto:rps
    ```

??? example "🚀 Level up — duel over radio"

    Two boards on the **same group**. You both shake, and each screen shows 😀 win, 😢 lose, or `=` draw:

    ```makecode
    auto:rps-radio
    ```

??? note "How it works"

    **Think of it like a referee with a rulebook.**

    - `pick random 0 to 2` chooses rock (0), paper (1) or scissors (2), drawn with `show leds`.
    - In the duel you `send` your throw; when your friend's throw *arrives*, an `if / else if` compares them (rock beats scissors, paper beats rock, scissors beats paper) and shows the result — the same throw is a draw `=`.

    **Watch for:** both players **shake at about the same time**, then look. The duel uses its **own group** so it won't cross the message games.

??? example "🚀 Level up — keep score, first to 5"

    Play a real match: your board **remembers your wins** and shows your score. First to **5** wins the match! 🏆

    **✊✋✌️ Scoring duel** — both players flash this, same group:

    ```makecode
    auto:rps-score
    ```

    *How: a `myScore` **variable** goes up by 1 on every win (`change myScore by 1`); at **5** it flashes `WIN!` and resets. Keeping score across rounds is the new idea.*

## 🎃 Halloween 👻

A spooky seasonal treat that teaches something **new** — the micro:bit's hidden **light sensor**! 🦇

??? example "🌑 Ghost in the Dark 🔦 — *learn the light sensor!*"

    **Something new:** the micro:bit can **feel how light or dark it is** — it has a hidden **light sensor**! Keep it in the light and it's calm 😀, but cover it or turn off the lights and a **ghost appears and wails** 👻. Spooky!

    ```makecode
    auto:ghost-in-dark
    ```

    *How: a `forever` loop checks **`light level`** (0–255 — the LEDs double as a light sensor). Below **50** (dark) → ghost + wail; otherwise calm. A brand-new **input** — the micro:bit's eyes! Drag the light slider in the simulator to test.*

??? example "🕯️ Ghost in the Dark — with a real LED 💡"

    Same idea, now with a **real LED** you wire up: in the dark, an external LED **flickers** like a haunted candle; in the light it's off. 🕯️👻

    Wire an **LED** to pin **P0** (long leg) and **GND** (short leg).

    ```makecode
    auto:ghost-in-dark-led
    ```

    *How: when `light level` is low, `digital write pin P0` flips the LED **on/off at random** (a candle flicker); in the light it stays off. Now it reads a sensor **and** drives a real circuit — a taste of the LED weeks ahead. No LED? Watch the **P0** pin in the simulator.*

## ✅ I did it when…

- ☐ I played **Red Light, Green Light** without getting caught on red. 🚦
- ☐ I won a **Rock-Paper-Scissors** duel over radio. ✊✋✌️
- ☐ *(Legend!)* I built the **auto-caller** or kept **score to 5**. 🏆
- ☐ *(Scientist!)* I used the **light sensor** to make a ghost appear in the dark — on screen and with a **real LED**. 🌑💡

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-6
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** two whole-room **radio** games that carry on from Week 4. Both need **2+ boards on the same group** — decide group numbers as a class. Everyone gets the base game going; fast finishers climb the level-ups.

    **The games:**

    - **🚦 Red Light, Green Light** — one caller broadcasts red/green; players get caught moving on red (accelerometer + `game over`). Level-up: an **auto-caller** that flips at random times.
    - **✊✋✌️ Rock, Paper, Scissors** — a quick solo throw, then a 2-player radio duel that auto-judges; the level-up keeps **score to 5**.

    **Materials**

    - micro:bits — **2+ per group** + USB (radio needs real boards; a single simulator can't test it)
    - **V2** for the built-in speaker; V1 works otherwise
    - open floor space, especially for Red Light, Green Light

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap groups & radio → 25 **Red Light, Green Light** (button caller, then the auto-caller) → 25 **RPS** solo → radio duel → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 20 class tournament — **RPS first-to-5** + **Red Light** rounds → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens in **Blocks**. The games here use groups **2–3**. Coming next: **LED & circuit** projects — lights you wire yourself, toward the Ticklebot and pinball electronics. 💡
