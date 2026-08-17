# Week 8 — Motion instrument

> 🎵 Tilt to change the pitch — your micro:bit becomes a musical instrument you play by waving it around.

**Goal:** map a sensor value onto another range (`map`) — the idea behind almost every cool gadget.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="a music note bouncing" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="1;0"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="70" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="0.9s" repeatCount="indefinite" keyTimes="0.0000;0.5000" values="0;1"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## What you’ll build

Hold A and tilt: the tone slides up and down with the angle. Add light level for volume if you want.

## Example code

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 312 203" width="100%" style="max-width:312px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">forever</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#59b04a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">if button A is pressed</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set pitch to map(rotation pitch, -90, 90, 200, 1000)</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play tone (pitch) for 100 ms</text>
<rect x="30" y="160" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="180.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">else stop all sounds</text>
</svg>
</div>

```javascript
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        let pitch = Math.map(input.rotation(Rotation.Pitch), -90, 90, 200, 1000)
        music.playTone(pitch, 100)
    } else {
        music.stopAllSounds()
    }
})
```

## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 10 min — what does `map` do? (turn one range into another)
- 25 min — build the tilt theremin
- 15 min — experiment: change the 200–1000 range, try roll instead of pitch
- 10 min — mini concert

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Concert
- 15 min — upgrade your instrument: light level for volume, or snap the pitch to a real scale
- 10 min — practise a short tune with a partner (one plays rhythm, one plays melody)
- 5 min — mini concert — every pair performs 20 seconds

## ✅ Done when
- Holding A and tilting slides the pitch smoothly.
- Letting go of A stops the sound.

## How it works

`map` converts one range into another: tilt is −90…90 degrees, and we stretch that onto 200…1000 Hz. Every 'smart' gadget does this — take a sensor's range, map it onto something useful.

## Extra challenges
- Use light level for volume while tilt controls pitch.
- Snap to real notes instead of a smooth slide (a scale).
- Record a short tune by saving the notes into a list.

## If it doesn’t work
- No sound on a V1 board? Clip a buzzer or headphones to **pin 0** and **GND**.
- Sound never stops? Make sure `stop all sounds` is in the `else` branch.

## Links & references
- Official MakeCode projects: <https://makecode.microbit.org/projects>
- micro:bit Foundation lessons & videos: <https://microbit.org/projects/make-it-code-it/>
- Block reference (look up any block): <https://makecode.microbit.org/reference>

!!! note "Add your own link"
    Found a good video or a MakeCode project for this week? Paste the link here
    (and drop the `.hex` or share link into this week's `code/` folder).

## Notes
_(space for session notes)_
