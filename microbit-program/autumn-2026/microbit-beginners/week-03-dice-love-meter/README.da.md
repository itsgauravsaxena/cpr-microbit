# Uge 3 — Dice + Love Meter

🎲 Ryst den og slå en terning — helt uden terning, det hele sker i lysene! Byg så en **kærlighedsmåler**, som du selv giver strøm med fingrene. ⚡

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="en micro:bit der slår terning" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="1;0;0;0;0;0"/><rect x="85" y="85" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;1;0;0;0;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;1;0;0;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;0;1;0;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;0;0;1;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;0;0;0;1"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g></g>
</svg>
</div>

**Mål:** tilfældige tal (via rysten) og berøringspin-sensorering.

**Officielle tutorials:**
- https://makecode.microbit.org/projects/dice
- https://makecode.microbit.org/projects/love-meter

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min opsummering
- 25 min — Dice-tutorial (accelerometer + `pick random`)
- 25 min — Love Meter-tutorial (berøringspins)
- 5 min — del/test

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Terningeduel
- 10 min — **terningeduel**: ryst samtidig med en makker, højeste tal vinder. Bedst af fem
- 10 min — udvidelse: vis **prikker** i stedet for et tal (tegn dem med `show leds`)
- 5 min — prøv kærlighedsmåleren rundt om bordet — hvem har de 'varmeste' fingre?
- 5 min — 🎉 **Kahoot-quiz** — hele holdet sammen ([ugens spørgsmål](../../quiz/README.md#uge-3))

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 98" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on shake</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number (pick random 1 to 6)</text>
</svg>
</div>

```javascript
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(Math.randomRange(1, 6))
})
```

**Love Meter** (berøringspin 0):

```javascript
input.onPinPressed(TouchPin.P0, function () {
    basic.showNumber(Math.randomRange(0, 100))
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
- Et ryst viser et tilfældigt tal **1–6** (terningen).
- Berøring af pin **0** viser en tilfældig 'kærligheds'-score 0–100.

## Noter
_(plads til sessionsnoter)_

## Reference
- Udvidelsesmål for Dice: vis prikker i stedet for et tal (Graphical Dice-varianten, linket fra Dice-tutorialsiden)
