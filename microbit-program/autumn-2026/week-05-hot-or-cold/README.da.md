# Uge 5 — Varmt eller koldt 🔥❄️

> Tilbage til skattejagten! Sidste uge viste detektoren **ansigter**. I denne uge gør vi den **klogere** — en bjælkemåler, bip der speeder op, "varmere/koldere" og en **du fandt den!**-fejring. 💎

!!! abstract "🎓 Hvad I lærer i dag"
    - **signalstyrke** — radio bliver svagere med afstand
    - **`for altid`**-løkker + **variabler** til at huske den seneste måling
    - at **sammenligne** tal (`>` / `<`) og lidt **tilstand** (varmere vs koldere)
    - at vise data med en **bjælkegraf** og **lyd**

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="et radiosignal der breder sig udad" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ffd23f"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

!!! tip "I skal bruge **to** micro:bits + plads til at bevæge jer"
    Det ene board er den gemte **skat** (`BEACON`), det andet er **detektoren**. Begge på **samme gruppe**. Gem skatten, og gå så på jagt! Ny til det? Det startede i **[Uge 4 — Spil-lab](../week-04-game-lab/README.md)**. 🎮

## 💎 Skattejagten (genopfriskning)

**Skatten** bipper et radiosignal ud; **detektoren** viser med et ansigt, hvor tæt du er. 😢 langt væk → 💗 rygende varmt.

*🎓 Begreb: **signalstyrke** — et stærkt signal betyder, at skatten er tæt på.*

??? example "👀 Se de to programmer"

    **💎 Skat (sender)** — gem denne:

    ```makecode
    auto:beacon
    ```

    **🔍 Detektor (ansigter)** — 😢 koldt → 😕 → 😀 → 💗 rygende varmt:

    ```makecode
    auto:detector
    ```

## 🔬 Gør detektoren klogere

Behold **samme skat** (`BEACON`) — flash bare **detektoren** igen med hver ny idé. Byg så langt du kan! 🌱

??? example "① Signal-bjælkemåler 📊"

    Byt ansigter ud med en **bjælke**, der fyldes op, jo tættere du kommer — mere præcis end ansigter.

    ```makecode
    auto:detector-bar
    ```

    *Hvordan: en `for altid`-løkke **omregner** (map) signalstyrken til `0–100` og tegner den med `vis bjælkegraf`. Fuld bjælke = lige oven på den!*

??? example "② Bip der speeder op 🔊"

    Som en rigtig metaldetektor: langsomme bip langt væk, **hektiske** bip når du er tæt på.

    ```makecode
    auto:detector-beep
    ```

    *Hvordan: den gemmer den seneste styrke i en **variabel**, og så spiller en `for altid`-løkke et bip og **`venter`** en tid omregnet fra signalet — tættere = kortere pause = hurtigere bip.*

??? example "③ Varmere eller koldere? ↕️"

    Detektoren **husker** den sidste måling og fortæller, om du bliver **varmere** ⬆️ eller **koldere** ⬇️.

    ```makecode
    auto:detector-warmer
    ```

    *Hvordan: den holder en `last`-variabel. Hver gang sammenlignes den nye styrke med `last`: større → ⬆️ varmere, mindre → ⬇️ koldere. At huske den forrige værdi hedder **tilstand**.*

??? example "④ Du fandt den! 🏆"

    En rigtig sejr: mens du søger, viser den en bjælke, og når du er **lige oven på den**, blinker den ✓ og spiller en sejrsmelodi.

    ```makecode
    auto:detector-found
    ```

    *Hvordan: et `hvis / ellers` — er signalet meget stærkt (`> -48`), så fejr 🎉, ellers bliv ved med at vise søge-bjælken.*

??? example "⑤ Varme-tal 🔢"

    Vis et **tal fra 0 til 100** — præcis hvor varm du er.

    ```makecode
    auto:detector-number
    ```

    *Hvordan: den **omregner** (map) signalet til `0–100` og **runder** det til et helt tal, og så `vis tal`.*

??? example "⑥ Lys op 🔆"

    Hele hjertet **lyser kraftigere**, jo tættere du kommer — svagt langt væk, blændende oven på.

    ```makecode
    auto:detector-glow
    ```

    *Hvordan: `sæt lysstyrke` får det omregnede signal (`5–255`), så LED'erne bliver lysere ved et stærkere signal.*

??? example "⑦ Stigende tone — theremin 🎼"

    I stedet for bip: en **tone, der glider højere op**, jo tættere du kommer — som en musikalsk skattedetektor.

    ```makecode
    auto:detector-pitch
    ```

    *Hvordan: `spil tone` får en **frekvens** omregnet fra signalet (`200 Hz` langt væk → `900 Hz` tæt på), så tonehøjden stiger, når du nærmer dig.*

??? example "⑧ Kap med uret ⏱️"

    Tryk på **A** for at starte uret, gå på jagt, og når du når skatten, viser den **hvor mange sekunder** det tog. Kap med dine venner!

    ```makecode
    auto:detector-race
    ```

    *Hvordan: **A** gemmer starttiden (`kørselstid`); en `for altid`-løkke venter på et stærkt signal og viser så `(nu − start) ÷ 1000` sekunder med en sejrsmelodi. Bruger **tilstand** til at huske, at den er startet.*

??? example "⑨ Tænd en rigtig LED 💡"

    Slut en rigtig **LED** til pin **P0** (langt ben) og **GND** (kort ben): den lyser **kraftigere**, jo tættere du kommer — en skattelampe, du selv har bygget! *(En første smagsprøve på Uge 6's kredsløb.)*

    ```makecode
    auto:detector-led
    ```

    *Hvordan: `analog skriv pin P0` sender en lysstyrke (`0–1023`) omregnet fra signalet, så en rigtig LED på P0 dæmpes og lyser op som skærmen. Ingen LED endnu? Hold øje med **P0**-pinnen i simulatoren.*

??? note "Sådan virker signalstyrke"

    **Tænk på det som et råb over en mark.** Lige ved siden af nogen er det **højt**; langt væk er det **svagt**. Radio er det samme: `modtaget pakke signalstyrke` er et tal, der er **større (tættere på 0), når man er tæt på** — omkring `-42` oven på skatten, ned til `-95`+ langt væk. Alle variationerne ovenfor gør bare det ene tal til noget, man kan se eller høre.

    **Vær opmærksom på:** signalstyrken ændrer sig næsten ikke i **simulatoren** — det her skinner på **rigtige boards** med plads til at gå rundt. Alle detektorer bruger **samme gruppe** som skatten.

## ✅ Jeg er færdig når…

- ☐ Jeg fandt den gemte skat med **ansigt**-detektoren. 💗
- ☐ Jeg opgraderede den til en **bjælkemåler** eller **bip**. 📊🔊
- ☐ *(Legende!)* Jeg byggede **tre eller flere** detektorer — varmere/koldere, fandt-den, lys-op, theremin, kap-med-uret eller tændte en **rigtig LED**. 🏆💡

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-5
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** gå i dybden med **ét** spil — radio-skattejagten — så børnene møder **signalstyrke**, `for altid`-løkker, variabler og simpel **tilstand** uden et helt nyt emne. Skat-programmet (`BEACON`) ændrer sig aldrig; børnene flasher bare **detektoren** igen med hver klogere version. Godt til blandede niveauer: alle får ansigt-versionen til at spille, og de hurtige klatrer op ad stigen.

    **Stigen (nemt → svært):**

    - **Genopfriskning** — ansigt-detektor (😢→💗). Alle får den i gang først.
    - **① Bjælkemåler** — `vis bjælkegraf` af det omregnede signal. En renere aflæsning.
    - **② Bip speeder op** — lyd-feedback; en variabel holder det seneste signal, så bip-takten er jævn (ikke bundet til pakke-timingen).
    - **③ Varmere/koldere** — introducerer **tilstand** (en `last`-variabel, der sammenlignes med den nye måling).
    - **④ Fandt den!** — en `hvis / ellers`-sejrsbetingelse + en fejringsmelodi.

    **Materialer**

    - **≥2 micro:bits** pr. gruppe + USB (radio + signalstyrke kræver **rigtige boards** — simulatorens signal bevæger sig næsten ikke)
    - **V2** giver en indbygget højtaler til ② og ④; på V1 brug en buzzer på pin 0
    - åbent gulv og gemmesteder til skatten

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 10 genopfrisk hvordan radio & signalstyrke virker → 20 få **ansigt-skattejagten** i gang (gemme & lede) → 25 byg **① bjælkemåler** og **② bip** → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 20 **③ varmere/koldere** og **④ fandt-den!** for de hurtige, plus en klasse-turnering i skattejagt → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner i **Blokke**. `modtaget pakke signalstyrke` ligger ≈ `-42` (rører) til `-128` (langt væk); variationerne `omregner` (map) det til en bjælke, en bip-forsinkelse eller en pil. Næste gang: **LED'er & kredsløb** (Uge 6) — lys, I selv slutter til, på vej mod Ticklebot'en og pinball-elektronikken. 💡
