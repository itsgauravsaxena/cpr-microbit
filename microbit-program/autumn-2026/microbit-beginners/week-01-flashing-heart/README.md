# Week 1 — Flashing Heart (and make it yours)

> **Meet your micro:bit!** 💛 It's a tiny computer with **25 little lights**. Right now it's fast asleep… let's wake it up, teach it to show a **beating heart** — and then push it as far as you can!

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

!!! tip "▶️ See it come alive"
    Open the [Flashing Heart tutorial](https://makecode.microbit.org/projects/flashing-heart) and press **▶️ play** in the on-screen simulator — the heart beats on the screen before you even touch a real micro:bit. Then make **your** board do it! ✨

**Goal:** get comfortable with the MakeCode editor and the download-to-board workflow — then keep going. The beating heart is the *warm-up*; the **stretch ladder** below is where the real fun (and the whole 90 minutes) lives, so no one runs out of things to do.

**Official tutorial:** https://makecode.microbit.org/projects/flashing-heart

## Materials
- 1 micro:bit + USB cable per kid
- Laptop/Chromebook with makecode.microbit.org open

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min · Core + first rungs
- 10 min — what's a micro:bit, tour of the LED grid, buttons A/B
- 25 min — build the beating heart together (follow along), press ▶️ in the simulator
- 15 min — download the `.hex`, drag it onto the MICROBIT USB drive, watch it flash on the real board
- 10 min — **Make it yours:** climb rungs ① and ② of the stretch ladder (change the speed, add more icons)

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Climb the stretch ladder
- 20 min — everyone keeps climbing the **stretch ladder** below from wherever they are — pick your own level, no pressure to reach the top. Helpers roam.
- 5 min — **gallery walk:** show the person next to you the coolest rung you reached
- 5 min — 🎉 **Kahoot quiz** — whole group together

!!! note "For helpers — how the ladder works"
    Everyone finishes the same **core** (a beating heart on their board). After that, kids climb the ladder at their own pace: confident coders race to the boss level, while others take rungs ① and ② slowly — nobody is stuck waiting and nobody is bored. Rungs ④–⑥ quietly preview buttons, randomness and variables from the weeks ahead.

## Example code

The program we build together. Open the box to run it, read it as blocks / JavaScript / Python, and click **Open full-screen in MakeCode** to make your own version:

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

## 🚀 Stretch ladder — finish early? Keep climbing!

Start at the top and go as far as you can. Each rung tells you **what to try**, the **blocks to look for**, and a ✅ **buddy check** — show a friend when you get it working. Stuck? Open **👀 Peek** to run the finished rung right there and read it as blocks, JavaScript or Python.

**① Faster / slower heartbeat** — add a `pause (ms)` block between the two `show icon` blocks. Try `100` then `1000`. *Look in:* **Basic → pause.** ✅ Show a buddy your fastest *and* slowest heartbeat.

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

**② Make a mini-movie** — put 3–4 *different* icons inside `forever` so the LEDs play a little animation loop (heart → duck → ghost → yes → …). *Look in:* **Basic → show icon.** ✅ Give your animation a name.

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

**③ Say hello first** — in `on start`, use `show string` with your name once, *then* let the animation run forever. *Look in:* **Basic → show string / on start.** ✅ Your board greets you by name.

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

**④ Two moods, two buttons** — `on button A pressed` → happy face; `on button B pressed` → sad face. *Look in:* **Input → on button pressed.** ✅ A = 😀, B = 🙁.

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

**⑤ Shake for a surprise** *(peek at Week 3!)* — `on shake` → show a **random** icon each time. *Look in:* **Input → on shake** and **Math → pick random.** ✅ Every shake is different.

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

**⑥ 🏆 Boss level — mood pet** — build a tiny pet: on start it's **asleep** (`Asleep` icon); press **A** to *feed* it (heart + happy face); press **B** to *play* (a quick giggle animation). *Look in:* everything above + a **variable** to remember its mood. ✅ Your pet reacts to both buttons.

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

**Made it to the top?** Invent rung ⑦ yourself — a brand-new thing your micro:bit does — and teach it to a friend.

## ✅ Done when
- **Core (everyone):** the heart keeps beating (big ↔ small) on the real board, forever.
- **Reached for more:** you climbed at least to rung ③, and you can explain one block you used.
- **Legend:** you hit the boss level (⑥) or invented your own rung.

## Notes
_(space for session notes, what worked, which rungs kids reached, timing adjustments)_

## Reference
- MakeCode Tutorials mode (Tutorials tab on the MakeCode home page) gives step-by-step pictures + simulator animation — use it instead of a slide deck

## 🎉 Kahoot quiz

Finish the session with this week's quiz — **both groups play together**. Click below to open it, press **Host**, and share the game PIN with the kids. (Prefer to read them out, or need the import sheet? See the weekly quiz.)

```kahoot
week-1
```
