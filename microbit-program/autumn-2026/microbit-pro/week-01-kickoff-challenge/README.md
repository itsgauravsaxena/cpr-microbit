# Week 1 — Pinball scoreboard 🎯 (part 1)

> This term the Pro crew builds the **brain of a pinball machine** — a little each week. First class: a quick revision, then the very first piece — a **score that goes up when you hit a target**.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="the guessing game counting" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## 🎯 What we're making today

The **start** of our pinball scoreboard: touch a target and your **score** goes up — plus a **reset** and a **new game** button. That's the goal for today. Finished early? There's an optional **level-up** ladder that turns it into a real little machine.

*(The 3D-printed pinball body is the other group's job — we build the code.)*

## 🎮 The parts of a pinball

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg viewBox="0 0 360 500" width="100%" style="max-width:340px;height:auto;display:block;margin:0 auto;" role="img" aria-label="Parts of a pinball machine" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="90" y="45" width="180" height="415" rx="16" fill="#20486e" stroke="#c8a24a" stroke-width="3"/>
<path d="M96 110 Q180 55 264 110" fill="none" stroke="#3d6a95" stroke-width="4"/>
<rect x="120" y="28" width="120" height="28" rx="5" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<text x="180" y="47" font-size="14" fill="#ffd23f" text-anchor="middle" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">SCORE 120</text>
<line x1="238" y1="110" x2="238" y2="440" stroke="#3d6a95" stroke-width="3"/>
<circle cx="250" cy="95" r="7" fill="#d7dbe1" stroke="#9aa0aa"/>
<rect x="243" y="426" width="14" height="18" rx="3" fill="#c0c4cc" stroke="#8a8f98"/>
<path d="M250 444 l-7 5 l14 5 l-14 5" fill="none" stroke="#8a8f98" stroke-width="2"/>
<circle cx="135" cy="150" r="20" fill="#e63946"/><circle cx="135" cy="150" r="8" fill="#fff"/>
<circle cx="198" cy="124" r="20" fill="#e63946"/><circle cx="198" cy="124" r="8" fill="#fff"/>
<circle cx="160" cy="205" r="18" fill="#e63946"/><circle cx="160" cy="205" r="7" fill="#fff"/>
<rect x="114" y="262" width="18" height="10" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="142" y="262" width="18" height="10" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="170" y="262" width="18" height="10" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<circle cx="150" cy="320" r="9" fill="#d7dbe1" stroke="#9aa0aa"/><circle cx="147" cy="317" r="2.5" fill="#fff"/>
<rect x="132" y="406" width="50" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(-22 137 414)"/>
<rect x="140" y="406" width="50" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(22 223 414)"/>
<rect x="160" y="446" width="40" height="14" rx="3" fill="#0a1a2a"/>
<path d="M180 428 l-7 12 l14 0 z" fill="#0a1a2a" opacity="0.6"/>
<line x1="86" y1="150" x2="115" y2="150" stroke="#c8a24a" stroke-width="1.5"/>
<text x="84" y="150" font-size="13" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🔴 Bumpers</text>
<line x1="86" y1="270" x2="112" y2="268" stroke="#c8a24a" stroke-width="1.5"/>
<text x="84" y="270" font-size="13" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎯 Targets</text>
<line x1="86" y1="420" x2="120" y2="414" stroke="#c8a24a" stroke-width="1.5"/>
<text x="84" y="420" font-size="13" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🕹️ Flippers</text>
<line x1="262" y1="436" x2="276" y2="436" stroke="#c8a24a" stroke-width="1.5"/>
<text x="278" y="436" font-size="13" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🚀 Plunger</text>
<line x1="240" y1="45" x2="274" y2="45" stroke="#c8a24a" stroke-width="1.5"/>
<text x="276" y="45" font-size="13" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🔢 Score</text>
<text x="180" y="490" font-size="13" fill="var(--md-default-fg-color)" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif">🎱 Drain</text>
<line x1="180" y1="462" x2="180" y2="480" stroke="#c8a24a" stroke-width="1.5"/>
</svg>
</div>

- 🚀 **Plunger** — launches the ball onto the field.
- 🔴 **Bumpers** — the ball bounces off them and scores.
- 🎯 **Targets** — hit these to score (these are our metal **touch-pins**!).
- 🕹️ **Flippers** — flick the ball back up so it doesn't fall.
- 🎱 **Drain** — the gap at the bottom; if the ball falls in, you lose it.
- 🔢 **Score** — how many points you've got.

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

New to the micro:bit and its pins? Start with **[Meet the gear](../../gear/README.md)** 🔧.

## 🔁 Warm-up — quick revision

A 30-second refresher: a **click counter**. Press **A** and a number goes up. That number is a **variable** — exactly how a score works.

??? example "👀 Run it, or read the code"

    === "Blocks & simulator"

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

1. Make a **variable** called `score` (starts at 0).
2. From **Input**, use **`on pin P0 pressed`**.
3. Inside it: **change `score` by 10**, then **show number `score`**.

Click **P0** in the sim (or touch the real pin) — watch it climb! 🔢

??? example "👀 Run it, or read the code"

    === "Blocks & simulator"

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

**① Reset** ♻️ — press **A** to set the score back to 0.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

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

    === "Blocks & simulator"

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

**③ Second target** 🎯 — wire a metal to **P1**, worth **50**.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

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

    === "Blocks & simulator"

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

    === "Blocks & simulator"

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

    === "Blocks & simulator"

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

## 🔭 Where we're headed

Over the term the machine keeps growing:

- 🕹️ **Flippers** — buttons A/B drive **servos** that flip
- 🚀 **Plunger / launch** — a button (later a servo) to fire the ball
- 🌈 **Playfield lights** — a **NeoPixel** strip that flashes on hits
- 🏆 **High score** — remember the best game
- ✨ **Bonus & multiball** — combos, multipliers, extra balls
- 😴 **Attract mode** — scroll "PLAY!" when the machine is idle

## ✅ I did it when…

- ☐ Touching **P0** makes the **score** go up on screen.
- ☐ **A** resets, and **B** starts a new game.
- ☐ *(Level up!)* A second target, a **ding**, **3 balls** and **TILT** all work.

## 🎉 Kahoot time!

Finish with this week's quiz — **both groups play together**.

```kahoot
week-1
```

---

??? note "👩‍🏫 For helpers — session plan, materials & notes"

    **Goal (today):** revise variables + buttons, then build **score-on-touch** with reset and new game. That's the class target. Rungs ③–⑥ are optional stretch for fast finishers and a preview of the coming weeks — don't feel you must reach them today.

    **Materials**

    - micro:bit (**V2** recommended — capacitive touch on P0/P1/P2 **and** the built-in speaker for the ding) + USB
    - **Keyestudio micro:bit sensor shield**, crocodile-clip / jumper wires, a few metal targets (foil, coins)
    - Laptop/Chromebook — the **simulator is enough** to build & test (click the pins)
    - *(V1 works for scoring — the metal must complete a circuit to **GND**; the ding needs a buzzer.)*

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 project intro + the feature map → 15 revision click counter → 10 wire up / how pin-touch works → 25 build score-on-touch (P0) together → 5 checkpoint
    - **Break (20)**
    - **Block 2 (30):** 15 reset (A) + new game (B) → 5 fast finishers start the level-up ladder → 5 showcase → 5 Kahoot

    **Notes:** only **P0/P1/P2** are touch pads, so P2 doubles as the "drain". Test in the sim by **clicking the pins**. `addPoints`/`loseBall` (④–⑥) are a gentle intro to **functions** (revisited Week 7). This is **part 1** — flippers (servos), lights (NeoPixels), plunger, high score and multiball come later.
