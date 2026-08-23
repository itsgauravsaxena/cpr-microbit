# This week's MakeCode programs

The lesson page embeds programs from the `.ts` files in this folder (MakeCode
"JavaScript" / TypeScript — MakeCode generates the blocks automatically).

- `main.ts` — the week's main program (embedded on the page with an `auto` fence).
- extra `*.ts` (e.g. `rung-1.ts`) — more programs on the same page, embedded
  with `auto:rung-1` etc. The filename without `.ts` is the program name.
- `deps.txt` *(optional)* — extra MakeCode extensions, one per line
  (defaults: `core`, `radio`, `microphone`).

To (re)publish after adding or editing a program, from the repo root:

    python scripts/publish_makecode.py

It publishes only what changed and writes the share ids into `shares.txt`
(auto-generated — don't edit by hand).

See the repo README ("MakeCode embeds") for details.
