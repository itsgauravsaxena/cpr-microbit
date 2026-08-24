# Uge 1 — Flashing Heart (gør den til din egen)

> **Mød din micro:bit!** 💛 Den er en lille computer med **25 små lys**. Lige nu sover den dybt … lad os vække den, lære den at vise et **bankende hjerte** — og så presse den så langt du kan!

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

!!! tip "▶️ Se den blive levende"
    Åbn [Flashing Heart-tutorialen](https://makecode.microbit.org/projects/flashing-heart) og tryk på **▶️ afspil** i simulatoren på skærmen — hjertet banker på skærmen, før du overhovedet rører en rigtig micro:bit. Lav så **dit** board om til at gøre det samme! ✨

**Mål:** bliv fortrolig med MakeCode-editoren og arbejdsgangen med at downloade til boardet — og fortsæt så. Det bankende hjerte er *opvarmningen*; **udfordringsstigen** nedenfor er der, hvor det sjove (og hele de 90 minutter) foregår, så ingen løber tør for ting at lave.

**Officiel tutorial:** https://makecode.microbit.org/projects/flashing-heart

## Materialer
- 1 micro:bit + USB-kabel pr. barn
- Bærbar/Chromebook med makecode.microbit.org åben

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min · Kerne + første trin
- 10 min — hvad er en micro:bit, rundvisning i LED-gitteret, knapperne A/B
- 25 min — byg det bankende hjerte sammen (følg med), tryk på ▶️ i simulatoren
- 15 min — download `.hex`-filen, træk den over på MICROBIT-USB-drevet, se den blinke på det rigtige board
- 10 min — **Gør den til din egen:** klatr op ad trin ① og ② på udfordringsstigen (ændr farten, tilføj flere ikoner)

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Klatr op ad udfordringsstigen
- 20 min — alle klatrer videre på **udfordringsstigen** nedenfor derfra hvor de er — vælg dit eget niveau, ingen skal nå toppen. Hjælpere går rundt.
- 5 min — **gallerivandring:** vis din sidemand det fedeste trin, du nåede
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen

!!! note "Til hjælpere — sådan virker stigen"
    Alle laver den samme **kerne** færdig (et bankende hjerte på deres board). Derefter klatrer børnene op ad stigen i deres eget tempo: de sikre kodere kapløber mod boss-niveauet, mens andre tager trin ① og ② langsomt — ingen sidder og venter, og ingen keder sig. Trin ④–⑥ giver et lille smugkig på knapper, tilfældighed og variabler fra de kommende uger.

## Eksempelkode

Programmet vi bygger sammen. Åbn boksen for at køre det, se det som blokke / JavaScript / Python, og klik på **Open full-screen in MakeCode** for at lave din egen version:

??? example "👀 Programmet — kør, eller læs koden"

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

## 🚀 Udfordringsstige — færdig tidligt? Bliv ved med at klatre!

Start i toppen og kom så langt du kan. Hvert trin fortæller dig **hvad du skal prøve**, **hvilke blokke du skal finde**, og et ✅ **makker-tjek** — vis en ven, når du får det til at virke. Sidder du fast? Åbn **👀 Se koden** for at køre det færdige trin med det samme og se det som blokke, JavaScript eller Python.

**① Hurtigere / langsommere hjerteslag** — læg en `pause (ms)`-blok mellem de to `show icon`-blokke. Prøv `100` og så `1000`. *Find den under:* **Basic → pause.** ✅ Vis en makker dit hurtigste *og* langsomste hjerteslag.

??? example "👀 Se koden — kør, eller læs koden"

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

**② Lav en mini-film** — sæt 3–4 *forskellige* ikoner inde i `forever`, så LED'erne spiller en lille animationsløkke (hjerte → and → spøgelse → ja → …). *Find den under:* **Basic → show icon.** ✅ Giv din animation et navn.

??? example "👀 Se koden — kør, eller læs koden"

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

**③ Sig hej først** — brug `show string` med dit navn én gang i `on start`, og lad *derefter* animationen køre for evigt. *Find den under:* **Basic → show string / on start.** ✅ Dit board hilser på dig med navn.

??? example "👀 Se koden — kør, eller læs koden"

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

**④ To humører, to knapper** — `on button A pressed` → glad ansigt; `on button B pressed` → surt ansigt. *Find den under:* **Input → on button pressed.** ✅ A = 😀, B = 🙁.

??? example "👀 Se koden — kør, eller læs koden"

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

**⑤ Ryst for en overraskelse** *(smugkig på uge 3!)* — `on shake` → vis et **tilfældigt** ikon hver gang. *Find den under:* **Input → on shake** og **Math → pick random.** ✅ Hvert ryst er forskelligt.

??? example "👀 Se koden — kør, eller læs koden"

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

**⑥ 🏆 Boss-niveau — kæledyr med humør** — byg et lille kæledyr: ved start **sover** det (`Asleep`-ikon); tryk **A** for at *fodre* det (hjerte + glad ansigt); tryk **B** for at *lege* (en hurtig fnise-animation). *Find den under:* alt ovenfor + en **variabel** til at huske dets humør. ✅ Dit kæledyr reagerer på begge knapper.

??? example "👀 Se koden — kør, eller læs koden"

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

**Nået til toppen?** Find selv på trin ⑦ — noget helt nyt din micro:bit kan gøre — og lær det til en ven.

## ✅ Færdig når
- **Kerne (alle):** hjertet bliver ved med at banke (stort ↔ lille) på det rigtige board, for evigt.
- **Strakte sig:** du nåede mindst til trin ③ og kan forklare én blok, du brugte.
- **Legende:** du ramte boss-niveauet (⑥) eller fandt på dit eget trin.

## Noter
_(plads til sessionsnoter, hvad virkede, hvilke trin børnene nåede, justeringer af tidsforbrug)_

## Reference
- MakeCodes Tutorials-tilstand (fanen Tutorials på MakeCodes startside) giver trinvise billeder + simulatoranimation — brug den i stedet for et slidedeck

## 🎉 Kahoot-quiz

Afslut sessionen med denne uges quiz — **begge grupper spiller sammen**. Klik nedenfor for at åbne den, tryk på **Host**, og del spil-PIN'en med børnene. (Vil du hellere læse dem op, eller mangler du import-arket? Se den ugentlige quiz.)

```kahoot
week-1
```
