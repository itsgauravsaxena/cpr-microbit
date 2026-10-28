# Week 8 — Servo Moves 🤖

> Today things start to **move**! Meet the **servo motor**, make it wave, nod and dance — and give it a **paper costume**. It's also the start of our **final project**: a cardboard robot that moves, lights up and makes sounds. 🎉

!!! abstract "🎓 What you'll learn today"
    - **servos** — a small motor that turns to an **angle** from **0°** to **180°**
    - **wiring** — three wires: **brown → G**, **red → V**, **orange → S**
    - **movement in code** — `set angle`, loops for smooth moves, and sensors (tilt, light, touch) that steer the servo
    - **design** — plan your own robot on paper

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="240" height="190" viewBox="0 0 240 190" role="img" aria-label="a servo waving a paper hand" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<path d="M20 130 C 40 130, 40 150, 62 150" fill="none" stroke="#6d4c41" stroke-width="4"/>
<path d="M20 138 C 40 138, 40 156, 62 156" fill="none" stroke="#e53935" stroke-width="4"/>
<path d="M20 146 C 40 146, 40 162, 62 162" fill="none" stroke="#fb8c00" stroke-width="4"/>
<rect x="50" y="122" width="150" height="16" rx="4" fill="#1565c0"/>
<rect x="62" y="110" width="126" height="64" rx="8" fill="#1e88e5"/>
<text x="150" y="150" text-anchor="middle" fill="#fff" font-size="15" font-weight="700">SERVO</text>
<circle cx="96" cy="110" r="14" fill="#fff" stroke="#90a4ae" stroke-width="2"/>
<g>
<animateTransform attributeName="transform" type="rotate" values="-50 96 110;50 96 110;-50 96 110" dur="1.6s" repeatCount="indefinite"/>
<rect x="90" y="40" width="12" height="72" rx="6" fill="#fff" stroke="#90a4ae" stroke-width="2"/>
<text x="96" y="40" text-anchor="middle" font-size="34">✋</text>
</g>
<circle cx="96" cy="110" r="4" fill="#90a4ae"/>
</svg>
</div>

## 🏆 Our final project starts today

In the **last class** everyone shows a robot they built themselves. Here's the plan:

| Week | What we do |
|---|---|
| **8 — today** | Learn the **servo** + fun moves, then **design** your robot on paper ✏️ |
| **9** | **Build** the body from cardboard and wire up the servo(s) ✂️ |
| **10** | Bring it **alive** — LEDs 💡, sounds 🔊, touch / light / tilt sensors |
| **11** | 🎉 **Showcase** — show your robot to everyone |

**Rules:** paper, cardboard, tape, glue, string and paper clips — **no plastic** (apart from the electronics). ♻️

??? tip "💡 Robot ideas to get you thinking"
    - 🤖 **Ticklebot** — tickle its foot and it wiggles and giggles
    - 👋 **Waving robot** — says hi when you press a button
    - 🐶 **Nodding dog** — nods when you tilt it or clap
    - 👾 **Hungry monster** — the jaw chomps open and shut
    - 🦋 **Flapping butterfly / bird** — wings on two servos
    - 🌻 **Sunflower** — opens in the light, closes in the dark
    - 🎯 **Decision robot** — points at "Yes / No / Maybe"

## 🔌 Meet the servo

Our servo is the **micro servo 9g (SG90)** — a little blue motor that doesn't spin round and round — it turns to an **angle** you choose, from **0°** to **180°**, and **stays there**. The white plastic arm on top is the **horn** — that's where your cardboard parts go.

!!! tip "Wiring a servo 🔌"
    Plug the servo's three-wire plug into the **[sensor shield](../gear/README.md)** at pin **P1**:

    - 🟤 **brown** (or black) → **G** (ground)
    - 🔴 **red** → **V** (power)
    - 🟠 **orange** (or yellow) → **S** (signal)

    Read the little letters on the board — and check the colours match before you switch on!

!!! warning "Before you start ⚠️"
    - **Don't twist the arm by hand** — it can break the gears inside. Let the code move it.
    - The SG90 is made for about **5 V**, but the micro:bit gives about **3 V** — so on USB **one servo** works but can be a bit weak or slow. If the micro:bit **restarts** or the servo **shakes**, ask for a **battery pack**.
    - Building your own project in MakeCode? Add the servo blocks: **Extensions → search "servo"**. (The programs on this page already have them.)

## 🎛️ Part 1 — First moves

### Point with the buttons · P1

**A** → 0°, **B** → 180°, **A + B** → 90° (the middle). Watch where the arm goes!

??? example "👀 See the program"

    ```makecode
    auto:servo-buttons
    ```

    *🎓 Concept: `servo P1 set angle to 90` — the servo turns to that angle and stays.*

### Wave back and forth · P1

A `forever` loop: 0°, wait, 180°, wait… like a windscreen wiper. 🚗

??? example "👀 See the program"

    ```makecode
    auto:servo-sweep
    ```

    *Try it: change `pause 1000` to `300`. Or use 45° and 135° for a smaller wave.*

### Slow and smooth · P1

Instead of jumping, the arm moves **5° at a time** — slow and smooth, like a robot in a film. 🎬

??? example "👀 See the program"

    ```makecode
    auto:servo-slow
    ```

    *How: a `for` loop counts 0 → 36 and sets the angle to `index × 5` (0° → 180°); a second loop goes back. Change `pause 30` to make it faster or slower.*

### Steer by tilting · P1

Tilt the micro:bit left and right — the servo **follows**! Like a steering wheel. 🎡

??? example "👀 See the program"

    ```makecode
    auto:servo-tilt
    ```

    *How: `acceleration x` goes from about −1023 (tilted left) to 1023 (tilted right), and `map` turns that into 0°–180°.*

## ✂️ Part 2 — Give it a paper costume

Now tape something **paper** onto the horn — and give your servo a job!

??? example "👋 Waving hand · P1"

    Cut out a **paper hand** and tape it to the arm. Press **A** → it waves hello 3 times. 👋

    ```makecode
    auto:servo-wave
    ```

    *Try it: wave 5 times? Faster? Show a different face?*

??? example "🌻 Sunflower · P1 — *remember the light sensor?*"

    Make a **paper flower** (or a sun) on the arm. In the **light** it stands up and opens 🌞; **cover the screen** and it goes to sleep 😴.

    ```makecode
    auto:servo-flower
    ```

    *Just like the Halloween ghost: the **screen** is the light sensor. Always asleep? Your room is darker than **50** — change `50` to **20**.*

??? example "🎯 Decision spinner · P1"

    Draw a **half-circle dial** on cardboard: *Yes · No · Maybe · Ask again* 🤔. Press **A** → the arm wobbles, ticks… and stops on an answer!

    ```makecode
    auto:servo-spinner
    ```

    *How: `pick random 0 to 180` gives a random angle. Make your own dial — "Who goes first?", "What's for dinner?", "Which game?"*

??? example "🤖 Tickle me! · P1 + touch P2"

    A first taste of the **Ticklebot**: touch **P2** (and hold **G**) → a giggle and a wiggle! 😆 Tape a piece of **foil** onto the end of a wire on **P2** to make a "foot".

    ```makecode
    auto:servo-tickle
    ```

    *How: `on pin P2 pressed` works just like the tickle counter in Week 7 — now it moves a servo instead.*

## 🚀 Level up — two servos & remote control

??? example "💃 Robot dance · P1 + P2"

    Plug a **second servo** into **P2**. Press **A** → music + a dance: arms swing in opposite directions, then wave together! 🎶

    ```makecode
    auto:servo-dance
    ```

    *Two servos may need a **battery pack**. Try making two paper arms or two wings!*

??? example "🎮 Remote-control arm · radio · P1"

    Work with a **partner**: both download this. **Hold A and tilt** → **your partner's** servo moves! 📡

    ```makecode
    auto:servo-remote
    ```

    *Important: each pair changes `radio set group 8` to **their own number** (like Week 4), or you'll steer everyone's servos!*

## ✏️ Design your robot

Grab a sheet of paper and plan your final project. Draw it and answer:

1. **What's its name?** 🏷️
2. **What moves?** (an arm, a head, a mouth, wings…) — that's your **servo** 🔧
3. **What lights up?** (eyes, a heart, a nose…) — your **LEDs** 💡
4. **What sound does it make?** 🔊
5. **What makes it react?** (a button, a touch, light, tilt, shake…) 👆
6. **What do I need to bring?** (boxes, toilet rolls, paper, string…) 📦

Keep your drawing — you'll build it next week! 🛠️

## ✅ I did it when…

- ☐ I wired a **servo** (brown → G, red → V, orange → S) and moved it with **buttons**. 🔌
- ☐ I made it **sweep** — fast *and* slow & smooth. 🔁
- ☐ I steered it by **tilting** the micro:bit. 🎡
- ☐ I gave my servo a **paper costume** (hand, flower or spinner). ✂️
- ☐ *(Legend!)* I made the **tickle** robot, the **dance** or the **remote-control arm**. 🤖
- ☐ I **drew my robot** for the final project. ✏️

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-8
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** everyone can wire a servo and move it from code, tries a paper prop, and leaves with a **sketch of their final-project robot**. Fast finishers try two servos and radio.

    **Materials**

    - micro:bits + USB + **sensor shields** — **1 per kid**
    - **micro servo 9g (SG90)**, 0–180° — **1 per kid**, a few extra for the two-servo dance; the little screws for the horns
    - **battery packs** (AA/AAA for the shield or micro:bit) — needed for two servos or if boards keep restarting
    - **cardboard, paper, card, masking tape, glue sticks, scissors, markers, string, paper clips, foil** — **no plastic**
    - **A4 paper + pencils** for the robot design

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 final-project reveal + robot ideas → 10 **meet the servo + wiring** → 10 **buttons → sweep** → 10 **slow & smooth → tilt** → 20 ✂️ **paper costume** (each kid picks wave / sunflower / spinner) → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 10 🤖 **tickle / dance / remote** (fast finishers) → 15 ✏️ **design your robot** (keep the sheets for next week!) → 5 Kahoot.

    **Notes:** every embed opens in **Blocks** and already includes the **servo** extension; kids starting from scratch add it via **Extensions → "servo"**. **Restarts, buzzing or a micro:bit that goes dark** when the servo moves = not enough power → battery pack (two servos almost always need one). If the servo **doesn't move at all**, check the plug isn't **backwards** (brown on G) and that it's on **P1**. Most kits are **positional** servos (0–180°); a **continuous-rotation** (360°) servo spins instead of pointing — it needs the `continuous servo P1 run at …%` block rather than `set angle`. Push the horn on **at 90°** (run the button program, press A + B, then fit the arm) so the paper parts start straight. Sound in these programs doesn't clash with P1/P2. For the remote arm, **give each pair a group number** before they start. Collect the robot sketches — Week 9 starts from them.
