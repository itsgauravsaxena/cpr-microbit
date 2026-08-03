# Week 1 — Flashing Heart (solo project)

> **Meet your micro:bit!** 💛 It's a tiny computer with **25 little lights**. Right now it's fast asleep… let's wake it up and teach it to show a **beating heart!**

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="230" height="230" viewBox="0 0 196 196" role="img" aria-label="A micro:bit blinking a heart" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="196" height="196" rx="22" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<g fill="#2b3038">
<rect x="17" y="17" width="26" height="26" rx="6"/><rect x="51" y="17" width="26" height="26" rx="6"/><rect x="85" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/><rect x="153" y="17" width="26" height="26" rx="6"/>
<rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/>
<rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/>
<rect x="17" y="119" width="26" height="26" rx="6"/><rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/><rect x="153" y="119" width="26" height="26" rx="6"/>
<rect x="17" y="153" width="26" height="26" rx="6"/><rect x="51" y="153" width="26" height="26" rx="6"/><rect x="85" y="153" width="26" height="26" rx="6"/><rect x="119" y="153" width="26" height="26" rx="6"/><rect x="153" y="153" width="26" height="26" rx="6"/>
</g>
<g fill="#ff4d4d">
<animate attributeName="opacity" values="1;0.25;1" dur="1.1s" repeatCount="indefinite"/>
<rect x="51" y="17" width="26" height="26" rx="6"/><rect x="119" y="17" width="26" height="26" rx="6"/>
<rect x="17" y="51" width="26" height="26" rx="6"/><rect x="51" y="51" width="26" height="26" rx="6"/><rect x="85" y="51" width="26" height="26" rx="6"/><rect x="119" y="51" width="26" height="26" rx="6"/><rect x="153" y="51" width="26" height="26" rx="6"/>
<rect x="17" y="85" width="26" height="26" rx="6"/><rect x="51" y="85" width="26" height="26" rx="6"/><rect x="85" y="85" width="26" height="26" rx="6"/><rect x="119" y="85" width="26" height="26" rx="6"/><rect x="153" y="85" width="26" height="26" rx="6"/>
<rect x="51" y="119" width="26" height="26" rx="6"/><rect x="85" y="119" width="26" height="26" rx="6"/><rect x="119" y="119" width="26" height="26" rx="6"/>
<rect x="85" y="153" width="26" height="26" rx="6"/>
</g>
</svg>
</div>

!!! tip "▶️ See it come alive"
    Open the [Flashing Heart tutorial](https://makecode.microbit.org/projects/flashing-heart) and press **▶️ play** in the on-screen simulator — the heart beats on the screen before you even touch a real micro:bit. Then make **your** board do it! ✨

**Goal:** get comfortable with the MakeCode editor and the download-to-board workflow. No rush — this is the only single-project week.

**Official tutorial:** https://makecode.microbit.org/projects/flashing-heart

## Materials
- 1 micro:bit + USB cable per kid
- Laptop/Chromebook with makecode.microbit.org open

## Session outline (60 min)
- 10 min — what's a micro:bit, tour of the LED grid, buttons A/B
- 35 min — follow the Flashing Heart tutorial live on the projector; kids follow along on their own machines
- 10 min — download the `.hex` file, drag it onto the MICROBIT USB drive, watch it flash
- 5 min — take-home moment: everyone's board blinking a heart

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 300 133" width="100%" style="max-width:300px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="250" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="30" y="55" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (heart)</text>
<rect x="30" y="90" width="250" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (small heart)</text>
</svg>
</div>

```javascript
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
})
```

## ✅ Done when
- The heart on the LEDs keeps beating (big heart ↔ small heart), forever.

## Notes
_(space for session notes, what worked, timing adjustments)_

## Reference
- MakeCode Tutorials mode (Tutorials tab on the MakeCode home page) gives step-by-step pictures + simulator animation — use it instead of a slide deck

