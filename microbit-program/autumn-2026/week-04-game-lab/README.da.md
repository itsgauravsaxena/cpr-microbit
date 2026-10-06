# Uge 4 — Spil-lab 📡

> Nu **taler micro:bit'ene sammen**! Byg en **fjernbetjening** 🎮 og en **Varmt eller koldt**-skattejagt 💎 — alt sammen gennem luften. 📡

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

## ✅ Jeg er færdig når…

- ☐ Jeg byggede en **fjernbetjening** — en sender og en modtager. 🎮
- ☐ Jeg spillede **Varmt eller koldt** og fandt den gemte skat. 💎
- ☐ *(Legende!)* Jeg byggede den **fjernstyrede prik** — vip for at styre. 🎮

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-4
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** **radio- & multiplayer**-sessionen — hvert spil kræver **2+ boards på samme gruppe**. Det er semesterets højdepunkt: børnenes boards *taler sammen*. Medbring rigeligt med par-boards, og beslut gruppenumre samlet i klassen, så par ikke støder sammen. Der er med vilje **mere her end der kan nås på én session**. 🎯

    **Spillene (nemt → svært):**

    - **📡 Sender & modtager** — *roller*: ét board sender, ét lytter. Indeholder **🔥 Varmt eller koldt** (signalstyrke — skattejagten i lokalet) og en **fjernstyret prik** (vip for at styre).

    (**🚦 Rødt lys, grønt lys** og **✊✋✌️ Sten-Saks-Papir** har nu deres egen session — se **[Uge 6 — Holdspil](../week-06-team-games/README.md)**.)

    **Materialer**

    - micro:bits — **mindst 2 pr. par/gruppe** + USB (radio kræver rigtige boards; én simulator kan ikke teste det)
    - **V2**-boards giver en indbygget højtaler til besked-"bippet"; V1 virker ellers
    - plads til at bevæge sig til **Varmt eller koldt**

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 10 hvordan radio & grupper virker → 25 byg **Sender & modtager**-fjernbetjeningen (samme gruppe) → 20 **Varmt eller koldt**-skattejagt → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 20 **Varmt eller koldt**-skattejagt + **fjernstyret prik**-level op → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner direkte i **Blokke**. Radio-spil bruger **gruppenumre** — beslut dem samlet i klassen, så par ikke støder sammen (spillene her bruger gruppe 1–3). Spil, der læser **signalstyrke** eller kræver plads (**Varmt eller koldt**, **Rødt lys**), vil helst have **rigtige boards**. Næste gang: **[Uge 5 — Varmt eller koldt](../week-05-hot-or-cold/README.md)** går i dybden med skattejagten, så **[Uge 6 — Holdspil](../week-06-team-games/README.md)** (Rødt lys, SSP), og senere **LED- & kredsløbs**-projekter mod Ticklebot'en & pinball. 💡
