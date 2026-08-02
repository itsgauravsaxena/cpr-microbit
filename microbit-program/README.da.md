# Micro:bit Frivilligprogram — 10 uger

Et 10-ugers kodningsprogram for to grupper af 8-10-årige, opdelt efter erfaring. Sessioner på 1 time, fysiske micro:bits til alle. Bygget næsten udelukkende på officielle tutorials fra micro:bit Foundation / MakeCode.

## Grupper

- **[Gruppe A — Startup](./group-a-startup/README.md)** — helt nye til kodning. Uge 1-4 opbygger grundlæggende færdigheder gennem officielle MakeCode-tutorials, uge 5-6 bygger en servodrevet "Ticklebot"-robot, uge 7-8 bygger et radiosender/-modtager-projekt, uge 9 samler trådene, og uge 10 er en fremvisning.
- **[Gruppe B — Avanceret (Mini-flippermaskine)](./group-b-advanced-pinball/README.md)** — allerede fortrolige med MakeCode. Et 10-ugers afgangsprojekt, hvor der bygges en lille flippermaskine til bordet: børnene 3D-designer og printer de simple indvendige dele (bumpere, sensorholdere), mens det udvendige kabinet/de præcisionskrævende dele leveres på forhånd. Programmeringen dækker pointtælling, sensorer og en radioforbundet resultattavle.

## Repo-struktur

Hver uge har sin egen mappe med:
- `README.md` — mål, link(s) til officiel tutorial, materialer, trinnoter og referencelinks
- `code/` — hvor det eksporterede MakeCode-projekt for ugen lægges (`.hex`-fil eller det delbare `makecode.microbit.org/_xxxxx`-link indsat i en tekstfil). MakeCode-projekter lever som udgangspunkt i browseren, så eksport hertil er det, der rent faktisk bevarer hver uges arbejde.

## Sådan gemmer du et MakeCode-projekt i `code/`

1. I MakeCode-editoren klikkes på tandhjulsikonet → **Share** for at få et delbart link, eller **Download** for at få en `.hex`-fil
2. Læg `.hex`-filen i den pågældende uges `code/`-mappe, eller indsæt delelinket i en `link.md`-fil dér
3. Commit og push

## Undervisningstilgang: billed-/animationsforklaringer

MakeCodes indbyggede **Tutorials**-tilstand (fanen Tutorials på MakeCodes startskærm) gennemgår hvert projekt trin for trin med billeder, fremhæver den præcise blok, der skal trækkes som den næste, og kører live i simulatoren på skærmen. Vis den på en skærm hver uge, og lad tutorialen stå for forklaringen — dette er det primære visuelle hjælpemiddel for hele programmet, og der henvises til det i ugernes README-filer nedenfor i stedet for at bygge det op fra bunden.

## Referencebyg (Gruppe B)

- ["3D Printed Pinball" af ctrl design](https://pinshape.com/items/24228-3d-printed-pinball) — micro:bit/Arduino-baseret, skalerbar sværhedsgrad, gratis STL-filer
- micro:bit + PinBox 3000 pap-flippermaskine (TechnoChic) — reference til at styre lys, lyd og en resultattavle fra en micro:bit på et enkelt stel
