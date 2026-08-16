# Uge 2 — Data & sensorer: live søjlediagram

> 📊 Din micro:bit kan *mærke* rummet — lys, temperatur, lyd. I dag laver I tallene om til et **live søjlediagram** på LED'erne.

**Mål:** aflæs rigtige sensorværdier og visualisér dem med `plot bar graph`.

## Hvad I bygger

En lysmåler, der tegner et søjlediagram, plus en knap til at skifte til temperatur.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 148" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">plot bar graph of (light level) up to 255</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number (temperature)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 1000 ms</text>
</svg>
</div>

```javascript
basic.forever(function () {
    led.plotBarGraph(input.lightLevel(), 255)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
    basic.pause(1000)
})
```

## Sessionsforløb (60 min)
- 5 min — opsummering: hvilke sensorer har en micro:bit?
- 20 min — byg lys-søjlediagrammet, hold hånden over boardet og se det falde
- 20 min — tilføj temperatur-knappen; prøv at varme boardet med fingrene
- 15 min — eksperiment: hvis søjlediagram reagerer hurtigst? hvorfor?

## ✅ Færdig når
- Søjlediagrammet går op og ned, når lyset ændrer sig.
- Knap **A** viser temperaturen i °C.

## Noter
_(plads til sessionsnoter)_
