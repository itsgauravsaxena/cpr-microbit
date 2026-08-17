# Week 6 — Radio multiplayer: rock, paper, scissors

> ✊✋✌️ Shake to choose, radio to compare, and the board tells you who won — a whole-group tournament in one program.

**Goal:** send and compare data between many boards, and write the logic that decides a winner.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="rock, paper and scissors cycling" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## What you’ll build

Shake to pick 0/1/2, send it over radio, compare with your opponent's choice, and show win/lose/draw.

## Example code

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

## Session outline (60 min)
- 10 min — recap sending numbers over radio
- 25 min — build shake-to-choose and send
- 20 min — the winner logic: work out the `(mine + 1) % 3` trick together
- 5 min — class tournament

## ✅ Done when
- A shake picks a symbol and sends it.
- Both players see the correct result: win, lose or draw.

## How it works

Rock (0), paper (1), scissors (2) are just numbers, which makes the winner rule a piece of maths: **`(mine + 1) % 3 == theirs`** means *they* beat you. `%` is 'remainder', which wraps 2 back around to 0.

## Extra challenges
- Let players *choose* with buttons instead of random.
- Best of five with a running score.
- Add a fourth option (lizard!) and work out the new rules.

## If it doesn’t work
- Everyone draws every time? You're comparing your own message — ignore messages you sent yourself.
- Result shows too early? Add a short `pause` so both boards have chosen.

## Links & references
- Official MakeCode projects: <https://makecode.microbit.org/projects>
- micro:bit Foundation lessons & videos: <https://microbit.org/projects/make-it-code-it/>
- Block reference (look up any block): <https://makecode.microbit.org/reference>

!!! note "Add your own link"
    Found a good video or a MakeCode project for this week? Paste the link here
    (and drop the `.hex` or share link into this week's `code/` folder).

## Notes
_(space for session notes)_
