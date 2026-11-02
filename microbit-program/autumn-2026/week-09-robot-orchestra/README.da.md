# Uge 9–10 — Robot-orkester 🤖🎶

> Vores afsluttende projekt — to gange på én side! I **uge 9** bygger alle en **papirrobot** med **to servoer** (en trommearm og et hoved, der vipper), **LED-øjne** og sin helt egen **tone**. I **uge 10** lærer robotterne at spille **sammen** over radio. Og i den sidste time giver vi en **koncert** for alle. 🎉

!!! abstract "🎓 Hvad I lærer i dag"
    - **at bygge** — gør fladt papir til en robot, der kan stå, med servoer tapet på
    - **at forbinde** — to servoer (P1, P2) og to LED'er (P8, P13) på shieldet
    - **at teste** — tjek, at hver del virker, før du tilføjer den næste
    - **ét program, mange robotter** — alle robotter kører den samme kode; kun *din tone* er forskellig
    - **at spille sammen** — én dirigent sender sangen over radio, otte robotter svarer

## 🎼 Planen

| Uge | Hvad vi laver |
|---|---|
| **9** | **Byg** din robot, og test den 🛠️ |
| **10** | **Orkesterprøve** — alle robotter spiller “Mester Jakob” sammen over radio 📡 |
| **11** | 🎉 **Koncert** for forældre og venner |

**Otte robotter, otte job:** syv robotter ejer hver **én tone** (dyb G, C, D, E, F, G, A), og én robot er **trommeslager** 🥁. Din lærer fortæller dig, hvilken du er.

## 🛠️ Gang 1 · uge 9 — byg

I dag: print, byg, forbind og test din robot, og sæt **din tone**.

### 📄 Print robotten

Alt er af papir — intet pap, ingen hobbykniv. Print PDF'en, klip, fold, tape. ✂️

[⬇️ Robot-skabelon — dansk (PDF, 7 sider)](robot-skabelon-A4.pdf){ .md-button .md-button--primary }
[⬇️ Robot template — English (PDF)](robot-template-A4.pdf){ .md-button }

!!! tip "Print 🖨️"
    - Print i **100 % / “faktisk størrelse”** — ikke “tilpas til side”. Tjek: stregen på ark 4 skal være **præcis 5 cm**.
    - **Hvert barn:** ark **1** (krop A) og **2** (hoved B, arme C + D, tromme E).
    - **Til deling:** ark **3** (tone-badges G, trommeskind F, pynt H) — 2–3 kopier.
    - **Pr. bord:** ark **4–7** (deleliste, sådan sidder servoerne, billedtrin).
    - Almindeligt papir virker. Tykkere papir (160–200 g) eller et stykke **cornflakespakke** limet bag kroppen gør den stærkere.

### 🛠️ Byg den

Følg **billedtrinene** på ark 6–7. Delene har bogstaver, ligesom hos IKEA: **A** krop · **B** hoved · **C** trommestik-arm · **D** pynt-arm (valgfri) · **E** tromme · **F** trommeskind · **G** din tone-badge · **H** pynt.

!!! info "Sådan sidder servoerne (ark 5) 🔧"
    Servoen ligger **fladt på papiret**, og **akslen peger mod dig** — ligesom viseren på et ur.

    - **Arm:** servo 1 sidder på **højre skulder**. Arm **C** tapes på hornet og hænger ned. Når servoen drejer, svinger C og slår på trommen.
    - **Hoved:** servo 2 sidder på **halsen**. Bagsiden af hoved **B** tapes på hornet, så hovedet skjuler servoen. Når servoen drejer, **vipper** hovedet fra side til side.

**Trin 4 — sæt begge servoer på 90°, *før* du taper noget på**, så armen hænger lige, og hovedet sidder lige:

??? example "🎯 servo-center · P1 + P2"

    ```makecode
    auto:servo-center
    ```

    *Download det, vent på ✓, og sæt så hornene, armen og hovedet på. Drej ikke servoerne med hånden bagefter!*

### 🔌 Ledninger

| Del | Pin | Ledninger |
|---|---|---|
| Servo 1 · arm | **P1** | brun → G · rød → V · orange → S |
| Servo 2 · hoved | **P2** | brun → G · rød → V · orange → S |
| LED-øje venstre | **P8** | langt ben → S · kort ben → G |
| LED-øje højre | **P13** | langt ben → S · kort ben → G |

*Forbliver LED-øjnene mørke? Vend LED'en om — se 🔧-tjeklisten i [Uge 7](../week-07-light-it-up/README.md).*

### 🧪 Test din robot

Før du pynter, så tjek, at alt bevæger sig: **A** = armen slår + øjnene blinker, **B** = hovedet vipper.

??? example "🧪 robot-test · P1 + P2 + P8 + P13"

    ```makecode
    auto:robot-test
    ```

    *Rammer armen ikke trommen? Flyt trommen, eller tape C lidt længere nede. Sidder hovedet skævt? Kør servo-center igen, og tape B på igen.*

### 🎵 Dit robotprogram

Det er det program, din robot spiller i koncerten. **Alle med en tone bruger det samme program** — du ændrer kun **to ting** i starten:

1. **`sæt myNote til …`** — klik på 🎹 klaveret, og vælg **din tone**. Dyb G er det G, der ligger længere til venstre på klaveret.
2. **`vis streng "ROBO"`** (inde i *når der trykkes på knap A*) — skriv **din robots navn**.

??? example "🎵 robot — til de 7 tone-robotter"

    ```makecode
    auto:robot
    ```

    | Når… | din robot… |
    |---|---|
    | dens tone kommer over radio 📡 | slår på trommen, vipper hovedet, blinker med øjnene og spiller sin tone |
    | du trykker **A** | laver en **solo**: siger sit navn, danser og siger hej 👋 |
    | du rører **logoet** 👆 | fniser og vrikker (Ticklebot!) |
    | publikum **klapper** 👏 | bukker (kun når musikken er stoppet) |

    *Svinger armen væk fra trommen i stedet for ned på den? Skift `armDown` fra **60** til **120**.*

??? example "🥁 drummer — til tromme-robotten"

    Trommeslageren skal ikke have en tone: **BUM** (arm + dyb tromme) på slag 1 og 3, **TIK** (hoved + tik) på slag 2 og 4. Skift `"DRUM"` til din robots navn.

    ```makecode
    auto:drummer
    ```

## 🎼 Gang 2 · uge 10 — orkesterprøve

I dag bliver robotterne til et **orkester**! 🎶

### 1. Gør klar 🔋

- Tjek dit robotprogram: den rigtige **tone** 🎹 og **din robots navn**. Download det igen, hvis du har ændret noget.
- Sæt **batteripakken** i — robotter på scenen kan ikke hænge i et USB-kabel.
- Tryk **A**: laver din robot sin solo? Så er du klar!

### 2. Stil jer op som et klaver 🎹

Stil robotterne på række **fra dyb til lys**: dyb G · C · D · E · F · G · A · og 🥁 trommeslageren til sidst. Når sangen spiller, kan I **se** melodien hoppe hen ad rækken!

### 3. Dirigenten 🎼

Din lærer holder dirigent-micro:bit'en:

??? example "🎼 conductor — lærerens micro:bit"

    - **A** → spiller “Mester Jakob”: sender hver tone og hvert trommeslag over **radiogruppe 9**
    - **B** → **hjælpe-tilstand** (viser **H**): dirigenten spiller også melodien, så manglende toner bliver dækket
    - **A + B** → alle robotter **bukker** 🙇

    ```makecode
    auto:conductor
    ```

    *For hurtigt? Skift `eighth` fra **200** til **250** for en langsommere sang.*

### 4. Fiks det 🔧

| Problem | Prøv det her |
|---|---|
| Min robot spiller aldrig | Er 🎹 tonen rigtig? Radiogruppe **9**? Er batterierne tændt? |
| Min robot laver en solo midt i sangen | Rør ikke **A** eller **logoet**, mens orkestret spiller |
| Armen rammer ikke trommen | Flyt trommen, eller skift `armDown` (60 ↔ 120) |
| Robotterne bukker midt i sangen | Lokalet er for larmende — brug **A + B** på dirigenten til buk i stedet |
| En tone mangler | Nogen er væk → tryk **B** på dirigenten (hjælpe-tilstand) |

### 5. Øv koncerten 🎤

1. **Hej!** En ad gangen trykker hver robot på **A** — navn, dans, “hej”. 👋
2. **Sangen:** dirigenten trykker **A** — “Mester Jakob”. 🎶
3. **Klapsalve:** alle klapper → robotterne bukker. 🙇
4. **Din tur:** en gæst får lov at være dirigent! 🎼

### 🚀 Level op — gør den til din egen

- **Flere lys:** sæt LED'er på **P14, P15 eller P16**, og tænd dem også inde i `hit`. *(Ikke P0 — højttaleren bruger den.)*
- **Din egen solo:** skift dansen i *når der trykkes på knap A*, og vælg en anden lyd — `giggle`, `twinkle`, `soaring`…
- **Et kostume:** en hat, en kappe, en butterfly fra ark 3 (**H**) — gør din robot nem at genkende!

## ✅ Jeg er færdig når…

**Gang 1 · uge 9**

- ☐ Jeg klippede og foldede min robot, og den **kan stå**. ✂️
- ☐ Jeg kørte **servo-center** og satte **armen** og **hovedet** lige på. 🎯
- ☐ Min **robot-test** virker: armen slår, hovedet vipper, øjnene blinker. 🧪
- ☐ Jeg satte **min tone** og **min robots navn** i robotprogrammet. 🎵

**Gang 2 · uge 10**

- ☐ Min robot spiller **sin tone**, når dirigenten spiller sangen. 🎶
- ☐ Vi spillede **“Mester Jakob” sammen**, fra start til slut. 🎼
- ☐ Min robot laver sin **solo**, **fniser**, når den bliver kildet, og **bukker**, når vi klapper. 🙇
- ☐ *(Legende!)* Jeg gav min robot noget **ekstra** — flere LED'er, en ny solo eller et kostume. 🌟

## 🎉 Kahoot-tid!

**Uge 9**

```kahoot
week-9
```

**Uge 10**

```kahoot
week-10
```

---

??? note "👩‍🏫 Til hjælpere — sessionsplan & noter"

    **Mål:** uge 9 — hvert barn har en **papirrobot, der kan stå**, hvor armen, hovedet og øjnene virker, med **robotprogrammet** sat til sin tone. Uge 10 — **hele orkestret spiller sangen sammen** og øver koncerten.

    **Hvem gør hvad (8 børn):** alle bygger **deres egen robot** — de viser den frem til koncerten. Arbejd i **par**: én klipper, mens den anden forbinder og tester, og så bytter I, så hvert par bliver færdigt med to robotter. Giv toner i denne rækkefølge, så sangen stadig virker, hvis nogen mangler: **C, G, E, F, D, A, dyb G, trommeslager**. Listen over, hvem der har hvilken tone, beholder du selv — den står ikke på denne side.

    **Materialer**

    - 8 micro:bits (V2) + USB + **sensor-shields**, **16 SG90-servoer**, **16 LED'er**, ledninger
    - **batteripakker** — to servoer på USB kan få micro:bit'en til at genstarte; skal alligevel bruges til koncerten
    - den printede PDF (se *Print* ovenfor), **sakse, tape** (malertape er nemmest), **limstifter**, blyanter + viskelædere (til øjenhullerne), farver
    - valgfrit: pap fra en cornflakespakke til at gøre kroppen stiv, ispinde af træ til at gøre arm C stiv (ingen plastik)
    - én micro:bit til **dig** som dirigent

    **Gang 1 · uge 9 (60 + 20 pause + 30)**

    - **Blok 1 (60):** 5 vis idéen + del toner ud → 10 **forbind** 2 servoer + 2 LED'er, og kør **robot-test** på de løse dele (bevis først, at elektronikken virker!) → 30 **byggetrin 1–4** i par (klip, fold, øjenhuller, servo-center) → 10 **trin 5–6** (servoer på kroppen, hoved + arm på hornene) → 5 tjek-ind.
    - **Pause (20)**
    - **Blok 2 (30):** 10 **trin 7–8** (tromme, forbind) → 10 download **robot**, sæt tone + navn, prøv solo / kild / klap → 5 🎼 **første orkesterprøve** med dirigenten → 5 Kahoot (spring over, hvis tiden er knap).

    **Gang 2 · uge 10 (60 + 20 pause + 30)**

    - **Blok 1 (60):** 10 **gør færdig / fiks** robotter fra sidste uge → 5 batterier i, tjek tone + navn → 5 **stil op** fra dyb → lys → 10 **første gennemspilning** + 🔧 fiks-listen → 15 **øv**, til det lyder godt (prøv hjælpe-tilstand, en langsommere `eighth`) → 15 **level op** og kostumer.
    - **Pause (20)**
    - **Blok 2 (30):** 15 🎤 **generalprøve** (hej → sang → klapsalve → gæstedirigent) → 10 sidste finpudsning → 5 Kahoot.

    **Noter:** hver indlejring åbner i **Blokke** med **servo**-udvidelsen allerede tilføjet. Alle robotter og dirigenten bruger **radiogruppe 9** — skift den ikke. Kør **servo-center, før hornene tapes på**, ellers kommer arme og hoveder til at sidde skævt. **Genstart, summen eller rysten** = for lidt strøm → batteripakke. **Klap-og-buk** lytter med mikrofonen, men kun når intet har spillet i 3 sekunder, så musikken ikke udløser det; i et larmende lokale kan du i stedet bruge **A + B på dirigenten** til at få alle til at bukke. Tonerne er **korte “ding”-lyde** — med vilje, så en robot er klar igen til sin næste tone. Mangler der børn? Tryk **B** på dirigenten (hjælpe-tilstand) for at fylde hullerne. Bliver papiret blødt, hvor en servo sidder, så lim et stykke cornflakespakke bag det.
