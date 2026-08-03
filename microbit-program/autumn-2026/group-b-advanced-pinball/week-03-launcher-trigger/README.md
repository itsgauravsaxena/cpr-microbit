# Week 3 — Program the launcher/flipper trigger

**Goal:** a button press (or accelerometer tap) fires a **"flip"/"launch"** event with sound + LED feedback.

## What you'll build
Press button **B** and the micro:bit flashes a flipper shape and plays a zap. If you have a servo, make a real flipper swing.

## Example code
```blocks
on button B pressed:          // the flipper / launcher
    show leds:
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
    play tone (High C) for (1/4 beat)
    pause (200) ms
    clear screen
```

Got a servo? Make a real flipper move:

```blocks
on button B pressed:
    servo write pin (P0) to (90)
    pause (300) ms
    servo write pin (P0) to (0)
```

## Session outline (60 min)
- 10 min — recap
- 40 min — program the trigger event; if servos are available, wire one to pin P0 and make a flipper move (search "servo" under makecode.microbit.org/projects for reference blocks)
- 10 min — test

## ✅ Done when
- Pressing **B** flashes a flipper shape and plays a sound.
- The screen clears again afterwards, ready for the next flip.
- *(With a servo)* the flipper physically swings out and returns.

## Notes
If there's no servo, flippers can be simple manual/spring mechanisms — the micro:bit just gives sound/light feedback on the trigger.
