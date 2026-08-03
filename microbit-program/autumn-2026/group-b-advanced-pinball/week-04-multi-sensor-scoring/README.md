# Week 4 — Multi-sensor scoring + game over

**Goal:** 2-3 scoring zones each worth different points, a ball/lives counter, and a **GAME OVER** screen.

## What you'll build
Wire two switches/light sensors to pins **P1** and **P2** as bumpers worth different points, count down from 3 balls, and scroll GAME OVER with the final score.

## Example code
<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 580 318" width="100%" style="max-width:580px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#5c8aa8" />
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8" />
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set score to 0</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set balls to 3</text>
<rect x="30" y="140" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="40" y="135" width="34" height="12" rx="6" fill="#9857c9" />
<text x="44" y="160.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P1 pressed</text>
<rect x="30" y="175" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change score by 10</text>
<rect x="30" y="225" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="40" y="220" width="34" height="12" rx="6" fill="#9857c9" />
<text x="44" y="245.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P2 pressed</text>
<rect x="30" y="260" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="44" y="280.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change score by 50</text>
<rect x="310" y="20" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="320" y="15" width="34" height="12" rx="6" fill="#9857c9" />
<text x="324" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="310" y="55" width="250" height="32" rx="7" fill="#ff8f1a" />
<text x="324" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change balls by -1</text>
<rect x="310" y="90" width="250" height="32" rx="7" fill="#59b04a" />
<text x="324" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if  balls = 0  then</text>
<rect x="326" y="125" width="234" height="32" rx="7" fill="#2a7fff" />
<text x="340" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show string &quot;GAME OVER&quot;</text>
<rect x="326" y="160" width="234" height="32" rx="7" fill="#2a7fff" />
<text x="340" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show number score</text>
<rect x="310" y="125" width="8" height="67" rx="0" fill="#59b04a" />
<rect x="310" y="195" width="250" height="12" rx="6" fill="#59b04a" />
</svg>
</div>

```javascript
let score = 0
let balls = 3
input.onPinPressed(TouchPin.P1, function () {
    score += 10
})
input.onPinPressed(TouchPin.P2, function () {
    score += 50
})
input.onButtonPressed(Button.A, function () {
    balls += -1
    if (balls == 0) {
        basic.showString("GAME OVER")
        basic.showNumber(score)
    }
})
```

!!! tip "Optional stretch — radio scoreboard"
    Fast group? Use a **second micro:bit** as a remote scoreboard. The playfield board radio-sends the score; the scoreboard board shows it. Builds on Group A's *Micro Chat* idea.

    ```javascript
// --- Playfield micro:bit (sends the score) ---
radio.setGroup(1)
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(score)
})

// --- Scoreboard micro:bit (shows the score) ---
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
```

## Session outline (60 min)
- 10 min — recap
- 40 min — wire and program the scoring zones, add a lives/ball counter and the GAME OVER screen
- 10 min — test the full scoring loop (and the radio scoreboard if you tried it)

## ✅ Done when
- The two bumpers (**P1**, **P2**) add **different** amounts of points.
- The ball count goes **down from 3**.
- When balls reach **0**, the board scrolls **GAME OVER** and shows the final score.
- *(Optional stretch)* a second micro:bit shows the score over radio.

## Notes
_(space for session notes)_
