# Week 5 — Radio duel: 2-player reaction game

> ⚡ Two boards, one winner. When the light flashes — smash that button! First one wins the round.

**Goal:** use radio to sync two micro:bits and decide a winner fairly.

## What you’ll build

Both boards wait a random time, flash together, and the first button press wins — announced on both screens.

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 303" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio set group 7</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set armed to false</text>
<rect x="30" y="140" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="135" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if armed → radio send &quot;WIN&quot;</text>
<rect x="30" y="210" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="230.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (happy)</text>
<rect x="30" y="245" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="265.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set armed to false</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#c2185b"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (sad)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set armed to false</text>
</svg>
</div>

```javascript
let armed = false
radio.setGroup(7)
input.onButtonPressed(Button.B, function () {   // referee: start a round
    radio.sendString("GO")
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "GO") {
        basic.pause(randint(1000, 4000))
        basic.showIcon(IconNames.Target)
        armed = true
    } else if (receivedString == "WIN") {
        basic.showIcon(IconNames.Sad)
        armed = false
    }
})
input.onButtonPressed(Button.A, function () {
    if (armed) {
        radio.sendString("WIN")
        basic.showIcon(IconNames.Happy)
        armed = false
    }
})
```

## Session outline (60 min)
- 10 min — recap radio groups; everyone on group 7
- 25 min — build the duel program together
- 15 min — pair up and play best-of-five
- 10 min — why do we need `armed`? (stops early presses winning)

## ✅ Done when
- Both boards flash the target at the same moment.
- The first player to press A sees ✓ and the other sees ✗ — every time.

## Notes
_(space for session notes)_
