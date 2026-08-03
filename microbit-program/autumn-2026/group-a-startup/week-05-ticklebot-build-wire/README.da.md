# Uge 5 — Ticklebot: Byg & ledningsføring (del 1 af 2)

🤖 Nu bygger vi en **robot**! Den lille fyr vrikker, når du kilder hans fod. I dag bygger vi kroppen og laver ledningerne.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="en micro:bit-robot" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

**Mål:** gå i gang med Ticklebot — en lille servodreven robot, der reagerer, når man kilder dens fod. Denne uge handler udelukkende om at bygge kroppen og forbinde hardwaren. Uge 6 færdiggør og personliggør den.

**Officiel tutorial:** https://makecode.microbit.org/projects/ticklebot

## Materialer (hele Ticklebot-projektet, uge 5-6)
- 1 micro:bit pr. robot
- 2 små servoer (ikke kontinuerlig rotation) pr. robot
- Berøringsfølsomt materiale: krokodillenæb, ledende tape eller lignende, forbundet til en berøringspin
- Pap/hobbymaterialer til robottens krop (arme, ben, pynt)
- Batteripakke (servoer kræver ekstern strøm ud over USB)

## Sessionsforløb (60 min)
- 10 min — vis en færdig Ticklebot (video eller dit eget byg), så børnene ser målet
- 40 min — byg pap-kroppen, forbind de to servoer og berøringssensoren, gå i gang med tutorialens kode
- 10 min — tjekpunkt: berøringssensoren registrerer, servoerne dirrer i simulatoren

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 238" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P0 pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P1 to 180</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P2 to 0</text>
<rect x="30" y="125" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 300 ms</text>
<rect x="30" y="160" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P1 to 90</text>
<rect x="30" y="195" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="215.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P2 to 90</text>
</svg>
</div>

```javascript
input.onPinPressed(TouchPin.P0, function () {
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 0)
    basic.pause(300)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
})
```

## ✅ Færdig når
- Berøring af foden (pin **0**) får begge servoer til at vrikke og vende tilbage til midten.
- Berøringssensoren registrerer pålideligt.

## Noter
_(plads til sessionsnoter — dette er et mere fumlet byg, notér hvad der tog længere end forventet)_

## Reference
- makecode.microbit.org/projects/ticklebot har den fulde materialeliste og trinvise tutorial
- Fortsætter næste uge: [Uge 6 — Ticklebot: Færdiggør & personliggør](../week-06-ticklebot-finish-personalize/README.md)
