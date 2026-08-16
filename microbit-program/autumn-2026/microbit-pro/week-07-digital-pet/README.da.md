# Uge 7 — Digitalt kæledyr

> 🐣 Din micro:bit lever! Den bliver sulten, den bliver glad, og hvis du ignorerer den … bliver den ked af det. Jeres første program med **tilstand**.

**Mål:** hold styr på tilstand over tid (en variabel, der ændrer sig af sig selv) og brug funktioner til at rydde op i koden.

## Hvad I bygger

Et kæledyr med et humørniveau, der falder langsomt. Tryk A for at fodre, B for at lege. Falder det til nul, falder det i søvn.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 353" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set happy to 5</text>
<rect x="30" y="105" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="100" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="125.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">every 5 seconds</text>
<rect x="30" y="140" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="160.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by -1</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
<rect x="30" y="225" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="220" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="245.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="260" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="280.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by 2 (feed)</text>
<rect x="30" y="295" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="44" y="315.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by 1 (play)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
</svg>
</div>

```javascript
let happy = 5
function showFace() {
    if (happy <= 0) { basic.showIcon(IconNames.Asleep) }
    else if (happy <= 3) { basic.showIcon(IconNames.Sad) }
    else { basic.showIcon(IconNames.Happy) }
}
input.onButtonPressed(Button.A, function () {   // feed
    happy += 2
    showFace()
})
input.onButtonPressed(Button.B, function () {   // play
    happy += 1
    showFace()
})
loops.everyInterval(5000, function () {
    happy += -1
    showFace()
})
```

## Sessionsforløb (60 min)
- 10 min — hvad er 'tilstand'? dit kæledyr husker, hvordan det har det
- 25 min — byg humør, fodring og ansigts-funktionen
- 15 min — tilføj det langsomme fald med `hvert 5. sekund`
- 10 min — personliggør: dine egne ikoner, lyde, et navn

## ✅ Færdig når
- Kæledyrets ansigt ændrer sig, når humøret går op og ned.
- Ignorerer man det et stykke tid, falder det i søvn; fodring vækker det.

## Noter
_(plads til sessionsnoter)_
