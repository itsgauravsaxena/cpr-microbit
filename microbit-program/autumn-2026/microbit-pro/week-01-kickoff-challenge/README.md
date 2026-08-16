# Week 1 — Kickoff & code challenge

> 🏴‍☠️ Welcome to Pro! You already know the basics — this term is about **bigger ideas**: sensors, data, motion, sound, radio and your own inventions. First, a warm-up challenge.

**Goal:** warm up, agree on how we work (share your code every week), and beat a small code challenge.

## What you’ll build

A **secret-number guessing game**: the micro:bit picks a number, you press A to guess lower / B higher, and it tells you when you're right.

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 268" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set secret to pick random 1 to 20</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set guess to 10</text>
<rect x="30" y="140" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="135" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change guess by -1</text>
<rect x="30" y="210" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="230.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number guess</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change guess by 1</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number guess</text>
<rect x="322" y="140" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="135" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A+B pressed</text>
<rect x="322" y="175" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if guess = secret → show yes</text>
<rect x="322" y="210" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="336" y="230.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">else → show no</text>
</svg>
</div>

```javascript
let secret = randint(1, 20)
let guess = 10
input.onButtonPressed(Button.A, function () {
    guess += -1
    basic.showNumber(guess)
})
input.onButtonPressed(Button.B, function () {
    guess += 1
    basic.showNumber(guess)
})
input.onButtonPressed(Button.AB, function () {
    if (guess == secret) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
```

## Session outline (60 min)
- 5 min — welcome, what Pro is about, look at the 10-week map
- 15 min — challenge: can you make the guessing game on your own?
- 30 min — build it together, compare solutions
- 10 min — export your .hex and save it in `code/`

## ✅ Done when
- A and B change the guess, and A+B shows ✓ or ✗ correctly.
- Everyone has saved their project to `code/`.

## Notes
_(space for session notes)_
