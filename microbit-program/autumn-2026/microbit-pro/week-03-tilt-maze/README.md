# Week 3 — Motion: tilt maze

> 🎮 Tilt the board and a dot rolls across the screen — like a marble in a tray. This is how real motion controls work!

**Goal:** use the accelerometer to move a sprite — your first game with real physics feel.

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

## Session outline (60 min)
- 5 min — recap the accelerometer
- 25 min — build the tilt-controlled dot
- 20 min — add the target and scoring; tune the `/ 300` until it feels right
- 10 min — swap boards and play each other's version

## ✅ Done when
- Tilting the board moves the dot smoothly in all directions.
- Catching the target adds a point and the target jumps somewhere new.

## Notes
_(space for session notes)_
