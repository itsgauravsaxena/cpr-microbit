# Uge 2 — Knap-ansigter 😀

> Byg en ansigtsmaskine, ét trin ad gangen: knapper laver ansigter, et ryst giver en overraskelse, og den hilser på dig, når den vågner.

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

Her er det færdige program — du bygger op til det, ét lille trin ad gangen. Tryk på **▶️ Open & run** for at lege med det:

```makecode
auto
```

## 🧱 Byg det — ét trin ad gangen

Åbn hvert trin, tilføj **kun de nye blokke**, og tjek så dine blokke mod billedet. Dit program vokser for hvert trin! 🌱

??? example "① Glad ansigt på knap A"

    Tilføj **`når der trykkes på knappen A`** → **`vis ikon`** og vælg 😀 **Happy**. Tryk på A!

    === "Blokke"

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

??? example "② Ked af det på knap B"

    Tilføj endnu en **`når der trykkes på knappen B`** → **`vis ikon`** → 🙁 **Sad**.

    === "Blokke"

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

??? example "③ Hjerte når du trykker A+B"

    Tilføj **`når der trykkes på knappen A+B`** → **`vis ikon`** → 💗 **Heart** (tryk begge samtidig).

    === "Blokke"

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

??? example "④ Overraskelse når du ryster"

    Tilføj **`på ryst`** → **`vis ikon`** → 😲 **Surprised**. Giv den et ryst!

    === "Blokke"

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

??? example "⑤ Tilfældigt ansigt ved ryst"

    Lav rystelsen om, så den vælger et **tilfældigt** ansigt — brug **vælg tilfældig** og **hvis / ellers**.

    === "Blokke"

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

??? example "⑥ Sig hej når den starter"

    Øverst tilføj **`når programmet starter`** → **`vis streng`** med en hilsen (fx HEJ!).

    === "Blokke"

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


## 🌟 Ekstra udfordringer

??? example "🎨 Tegn dit eget billede"

    Få **knap A** til at tænde dine egne LED'er med **`vis LED'er`** — tegn hvad som helst!

    === "Blokke"

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

??? example "✊✋✌️ Sten, Saks, Papir"

    Ryst for at kaste sten, saks eller papir — dyst så en ven, bedst af fem!

    === "Blokke"

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


## ✅ Jeg er færdig når…

- ☐ Knap **A** viser 😀 og **B** viser 🙁 på det rigtige board.
- ☐ Et **ryst** giver en overraskelse (eller et tilfældigt ansigt).
- ☐ *(Legende!)* Jeg lavede alle 6 trin — eller byggede en ekstra udfordring.


## 🎉 Kahoot-tid!

Lad os slutte af med en quiz — alle sammen!

```kahoot
week-2
```


---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** byg videre på uge 1's `vis ikon` — tilføj **knapper** (A/B/A+B), **ryste**-gesten og et første strejf af **tilfældighed**, som ét program bygget op trin for trin.

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 repetition af uge 1 → 40 arbejd gennem trin ①–⑥ sammen, tjek blokke hvert trin → 15 download til board
    - **Pause (20)**
    - **Blok 2 (30):** 20 ekstra udfordringer (tegn, Sten-Saks-Papir) i eget tempo → 5 fremvisning → 5 Kahoot

    **Noter:** hvert trins embed viser programmet *indtil videre*, så børnene bygger ét program i stedet for at kopiere færdig kode. Trin ⑤ er et blidt kig på **vælg tilfældig** + **hvis/ellers**.
