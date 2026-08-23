# Week 7 — Digital pet

> 🐣 Your micro:bit is alive! It gets hungry, it gets happy, and if you ignore it… it gets sad. Your first program with **state**.

**Goal:** keep track of state over time (a variable that changes by itself) and use functions to tidy your code.

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="a pet face changing happy, sad and asleep" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ff4d4d"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.8s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

## What you’ll build

A pet with a happiness level that drops slowly. Press A to feed, B to play. Let it drop to zero and it falls asleep.

## Example code

Run it right here, then click **Open & edit in MakeCode** to make your own version:

<!-- Paste this week's MakeCode share id below (Share -> Publish gives a link
     like https://makecode.microbit.org/_abc123 -- paste the id or the whole
     link). Until an id is added, this shows a "coming soon" note. -->
```makecode
auto
```

<div style="text-align:center;overflow-x:auto;margin:1rem 0;" markdown="0">
<svg viewBox="0 0 604 353" width="100%" style="max-width:604px;height:auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MakeCode blocks">
<rect x="30" y="20" width="262" height="32" rx="14" fill="#5c8aa8"/>
<rect x="40" y="15" width="34" height="12" rx="6" fill="#5c8aa8"/>
<text x="44" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on start</text>
<rect x="30" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">set happy to 5</text>
<rect x="30" y="105" width="262" height="32" rx="14" fill="#14a3a3"/>
<rect x="40" y="100" width="34" height="12" rx="6" fill="#14a3a3"/>
<text x="44" y="125.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">every 5 seconds</text>
<rect x="30" y="140" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="160.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by -1</text>
<rect x="30" y="175" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="44" y="195.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
<rect x="30" y="225" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="40" y="220" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="44" y="245.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button A pressed</text>
<rect x="30" y="260" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="44" y="280.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by 2 (feed)</text>
<rect x="30" y="295" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="44" y="315.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
<rect x="322" y="20" width="262" height="32" rx="14" fill="#9857c9"/>
<rect x="332" y="15" width="34" height="12" rx="6" fill="#9857c9"/>
<text x="336" y="40.0" font-size="13" fill="#fff" font-weight="700" font-family="system-ui,Segoe UI,sans-serif">on button B pressed</text>
<rect x="322" y="55" width="262" height="32" rx="7" fill="#ff8f1a"/>
<text x="336" y="75.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">change happy by 1 (play)</text>
<rect x="322" y="90" width="262" height="32" rx="7" fill="#8f6ed5"/>
<text x="336" y="110.0" font-size="13" fill="#fff"  font-family="system-ui,Segoe UI,sans-serif">show face</text>
</svg>
</div>

```javascript
let happy = 5
function showFace() {
    if (happy <= 0) { basic.showIcon(IconNames.Asleep) }
    else if (happy <= 3) { basic.showIcon(IconNames.Sad) }
    else { basic.showIcon(IconNames.Happy) }
}
input.onButtonPressed(Button.A, function () {   // feed
    happy += 2
    showFace()
})
input.onButtonPressed(Button.B, function () {   // play
    happy += 1
    showFace()
})
loops.everyInterval(5000, function () {
    happy += -1
    showFace()
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
- 10 min — what is 'state'? your pet remembers how it feels
- 25 min — build happiness, feeding and the face function
- 15 min — add the slow decay with `every 5 seconds`
- 10 min — personalise: your own icons, sounds, a name

### ☕ Break — 20 min
Snacks and running around. Boards stay on the table.

### Block 2 — 30 min · Raise your pet
- 10 min — add a **second need** (hunger with its own timer) or make it sleep when the room goes dark
- 10 min — give it a personality: a name that scrolls, custom faces, a sound when you feed it
- 5 min — pet swap: look after a partner's pet for two minutes without letting it fall asleep
- 5 min — 🎉 **Kahoot quiz** — whole group together

## ✅ Done when
- The pet's face changes as happiness goes up and down.
- Ignoring it for a while makes it fall asleep; feeding wakes it up.

## How it works

**State** just means a variable the program remembers between events. `happy` survives button presses and the timer, so the pet has a memory. The `showFace` **function** keeps you from copying the same three `if`s everywhere.

## Extra challenges
- Add hunger as a second variable with its own timer.
- Make it sleep at 'night' — when the light level is low.
- Give it a name that scrolls when you press A+B.

## If it doesn’t work
- Happiness runs away to 99? Cap it: if it's above 5, set it back to 5.
- Face never updates? Call `showFace()` at the end of *every* block that changes `happy`.

## Links & references
- Official MakeCode projects: <https://makecode.microbit.org/projects>
- micro:bit Foundation lessons & videos: <https://microbit.org/projects/make-it-code-it/>
- Block reference (look up any block): <https://makecode.microbit.org/reference>

!!! note "Add your own link"
    Found a good video or a MakeCode project for this week? Paste the link here
    (and drop the `.hex` or share link into this week's `code/` folder).

## Notes
_(space for session notes)_
