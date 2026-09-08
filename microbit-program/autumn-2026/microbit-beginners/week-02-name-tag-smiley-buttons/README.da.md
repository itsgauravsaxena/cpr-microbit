# Uge 2 — Spil-lab 🎮

> Varm op med en ansigtsmaskine, og byg så **rigtige spil**: terning 🎲, musik 🎵, hemmelige radiobeskeder 📻 og en spåkugle 🔮.

!!! abstract "🎓 Hvad I lærer i dag"
    - **hændelser** — kør kode ved en knap eller et ryst
    - **`hvis / ellers`** (betingelser) — få micro:bit'en til at *vælge*
    - **tilfældig** — overraskelsestal
    - **radio** — to micro:bits der taler sammen
    - **Musik**-klodserne — melodier & noder

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="220" height="220" viewBox="0 0 216 216" role="img" aria-label="et ansigt der skifter glad, ked af det, overrasket" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="0" y="0" width="216" height="216" rx="24" fill="#0f1419" stroke="#c8a24a" stroke-width="3"/>
<rect x="17" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#2b3038"/>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
</svg>
</div>

## 🔥 Opvarmning: Knap-ansigter

Knapper laver ansigter, et ryst giver en overraskelse. Tryk på **▶️ Open & run** for at lege:

*🎓 Begreb: **hændelser** — kør kode ved knap eller ryst.*

??? example "👀 Se de færdige klodser"

    ```makecode
    auto
    ```

??? example "🔨 Byg det — ét trin ad gangen"

    Åbn hvert trin, tilføj **kun de nye klodser**, og tjek mod billedet. 🌱

    **① Glad ansigt på knap A**

    ```makecode
    auto:step-1
    ```

    **② Ked-af-det ansigt på knap B**

    ```makecode
    auto:step-2
    ```

    **③ Hjerte på A + B (tryk begge!)**

    ```makecode
    auto:step-3
    ```

    **④ Overraskelse når du ryster**

    ```makecode
    auto:step-4
    ```

    **⑤ Et *tilfældigt* ansigt når du ryster**

    ```makecode
    auto:step-5
    ```

    **⑥ Sig hej når den starter**

    ```makecode
    auto:step-6
    ```

---

## 🎮 Byg nu et spil!

Vælg et spil, byg klodserne, spil det. Start nemt — arbejd dig op. Hvert spil har en **🔨 Byg det** med en nem start og derefter det fulde spil. 🌱

### 🎲 Terning

Ryst for et tilfældigt **1–6**. 🎲

*🎓 Begreb: **tilfældig** + **`hvis / ellers`** (betingelser).*

??? example "👀 Se det færdige spil"

    ```makecode
    auto:dice
    ```

??? example "🔨 Byg det — 3 små trin"

    **① Rul et tal** — ryst → et tilfældigt **1–6**:

    ```makecode
    auto:dice-1
    ```

    **② Gør 6 speciel** — dit første `hvis / ellers`: et **6-tal** viser et ✓, alt andet viser tallet:

    ```makecode
    auto:dice-2
    ```

    **③ Rigtig terning** — byt tallet ud med **prikker** (et større `hvis / ellers`):

    ```makecode
    auto:dice
    ```

### 🎵 Musik-maskine

Knapper laver musik. Ryst for en overraskelses-melodi! 🎵 *(skru op for lyden 🔊)*

*🎓 Begreb: **Musik**-klodserne — melodier & noder.*

??? example "👀 Se det færdige spil"

    ```makecode
    auto:music
    ```

??? example "🔨 Byg det — 3 små trin"

    **① Tryk på A** — én knap, én lyd:

    ```makecode
    auto:music-1
    ```

    **② Tilføj B** — en knap mere med en anden melodi:

    ```makecode
    auto:music-2
    ```

    **③ Ryste-overraskelse** — tilføj **ryst** → en node 🎵 og en overraskelses-sang:

    ```makecode
    auto:music
    ```

### 📻 Hemmelige beskeder

Send hjerter 💗 og smileys 😀 til en vens micro:bit — gennem luften! 📻

*🎓 Begreb: **radio** — send & modtag mellem micro:bits.*

!!! tip "I skal bruge **to** micro:bits"
    Du og din makker bruger begge det **samme gruppenummer** (skift `1`-tallet i *sæt gruppe*). Vælg jeres eget, så I ikke blander jer med det næste par!

??? example "👀 Se det færdige spil"

    ```makecode
    auto:radio
    ```

??? example "🔨 Byg det — 3 små trin"

    **① Send + vis** — sæt din **gruppe**, tryk på **A** for at sende, vis et 💗 når en besked kommer:

    ```makecode
    auto:radio-1
    ```

    **② Knap nummer to** — tilføj **B**, så du kan sende to forskellige beskeder:

    ```makecode
    auto:radio-2
    ```

    **③ To billeder** — brug `hvis / ellers`, så **A** viser et hjerte 💗 og **B** en smiley 😀:

    ```makecode
    auto:radio
    ```

### 🔮 Spåkugle

Stil et ja/nej-spørgsmål, giv den et ryst, og se hvad den siger! 🔮

*🎓 Begreb: **`hvis / ellers hvis`** — vælg mellem svar.*

??? example "👀 Se det færdige spil"

    ```makecode
    auto:fortune
    ```

??? example "🔨 Byg det — 3 små trin"

    **① Ja eller nej** — ryst → ✓ eller ✗ (dit første `hvis / ellers`):

    ```makecode
    auto:fortune-1
    ```

    **② Tilføj Måske** — et tredje svar 🤔 med `ellers hvis`:

    ```makecode
    auto:fortune-2
    ```

    **③ Lad den tænke** — den "tænker" først 😴 og giver så et af **fire** svar:

    ```makecode
    auto:fortune
    ```

---

## 🌟 Bonus

??? example "🎨 Tegn dit eget billede"

    Få **knap A** til at tænde dine egne LED'er med **`vis lys`** — tegn hvad som helst!

    ```makecode
    auto:draw
    ```

??? example "✊✋✌️ Sten, Saks, Papir"

    Ryst for at kaste sten, saks eller papir — dyst så mod en ven, bedst af fem!

    ```makecode
    auto:rps
    ```

## ✅ Jeg er færdig når…

- ☐ Mine **Knap-ansigter** virker på det rigtige board (A 😀, B 🙁).
- ☐ Jeg byggede **mindst ét spil** og spillede det.
- ☐ *(Legende!)* Jeg byggede **to eller flere** spil — eller narrede spåkuglen. 🔮

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-2
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** byg videre på Uge 1's `vis ikon`. Varm op med **Knap-ansigter** (knapper A/B/A+B, ryst, en første smagsprøve på **tilfældig**), og lad så børnene vælge fra en menu af små **spil**, så de hurtige altid har mere at strække sig efter. Der er med vilje **mere her end der kan nås på én session** — det er meningen. 🎯

    **Spillene (nemt → svært):**

    - **🎲 Terning** — `vælg tilfældig` + `hvis/ellers`. Alle kan nå denne.
    - **🎵 Musik-maskine** — Musik-klodserne. Højt og sjovt (høretelefoner hjælper i et fyldt lokale).
    - **📻 Hemmelige beskeder** — første smagsprøve på **radio**; kræver **2 boards pr. par**, begge på **samme gruppe**. Magisk for børn.
    - **🔮 Spåkugle** — mere `hvis / ellers`-træning, kun ikoner (ingen langsom tekst). Skør og social — børn elsker at stille den spørgsmål.

    *(Et større **🚀 Stjernefanger**-spil — variabel + løkke + LED-tegning — er parkeret i `archive/week-02-star-catcher/`, hvis du vil have et sværere Uge 3-stræk. Sådan henter du det tilbage står i den mappes README.)*

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 genopfrisk Uge 1 → 30 byg **Knap-ansigter** sammen (trin ①–⑥) → 10 overfør til boardet → 15 start **Terning**.
    - **Pause (20)**
    - **Blok 2 (30):** 20 frit valg fra spil-menuen (Terning → Musik → Radio → Spåkugle) i eget tempo → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner direkte i **Blokke**. Hver *Byg det* viser en nem **start** først og derefter det **fulde** program, så børnene vokser ét program frem i stedet for at kopiere færdig kode. De øvrige spil er perfekte at tage med til **Uge 3** — bedre at have for meget end for lidt.
