# Uge 6 — Ticklebot: Færdiggør & personliggør (del 2 af 2)

🤖 Væk din robot til live! Færdiggør koden, giv den rulleøjne, og se den vrikke, når den bliver kildet. 🎨

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="en micro:bit-robot" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

**Mål:** færdiggør den Ticklebot, der blev påbegyndt i uge 5 — færdiggør koden, test på den rigtige robot, og pynt den.

**Officiel tutorial:** https://makecode.microbit.org/projects/ticklebot

**Fortsætter fra:** [Uge 5 — Ticklebot: Byg & ledningsføring](../week-05-ticklebot-build-wire/README.md). Samme materialer som i uge 5 (de igangværende robotter, servoer, berøringssensor, batteripakker); tilføj hobby-/pyntematerialer (rulleøjne, maling osv.).

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min opsummering
- 35 min — færdiggør tutorial-koden, download og test på den rigtige robot
- 15 min — pynt/personliggør (rulleøjne, maling osv.) og fri leg
- 5 min — del med gruppen

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Robot-legetid
- 15 min — **kildefest**: prøv alle robotter i lokalet, find den sjoveste reaktion
- 10 min — tilføj ét trick mere: en lyd eller et ansigt på LED'erne, når den bliver kildet
- 5 min — robotparade — alle viser deres robot med én sætning

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 308" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P0 pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (surprised)</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P1 to 180</text>
<rect x="30" y="125" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P2 to 0</text>
<rect x="30" y="160" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 300 ms</text>
<rect x="30" y="195" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="215.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P1 to 90</text>
<rect x="30" y="230" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="250.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P2 to 90</text>
<rect x="30" y="265" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="285.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (happy)</text>
</svg>
</div>

```javascript
input.onPinPressed(TouchPin.P0, function () {
    basic.showIcon(IconNames.Surprised)
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 0)
    basic.pause(300)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
    basic.showIcon(IconNames.Happy)
})
```

## ✅ Færdig når
- Når man kilder foden, reagerer Ticklebot med et ansigt (overrasket → glad) **og** vrikker.
- Den færdige robot er pyntet og kører på USB/batteri.

## Noter
_(plads til sessionsnoter)_

## Reference
- makecode.microbit.org/projects/ticklebot har den fulde materialeliste og trinvise tutorial
