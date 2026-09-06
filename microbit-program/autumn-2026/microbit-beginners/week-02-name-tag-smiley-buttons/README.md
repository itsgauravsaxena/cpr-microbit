# Week 2 — Button Faces 😀

> Build a face machine, one step at a time: buttons make faces, a shake gives a surprise, and it greets you when it wakes up.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="220" height="220" viewBox="0 0 216 216" role="img" aria-label="a face changing happy, sad, surprised" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="0" y="0" width="216" height="216" rx="24" fill="#0f1419" stroke="#c8a24a" stroke-width="3"/>
<rect x="17" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#2b3038"/>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
</svg>
</div>

## 🎯 What we're making

Here's the finished program — you'll build up to it, one small step at a time. Press **▶️ Open & run** to play with it:

```makecode
auto
```

## 🧱 Build it — one step at a time

Open each step, add **only the new blocks**, then check your blocks against the picture. Your program grows every step! 🌱

??? example "① Happy face on button A"

    Add **`on button A pressed`** → **`show icon`** and pick 😀 **Happy**. Press A!

    === "Blocks"

        ```makecode
        auto:step-1
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        ```

    === "Python"

        ```python
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        ```

??? example "② Sad face on button B"

    Add another **`on button B pressed`** → **`show icon`** → 🙁 **Sad**.

    === "Blocks"

        ```makecode
        auto:step-2
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            basic.showIcon(IconNames.Sad)
        })
        ```

    === "Python"

        ```python
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        def on_button_pressed_b():
            basic.show_icon(IconNames.SAD)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

??? example "③ Heart when you press A+B"

    Add **`on button A+B pressed`** → **`show icon`** → 💗 **Heart** (press both together).

    === "Blocks"

        ```makecode
        auto:step-3
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            basic.showIcon(IconNames.Sad)
        })
        input.onButtonPressed(Button.AB, function () {
            basic.showIcon(IconNames.Heart)
        })
        ```

    === "Python"

        ```python
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        def on_button_pressed_b():
            basic.show_icon(IconNames.SAD)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        def on_button_pressed_ab():
            basic.show_icon(IconNames.HEART)
        input.on_button_pressed(Button.AB, on_button_pressed_ab)
        ```

??? example "④ Surprise when you shake"

    Add **`on shake`** → **`show icon`** → 😲 **Surprised**. Give it a wiggle!

    === "Blocks"

        ```makecode
        auto:step-4
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            basic.showIcon(IconNames.Sad)
        })
        input.onButtonPressed(Button.AB, function () {
            basic.showIcon(IconNames.Heart)
        })
        input.onGesture(Gesture.Shake, function () {
            basic.showIcon(IconNames.Surprised)
        })
        ```

    === "Python"

        ```python
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        def on_button_pressed_b():
            basic.show_icon(IconNames.SAD)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        def on_button_pressed_ab():
            basic.show_icon(IconNames.HEART)
        input.on_button_pressed(Button.AB, on_button_pressed_ab)
        def on_gesture_shake():
            basic.show_icon(IconNames.SURPRISED)
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```

??? example "⑤ Random face on shake"

    Change the shake so it picks a **random** face — use **pick random** and **if / else**.

    === "Blocks"

        ```makecode
        auto:step-5
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            basic.showIcon(IconNames.Sad)
        })
        input.onButtonPressed(Button.AB, function () {
            basic.showIcon(IconNames.Heart)
        })
        input.onGesture(Gesture.Shake, function () {
            let n = randint(0, 3)
            if (n == 0) {
                basic.showIcon(IconNames.Happy)
            } else if (n == 1) {
                basic.showIcon(IconNames.Sad)
            } else if (n == 2) {
                basic.showIcon(IconNames.Surprised)
            } else {
                basic.showIcon(IconNames.Silly)
            }
        })
        ```

    === "Python"

        ```python
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        def on_button_pressed_b():
            basic.show_icon(IconNames.SAD)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        def on_button_pressed_ab():
            basic.show_icon(IconNames.HEART)
        input.on_button_pressed(Button.AB, on_button_pressed_ab)
        def on_gesture_shake():
            n = randint(0, 3)
            if n == 0:
                basic.show_icon(IconNames.HAPPY)
            elif n == 1:
                basic.show_icon(IconNames.SAD)
            elif n == 2:
                basic.show_icon(IconNames.SURPRISED)
            else:
                basic.show_icon(IconNames.SILLY)
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```

??? example "⑥ Say hi when it starts"

    At the top add **`on start`** → **`show string`** with a greeting (e.g. HEJ!).

    === "Blocks"

        ```makecode
        auto:step-6
        ```

    === "JavaScript"

        ```javascript
        basic.showString("HEJ!")
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            basic.showIcon(IconNames.Sad)
        })
        input.onButtonPressed(Button.AB, function () {
            basic.showIcon(IconNames.Heart)
        })
        input.onGesture(Gesture.Shake, function () {
            let n = randint(0, 3)
            if (n == 0) {
                basic.showIcon(IconNames.Happy)
            } else if (n == 1) {
                basic.showIcon(IconNames.Sad)
            } else if (n == 2) {
                basic.showIcon(IconNames.Surprised)
            } else {
                basic.showIcon(IconNames.Silly)
            }
        })
        ```

    === "Python"

        ```python
        basic.show_string("HEJ!")
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        def on_button_pressed_b():
            basic.show_icon(IconNames.SAD)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        def on_button_pressed_ab():
            basic.show_icon(IconNames.HEART)
        input.on_button_pressed(Button.AB, on_button_pressed_ab)
        def on_gesture_shake():
            n = randint(0, 3)
            if n == 0:
                basic.show_icon(IconNames.HAPPY)
            elif n == 1:
                basic.show_icon(IconNames.SAD)
            elif n == 2:
                basic.show_icon(IconNames.SURPRISED)
            else:
                basic.show_icon(IconNames.SILLY)
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```


## 🌟 Extra challenges

??? example "🎨 Draw your own picture"

    Make **button A** light up your own LEDs with **`show leds`** — draw anything!

    === "Blocks"

        ```makecode
        auto:draw
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
        })
        ```

    === "Python"

        ```python
        def on_button_pressed_a():
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                """)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        ```

??? example "✊✋✌️ Rock, Paper, Scissors"

    Shake to throw rock, paper or scissors — then duel a friend, best of five!

    === "Blocks"

        ```makecode
        auto:rps
        ```

    === "JavaScript"

        ```javascript
        input.onGesture(Gesture.Shake, function () {
            let pick = randint(0, 2)
            if (pick == 0) {
                basic.showIcon(IconNames.Square)
            } else if (pick == 1) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    `)
            } else {
                basic.showIcon(IconNames.Scissors)
            }
        })
        ```

    === "Python"

        ```python
        def on_gesture_shake():
            pick = randint(0, 2)
            if pick == 0:
                basic.show_icon(IconNames.SQUARE)
            elif pick == 1:
                basic.show_leds("""
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    """)
            else:
                basic.show_icon(IconNames.SCISSORS)
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```


## ✅ I did it when…

- ☐ Button **A** shows 😀 and **B** shows 🙁 on the real board.
- ☐ A **shake** gives a surprise (or a random face).
- ☐ *(Legend!)* I finished all 6 steps — or built an extra challenge.


## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-2
```


---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** build on Week 1's `show icon` — add **buttons** (A/B/A+B), the **shake** gesture, and a first taste of **randomness**, as one program built up step by step.

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap Week 1 → 40 work through Steps ①–⑥ together, checking blocks each step → 15 download to the board
    - **Break (20)**
    - **Block 2 (30):** 20 extra challenges (draw, Rock-Paper-Scissors) at own pace → 5 showcase → 5 Kahoot

    **Notes:** each step's embed shows the program *so far*, so kids build one program rather than copying finished code. Step ⑤ is a gentle intro to **pick random** + **if/else**.
