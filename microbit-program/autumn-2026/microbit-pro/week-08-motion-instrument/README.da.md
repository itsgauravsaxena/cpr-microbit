# Uge 8 — Bevægelsesinstrument

> 🎵 Vip for at ændre tonehøjden — din micro:bit bliver et musikinstrument, du spiller ved at vifte med det.

**Mål:** omsæt en sensorværdi til et andet interval (`map`) — idéen bag næsten alle fede gadgets.

## Hvad I bygger

Hold A nede og vip: tonen glider op og ned med vinklen. Tilføj lysniveau som lydstyrke, hvis I vil.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 312 203" width="100%" style="max-width:312px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if button A is pressed</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set pitch to map(rotation pitch, -90, 90, 200, 1000)</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone (pitch) for 100 ms</text>
<rect x="30" y="160" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">else stop all sounds</text>
</svg>
</div>

```javascript
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        let pitch = Math.map(input.rotation(Rotation.Pitch), -90, 90, 200, 1000)
        music.playTone(pitch, 100)
    } else {
        music.stopAllSounds()
    }
})
```

## Sessionsforløb (60 min)
- 10 min — hvad gør `map`? (omsætter ét interval til et andet)
- 25 min — byg vippe-thereminen
- 15 min — eksperimentér: ændr intervallet 200–1000, prøv roll i stedet for pitch
- 10 min — minikoncert

## ✅ Færdig når
- At holde A og vippe glider tonehøjden jævnt.
- Slipper man A, stopper lyden.

## Noter
_(plads til sessionsnoter)_
