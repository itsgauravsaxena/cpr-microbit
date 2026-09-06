# Week 1 — Flashing Heart 💛

> Wake up your micro:bit and teach it to show a **beating heart** — then make it your own!

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="A micro:bit blinking a heart" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038">
<rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/>
<rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/>
<rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/>
<rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/>
<rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/>
</g>
<g fill="#ff4d4d">
<animate attributeName="opacity" values="1;0.25;1" dur="1.1s" repeatCount="indefinite"/>
<rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/>
<rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/>
<rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/>
<rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/>
<rect x="85" y="153" width="26" height="26" rx="6"/>
</g>
</svg>
</div>

## 🎯 What we're making

A **beating heart** on the micro:bit's lights — big heart, small heart, over and over. 💓

## ▶️ Build it

1. Open **[makecode.microbit.org](https://makecode.microbit.org)** → **New Project**.
2. From **Basic**, drag **`show icon`** into **`forever`** and pick the ❤️ **heart**.
3. Add another **`show icon`** underneath and pick the 💛 **small heart**.
4. Press **▶️** to watch it beat on screen.
5. 📥 **Put it on your micro:bit:** click **Download**, then drag the file onto the **MICROBIT** drive.

Here's the finished program — press play, or **Open full-screen in MakeCode** to make it yours:

??? example "👀 The program — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            basic.showIcon(IconNames.Heart)
            basic.showIcon(IconNames.SmallHeart)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            basic.show_icon(IconNames.HEART)
            basic.show_icon(IconNames.SMALL_HEART)
        basic.forever(on_forever)
        ```

## 🪜 Make it yours

Finished early? Climb as high as you can — each step is a new trick. Tap **👀 Peek** to try it and see the code.

**① Faster or slower** 🕒 — put a `pause` between the two hearts. Try `100`, then `1000`.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-1
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            basic.showIcon(IconNames.Heart)
            basic.pause(1000)
            basic.showIcon(IconNames.SmallHeart)
            basic.pause(100)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            basic.show_icon(IconNames.HEART)
            basic.pause(1000)
            basic.show_icon(IconNames.SMALL_HEART)
            basic.pause(100)
        basic.forever(on_forever)
        ```

**② Make a mini-movie** 🎬 — add 3–4 different icons inside `forever`.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-2
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            basic.showIcon(IconNames.Heart)
            basic.showIcon(IconNames.Duck)
            basic.showIcon(IconNames.Ghost)
            basic.showIcon(IconNames.Yes)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            basic.show_icon(IconNames.HEART)
            basic.show_icon(IconNames.DUCK)
            basic.show_icon(IconNames.GHOST)
            basic.show_icon(IconNames.YES)
        basic.forever(on_forever)
        ```

**③ Say your name** 🙋 — use `show string` in `on start`, then let it beat.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-3
        ```

    === "JavaScript"

        ```javascript
        basic.showString("Mia")
        basic.forever(function () {
            basic.showIcon(IconNames.Heart)
            basic.showIcon(IconNames.SmallHeart)
        })
        ```

    === "Python"

        ```python
        basic.show_string("Mia")
        def on_forever():
            basic.show_icon(IconNames.HEART)
            basic.show_icon(IconNames.SMALL_HEART)
        basic.forever(on_forever)
        ```

**④ Two buttons, two faces** 😀🙁 — button **A** → happy, button **B** → sad.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-4
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

**⑤ Shake for a surprise** 🎲 — `on shake` shows a random icon. *(A peek at Week 3!)*

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-5
        ```

    === "JavaScript"

        ```javascript
        input.onGesture(Gesture.Shake, function () {
            let n = randint(0, 3)
            if (n == 0) {
                basic.showIcon(IconNames.Heart)
            } else if (n == 1) {
                basic.showIcon(IconNames.Ghost)
            } else if (n == 2) {
                basic.showIcon(IconNames.Duck)
            } else {
                basic.showIcon(IconNames.Yes)
            }
        })
        ```

    === "Python"

        ```python
        def on_gesture_shake():
            n = randint(0, 3)
            if n == 0:
                basic.show_icon(IconNames.HEART)
            elif n == 1:
                basic.show_icon(IconNames.GHOST)
            elif n == 2:
                basic.show_icon(IconNames.DUCK)
            else:
                basic.show_icon(IconNames.YES)
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```

**⑥ 🏆 Boss — mood pet** — starts asleep 😴, **A** feeds it 💗, **B** plays 😆.

??? example "👀 Peek — run it, or read the code"

    === "Blocks & simulator"

        ```makecode
        auto:rung-6
        ```

    === "JavaScript"

        ```javascript
        let mood = ""
        basic.showIcon(IconNames.Asleep)
        mood = "sleep"
        input.onButtonPressed(Button.A, function () {
            mood = "fed"
            basic.showIcon(IconNames.Heart)
            basic.showIcon(IconNames.Happy)
        })
        input.onButtonPressed(Button.B, function () {
            mood = "play"
            basic.showIcon(IconNames.Happy)
            basic.showIcon(IconNames.SmallHeart)
            basic.showIcon(IconNames.Happy)
        })
        ```

    === "Python"

        ```python
        mood = ""
        basic.show_icon(IconNames.ASLEEP)
        mood = "sleep"

        def on_button_pressed_a():
            global mood
            mood = "fed"
            basic.show_icon(IconNames.HEART)
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def on_button_pressed_b():
            global mood
            mood = "play"
            basic.show_icon(IconNames.HAPPY)
            basic.show_icon(IconNames.SMALL_HEART)
            basic.show_icon(IconNames.HAPPY)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        ```

**Reached the top?** Invent your own trick and teach a friend! ✨

## ✅ I did it when…

- ☐ My heart beats on the **real** micro:bit.
- ☐ I climbed at least to step ③.
- ☐ *(Legend!)* I built the mood pet — or my own trick.

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-1
```

---

??? note "👩‍🏫 For helpers — session plan, materials & notes"

    **Goal:** get comfortable with the MakeCode editor and the download-to-board flow. The heart is the warm-up; the ladder fills the session so no one runs out.

    **Materials**

    - 1 micro:bit + USB cable per kid
    - Laptop/Chromebook with makecode.microbit.org open

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 10 intro → 25 build the heart together → 15 download to the board → 10 rungs ①–② (speed, more icons)
    - **Break (20)**
    - **Block 2 (30):** 20 climb the ladder → 5 gallery walk → 5 Kahoot

    **How the ladder works:** everyone finishes the core heart, then climbs at their own pace — fast coders race to the boss, others take ①–② slowly. Rungs ④–⑥ preview buttons, randomness and variables from the weeks ahead.

    **Reference:** MakeCode Tutorials mode, and the [Flashing Heart tutorial](https://makecode.microbit.org/projects/flashing-heart). _Notes: what worked, which rungs kids reached, timing._
