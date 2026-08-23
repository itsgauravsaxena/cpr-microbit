# Uge 3 — Bevægelse: vippelabyrint

> 🎮 Vip boardet, og en prik triller hen over skærmen — som en kugle på en bakke. Sådan virker rigtige bevægelsesstyringer!

**Mål:** brug accelerometeret til at flytte en sprite — jeres første spil med rigtig fysik-fornemmelse.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="en prik der triller over skærmen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="1;0;0;0;0;0;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;1;0;0;0;0;0;0"/><rect x="98" y="42" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;1;0;0;0;0;0"/><rect x="126" y="14" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;1;0;0;0;0"/><rect x="98" y="42" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;1;0;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;0;1;0;0"/><rect x="42" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;0;0;1;0"/><rect x="14" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;0;0;0;1"/><rect x="42" y="98" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Hvad I bygger

En prik, du styrer ved at vippe, plus et mål, du skal fange. Fang det, og pointtallet stiger.

## Eksempelkode

Kør det her, og klik på **Open & edit in MakeCode** for at lave din egen version:

<!-- Indsæt ugens MakeCode-del-id nedenfor (Share -> Publish giver et link
     som https://makecode.microbit.org/_abc123 -- indsæt id'et eller hele
     linket). Indtil et id er tilføjet, vises en "kommer snart"-note. -->
```makecode
auto
```

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

    Børnene kan gøre præcis det samme for at komme i gang og derefter ændre tingene, så det bliver deres eget.


## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min — opsummér accelerometeret
- 25 min — byg den vippestyrede prik
- 20 min — tilføj målet og pointtælling; justér `/ 300`, indtil det føles rigtigt
- 10 min — byt boards og spil hinandens version

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Gør det til et rigtigt spil
- 15 min — tilføj **vægge** (blink og start forfra ved kanten) eller en **30-sekunders nedtælling** — dit valg
- 5 min — justér sværhedsgraden: ændr divisoren, indtil det er svært men fair
- 5 min — byt boards og sæt en highscore i en andens spil
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen ([ugens spørgsmål](../../quiz/README.md#uge-3))

## ✅ Færdig når
- Når man vipper boardet, bevæger prikken sig jævnt i alle retninger.
- At fange målet giver et point, og målet hopper et nyt sted hen.

## Sådan virker det

`acceleration (X)` er cirka −1023…1023. At dividere med 300 gør det til et lille skridt som −3…3 — den division er din **fartkontrol**. Mindre tal = hurtigere og mere nervøst.

## Ekstra udfordringer
- Tilføj vægge: rammer spilleren kanten, så blink og start i midten.
- Tilføj nedtælling — hvor mange mål på 30 sekunder?
- To mål ad gangen: ét giver 1 point, ét giver 5.

## Hvis det ikke virker
- Prikken flyver af sted med det samme? Øg divisoren (prøv 500).
- Prikken bevæger sig ikke? Tjek at du brugte `change x by`, ikke `set x to`.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
