# Week 2 — Program scoring basics

**Goal:** a button or switch press = **+10 points**, play a sound, and show the score. This is the heart of the whole machine.

**Reference:** https://makecode.microbit.org/projects/love-meter and https://makecode.microbit.org/projects/guess for block-style inspiration

## What you'll build
A `score` variable that starts at 0 and goes up by 10 every time a bumper (button/switch) is hit, with a beep and the number shown on the LEDs.

## Example code
<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 183" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8" />
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8" />
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set score to 0</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="320" y="15" width="34" height="12" rx="6" fill="#9857c9" />
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change score by 10</text>
<rect x="310" y="90" width="250" height="32" rx="7" fill="#d94fb0" />
<text x="324" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone Middle C</text>
<rect x="310" y="125" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="324" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number score</text>
</svg>
</div>

```javascript
let score = 0
input.onButtonPressed(Button.A, function () {
    score += 10
    music.playTone(Note.C, music.beat(BeatFraction.Half))
    basic.showNumber(score)
})
```

## Session outline (60 min)
- 10 min — recap variables
- 40 min — build the program: a `score` variable, +10 on press, a `music` beep, show the score
- 10 min — test in the simulator, then on a real micro:bit with a crocodile-clip switch

## ✅ Done when
- Pressing the button/switch adds **10** to the score.
- A sound plays on every hit.
- The current score shows on the LEDs.
- The score starts at **0** each time the program restarts.

## Notes
_(space for session notes)_
