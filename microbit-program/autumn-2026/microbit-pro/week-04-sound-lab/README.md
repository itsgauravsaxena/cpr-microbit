# Week 4 — Sound lab (micro:bit V2)

> 🔊 The V2 board can **hear** you and **sing back**. Make a clap-detector and a mini sound machine.

**Goal:** use the V2 microphone and speaker: react to loud sounds and play melodies.

## What you’ll build

A clap-activated light show, plus a button that plays a tune. (V1 board? Use a headphone/buzzer on pin 0 and skip the microphone part.)

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 183" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on loud sound</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (yes)</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play melody dadadum</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">clear screen</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play melody entertainer</text>
</svg>
</div>

```javascript
input.onSound(DetectedSound.Loud, function () {
    basic.showIcon(IconNames.Yes)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle),
        music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    music.play(music.builtinPlayableMelody(Melodies.Entertainer),
        music.PlaybackMode.InBackground)
})
```

## Session outline (60 min)
- 5 min — V1 vs V2: who has which board?
- 20 min — clap detector: react to loud sound
- 20 min — add melodies; try `sound level` on a bar graph too
- 15 min — sound-off: whose clap detector is most reliable?

## ✅ Done when
- Clapping makes the board react.
- A button plays a melody through the built-in speaker.

## Notes
_(space for session notes)_
