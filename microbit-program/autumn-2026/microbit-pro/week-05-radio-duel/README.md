# Week 5 — Radio duel: 2-player reaction game

> ⚡ Two boards, one winner. When the light flashes — smash that button! First one wins the round.

**Goal:** use radio to sync two micro:bits and decide a winner fairly.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="a target flashing then a lightning bolt" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="0;1"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

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

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 10 min — recap radio groups; everyone on group 7
- 25 min — build the duel program together
- 15 min — pair up and play best-of-five
- 10 min — why do we need `armed`? (stops early presses winning)

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Tournament
- 15 min — add **scoring** (first to 5 wins) and run a knockout tournament across the group
- 5 min — show the winner's reaction time in milliseconds
- 5 min — talk it through: why does the `armed` check make the game fair?
- 5 min — 🎉 **Kahoot quiz** — whole group together ([this week's questions](../../quiz/README.md#week-5))

## ✅ Done when
- Both boards flash the target at the same moment.
- The first player to press A sees ✓ and the other sees ✗ — every time.

## How it works

Both boards must be on the **same radio group** or they can't hear each other. The `armed` variable is the referee — it only lets a press count *after* the target appears, so nobody can win by mashing the button early.

## Extra challenges
- Keep score across rounds — first to 5 wins the match.
- Show *how fast* the winner pressed, in milliseconds.
- Punish early presses: press before the target and you lose the round.

## If it doesn’t work
- Boards don't react to each other? Same `radio set group` number on both — check for a typo.
- Both show ✓? Radio messages crossed; add a short `pause` before showing the result.

## Links & references
- Official MakeCode projects: <https://makecode.microbit.org/projects>
- micro:bit Foundation lessons & videos: <https://microbit.org/projects/make-it-code-it/>
- Block reference (look up any block): <https://makecode.microbit.org/reference>

!!! note "Add your own link"
    Found a good video or a MakeCode project for this week? Paste the link here
    (and drop the `.hex` or share link into this week's `code/` folder).

## Notes
_(space for session notes)_
