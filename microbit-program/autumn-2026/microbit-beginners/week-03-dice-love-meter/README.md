# Week 3 — Dice + Love Meter

🎲 Give it a shake and roll a dice — no dice needed, it all happens in the lights! Then build a **love meter** you power with your own fingers. ⚡

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a micro:bit rolling dice" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="1;0;0;0;0;0"/><rect x="85" y="85" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;1;0;0;0;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;1;0;0;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;0;1;0;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;0;0;1;0"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="3.0s" repeatCount="indefinite" keyTimes="0.0000;0.1667;0.3333;0.5000;0.6667;0.8333" values="0;0;0;0;0;1"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/></g></g>
</svg>
</div>

**Goal:** random numbers (via shake) and touch-pin sensing.

**Official tutorials:**
- https://makecode.microbit.org/projects/dice
- https://makecode.microbit.org/projects/love-meter

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 5 min recap
- 25 min — Dice tutorial (accelerometer + `pick random`)
- 25 min — Love Meter tutorial (touch pins)
- 5 min — share/test

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Dice duel
- 10 min — **dice duel**: shake at the same time as a partner, highest number wins. Best of five
- 10 min — stretch: show **dots** instead of a number (draw them with `show leds`)
- 5 min — try the love meter on the whole table — who has the 'warmest' fingers?
- 5 min — 🎉 **Kahoot quiz** — whole group together ([this week's questions](../../quiz/README.md#week-3))

## Example code

Run it right here, then click **Open & edit in MakeCode** to make your own version:

<!-- Paste this week's MakeCode share id below (Share -> Publish gives a link
     like https://makecode.microbit.org/_abc123 -- paste the id or the whole
     link). Until an id is added, this shows a "coming soon" note. -->
```makecode
auto
```

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 98" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on shake</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number (pick random 1 to 6)</text>
</svg>
</div>

```javascript
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(Math.randomRange(1, 6))
})
```

**Love Meter** (touch pin 0):

```javascript
input.onPinPressed(TouchPin.P0, function () {
    basic.showNumber(Math.randomRange(0, 100))
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
- A shake shows a random number **1–6** (the dice).
- Touching pin **0** shows a random 'love' score 0–100.

## Notes
_(space for session notes)_

## Reference
- Stretch goal for Dice: show dots instead of a number (Graphical Dice variant, linked from the Dice tutorial page)

