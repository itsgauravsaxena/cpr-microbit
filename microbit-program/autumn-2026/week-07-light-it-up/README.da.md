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

    Alle programmer tænder en **rigtig LED** — **💡**-mærket viser hvilke(n) pin(s). De fleste skal kun bruge **én LED på P0**; Del 2 bruger **to eller tre** (spørg en hjælper efter flere).

!!! failure "🔧 Min LED lyser ikke — tjek det her i rækkefølge"
    1. **Vend LED'en om.** **Langt ben (+) → S**, **kort ben (−) → G**. Er benene klippet lige lange? Den **flade kant** på LED'ens rand er det korte (−) ben. Omvendt skader ikke — den forbliver bare mørk.
    2. **S og G — aldrig V.** Læs de små bogstaver på boardet: de tre rækker sidder ikke altid i samme rækkefølge. En almindelig LED skal aldrig bruge **V**.
    3. **Sidder micro:bit'en helt og lige i?** Sidder den skævt eller halvt, **virker nogle pins og andre ikke**. Tag den ud og tryk den godt i igen.
    4. **Samme pin i koden og på boardet?** LED i P1, men koden siger P0 = mørk. Brug **P0, P1, P2** — nogle andre pins er optaget inde i micro:bit'en (**P3, P4, P6, P7, P10** styrer skærmen, **P5 / P11** er knap A / B).
    5. **Rok ved ledningen.** Flimrer LED'en, sidder stikket løst — byt ledningen, eller bøj LED-benet en lille smule, så det sidder fast.
    6. **Blå eller hvid LED?** De kan være for svage ved 3 V — prøv en **rød**.
    7. **Har du downloadet** det nyeste program til micro:bit'en?

??? example "🔧 Pin-tester — find den drillende LED på få sekunder · 💡 P0 + P1 + P2"

    Sæt dine LED'er i **P0, P1, P2** og kør programmet. Skærmen viser **0**, **1**, **2** efter tur og tænder LED'en på **den** pin. Vises tallet, men LED'en er mørk? Så er det den, der skal fikses — flyt LED'en til en anden pin for at se, om det er **LED'en** eller **stikket**.

    ```makecode
    auto:pin-test
    ```

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

## 🌈 Del 2 — Flere LED'er

Hent **en eller to LED'er mere** (spørg en hjælper!) og sæt dem i **P1** og **P2** — lange ben til S, korte ben til G, præcis som P0. Samme blokke som i Del 1 — `digital skriv` og `pause` — men nu styrer du et helt lysshow! 🎆

??? example "🚓 Politilys · 💡 P0 + P1"

    **To LED'er** skiftes: én tændt, den anden slukket, byt — *ba-bu!* Blå og røde LED'er ser bedst ud.

    ```makecode
    auto:police
    ```

    *Prøv: gør det hurtigere med `pause 100`, eller blink hver LED **to gange**, før de bytter.*

??? example "🙋 Quiz-buzzer · 💡 P0 + P1"

    To spillere! **A** tænder LED'en på **P0** og viser **A**, **B** tænder LED'en på **P1** og viser **B** — hvem trykker først? ⏱️

    ```makecode
    auto:buzzer
    ```

    *Prøv: spil en forskellig lyd for hver spiller, eller lad vinderens lys være tændt længere.*

??? example "🏃 Løbelys · 💡 P0 + P1 + P2"

    Tre LED'er lyser **én efter én**: P0 → P1 → P2 → igen… som et lys, der løber hen ad en linje.

    ```makecode
    auto:chaser
    ```

    *Prøv: kan du få det til at løbe **tilbage** også (P2 → P1 → P0)? Eller tænde to ad gangen?*

??? example "🚦 Lyskryds · 💡 P0 + P1 + P2"

    Brug **rød → P0**, **gul → P1**, **grøn → P2** til et rigtigt dansk lyskryds: rød → rød + gul → grøn → gul → rød igen… præcis som ved vejkrydset.

    ```makecode
    auto:traffic-light
    ```

    *Hvordan: det er bare `digital skriv` og `pause` i den rigtige rækkefølge. Prøv at tilføje en **fodgængerknap**: tryk A for at skifte til rødt før tid!*

??? example "✨ Funkel · 💡 P0 + P1 + P2"

    Tre LED'er tænder og slukker **tilfældigt** — som en lyskæde. ✨

    ```makecode
    auto:led-twinkle
    ```

    *Hvordan: `vælg tilfældig 0 til 1` giver hver pin enten **0** (slukket) eller **1** (tændt) hvert 150. ms. Skift pausen for roligere eller vildere funkel.*

??? example "🚀 Raketopsendelse · 💡 P0 + P1 + P2"

    Tryk **A** for en nedtælling: **3** 💡 … **2** 💡💡 … **1** 💡💡💡 … **AFFYRING!** Alle lysene blinker, og raketten drøner af sted med lyd. 🚀

    ```makecode
    auto:rocket
    ```

    *Hvordan: én LED tænder for hvert tal, og så blinker en `gentag 4 gange`-løkke med alle tre. Prøv en nedtælling fra **5** — hvor skulle de ekstra LED'er sidde?*

## ✨ Del 3 — Kraftigt og svagt

`digital skriv` kan kun **tænde (1)** eller **slukke (0)**. `analog skriv pin` kan alt **midt imellem**: **0** = slukket, **1023** = fuld styrke. Nu kan din LED gløde blødt! 🌗

??? example "🌙 LED, der trækker vejret · 💡 P0"

    LED'en **fader langsomt op** og **ned igen** — som om den trækker vejret.

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

## 🧠 Del 4 — Et lys, der kan huske

Indtil nu glemmer micro:bit'en alt mellem hvert tryk. Nu skal den **huske** — og vælge med `hvis / ellers`, præcis som spøgelset gør bagefter.

### 🔦 Lommelygte med én knap · 💡 P0

Kun **én** knap denne gang: tryk **A** én gang → tændt, tryk igen → slukket. micro:bit'en skal **huske**, om lyset er tændt.

??? example "👀 Se programmet"

    ```makecode
    auto:led-toggle
    ```

    *Hvordan: variablen `on` er **sand** eller **falsk**. `sæt on til ikke on` vender den ved hvert tryk, og `hvis` vælger tændt eller slukket. En lyskontakt, der kan huske!*

## 🎃 Halloween 👻

En uhyggelig sæson-godbid, der lærer noget **nyt** — micro:bit'ens skjulte **lyssensor**! 🦇

??? example "🕯️ Spøgelse i mørket · 💡 P0 — *lær lyssensoren!*"

    **Noget nyt:** micro:bit'en kan **mærke, hvor lyst eller mørkt der er** — skærmens LED'er virker også som en skjult **lyssensor**! I lyset er den rolig 😀, og din LED er slukket. Dæk den til eller sluk lyset, så **dukker et spøgelse op** 👻, mens din LED **flimrer** som et hjemsøgt stearinlys 🕯️. Uhyggeligt!

    Behold din LED på pin **P0** fra Del 1.

    ```makecode
    auto:ghost-in-dark-led
    ```

    *Hvordan: en `for altid`-løkke tjekker **`lysniveau`** (0–255). Under **50** (mørkt) → spøgelse, og `digital skriv pin P0` tænder/slukker LED'en **tilfældigt** (stearinlys-flimmeret); ellers rolig og slukket. Den læser en sensor **og** styrer et rigtigt kredsløb! Træk i lys-skyderen i simulatoren for at teste.*

## 🚀 Level op — berøringskontakter

Pins kan også være **input**! Når du rører en pin (mens du holder om **GND**), lukker du et kredsløb — en hjemmelavet **kontakt**. Sådan kommer **Ticklebot'en** og pinball-målene til at virke. Behold din LED på **P0** — rør ved **P1** *(tag først en eventuel LED af P1)*.

??? example "🔔 Dørklokke-lys · 💡 P0"

    Rør **P1** (og hold om **GND** med den anden hånd) → din LED lyser et halvt sekund + et ding. Input på én pin, output på en anden!

    ```makecode
    auto:led-touch
    ```

??? example "🤖 Kildetæller · 💡 P0"

    Hver berøring på **P1** giver et point: LED'en blinker, en melodi spiller, og pointene vises — en første smagsprøve på Ticklebot'en! 😆

    ```makecode
    auto:tickle
    ```

    *Hvordan: en `score`-**variabel** stiger med 1 ved hvert `når pin P1 trykkes`, og LED'en lyser, mens pointene vises. Prøv at forbinde sølvpapir eller et krokodillenæb til P1 for at lave en større "kildeplade".*

## ✅ Jeg er færdig når…

- ☐ Jeg sluttede en **LED** til og **tændte og slukkede** den med knapper. 💡
- ☐ Jeg fik min LED til at **blinke** og ændrede farten. 🔁
- ☐ Jeg forbandt **to eller tre LED'er** og lavede et lysshow (politilys, løbelys, lyskryds eller raket). 🌈
- ☐ Jeg fik min LED til at **gløde blødt** med `analog skriv` (vejrtrækning eller lysdæmper). 🌙
- ☐ Jeg byggede en **lommelygte med én knap**, der husker, om den er tændt. 🔦
- ☐ *(Forsker!)* Jeg brugte **lyssensoren** til at få min LED til at flimre i mørket. 🌑👻
- ☐ *(Legende!)* Jeg byggede **dørklokke-lyset** eller **kildetælleren**. 🤖

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
    - til Del 2: **2 ekstra LED'er** pr. barn — helst **rød, gul og grøn** (lyskryds) og en **blå** (politilys)
    - **ingen pærer** — lommelygte-/glødepærer trækker for meget strøm til en micro:bit-pin
    - en måde at **mørklægge lokalet** på (eller hænder/papir til at dække boardet) til spøgelset
    - **V2** til den indbyggede højtaler; V1 virker ellers

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 mød LED'en (langt ben +, kort ben −) → 15 **forbind + tænd/sluk** → 5 **blink** → 15 🌈 **flere LED'er** (politilys → buzzer → løbelys → lyskryds → funkel → raket; hvert barn vælger 2–3) → 10 **vejrtræknings-LED → lysdæmper** → 5 🔦 **lommelygte** (variabel + `hvis / ellers`, opvarmning til spøgelset) → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 10 🕯️ **Spøgelse i mørket** + spøgelsesjagt med slukket lys 👻 → 10 level op **dørklokke-lys → kildetæller** → 5 fremvisning (🚀 raketopsendelser!) → 5 Kahoot.

    **Noter:** hver indlejring åbner i **Blokke**. Ved "min LED virker ikke": gå **🔧-tjeklisten** øverst på siden igennem, og kør **pin-testeren** — de fleste tilfælde er en LED, der sidder **omvendt**, sidder i **V i stedet for G**, en micro:bit, der **ikke er trykket helt ned i shieldet** (præcis "nogle pins virker, andre ikke"), eller den **forkerte pin**. På en **V2** kommer lyden som standard også ud af **P0**, så en LED på P0 summer eller blinker på mærkelige tidspunkter — derfor starter programmerne med lyd (buzzer, raket, dørklokke, kildetæller) med blokken `set audio pin enabled false` (slår lyd-pinnen fra); lyden spiller stadig i den indbyggede højttaler (på en V1 er de lydløse). En svag blå/hvid LED er ikke i stykker — byt den til en rød. `analog skriv` tager **0–1023** (ikke 0–255 som skærmens lysstyrke). Del 2 sætter LED'er på **P1** og **P2**; berøringsprogrammerne bruger **P1** som input — mind børnene om at tage LED'en af P1 først. Den allerførste `lysniveau`-måling kan være skæv, mens sensoren vågner — giv den et sekund. Berøringspins kræver, at barnet også rører **GND** for at lukke kredsløbet. Spøgelsesprogrammet er flyttet hertil fra Uge 6, så det lander i **Halloween-ugen**. 🎃
