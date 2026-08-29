# Uge 1 — Flipper-scoreboard 🎯 (del 1)

> Dette semester bygger Pro-holdet **hjernen i en flippermaskine** — lidt hver uge. Første gang: en hurtig repetition, og så den allerførste del — en **score, der stiger, når du rammer et mål**.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="gættespillet der tæller" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## 🎯 Hvad vi laver i dag

**Begyndelsen** på vores flipper-scoreboard: rør et mål, og din **score** stiger — plus en **nulstil**- og en **nyt spil**-knap. Det er målet for i dag. Færdig tidligt? Der er en valgfri **level-up**-stige, der gør det til en rigtig lille maskine.

*(Den 3D-printede flipperkasse er den anden gruppes opgave — vi bygger koden.)*

## 🎮 Flipperens dele

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg viewBox="0 0 360 500" width="100%" style="max-width:340px;height:auto;display:block;margin:0 auto;" role="img" aria-label="Parts of a pinball machine" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="90" y="45" width="180" height="415" rx="16" fill="#20486e" stroke="#c8a24a" stroke-width="3"/>
<path d="M96 110 Q180 55 264 110" fill="none" stroke="#3d6a95" stroke-width="4"/>
<rect x="120" y="28" width="120" height="28" rx="5" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<text x="180" y="47" font-size="14" fill="#ffd23f" text-anchor="middle" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">SCORE 120</text>
<line x1="238" y1="110" x2="238" y2="440" stroke="#3d6a95" stroke-width="3"/>
<circle cx="250" cy="95" r="7" fill="#d7dbe1" stroke="#9aa0aa"/>
<rect x="243" y="426" width="14" height="18" rx="3" fill="#c0c4cc" stroke="#8a8f98"/>
<path d="M250 444 l-7 5 l14 5 l-14 5" fill="none" stroke="#8a8f98" stroke-width="2"/>
<circle cx="135" cy="150" r="20" fill="#e63946"/><circle cx="135" cy="150" r="8" fill="#fff"/>
<circle cx="198" cy="124" r="20" fill="#e63946"/><circle cx="198" cy="124" r="8" fill="#fff"/>
<circle cx="160" cy="205" r="18" fill="#e63946"/><circle cx="160" cy="205" r="7" fill="#fff"/>
<rect x="114" y="262" width="18" height="10" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="142" y="262" width="18" height="10" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<rect x="170" y="262" width="18" height="10" rx="2" fill="#ffd23f" stroke="#c8a24a"/>
<circle cx="150" cy="320" r="9" fill="#d7dbe1" stroke="#9aa0aa"/><circle cx="147" cy="317" r="2.5" fill="#fff"/>
<rect x="132" y="406" width="50" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(-22 137 414)"/>
<rect x="140" y="406" width="50" height="16" rx="8" fill="#e6eaf0" stroke="#9aa0aa" transform="rotate(22 223 414)"/>
<rect x="160" y="446" width="40" height="14" rx="3" fill="#0a1a2a"/>
<path d="M180 428 l-7 12 l14 0 z" fill="#0a1a2a" opacity="0.6"/>
<line x1="86" y1="150" x2="115" y2="150" stroke="#c8a24a" stroke-width="1.5"/>
<text x="84" y="150" font-size="13" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🔴 Bumpere</text>
<line x1="86" y1="270" x2="112" y2="268" stroke="#c8a24a" stroke-width="1.5"/>
<text x="84" y="270" font-size="13" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🎯 Mål</text>
<line x1="86" y1="420" x2="120" y2="414" stroke="#c8a24a" stroke-width="1.5"/>
<text x="84" y="420" font-size="13" fill="var(--md-default-fg-color)" text-anchor="end" font-family="system-ui,Segoe UI,sans-serif">🕹️ Flippere</text>
<line x1="262" y1="436" x2="276" y2="436" stroke="#c8a24a" stroke-width="1.5"/>
<text x="278" y="436" font-size="13" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🚀 Plunger</text>
<line x1="240" y1="45" x2="274" y2="45" stroke="#c8a24a" stroke-width="1.5"/>
<text x="276" y="45" font-size="13" fill="var(--md-default-fg-color)" text-anchor="start" font-family="system-ui,Segoe UI,sans-serif">🔢 Score</text>
<text x="180" y="490" font-size="13" fill="var(--md-default-fg-color)" text-anchor="middle" font-family="system-ui,Segoe UI,sans-serif">🎱 Drain</text>
<line x1="180" y1="462" x2="180" y2="480" stroke="#c8a24a" stroke-width="1.5"/>
</svg>
</div>

- 🚀 **Plunger** — skyder kuglen ind på banen.
- 🔴 **Bumpere** — kuglen hopper af dem og scorer.
- 🎯 **Mål** — ram dem for at score (det er vores metal-**touch-pins**!).
- 🕹️ **Flippere** — slår kuglen op igen, så den ikke falder ned.
- 🎱 **Drain** — hullet i bunden; falder kuglen i, mister du den.
- 🔢 **Score** — hvor mange point du har.

Det er maskinen — lad os se, hvordan micro:bit'en styrer hver del 👇

## 🎛️ Flipper-funktioner → micro:bit

Alt hvad en flippermaskine kan, kan micro:bit'en også:

| Flipper-funktion | Vi bruger micro:bit'ens… |
|---|---|
| 🎯 Mål & bumpere giver point | **touch-pins** (P0, P1) |
| 🔢 Scoreboard | **LED-skærmen** |
| 🔊 "Ding!" og en game-over-melodi | **højtaleren** |
| 🎱 Kuglen ryger ud → mist et liv | en **drain-pin** (P2) + en `balls`-variabel |
| 💥 TILT (rystet for hårdt) | **ryste-sensoren** |
| 🕹️ Flippere (senere) | **knapperne A/B** → **servoer** på pins |
| 🌈 Banelys (senere) | en **NeoPixel**-strip på en pin |
| 🏆 Highscore (senere) | husk den i en **variabel** |

Ny til micro:bit'en og dens pins? Start med **[Mød dit udstyr](../../gear/README.md)** 🔧.

## 🔁 Opvarmning — hurtig repetition

En 30-sekunders genopfriskning: en **klik-tæller**. Tryk på **A**, og et tal stiger. Det tal er en **variabel** — præcis sådan en score virker.

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

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

## ▶️ Byg det — score ved berøring

Få det til at give point at røre **P0** og vise scoren.

1. Lav en **variabel** kaldet `score` (starter på 0).
2. Fra **Input**, brug **`on pin P0 pressed`**.
3. Indeni: **ændr `score` med 10**, og **vis tal `score`**.

Klik på **P0** i simulatoren (eller rør den rigtige pin) — se den stige! 🔢

??? example "👀 Kør det, eller læs koden"

    === "Blokke & simulator"

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

## 🪜 Gør det spilbart (dagens mål)

To små trin, og du har et rigtigt mini-spil.

**① Nulstil** ♻️ — tryk på **A** for at sætte scoren tilbage til 0.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**② Nyt spil** 🆕 — tryk på **B** for at nulstille og blinke **GO**.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

## 🕹️ Byg videre mod den rigtige maskine *(valgfrit)*

Færdig med målet? Byg videre — hvert trin tilføjer en rigtig flipper-funktion. Til sidst har du en lille maskine, du faktisk kan spille.

**③ Andet mål** 🎯 — forbind et metal til **P1**, værd **50**.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**④ Ding ved ramt** 🔊 — spil et kort bip, hver gang du scorer. Vi rydder scoringen ind i én **funktion**, så lyden bor ét sted. *(Kræver micro:bit **V2**-højtaler eller en buzzer.)*

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**⑤ 3 kugler & game over** 🎱 — et **drain**-mål (**P2**) koster en kugle; ved **0** viser den **OVER** og din slutscore. **B** giver dig 3 friske kugler.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

**⑥ 🏆 Boss — TILT!** — ryst for hårdt, og du **mister en kugle**. Nu er det en rigtig lille maskine: to mål, en ding, tre kugler, en drain, TILT, nulstil og nyt spil.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke & simulator"

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

## 🔭 Hvor vi er på vej hen

Henover semesteret vokser maskinen:

- 🕹️ **Flippere** — knapperne A/B styrer **servoer**, der flipper
- 🚀 **Plunger / affyring** — en knap (senere en servo) til at skyde kuglen
- 🌈 **Banelys** — en **NeoPixel**-strip, der blinker ved ramt
- 🏆 **Highscore** — husk det bedste spil
- ✨ **Bonus & multibold** — combos, multiplikatorer, ekstra kugler
- 😴 **Attract-mode** — scroll "PLAY!", når maskinen står stille

## ✅ Jeg er færdig når…

- ☐ At røre **P0** får **scoren** til at stige på skærmen.
- ☐ **A** nulstiller, og **B** starter et nyt spil.
- ☐ *(Level up!)* Et andet mål, en **ding**, **3 kugler** og **TILT** virker alle.

## 🎉 Kahoot-tid!

Slut af med denne uges quiz — **begge grupper spiller sammen**.

```kahoot
week-1
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan, materialer & noter"

    **Mål (i dag):** repetér variabler + knapper, og byg så **score-ved-berøring** med nulstil og nyt spil. Det er klassens mål. Trin ③–⑥ er valgfri stretch for hurtige og et smugkig på de kommende uger — I behøver ikke nå dem i dag.

    **Materialer**

    - micro:bit (**V2** anbefales — kapacitiv touch på P0/P1/P2 **og** den indbyggede højtaler til ding'en) + USB
    - **Keyestudio micro:bit sensor-shield**, krokodillenæb / jumper-ledninger, et par metalmål (folie, mønter)
    - Bærbar/Chromebook — **simulatoren er nok** til at bygge & teste (klik på pinsene)
    - *(V1 virker til scoring — metallet skal slutte et kredsløb til **GND**; ding'en kræver en buzzer.)*

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 projekt-intro + funktionskortet → 15 repetition klik-tæller → 10 slut til / hvordan pin-touch virker → 25 byg score-ved-berøring (P0) sammen → 5 tjek-ind
    - **Pause (20)**
    - **Blok 2 (30):** 15 nulstil (A) + nyt spil (B) → 5 hurtige starter level-up-stigen → 5 fremvisning → 5 Kahoot

    **Noter:** kun **P0/P1/P2** er touch-pads, så P2 fungerer også som "drain". Test i simulatoren ved at **klikke på pinsene**. `addPoints`/`loseBall` (④–⑥) er et blidt kig på **funktioner** (repeteres uge 7). Dette er **del 1** — flippere (servoer), lys (NeoPixels), plunger, highscore og multibold kommer senere.
