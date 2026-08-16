# Uge 6 — Radio-multiplayer: sten, saks, papir

> ✊✋✌️ Ryst for at vælge, radio for at sammenligne, og boardet fortæller, hvem der vandt — en hel gruppeturnering i ét program.

**Mål:** send og sammenlign data mellem mange boards, og skriv logikken, der afgør vinderen.

## Hvad I bygger

Ryst for at vælge 0/1/2, send det over radio, sammenlign med modstanderens valg, og vis vundet/tabt/uafgjort.

## Eksempelkode

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 183" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on shake</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set mine to pick random 0 to 2</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show my icon</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio send number mine</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#c2185b"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set theirs to receivedNumber</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">compare and show result</text>
</svg>
</div>

```javascript
let mine = 0
let theirs = 0
radio.setGroup(8)
input.onGesture(Gesture.Shake, function () {
    mine = randint(0, 2)                 // 0 rock, 1 paper, 2 scissors
    if (mine == 0) { basic.showIcon(IconNames.Square) }
    else if (mine == 1) { basic.showIcon(IconNames.Yes) }
    else { basic.showIcon(IconNames.Scissors) }
    radio.sendNumber(mine)
})
radio.onReceivedNumber(function (receivedNumber) {
    theirs = receivedNumber
    basic.pause(500)
    if (mine == theirs) {
        basic.showString("=")
    } else if ((mine + 1) % 3 == theirs) {
        basic.showIcon(IconNames.Sad)     // they beat me
    } else {
        basic.showIcon(IconNames.Happy)   // I win
    }
})
```

## Sessionsforløb (60 min)
- 10 min — opsummér at sende tal over radio
- 25 min — byg ryst-for-at-vælge og send
- 20 min — vinder-logikken: regn `(mine + 1) % 3`-tricket ud sammen
- 5 min — klasseturnering

## ✅ Færdig når
- Et ryst vælger et symbol og sender det.
- Begge spillere ser det rigtige resultat: vundet, tabt eller uafgjort.

## Noter
_(plads til sessionsnoter)_
