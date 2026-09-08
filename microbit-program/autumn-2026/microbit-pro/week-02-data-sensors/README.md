# Week 2 — Pinball scoreboard 🎯 (part 1)

> This term the Pro crew builds the **brain of a pinball machine** — a little each week. We kick off the build: a quick revision, then the very first piece — a **score that goes up when you hit a target**.

!!! abstract "🎓 What you'll learn today"
    - **variables** — a number you can change (the score)
    - **events** — run code on buttons & touch pins
    - **functions** *(Level up)* — name a job, reuse it
    - **digital input** *(Level 2)* — read a real switch

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="the guessing game counting" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

!!! info "🎯 New to the pinball project?"
    See **[The pinball project](../../pinball/README.md)** for the big picture — the parts of a pinball, how the micro:bit runs each one, and where the build is headed.

## 🎯 What we're making today

The **start** of our pinball scoreboard: touch a target and your **score** goes up — plus a **reset** and a **new game** button. That's the goal for today. Finished early? There's an optional **level-up** ladder that turns it into a real little machine.

*(The 3D-printed pinball body is the other group's job — we build the code.)*

## 🔁 Warm-up — quick revision

A 30-second refresher: a **click counter**. Press **A** and a number goes up. That number is a **variable** — exactly how a score works.

*🎓 Concept: **variables** — a number you can change.*

??? example "👀 Run it, or read the code"

    === "Blocks"

        ```makecode
        auto:warmup
        ```

    === "JavaScript"

        ```javascript
        let count = 0
        input.onButtonPressed(Button.A, function () {
            count += 1
            basic.showNumber(count)
        })
        ```

    === "Python"

        ```python
        count = 0
        def on_button_pressed_a():
            global count
            count += 1
            basic.show_number(count)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        ```

## ▶️ Build it — score on touch

Make touching **P0** add points and show the score.

*🎓 Concept: **events** + **input** — a touch pin changes a variable.*

1. Make a **variable** called `score` (starts at 0).
2. From **Input**, use **`on pin P0 pressed`**.
3. Inside it: **change `score` by 10**, then **show number `score`**.

Click **P0** in the sim (or touch the real pin) — watch it climb! 🔢

!!! tip "🔌 On the real board — use the shield"
    Slot your micro:bit into the **Keyestudio sensor shield** so every pin becomes an easy socket, then clip a wire from the metal target to **P0** and one to **GND**. *(Without the shield you can only reach the big **P0/P1/P2** pads.)* Full how-to: **[Meet the gear](../../gear/README.md#wiring-a-touch-target-for-our-pinball)**.

??? example "👀 Run it, or read the code"

    === "Blocks"

        ```makecode
        auto
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        input.onPinPressed(TouchPin.P0, function () {
            score += 10
            basic.showNumber(score)
        })
        ```

    === "Python"

        ```python
        score = 0
        def on_pin_pressed_p0():
            global score
            score += 10
            basic.show_number(score)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
        ```

## 🪜 Make it playable (today's goal)

Two small steps and you've got a real mini-game.

*🎓 Concept: **events** — buttons A/B control the game.*

**① Reset** ♻️ — press **A** to set the score back to 0.

??? example "👀 Peek — run it, or read the code"

    === "Blocks"

        ```makecode
        auto:rung-1
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        input.onPinPressed(TouchPin.P0, function () {
            score += 10
            basic.showNumber(score)
        })
        input.onButtonPressed(Button.A, function () {
            score = 0
            basic.showNumber(0)
        })
        ```

    === "Python"

        ```python
        score = 0
        def on_pin_pressed_p0():
            global score
            score += 10
            basic.show_number(score)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

        def on_button_pressed_a():
            global score
            score = 0
            basic.show_number(0)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        ```

**② New game** 🆕 — press **B** to reset and flash **GO**.

??? example "👀 Peek — run it, or read the code"

    === "Blocks"

        ```makecode
        auto:rung-2
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        input.onPinPressed(TouchPin.P0, function () {
            score += 10
            basic.showNumber(score)
        })
        input.onButtonPressed(Button.A, function () {
            score = 0
            basic.showNumber(0)
        })
        input.onButtonPressed(Button.B, function () {
            score = 0
            basic.showString("GO")
        })
        ```

    === "Python"

        ```python
        score = 0
        def on_pin_pressed_p0():
            global score
            score += 10
            basic.show_number(score)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

        def on_button_pressed_a():
            global score
            score = 0
            basic.show_number(0)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def on_button_pressed_b():
            global score
            score = 0
            basic.show_string("GO")
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

## 🕹️ Level up toward the real machine *(optional)*

Finished the goal? Keep going — each step adds a real pinball feature. By the end you have a little machine you can actually play.

*🎓 Concept: **functions** — name a job, reuse it.*

**③ Second target** 🎯 — wire a metal to **P1**, worth **50**.

??? example "👀 Peek — run it, or read the code"

    === "Blocks"

        ```makecode
        auto:rung-3
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        input.onPinPressed(TouchPin.P0, function () {
            score += 10
            basic.showNumber(score)
        })
        input.onPinPressed(TouchPin.P1, function () {
            score += 50
            basic.showNumber(score)
        })
        input.onButtonPressed(Button.A, function () {
            score = 0
            basic.showNumber(0)
        })
        input.onButtonPressed(Button.B, function () {
            score = 0
            basic.showString("GO")
        })
        ```

    === "Python"

        ```python
        score = 0
        def on_pin_pressed_p0():
            global score
            score += 10
            basic.show_number(score)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

        def on_pin_pressed_p1():
            global score
            score += 50
            basic.show_number(score)
        input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

        def on_button_pressed_a():
            global score
            score = 0
            basic.show_number(0)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def on_button_pressed_b():
            global score
            score = 0
            basic.show_string("GO")
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

**④ Ding on a hit** 🔊 — play a short beep each time you score. We tidy the scoring into one **function** so the sound lives in a single place. *(Needs a micro:bit **V2** speaker, or a buzzer.)*

??? example "👀 Peek — run it, or read the code"

    === "Blocks"

        ```makecode
        auto:rung-4
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        function addPoints (points: number) {
            score += points
            music.playTone(988, 100)
            basic.showNumber(score)
        }
        input.onPinPressed(TouchPin.P0, function () {
            addPoints(10)
        })
        input.onPinPressed(TouchPin.P1, function () {
            addPoints(50)
        })
        input.onButtonPressed(Button.A, function () {
            score = 0
            basic.showNumber(0)
        })
        input.onButtonPressed(Button.B, function () {
            score = 0
            basic.showString("GO")
        })
        ```

    === "Python"

        ```python
        score = 0
        def add_points(points: number):
            global score
            score += points
            music.play_tone(988, 100)
            basic.show_number(score)

        def on_pin_pressed_p0():
            add_points(10)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

        def on_pin_pressed_p1():
            add_points(50)
        input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

        def on_button_pressed_a():
            global score
            score = 0
            basic.show_number(0)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def on_button_pressed_b():
            global score
            score = 0
            basic.show_string("GO")
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

**⑤ 3 balls & game over** 🎱 — a **drain** target (**P2**) costs you a ball; at **0** it shows **OVER** and your final score. **B** gives you 3 fresh balls.

??? example "👀 Peek — run it, or read the code"

    === "Blocks"

        ```makecode
        auto:rung-5
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        let balls = 3
        function addPoints (points: number) {
            score += points
            music.playTone(988, 100)
            basic.showNumber(score)
        }
        input.onPinPressed(TouchPin.P0, function () {
            addPoints(10)
        })
        input.onPinPressed(TouchPin.P1, function () {
            addPoints(50)
        })
        input.onPinPressed(TouchPin.P2, function () {
            balls += -1
            if (balls <= 0) {
                basic.showString("OVER")
                basic.showNumber(score)
            } else {
                basic.showString("BALL")
                basic.showNumber(balls)
            }
        })
        input.onButtonPressed(Button.A, function () {
            score = 0
            basic.showNumber(0)
        })
        input.onButtonPressed(Button.B, function () {
            score = 0
            balls = 3
            basic.showString("GO")
        })
        ```

    === "Python"

        ```python
        score = 0
        balls = 3
        def add_points(points: number):
            global score
            score += points
            music.play_tone(988, 100)
            basic.show_number(score)

        def on_pin_pressed_p0():
            add_points(10)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

        def on_pin_pressed_p1():
            add_points(50)
        input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

        def on_pin_pressed_p2():
            global balls
            balls += -1
            if balls <= 0:
                basic.show_string("OVER")
                basic.show_number(score)
            else:
                basic.show_string("BALL")
                basic.show_number(balls)
        input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

        def on_button_pressed_a():
            global score
            score = 0
            basic.show_number(0)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def on_button_pressed_b():
            global score, balls
            score = 0
            balls = 3
            basic.show_string("GO")
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

**⑥ 🏆 Boss — TILT!** — shake it too hard and you **lose a ball**. Now it's a real little machine: two targets, a ding, three balls, a drain, TILT, reset and new game.

??? example "👀 Peek — run it, or read the code"

    === "Blocks"

        ```makecode
        auto:rung-6
        ```

    === "JavaScript"

        ```javascript
        let score = 0
        let balls = 3
        function addPoints (points: number) {
            score += points
            music.playTone(988, 100)
            basic.showNumber(score)
        }
        function loseBall () {
            balls += -1
            if (balls <= 0) {
                basic.showString("OVER")
                basic.showNumber(score)
            } else {
                basic.showString("BALL")
                basic.showNumber(balls)
            }
        }
        input.onPinPressed(TouchPin.P0, function () {
            addPoints(10)
        })
        input.onPinPressed(TouchPin.P1, function () {
            addPoints(50)
        })
        input.onPinPressed(TouchPin.P2, function () {
            loseBall()
        })
        input.onGesture(Gesture.Shake, function () {
            basic.showString("TILT")
            loseBall()
        })
        input.onButtonPressed(Button.A, function () {
            score = 0
            basic.showNumber(0)
        })
        input.onButtonPressed(Button.B, function () {
            score = 0
            balls = 3
            basic.showString("GO")
        })
        ```

    === "Python"

        ```python
        score = 0
        balls = 3
        def add_points(points: number):
            global score
            score += points
            music.play_tone(988, 100)
            basic.show_number(score)

        def lose_ball():
            global balls
            balls += -1
            if balls <= 0:
                basic.show_string("OVER")
                basic.show_number(score)
            else:
                basic.show_string("BALL")
                basic.show_number(balls)

        def on_pin_pressed_p0():
            add_points(10)
        input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

        def on_pin_pressed_p1():
            add_points(50)
        input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

        def on_pin_pressed_p2():
            lose_ball()
        input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

        def on_gesture_shake():
            basic.show_string("TILT")
            lose_ball()
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)

        def on_button_pressed_a():
            global score
            score = 0
            basic.show_number(0)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def on_button_pressed_b():
            global score, balls
            score = 0
            balls = 3
            basic.show_string("GO")
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

## ⚡ Level 2 — wire up more targets *(optional)*

**Why?** So far your targets are the **3 touch pins** (P0/P1/P2). A real pinball has *loads* of targets, bumpers and lanes — and every one is just a tiny **switch the ball closes**. Level 2 is how you **wire and read your own switches**, so your machine can grow as big as you want. This is the real electronics the lights and flippers plug into later. 🔌

Build it up **one small step at a time** — each step adds just a little. 🌱

*🎓 Concept: **digital input** + **loops** (`forever`) + **state**.*

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

## ✅ I did it when…

- ☐ Touching **P0** makes the **score** go up on screen.
- ☐ **A** resets, and **B** starts a new game.
- ☐ *(Level up!)* A second target, a **ding**, **3 balls** and **TILT** all work.
- ☐ *(Level 2!)* I **read my own switch**, fixed it to **one hit = one point**, and added a **second target** (bonus: rollover lanes).

## 🎉 Kahoot time!

Finish with this week's quiz — **both groups play together**.

```kahoot
week-2
```

---

??? note "👩‍🏫 For helpers — session plan, materials & notes"

    **Goal (today):** revise variables + buttons, then build **score-on-touch** with reset and new game. That's the class target. Rungs ③–⑥ are optional stretch for fast finishers and a preview of the coming weeks — don't feel you must reach them today. **⚡ Level 2** (below the checklist) is a deeper, **electronics-first** stretch — reading your own **switches**, one small step at a time; still **no new parts**, just wires and the shield.

    **Materials**

    - micro:bit (**V2** recommended — capacitive touch on P0/P1/P2 **and** the built-in speaker for the ding) + USB
    - **Keyestudio micro:bit sensor shield**, crocodile-clip / jumper wires, a few metal targets (foil, coins)
    - *(Level 2)* a couple of extra wires (and foil/a button) to make **switch targets** — practise on P0/P1, then real switches on **P8/P9**
    - Laptop/Chromebook — the **simulator is enough** to build & test (click the pins)
    - *(V1 works for scoring — the metal must complete a circuit to **GND**; the ding needs a buzzer.)*

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 project intro + the feature map → 15 revision click counter → 10 wire up / how pin-touch works → 25 build score-on-touch (P0) together → 5 checkpoint
    - **Break (20)**
    - **Block 2 (30):** 15 reset (A) + new game (B) → 5 fast finishers start the level-up ladder → 5 showcase → 5 Kahoot

    **Notes:** only **P0/P1/P2** are touch pads, so P2 doubles as the "drain". Test in the sim by **clicking the pins**. `addPoints`/`loseBall` (④–⑥) are a gentle intro to **functions** (revisited Week 7). This is **part 1** — flippers (servos), lights (NeoPixels), plunger, high score and multiball come later.

    **⚡ Level 2 notes:** an **electronics-first** ladder — *reading a switch*, built up one small step at a time (each embed adds only the new bit, so kids see it grow). The concept: a switch is two wires the ball closes; `set pull pin … up` makes the pin read **1** open / **0** closed, and a `forever` loop watches it. The big teaching moment is **② → ③**: without an edge flag the score races while held; the **`wasClosed`** flag ("only on the change") fixes it — the same trick behind every button and bumper. Steps ①–⑤ practise on **P0/P1** so kids can **press the pads in the simulator**; ⑥ moves the extra switches to spare pins **P8/P9** exactly as on the real board (same blocks, different pin — the sim can't click those, so test ⑥ on hardware or by temporarily reading P0/P1). ⑤ (rollover lanes) adds **ordered state** for a combo. Blocks are shown; **JavaScript/Python** are one click away via **Open & run**. This is the input half of the pinball electronics — it sets up the hardware weeks: 🌈 NeoPixels and 🕹️ servos.
