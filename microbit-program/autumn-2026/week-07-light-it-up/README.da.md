# Uge 7 — Tænd lyset 💡🎃

> Vores første **rigtige kredsløb**! Slut en LED til og få den til at tænde, blinke og flimre — og brug så micro:bit'ens skjulte **lyssensor** til et uhyggeligt **Halloween**-spøgelse, der kun kommer frem i mørket. 👻

!!! abstract "🎓 Hvad I lærer i dag"
    - **output** — `digital skriv pin` tænder en rigtig LED (**1**) og slukker den (**0**)
    - **at forbinde** — en LED har et **langt ben (+)** og et **kort ben (−)**
    - **lyssensoren** — et helt nyt **input** (`lysniveau`, 0–255)
    - **input → output** — læs en sensor, og styr så et kredsløb

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="et flimrende spøgelse på LED-skærmen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="17" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="17" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="51" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="85" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="119" width="26" height="26" rx="6" fill="#2b3038"/><rect x="17" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="51" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="85" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="119" y="153" width="26" height="26" rx="6" fill="#2b3038"/><rect x="153" y="153" width="26" height="26" rx="6" fill="#2b3038"/><g fill="#ff8c1a"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0;0.15;0.25;0.4;0.55;0.6" values="1;0.25;1;0.5;1;0.2"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

!!! tip "Sådan slutter du en LED til 🔌"
    Sæt micro:bit'en i **[sensor-shieldet](../gear/README.md)** og forbind en **LED** til pin **P0**: **langt ben → S (signal)**, **kort ben → G (jord)**. Intet shield? Brug krokodillenæb på **P0** og **GND**. Forbliver LED'en mørk? Vend den om — LED'er virker kun den ene vej! 🔄

!!! warning "Hvilke lys kan jeg bruge? 💡"
    - ✅ **LED-moduler** (små boards med S / V / G) — nemmest: sæt dem direkte i shieldet, modstanden er indbygget.
    - ✅ **Løse LED'er** — røde, gule og grønne lyser kraftigst. Blå og hvide kan være svage (pinsene giver kun ca. 3 V). En **modstand på 100–220 Ω** i serie skåner pinnen.
    - ❌ **Pærer** (lommelygte-/glødepærer) — de skal bruge langt mere strøm, end en pin kan give. De lyser ikke og kan skade micro:bit'en.

    Alle programmer mærket **💡 P0** tænder din rigtige LED. **🖥️ skærm**-programmer bruger de indbyggede lys og kræver ingen ledninger.

## 💡 Del 1 — Din første LED

### Tænd og sluk · 💡 P0

Tryk **A** for at **tænde** LED'en og **B** for at **slukke** den. Du styrer et rigtigt lys med kode!

*🎓 Begreb: **output** — `digital skriv pin P0 til 1` = tændt, `0` = slukket.*

??? example "👀 Se programmet"

    ```makecode
    auto:ledon
    ```

### Få den til at blinke · 💡 P0

Ingen knapper denne gang — en `for altid`-løkke tænder LED'en, venter, slukker den, venter… for altid. 🔁

??? example "👀 Se programmet"

    ```makecode
    auto:blink
    ```

    *Prøv: skift `500` til `100` for et hurtigt blink eller `1000` for et langsomt. Kan du lave et **SOS** (kort-kort-kort, lang-lang-lang)?*

### 🔦 Lommelygte med én knap · 💡 P0

Kun **én** knap denne gang: tryk **A** én gang → tændt, tryk igen → slukket. micro:bit'en skal **huske**, om lyset er tændt.

??? example "👀 Se programmet"

    ```makecode
    auto:led-toggle
    ```

    *Hvordan: variablen `on` er **sand** eller **falsk**. `sæt on til ikke on` vender den ved hvert tryk, og `hvis` vælger tændt eller slukket. En lyskontakt, der kan huske!*

## ✨ Del 2 — Kraftigt og svagt

`digital skriv` kan kun **tænde (1)** eller **slukke (0)**. `analog skriv pin` kan alt **midt imellem**: **0** = slukket, **1023** = fuld styrke. Nu kan din LED gløde blødt! 🌗

??? example "🌙 LED, der trækker vejret · 💡 P0"

    Den rigtige LED **fader langsomt op** og **ned igen** — som om den trækker vejret.

    ```makecode
    auto:led-fade
    ```

    *Hvordan: en `for`-løkke tæller 0 → 20 og skriver `index × 50` (0 → 1000); en anden løkke tæller ned igen. Skift `pause 40` for at få den til at trække vejret hurtigere eller langsommere.*

??? example "🎚️ Lysdæmper · 💡 P0"

    **B** = kraftigere, **A** = svagere. Skærmen viser niveauet **0–10**.

    ```makecode
    auto:led-dimmer
    ```

    *Hvordan: variablen `level` går fra 0 til 10, og `analog skriv pin P0` får `level × 100`. `min` / `maks` sørger for, at den ikke kommer over 10 eller under 0.*

### 🖥️ På skærmen

De 25 lys på forsiden er også LED'er! To tricks til den indbyggede skærm — ingen ledninger:

??? example "💗 Fade — et hjerte, der trækker vejret · 🖥️ skærm"

    `sæt lysstyrke` går fra **0** (slukket) til **255** (fuld). Når der skiftes mellem kraftigt og svagt, pulserer hjertet.

    ```makecode
    auto:fade
    ```

??? example "✨ Funkel — tilfældige glimt · 🖥️ skærm"

    `tegn` tænder én LED på et tilfældigt **x, y**-sted, `slet` slukker en anden — som en stjernehimmel.

    ```makecode
    auto:sparkle
    ```

## 🎃 Halloween 👻

En uhyggelig sæson-godbid, der lærer noget **nyt** — micro:bit'ens skjulte **lyssensor**! 🦇

??? example "🌑 Spøgelse i mørket 🔦 — *lær lyssensoren!* · 🖥️ skærm"

    **Noget nyt:** micro:bit'en kan **mærke, hvor lyst eller mørkt der er** — den har en skjult **lyssensor**! Hold den i lyset, og den er rolig 😀, men dæk den til eller sluk lyset, og et **spøgelse dukker op og hyler** 👻. Uhyggeligt!

    ```makecode
    auto:ghost-in-dark
    ```

    *Hvordan: en `for altid`-løkke tjekker **`lysniveau`** (0–255 — LED'erne virker også som en lyssensor). Under **50** (mørkt) → spøgelse + hyl; ellers rolig. Et helt nyt **input** — micro:bit'ens øjne! Træk i lys-skyderen i simulatoren for at teste.*

??? example "🕯️ Spøgelse i mørket — med en rigtig LED · 💡 P0"

    Samme idé, nu med **LED'en, du har sluttet til**: i mørket **flimrer** den som et hjemsøgt stearinlys; i lyset er den slukket. 🕯️👻

    Behold din LED på pin **P0** fra Del 1.

    ```makecode
    auto:ghost-in-dark-led
    ```

    *Hvordan: når `lysniveau` er lavt, tænder/slukker `digital skriv pin P0` LED'en **tilfældigt** (et stearinlys-flimmer); i lyset er den slukket. Nu læser den en sensor **og** styrer et rigtigt kredsløb. Ingen LED? Hold øje med **P0**-pinnen i simulatoren.*

## 🚀 Level op — berøringskontakter

Pins kan også være **input**! Når du rører en pin (mens du holder om **GND**), lukker du et kredsløb — en hjemmelavet **kontakt**. Sådan kommer **Ticklebot'en** og pinball-målene til at virke.

??? example "👆 Berøringskontakt"

    Rør **P1** (og hold om **GND** med den anden hånd) → ✓ og et bip.

    ```makecode
    auto:switch
    ```

??? example "🔔 Dørklokke-lys · 💡 P0"

    Samme berøringskontakt, men nu blinker din **LED** også: rør **P1** → LED'en på **P0** lyser et halvt sekund + et ding. Input på én pin, output på en anden!

    ```makecode
    auto:led-touch
    ```

??? example "🤖 Kildetæller"

    Hver berøring på **P1** giver et point, spiller en melodi og viser pointene — en første smagsprøve på Ticklebot'en! 😆

    ```makecode
    auto:tickle
    ```

    *Hvordan: en `score`-**variabel** stiger med 1 ved hvert `når pin P1 trykkes`. Prøv at forbinde sølvpapir eller et krokodillenæb til P1 for at lave en større "kildeplade".*

## 🚦 Superlevel — lyskryds

Har du **tre LED'er**? Byg et rigtigt dansk lyskryds! **Rød → P0**, **gul → P1**, **grøn → P2** (lange ben til S, korte ben til G).

??? example "🚦 Lyskryds · 💡 P0 + P1 + P2"

    Rød → rød + gul → grøn → gul → rød igen… præcis som ved vejkrydset.

    ```makecode
    auto:traffic-light
    ```

    *Hvordan: det er bare `digital skriv` og `pause` i den rigtige rækkefølge. Prøv at tilføje en **fodgængerknap**: tryk A for at skifte til rødt før tid!*

## ✅ Jeg er færdig når…

- ☐ Jeg sluttede en **LED** til og **tændte og slukkede** den med knapper. 💡
- ☐ Jeg fik min LED til at **blinke** og ændrede farten. 🔁
- ☐ Jeg fik min LED til at **gløde blødt** med `analog skriv` (vejrtrækning eller lysdæmper). 🌙
- ☐ *(Forsker!)* Jeg brugte **lyssensoren** til at få et spøgelse frem i mørket — på skærmen og med min **rigtige LED**. 🌑👻
- ☐ *(Legende!)* Jeg byggede en **berøringskontakt**, **dørklokke-lyset** eller **kildetælleren**. 🤖
- ☐ *(Superlegende!)* Jeg forbandt **tre LED'er** til et **lyskryds**. 🚦

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-7
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** alle slutter **én LED** til og styrer den fra kode, og kombinerer så et **input** (lyssensoren) med det **output** til Halloween-spøgelset. De hurtige går videre til **berøringskontakter** (på vej mod Ticklebot'en / pinball).

    **Materialer**

    - micro:bits + USB + **sensor-shields** — **1 pr. barn** (denne uge virker solo)
    - **LED'er** (1–2 hver, plus nogle ekstra; LED-moduler er nemmest) + ledninger / krokodillenæb
    - til lyskrydset: **røde, gule og grønne** LED'er (3 pr. barn, der når så langt)
    - **ingen pærer** — lommelygte-/glødepærer trækker for meget strøm til en micro:bit-pin
    - en måde at **mørklægge lokalet** på (eller hænder/papir til at dække boardet) til spøgelset
    - **V2** til den indbyggede højtaler; V1 virker ellers

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 mød LED'en (langt ben +, kort ben −) → 15 **forbind + tænd/sluk** → 10 **blink / lommelygte** → 10 **vejrtræknings-LED / lysdæmper** (skærm-fade / funkel til dem uden LED) → 15 🌑 **Spøgelse i mørket** (skærm) → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 10 🕯️ **spøgelse med den rigtige LED** → spøgelsesjagt med slukket lys 👻 → 10 level op **berøringskontakt / dørklokke-lys / kildetæller** (🚦 lyskryds til de hurtige) → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner i **Blokke**. De fleste "min LED virker ikke"-problemer skyldes en LED, der sidder **omvendt** eller på den **forkerte pin** — tjek P0 og vend den. En svag blå/hvid LED er ikke i stykker — byt den til en rød. `analog skriv` tager **0–1023** (ikke 0–255 som skærmens lysstyrke). Dørklokke-lyset bruger **P1** til berøring, så lyskrydset (som skal bruge P1 til gul) er et separat program. Den allerførste `lysniveau`-måling kan være skæv, mens sensoren vågner — giv den et sekund. Berøringspins kræver, at barnet også rører **GND** for at lukke kredsløbet. Spøgelsesprogrammerne er flyttet hertil fra Uge 6, så de lander i **Halloween-ugen**. 🎃
