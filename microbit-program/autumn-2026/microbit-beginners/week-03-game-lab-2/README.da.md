# Uge 3 — Spil-lab 2 🎮

> Tilbage til Spil-labben! Lav **musik** 🎵, byg en **spåkugle** 🔮 og tegn dine egne billeder 🎨. *(Radio- & holdspil har deres egen session — se [Uge 4](../../week-04-game-lab/README.md).)*

!!! abstract "🎓 Hvad I lærer i dag"
    - **Musik**-klodserne — melodier & noder
    - mere **`hvis / ellers hvis`** — vælg mellem svar
    - **`vis lys`** — tegn dine egne billeder

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="et smiley-ansigt der blinker på LED-skærmen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ffd23f"><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><g><animate attributeName="opacity" dur="3s" repeatCount="indefinite" keyTimes="0;0.9;0.95;1" values="1;1;0;1"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/></g></g>
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
    - **💗 Kærlighedsmåler** — `ved tryk på pin P0` → `vis tal (vælg tilfældig 0 til 100)`. "Sensoren" er din krop: at holde **P0** og **GND** slutter et kredsløb, som tæller som et tryk — præcis som "kærlighedstester"-maskinerne i et tivoli. (V2 mærker berøring på P0 direkte.)

??? example "🎨 Tegn dit eget billede"

    Få **knap A** til at tænde dine egne LED'er med **`vis lys`** — tegn hvad som helst!

    ```makecode
    auto:draw
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

- ☐ Jeg byggede **Musik-maskinen** og fik den til at spille en melodi. 🎵
- ☐ Jeg narrede **Spåkuglen**. 🔮
- ☐ *(Legende!)* Jeg tegnede mit eget billede eller prøvede **Kærlighedsmåleren**.

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-3
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** en afslappet spil-session — **🎵 Musik-maskine** og **🔮 Spåkugle**, begge ren on-board-sjov (ingen ekstra dele). Børnene bygger i eget tempo og remixer så med bonusspillene. De større **radio- & holdspil** har nu deres egen session i **[Uge 4 — Spil-lab](../../week-04-game-lab/README.md)**.

    **Spillene (nemt → svært):**

    - **🎵 Musik-maskine** — Musik-klodserne. Højt og sjovt (høretelefoner hjælper i et fyldt lokale).
    - **🔮 Spåkugle** — mere `hvis / ellers`-træning, kun ikoner (ingen langsom tekst). Skør og social.
    - **🌟 Bonus** — tegn-dit-eget og en **💗 Kærlighedsmåler** (touch pin P0 → en første smagsprøve på et "kredsløb").

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 genopfrisk terningen → 25 byg **Musik-maskine** sammen (trin ①–③) → 10 overfør til boardet → 15 start **Spåkuglen** → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 20 færdiggør Spåkuglen + frit valg af bonusspil i eget tempo → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner direkte i **Blokke**. Hver *Byg det* viser en nem **start** først og derefter det **fulde** program, så børnene vokser ét program frem i stedet for at kopiere færdig kode. **🚀 Stjernefanger**-stækket er parkeret i `archive/week-02-star-catcher/`, hvis nogen vil have en større udfordring.
