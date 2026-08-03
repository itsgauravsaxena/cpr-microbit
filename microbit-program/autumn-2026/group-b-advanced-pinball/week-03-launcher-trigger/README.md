# Week 3 — Program the launcher/flipper trigger

**Goal:** a button press (or accelerometer tap) fires a **"flip"/"launch"** event with sound + LED feedback.

## What you'll build
Press button **B** and the micro:bit flashes a flipper shape and plays a zap. If you have a servo, make a real flipper swing.

## Example code
<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 203" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9" />
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9" />
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show leds</text>
<rect x="248" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="61" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="268" y="61" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="248" y="66" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="66" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="66" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="66" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="268" y="66" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="248" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="253" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="258" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="268" y="71" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="248" y="76" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="76" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="76" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="76" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="268" y="76" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="248" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="253" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="258" y="81" width="4" height="4" rx="1" fill="#ffffff" />
<rect x="263" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="268" y="81" width="4" height="4" rx="1" fill="#ffffff33" />
<rect x="30" y="90" width="250" height="32" rx="7" fill="#d94fb0" />
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone High C</text>
<rect x="30" y="125" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 200 ms</text>
<rect x="30" y="160" width="250" height="32" rx="7" fill="#2a7fff" />
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">clear screen</text>
</svg>
</div>

```javascript
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
        `)
    music.playTone(Note.C5, music.beat(BeatFraction.Quarter))
    basic.pause(200)
    basic.clearScreen()
})
```

Got a servo? Make a real flipper move:

```javascript
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P0, 90)
    basic.pause(300)
    pins.servoWritePin(AnalogPin.P0, 0)
})
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
