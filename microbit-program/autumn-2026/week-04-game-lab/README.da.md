# Uge 4 — Spil-lab 📡

> Nu **taler micro:bit'ene sammen**! Byg en fjernbetjening 🎮 og spil **Varmt eller koldt**, **Rødt lys grønt lys** og **Sten-Saks-Papir** — alt sammen gennem luften. 📡

!!! abstract "🎓 Hvad I lærer i dag"
    - **radio** — send, modtag og del en **gruppe** (kanal)
    - **roller** — en **sender** og en **modtager**
    - **signalstyrke** — hvordan radio bliver svagere med afstand
    - **accelerometeret** — at fange bevægelse

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="et hjerte der banker på LED-skærmen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" dur="1.4s" repeatCount="indefinite" values="1;0.3;1" keyTimes="0;0.5;1"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

## 🎮 Vælg et spil

Alle spil her bruger **to eller flere micro:bits**, der taler over **radio**. Læg et program på hvert board, og spil! Ny her? Den tidligere **[Spil-lab](../microbit-beginners/week-03-game-lab-2/README.md)** har on-board-spillene. 🌱

### 📡 Sender & modtager

Indtil nu laver begge boards det **samme** job. Giv dem nu **forskellige** job: det ene board er **senderen** (fjernbetjeningen) og det andet er **modtageren** (legetøjet). Læg et forskelligt program på hvert! 🎮

*🎓 Begreb: **roller** — en sender og en lytter, som en fjernbetjening og et fjernsyn.*

!!! tip "To micro:bits, to *forskellige* programmer"
    Læg **`TX`** (sender) på det ene board og **`RX`** (modtager) på det andet — begge på **samme gruppe**. Fjernbetjenings-boardets knapper styrer nu det andet boards skærm!

??? example "👀 Se de to programmer"

    **📤 Sender (fjernbetjeningen)** — tryk A/B eller ryst for at sende en kommando:

    ```makecode
    auto:tx
    ```

    **📥 Modtager (legetøjet)** — reagerer på det, fjernbetjeningen sender:

    ```makecode
    auto:rx
    ```

??? example "🔥 Varmt eller koldt — radio-skattejagt"

    En klassiker! Det ene board er en gemt **skat**, der bliver ved med at bippe et signal ud; det andet er en **detektor**, hvis ansigt bliver gladere, jo tættere du er. Gem skatten, og find den så! 💎

    **💎 Skat (sender)** — gem denne et sted i lokalet:

    ```makecode
    auto:beacon
    ```

    **🔍 Detektor (modtager)** — gå rundt: 😢 koldt → 😕 → 😀 → 💗 rygende varmt!

    ```makecode
    auto:detector
    ```

??? note "Sådan virker det"

    **Tænk på det som en fjernbetjening — og en leg om tampen brænder.**

    - **Fjernbetjening** — **senderen** *sender* kun (knap/ryst → `radio send nummer`); **modtageren** *lytter* kun (*når radio modtager* → viser en pil eller et ansigt). At dele de to job op er det, der gør det til en rigtig fjernbetjening.
    - **Skattejagt** — skatten `sender` et signal igen og igen i en `for altid`-løkke. Detektoren læser, hvor **stærkt** signalet er (`modtaget pakke signalstyrke`): et stærkt signal betyder, at du er tæt på, så den viser et gladere ansigt. Radio bliver svagere med afstand — det er det, der gør det "varmt/koldt."

    **Vær opmærksom på:** to **forskellige** programmer, begge på **samme gruppe**. Skattejagten kræver rigtige **boards** og plads til at bevæge sig — signalstyrken ændrer sig næsten ikke i simulatoren.

??? example "🚀 Level op — fjernstyret prik"

    Lav fjernbetjeningen om til en rigtig controller: **vip** senderen, og en prik glider hen over modtagerens skærm. 🎮

    **📤 Sender (vip den)** — sender, hvor meget den vippes, igen og igen:

    ```makecode
    auto:tx-tilt
    ```

    **📥 Modtager (skærmen)** — en prik bevæger sig til venstre/højre efter vippet:

    ```makecode
    auto:rx-move
    ```

    *Hvordan: senderen `sender` sin **acceleration (X)** i en `for altid`-løkke; modtageren **omregner** (map) tallet til en prik-position (0–4) og flytter en **sprite**. Live sensordata over radio!*

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

## ✅ Jeg er færdig når…

- ☐ Jeg byggede en **fjernbetjening** — en sender og en modtager. 🎮
- ☐ Jeg spillede **Varmt eller koldt** og fandt den gemte skat. 💎
- ☐ *(Legende!)* Jeg vandt **Rødt lys grønt lys** eller en **SSP**-dyst. 🏆

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-4
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** **radio- & multiplayer**-sessionen — hvert spil kræver **2+ boards på samme gruppe**. Det er semesterets højdepunkt: børnenes boards *taler sammen*. Medbring rigeligt med par-boards, og beslut gruppenumre samlet i klassen, så par ikke støder sammen. Der er med vilje **mere her end der kan nås på én session**. 🎯

    **Spillene (nemt → svært):**

    - **📡 Sender & modtager** — *roller*: ét board sender, ét lytter. Indeholder **🔥 Varmt eller koldt** (signalstyrke — skattejagten i lokalet).
    - **🚦 Rødt lys, grønt lys** — én kalder udsender rødt/grønt; spillere fanges i at bevæge sig på rødt (accelerometer + `game over`).
    - **✊✋✌️ Sten, Saks, Papir** — et hurtigt solo-kast og så en 2-spiller radio-dyst, der selv dømmer.

    **Materialer**

    - micro:bits — **mindst 2 pr. par/gruppe** + USB (radio kræver rigtige boards; én simulator kan ikke teste det)
    - **V2**-boards giver en indbygget højtaler til besked-"bippet"; V1 virker ellers
    - plads til at bevæge sig til **Varmt eller koldt** og **Rødt lys, grønt lys**

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 10 hvordan radio & grupper virker → 25 byg **Sender & modtager**-fjernbetjeningen (samme gruppe) → 20 **Varmt eller koldt**-skattejagt → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 20 spil i hele lokalet — **Varmt eller koldt**, **Rødt lys grønt lys**, **SSP-dyst** → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner direkte i **Blokke**. Radio-spil bruger **gruppenumre** — beslut dem samlet i klassen, så par ikke støder sammen (spillene her bruger gruppe 1–3). Spil, der læser **signalstyrke** eller kræver plads (**Varmt eller koldt**, **Rødt lys**), vil helst have **rigtige boards**. Næste gang: **[Uge 5 — Varmt eller koldt](../week-05-hot-or-cold/README.md)** går i dybden med skattejagten (en klogere detektor), så **LED- & kredsløbs**-projekter — lys, I selv slutter til, på vej mod Ticklebot'en og pinball-elektronikken. 💡
