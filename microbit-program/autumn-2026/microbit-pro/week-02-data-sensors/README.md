# Week 2 — Pinball scoreboard 🎯 (part 1)

**🔗 Open this page on a computer:** go to **[tinyurl.com/mbprow2](https://tinyurl.com/mbprow2)**

> This term the Pro crew builds the **brain of a pinball machine** — a little each week. We kick off the build: a quick revision, then the very first piece — a **score that goes up when you hit a target**.

!!! abstract "🎓 What you'll learn today"
    - **variables** — a number you can change (the score)
    - **events** — run code on buttons & touch pins
    - **functions** *(Level up)* — name a job, reuse it

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

??? note "How it works"

    **Purpose.** A 30-second refresher that proves a **variable** is just a number the board *remembers* — which is exactly how a score works.

    **Think of it like a clicker counter:** a doorman's tally clicker adds one on each press and remembers the running total — a pinball score is the same idea.

    **How the code works:** `count` starts at `0`. `on button A pressed` runs `change count by 1` then `show number count`. The key idea: `count` keeps its value between presses, so each press builds on the last. Swap "count" for "score" and you already have the pinball scoreboard.

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

??? note "How it works"

    **Purpose.** The heart of the whole term's build: a hit on a target makes the **score** climb. Everything later (more targets, balls, TILT, wired switches) hangs off this one idea.

    **In the pinball:** this *is* a **bumper** — the ball touches the target and the points ring up. The pin "touch" is the ball closing a contact.

    **How the code works:**

    - `score` is a variable starting at `0`.
    - `on pin P0 pressed` is an **event** fired when the metal target completes a circuit (P0 → your hand/ball → **GND**). Inside: `change score by 10`, then `show number score`.
    - **Reset (A)** sets `score` back to 0; **New game (B)** resets it and flashes `GO` — two more button events.

    **Watch for:** in the simulator, *click* the P0 pin to fake a touch. On hardware, the touch must reach **GND** — a **V2** senses this capacitively on P0/P1/P2; a **V1** needs the metal to actually close a circuit to a GND pin.

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

??? note "How it works"

    **Purpose.** Once there are several targets and rules, copy-pasting the same lines everywhere gets fragile. A **function** lets you name a job once and reuse it — the first real "software design" idea of the course.

    **Think of it like a rubber stamp:** carve the stamp once (the function), then every bumper stamps its points the same way — re-cut the stamp and all of them change at once.

    **How the code works:**

    - `addPoints(points)` is a function holding the three lines every target needs: `change score`, play the **ding**, `show number`. Each target just calls `addPoints(10)` or `addPoints(50)` instead of repeating them.
    - `loseBall()` is a second function: it subtracts a ball, and with an `if / else` shows **OVER** + the final score when balls reach 0, otherwise how many are left. Both the **drain (P2)** and **TILT (shake)** call `loseBall()`, so "lose a ball" behaves identically wherever it's triggered.
    - `score` and `balls` are variables the functions read and update.

    **Watch for:** the payoff is *change one place, fixed everywhere* — e.g. edit the ding inside `addPoints` and every target updates. Rungs ③–⑥ are optional stretch; functions come back properly in Week 7.

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

## ⚡ Next week — wire up your own switches

**[Week 3 — Pinball switches](../week-03-pinball-switches/README.md)** picks the build straight back up. So far your targets are the **3 touch pins** (P0/P1/P2); a real pinball has *loads* of targets, bumpers and lanes — and every one is just a tiny **switch the ball closes**. Next week is the **electronics-first** ladder: wire and read your own switches so your machine can grow as big as you want. Finished today's goal and the level-up ladder? Take a peek. 🔌

## ✅ I did it when…

- ☐ Touching **P0** makes the **score** go up on screen.
- ☐ **A** resets, and **B** starts a new game.
- ☐ *(Level up!)* A second target, a **ding**, **3 balls** and **TILT** all work.

## 🎉 Kahoot time!

Finish with this week's quiz — **both groups play together**.

```kahoot
week-2
```

---

??? note "👩‍🏫 For helpers — session plan, materials & notes"

    **Goal (today):** revise variables + buttons, then build **score-on-touch** with reset and new game. That's the class target. Rungs ③–⑥ are optional stretch for fast finishers and a preview of the coming weeks — don't feel you must reach them today. The deeper, **electronics-first** stretch — reading your own **switches** — has moved to **[Week 3 — Pinball switches](../week-03-pinball-switches/README.md)**, so today stays focused on getting everyone scoring.

    **Materials**

    - micro:bit (**V2** recommended — capacitive touch on P0/P1/P2 **and** the built-in speaker for the ding) + USB
    - **Keyestudio micro:bit sensor shield**, crocodile-clip / jumper wires, a few metal targets (foil, coins)
    - Laptop/Chromebook — the **simulator is enough** to build & test (click the pins)
    - *(V1 works for scoring — the metal must complete a circuit to **GND**; the ding needs a buzzer.)*

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 project intro + the feature map → 15 revision click counter → 10 wire up / how pin-touch works → 25 build score-on-touch (P0) together → 5 checkpoint
    - **Break (20)**
    - **Block 2 (30):** 15 reset (A) + new game (B) → 5 fast finishers start the level-up ladder → 5 showcase → 5 Kahoot

    **Notes:** only **P0/P1/P2** are touch pads, so P2 doubles as the "drain". Test in the sim by **clicking the pins**. `addPoints`/`loseBall` (④–⑥) are a gentle intro to **functions** (revisited Week 7). This is **part 1** — the **switch-reading** ladder is now **[Week 3](../week-03-pinball-switches/README.md)**; flippers (servos), lights (NeoPixels), plunger, high score and multiball come later.
