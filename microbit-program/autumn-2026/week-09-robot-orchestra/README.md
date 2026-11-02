# Week 9 — Robot Orchestra 🤖🎶 (part 1: build)

> Our final project starts now! Everyone builds a **paper robot** with **two servos** (a drumming arm and a tilting head), **LED eyes** and a **note** of its own. Next week the robots learn to play **together** over radio, and in the last class we give a **concert** for everyone. 🎉

!!! abstract "🎓 What you'll learn today"
    - **building** — turn flat paper into a robot that stands, with servos taped on
    - **wiring** — two servos (P1, P2) and two LEDs (P8, P13) on the shield
    - **testing** — check every part works before you add the next one
    - **one program, many robots** — every robot runs the same code; only *your note* changes

## 🎼 The plan

| Week | What we do |
|---|---|
| **9 — today** | **Build** your robot and test it 🛠️ |
| **10** | **Band practice** — all robots play “Mester Jakob” together over radio 📡 |
| **11** | 🎉 **Concert** for parents and friends |

**Eight robots, eight jobs:** seven robots each own **one note** (low G, C, D, E, F, G, A) and one robot is the **drummer** 🥁. Your teacher tells you which one you are.

## 📄 Print the robot

Everything is on paper — no cardboard, no craft knife. Print the PDF, cut, fold, tape. ✂️

[⬇️ Robot template — English (PDF, 7 pages)](robot-template-A4.pdf){ .md-button .md-button--primary }
[⬇️ Robot-skabelon — dansk (PDF)](robot-skabelon-A4.pdf){ .md-button }

!!! tip "Printing 🖨️"
    - Print at **100% / “Actual size”** — not “Fit to page”. Check: the line on sheet 4 must measure **exactly 5 cm**.
    - **Each kid:** sheets **1** (body A) and **2** (head B, arms C + D, drum E).
    - **To share:** sheet **3** (note badges G, drum top F, decorations H) — 2–3 copies.
    - **Per table:** sheets **4–7** (parts list, how the servos sit, picture steps).
    - Normal paper works. Thicker paper (160–200 g) or a piece of **cereal box** glued behind the body makes it stronger.

## 🛠️ Build it

Follow the **picture steps** on sheets 6–7. The parts have letters, IKEA-style: **A** body · **B** head · **C** drumstick arm · **D** decoration arm (optional) · **E** drum · **F** drum top · **G** your note badge · **H** decorations.

!!! info "How the servos sit (sheet 5) 🔧"
    The servo lies **flat on the paper**, with the **shaft pointing at you** — like the hand of a clock.

    - **Arm:** servo 1 sits on the **right shoulder**. Arm **C** is taped onto the horn and hangs down. When the servo turns, C swings and hits the drum.
    - **Head:** servo 2 sits on the **neck**. The back of head **B** is taped onto the horn, so the head hides the servo. When the servo turns, the head **tilts** left and right.

**Step 4 — set both servos to 90° *before* you tape anything on**, so the arm hangs straight and the head sits straight:

??? example "🎯 servo-center · P1 + P2"

    ```makecode
    auto:servo-center
    ```

    *Download it, wait for ✓, then fit the horns, arm and head. Don't turn the servos by hand afterwards!*

## 🔌 Wiring

| Part | Pin | Wires |
|---|---|---|
| Servo 1 · arm | **P1** | brown → G · red → V · orange → S |
| Servo 2 · head | **P2** | brown → G · red → V · orange → S |
| LED eye, left | **P8** | long leg → S · short leg → G |
| LED eye, right | **P13** | long leg → S · short leg → G |

*LED eyes stay dark? Turn the LED round — see the 🔧 checklist in [Week 7](../week-07-light-it-up/README.md).*

## 🧪 Test your robot

Before you decorate, check that everything moves: **A** = arm hits + eyes flash, **B** = head tilts.

??? example "🧪 robot-test · P1 + P2 + P8 + P13"

    ```makecode
    auto:robot-test
    ```

    *Arm doesn't hit the drum? Move the drum, or re-tape C a bit lower. Head crooked? Run servo-center again and re-tape B.*

## 🎵 Your robot program

This is the program your robot plays in the concert. **Everyone with a note uses the same program** — you only change **two things** at the start:

1. **`set myNote to …`** — click the 🎹 piano and pick **your note**. Low G is the G further left on the keyboard.
2. **`show string "ROBO"`** (inside *on button A*) — write **your robot’s name**.

??? example "🎵 robot — for the 7 note robots"

    ```makecode
    auto:robot
    ```

    | When… | your robot… |
    |---|---|
    | its note arrives over radio 📡 | hits the drum, tilts its head, flashes its eyes and plays its note |
    | you press **A** | does a **solo**: says its name, dances and says hello 👋 |
    | you touch the **logo** 👆 | giggles and wiggles (Ticklebot!) |
    | the audience **claps** 👏 | bows (only when the music has stopped) |

    *Arm swings away from the drum instead of onto it? Change `armDown` from **60** to **120**.*

??? example "🥁 drummer — for the drum robot"

    The drummer doesn't need a note: **BOOM** (arm + deep drum) on beats 1 and 3, **TIK** (head + tick) on beats 2 and 4. Change `"DRUM"` to your robot’s name.

    ```makecode
    auto:drummer
    ```

## 🎼 Sneak peek — the conductor

At the end of class, try it once with **all robots together**! Your teacher holds the conductor micro:bit:

??? example "🎼 conductor — teacher’s micro:bit"

    - **A** → plays “Mester Jakob”: sends each note and drum beat over **radio group 9**
    - **B** → **helper mode** (shows **H**): the conductor plays the melody too, so missing notes are covered
    - **A + B** → every robot **bows** 🙇

    ```makecode
    auto:conductor
    ```

## ✅ I did it when…

- ☐ I cut out and folded my robot, and it **stands up**. ✂️
- ☐ I ran **servo-center** and fitted the **arm** and **head** straight. 🎯
- ☐ My **robot-test** works: arm hits, head tilts, eyes flash. 🧪
- ☐ I set **my note** and **my robot’s name** in the robot program. 🎵
- ☐ *(Legend!)* My robot does a **solo**, **giggles** when tickled and **bows** when we clap. 👏

## 🎉 Kahoot time!

```kahoot
week-9
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** every kid leaves with a **standing paper robot** whose arm, head and eyes work, and with the **robot program** set to their note. Next week is band practice.

    **Who does what (8 kids):** everyone builds **their own robot** — they present it at the concert. Work in **pairs**: one cuts while the other wires and tests, then swap, so each pair finishes two robots. Give notes in this order so the song still works if someone is missing: **C, G, E, F, D, A, low G, drummer**. The note list stays with you, not on this page.

    **Materials**

    - 8 micro:bits (V2) + USB + **sensor shields**, **16 SG90 servos**, **16 LEDs**, jumper wires
    - **battery packs** — two servos on USB can make the micro:bit restart; needed on stage anyway
    - printed PDF (see *Printing* above), **scissors, tape** (masking tape is easiest), **glue sticks**, pencils + erasers (for the eye holes), colour pens
    - optional: cereal-box card to stiffen the body, wooden lolly sticks to stiffen arm C (no plastic)
    - one micro:bit for **you** as the conductor

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 show the idea + give out notes → 10 **wire** 2 servos + 2 LEDs and run **robot-test** on the bare parts (prove the electronics first!) → 30 **build steps 1–4** in pairs (cut, fold, eye holes, servo-center) → 10 **steps 5–6** (servos on the body, head + arm on the horns) → 5 checkpoint.
    - **Break (20)**
    - **Block 2 (30):** 10 **steps 7–8** (drum, connect) → 10 download **robot**, set note + name, try solo / tickle / clap → 5 🎼 **first band try** with the conductor → 5 Kahoot (skip if short on time).

    **Notes:** every embed opens in **Blocks** with the **servo** extension already added. All robots and the conductor use **radio group 9** — don't change it. Run **servo-center before taping on the horns**, otherwise arms and heads end up crooked. **Restarts, buzzing or shaking** = not enough power → battery pack. The **clap-to-bow** listens to the microphone, but only when nothing has played for 3 seconds, so the music doesn't trigger it; in a loud room, use **A + B on the conductor** to make everyone bow instead. Notes are **short “ding” sounds** — that’s on purpose, so a robot is ready again for its next note. Kids absent? Press **B** on the conductor (helper mode) to fill the gaps. If paper gets floppy where a servo sits, glue a piece of cereal box behind it.
