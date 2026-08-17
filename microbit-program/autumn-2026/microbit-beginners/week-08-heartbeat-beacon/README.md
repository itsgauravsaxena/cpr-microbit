# Week 8 — Heartbeat Beacon (radio, part 2 of 2)

💗 One micro:bit hides and whispers *hello* on the radio; the other hunts for it — getting **warmer** as it gets closer. A treasure hunt with light!

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a pulsing radio beacon" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><g><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="85" y="85" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g></g>
</svg>
</div>

**Goal:** build on last week's radio basics — one micro:bit broadcasts a low-power "hello" on a radio channel, the other detects it and shows a heart when nearby. Then turn it into a hide-and-seek beacon-hunt game.

**Official tutorial:** https://microbit.org/projects/make-it-code-it/heartbeat-beacon/

**Picking up from:** [Week 7 — Micro Chat](../week-07-micro-chat/README.md).

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 5 min recap of radio basics from week 7
- 35 min — Heartbeat Beacon tutorial: one micro:bit broadcasts a low-power "hello" on a radio channel, the other detects it and shows a heart when nearby
- 15 min — turn it into a game: hide the transmitter micro:bit somewhere in the room, kids use the receiver to "hunt" for it (getting warmer as the signal strengthens)
- 5 min — wrap up

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · The big beacon hunt
- 15 min — the real hunt: a volunteer hides the transmitter, everyone hunts with receivers. Play three rounds, hide it better each time
- 5 min — hunters' tips: what made it easier to find? (turn slowly, watch the pattern)
- 5 min — swap roles so everyone gets to hide it once
- 5 min — 🎉 **Kahoot quiz** — whole group together ([this week's questions](../../quiz/README.md#week-8))

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 183" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio set group 1</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#c2185b"/>
<rect x="320" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (heart)</text>
<rect x="310" y="90" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 200 ms</text>
<rect x="310" y="125" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">clear screen</text>
</svg>
</div>

```javascript
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    basic.showIcon(IconNames.Heart)
    basic.pause(200)
    basic.clearScreen()
})
```

**Transmitter** (the hidden beacon):

```javascript
radio.setGroup(1)
basic.forever(function () {
    radio.sendNumber(1)
    basic.pause(1000)
})
```

!!! tip "▶️ Try it in MakeCode (30 seconds)"
    1. Open <https://makecode.microbit.org> → **New Project**
    2. Click the **`{ } JavaScript`** button at the top
    3. Select everything in the editor and **delete it**, then **paste the code above**
    4. Click **Blocks** to switch back — the real blocks appear, ready to explore
    5. **Download** to put it on a board, or press ▶️ to run it in the simulator

    Kids can do exactly the same to get started, then change things and make it theirs.


## ✅ Done when
- The transmitter keeps sending a signal on the radio group.
- The receiver shows a heart whenever it hears the beacon — closer = more often.

## Notes
_(space for session notes)_

## Reference
- Radio groups are like walkie-talkie channels — same channel number = same conversation, set in `on start`
