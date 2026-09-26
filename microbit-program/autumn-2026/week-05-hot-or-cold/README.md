# Week 5 — Hot or Cold 🔥❄️

> Back to the treasure hunt! Last week the detector showed **faces**. This week we make it **smarter** — a bar meter, beeps that speed up, "warmer/colder", and a **you found it!** celebration. 💎

!!! abstract "🎓 What you'll learn today"
    - **signal strength** — radio gets weaker with distance
    - **`forever`** loops + **variables** to remember the latest reading
    - **comparing** numbers (`>` / `<`) and a bit of **state** (warmer vs colder)
    - showing data with a **bar graph** and **sound**

<div style="text-align:center;margin:1.25rem 0;" markdown="0">
<svg width="200" height="200" viewBox="0 0 162 162" role="img" aria-label="a radio signal pinging outward" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="162" height="162" rx="20" fill="#0f1419" stroke="#c8a24a" stroke-width="2"/>
<rect x="14" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="14" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="42" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="70" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="98" width="22" height="22" rx="5" fill="#2b3038"/><rect x="14" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="42" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="70" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="98" y="126" width="22" height="22" rx="5" fill="#2b3038"/><rect x="126" y="126" width="22" height="22" rx="5" fill="#2b3038"/><g fill="#ffd23f"><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="70" y="70" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="42" y="42" width="22" height="22" rx="5"/><rect x="70" y="42" width="22" height="22" rx="5"/><rect x="98" y="42" width="22" height="22" rx="5"/><rect x="42" y="70" width="22" height="22" rx="5"/><rect x="98" y="70" width="22" height="22" rx="5"/><rect x="42" y="98" width="22" height="22" rx="5"/><rect x="70" y="98" width="22" height="22" rx="5"/><rect x="98" y="98" width="22" height="22" rx="5"/></g><g opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="1.5s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="14" y="14" width="22" height="22" rx="5"/><rect x="42" y="14" width="22" height="22" rx="5"/><rect x="70" y="14" width="22" height="22" rx="5"/><rect x="98" y="14" width="22" height="22" rx="5"/><rect x="126" y="14" width="22" height="22" rx="5"/><rect x="14" y="42" width="22" height="22" rx="5"/><rect x="126" y="42" width="22" height="22" rx="5"/><rect x="14" y="70" width="22" height="22" rx="5"/><rect x="126" y="70" width="22" height="22" rx="5"/><rect x="14" y="98" width="22" height="22" rx="5"/><rect x="126" y="98" width="22" height="22" rx="5"/><rect x="14" y="126" width="22" height="22" rx="5"/><rect x="42" y="126" width="22" height="22" rx="5"/><rect x="70" y="126" width="22" height="22" rx="5"/><rect x="98" y="126" width="22" height="22" rx="5"/><rect x="126" y="126" width="22" height="22" rx="5"/></g></g>
</svg>
</div>

!!! tip "You need **two** micro:bits + room to move"
    One board is the hidden **treasure** (`BEACON`), the other is the **detector**. Both on the **same group**. Hide the treasure, then hunt! New to this? It started in **[Week 4 — Game Lab](../week-04-game-lab/README.md)**. 🎮

## 💎 The treasure hunt (recap)

The **treasure** beeps out a radio signal; the **detector** shows how close you are with a face. 😢 far → 💗 red-hot.

*🎓 Concept: **signal strength** — a strong signal means the treasure is near.*

??? example "👀 See the two programs"

    **💎 Treasure (transmitter)** — hide this one:

    ```makecode
    auto:beacon
    ```

    **🔍 Detector (faces)** — 😢 cold → 😕 → 😀 → 💗 red-hot:

    ```makecode
    auto:detector
    ```

## 🔬 Make the detector smarter

Keep the **same treasure** (`BEACON`) — just re-flash the **detector** with each new idea. Build up as far as you can! 🌱

??? example "① Signal bar meter 📊"

    Swap faces for a **bar** that fills up the closer you get — more precise than faces.

    ```makecode
    auto:detector-bar
    ```

    *How: a `forever` loop **maps** the signal strength to `0–100` and draws it with `plot bar graph`. Full bar = right on top of it!*

??? example "② Beeps that speed up 🔊"

    Like a real metal detector: slow beeps far away, **frantic** beeps when you're close.

    ```makecode
    auto:detector-beep
    ```

    *How: it stores the latest strength in a **variable**, then a `forever` loop plays a beep and **`pause`s** for a time mapped from the signal — closer = shorter pause = faster beeps.*

??? example "③ Warmer or colder? ↕️"

    The detector **remembers** the last reading and tells you if you're getting **warmer** ⬆️ or **colder** ⬇️.

    ```makecode
    auto:detector-warmer
    ```

    *How: it keeps a `last` variable. Each check compares the new strength to `last`: bigger → ⬆️ warmer, smaller → ⬇️ colder. Remembering the previous value is called **state**.*

??? example "④ You found it! 🏆"

    A proper win: while you search it shows a bar, and when you're **right on top** it flashes ✓ and plays a victory tune.

    ```makecode
    auto:detector-found
    ```

    *How: an `if / else` — if the signal is very strong (`> -48`) celebrate 🎉, otherwise keep showing the search bar.*

??? example "⑤ Hotness number 🔢"

    Show a **number from 0 to 100** — exactly how hot you are.

    ```makecode
    auto:detector-number
    ```

    *How: it **maps** the signal to `0–100` and `rounds` it to a whole number, then `show number`.*

??? example "⑥ Glow brighter 🔆"

    The whole heart **glows brighter** the closer you get — dim when far, dazzling on top.

    ```makecode
    auto:detector-glow
    ```

    *How: `set brightness` is fed the mapped signal (`5–255`), so the LEDs get brighter with a stronger signal.*

??? example "⑦ Rising pitch — theremin 🎼"

    Instead of beeps, a **tone that slides higher** as you approach — like a musical treasure detector.

    ```makecode
    auto:detector-pitch
    ```

    *How: `play tone` gets a **frequency** mapped from the signal (`200 Hz` far → `900 Hz` close), so the pitch rises as you near it.*

??? example "⑧ Race the clock ⏱️"

    Press **A** to start the timer, hunt, and when you reach the treasure it shows **how many seconds** it took. Race your friends!

    ```makecode
    auto:detector-race
    ```

    *How: **A** stores the start time (`running time`); a `forever` loop waits for a strong signal, then shows `(now − start) ÷ 1000` seconds with a victory tune. Uses **state** to remember it started.*

??? example "⑨ Light a real LED 💡"

    Wire a real **LED** to pin **P0** (long leg) and **GND** (short leg): it glows **brighter** the closer you get — a treasure lamp you built yourself! *(A first taste of Week 6's circuits.)*

    ```makecode
    auto:detector-led
    ```

    *How: `analog write pin P0` sends a brightness (`0–1023`) mapped from the signal, so a real LED on P0 dims and brightens like the screen. No LED yet? Watch the **P0** pin light up in the simulator.*

??? note "How signal strength works"

    **Think of it like a shout across a field.** Right next to someone it's **loud**; far away it's **faint**. Radio is the same: `received packet signal strength` is a number that's **bigger (closer to 0) when near** — about `-42` on top of the treasure, down to `-95`+ far away. Every variation above just turns that one number into something you can see or hear.

    **Watch for:** signal strength barely changes in the **simulator** — these really shine on **real boards** with space to walk around. All detectors use the **same group** as the treasure.

## ✅ I did it when…

- ☐ I found the hidden treasure with the **face** detector. 💗
- ☐ I upgraded it to a **bar meter** or **beeps**. 📊🔊
- ☐ *(Legend!)* I built **three or more** detectors — warmer/colder, found-it, glow, theremin, raced the clock, or lit a **real LED**. 🏆💡

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-5
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** go deeper on **one** game — the radio treasure hunt — so kids meet **signal strength**, `forever` loops, variables and simple **state** without a brand-new topic. The treasure program (`BEACON`) never changes; kids just re-flash the **detector** with each smarter version. Great for mixed abilities: everyone gets the faces version working, fast finishers climb the ladder.

    **The ladder (easy → hard):**

    - **Recap** — faces detector (😢→💗). Everyone gets this playing first.
    - **① Bar meter** — `plot bar graph` of the mapped signal. A cleaner readout.
    - **② Beeps speed up** — sound feedback; a variable holds the latest signal so the beep rate is smooth (not tied to packet timing).
    - **③ Warmer/colder** — introduces **state** (a `last` variable compared to the new reading).
    - **④ Found it!** — an `if / else` win condition + a celebration tune.

    **Materials**

    - **≥2 micro:bits** per group + USB (radio + signal strength need **real boards** — the simulator's signal barely moves)
    - **V2** gives a built-in speaker for ② and ④; on V1 use a buzzer on pin 0
    - open floor space and hiding spots for the treasure

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 10 recap how radio & signal strength work → 20 get the **faces treasure hunt** running (hide & seek) → 25 build **① bar meter** and **② beeps** → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 20 **③ warmer/colder** and **④ found-it!** for fast finishers, plus a class treasure-hunt tournament → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens in **Blocks**. `received packet signal strength` ranges ≈ `-42` (touching) to `-128` (far); the variations `map` that to a bar, a beep delay, or an arrow. Coming next: **LEDs & circuits** (Week 6) — lights you wire yourself, toward the Ticklebot and pinball electronics. 💡
