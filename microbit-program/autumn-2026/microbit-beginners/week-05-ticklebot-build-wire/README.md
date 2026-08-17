# Week 5 — Ticklebot: Build & wire (part 1 of 2)

🤖 Time to build a **robot**! This little guy wiggles when you tickle his foot. Today we build his body and wire him up.

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="a micro:bit robot" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038"><rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/></g>
<g fill="#ff4d4d"><animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/><rect x="17" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/><rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/></g>
</svg>
</div>

**Goal:** start the Ticklebot — a little servo-powered robot that reacts when its foot is tickled. This week is all about building the body and wiring the hardware. Week 6 finishes and personalizes it.

**Official tutorial:** https://makecode.microbit.org/projects/ticklebot

## Materials (whole Ticklebot project, weeks 5-6)
- 1 micro:bit per robot
- 2 small (non-continuous-rotation) servos per robot
- Touch-sensing material: crocodile clip, conductive tape, or similar, wired to a touch pin
- Cardboard/craft materials for the robot's body (arms, legs, decoration)
- Battery pack (servos need external power beyond USB)

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 10 min — show a finished Ticklebot (video or your own build) so kids see the goal
- 40 min — build the cardboard body, wire the two servos and the touch sensor, start the tutorial's code
- 10 min — checkpoint: touch sensor registering, servos twitching in the simulator

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Give it a personality
- 15 min — decorate the body while the glue dries: eyes, arms, hair, a name
- 10 min — test the touch sensor again and again — does it trigger every time? fix loose wires
- 5 min — line up all the half-built robots and take a group photo

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 238" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on pin P0 pressed</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P1 to 180</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P2 to 0</text>
<rect x="30" y="125" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">pause 300 ms</text>
<rect x="30" y="160" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P1 to 90</text>
<rect x="30" y="195" width="250" height="32" rx="7" fill="#7c5e3c"/>
<text x="44" y="215.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">servo write P2 to 90</text>
</svg>
</div>

```javascript
input.onPinPressed(TouchPin.P0, function () {
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 0)
    basic.pause(300)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
})
```

## ✅ Done when
- Touching the foot (pin **0**) makes both servos wiggle, then return to the middle.
- The touch sensor registers reliably.

## Notes
_(space for session notes — this is a fiddlier build, note what took longer than expected)_

## Reference
- makecode.microbit.org/projects/ticklebot has the full parts list and step-by-step tutorial
- Continues next week: [Week 6 — Ticklebot: Finish & personalize](../week-06-ticklebot-finish-personalize/README.md)
