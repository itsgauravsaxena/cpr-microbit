# Week 2 — Game Lab 🎮

**🔗 Open this page on a computer:** go to **[tinyurl.com/beginw2](https://tinyurl.com/beginw2)**

> Warm up with a face machine, then build your first **real game**: a shake-to-roll **dice** 🎲. (More games — music 🎵 and a fortune teller 🔮 — come in Week 3, and radio games 📻 in Week 4.)

!!! abstract "🎓 What you'll learn today"
    - **events** — run code on a button or a shake
    - **random** — surprise numbers
    - **`if / else`** (conditionals) — make the micro:bit *choose*

<div style="text-align:center;margin:1.5rem 0;" markdown="0">
<svg width="220" height="220" viewBox="0 0 216 216" role="img" aria-label="a face changing happy, sad, surprised" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,Segoe UI,sans-serif">
<rect x="0" y="0" width="216" height="216" rx="24" fill="#0f1419" stroke="#c8a24a" stroke-width="3"/>
<rect x="17" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="17" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="53" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="89" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#2b3038"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#2b3038"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#2b3038"/>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="1;0;0"/><rect x="17" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="125" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;1;0"/><rect x="17" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="161" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
<g fill="#ffd23f" opacity="0"><animate attributeName="opacity" calcMode="discrete" dur="2.1s" repeatCount="indefinite" keyTimes="0.0000;0.3333;0.6667" values="0;0;1"/><rect x="53" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="53" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="89" y="161" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="53" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="125" width="30" height="30" rx="6" fill="#ffd23f"/><rect x="125" y="161" width="30" height="30" rx="6" fill="#ffd23f"/></g>
</svg>
</div>

## 🔥 Warm-up: Button Faces

Buttons make faces, a shake gives a surprise. Press **▶️ Open & run** to play:

*🎓 Concept: **events** — run code on a button or shake.*

??? note "How it works"

    **Purpose.** A gentle warm-up that turns Week 1's `show icon` into something *interactive* — the first taste of **events** (code that waits for something to happen) and **random**.

    **Think of it like a doorbell:** the code sits quietly until its button is pressed, then does its one job — and there's a separate bell for A, B, both-at-once, and a shake.

    **How the code works:**

    - `on start` runs once when the board powers on — here it shows `HEJ!`.
    - `on button A pressed` and `on button B pressed` are two separate **events**. Each is its own little program that sits and waits for its button, then shows a Happy / Sad face.
    - `on button A+B pressed` is a *third* event that fires only when both buttons are pressed together.
    - `on shake` picks a random number **0–3** (`pick random`) into a variable, then an `if / else if` chain shows a different face for each value — the first look at *choosing* based on a number.

    **Watch for:** A+B is its own event — press both at once (in the simulator, click the small **A+B** button). Events don't run in order top-to-bottom; each just waits for its own trigger.

??? example "👀 See the finished blocks"

    ```makecode
    auto
    ```

??? example "🔨 Build it — one step at a time"

    Open each step, add **only the new blocks**, then check against the picture. 🌱

    **① Happy face on button A**

    ```makecode
    auto:step-1
    ```

    **② Sad face on button B**

    ```makecode
    auto:step-2
    ```

    **③ Heart on A + B (press both!)**

    ```makecode
    auto:step-3
    ```

    **④ Surprise when you shake**

    ```makecode
    auto:step-4
    ```

    **⑤ A *random* face on shake**

    ```makecode
    auto:step-5
    ```

    **⑥ Say hi when it starts**

    ```makecode
    auto:step-6
    ```

---

## 🎮 Now build a game!

Build the **dice** game one small piece at a time. The **🔨 Build it** starts with a simple version, then grows into the full game. 🌱

### 🎲 Dice

Shake for a random **1–6**. 🎲

*🎓 Concept: **random** + **`if / else`** (conditionals).*

??? note "How it works"

    **Purpose.** The game everyone can finish. It turns "shake → a random number" into a *real* dice that shows dot patterns, so kids see a number drive what's drawn on screen.

    **Think of it like a board-game dice:** shake and you get a 1–6 — and the `if / else` is the rule sheet ("if you rolled 3, light up three dots").

    **How the code works:**

    - `on shake` is the **event** — it fires once each time the board is shaken.
    - `pick random 1 to 6` produces a fresh number and stores it in a variable (`roll`).
    - An `if / else if` ladder checks `roll` and draws the matching face with `show leds` (each branch is a 5×5 dot pattern). The final `else` handles the 6, so you only need five checks for six outcomes.
    - The build grows in three steps: ① just `show number`, ② make **6** special with one `if / else`, ③ swap every number for real **dots**.

    **Watch for:** kids add the `if` branches one at a time — resist pasting the finished ladder. In the simulator, use the **shake** button to test.

??? example "👀 See the finished game"

    ```makecode
    auto:dice
    ```

??? example "🔨 Build it — 3 small steps"

    **① Roll a number** — shake → a random **1–6**:

    ```makecode
    auto:dice-1
    ```

    **② Make 6 special** — your first `if / else`: a **6** shows a ✓, everything else the number:

    ```makecode
    auto:dice-2
    ```

    **③ Real dice** — swap the number for **dots** (a bigger `if / else`):

    ```makecode
    auto:dice
    ```

### ➡️ More games — next week

Music 🎵 and a fortune teller 🔮 are waiting in **[Week 3 — Game Lab 2](../week-03-game-lab-2/README.md)**, and radio & team games 📻 in **[Week 4](../../week-04-game-lab/README.md)**. Finished the dice with time to spare? Sneak a peek! 👀

---

## ✅ I did it when…

- ☐ My **Button Faces** works on the real board (A 😀, B 🙁).
- ☐ I built the **Dice** game and rolled it.
- ☐ *(Legend!)* My dice shows real **dots**, not just a number. 🎲

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-2
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** build on Week 1's `show icon`. Warm up with **Button Faces** (buttons A/B/A+B, shake, a first taste of **random**), then everyone builds the **🎲 Dice** game — `pick random` + a growing `if / else`, finishing with real **dots**. That's the whole session; the rest of the game menu (music & fortune teller in **[Week 3](../week-03-game-lab-2/README.md)**, radio & team games in **[Week 4](../../week-04-game-lab/README.md)**) comes later, so Week 2 stays calm and everyone lands the same win. 🎯

    **Fast finishers:** point them straight at **Week 3** for the next games, or at the **🌟 Bonus** there (draw-your-own, Love Meter).

    *(A bigger **🚀 Star Catcher** game — variable + loop + LED plotting — is parked in `archive/week-02-star-catcher/` if you want an extra stretch. Pull-back steps are in that folder's README.)*

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap Week 1 → 30 build **Button Faces** together (steps ①–⑥) → 10 download to the board → 15 start **Dice** (① roll a number).
    - **Break (20)**
    - **Block 2 (30):** 20 finish **Dice** (② make 6 special → ③ real dots) at own pace → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens straight into **Blocks**. Each *Build it* shows a simple **starter** first, then the **full** program, so kids grow one program rather than copy finished code.
