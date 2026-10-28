# Uge 8 — Servo-bevægelser 🤖

> I dag begynder tingene at **bevæge sig**! Mød **servomotoren**, få den til at vinke, nikke og danse — og giv den et **papirkostume**. Det er også starten på vores **afsluttende projekt**: en papkasse-robot, der bevæger sig, lyser og laver lyde. 🎉

!!! abstract "🎓 Hvad I lærer i dag"
    - **servoer** — en lille motor, der drejer til en **vinkel** fra **0°** til **180°**
    - **at forbinde** — tre ledninger: **brun → G**, **rød → V**, **orange → S**
    - **bevægelse i kode** — `sæt vinkel`, løkker til bløde bevægelser, og sensorer (hældning, lys, berøring), der styrer servoen
    - **design** — planlæg din egen robot på papir

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="240" height="190" viewBox="0 0 240 190" role="img" aria-label="en servo, der vinker med en papirhånd" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<path d="M20 130 C 40 130, 40 150, 62 150" fill="none" stroke="#6d4c41" stroke-width="4"/>
<path d="M20 138 C 40 138, 40 156, 62 156" fill="none" stroke="#e53935" stroke-width="4"/>
<path d="M20 146 C 40 146, 40 162, 62 162" fill="none" stroke="#fb8c00" stroke-width="4"/>
<rect x="50" y="122" width="150" height="16" rx="4" fill="#1565c0"/>
<rect x="62" y="110" width="126" height="64" rx="8" fill="#1e88e5"/>
<text x="150" y="150" text-anchor="middle" fill="#fff" font-size="15" font-weight="700">SERVO</text>
<circle cx="96" cy="110" r="14" fill="#fff" stroke="#90a4ae" stroke-width="2"/>
<g>
<animateTransform attributeName="transform" type="rotate" values="-50 96 110;50 96 110;-50 96 110" dur="1.6s" repeatCount="indefinite"/>
<rect x="90" y="40" width="12" height="72" rx="6" fill="#fff" stroke="#90a4ae" stroke-width="2"/>
<text x="96" y="40" text-anchor="middle" font-size="34">✋</text>
</g>
<circle cx="96" cy="110" r="4" fill="#90a4ae"/>
</svg>
</div>

## 🏆 Vores afsluttende projekt starter i dag

I den **sidste time** viser alle en robot, de selv har bygget. Her er planen:

| Uge | Hvad vi laver |
|---|---|
| **8 — i dag** | Lær **servoen** + sjove bevægelser, og **design** så din robot på papir ✏️ |
| **9** | **Byg** kroppen af pap, og forbind servoen/servoerne ✂️ |
| **10** | Gør den **levende** — LED'er 💡, lyde 🔊, berørings-/lys-/hældningssensorer |
| **11** | 🎉 **Fremvisning** — vis din robot for alle |

**Regler:** papir, pap, tape, lim, snor og papirclips — **ingen plastik** (bortset fra elektronikken). ♻️

??? tip "💡 Robotidéer at tænke over"
    - 🤖 **Ticklebot** — kild den under foden, så vrikker og fniser den
    - 👋 **Vinkende robot** — siger hej, når du trykker på en knap
    - 🐶 **Nikkende hund** — nikker, når du hælder den eller klapper
    - 👾 **Sultent monster** — kæben smasker op og i
    - 🦋 **Flagrende sommerfugl / fugl** — vinger på to servoer
    - 🌻 **Solsikke** — åbner sig i lyset og lukker i mørket
    - 🎯 **Beslutningsrobot** — peger på "Ja / Nej / Måske"

## 🔌 Mød servoen

Vores servo er **mikroservoen 9g (SG90)** — en lille blå motor, der ikke drejer rundt og rundt — den drejer til en **vinkel**, du vælger, fra **0°** til **180°**, og **bliver der**. Den hvide plastikarm på toppen hedder **hornet** — det er der, dine papdele skal sidde.

!!! tip "Sådan forbinder du en servo 🔌"
    Sæt servoens stik med tre ledninger i **[sensor-shieldet](../gear/README.md)** på pin **P1**:

    - 🟤 **brun** (eller sort) → **G** (jord)
    - 🔴 **rød** → **V** (strøm)
    - 🟠 **orange** (eller gul) → **S** (signal)

    Læs de små bogstaver på boardet — og tjek, at farverne passer, før du tænder!

!!! warning "Før du starter ⚠️"
    - **Drej ikke armen med hånden** — det kan ødelægge tandhjulene indeni. Lad koden bevæge den.
    - SG90 er lavet til ca. **5 V**, men micro:bit'en giver ca. **3 V** — så med USB virker **én servo**, men den kan være lidt svag eller langsom. Hvis micro:bit'en **genstarter**, eller servoen **ryster**, så spørg efter en **batteripakke**.
    - Bygger du dit eget projekt i MakeCode? Tilføj servo-blokkene: **Udvidelser → søg "servo"**. (Programmerne på denne side har dem allerede.)

## 🎛️ Del 1 — De første bevægelser

### Peg med knapperne · P1

**A** → 0°, **B** → 180°, **A + B** → 90° (midten). Se, hvor armen peger hen!

??? example "👀 Se programmet"

    ```makecode
    auto:servo-buttons
    ```

    *🎓 Begreb: `servo P1 sæt vinkel til 90` — servoen drejer til den vinkel og bliver der.*

### Vink frem og tilbage · P1

En `for altid`-løkke: 0°, vent, 180°, vent… som en vinduesvisker. 🚗

??? example "👀 Se programmet"

    ```makecode
    auto:servo-sweep
    ```

    *Prøv: skift `pause 1000` til `300`. Eller brug 45° og 135° til et mindre vink.*

### 🛑 Tre stop · P1

Ét stop mere i midten: 0° → 90° → 180° → 90° → igen… De samme `sæt vinkel`- og `pause`-blokke — bare flere af dem.

??? example "👀 Se programmet"

    ```makecode
    auto:servo-stops
    ```

    *Prøv: tilføj et stop ved 45° og 135°. Kan du få armen til at besøge **fem** steder?*

### 👆 Klik-klik · P1

Hvert tryk på **A** flytter armen **30° videre**, **B** flytter den tilbage. Hvor mange klik skal der til, før den når enden? 🤔

??? example "👀 Se programmet"

    ```makecode
    auto:servo-click
    ```

    *Hvordan: variablen `angle` husker, hvor armen er. **A** lægger 30 til, **B** trækker 30 fra, og `min` / `maks` stopper den ved 180° og 0° — præcis som lysdæmperen i Uge 7. Prøv trin på **10°** eller **45°**.*

### 🕐 Urviser · P1

Armen **tikker** hen over i trin på 45° — *tik, tik, tik* — hopper så tilbage og starter forfra. ⏰

??? example "👀 Se programmet"

    ```makecode
    auto:servo-tick
    ```

    *Hvordan: en `for`-løkke tæller 0 → 4 og sætter vinklen til `index × 45` (0°, 45°, 90°, 135°, 180°). Nu gør vi trinene **bittesmå**, så bevægelsen bliver blød…*

### Langsomt og blødt · P1

I stedet for at hoppe bevæger armen sig **5° ad gangen** — langsomt og blødt, som en robot i en film. 🎬

??? example "👀 Se programmet"

    ```makecode
    auto:servo-slow
    ```

    *Hvordan: en `for`-løkke tæller 0 → 36 og sætter vinklen til `index × 5` (0° → 180°); en anden løkke går tilbage. Skift `pause 30` for at gøre det hurtigere eller langsommere.*

### Styr ved at hælde · P1

Hæld micro:bit'en til venstre og højre — servoen **følger med**! Som et rat. 🎡

??? example "👀 Se programmet"

    ```makecode
    auto:servo-tilt
    ```

    *Hvordan: `acceleration x` går fra cirka −1023 (hældt til venstre) til 1023 (hældt til højre), og `map` laver det om til 0°–180°.*

## ✂️ Del 2 — Giv den et papirkostume

Tape nu noget af **papir** fast på hornet — og giv din servo et job!

??? example "👋 Vinkende hånd · P1"

    Klip en **papirhånd** ud, og tape den fast på armen. Tryk **A** → den vinker hej 3 gange. 👋

    ```makecode
    auto:servo-wave
    ```

    *Prøv: vink 5 gange? Hurtigere? Vis et andet ansigt?*

??? example "🌻 Solsikke · P1 — *kan du huske lyssensoren?*"

    Lav en **papirblomst** (eller en sol) på armen. I **lyset** står den op og åbner sig 🌞; **dæk skærmen**, så falder den i søvn 😴.

    ```makecode
    auto:servo-flower
    ```

    *Ligesom Halloween-spøgelset: **skærmen** er lyssensoren. Sover den altid? Så er lokalet mørkere end **50** — skift `50` til **20**.*

??? example "🎯 Beslutnings-spinner · P1"

    Tegn en **halvcirkel-skive** på pap: *Ja · Nej · Måske · Spørg igen* 🤔. Tryk **A** → armen vakler, tikker… og stopper på et svar!

    ```makecode
    auto:servo-spinner
    ```

    *Hvordan: `vælg tilfældig 0 til 180` giver en tilfældig vinkel. Lav din egen skive — "Hvem starter?", "Hvad skal vi have til aftensmad?", "Hvilket spil?"*

??? example "🤖 Kild mig! · P1 + berøring P2"

    En første smagsprøve på **Ticklebot'en**: rør **P2** (og hold om **G**) → et fnis og et vrik! 😆 Tape et stykke **sølvpapir** på enden af en ledning i **P2** for at lave en "fod".

    ```makecode
    auto:servo-tickle
    ```

    *Hvordan: `når pin P2 trykkes` virker præcis som kildetælleren i Uge 7 — nu bevæger den en servo i stedet.*

## 🚀 Level op — to servoer & fjernstyring

??? example "💃 Robotdans · P1 + P2"

    Sæt en **servo mere** i **P2**. Tryk **A** → musik + en dans: armene svinger hver sin vej og vinker så sammen! 🎶

    ```makecode
    auto:servo-dance
    ```

    *To servoer kan kræve en **batteripakke**. Prøv at lave to papirarme eller to vinger!*

??? example "🎮 Fjernstyret arm · radio · P1"

    Arbejd sammen med en **makker**: I downloader begge to programmet. **Hold A og hæld** → **din makkers** servo bevæger sig! 📡

    ```makecode
    auto:servo-remote
    ```

    *Vigtigt: hvert par skifter `radio sæt gruppe 8` til **deres eget nummer** (som i Uge 4) — ellers styrer I alles servoer!*

## ✏️ Design din robot

Tag et stykke papir, og planlæg dit afsluttende projekt. Tegn den, og svar på:

1. **Hvad hedder den?** 🏷️
2. **Hvad bevæger sig?** (en arm, et hoved, en mund, vinger…) — det er din **servo** 🔧
3. **Hvad lyser?** (øjne, et hjerte, en næse…) — dine **LED'er** 💡
4. **Hvilken lyd laver den?** 🔊
5. **Hvad får den til at reagere?** (en knap, berøring, lys, hældning, rystelse…) 👆
6. **Hvad skal jeg have med?** (kasser, toiletruller, papir, snor…) 📦

Gem din tegning — du skal bygge robotten i næste uge! 🛠️

## ✅ Jeg er færdig når…

- ☐ Jeg forbandt en **servo** (brun → G, rød → V, orange → S) og bevægede den med **knapperne**. 🔌
- ☐ Jeg fik den til at **svinge** og flyttede den så **trin for trin** (tre stop, klik-klik eller urviseren). 🔁
- ☐ Jeg fik den til at bevæge sig **langsomt og blødt**. 🎬
- ☐ Jeg styrede den ved at **hælde** micro:bit'en. 🎡
- ☐ Jeg gav min servo et **papirkostume** (hånd, blomst eller spinner). ✂️
- ☐ *(Legende!)* Jeg lavede **kilderobotten**, **dansen** eller den **fjernstyrede arm**. 🤖
- ☐ Jeg **tegnede min robot** til det afsluttende projekt. ✏️

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-8
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** alle kan forbinde en servo og bevæge den fra kode, prøver en papir-rekvisit og går hjem med en **skitse af deres robot til det afsluttende projekt**. De hurtige prøver to servoer og radio.

    **Materialer**

    - micro:bits + USB + **sensor-shields** — **1 pr. barn**
    - **mikroservo 9g (SG90)**, 0–180° — **1 pr. barn**, nogle ekstra til dansen med to servoer; de små skruer til hornene
    - **batteripakker** (AA/AAA til shieldet eller micro:bit'en) — nødvendige til to servoer, eller hvis boards bliver ved med at genstarte
    - **pap, papir, karton, malertape, limstifter, sakse, tusser, snor, papirclips, sølvpapir** — **ingen plastik**
    - **A4-papir + blyanter** til robotdesignet

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 afsløring af det afsluttende projekt + robotidéer → 10 **mød servoen + forbind** → 15 **knapper → sving → tre stop → klik-klik → urviser** → 10 **langsomt og blødt → hældning** → 15 ✂️ **papirkostume** (hvert barn vælger vinke / solsikke / spinner) → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 10 🤖 **kild / dans / fjernstyring** (de hurtige) → 15 ✏️ **design din robot** (gem arkene til næste uge!) → 5 Kahoot.

    **Noter:** hver indlejring åbner i **Blokke** og har allerede **servo**-udvidelsen; børn, der starter forfra, tilføjer den via **Udvidelser → "servo"**. **Genstart, summen eller en micro:bit, der går helt ud**, når servoen bevæger sig = for lidt strøm → batteripakke (to servoer kræver næsten altid en). Hvis servoen **slet ikke bevæger sig**, så tjek, at stikket ikke sidder **omvendt** (brun på G), og at det sidder i **P1**. De fleste sæt er **positionsservoer** (0–180°); en **kontinuerlig** (360°) servo drejer rundt i stedet for at pege — den skal bruge blokken `continuous servo P1 run at …%` i stedet for `sæt vinkel`. Sæt hornet på **ved 90°** (kør knap-programmet, tryk A + B, og sæt så armen på), så papirdelene starter lige. Lyden i disse programmer kolliderer ikke med P1/P2. Til den fjernstyrede arm: **giv hvert par et gruppenummer**, før de starter. Saml robotskitserne ind — Uge 9 starter fra dem.
