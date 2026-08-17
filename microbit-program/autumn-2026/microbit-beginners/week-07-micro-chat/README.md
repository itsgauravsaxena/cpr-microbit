# Week 7 — Micro Chat (radio, part 1 of 2)

📡 Two micro:bits talking across the room — with no wires! Send secret messages through the air, like walkie-talkies.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="radio waves between micro:bits" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g>
</svg>
</div>

**Goal:** two micro:bits talking to each other over radio — intro to radio messaging. This is the first of a two-week radio project; week 8 builds it into a "find the hidden beacon" game.

**Official tutorial:** https://makecode.microbit.org/projects/micro-chat

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 5 min recap
- 45 min — Micro Chat tutorial: two boards sending messages to each other, intro to radio groups/channels
- 10 min — pair up and test sending messages across the room

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Secret codes
- 10 min — agree on a **secret code** with your partner (1 = hello, 2 = meet me, 3 = look behind you)
- 10 min — **message relay**: stand in a line and pass a message from one end to the other by radio
- 5 min — what happens if two pairs use the same group number? try it and see
- 5 min — 🎉 **Kahoot quiz** — whole group together ([this week's questions](../../quiz/README.md#week-7))

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 198" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio set group 1</text>
<rect x="30" y="105" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="100" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="125.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="140" width="250" height="32" rx="7" fill="#c2185b"/>
<text x="44" y="160.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">radio send string &quot;HI&quot;</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#c2185b"/>
<rect x="320" y="15" width="34" height="12" rx="6" fill="#c2185b"/>
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on radio received</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show string (receivedString)</text>
</svg>
</div>

```javascript
radio.setGroup(1)
input.onButtonPressed(Button.A, function () {
    radio.sendString("HI")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
```

## ✅ Done when
- Two micro:bits on the same **radio group** can send messages.
- Pressing **A** on one makes the message appear on the other.

## Notes
_(space for session notes)_

## Reference
- Radio groups are like walkie-talkie channels — same channel number = same conversation, set in `on start`
- Continues next week: [Week 8 — Heartbeat Beacon](../week-08-heartbeat-beacon/README.md)
