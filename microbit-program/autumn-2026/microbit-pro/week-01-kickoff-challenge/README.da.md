# Uge 1 — Velkommen tilbage til Pro! 🚀

> 🏴‍☠️ Velkommen tilbage! Dette semester handler om **større idéer** — sensorer, data, bevægelse, lyd, radio og jeres egne opfindelser. I dag: en hurtig opvarmnings-dyst, og så får vi micro:bit'en til at gøre noget, der føles som **ren magi** — med kun en håndfuld blokke.

**Mål:** ryst sommerrusten af med et sjovt spil, lås micro:bit'ens skjulte superkraft op — dens **sensorer** — med en imponerende demo på få blokke, og bliv enige om, hvordan vi arbejder: **del din kode hver uge**.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="gættespillet der tæller" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Materialer
- 1 micro:bit **V2** + USB-kabel pr. barn (i dag bruger vi V2'ens **mikrofon** og **højtaler**)
- Bærbar/Chromebook med makecode.microbit.org åben
- En makker til radio-trinnet (trin ⑤)

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min · Opvarmning + magien
- 5 min — velkommen tilbage, kig på 10-ugers Pro-kortet, vores ene regel: **del din kode hver uge**
- 15 min — **opvarmning:** byg og spil Sten-Saks-Papir-dyster
- 20 min — **magien:** byg lyd-søjlediagrammet sammen, flash det til et rigtigt board, få rummet til at blive højt/stille
- 20 min — begynd at klatre op ad **sensor-stigen** (trin ①–②)

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Klatr op ad sensor-stigen
- 20 min — klatr videre i dit eget tempo (hjælpere går rundt; find en makker til radio-trinnet)
- 5 min — **fremvisning:** vis dit yndlings-sensortrick til gruppen
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen ([ugens spørgsmål](../../quiz/README.md#uge-1))

## 🔥 Opvarmning — Sten, Saks, Papir-dyst

Ryst din micro:bit for at kaste **sten, saks eller papir**, og dyst så med din sidemand — bedst af fem! En to-minutters byggeøvelse, der ryster rusten af.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:warmup
        ```

    === "JavaScript"

        ```javascript
        input.onGesture(Gesture.Shake, function () {
            let choice = randint(0, 2)
            if (choice == 0) {
                basic.showIcon(IconNames.Square)
            } else if (choice == 1) {
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
            choice = randint(0, 2)
            if choice == 0:
                basic.show_icon(IconNames.SQUARE)
            elif choice == 1:
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

## 🤯 Magien — få micro:bit'en til at *se din stemme*

Her er "wow"-øjeblikket. micro:bit **V2** har en lille **mikrofon**. Med kun et par blokke omdanner den, hvor højt der er i rummet, til et levende søjlediagram på LED'erne — **tal, klap eller råb** og se det danse. Det er en ægte sensor, der aflæses ~hundrede gange i sekundet.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            led.plotBarGraph(input.soundLevel(), 255)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            led.plot_bar_graph(input.sound_level(), 255)
        basic.forever(on_forever)
        ```

## 🚀 Udfordringsstige — hvor langt kan du presse sensorerne?

Hvert trin er en **ny superkraft på få blokke**. Start i toppen og kom så langt du kan. Åbn **👀 Kør det** for at prøve det færdige trin og se det som blokke, JavaScript eller Python.

**① Klap-detektor** — få boardet til at reagere på en **høj** lyd (et klap eller råb) med et overrasket ansigt. *Find den under:* **Input → ved høj lyd.** ✅ Klap → 😲.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:rung-1
        ```

    === "JavaScript"

        ```javascript
        input.onSound(DetectedSound.Loud, function () {
            basic.showIcon(IconNames.Surprised)
            basic.pause(500)
            basic.clearScreen()
        })
        ```

    === "Python"

        ```python
        def on_loud():
            basic.show_icon(IconNames.SURPRISED)
            basic.pause(500)
            basic.clear_screen()
        input.on_sound(DetectedSound.LOUD, on_loud)
        ```

**② Lys-theremin** 🎵 — vift hånden over boardet; **tonehøjden ændrer sig med lyset**. *Find den under:* **Input → lysniveau, Music → ring tone, Math → map.** ✅ Din hånd spiller musik.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:rung-2
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            let pitch = Math.map(input.lightLevel(), 0, 255, 200, 1200)
            music.ringTone(pitch)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            pitch = Math.map(input.light_level(), 0, 255, 200, 1200)
            music.ring_tone(pitch)
        basic.forever(on_forever)
        ```

**③ Vater med hældning** — en enkelt prik triller mod den lave side, når du vipper boardet, som et vaterpas. *Find den under:* **Input → acceleration (x), LED → plot x y, Math → map.** ✅ Prikken følger tyngdekraften.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:rung-3
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            let x = Math.map(input.acceleration(Dimension.X), -1000, 1000, 0, 4)
            basic.clearScreen()
            led.plot(Math.round(x), 2)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            x = Math.map(input.acceleration(Dimension.X), -1000, 1000, 0, 4)
            basic.clear_screen()
            led.plot(Math.round(x), 2)
        basic.forever(on_forever)
        ```

**④ Ryste-spådom (Magic 8-ball)** — ryst for et tilfældigt svar fra en liste, du selv skriver. *Find den under:* **Input → ved rystelse, Arrays, Math → vælg tilfældig.** ✅ Stil et spørgsmål, ryst, få et svar.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:rung-4
        ```

    === "JavaScript"

        ```javascript
        input.onGesture(Gesture.Shake, function () {
            let answers = ["YES", "NO", "MAYBE", "SOON", "NO WAY"]
            basic.showString(answers[randint(0, answers.length - 1)])
        })
        ```

    === "Python"

        ```python
        answers = ["YES", "NO", "MAYBE", "SOON", "NO WAY"]
        def on_gesture_shake():
            basic.show_string(answers[randint(0, len(answers) - 1)])
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        ```

**⑤ Radio-ping** 📡 *(find en makker — smugkig på uge 5–6)* — tryk **A** for at pinge; din makkers board blinker ✓. *Find den under:* **Radio → sæt gruppe / send streng / ved modtaget streng.** ✅ To boards taler trådløst.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:rung-5
        ```

    === "JavaScript"

        ```javascript
        radio.setGroup(1)
        input.onButtonPressed(Button.A, function () {
            radio.sendString("ping")
        })
        radio.onReceivedString(function (receivedString) {
            basic.showIcon(IconNames.Yes)
            basic.pause(300)
            basic.clearScreen()
        })
        ```

    === "Python"

        ```python
        def on_received_string(receivedString):
            basic.show_icon(IconNames.YES)
            basic.pause(300)
            basic.clear_screen()
        radio.on_received_string(on_received_string)

        def on_button_pressed_a():
            radio.send_string("ping")
        input.on_button_pressed(Button.A, on_button_pressed_a)

        radio.set_group(1)
        ```

**⑥ 🏆 Boss — instrument med to sensorer** — spil micro:bit'en som et instrument: **lys sætter tonehøjden, hældning sætter lydstyrken.** *Find den under:* alt ovenfor + **Music → sæt lydstyrke.** ✅ To sensorer, ét instrument.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

        ```makecode
        auto:rung-6
        ```

    === "JavaScript"

        ```javascript
        basic.forever(function () {
            let pitch = Math.map(input.lightLevel(), 0, 255, 200, 1200)
            let vol = Math.map(Math.abs(input.acceleration(Dimension.X)), 0, 1000, 0, 255)
            music.setVolume(vol)
            music.ringTone(pitch)
        })
        ```

    === "Python"

        ```python
        def on_forever():
            pitch = Math.map(input.light_level(), 0, 255, 200, 1200)
            vol = Math.map(Math.abs(input.acceleration(Dimension.X)), 0, 1000, 0, 255)
            music.set_volume(vol)
            music.ring_tone(pitch)
        basic.forever(on_forever)
        ```

**Nået til toppen?** Find selv på trin ⑦ — vælg en sensor vi ikke har brugt (temperatur, kompas, touch-logo) og få den til at gøre noget — og lær det til en ven.

!!! note "Til hjælpere — sådan virker stigen"
    Alle får først **lyd-søjlediagrammet** til at virke (den fælles sejr). Derefter klatrer børnene i deres eget tempo: de sikre kodere kapløber til theremin'en og boss-instrumentet, mens andre nyder klap-detektoren og ryste-spådommen. Trinnene giver et smugkig på semesteret — sensorer (uge 2), lyd (uge 4), radio (uge 5–6).

## ✅ Færdig når
- **Kerne (alle):** lyd-søjlediagrammet reagerer på din stemme på det rigtige board.
- **Strakte sig:** du nåede mindst til trin ③ og kan sige, hvilken sensor det bruger.
- **Legende:** du ramte boss-instrumentet (⑥) eller fandt på dit eget trin.

## 🎉 Kahoot-quiz

Afslut sessionen med denne uges quiz — **begge grupper spiller sammen**. Klik nedenfor for at åbne den, tryk på **Host**, og del spil-PIN'en med børnene. (Vil du hellere læse dem op, eller mangler du import-arket? Se [den ugentlige quiz](../../quiz/README.md#uge-1).)

```kahoot
week-1
```

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

## Noter
_(plads til sessionsnoter, hvilke trin børnene nåede, justeringer af tidsforbrug)_
