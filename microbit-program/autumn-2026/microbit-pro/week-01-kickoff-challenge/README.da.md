# Uge 1 — Flashing Heart 💛

> Væk din micro:bit og lær den at vise et **bankende hjerte** — og gør den så til din egen!

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="En micro:bit der blinker et hjerte" xmlns="http://www.w3.org/2000/svg">
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

## 🎯 Hvad vi laver

Et **bankende hjerte** på micro:bit'ens lys — stort hjerte, lille hjerte, igen og igen. 💓

## ▶️ Byg det

1. Åbn **[makecode.microbit.org](https://makecode.microbit.org)** → **New Project**.
2. Fra **Basic** træk **`show icon`** ind i **`forever`** og vælg ❤️ **hjertet**.
3. Tilføj endnu et **`show icon`** nedenunder og vælg det 💛 **lille hjerte**.
4. Tryk på **▶️** for at se det banke på skærmen.
5. 📥 **Læg det på din micro:bit:** klik **Download**, og træk filen over på **MICROBIT**-drevet.

Her er det færdige program — tryk på play, eller **Open full-screen in MakeCode** for at gøre det til dit eget:

??? example "👀 Programmet — kør det, eller læs koden"

    === "Blokke & simulator"

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

## 🪜 Gør det til din egen

Færdig tidligt? Klatr så højt du kan — hvert trin er et nyt trick. Tryk på **👀 Kig** for at prøve det og se koden.

**① Hurtigere eller langsommere** 🕒 — sæt en `pause` mellem de to hjerter. Prøv `100` og så `1000`.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**② Lav en mini-film** 🎬 — tilføj 3–4 forskellige ikoner i `forever`.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**③ Sig dit navn** 🙋 — brug `show string` i `on start`, og lad det så banke.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**④ To knapper, to ansigter** 😀🙁 — knap **A** → glad, knap **B** → sur.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**⑤ Ryst for en overraskelse** 🎲 — `on shake` viser et tilfældigt ikon. *(Et smugkig på uge 3!)*

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**⑥ 🏆 Boss — kæledyr med humør** — starter sovende 😴, **A** fodrer det 💗, **B** leger 😆.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**Nået til toppen?** Find på dit eget trick og lær det til en ven! ✨

## ✅ Jeg er færdig når…

- ☐ Mit hjerte banker på den **rigtige** micro:bit.
- ☐ Jeg nåede mindst til trin ③.
- ☐ *(Legende!)* Jeg byggede kæledyret — eller mit eget trick.

## 🎉 Kahoot-tid!

Lad os slutte af med en quiz — alle sammen!

```kahoot
week-1
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan, materialer & noter"

    **Mål:** bliv fortrolig med MakeCode-editoren og download-til-board. Hjertet er opvarmningen; stigen fylder sessionen, så ingen løber tør.

    **Materialer**

    - 1 micro:bit + USB-kabel pr. barn
    - Bærbar/Chromebook med makecode.microbit.org åben

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 10 intro → 25 byg hjertet sammen → 15 download til board → 10 trin ①–② (fart, flere ikoner)
    - **Pause (20)**
    - **Blok 2 (30):** 20 klatr op ad stigen → 5 gallerivandring → 5 Kahoot

    **Sådan virker stigen:** alle laver kerne-hjertet færdigt og klatrer så i deres eget tempo — hurtige kodere kapløber til bossen, andre tager ①–② langsomt. Trin ④–⑥ giver et smugkig på knapper, tilfældighed og variabler fra de kommende uger.

    **Reference:** MakeCodes Tutorials-tilstand og [Flashing Heart-tutorialen](https://makecode.microbit.org/projects/flashing-heart). _Noter: hvad virkede, hvilke trin børnene nåede, tidsforbrug._
