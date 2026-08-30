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
<svg viewBox="0 0 400 700" width="100%" style="max-width:340px;height:auto;display:block;margin:0 auto;" role="img" aria-label="Parts of a pinball machine and where the micro:bit fits" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="105" y="70" width="190" height="450" rx="18" fill="#20486e" stroke="#c8a24a" stroke-width="3"/>
<path d="M112 150 Q200 90 288 150" fill="none" stroke="#3d6a95" stroke-width="4"/>
<rect x="135" y="44" width="130" height="30" rx="6" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<text x="200" y="65" font-size="15" fill="#ffd23f" text-anchor="middle" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">SCORE 120</text>
<line x1="262" y1="150" x2="262" y2="505" stroke="#3d6a95" stroke-width="3"/>
<circle cx="278" cy="120" r="7" fill="#d7dbe1" stroke="#9aa0aa"/>
<rect x="271" y="486" width="14" height="18" rx="3" fill="#c0c4cc" stroke="#8a8f98"/>
<path d="M278 504 l-7 5 l14 5 l-14 5" fill="none" stroke="#8a8f98" stroke-width="2"/>
<circle cx="152" cy="190" r="21" fill="#e63946"/><circle cx="152" cy="190" r="8" fill="#fff"/>
<circle cx="222" cy="158" r="21" fill="#e63946"/><circle cx="222" cy="158" r="8" fill="#fff"/>
<circle cx="188" cy="262" r="21" fill="#e63946"/><circle cx="188" cy="262" r="8" fill="#fff"/>
<rect x="150" y="330" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="184" y="330" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="218" y="330" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<circle cx="168" cy="400" r="9" fill="#d7dbe1" stroke="#9aa0aa"/><circle cx="165" cy="397" r="2.5" fill="#fff"/>
<rect x="145" y="477" width="46" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(-26 145 485)"/>
<rect x="209" y="477" width="46" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(26 255 485)"/>
<rect x="182" y="503" width="36" height="14" rx="3" fill="#0a1a2a"/>
<path d="M200 486 l-8 12 l16 0 z" fill="#0a1a2a" opacity="0.55"/>
<path d="M184 341 C 150 430, 150 500, 175 560" fill="none" stroke="#ffd23f" stroke-width="2" stroke-dasharray="4 4"/>
<rect x="115" y="545" width="170" height="105" rx="12" fill="#2b3038" stroke="#c8a24a" stroke-width="2"/>
<rect x="140" y="560" width="120" height="72" rx="9" fill="#1f6fb2" stroke="#0d4a7a" stroke-width="2"/>
<rect x="158" y="568" width="84" height="46" rx="7" fill="#0f1419" stroke="#c8a24a" stroke-width="1.5"/>
<rect x="166" y="573" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="179" y="573" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="192" y="573" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="205" y="573" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="218" y="573" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="166" y="581" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="179" y="581" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="192" y="581" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="205" y="581" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="218" y="581" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="166" y="589" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="179" y="589" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="192" y="589" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="205" y="589" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="218" y="589" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="166" y="597" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="179" y="597" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="192" y="597" width="7" height="6" rx="1.5" fill="#ff4d4d"/>
<rect x="205" y="597" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="218" y="597" width="7" height="6" rx="1.5" fill="#2b3038"/>
<rect x="176" y="606" width="12" height="6" rx="1" fill="#ffd23f"/>
<rect x="196" y="606" width="12" height="6" rx="1" fill="#ffd23f"/>
<rect x="216" y="606" width="12" height="6" rx="1" fill="#ffd23f"/>
<line x1="98" y1="190" x2="131" y2="190" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="190" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🔴 Bumpers</text>
<line x1="98" y1="335" x2="148" y2="335" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="335" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎯 Targets</text>
<line x1="98" y1="486" x2="150" y2="484" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="486" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🕹️ Flippers</text>
<line x1="286" y1="120" x2="302" y2="120" stroke="#c8a24a" stroke-width="1.5"/>
<text x="304" y="120" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🚀 Plunger</text>
<line x1="266" y1="60" x2="302" y2="60" stroke="#c8a24a" stroke-width="1.5"/>
<text x="304" y="60" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🔢 Score</text>
<line x1="98" y1="510" x2="182" y2="510" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="510" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎱 Drain</text>
<text x="200" y="675" font-size="14" fill="var(--md-default-fg-color)" text-anchor="middle" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">🧠 micro:bit + shield slot in here</text>
</svg>
</div>

- 🚀 **Plunger** — launches the ball onto the field.
- 🔴 **Bumpers** — the ball bounces off them and scores.
- 🎯 **Targets** — hit these to score (these are our metal **touch-pins**!).
- 🕹️ **Flippers** — flick the ball back up so it doesn't fall.
- 🎱 **Drain** — the gap at the bottom; if the ball falls in, you lose it.
- 🔢 **Score** — how many points you've got.
- 🧠 **micro:bit + shield** — the **brain**, tucked in the base. Every target wires back to it, and its little screen shows the score.

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
