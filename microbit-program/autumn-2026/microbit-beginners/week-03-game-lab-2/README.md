# Week 3 — Game Lab 2 🎮

> Back to the Game Lab! Last week you built the dice 🎲 — now make **music** 🎵, send **secret radio messages** 📻, and build a **fortune teller** 🔮.

!!! abstract "🎓 What you'll learn today"
    - **radio** — two micro:bits talking to each other
    - the **Music** blocks — melodies & notes
    - more **`if / else`** — choosing between answers

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a heart beating on the LED screen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" dur="1.4s" repeatCount="indefinite" values="1;0.3;1" keyTimes="0;0.5;1"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

## 🎮 Pick a game

Pick a game, build the blocks, play it. Each one has a **🔨 Build it** with a simple starter, then the full game. New here? **[Week 2](../week-02-name-tag-smiley-buttons/README.md)** has the warm-up and the dice. 🌱

### 🎵 Music Maker

Buttons make music. Shake for a surprise tune! 🎵 *(turn the sound up 🔊)*

*🎓 Concept: the **Music** blocks — melodies & notes.*

??? note "How it works"

    **Purpose.** Loud and motivating. It shows that each **event** can trigger a different sound, and introduces the **Music** block category.

    **Think of it like a soundboard:** each button is a pad that fires its own clip — press a different pad, hear a different sound.

    **How the code works:**

    - Three events run the show: `on button A`, `on button B`, and `on shake`.
    - Each one calls `start melody` with a **built-in tune** (Ba Ding, Jump Up, Nyan) set to play **once**.
    - The shake version also flashes an eighth-note ♪ icon first, then plays the surprise song — a quick way to show you can stack two actions in one event.

    **Watch for:** it needs sound — a micro:bit **V2** has a built-in speaker; on **V1** or a quiet room, plug headphones/a buzzer into pin 0. A melody plays to the end, but a new button press starts a different one over it.

??? example "👀 See the finished game"

    ```makecode
    auto:music
    ```

??? example "🔨 Build it — 3 small steps"

    **① Press A** — one button, one sound:

    ```makecode
    auto:music-1
    ```

    **② Add B** — a second button with a different tune:

    ```makecode
    auto:music-2
    ```

    **③ Shake surprise** — add a **shake** → a music note 🎵 and a surprise song:

    ```makecode
    auto:music
    ```

### 📻 Secret Messages

Send hearts 💗 and smileys 😀 to a friend's micro:bit — over the air! 📻

*🎓 Concept: **radio** — send & receive between micro:bits.*

!!! tip "You need **two** micro:bits"
    You and your partner both use the **same group number** (change the `1` in *set group*). Pick your own so you don't cross wires with the next pair!

??? note "How it works"

    **Purpose.** The magic moment of the term — two boards talk *wirelessly*. It teaches **send**, **receive**, and the idea of a shared **group** (channel).

    **Think of it like walkie-talkies:** you only hear each other if you're both tuned to the same channel — that's what the group number does.

    **How the code works:**

    - `radio set group 1` at the start puts the board on a channel. Only boards on the **same group number** can hear each other.
    - `on button A` → `send number 1`; `on button B` → `send number 2`. Sending just broadcasts a number into the air.
    - `on radio received (receivedNumber)` is a **new kind of event** — it fires on the *other* board when a number arrives. An `if / else` shows a 💗 for `1` and a 😀 for `2`.
    - Both partners flash the **same** program, so each board can both send and receive.

    **Watch for:** you need **2 boards per pair**, both on the same group. Decide group numbers as a class (pair 1 → group 1, pair 2 → group 2 …) so signals don't cross. Radio can't be tested with a single simulator — this one needs real boards.

??? example "👀 See the finished game"

    ```makecode
    auto:radio
    ```

??? example "🔨 Build it — 3 small steps"

    **① Send + show** — set your **group**, press **A** to send, show a 💗 when a message arrives:

    ```makecode
    auto:radio-1
    ```

    **② Second button** — add **B** so you can send two different messages:

    ```makecode
    auto:radio-2
    ```

    **③ Two pictures** — use `if / else` so **A** shows a heart 💗 and **B** a smiley 😀:

    ```makecode
    auto:radio
    ```

### 🔮 Fortune Teller

Ask a yes/no question, give it a shake, and see what it says! 🔮

*🎓 Concept: **`if / else if`** — choosing between answers.*

??? note "How it works"

    **Purpose.** Silly and social — kids love asking it questions. It's extra `if / else if` practice using only icons (no slow scrolling text).

    **Think of it like a Magic 8-Ball:** shake it, wait while it "thinks," and get one of a few set answers back.

    **How the code works:**

    - `on shake` shows a "thinking" 😴 icon and `pause 500 ms` — the little delay is what makes it feel like the micro:bit is *pondering*.
    - `pick random 0 to 3` stores a number in a variable (`pick`).
    - An `if / else if` chain maps each value to an answer: 0 → Yes ✓, 1 → No ✗, 2 → 🤔, 3 → 😀 — **four** possible outcomes.

    **Watch for:** four answers come from `0 to 3` (four values, counting from zero). To add a fifth answer, widen the range to `0 to 4` *and* add one more `else if`.

??? example "👀 See the finished game"

    ```makecode
    auto:fortune
    ```

??? example "🔨 Build it — 3 small steps"

    **① Yes or No** — shake → ✓ or ✗ (your first `if / else`):

    ```makecode
    auto:fortune-1
    ```

    **② Add Maybe** — a third answer 🤔 with `else if`:

    ```makecode
    auto:fortune-2
    ```

    **③ Let it think** — it "thinks" first 😴, then gives one of **four** answers:

    ```makecode
    auto:fortune
    ```

---

## 🌟 Bonus

??? note "How the bonus games work"

    **Purpose.** Quick extensions for fast finishers — no new concepts, just remixing what they know.

    - **🎨 Draw your own** — `on button A` → `show leds` with a hand-toggled 5×5 pattern. Pure creativity, like pixel-art on an Etch A Sketch.
    - **✊✋✌️ Rock, Paper, Scissors** — `on shake` → `pick random 0 to 2` → an `if / else if` shows a square / full grid / scissors. Same random-plus-choose pattern as the dice, now for a playground duel.
    - **💗 Love Meter** — `on pin P0 pressed` → `show number (pick random 0 to 100)`. The "sensor" is your body: holding **P0** and **GND** completes a circuit — just like the "love tester" grip machines at a fair. (V2 senses touch on P0 directly.)

    Make **button A** light up your own LEDs with **`show leds`** — draw anything!

    ```makecode
    auto:draw
    ```

??? example "✊✋✌️ Rock, Paper, Scissors"

    Shake to throw rock, paper or scissors — then duel a friend, best of five!

    ```makecode
    auto:rps
    ```

??? example "💗 Love Meter"

    Hold **pin 0** with one hand and touch **GND** with the other — the micro:bit shows how 'warm' your fingers are (a random score **0–100**). 💗

    Build it with the 30-second paste trick: open <https://makecode.microbit.org> → **New Project** → click **`{ } JavaScript`**, delete everything, paste this, then click **Blocks**:

    ```javascript
    input.onPinPressed(TouchPin.P0, function () {
        basic.showNumber(Math.randomRange(0, 100))
    })
    ```

## ✅ I did it when…

- ☐ I built **at least one game** (music, radio or fortune teller) and played it.
- ☐ I sent a **secret radio message** to a partner. 📻
- ☐ *(Legend!)* I built **two or more** games — or stumped the Fortune Teller. 🔮

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-3
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** this is the second half of the Game Lab — the games that didn't fit Week 2. Kids pick from a menu of small **games** at their own pace. **📻 Secret Messages** is the highlight: it needs **2 boards per pair**, both on the **same group**. There's deliberately **more here than fits one session** — better too much than too little. 🎯

    **The games (easy → hard):**

    - **🎵 Music Maker** — the Music blocks. Loud and fun (headphones help a full room).
    - **📻 Secret Messages** — **radio**; needs **2 boards per pair**, both on the **same group**. Magical for kids.
    - **🔮 Fortune Teller** — more `if / else` practice, all icons (no slow scrolling text). Silly and social — kids love asking it questions.
    - **🌟 Bonus** — draw-your-own, rock-paper-scissors, and a **💗 Love Meter** (touch pin P0).

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap the dice → 15 build **Music Maker** together → 10 download to the board → 25 pair up for **Secret Messages** (set matching groups) → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 20 free choice from the menu (Fortune Teller, bonus games) at own pace → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens straight into **Blocks**. Each *Build it* shows a simple **starter** first, then the **full** program, so kids grow one program rather than copy finished code. Radio needs matching **group numbers** — decide them as a class so pairs don't clash. The **🚀 Star Catcher** stretch is parked in `archive/week-02-star-catcher/` if anyone wants a bigger challenge.
