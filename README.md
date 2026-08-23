# cpr-microbit

All micro:bit teaching material for the Coding Pirates Rødovre (CPR) micro:bit hold, organized by term, published as a searchable bilingual (English + Danish) website.

**Live site:** https://itsgauravsaxena.github.io/cpr-microbit/

## Structure

- `microbit-program/` — the documentation content (this is the MkDocs `docs_dir`)
  - `README.md` — the hub / landing page
  - `<term>/` — one folder per term (e.g. `autumn-2026/`), each with groups → weeks
  - each week folder has a `README.md` (lesson content) and a `code/` folder holding that week's MakeCode program as `main.ts` (see **MakeCode embeds** below)
- `mkdocs.yml` — site configuration (Material theme, term tabs, search, i18n)
- `scripts/translate_da.py` — build-time Danish auto-translation (see below)
- `scripts/makecode_hooks.py` — the ` ```makecode ` embed block + `auto` id resolution
- `scripts/publish_makecode.py` — publishes each week's `code/main.ts` to a MakeCode share and caches the id
- `.github/workflows/deploy-docs.yml` — builds and deploys to GitHub Pages on every push to `main`

## Languages: English is the source of truth

- You only need to write and maintain the **English** `README.md` files.
- A hand-written Danish translation can live beside any page as `README.da.md`. These are **curated** and always win.
- Any page **without** a `README.da.md` is **machine-translated to Danish at build time** by `scripts/translate_da.py` (via DeepL). Curated Danish is never overwritten, and nothing is ever deleted.
- If a page has no Danish at all (no curated file and no API key), it simply falls back to English.

### Enabling Danish auto-translation (one-time setup)

The build looks for a repository secret named `DEEPL_API_KEY`. Without it, the site still builds — untranslated pages just fall back to English.

1. Get a free DeepL API key: https://www.deepl.com/pro-api (the free plan covers 500,000 characters/month, which is far more than this site needs).
2. In GitHub: **Settings → Secrets and variables → Actions → New repository secret**.
   - Name: `DEEPL_API_KEY`
   - Value: your DeepL API key (free keys end in `:fx`).
3. Push, or re-run the **Deploy docs** workflow. New English-only pages will now appear in Danish automatically.

## MakeCode embeds

Each lesson page can embed a **live, runnable MakeCode program** (code + simulator + zoom, and an "open & edit" button so kids can fork their own version). You maintain only the TypeScript — MakeCode draws the blocks from it automatically.

Per week, in the `code/` folder:

- **`main.ts`** — the week's main program, in MakeCode "JavaScript" (TypeScript). *Source of truth.*
- **extra `*.ts`** *(optional)* — more programs on the same page (e.g. `rung-1.ts` … `rung-6.ts` for the stretch-ladder embeds). A file's name without `.ts` is its **program name**.
- **`deps.txt`** *(optional)* — extra MakeCode extensions, one per line (defaults: `core`, `radio`, `microphone`).
- **`shares.txt`** — auto-generated map of `name → share id`. **Don't edit by hand.**

In the lesson `README.md` (and `README.da.md`), embed a program with an `auto` fence — `auto` for `main.ts`, or `auto:<name>` for another `.ts`:

    ```makecode
    auto
    ```

    ```makecode
    auto:rung-1
    ```

These resolve from `code/shares.txt` at build time, so English and Danish share the same ids. An explicit `_id` also works if you ever want to hard-code one.

To (re)publish after adding or changing a program:

```bash
python scripts/publish_makecode.py            # publishes only what changed
python scripts/publish_makecode.py --check    # dry run: report, no API calls
python scripts/publish_makecode.py --adopt _abc123 --name main <week-dir>   # register an id you made by hand in the editor
```

The publisher walks every `code/*.ts` in each week and only (re)publishes files whose contents changed. It POSTs to MakeCode's public anonymous-share API (no login). Anonymous shares can't be edited or deleted, so each change mints a new id (the old one lingers harmlessly). Run it locally and commit the updated `shares.txt`; the deploy build does **not** publish.

## Local development

The site needs a recent Python (3.10+). Set up a virtualenv once, then use it every time:

```bash
# one-time setup (creates .venv and installs MkDocs + plugins)
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r docs-requirements.txt
```

> If your default `python3` is too old, use an explicit version (e.g. `python3.13`). On macOS you can install one with `brew install python@3.13`.

Then, to preview:

```bash
source .venv/bin/activate     # activate the venv (each new terminal)
mkdocs serve                  # open http://127.0.0.1:8000/cpr-microbit/
```

`mkdocs serve` hot-reloads on content edits; press **Ctrl+C** to stop. Two gotchas:

- The site is served under the `/cpr-microbit/` base path — use the full URL above, not `http://127.0.0.1:8000/`.
- Editing a hook in `scripts/` (e.g. `makecode_hooks.py`) needs a **restart** of `mkdocs serve` — it hot-reloads content and `mkdocs.yml`, but not Python modules.

Other handy commands (all with the venv active):

```bash
# check what Danish auto-translation would do (no API calls)
python scripts/translate_da.py --dry-run

# (re)publish MakeCode programs after editing any code/*.ts  (see "MakeCode embeds")
python scripts/publish_makecode.py --check   # dry run first
python scripts/publish_makecode.py

# a strict build (fails on warnings) — what CI effectively does
mkdocs build --clean --strict
```
