# Week 9 — Step Counter + Coin Toss

👟 Turn your micro:bit into a step counter, then flip a coin with a shake — heads or tails? 🪙

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a flipping coin" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><g><animate attributeName="opacity" calcMode="discrete" dur="1.0s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="1;0"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/></g><g><animate attributeName="opacity" calcMode="discrete" dur="1.0s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="0;1"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/></g></g>
</svg>
</div>

**Goal:** consolidation week pulling together sensors, variables, and randomness so everyone finishes the program at a solid, consistent level.

**Official tutorials:**
- https://makecode.microbit.org/projects/step-counter
- https://makecode.microbit.org/projects/coin-toss

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 5 min recap of the whole program so far
- 25 min — Step Counter tutorial
- 25 min — Coin Toss tutorial
- 5 min — share/test

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Step challenge
- 10 min — **step challenge**: strap on the board and walk a lap — does the count match your real steps?
- 10 min — cheat test: can you shake it to add fake steps? how would you stop that?
- 5 min — coin toss to decide something silly for the group (who demos first next week)
- 5 min — 🎉 **Kahoot quiz** — whole group together

## Example code

Run it right here, then click **Open & edit in MakeCode** to make your own version:

<!-- Paste this week's MakeCode share id below (Share -> Publish gives a link
     like https://makecode.microbit.org/_abc123 -- paste the id or the whole
     link). Until an id is added, this shows a "coming soon" note. -->
```makecode
auto
```

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 148" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set steps to 0</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="320" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on shake</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#ff8f1a"/>
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change steps by 1</text>
<rect x="310" y="90" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="324" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number steps</text>
</svg>
</div>

```javascript
let steps = 0
input.onGesture(Gesture.Shake, function () {
    steps += 1
    basic.showNumber(steps)
})
```

**Coin Toss** (heads ✓ or tails ✗):

```javascript
input.onGesture(Gesture.Shake, function () {
    if (Math.randomRange(0, 1) == 0) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
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
- **Step Counter**: each shake adds 1 and shows the count.
- **Coin Toss**: a shake shows heads (✓) or tails (✗).

## Notes
_(space for session notes)_

