# Uge 4 — Lydlab (micro:bit V2)

> 🔊 V2-boardet kan **høre** dig og **synge tilbage**. Lav en klap-detektor og en mini-lydmaskine.

**Mål:** brug V2-mikrofonen og -højttaleren: reagér på høje lyde og spil melodier.

## Hvad I bygger

Et klap-aktiveret lysshow plus en knap, der spiller en melodi. (V1-board? Brug hovedtelefon/buzzer på pin 0 og spring mikrofon-delen over.)

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 183" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on loud sound</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (yes)</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play melody dadadum</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">clear screen</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play melody entertainer</text>
</svg>
</div>

```javascript
input.onSound(DetectedSound.Loud, function () {
    basic.showIcon(IconNames.Yes)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle),
        music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    music.play(music.builtinPlayableMelody(Melodies.Entertainer),
        music.PlaybackMode.InBackground)
})
```

## Sessionsforløb (60 min)
- 5 min — V1 vs V2: hvem har hvilket board?
- 20 min — klap-detektor: reagér på høj lyd
- 20 min — tilføj melodier; prøv også `sound level` på et søjlediagram
- 15 min — lyd-dyst: hvis klap-detektor er mest pålidelig?

## ✅ Færdig når
- Et klap får boardet til at reagere.
- En knap spiller en melodi gennem den indbyggede højttaler.

## Noter
_(plads til sessionsnoter)_
