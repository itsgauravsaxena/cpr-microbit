# Uge 3 — Spil-lab 2 🎮

> Tilbage til Spil-labben! Sidste uge byggede du terningen 🎲 — nu skal du lave **musik** 🎵, sende **hemmelige radiobeskeder** 📻 og bygge en **spåkugle** 🔮.

!!! abstract "🎓 Hvad I lærer i dag"
    - **radio** — to micro:bits der taler sammen
    - **Musik**-klodserne — melodier & noder
    - mere **`hvis / ellers`** — vælg mellem svar

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="et hjerte der banker på LED-skærmen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" dur="1.4s" repeatCount="indefinite" values="1;0.3;1" keyTimes="0;0.5;1"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

## 🎮 Vælg et spil

Vælg et spil, byg klodserne, spil det. Hvert spil har en **🔨 Byg det** med en nem start og derefter det fulde spil. Ny her? **[Uge 2](../week-02-name-tag-smiley-buttons/README.md)** har opvarmningen og terningen. 🌱

### 🎵 Musik-maskine

Knapper laver musik. Ryst for en overraskelses-melodi! 🎵 *(skru op for lyden 🔊)*

*🎓 Begreb: **Musik**-klodserne — melodier & noder.*

??? note "Sådan virker det"

    **Formål.** Højt og motiverende. Det viser, at hver **hændelse** kan udløse sin egen lyd, og introducerer **Musik**-kategorien.

    **Tænk på det som en lydpult:** hver knap er en pad, der affyrer sit eget klip — tryk en anden pad, hør en anden lyd.

    **Sådan virker koden:**

    - Tre hændelser styrer det hele: `ved tryk på knap A`, `ved tryk på knap B` og `ved ryst`.
    - Hver kalder `start melodi` med en **indbygget melodi** (Ba Ding, Jump Up, Nyan) sat til at spille **én gang**.
    - Ryste-versionen blinker også en ottendedelsnode ♪ først og spiller så overraskelses-sangen — en nem måde at vise, at man kan stable to handlinger i én hændelse.

    **Vær opmærksom på:** den kræver lyd — en micro:bit **V2** har en indbygget højtaler; på **V1** eller i et stille lokale: sæt høretelefoner/en buzzer i pin 0. En melodi spiller færdig, men et nyt tryk starter en anden oven i.

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

??? note "Sådan virker det"

    **Formål.** Semesterets magiske øjeblik — to boards taler *trådløst*. Det lærer **send**, **modtag** og idéen om en fælles **gruppe** (kanal).

    **Tænk på det som walkie-talkies:** I hører kun hinanden, hvis I begge er på samme kanal — det er det, gruppenummeret gør.

    **Sådan virker koden:**

    - `radio sæt gruppe 1` i starten sætter boardet på en kanal. Kun boards på **samme gruppenummer** kan høre hinanden.
    - `ved tryk på knap A` → `send tal 1`; `ved tryk på knap B` → `send tal 2`. At sende udsender bare et tal ud i luften.
    - `ved radio modtaget (receivedNumber)` er en **ny slags hændelse** — den kører på det *andet* board, når et tal ankommer. Et `hvis / ellers` viser et 💗 ved `1` og et 😀 ved `2`.
    - Begge makkere flasher **samme** program, så hvert board både kan sende og modtage.

    **Vær opmærksom på:** I skal bruge **2 boards pr. par**, begge på samme gruppe. Beslut gruppenumre samlet i klassen (par 1 → gruppe 1, par 2 → gruppe 2 …), så signalerne ikke krydser. Radio kan ikke testes med én simulator — denne kræver rigtige boards.

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

??? note "Sådan virker det"

    **Formål.** Skør og social — børn elsker at stille den spørgsmål. Det er ekstra `hvis / ellers hvis`-træning med kun ikoner (ingen langsom tekst).

    **Tænk på det som en Magic 8-Ball:** ryst den, vent, mens den "tænker", og få et af nogle få faste svar tilbage.

    **Sådan virker koden:**

    - `ved ryst` viser et "tænker"-ikon 😴 og `pause 500 ms` — den lille forsinkelse er det, der får micro:bit'en til at *virke betænksom*.
    - `vælg tilfældig 0 til 3` gemmer et tal i en variabel (`pick`).
    - En `hvis / ellers hvis`-kæde knytter hver værdi til et svar: 0 → Ja ✓, 1 → Nej ✗, 2 → 🤔, 3 → 😀 — **fire** mulige udfald.

    **Vær opmærksom på:** fire svar kommer af `0 til 3` (fire værdier, talt fra nul). Vil du have et femte svar, så udvid til `0 til 4` *og* tilføj ét `ellers hvis` mere.

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

??? note "Sådan virker bonusspillene"

    **Formål.** Hurtige udvidelser til de hurtige — ingen nye begreber, bare remix af det, de kan.

    - **🎨 Tegn dit eget** — `ved tryk på knap A` → `vis lys` med et hånd-tændt 5×5-mønster. Ren kreativitet — som pixelkunst på en Etch A Sketch.
    - **✊✋✌️ Sten, Saks, Papir** — `ved ryst` → `vælg tilfældig 0 til 2` → et `hvis / ellers hvis` viser firkant / fyldt gitter / saks. Samme tilfældig-og-vælg-mønster som terningen, nu til en dyst i skolegården.
    - **💗 Kærlighedsmåler** — `ved tryk på pin P0` → `vis tal (vælg tilfældig 0 til 100)`. "Sensoren" er din krop: at holde **P0** og **GND** slutter et kredsløb, som tæller som et tryk — præcis som "kærlighedstester"-maskinerne i et tivoli. (V2 mærker berøring på P0 direkte.)

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

??? example "💗 Kærlighedsmåler"

    Hold **pin 0** med den ene hånd og rør **GND** med den anden — micro:bit'en viser, hvor 'varme' dine fingre er (et tilfældigt tal **0–100**). 💗

    Byg den med 30-sekunders-tricket: åbn <https://makecode.microbit.org> → **New Project** → klik på **`{ } JavaScript`**, slet alt, indsæt dette, og klik så på **Blocks**:

    ```javascript
    input.onPinPressed(TouchPin.P0, function () {
        basic.showNumber(Math.randomRange(0, 100))
    })
    ```

## ✅ Jeg er færdig når…

- ☐ Jeg byggede **mindst ét spil** (musik, radio eller spåkugle) og spillede det.
- ☐ Jeg sendte en **hemmelig radiobesked** til en makker. 📻
- ☐ *(Legende!)* Jeg byggede **to eller flere** spil — eller narrede spåkuglen. 🔮

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-3
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** dette er anden halvdel af Spil-labben — spillene, der ikke kunne nås i Uge 2. Børnene vælger fra en menu af små **spil** i eget tempo. **📻 Hemmelige beskeder** er højdepunktet: den kræver **2 boards pr. par**, begge på **samme gruppe**. Der er med vilje **mere her end der kan nås på én session** — bedre for meget end for lidt. 🎯

    **Spillene (nemt → svært):**

    - **🎵 Musik-maskine** — Musik-klodserne. Højt og sjovt (høretelefoner hjælper i et fyldt lokale).
    - **📻 Hemmelige beskeder** — **radio**; kræver **2 boards pr. par**, begge på **samme gruppe**. Magisk for børn.
    - **🔮 Spåkugle** — mere `hvis / ellers`-træning, kun ikoner (ingen langsom tekst). Skør og social — børn elsker at stille den spørgsmål.
    - **🌟 Bonus** — tegn-dit-eget, sten-saks-papir og en **💗 Kærlighedsmåler** (touch pin P0).

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 genopfrisk terningen → 15 byg **Musik-maskine** sammen → 10 overfør til boardet → 25 dan par til **Hemmelige beskeder** (sæt samme gruppe) → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 20 frit valg fra menuen (Spåkugle, bonusspil) i eget tempo → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner direkte i **Blokke**. Hver *Byg det* viser en nem **start** først og derefter det **fulde** program, så børnene vokser ét program frem i stedet for at kopiere færdig kode. Radio kræver ens **gruppenumre** — beslut dem samlet i klassen, så par ikke støder sammen. **🚀 Stjernefanger**-stækket er parkeret i `archive/week-02-star-catcher/`, hvis nogen vil have en større udfordring.
