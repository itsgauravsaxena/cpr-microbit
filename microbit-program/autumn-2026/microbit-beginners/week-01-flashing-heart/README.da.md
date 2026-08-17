# Uge 1 — Flashing Heart (soloprojekt)

> **Mød din micro:bit!** 💛 Den er en lille computer med **25 små lys**. Lige nu sover den dybt … lad os vække den og lære den at vise et **bankende hjerte!**

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="En micro:bit der blinker et hjerte" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038">
<rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/>
<rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/>
<rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/>
<rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/>
<rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/>
</g>
<g fill="#ff4d4d">
<animate attributeName="opacity" values="1;0.25;1" dur="1.1s" repeatCount="indefinite"/>
<rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/>
<rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/>
<rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/>
<rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/>
<rect x="85" y="153" width="26" height="26" rx="6"/>
</g>
</svg>
</div>

!!! tip "▶️ Se den blive levende"
    Åbn [Flashing Heart-tutorialen](https://makecode.microbit.org/projects/flashing-heart) og tryk på **▶️ afspil** i simulatoren på skærmen — hjertet banker på skærmen, før du overhovedet rører en rigtig micro:bit. Lav så **dit** board om til at gøre det samme! ✨

**Mål:** bliv fortrolig med MakeCode-editoren og arbejdsgangen med at downloade til boardet. Ingen hastværk — dette er den eneste uge med ét enkelt projekt.

**Officiel tutorial:** https://makecode.microbit.org/projects/flashing-heart

## Materialer
- 1 micro:bit + USB-kabel pr. barn
- Bærbar/Chromebook med makecode.microbit.org åben

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 10 min — hvad er en micro:bit, rundvisning i LED-gitteret, knapperne A/B
- 35 min — følg Flashing Heart-tutorialen live på projektoren; børnene følger med på deres egne maskiner
- 10 min — download `.hex`-filen, træk den over på MICROBIT-USB-drevet, se den blinke
- 5 min — take-home-øjeblik: alles board blinker et hjerte

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Gør den til din egen
- 10 min — byt hjertet ud med et andet ikon (`show icon`): and, spøgelse, paraply … prøv nogle stykker
- 10 min — ændr `pause` så det banker hurtigere eller langsommere; find den fart, du bedst kan lide
- 5 min — tilføj `show string` med dit navn, så boardet siger hej først
- 5 min — gå rundt og se på alles boards

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 133" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (heart)</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (small heart)</text>
</svg>
</div>

```javascript
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
})
```

## ✅ Færdig når
- Hjertet på LED'erne bliver ved med at banke (stort hjerte ↔ lille hjerte).

## Noter
_(plads til sessionsnoter, hvad virkede, justeringer af tidsforbrug)_

## Reference
- MakeCodes Tutorials-tilstand (fanen Tutorials på MakeCodes startside) giver trinvise billeder + simulatoranimation — brug den i stedet for et slidedeck
