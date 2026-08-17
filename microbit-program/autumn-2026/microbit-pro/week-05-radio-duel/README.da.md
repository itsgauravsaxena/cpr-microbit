# Uge 5 — Radioduel: reaktionsspil for 2

> ⚡ To boards, én vinder. Når lyset blinker — smæk på knappen! Den første vinder runden.

**Mål:** brug radio til at synkronisere to micro:bits og kåre en vinder retfærdigt.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="et mål der blinker og så et lyn" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="0;1"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Hvad I bygger

Begge boards venter tilfældig tid, blinker samtidig, og det første knaptryk vinder — vist på begge skærme.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 303" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio set group 7</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set armed to false</text>
<rect x="30" y="140" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="135" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if armed → radio send &quot;WIN&quot;</text>
<rect x="30" y="210" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="230.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (happy)</text>
<rect x="30" y="245" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="265.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set armed to false</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#c2185b"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (sad)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set armed to false</text>
</svg>
</div>

```javascript
let armed = false
radio.setGroup(7)
input.onButtonPressed(Button.B, function () {   // referee: start a round
    radio.sendString("GO")
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "GO") {
        basic.pause(randint(1000, 4000))
        basic.showIcon(IconNames.Target)
        armed = true
    } else if (receivedString == "WIN") {
        basic.showIcon(IconNames.Sad)
        armed = false
    }
})
input.onButtonPressed(Button.A, function () {
    if (armed) {
        radio.sendString("WIN")
        basic.showIcon(IconNames.Happy)
        armed = false
    }
})
```

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 10 min — opsummér radiogrupper; alle på gruppe 7
- 25 min — byg duel-programmet sammen
- 15 min — find en makker og spil bedst af fem
- 10 min — hvorfor bruger vi `armed`? (forhindrer at tidlige tryk vinder)

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Turnering
- 20 min — tilføj **pointtælling** (først til 5 vinder) og afhold en cup-turnering i gruppen
- 5 min — vis vinderens reaktionstid i millisekunder
- 5 min — snak om det: hvorfor gør `armed`-tjekket spillet fair?

## ✅ Færdig når
- Begge boards viser målet på samme tid.
- Den første, der trykker A, ser ✓, og den anden ser ✗ — hver gang.

## Sådan virker det

Begge boards skal være på **samme radiogruppe**, ellers kan de ikke høre hinanden. Variablen `armed` er dommeren — den tæller kun et tryk *efter* målet dukker op, så ingen kan vinde ved at hamre på knappen for tidligt.

## Ekstra udfordringer
- Hold point over flere runder — først til 5 vinder matchen.
- Vis *hvor hurtigt* vinderen trykkede, i millisekunder.
- Straf tidlige tryk: trykker du før målet, taber du runden.

## Hvis det ikke virker
- Boards reagerer ikke på hinanden? Samme `radio set group`-nummer på begge — tjek for tastefejl.
- Begge viser ✓? Radiobeskederne krydsede; tilføj en kort `pause` før resultatet vises.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
