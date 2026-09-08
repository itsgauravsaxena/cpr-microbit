# Week 2 — Game Lab 🎮

**🔗 Open this page on a computer:** go to **[tinyurl.com/beginw2](https://tinyurl.com/beginw2)**

> Warm up with a face machine, then build **real games**: dice 🎲, music 🎵, secret radio messages 📻, and a fortune teller 🔮.

!!! abstract "🎓 What you'll learn today"
    - **events** — run code on a button or a shake
    - **`if / else`** (conditionals) — make the micro:bit *choose*
    - **random** — surprise numbers
    - **radio** — two micro:bits talking to each other
    - the **Music** blocks — melodies & notes

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

Pick a game, build the blocks, play it. Start easy — work your way up. Each one has a **🔨 Build it** with a simple starter, then the full game. 🌱

### 🎲 Dice

Shake for a random **1–6**. 🎲

*🎓 Concept: **random** + **`if / else`** (conditionals).*

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

### 🎵 Music Maker

Buttons make music. Shake for a surprise tune! 🎵 *(turn the sound up 🔊)*

*🎓 Concept: the **Music** blocks — melodies & notes.*

??? example "👀 See the finished game"

    ```makecode
    auto:music
    ```

??? example "🔨 Build it — 3 small steps"

    **① Press A** — one button, one sound:

    ```makecode
    auto:music-1
    ```

    **② Add B** — a second button with a different tune:

    ```makecode
    auto:music-2
    ```

    **③ Shake surprise** — add a **shake** → a music note 🎵 and a surprise song:

    ```makecode
    auto:music
    ```

### 📻 Secret Messages

Send hearts 💗 and smileys 😀 to a friend's micro:bit — over the air! 📻

*🎓 Concept: **radio** — send & receive between micro:bits.*

!!! tip "You need **two** micro:bits"
    You and your partner both use the **same group number** (change the `1` in *set group*). Pick your own so you don't cross wires with the next pair!

??? example "👀 See the finished game"

    ```makecode
    auto:radio
    ```

??? example "🔨 Build it — 3 small steps"

    **① Send + show** — set your **group**, press **A** to send, show a 💗 when a message arrives:

    ```makecode
    auto:radio-1
    ```

    **② Second button** — add **B** so you can send two different messages:

    ```makecode
    auto:radio-2
    ```

    **③ Two pictures** — use `if / else` so **A** shows a heart 💗 and **B** a smiley 😀:

    ```makecode
    auto:radio
    ```

### 🔮 Fortune Teller

Ask a yes/no question, give it a shake, and see what it says! 🔮

*🎓 Concept: **`if / else if`** — choosing between answers.*

??? example "👀 See the finished game"

    ```makecode
    auto:fortune
    ```

??? example "🔨 Build it — 3 small steps"

    **① Yes or No** — shake → ✓ or ✗ (your first `if / else`):

    ```makecode
    auto:fortune-1
    ```

    **② Add Maybe** — a third answer 🤔 with `else if`:

    ```makecode
    auto:fortune-2
    ```

    **③ Let it think** — it "thinks" first 😴, then gives one of **four** answers:

    ```makecode
    auto:fortune
    ```

---

## 🌟 Bonus

??? example "🎨 Draw your own picture"

    Make **button A** light up your own LEDs with **`show leds`** — draw anything!

    ```makecode
    auto:draw
    ```

??? example "✊✋✌️ Rock, Paper, Scissors"

    Shake to throw rock, paper or scissors — then duel a friend, best of five!

    ```makecode
    auto:rps
    ```

## ✅ I did it when…

- ☐ My **Button Faces** works on the real board (A 😀, B 🙁).
- ☐ I built **at least one game** and played it.
- ☐ *(Legend!)* I built **two or more** games — or stumped the Fortune Teller. 🔮

## 🎉 Kahoot time!

Let's finish with a quiz — everyone together!

```kahoot
week-2
```

---

??? note "👩‍🏫 For helpers — session plan & notes"

    **Goal:** build on Week 1's `show icon`. Warm up with **Button Faces** (buttons A/B/A+B, shake, a first taste of **random**), then let kids pick from a menu of small **games** so fast finishers always have more to reach for. There is deliberately **more here than fits one session** — that's on purpose. 🎯

    **The games (easy → hard):**

    - **🎲 Dice** — `pick random` + `if/else`. Everyone can finish this.
    - **🎵 Music Maker** — the Music blocks. Loud and fun (headphones help a full room).
    - **📻 Secret Messages** — first taste of **radio**; needs **2 boards per pair**, both on the **same group**. Magical for kids.
    - **🔮 Fortune Teller** — more `if / else` practice, all icons (no slow scrolling text). Silly and social — kids love asking it questions.

    *(A bigger **🚀 Star Catcher** game — variable + loop + LED plotting — is parked in `archive/week-02-star-catcher/` if you want a harder Week 3 stretch. Pull-back steps are in that folder's README.)*

    **Session plan (60 + 20 break + 30)**

    - **Block 1 (60):** 5 recap Week 1 → 30 build **Button Faces** together (steps ①–⑥) → 10 download to the board → 15 start **Dice**.
    - **Break (20)**
    - **Block 2 (30):** 20 free choice from the game menu (Dice → Music → Radio → Fortune Teller) at own pace → 5 showcase → 5 Kahoot.

    **Notes:** every embed opens straight into **Blocks**. Each *Build it* shows a simple **starter** first, then the **full** program, so kids grow one program rather than copy finished code. Leftover games are perfect **Week 3** carry-over — better to have too much than too little.
