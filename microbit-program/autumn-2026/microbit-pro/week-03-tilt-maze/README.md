# Week 3 — Motion: tilt maze

> 🎮 Tilt the board and a dot rolls across the screen — like a marble in a tray. This is how real motion controls work!

**Goal:** use the accelerometer to move a sprite — your first game with real physics feel.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="a dot rolling across the screen" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="1;0;0;0;0;0;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;1;0;0;0;0;0;0"/><rect x="98" y="42" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;1;0;0;0;0;0"/><rect x="126" y="14" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;1;0;0;0;0"/><rect x="98" y="42" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;1;0;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;0;1;0;0"/><rect x="42" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;0;0;1;0"/><rect x="14" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.6s" repeatCount="indefinite" keyTimes="0.0000;0.1250;0.2500;0.3750;0.5000;0.6250;0.7500;0.8750" values="0;0;0;0;0;0;0;1"/><rect x="42" y="98" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## What you’ll build

A dot you steer by tilting, plus a target to catch. Catch it and the score goes up.

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 218" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set player to create sprite at 2,2</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set target to create sprite at 4,4</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">player change x by (acceleration X / 300)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#c94f7c"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">player change y by (acceleration Y / 300)</text>
<rect x="322" y="125" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if player touching target → score +1</text>
<rect x="322" y="160" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 100 ms</text>
</svg>
</div>

```javascript
let player = game.createSprite(2, 2)
let target = game.createSprite(4, 4)
basic.forever(function () {
    player.change(LedSpriteProperty.X, input.acceleration(Dimension.X) / 300)
    player.change(LedSpriteProperty.Y, input.acceleration(Dimension.Y) / 300)
    if (player.isTouching(target)) {
        game.addScore(1)
        target.set(LedSpriteProperty.X, randint(0, 4))
        target.set(LedSpriteProperty.Y, randint(0, 4))
    }
    basic.pause(100)
})
```

!!! tip "▶️ Try it in MakeCode (30 seconds)"
    1. Open <https://makecode.microbit.org> → **New Project**
    2. Click the **`{ } JavaScript`** button at the top
    3. Select everything in the editor and **delete it**, then **paste the code above**
    4. Click **Blocks** to switch back — the real blocks appear, ready to explore
    5. **Download** to put it on a board, or press ▶️ to run it in the simulator

    Kids can do exactly the same to get started, then change things and make it theirs.


## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 5 min — recap the accelerometer
- 25 min — build the tilt-controlled dot
- 20 min — add the target and scoring; tune the `/ 300` until it feels right
- 10 min — swap boards and play each other's version

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Make it a real game
- 15 min — add **walls** (flash and reset on the edge) or a **30-second countdown** — your choice
- 5 min — tune the difficulty: change the divisor until it's hard but fair
- 5 min — swap boards and set a high score on someone else's game
- 5 min — 🎉 **Kahoot quiz** — whole group together ([this week's questions](../../quiz/README.md#week-3))

## ✅ Done when
- Tilting the board moves the dot smoothly in all directions.
- Catching the target adds a point and the target jumps somewhere new.

## How it works

`acceleration (X)` is roughly −1023…1023. Dividing by 300 turns that into a small step like −3…3 — that division is your **speed control**. Smaller number = faster and twitchier.

## Extra challenges
- Add walls: if the player hits an edge, flash and reset to the middle.
- Add a countdown — how many targets in 30 seconds?
- Two targets at once: one worth 1 point, one worth 5.

## If it doesn’t work
- Dot flies off instantly? Increase the divisor (try 500).
- Dot won't move? Check you used `change x by`, not `set x to`.

## Links & references
- Official MakeCode projects: <https://makecode.microbit.org/projects>
- micro:bit Foundation lessons & videos: <https://microbit.org/projects/make-it-code-it/>
- Block reference (look up any block): <https://makecode.microbit.org/reference>

!!! note "Add your own link"
    Found a good video or a MakeCode project for this week? Paste the link here
    (and drop the `.hex` or share link into this week's `code/` folder).

## Notes
_(space for session notes)_
