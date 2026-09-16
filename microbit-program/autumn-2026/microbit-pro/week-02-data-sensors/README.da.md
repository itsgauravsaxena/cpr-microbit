# Uge 2 — Flipper-scoreboard 🎯 (del 1)

**🔗 Åbn siden på en computer:** gå til **[tinyurl.com/mbprow2](https://tinyurl.com/mbprow2)**

> Dette semester bygger Pro-holdet **hjernen i en flippermaskine** — lidt hver uge. Vi starter byggeriet: en hurtig repetition, og så den allerførste del — en **score, der stiger, når du rammer et mål**.

!!! abstract "🎓 Hvad I lærer i dag"
    - **variabler** — et tal, I kan ændre (scoren)
    - **hændelser** — kør kode ved knapper & touch-pins
    - **funktioner** *(Level up)* — navngiv en opgave, genbrug den

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="gættespillet der tæller" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

!!! info "🎯 Ny til flipperprojektet?"
    Se **[Flipperprojektet](../../pinball/README.md)** for det store billede — flipperens dele, hvordan micro:bit'en styrer hver del, og hvor byggeriet er på vej hen.

## 🎯 Hvad vi laver i dag

**Begyndelsen** på vores flipper-scoreboard: rør et mål, og din **score** stiger — plus en **nulstil**- og en **nyt spil**-knap. Det er målet for i dag. Færdig tidligt? Der er en valgfri **level-up**-stige, der gør det til en rigtig lille maskine.

*(Den 3D-printede flipperkasse er den anden gruppes opgave — vi bygger koden.)*

## 🔁 Opvarmning — hurtig repetition

En 30-sekunders genopfriskning: en **klik-tæller**. Tryk på **A**, og et tal stiger. Det tal er en **variabel** — præcis sådan en score virker.

*🎓 Begreb: **variabler** — et tal, I kan ændre.*

??? note "Sådan virker det"

    **Formål.** En 30-sekunders genopfriskning, der beviser, at en **variabel** bare er et tal, boardet *husker* — præcis sådan en score virker.

    **Tænk på det som en klik-tæller:** en dørmands tælle-klikker lægger én til ved hvert tryk og husker den løbende sum — en flipper-score er samme idé.

    **Sådan virker koden:** `count` starter på `0`. `ved tryk på knap A` kører `ændr count med 1` og så `vis tal count`. Nøgleidéen: `count` beholder sin værdi mellem tryk, så hvert tryk bygger videre på det forrige. Skift "count" ud med "score", og du har allerede flipper-scoreboardet.

??? example "👀 Kør det, eller læs koden"

    === "Blokke"

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

*🎓 Begreb: **hændelser** + **input** — en touch-pin ændrer en variabel.*

??? note "Sådan virker det"

    **Formål.** Hjertet i hele semesterets byg: et hit på et mål får **scoren** til at stige. Alt det senere (flere mål, kugler, TILT, kablede kontakter) hænger på denne ene idé.

    **I flipperen:** det her *er* en **bumper** — kuglen rører målet, og pointene ringer op. Pin-"berøringen" er kuglen, der slutter en kontakt.

    **Sådan virker koden:**

    - `score` er en variabel, der starter på `0`.
    - `ved tryk på pin P0` er en **hændelse**, der udløses, når metalmålet slutter et kredsløb (P0 → din hånd/kuglen → **GND**). Indeni: `ændr score med 10`, og så `vis tal score`.
    - **Nulstil (A)** sætter `score` tilbage til 0; **Nyt spil (B)** nulstiller og blinker `GO` — to knap-hændelser mere.

    **Vær opmærksom på:** i simulatoren *klikker* du på P0-pinnen for at snyde en berøring. På hardware skal berøringen nå **GND** — en **V2** mærker dette kapacitivt på P0/P1/P2; en **V1** kræver, at metallet faktisk slutter et kredsløb til en GND-pin.

1. Lav en **variabel** kaldet `score` (starter på 0).
2. Fra **Input**, brug **`on pin P0 pressed`**.
3. Indeni: **ændr `score` med 10**, og **vis tal `score`**.

Klik på **P0** i simulatoren (eller rør den rigtige pin) — se den stige! 🔢

!!! tip "🔌 På det rigtige board — brug shieldet"
    Sæt din micro:bit i **Keyestudio sensor-shieldet**, så hver pin bliver et nemt stik, og klips en ledning fra metalmålet til **P0** og en til **GND**. *(Uden shieldet kan I kun nå de store **P0/P1/P2**-pads.)* Hele guiden: **[Mød udstyret](../../gear/README.md#at-forbinde-et-berringsmal-til-vores-flipper)**.

??? example "👀 Kør det, eller læs koden"

    === "Blokke"

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

*🎓 Begreb: **hændelser** — knap A/B styrer spillet.*

**① Nulstil** ♻️ — tryk på **A** for at sætte scoren tilbage til 0.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke"

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

    === "Blokke"

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

*🎓 Begreb: **funktioner** — navngiv en opgave, genbrug den.*

??? note "Sådan virker det"

    **Formål.** Så snart der er flere mål og regler, bliver copy-paste af de samme linjer skrøbeligt. En **funktion** lader dig navngive en opgave én gang og genbruge den — kursets første rigtige "softwaredesign"-idé.

    **Tænk på det som et stempel:** skær stemplet én gang (funktionen), og så stempler hver bumper sine point på samme måde — skær stemplet om, og de ændrer sig alle på én gang.

    **Sådan virker koden:**

    - `addPoints(points)` er en funktion med de tre linjer, hvert mål har brug for: `ændr score`, spil **ding'en**, `vis tal`. Hvert mål kalder bare `addPoints(10)` eller `addPoints(50)` i stedet for at gentage dem.
    - `loseBall()` er en anden funktion: den trækker en kugle fra, og med et `hvis / ellers` viser den **OVER** + slutscoren, når kuglerne når 0, ellers hvor mange der er tilbage. Både **drainet (P2)** og **TILT (ryst)** kalder `loseBall()`, så "mist en kugle" opfører sig ens, uanset hvor den udløses.
    - `score` og `balls` er variabler, funktionerne læser og opdaterer.

    **Vær opmærksom på:** gevinsten er *ret ét sted, rettet alle steder* — fx ret ding'en inde i `addPoints`, og hvert mål opdateres. Trin ③–⑥ er valgfri stretch; funktioner vender ordentligt tilbage i uge 7.

**③ Andet mål** 🎯 — forbind et metal til **P1**, værd **50**.

??? example "👀 Kig — kør det, eller læs koden"

    === "Blokke"

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

    === "Blokke"

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

    === "Blokke"

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

    === "Blokke"

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

## ⚡ Næste uge — slut jeres egne kontakter til

**[Uge 3 — Pinball-kontakter](../week-03-pinball-switches/README.md)** samler bygget op med det samme. Indtil nu er jeres mål de **3 touch-pins** (P0/P1/P2); en rigtig flipper har *masser* af mål, bumpere og baner — og hver eneste er bare en lille **kontakt, som kuglen slutter**. Næste uge er den **elektronik-først**-stige: slut og læs jeres egne kontakter, så maskinen kan vokse, så stor I vil. Færdig med dagens mål og level-up-stigen? Tag et smugkig. 🔌

## ✅ Jeg er færdig når…

- ☐ At røre **P0** får **scoren** til at stige på skærmen.
- ☐ **A** nulstiller, og **B** starter et nyt spil.
- ☐ *(Level up!)* Et andet mål, en **ding**, **3 kugler** og **TILT** virker alle.

## 🎉 Kahoot-tid!

Slut af med denne uges quiz — **begge grupper spiller sammen**.

```kahoot
week-2
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan, materialer & noter"

    **Mål (i dag):** repetér variabler + knapper, og byg så **score-ved-berøring** med nulstil og nyt spil. Det er klassens mål. Trin ③–⑥ er valgfri stretch for hurtige og et smugkig på de kommende uger — I behøver ikke nå dem i dag. Den dybere, **elektronik-først**-stretch — at læse jeres egne **kontakter** — er flyttet til **[Uge 3 — Pinball-kontakter](../week-03-pinball-switches/README.md)**, så i dag holder fokus på at få alle til at score.

    **Materialer**

    - micro:bit (**V2** anbefales — kapacitiv touch på P0/P1/P2 **og** den indbyggede højtaler til ding'en) + USB
    - **Keyestudio micro:bit sensor-shield**, krokodillenæb / jumper-ledninger, et par metalmål (folie, mønter)
    - Bærbar/Chromebook — **simulatoren er nok** til at bygge & teste (klik på pinsene)
    - *(V1 virker til scoring — metallet skal slutte et kredsløb til **GND**; ding'en kræver en buzzer.)*

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 projekt-intro + funktionskortet → 15 repetition klik-tæller → 10 slut til / hvordan pin-touch virker → 25 byg score-ved-berøring (P0) sammen → 5 tjek-ind
    - **Pause (20)**
    - **Blok 2 (30):** 15 nulstil (A) + nyt spil (B) → 5 hurtige starter level-up-stigen → 5 fremvisning → 5 Kahoot

    **Noter:** kun **P0/P1/P2** er touch-pads, så P2 fungerer også som "drain". Test i simulatoren ved at **klikke på pinsene**. `addPoints`/`loseBall` (④–⑥) er et blidt kig på **funktioner** (repeteres uge 7). Dette er **del 1** — **kontakt-læse**-stigen er nu **[Uge 3](../week-03-pinball-switches/README.md)**; flippere (servoer), lys (NeoPixels), plunger, highscore og multibold kommer senere.
