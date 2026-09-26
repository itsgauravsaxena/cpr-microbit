# Week 4 — Game Lab 📡

> Now the micro:bits **talk to each other**! Build a remote control 🎮, and play **Hot or Cold**, **Red Light Green Light** and **Rock-Paper-Scissors** — all over the air. 📡

!!! abstract "🎓 What you'll learn today"
    - **radio** — send, receive, and share a **group** (channel)
    - **roles** — a **transmitter** and a **receiver**
    - **signal strength** — how radio fades with distance
    - the **accelerometer** — catching movement

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a heart beating on the LED screen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" dur="1.4s" repeatCount="indefinite" values="1;0.3;1" keyTimes="0;0.5;1"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

## 🎮 Pick a game

Every game here uses **two or more micro:bits** talking over **radio**. Flash a program onto each board, then play! New here? The earlier **[Game Lab](../microbit-beginners/week-03-game-lab-2/README.md)** has the on-board games. 🌱

### 📡 Transmitter & Receiver

So far both boards do the **same** job. Now give them **different** jobs: one board is the **transmitter** (the remote) and the other is the **receiver** (the toy). Flash a different program onto each! 🎮

*🎓 Concept: **roles** — a sender and a listener, like a TV remote and a TV.*

!!! tip "Two micro:bits, two *different* programs"
    Put **`TX`** (transmitter) on one board and **`RX`** (receiver) on the other — both on the **same group**. The remote board's buttons now control the other board's screen!

??? example "👀 See the two programs"

    **📤 Transmitter (the remote)** — press A/B or shake to send a command:

    ```makecode
    auto:tx
    ```

    **📥 Receiver (the toy)** — reacts to whatever the remote sends:

    ```makecode
    auto:rx
    ```

??? example "🔥 Hot or Cold — radio treasure hunt"

    A classic! One board is a hidden **treasure** that keeps beeping out a signal; the other is a **detector** whose face gets happier the closer you are. Hide the treasure, then find it! 💎

    **💎 Treasure (transmitter)** — hide this one somewhere in the room:

    ```makecode
    auto:beacon
    ```

    **🔍 Detector (receiver)** — walk around: 😢 cold → 😕 → 😀 → 💗 red-hot!

    ```makecode
    auto:detector
    ```

??? note "How it works"

    **Think of it like a TV remote — and a game of hotter-colder.**

    - **Remote control** — the **transmitter** only *sends* (button/shake → `radio send number`); the **receiver** only *listens* (*on radio received* → shows an arrow or a face). Splitting the two jobs is what makes a real remote control.
    - **Treasure hunt** — the treasure `sends` a signal over and over in a `forever` loop. The detector reads how **strong** the signal is (`received packet signal strength`): a strong signal means you're close, so it shows a happier face. Radio gets weaker with distance — that's what makes it "hotter/colder."

    **Watch for:** two **different** programs, both on the **same group**. The treasure hunt really needs **real boards** and room to move — signal strength barely changes in the simulator.

??? example "🚀 Level up — remote-controlled dot"

    Turn the remote into a real controller: **tilt** the transmitter and a dot slides across the receiver's screen. 🎮

    **📤 Transmitter (tilt it)** — sends how far it's tilted, over and over:

    ```makecode
    auto:tx-tilt
    ```

    **📥 Receiver (the screen)** — a dot moves left/right to match the tilt:

    ```makecode
    auto:rx-move
    ```

    *How: the transmitter `sends` its **acceleration (X)** in a `forever` loop; the receiver **maps** that number to a dot position (0–4) and moves a **sprite**. Live sensor data over radio!*

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

## ✅ I did it when…

- ☐ I built a **remote control** — a transmitter and a receiver. 🎮
- ☐ I played **Hot or Cold** and found the hidden treasure. 💎
- ☐ *(Legend!)* I won **Red Light Green Light** or an **RPS** duel. 🏆

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-4
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** the **radio & multiplayer** session — every game needs **2+ boards on the same group**. This is the highlight of the term: kids' boards *talk to each other*. Bring plenty of paired boards and decide group numbers as a class so pairs don't clash. There's deliberately **more here than fits one session**. 🎯

    **The games (easy → hard):**

    - **📡 Transmitter & Receiver** — *roles*: one board sends, one listens. Includes **🔥 Hot or Cold** (signal strength — the room treasure hunt).
    - **🚦 Red Light, Green Light** — one caller broadcasts red/green; players get caught moving on red (accelerometer + `game over`).
    - **✊✋✌️ Rock, Paper, Scissors** — a quick solo throw, then a 2-player radio duel that auto-judges the winner.

    **Materials**

    - micro:bits — **at least 2 per pair/group** + USB (radio needs real boards; a single simulator can't test it)
    - **V2** boards give a built-in speaker for the message "beep"; V1 works otherwise
    - room to move for **Hot or Cold** and **Red Light, Green Light**

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 10 how radio & groups work → 25 build the **Transmitter & Receiver** remote (matching groups) → 20 the **Hot or Cold** treasure hunt → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 20 whole-room games — **Hot or Cold**, **Red Light Green Light**, **RPS duel** → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens straight into **Blocks**. Radio games use **group numbers** — decide them as a class so pairs don't clash (the games here use groups 1–3). Games that read **signal strength** or need space (**Hot or Cold**, **Red Light**) really want **real boards**. Coming next: **[Week 5 — Hot or Cold](../week-05-hot-or-cold/README.md)** goes deeper on the treasure hunt (a smarter detector), then **LED & circuit** projects — lights you wire yourself, toward the Ticklebot and pinball electronics. 💡
