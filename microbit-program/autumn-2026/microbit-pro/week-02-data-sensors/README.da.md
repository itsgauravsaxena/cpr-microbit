# Uge 2 — Data & sensorer: live søjlediagram

> 📊 Din micro:bit kan *mærke* rummet — lys, temperatur, lyd. I dag laver I tallene om til et **live søjlediagram** på LED'erne.

**Mål:** aflæs rigtige sensorværdier og visualisér dem med `plot bar graph`.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="et live søjlediagram der stiger og falder" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.2000;0.4000;0.6000;0.8000" values="1;0;0;0;0"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.2000;0.4000;0.6000;0.8000" values="0;1;0;0;0"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.2000;0.4000;0.6000;0.8000" values="0;0;1;0;0"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.2000;0.4000;0.6000;0.8000" values="0;0;0;1;0"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.2000;0.4000;0.6000;0.8000" values="0;0;0;0;1"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

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

## Sessionsplan (60 min + 20 min pause + 30 min)

### Blok 1 — 60 min
- 5 min — opsummering: hvilke sensorer har en micro:bit?
- 20 min — byg lys-søjlediagrammet, hold hånden over boardet og se det falde
- 20 min — tilføj temperatur-knappen; prøv at varme boardet med fingrene
- 15 min — eksperiment: hvis søjlediagram reagerer hurtigst? hvorfor?

### ☕ Pause — 20 min
Snacks og løbe rundt. Boards bliver på bordet.

### Blok 2 — 30 min · Byg en mørke-alarm
- 20 min — lav grafen om til en **alarm**: lyd + blink, når lyset falder under en grænse
- 5 min — test den som en rigtig enhed — læg den i et skab eller en taske og åbn døren
- 5 min — sammenlign grænseværdier: hvis alarm er mest pålidelig? hvorfor?

## ✅ Færdig når
- Søjlediagrammet går op og ned, når lyset ændrer sig.
- Knap **A** viser temperaturen i °C.

## Sådan virker det

`plot bar graph` tager en **værdi** og et **maksimum** og tegner forholdet hen over alle 25 LED'er. Lysniveau er 0–255, derfor er maksimum 255. Ændrer du maksimum, bliver grafen mere eller mindre følsom.

## Ekstra udfordringer
- Gem det højeste lysniveau, du har set, og vis det på knap B.
- Lav en **mørke-alarm**: spil en lyd, når lyset falder under 50.
- Tegn lydniveauet i stedet (V2-boards).

## Hvis det ikke virker
- Grafen altid fuld? Dit maksimum er for lavt — prøv 255.
- Temperaturen ser for høj ud? Chippen varmer op; den måler boardet, ikke rummet.

## Links & referencer
- Officielle MakeCode-projekter: <https://makecode.microbit.org/projects>
- micro:bit Foundations lektioner & videoer: <https://microbit.org/projects/make-it-code-it/>
- Blok-reference (slå enhver blok op): <https://makecode.microbit.org/reference>

!!! note "Tilføj dit eget link"
    Fundet en god video eller et MakeCode-projekt til denne uge? Indsæt linket her
    (og læg `.hex`-filen eller delelinket i ugens `code/`-mappe).

## Noter
_(plads til sessionsnoter)_
