# Uge 6 — Holdspil 🎮

> To skolegårds-klassikere, nu **over radio**: **Rødt lys, grønt lys** 🚦 og **Sten-Saks-Papir** ✊✋✌️ — hver med et level op til de hurtige.

!!! abstract "🎓 Hvad I lærer i dag"
    - **sender & modtager** — én kalder, mange spillere
    - **accelerometeret** — at fange bevægelse
    - **tilfældig** + **variabler** — fair kast og at holde point

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="et rødt lys der bliver grønt" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g><animate attributeName="fill" calcMode="discrete" dur="2s" repeatCount="indefinite" keyTimes="0;0.5" values="#ff4d4d;#59b04a"/><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

## 🎮 Vælg et spil

Begge spil bruger **to eller flere micro:bits** på samme **gruppe**. Læg et program på hvert board, og spil! Ny til radio? Start med **[Uge 4 — Spil-lab](../week-04-game-lab/README.md)**. 🌱

### 🚦 Rødt lys, grønt lys

Skolegårdens klassiker — på micro:bit'en! Det ene board er **kalderen** (trafiklyset); alle andre holder et **spiller**-board. Bevæg dig på grønt ✓, frys på rødt ✗ — bliver du fanget i at bevæge dig på rødt, er du **ude**! 🚦

*🎓 Begreb: **sender & modtager** + **accelerometeret** (det mærker, at du bevæger dig).*

!!! tip "Én kalder, mange spillere — samme gruppe"
    Læg **`LIGHT`** (kalderen) på ét board og **`PLAYER`** på alle andres, alle på **samme gruppe**. Kalderen trykker **A = grøn**, **B = rød**.

??? example "👀 Se de to programmer"

    **🚦 Kalder (trafiklyset)** — tryk A for grøn, B for rød:

    ```makecode
    auto:rlgl-light
    ```

    **🏃 Spiller** — ✓ grøn = gå, ✗ rød = frys. Bevæg dig på rødt → 💀 ude!

    ```makecode
    auto:rlgl-player
    ```

??? note "Sådan virker det"

    **Tænk på det som den rigtige leg — micro:bit'en er en dommer, der aldrig blinker.**

    - **Kalderen** er en *sender*: **A** sender `1` (grøn ✓), **B** sender `2` (rød ✗).
    - Hver **spiller** er en *modtager*: den husker lyset i en variabel. `på ryst` = "du bevægede dig" — er lyset **rødt** lige da, viser den et 💀 og kalder **game over**.

    **Vær opmærksom på:** kræver **2+ boards på samme gruppe**. I simulatoren: ryst spilleren, mens lyset er rødt, for at se game over; på rigtige boards fanger *accelerometeret* rigtig bevægelse.

??? example "🚀 Level op — automatisk kalder"

    Ikke flere knaptryk — lyset skifter **rødt/grønt af sig selv** på tilfældige tidspunkter, så ingen kan forudse det. Snedigt! Spillerne beholder samme **`PLAYER`**-program.

    **🚦 Auto-kalder** — tilfældigt grønt, så tilfældigt rødt, for altid:

    ```makecode
    auto:rlgl-auto
    ```

    *Hvordan: en `for altid`-løkke sender grønt, venter et **tilfældigt** `1–4 s`, sender rødt, venter tilfældigt `1–3 s`, og gentager — `vælg tilfældig` gør timingen umulig at gætte.*

### ✊✋✌️ Sten, Saks, Papir

Ryst for at kaste ✊✋✌️. Spil det **solo**, og **dyst så mod en ven gennem luften** — boardene dømmer vinderen for dig!

*🎓 Begreb: **tilfældig** til at kaste, **radio** til at dyste.*

??? example "👀 Solo — ét board"

    Ryst for at kaste sten, saks eller papir:

    ```makecode
    auto:rps
    ```

??? example "🚀 Level op — dyst over radio"

    To boards på **samme gruppe**. I ryster begge, og hver skærm viser 😀 vundet, 😢 tabt eller `=` uafgjort:

    ```makecode
    auto:rps-radio
    ```

??? note "Sådan virker det"

    **Tænk på det som en dommer med en regelbog.**

    - `vælg tilfældig 0 til 2` vælger sten (0), papir (1) eller saks (2), tegnet med `vis lys`.
    - I dysten `sender` du dit kast; når din vens kast *ankommer*, sammenligner et `hvis / ellers hvis` dem (sten slår saks, papir slår sten, saks slår papir) og viser resultatet — samme kast er uafgjort `=`.

    **Vær opmærksom på:** begge spillere **ryster nogenlunde samtidig** og kigger så. Dysten bruger sin **egen gruppe**, så den ikke krydser besked-spillene.

??? example "🚀 Level op — hold point, først til 5"

    Spil en rigtig kamp: dit board **husker dine sejre** og viser din score. Først til **5** vinder kampen! 🏆

    **✊✋✌️ Point-dyst** — flash denne på begge boards, samme gruppe:

    ```makecode
    auto:rps-score
    ```

    *Hvordan: en `myScore`-**variabel** stiger med 1 for hver sejr (`ændr myScore med 1`); ved **5** blinker den `WIN!` og nulstiller. Det nye er at holde point på tværs af runder.*

## 🎃 Halloween 👻

En uhyggelig sæson-godbid, der lærer noget **nyt** — micro:bit'ens skjulte **lyssensor**! 🦇

??? example "🌑 Spøgelse i mørket 🔦 — *lær lyssensoren!*"

    **Noget nyt:** micro:bit'en kan **mærke, hvor lyst eller mørkt der er** — den har en skjult **lyssensor**! Hold den i lyset, og den er rolig 😀, men dæk den til eller sluk lyset, og et **spøgelse dukker op og hyler** 👻. Uhyggeligt!

    ```makecode
    auto:ghost-in-dark
    ```

    *Hvordan: en `for altid`-løkke tjekker **`lysniveau`** (0–255 — LED'erne virker også som en lyssensor). Under **50** (mørkt) → spøgelse + hyl; ellers rolig. Et helt nyt **input** — micro:bit'ens øjne! Træk i lys-skyderen i simulatoren for at teste.*

??? example "🕯️ Spøgelse i mørket — med en rigtig LED 💡"

    Samme idé, nu med en **rigtig LED**, du slutter til: i mørket **flimrer** en ekstern LED som et hjemsøgt stearinlys; i lyset er den slukket. 🕯️👻

    Slut en **LED** til pin **P0** (langt ben) og **GND** (kort ben).

    ```makecode
    auto:ghost-in-dark-led
    ```

    *Hvordan: når `lysniveau` er lavt, tænder/slukker `digital skriv pin P0` LED'en **tilfældigt** (et stearinlys-flimmer); i lyset er den slukket. Nu læser den en sensor **og** styrer et rigtigt kredsløb — en forsmag på LED-ugerne. Ingen LED? Hold øje med **P0**-pinnen i simulatoren.*

## ✅ Jeg er færdig når…

- ☐ Jeg spillede **Rødt lys, grønt lys** uden at blive fanget på rødt. 🚦
- ☐ Jeg vandt en **Sten-Saks-Papir**-dyst over radio. ✊✋✌️
- ☐ *(Legende!)* Jeg byggede **auto-kalderen** eller holdt **point til 5**. 🏆
- ☐ *(Forsker!)* Jeg brugte **lyssensoren** til at få et spøgelse frem i mørket — på skærmen og med en **rigtig LED**. 🌑💡

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-6
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** to spil i hele lokalet over **radio**, der fortsætter fra Uge 4. Begge kræver **2+ boards på samme gruppe** — beslut gruppenumre samlet i klassen. Alle får basis-spillet i gang; de hurtige klatrer op ad level op.

    **Spillene:**

    - **🚦 Rødt lys, grønt lys** — én kalder udsender rødt/grønt; spillere fanges i at bevæge sig på rødt (accelerometer + `game over`). Level op: en **auto-kalder**, der skifter på tilfældige tidspunkter.
    - **✊✋✌️ Sten, Saks, Papir** — et hurtigt solo-kast og så en 2-spiller radio-dyst, der selv dømmer; level op holder **point til 5**.

    **Materialer**

    - micro:bits — **2+ pr. gruppe** + USB (radio kræver rigtige boards; én simulator kan ikke teste det)
    - **V2** til den indbyggede højtaler; V1 virker ellers
    - åbent gulv, især til Rødt lys, grønt lys

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 genopfrisk grupper & radio → 25 **Rødt lys, grønt lys** (knap-kalder, så auto-kalderen) → 25 **SSP** solo → radio-dyst → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 20 klasse-turnering — **SSP først-til-5** + **Rødt lys**-runder → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner i **Blokke**. Spillene her bruger gruppe **2–3**. Næste gang: **LED- & kredsløbs**-projekter — lys, I selv slutter til, på vej mod Ticklebot'en og pinball-elektronikken. 💡
