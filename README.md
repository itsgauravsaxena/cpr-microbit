# cpr-microbit

All micro:bit teaching material for the Coding Pirates Rødovre (CPR) micro:bit hold, organized by term, published as a searchable bilingual (English + Danish) website.

**Live site:** https://itsgauravsaxena.github.io/cpr-microbit/

## Structure

- `microbit-program/` — the documentation content (this is the MkDocs `docs_dir`)
  - `README.md` — the hub / landing page
  - `<term>/` — one folder per term (e.g. `autumn-2026/`), each with groups → weeks
  - each week folder has a `README.md` (lesson content) and a `code/` folder for the exported MakeCode project (`.hex` file or a `link.md` with the shareable link)
- `mkdocs.yml` — site configuration (Material theme, term tabs, search, i18n)
- `scripts/translate_da.py` — build-time Danish auto-translation (see below)
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

## Local development

```bash
pip install -r docs-requirements.txt
mkdocs serve        # preview at http://127.0.0.1:8000

# optional: check what auto-translation would do (no API calls)
python scripts/translate_da.py --dry-run
```
