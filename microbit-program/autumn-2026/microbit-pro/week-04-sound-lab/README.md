# Week 4 — Sound lab (micro:bit V2)

> 🔊 The V2 board can **hear** you and **sing back**. Make a clap-detector and a mini sound machine.

**Goal:** use the V2 microphone and speaker: react to loud sounds and play melodies.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="sound rings expanding" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.2s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.2s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.2s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## What you’ll build

A clap-activated light show, plus a button that plays a tune. (V1 board? Use a headphone/buzzer on pin 0 and skip the microphone part.)

## Example code

Run it right here, then click **Open & edit in MakeCode** to make your own version:

<!-- Paste this week's MakeCode share id below (Share -> Publish gives a link
     like https://makecode.microbit.org/_abc123 -- paste the id or the whole
     link). Until an id is added, this shows a "coming soon" note. -->
```makecode
auto
```

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 183" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on loud sound</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show icon (yes)</text>
<rect x="30" y="90" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="44" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play melody dadadum</text>
<rect x="30" y="125" width="262" height="32" rx="7" fill="#2a7fff"/>
<text x="44" y="145.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">clear screen</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#d94fb0"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">play melody entertainer</text>
</svg>
</div>

```javascript
input.onSound(DetectedSound.Loud, function () {
    basic.showIcon(IconNames.Yes)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle),
        music.PlaybackMode.UntilDone)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    music.play(music.builtinPlayableMelody(Melodies.Entertainer),
        music.PlaybackMode.InBackground)
})
```

!!! tip "▶️ Try it in MakeCode (30 seconds)"
    1. Open <https://makecode.microbit.org> → **New Project**
    2. Click the **`{ } JavaScript`** button at the top
    3. Select everything in the editor and **delete it**, then **paste the code above**
    4. Click **Blocks** to switch back — the real blocks appear, ready to explore
    5. **Download** to put it on a board, or press ▶️ to run it in the simulator

    Kids can do exactly the same to get started, then change things and make it theirs.


## Session plan (60 min + 20 min break + 30 min)

### Block 1 — 60 min
- 5 min — V1 vs V2: who has which board?
- 20 min — clap detector: react to loud sound
- 20 min — add melodies; try `sound level` on a bar graph too
- 15 min — sound-off: whose clap detector is most reliable?

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Noise meter & clap counter
- 10 min — build a **clap counter** (how many claps in 10 seconds?) or a live **noise meter** bar graph
- 10 min — calibrate: find the threshold that ignores talking but catches a clap
- 5 min — loudest-room test — everyone shouts at once, watch the graphs max out
- 5 min — 🎉 **Kahoot quiz** — whole group together

## ✅ Done when
- Clapping makes the board react.
- A button plays a melody through the built-in speaker.

## How it works

`on loud sound` watches the built-in microphone and fires when the level crosses a threshold. You can change how touchy it is with **set loud sound threshold**.

## Extra challenges
- Make a **clap counter** — how many claps in 10 seconds?
- Build a noise meter: `plot bar graph` of `sound level`.
- Compose your own melody instead of a built-in one.

## If it doesn’t work
- Nothing happens on a clap? You need a **V2** board for the microphone — check for the notched logo and gold speaker.
- Too sensitive? Raise the loud-sound threshold.

## Links & references
- Official MakeCode projects: <https://makecode.microbit.org/projects>
- micro:bit Foundation lessons & videos: <https://microbit.org/projects/make-it-code-it/>
- Block reference (look up any block): <https://makecode.microbit.org/reference>

!!! note "Add your own link"
    Found a good video or a MakeCode project for this week? Paste the link here
    (and drop the `.hex` or share link into this week's `code/` folder).

## Notes
_(space for session notes)_
