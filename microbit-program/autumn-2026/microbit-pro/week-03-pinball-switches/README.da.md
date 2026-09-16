# Uge 3 — Pinball-kontakter ⚡ (del 2)

> Del 2 af pinball-bygget. Sidste uge var jeres mål de 3 touch-pins — i denne uge **slutter og læser I jeres egne kontakter**, så maskinen kan vokse, så stor I vil. 🔌

!!! abstract "🎓 Hvad I lærer i dag"
    - **digitalt input** — læs en rigtig kontakt
    - **løkker** (`for altid`) — hold øje med en pin hele tiden
    - **tilstand** — maskinen husker, hvad I gjorde

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="et bumper-hit der breder sig ud over skærmen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ffd23f"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

!!! info "🎯 Ny til pinball-projektet?"
    Se **[Pinball-projektet](../../pinball/README.md)** for det store billede og **[Uge 2 — Pinball-scoreboard](../week-02-data-sensors/README.md)** for score-ved-berøring-bygget, som dette fortsætter.

## ⚡ Sæt flere mål til

**Hvorfor?** Indtil nu er jeres mål de **3 touch-pins** (P0/P1/P2). En rigtig flipper har *masser* af mål, bumpere og baner — og hver eneste er bare en lille **kontakt, som kuglen slutter**. Denne uge er, hvordan I **slutter og læser jeres egne kontakter**, så maskinen kan vokse, så stor I vil. Det er den rigtige elektronik, som lys og flippere kobles på senere. 🔌

Byg det op **ét lille trin ad gangen** — hvert trin tilføjer kun lidt. 🌱

*🎓 Begreb: **digitalt input** + **løkker** (`for altid`) + **tilstand**.*

??? note "Sådan virker det"

    **Formål.** Lær, hvordan en *rigtig* kontakt læses, og det ene trick — **kant-detektion** — bag enhver knap, bumper og bane i verden. Det er input-elektronikken, som lys og flippere kobles på senere.

    **Tænk på det som en tælle-bom:** den skal tælle hver person **én gang**, når de skubber igennem — ikke blive ved med at tælle, mens nogen læner sig på den. Det "tæl ved ændringen" er `wasClosed`-tricket; i maskinen scorer en bumper én gang pr. hit, ikke mens kuglen hviler mod den.

    **Sådan virker koden (nøgletrinene):**

    - `sæt pull pin P0 op` gør, at pinnen hviler på **1**, når kontakten er åben; slutter man den (en ledning til **GND**), trækkes den til **0**. En `for altid`-løkke læser `digital læs P0` igen og igen.
    - **② er en bevidst fejl:** at lægge point til *inde i* løkken får scoren til at eksplodere, fordi løkken kører hundredvis af gange i sekundet, mens kontakten holdes.
    - **③ er rettelsen — den store idé:** en `wasClosed`-variabel (et **flag**), så den kun scorer, når pinnen *bliver* 0 (og `wasClosed` stadig var falsk), og sætter så flaget; at åbne kontakten rydder det. "Kun ved ændringen" = **kant-detektion** → ét hit, ét point.
    - **⑤ rollover-baner** holder et `leftArmed`-flag: at ramme P0 lader det op, at ramme P1 *mens det er ladet op* udbetaler BONUS. Maskinen husker nu, hvad der skete først — det er **tilstand**.

    **Vær opmærksom på:** trin ①–⑤ kører i simulatoren (klik P0/P1). Trin ⑥ flytter de ekstra kontakter til ledige pins **P8/P9**, som simulatoren ikke kan klikke — test det på hardware (eller læs P0/P1 midlertidigt).

!!! tip "Hvilken pin? P0 nu, ledige pins senere"
    Vi øver på **P0**, fordi I kan **trykke på den i simulatoren**. På det rigtige bord bliver jeres touch-mål på P0–P2, og hver *ekstra* kontakt kommer på en ledig pin (**P8, P9, …**) — læst med **præcis de samme klodser**, bare et andet pin-nummer. **Keyestudio-shieldet** giver hver pin sit eget stik — sådan når I **P8/P9** (en bar micro:bit kan kun klipse på P0/P1/P2).

**① Læs en kontakt** 🔌 — hele idéen i tre klodser: **`sæt pull pin P0 op`**, og så en **`for altid`**-løkke, der viser et ✓, mens kontakten er sluttet (**`digital læs pin P0` = 0**), og rydder skærmen ellers. Tryk på **P0** i simulatoren — ✓ til, ✓ fra.

??? example "👀 Se klodserne"

    ```makecode
    auto:adv-1
    ```

**② Få den til at score** 🔢 — læg point til, når den slutter. Tryk på P0 og se… scoren **stiger vildt hurtigt**, mens du holder! Det er et rigtigt problem — `for altid`-løkken tæller *hver* gang. Det retter vi nu.

??? example "👀 Se klodserne"

    ```makecode
    auto:adv-2
    ```

**③ Ét hit = ét point** 🎯 — tilføj et **`wasClosed`**-flag, så et hit kun scorer **én gang** — når kontakten *først* slutter. Det "kun ved ændringen"-trick er sådan enhver rigtig knap og bumper virker.

??? example "👀 Se klodserne"

    ```makecode
    auto:adv-3
    ```

**④ Et mål mere** ➕ — kopiér samme idé over på **P1** som endnu en kontakt, der giver flere point. To mål! På det rigtige board er det bare endnu en ledning til endnu en pin.

??? example "👀 Se klodserne"

    ```makecode
    auto:adv-4
    ```

**⑤ Rollover-baner** 🛣️ — en rigtig flipper-combo: ram den **venstre bane (P0)** for at *lade den op*, og derefter den **højre bane (P1)** for en stor **BONUS**. Forkert rækkefølge = ingen bonus. Nu husker maskinen, hvad I gjorde — det er **tilstand**.

??? example "👀 Se klodserne"

    ```makecode
    auto:adv-5
    ```

**⑥ Sæt det ind i din maskine** 🕹️ — læg jeres nye kontakter ind i hele spillet: touch-mål på **P0/P1/P2** *og* to kablede kontakter på **P8/P9** (en **100**-bumper og en **500**-jackpot), alle med ét-hit-ét-point-tricket. Et rigtigt bord med rigtige kontakter.

??? example "👀 Se klodserne — kør eller redigér"

    ```makecode
    auto:adv-6
    ```

### 🔭 Næste gang — lys & flippere

Nu hvor maskinen *læser* mange kontakter, er den klar til de dele, der får den til at bevæge sig og lyse (kommende uger):

- 🌈 **Spilleplade-lys** — en **NeoPixel**-strip der blinker ved hvert kontakt-hit.
- 🕹️ **Flippere** — **servoer** på knap **A/B** der slår kuglen op ad bordet igen.

## 🎮 Bonus — vippelabyrint (hjernepause)

Brug for et afbræk fra ledninger? Vip boardet, og en prik triller hen over skærmen — som en kugle på en bakke. Samme accelerometer som før, nu til at styre en sprite. 🎮

??? note "Sådan virker det"

    **Formål.** En hjernepause uden ledninger, der genbruger accelerometeret til at styre en **sprite** (en flytbar LED) på skærmen.

    **Tænk på det som et træ-labyrintspil med en kugle:** vip bakken, og kuglen triller den vej, du hælder den.

    **Sådan virker koden:** `opret sprite` laver spiller-prikken og et mål. En `for altid`-løkke læser `acceleration (X)` og `(Y)` — hver cirka −1023…1023 — **dividerer med 300** for at få et lille skridt, og `ændr x/y med` skubber prikken. Når spilleren `rører` målet, `score +1`, og målet hopper til et tilfældigt sted. **`/ 300`** er fartknappen: mindre = hurtigere og mere nervøst. Flyver prikken af sted? Sæt den op til 500.

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 218" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set player to create sprite at 2,2</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set target to create sprite at 4,4</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">player change x by (acceleration X / 300)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">player change y by (acceleration Y / 300)</text>
<rect x="322" y="125" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if player touching target → score +1</text>
<rect x="322" y="160" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 100 ms</text>
</svg>
</div>

```javascript
let player = game.createSprite(2, 2)
let target = game.createSprite(4, 4)
basic.forever(function () {
    player.change(LedSpriteProperty.X, input.acceleration(Dimension.X) / 300)
    player.change(LedSpriteProperty.Y, input.acceleration(Dimension.Y) / 300)
    if (player.isTouching(target)) {
        game.addScore(1)
        target.set(LedSpriteProperty.X, randint(0, 4))
        target.set(LedSpriteProperty.Y, randint(0, 4))
    }
    basic.pause(100)
})
```

!!! tip "▶️ Prøv den i MakeCode (30 sekunder)"
    1. Åbn <https://makecode.microbit.org> → **New Project**
    2. Klik på **`{ } JavaScript`**-knappen øverst
    3. Markér alt i editoren og **slet det**, indsæt derefter **koden ovenfor**
    4. Klik på **Blocks** for at skifte tilbage — de rigtige blokke dukker op, klar til at udforske
    5. **Download** for at lægge den på et board, eller tryk ▶️ for at køre den i simulatoren

    `acceleration (X)` er cirka −1023…1023. At dividere med 300 gør det til et lille skridt som −3…3 — den division er din **fartkontrol**. Mindre tal = hurtigere og mere nervøst. Flyver prikken af sted med det samme? Øg divisoren (prøv 500). Ekstra: tilføj **vægge** (blink og start forfra ved kanten), en **30-sekunders nedtælling** eller et mål mere, der giver 5.

## ✅ Jeg er færdig når…

- ☐ Jeg **læste min egen kontakt** og så ✓ til / ✓ fra.
- ☐ Jeg rettede den til **ét hit = ét point** (`wasClosed`-flaget).
- ☐ Jeg tilføjede et **mål mere** på en anden pin.
- ☐ *(Boss!)* **Rollover-baner** giver en **BONUS** kun i den rigtige rækkefølge.

## 🎉 Kahoot-tid!

Slut af med denne uges quiz — **begge grupper spiller sammen**.

```kahoot
week-3
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** den **elektronik-først**-halvdel af pinball-bygget — *at læse en kontakt*, bygget op ét lille trin ad gangen (hver indlejring tilføjer kun det nye, så børnene ser den vokse). Stadig **ingen nye dele** ud over Uge 2, kun ledninger og shieldet. Den fortsætter direkte fra **[Uge 2](../week-02-data-sensors/README.md)**.

    **Idéen:** en kontakt er to ledninger, kuglen slutter; `sæt pull pin … op` gør, at pinnen læser **1** åben / **0** sluttet, og en `for altid`-løkke holder øje. Det store aha er **② → ③**: uden et kant-flag stiger scoren, mens man holder; **`wasClosed`**-flaget ("kun ved ændringen") retter det — samme trick bag enhver knap og bumper. Trin ①–⑤ øver på **P0/P1**, så børnene kan **trykke på pads i simulatoren**; ⑥ flytter de ekstra kontakter til ledige pins **P8/P9** præcis som på det rigtige board (samme klodser, andet pin-nummer — simulatoren kan ikke klikke dem, så test ⑥ på hardware eller ved midlertidigt at læse P0/P1). ⑤ (rollover-baner) tilføjer **ordnet tilstand** til en combo.

    **Materialer**

    - micro:bit (**V2** anbefales) + USB, **Keyestudio sensor-shield**
    - et par ekstra ledninger (og folie/en knap) til at lave **kontakt-mål** — øv på P0/P1, og sæt så rigtige kontakter på **P8/P9**
    - Bærbar/Chromebook — **simulatoren er nok** til trin ①–⑤ (klik på pinsene)

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 genopfrisk scoreboardet → 15 ① læs en kontakt + ② få den til at score → 20 ③ ét-hit-ét-point (nøgleidéen) → 15 ④ et mål mere → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 15 ⑤ rollover-baner / ⑥ hele maskinen for hurtige → 5 **vippelabyrint**-hjernepause → 5 fremvisning → 5 Kahoot.

    **Noter:** klodserne vises; **JavaScript/Python** er ét klik væk via **Åbn & kør**. Det er input-halvdelen af pinball-elektronikken — og lægger op til hardware-ugerne: 🌈 NeoPixels og 🕹️ servoer. **🎮 Vippelabyrinten** er en valgfri hjernepause (accelerometeret, de allerede kender) — ingen ledninger, ren sim-sjov.
