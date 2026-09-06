# Week 2 — Button Faces 😀

> Make your micro:bit pull faces! Press a button and it smiles, frowns or gets a surprise.

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

A face machine: **button A = happy** 😀, **button B = sad** 🙁. Then we add more faces, a shake surprise, your name and even Rock-Paper-Scissors!

## ▶️ Build it

1. Open **[makecode.microbit.org](https://makecode.microbit.org)** → **New Project**.
2. From **Input**, grab **`on button A pressed`**. Inside it, add **`show icon`** → pick 😀 **Happy**.
3. Add **`on button B pressed`** with **`show icon`** → pick 🙁 **Sad**.
4. Press **A** and **B** in the simulator — then 📥 **Download** to your micro:bit!

??? example "👀 The program — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto
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


## 🪜 Make it yours

Keep going — each step adds a new trick. Tap **👀 Peek** to try it and see the code.

**① Press both = love** 💗 — `on button A+B pressed` shows a heart.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-1
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


**② Shake for a surprise** 😲 — `on shake` shows a surprised face.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-2
        ```

    === "JavaScript"

        ```javascript
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            basic.showIcon(IconNames.Sad)
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

        def on_gesture_shake():
            basic.show_icon(IconNames.SURPRISED)
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```


**③ Random face** 🎲 — shake and get a *different* face each time.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-3
        ```

    === "JavaScript"

        ```javascript
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


**④ Name badge** 🙋 — show your name when it starts up. *(Change MIA to your name!)*

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-4
        ```

    === "JavaScript"

        ```javascript
        basic.showString("HI MIA")
        input.onButtonPressed(Button.A, function () {
            basic.showIcon(IconNames.Happy)
        })
        ```

    === "Python"

        ```python
        basic.show_string("HI MIA")
        def on_button_pressed_a():
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        ```


**⑤ Draw your own picture** 🎨 — light up your own LEDs with `show leds`.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-5
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


**⑥ 🏆 Boss — Rock, Paper, Scissors** ✊✋✌️ — shake to throw, then duel a friend!

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-6
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


**Reached the top?** Invent your own face or button trick and teach a friend! ✨

## ✅ I did it when…

- ☐ Button **A** shows a happy face and **B** a sad face on the real board.
- ☐ I added a **shake** surprise.
- ☐ *(Legend!)* I built Rock-Paper-Scissors — or my own trick.

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-2
```

---

??? note "👩‍🏫 For helpers — session plan, materials & notes"

    **Goal:** build on Week 1's `show icon` — add **buttons** (A/B/A+B) and the **shake** gesture, plus a first taste of **randomness**.

    **Materials**

    - 1 micro:bit + USB cable per kid
    - Laptop/Chromebook with makecode.microbit.org open

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap Week 1 → 25 build A=happy / B=sad together → 15 download to board → 15 rungs ①–② (A+B heart, shake surprise)
    - **Break (20)**
    - **Block 2 (30):** 20 climb rungs ③–⑥ (random face, name badge, draw, RPS) → 5 showcase → 5 Kahoot

    **Notes:** everyone gets A/B faces working first; the ladder is self-paced. Rung ③ is a gentle intro to **pick random**; rung ⑥ (RPS) is a fun pair game.
