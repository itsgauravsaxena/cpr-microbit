# Uge 7 — Digitalt kæledyr

> 🐣 Din micro:bit lever! Den bliver sulten, den bliver glad, og hvis du ignorerer den … bliver den ked af det. Jeres første program med **tilstand**.

**Mål:** hold styr på tilstand over tid (en variabel, der ændrer sig af sig selv) og brug funktioner til at rydde op i koden.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="et kæledyrsansigt der skifter glad, ked af det og sovende" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Hvad I bygger

Et kæledyr med et humørniveau, der falder langsomt. Tryk A for at fodre, B for at lege. Falder det til nul, falder det i søvn.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 353" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set happy to 5</text>
<rect x="30" y="105" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="100" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="125.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">every 5 seconds</text>
<rect x="30" y="140" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="160.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by -1</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
<rect x="30" y="225" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="220" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="245.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="260" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="280.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by 2 (feed)</text>
<rect x="30" y="295" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="44" y="315.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by 1 (play)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
</svg>
</div>

```javascript
let happy = 5
function showFace() {
    if (happy <= 0) { basic.showIcon(IconNames.Asleep) }
    else if (happy <= 3) { basic.showIcon(IconNames.Sad) }
    else { basic.showIcon(IconNames.Happy) }
}
input.onButtonPressed(Button.A, function () {   // feed
    happy += 2
    showFace()
})
input.onButtonPressed(Button.B, function () {   // play
    happy += 1
    showFace()
})
loops.everyInterval(5000, function () {
    happy += -1
    showFace()
})
```

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 10 min — hvad er 'tilstand'? dit kæledyr husker, hvordan det har det
- 25 min — byg humør, fodring og ansigts-funktionen
- 15 min — tilføj det langsomme fald med `hvert 5. sekund`
- 10 min — personliggør: dine egne ikoner, lyde, et navn

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Pas dit kæledyr
- 10 min — tilføj et **andet behov** (sult med sin egen timer), eller få det til at sove, når rummet bliver mørkt
- 10 min — giv det personlighed: et navn der ruller, egne ansigter, en lyd når du fodrer det
- 5 min — kæledyrsbyt: pas en makkers kæledyr i to minutter uden at lade det falde i søvn
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen ([ugens spørgsmål](../../quiz/README.md#uge-7))

## ✅ Færdig når
- Kæledyrets ansigt ændrer sig, når humøret går op og ned.
- Ignorerer man det et stykke tid, falder det i søvn; fodring vækker det.

## Sådan virker det

**Tilstand** betyder bare en variabel, programmet husker mellem hændelser. `happy` overlever knaptryk og timeren, så kæledyret har en hukommelse. **Funktionen** `showFace` sparer dig for at kopiere de samme tre `if`-blokke overalt.

## Ekstra udfordringer
- Tilføj sult som en anden variabel med sin egen timer.
- Få det til at sove om 'natten' — når lysniveauet er lavt.
- Giv det et navn, der ruller, når du trykker A+B.

## Hvis det ikke virker
- Humøret løber op til 99? Sæt et loft: er det over 5, sæt det tilbage til 5.
- Ansigtet opdateres aldrig? Kald `showFace()` sidst i *hver* blok, der ændrer `happy`.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
