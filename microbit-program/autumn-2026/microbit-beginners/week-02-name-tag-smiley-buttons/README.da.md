# Uge 2 — Spil-lab 🎮

**🔗 Åbn siden på en computer:** gå til **[tinyurl.com/beginw2](https://tinyurl.com/beginw2)**

> Varm op med en ansigtsmaskine, og byg så dit første **rigtige spil**: en ryste-og-rul **terning** 🎲. (Flere spil — musik 🎵 og en spåkugle 🔮 — kommer i Uge 3, og radiospil 📻 i Uge 4.)

!!! abstract "🎓 Hvad I lærer i dag"
    - **hændelser** — kør kode ved en knap eller et ryst
    - **tilfældig** — overraskelsestal
    - **`hvis / ellers`** (betingelser) — få micro:bit'en til at *vælge*

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

??? note "Sådan virker det"

    **Formål.** En blid opvarmning, der gør Uge 1's `vis ikon` *interaktiv* — den første smagsprøve på **hændelser** (kode, der venter på, at noget sker) og **tilfældig**.

    **Tænk på det som en dørklokke:** koden sidder helt stille, indtil dens knap trykkes, og gør så sit ene job — og der er en klokke hver til A, B, begge-på-én-gang og et ryst.

    **Sådan virker koden:**

    - `ved start` kører én gang, når boardet tændes — her viser den `HEJ!`.
    - `ved tryk på knap A` og `ved tryk på knap B` er to separate **hændelser**. Hver er sit eget lille program, der venter på sin knap og så viser et glad / ked-af-det ansigt.
    - `ved tryk på knap A+B` er en *tredje* hændelse, der kun kører, når begge knapper trykkes samtidig.
    - `ved ryst` vælger et tilfældigt tal **0–3** (`vælg tilfældig`) og lægger det i en variabel, og en `hvis / ellers hvis`-kæde viser et ansigt for hver værdi — det første kig på at *vælge* ud fra et tal.

    **Vær opmærksom på:** A+B er sin egen hændelse — tryk begge på én gang (i simulatoren: klik på den lille **A+B**-knap). Hændelser kører ikke oppefra og ned; hver venter bare på sin egen udløser.

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

Byg **terning**-spillet ét lille stykke ad gangen. **🔨 Byg det** starter med en nem version og vokser så til det fulde spil. 🌱

### 🎲 Terning

Ryst for et tilfældigt **1–6**. 🎲

*🎓 Begreb: **tilfældig** + **`hvis / ellers`** (betingelser).*

??? note "Sådan virker det"

    **Formål.** Spillet, alle kan nå. Det gør "ryst → et tilfældigt tal" til en *rigtig* terning med prikker, så børnene ser et tal styre, hvad der tegnes på skærmen.

    **Tænk på det som en brætspilsterning:** ryst, og du får et 1–6 — og `hvis / ellers` er reglementet ("hvis du slog 3, så tænd tre prikker").

    **Sådan virker koden:**

    - `ved ryst` er **hændelsen** — den kører én gang, hver gang boardet rystes.
    - `vælg tilfældig 1 til 6` laver et nyt tal og gemmer det i en variabel (`roll`).
    - En `hvis / ellers hvis`-stige tjekker `roll` og tegner det rigtige ansigt med `vis lys` (hver gren er et 5×5-prikmønster). Det sidste `ellers` klarer 6'eren, så du kun behøver fem tjek til seks udfald.
    - Bygget vokser i tre trin: ① bare `vis tal`, ② gør **6** speciel med ét `hvis / ellers`, ③ byt hvert tal ud med rigtige **prikker**.

    **Vær opmærksom på:** børnene tilføjer `hvis`-grenene én ad gangen — undgå at indsætte den færdige stige. I simulatoren: brug **ryste**-knappen til at teste.

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

### ➡️ Flere spil — næste uge

Musik 🎵 og en spåkugle 🔮 venter i **[Uge 3 — Spil-lab 2](../week-03-game-lab-2/README.md)**, og radio- & holdspil 📻 i **[Uge 4](../../week-04-game-lab/README.md)**. Er du færdig med terningen og har tid til overs? Tag et smugkig! 👀

---

## ✅ Jeg er færdig når…

- ☐ Mine **Knap-ansigter** virker på det rigtige board (A 😀, B 🙁).
- ☐ Jeg byggede **Terning**-spillet og rullede det.
- ☐ *(Legende!)* Min terning viser rigtige **prikker**, ikke bare et tal. 🎲

## 🎉 Kahoot-tid!

Lad os slutte med en quiz — alle sammen!

```kahoot
week-2
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** byg videre på Uge 1's `vis ikon`. Varm op med **Knap-ansigter** (knapper A/B/A+B, ryst, en første smagsprøve på **tilfældig**), og byg så alle sammen **🎲 Terning**-spillet — `vælg tilfældig` + et voksende `hvis / ellers`, der slutter med rigtige **prikker**. Det er hele sessionen; resten af spil-menuen (musik & spåkugle i **[Uge 3](../week-03-game-lab-2/README.md)**, radio- & holdspil i **[Uge 4](../../week-04-game-lab/README.md)**) kommer senere, så Uge 2 er rolig, og alle lander den samme sejr. 🎯

    **Hurtige elever:** send dem direkte videre til **Uge 3** efter de næste spil eller til **🌟 Bonus** der (tegn-dit-eget, Kærlighedsmåler).

    *(Et større **🚀 Stjernefanger**-spil — variabel + løkke + LED-tegning — er parkeret i `archive/week-02-star-catcher/`, hvis du vil have et ekstra stræk. Sådan henter du det tilbage står i den mappes README.)*

    **Sessionsplan (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 genopfrisk Uge 1 → 30 byg **Knap-ansigter** sammen (trin ①–⑥) → 10 overfør til boardet → 15 start **Terning** (① rul et tal).
    - **Pause (20)**
    - **Blok 2 (30):** 20 færdiggør **Terning** (② gør 6 speciel → ③ rigtige prikker) i eget tempo → 5 fremvisning → 5 Kahoot.

    **Noter:** hver indlejring åbner direkte i **Blokke**. Hver *Byg det* viser en nem **start** først og derefter det **fulde** program, så børnene vokser ét program frem i stedet for at kopiere færdig kode.
