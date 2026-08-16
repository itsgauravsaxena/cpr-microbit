# Uge 2 — Programmér grundlæggende pointtælling

**Mål:** et tryk på en knap eller kontakt = **+10 point**, afspil en lyd, og vis pointtallet. Dette er hjertet i hele maskinen.

**Reference:** https://makecode.microbit.org/projects/love-meter og https://makecode.microbit.org/projects/guess for blok-inspiration

## Hvad I bygger
En `score`-variabel, der starter på 0 og stiger med 10, hver gang en bumper (knap/kontakt) rammes, med et bip og tallet vist på LED'erne.

## Eksempelkode
<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 183" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8" />
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8" />
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set score to 0</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="320" y="15" width="34" height="12" rx="6" fill="#9857c9" />
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change score by 10</text>
<rect x="310" y="90" width="250" height="32" rx="7" fill="#d94fb0" />
<text x="324" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone Middle C</text>
<rect x="310" y="125" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="324" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number score</text>
</svg>
</div>

```javascript
let score = 0
input.onButtonPressed(Button.A, function () {
    score += 10
    music.playTone(Note.C, music.beat(BeatFraction.Half))
    basic.showNumber(score)
})
```

## Sessionsforløb (60 min)
- 10 min — opsummér variabler
- 40 min — byg programmet: en `score`-variabel, +10 ved tryk, et `music`-bip, vis pointtallet
- 10 min — test i simulatoren, derefter på en rigtig micro:bit med en krokodillenæb-kontakt

## ✅ Færdig når
- Et tryk på knappen/kontakten lægger **10** til pointtallet.
- Der spiller en lyd ved hvert tryk.
- Det aktuelle pointtal vises på LED'erne.
- Pointtallet starter på **0**, hver gang programmet genstarter.

## Noter
_(plads til sessionsnoter)_
