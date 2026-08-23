# Uge 4 — Guess! + Reaction Time Game

🤔 Kan du narre din micro:bit? Først et gættespil, så en lynhurtig **reaktionstest** — hvor hurtige er dine fingre? ⚡

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="en micro:bit der viser et spørgsmålstegn" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

**Mål:** logik og timing — første forsmag på "rigtig" spilfølelse.

**Officielle tutorials:**
- https://makecode.microbit.org/projects/guess
- https://makecode.microbit.org/projects/reaction-time-game

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min opsummering
- 25 min — Guess!-tutorial
- 25 min — Reaction Time Game-tutorial
- 5 min — del/test

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Reaktionsmesterskab
- 10 min — afhold et **reaktionsmesterskab**: tre forsøg hver, skriv den bedste tid på tavlen
- 10 min — gør det sværere: en tilfældig ventetid før lyset, så ingen kan snyde ved at trykke for tidligt
- 5 min — finale: de to hurtigste dyster mod hinanden
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen

## Eksempelkode

Kør det her, og klik på **Open & edit in MakeCode** for at lave din egen version:

<!-- Indsæt ugens MakeCode-del-id nedenfor (Share -> Publish giver et link
     som https://makecode.microbit.org/_abc123 -- indsæt id'et eller hele
     linket). Indtil et id er tilføjet, vises en "kommer snart"-note. -->
```makecode
auto
```

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 98" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number (pick random 1 to 9)</text>
</svg>
</div>

```javascript
input.onButtonPressed(Button.A, function () {
    basic.showNumber(Math.randomRange(1, 9))
})
```

**Reaction Time** (hvor hurtigt kan du trykke?):

```javascript
let start = 0
basic.showString("WAIT")
basic.pause(Math.randomRange(1000, 4000))
basic.showIcon(IconNames.Target)
start = input.runningTime()
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.runningTime() - start)
})
```

!!! tip "▶️ Prøv den i MakeCode (30 sekunder)"
    1. Åbn <https://makecode.microbit.org> → **New Project**
    2. Klik på **`{ } JavaScript`**-knappen øverst
    3. Markér alt i editoren og **slet det**, indsæt derefter **koden ovenfor**
    4. Klik på **Blocks** for at skifte tilbage — de rigtige blokke dukker op, klar til at udforske
    5. **Download** for at lægge den på et board, eller tryk ▶️ for at køre den i simulatoren

    Børnene kan gøre præcis det samme for at komme i gang og derefter ændre tingene, så det bliver deres eget.


## ✅ Færdig når
- **Guess!**: et knaptryk viser et tilfældigt tal.
- **Reaction Time**: efter en tilfældig ventetid dukker målet op, og din reaktionstid (ms) vises, når du trykker.

## Noter
_(plads til sessionsnoter)_
