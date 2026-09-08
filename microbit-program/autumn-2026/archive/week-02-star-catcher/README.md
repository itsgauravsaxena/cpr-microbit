# 🚀 Star Catcher — parked game (was in Beginner Week 2)

A little too big for a 2nd session (it uses a **variable + a loop + LED plotting**), so it was moved here. The full working source is in `code/` — pull it back whenever you want it, e.g. as a Week 3 stretch.

## How to pull it back

1. Move the programs back into the target week's code folder (replace `week-XX`):

   ```bash
   mv microbit-program/autumn-2026/archive/week-02-star-catcher/code/star*.ts \
      microbit-program/autumn-2026/microbit-beginners/week-XX/code/
   ```

2. Regenerate the blocks and publish (mints fresh share ids into that week's `shares.txt`):

   ```bash
   node scripts/decompile_blocks.js microbit-program/autumn-2026/microbit-beginners/week-XX/code
   python3 scripts/publish_makecode.py microbit-program/autumn-2026/microbit-beginners/week-XX
   ```

3. Paste the page section below into that week's `README.md` (and the Danish one into `README.da.md`).

> The `.blocks` files here are just a snapshot; step 2 regenerates them.

## Page section — English

Copy everything between the lines into `README.md`:

````markdown
### 🚀 Star Catcher

<span title="spicy — a big one">🌶️ **Spicy!**</span> Catch the falling star ⭐. Move with **A** / **B**. Press **A + B** to see your score. *(Big challenge — you might finish it next week!)*

```makecode
auto:star
```

??? example "🔨 Build it — 4 small steps"

    **① Move** — a catcher dot you slide with **A** / **B**:

    ```makecode
    auto:star-1
    ```

    **② Stay on screen** — use **constrain** so it can't slide off the edge:

    ```makecode
    auto:star-2
    ```

    **③ Falling star** — a star drops from the top — practise sliding under it:

    ```makecode
    auto:star-3
    ```

    **④ Catch + score** — catch the star for **+1**, and press **A + B** to see your score:

    ```makecode
    auto:star
    ```
````

## Page section — Danish

Copy everything between the lines into `README.da.md`:

````markdown
### 🚀 Stjernefanger

<span title="svær — en stor en">🌶️ **Svær!**</span> Fang den faldende stjerne ⭐. Flyt med **A** / **B**. Tryk **A + B** for at se din score. *(Stor udfordring — måske gør du den færdig næste uge!)*

```makecode
auto:star
```

??? example "🔨 Byg det — 4 små trin"

    **① Flyt** — en fanger-prik du glider med **A** / **B**:

    ```makecode
    auto:star-1
    ```

    **② Bliv på skærmen** — brug **constrain**, så den ikke kan glide ud over kanten:

    ```makecode
    auto:star-2
    ```

    **③ Faldende stjerne** — en stjerne falder fra toppen — øv dig i at glide ind under den:

    ```makecode
    auto:star-3
    ```

    **④ Fang + score** — fang stjernen for **+1**, og tryk **A + B** for at se din score:

    ```makecode
    auto:star
    ```
````
