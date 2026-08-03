# Week 4 — Multi-sensor scoring + game over

**Goal:** 2-3 scoring zones each worth different points, a ball/lives counter, and a **GAME OVER** screen.

## What you'll build
Wire two switches/light sensors to pins **P1** and **P2** as bumpers worth different points, count down from 3 balls, and scroll GAME OVER with the final score.

## Example code
```blocks
on start:
    set score = 0
    set balls = 3

on pin P1 pressed:            // low bumper
    change score by 10

on pin P2 pressed:            // top bumper — worth more!
    change score by 50

on button A pressed:          // the ball drained out
    change balls by -1
    if balls = 0 then:
        show string "GAME OVER"
        show number score
```

!!! tip "Optional stretch — radio scoreboard"
    Fast group? Use a **second micro:bit** as a remote scoreboard. The playfield board radio-sends the score; the scoreboard board shows it. Builds on Group A's *Micro Chat* idea.

    ```blocks
// --- Playfield micro:bit (sends the score) ---
on start:
    radio set group (1)
on button B pressed:
    radio send number (score)

// --- Scoreboard micro:bit (shows the score) ---
on start:
    radio set group (1)
on radio received (receivedNumber):
    show number (receivedNumber)
```

## Session outline (60 min)
- 10 min — recap
- 40 min — wire and program the scoring zones, add a lives/ball counter and the GAME OVER screen
- 10 min — test the full scoring loop (and the radio scoreboard if you tried it)

## Notes
_(space for session notes)_
