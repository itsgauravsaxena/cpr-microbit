# Uge 2 — Knap-ansigter 😀

> Få din micro:bit til at lave grimasser! Tryk på en knap, og den smiler, surmuler eller bliver overrasket.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="220" height="220" viewBox="0 0 216 216" role="img" aria-label="et ansigt der skifter glad, ked af det, overrasket" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="0" y="0" width="216" height="216" rx="24" fill="#0f1419" stroke="#c8a24a" stroke-width="3"/>
<rect x="17" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#2b3038"/>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
</svg>
</div>

## 🎯 Hvad vi laver

En ansigtsmaskine: **knap A = glad** 😀, **knap B = ked af det** 🙁. Så tilføjer vi flere ansigter, en ryste-overraskelse, dit navn og endda Sten-Saks-Papir!

## ▶️ Byg det

1. Åbn **[makecode.microbit.org](https://makecode.microbit.org)** → **New Project**.
2. Fra **Input**, tag **`on button A pressed`**. Indeni: tilføj **`show icon`** → vælg 😀 **Happy**.
3. Tilføj **`on button B pressed`** med **`show icon`** → vælg 🙁 **Sad**.
4. Tryk på **A** og **B** i simulatoren — og 📥 **Download** til din micro:bit!

??? example "👀 Programmet — kør det, eller læs koden"

    === "Blokke & simulator"

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


## 🪜 Gør det til din egen

Byg videre — hvert trin er et nyt trick. Tryk på **👀 Kig** for at prøve det og se koden.

**① Tryk begge = kærlighed** 💗 — `on button A+B pressed` viser et hjerte.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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


**② Ryst for en overraskelse** 😲 — `on shake` viser et overrasket ansigt.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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


**③ Tilfældigt ansigt** 🎲 — ryst og få et *forskelligt* ansigt hver gang.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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


**④ Navneskilt** 🙋 — vis dit navn, når den starter op. *(Skift MIA ud med dit navn!)*

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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


**⑤ Tegn dit eget billede** 🎨 — tænd dine egne LED'er med `show leds`.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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


**⑥ 🏆 Boss — Sten, Saks, Papir** ✊✋✌️ — ryst for at kaste, og dyst en ven!

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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


**Nået til toppen?** Find på dit eget ansigt eller knap-trick og lær det til en ven! ✨

## ✅ Jeg er færdig når…

- ☐ Knap **A** viser et glad ansigt og **B** et ked-af-det-ansigt på det rigtige board.
- ☐ Jeg tilføjede en **ryste**-overraskelse.
- ☐ *(Legende!)* Jeg byggede Sten-Saks-Papir — eller mit eget trick.

## 🎉 Kahoot-tid!

Lad os slutte af med en quiz — alle sammen!

```kahoot
week-2
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan, materialer & noter"

    **Mål:** byg videre på uge 1's `show icon` — tilføj **knapper** (A/B/A+B) og **ryste**-gesten, plus et første strejf af **tilfældighed**.

    **Materialer**

    - 1 micro:bit + USB-kabel pr. barn
    - Bærbar/Chromebook med makecode.microbit.org åben

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 repetition af uge 1 → 25 byg A=glad / B=ked af det sammen → 15 download til board → 15 trin ①–② (A+B hjerte, ryste-overraskelse)
    - **Pause (20)**
    - **Blok 2 (30):** 20 klatr op ad trin ③–⑥ (tilfældigt ansigt, navneskilt, tegn, SSP) → 5 fremvisning → 5 Kahoot

    **Noter:** alle får A/B-ansigter til at virke først; stigen er selvkørende. Trin ③ er et blidt kig på **pick random**; trin ⑥ (SSP) er et sjovt par-spil.
