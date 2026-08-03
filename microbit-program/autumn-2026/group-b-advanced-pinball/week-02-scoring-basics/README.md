# Week 2 — Program scoring basics

**Goal:** a button or switch press = **+10 points**, play a sound, and show the score. This is the heart of the whole machine.

**Reference:** https://makecode.microbit.org/projects/love-meter and https://makecode.microbit.org/projects/guess for block-style inspiration

## What you'll build
A `score` variable that starts at 0 and goes up by 10 every time a bumper (button/switch) is hit, with a beep and the number shown on the LEDs.

## Example code
```blocks
on start:
    set score = 0

on button A pressed:          // a bumper / switch is hit
    change score by 10
    play tone (Middle C) for (1/2 beat)
    show number score
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
