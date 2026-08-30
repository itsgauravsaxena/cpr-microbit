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
<svg viewBox="0 0 400 660" width="100%" style="max-width:340px;height:auto;display:block;margin:0 auto;" role="img" aria-label="Pinball parts with the micro:bit in a top backbox holder" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="112" y="26" width="176" height="94" rx="12" fill="#2b3038" stroke="#c8a24a" stroke-width="2"/>
<rect x="140" y="38" width="120" height="66" rx="8" fill="#0f1419" stroke="#c8a24a" stroke-width="1.5"/>
<rect x="176" y="46" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="186" y="46" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="196" y="46" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="206" y="46" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="216" y="46" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="176" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="186" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="196" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="206" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="216" y="56" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="176" y="66" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="186" y="66" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="196" y="66" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="206" y="66" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="216" y="66" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="176" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="186" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="196" y="76" width="7" height="7" rx="1.5" fill="#ff4d4d"/>
<rect x="206" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<rect x="216" y="76" width="7" height="7" rx="1.5" fill="#2b3038"/>
<circle cx="152" cy="72" r="6" fill="#2b3038" stroke="#c8a24a"/><circle cx="248" cy="72" r="6" fill="#2b3038" stroke="#c8a24a"/>
<rect x="180" y="99" width="10" height="5" rx="1" fill="#ffd23f"/>
<rect x="196" y="99" width="10" height="5" rx="1" fill="#ffd23f"/>
<rect x="212" y="99" width="10" height="5" rx="1" fill="#ffd23f"/>
<rect x="176" y="118" width="48" height="20" fill="#2b3038"/>
<rect x="105" y="135" width="190" height="470" rx="18" fill="#20486e" stroke="#c8a24a" stroke-width="3"/>
<path d="M112 215 Q200 158 288 215" fill="none" stroke="#3d6a95" stroke-width="4"/>
<line x1="262" y1="215" x2="262" y2="590" stroke="#3d6a95" stroke-width="3"/>
<circle cx="278" cy="185" r="7" fill="#d7dbe1" stroke="#9aa0aa"/>
<rect x="271" y="571" width="14" height="18" rx="3" fill="#c0c4cc" stroke="#8a8f98"/>
<path d="M278 589 l-7 5 l14 5 l-14 5" fill="none" stroke="#8a8f98" stroke-width="2"/>
<circle cx="152" cy="268" r="21" fill="#e63946"/><circle cx="152" cy="268" r="8" fill="#fff"/>
<circle cx="222" cy="236" r="21" fill="#e63946"/><circle cx="222" cy="236" r="8" fill="#fff"/>
<circle cx="188" cy="338" r="21" fill="#e63946"/><circle cx="188" cy="338" r="8" fill="#fff"/>
<rect x="150" y="405" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="184" y="405" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="218" y="405" width="20" height="11" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<circle cx="168" cy="472" r="9" fill="#d7dbe1" stroke="#9aa0aa"/><circle cx="165" cy="469" r="2.5" fill="#fff"/>
<rect x="145" y="552" width="46" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(-26 145 560)"/>
<rect x="209" y="552" width="46" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(26 255 560)"/>
<rect x="182" y="578" width="36" height="14" rx="3" fill="#0a1a2a"/>
<path d="M200 561 l-8 12 l16 0 z" fill="#0a1a2a" opacity="0.55"/>
<path d="M150 405 C 118 330, 118 190, 176 132" fill="none" stroke="#ffd23f" stroke-width="2" stroke-dasharray="4 4"/>
<line x1="288" y1="72" x2="302" y2="72" stroke="#c8a24a" stroke-width="1.5"/>
<text x="304" y="72" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🧠 micro:bit</text>
<line x1="288" y1="185" x2="302" y2="185" stroke="#c8a24a" stroke-width="1.5"/>
<text x="304" y="185" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🚀 Plunger</text>
<line x1="98" y1="268" x2="131" y2="268" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="268" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🔴 Bumpers</text>
<line x1="98" y1="410" x2="148" y2="410" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="410" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎯 Targets</text>
<line x1="98" y1="560" x2="150" y2="558" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="560" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🕹️ Flippers</text>
<line x1="98" y1="584" x2="182" y2="584" stroke="#c8a24a" stroke-width="1.5"/>
<text x="96" y="584" font-size="13.5" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎱 Drain</text>
<text x="200" y="646" font-size="12.5" fill="var(--md-default-fg-color)" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif">↑ in a 3D-printed holder — the scoreboard + brain</text>
</svg>
</div>

- 🚀 **Plunger** — launches the ball onto the field.
- 🔴 **Bumpers** — the ball bounces off them and scores.
- 🎯 **Targets** — hit these to score (our metal **touch-pins**); thin wires run **up** to the micro:bit.
- 🕹️ **Flippers** — flick the ball back up so it doesn't fall.
- 🎱 **Drain** — the gap at the bottom; if the ball falls in, you lose it.
- 🧠 **micro:bit + shield** — the **brain**, in a **3D-printed holder at the top** (like a real pinball's backbox). Its LED screen is the **🔢 scoreboard**, buttons A/B are reset/new-game — and it's **out of the ball's way**.

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
