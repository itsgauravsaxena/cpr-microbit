# Week 2 — Data & sensors: live bar graph

> 📊 Your micro:bit can *feel* the room — light, temperature, sound. Today you turn those numbers into a **live graph** on the LEDs.

**Goal:** read real sensor values and visualise them with `plot bar graph`.

## What you’ll build

A light meter that draws a bar graph, plus a button to switch to temperature.

## Example code

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

## Session outline (60 min)
- 5 min — recap: what sensors does a micro:bit have?
- 20 min — build the light bar graph, cover the board with your hand and watch it drop
- 20 min — add the temperature button; try warming the board with your fingers
- 15 min — experiment: whose bar graph reacts fastest? why?

## ✅ Done when
- The bar graph goes up and down as the light changes.
- Button **A** shows the temperature in °C.

## Notes
_(space for session notes)_
