# Uge 1 — Kickoff & kodeudfordring

> 🏴‍☠️ Velkommen til Pro! I kan allerede det grundlæggende — denne sæson handler om **større idéer**: sensorer, data, bevægelse, lyd, radio og jeres egne opfindelser. Først en opvarmningsudfordring.

**Mål:** varm op, bliv enige om, hvordan vi arbejder (del din kode hver uge), og løs en lille kodeudfordring.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="gættespillet der tæller" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## Hvad I bygger

Et **gæt det hemmelige tal**-spil: micro:bitten vælger et tal, du trykker A for lavere / B for højere, og den siger til, når du rammer rigtigt.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 268" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set secret to pick random 1 to 20</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set guess to 10</text>
<rect x="30" y="140" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="135" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change guess by -1</text>
<rect x="30" y="210" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="230.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number guess</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change guess by 1</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number guess</text>
<rect x="322" y="140" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="135" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A+B pressed</text>
<rect x="322" y="175" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if guess = secret → show yes</text>
<rect x="322" y="210" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="230.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">else → show no</text>
</svg>
</div>

```javascript
let secret = randint(1, 20)
let guess = 10
input.onButtonPressed(Button.A, function () {
    guess += -1
    basic.showNumber(guess)
})
input.onButtonPressed(Button.B, function () {
    guess += 1
    basic.showNumber(guess)
})
input.onButtonPressed(Button.AB, function () {
    if (guess == secret) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
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
- 5 min — velkommen, hvad Pro handler om, se på 10-ugers-kortet
- 15 min — udfordring: kan I lave gættespillet selv?
- 30 min — byg det sammen, sammenlign løsninger
- 10 min — eksportér din .hex og gem den i `code/`

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Tag udfordringen videre
- 10 min — vælg én **ekstra udfordring** og byg den (varmere/koldere, eller tæl gættene)
- 10 min — find en makker: spil deres version og prøv at få den til at gå i stykker
- 5 min — eksportér din `.hex` til `code/` og notér, hvad du ville tilføje næste gang
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen ([ugens spørgsmål](../../quiz/README.md#uge-1))

## ✅ Færdig når
- A og B ændrer gættet, og A+B viser ✓ eller ✗ korrekt.
- Alle har gemt deres projekt i `code/`.

## Sådan virker det

Micro:bitten vælger et **secret**-tal én gang ved start. Dit `guess` er en separat variabel, du flytter op og ned — det er sammenligningen af de to, der gør det til et spil. Bemærk at `secret` ikke ændrer sig undervejs.

## Ekstra udfordringer
- Vis 🔥 *varmere* / ❄️ *koldere* i stedet for kun ✓ og ✗.
- Tæl hvor mange gæt det tog, og vis tallet til sidst.
- Tilføj et ryst for at starte en helt ny runde.

## Hvis det ikke virker
- Viser altid ✗? Tjek at `secret` sættes i **on start**, ikke inde i en knap-blok.
- Tallet ændrer sig ikke? Sørg for at du brugte `change … by` og ikke `set … to`.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
