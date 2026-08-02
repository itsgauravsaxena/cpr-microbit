# Autumn 2026 — 10-Week Program

_[← All terms](../README.md)_

A 10-week coding program for two groups of 8-10 year olds, split by experience. 1-hour sessions, physical micro:bits for everyone. Built almost entirely on official micro:bit Foundation / MakeCode tutorials.

## Groups

- **[Group A — Startup](./group-a-startup/README.md)** — brand new to coding. Weeks 1-4 build core skills through official MakeCode tutorials, weeks 5-6 build a servo-powered "Ticklebot" robot, weeks 7-8 build a radio transmitter/receiver project, week 9 consolidates, week 10 is a showcase.
- **[Group B — Advanced (Mini Pinball Machine)](./group-b-advanced-pinball/README.md)** — already comfortable with MakeCode. A 10-week capstone building a small tabletop pinball machine: kids 3D-design and print the simple interior parts (bumpers, sensor mounts) while the outer cabinet/precision parts are pre-supplied. Programming covers scoring, sensors, and a radio-linked scoreboard.

## Repo structure

Each week has its own folder with:
- `README.md` — goal, official tutorial link(s), materials, step notes, and reference links
- `code/` — where to drop the exported MakeCode project for that week (`.hex` file, or the shareable `makecode.microbit.org/_xxxxx` link pasted into a text file). MakeCode projects live in the browser by default, so exporting here is what actually preserves each week's work.

## How to save a MakeCode project into `code/`

1. In the MakeCode editor, click the gear icon → **Share** to get a shareable link, or **Download** to get a `.hex` file
2. Drop the `.hex` file into that week's `code/` folder, or paste the share link into a `link.md` file there
3. Commit and push

## Teaching approach: pictorial/animated explanations

MakeCode's built-in **Tutorials** mode (Tutorials tab on the MakeCode home screen) walks through each project step-by-step with pictures, highlights the exact block to drag next, and runs live in the on-screen simulator. Project it on a screen each week and let the tutorial do the explaining — this is the main visual aid for the whole program, referenced throughout the week READMEs below instead of rebuilt from scratch.

## Reference builds (Group B)

- ["3D Printed Pinball" by ctrl design](https://pinshape.com/items/24228-3d-printed-pinball) — micro:bit/Arduino-based, scalable difficulty, free STL files
- micro:bit + PinBox 3000 cardboard pinball (TechnoChic) — reference for driving lights, sound, and a scoreboard from a micro:bit on a simple frame

