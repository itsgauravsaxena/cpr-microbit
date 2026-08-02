#!/usr/bin/env python3
"""Build-time Danish auto-translation for pages that have no curated .da.md.

English is the source of truth. This script fills the gap: for every English
`README.md` under the docs tree that does NOT already have a hand-written
`README.da.md` next to it, it machine-translates the English into Danish via
the DeepL API and writes the `.da.md` so MkDocs can build a Danish page.

Curated `.da.md` files are always left untouched — an existing Danish file
means "a human wrote this", and it wins over machine translation. Nothing is
ever deleted or overwritten.

Behaviour:
  * No DEEPL_API_KEY set  -> prints a notice and exits 0 (pages fall back to
                             English; the build still succeeds).
  * Nothing missing        -> prints a notice and exits 0.
  * A page fails to translate -> logs it and skips (that page falls back to
                             English); the build still succeeds.

Usage:
  python scripts/translate_da.py            # translate missing pages
  python scripts/translate_da.py --dry-run  # list what would be translated
  python scripts/translate_da.py --self-test  # verify markdown masking logic
"""
from __future__ import annotations

import glob
import html
import os
import re
import sys

DOCS_DIR = "microbit-program"
TARGET_LANG = "DA"

# Spans that must survive translation verbatim. Order matters: fenced code and
# inline code first, then whole links/images, then bare URLs.
_PROTECT_PATTERNS = [
    re.compile(r"```.*?```", re.DOTALL),   # fenced code blocks
    re.compile(r"`[^`\n]+`"),              # inline code
    re.compile(r"!?\[[^\]]*\]\([^)]+\)"),  # [label](url) and ![alt](url)
    re.compile(r"https?://[^\s)]+"),       # bare URLs
]
_TAG_RE = re.compile(r"<x>(\d+)</x>")


def _mask(text: str) -> tuple[str, list[str]]:
    """Replace protected spans with <x>N</x> sentinels; XML-escape the rest."""
    protected: list[str] = []

    def stash(match: re.Match) -> str:
        protected.append(match.group(0))
        return f"<x>{len(protected) - 1}</x>"

    for pattern in _PROTECT_PATTERNS:
        text = pattern.sub(stash, text)

    # XML-escape everything that is not one of our sentinel tags, so the DeepL
    # XML parser sees valid input.
    parts = re.split(r"(<x>\d+</x>)", text)
    for i, part in enumerate(parts):
        if not _TAG_RE.fullmatch(part):
            parts[i] = part.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return "".join(parts), protected


def _unmask(text: str, protected: list[str]) -> str:
    """Undo _mask: unescape entities, then restore protected spans."""
    text = html.unescape(text)
    return _TAG_RE.sub(lambda m: protected[int(m.group(1))], text)


def translate_markdown(text: str, translate_fn) -> str:
    """Translate markdown while preserving code, links and URLs.

    `translate_fn` takes the masked/escaped string and returns the translated
    string (the DeepL call, or a stub in tests).
    """
    masked, protected = _mask(text)
    translated = translate_fn(masked)
    return _unmask(translated, protected)


def iter_english_pages():
    for path in sorted(glob.glob(f"{DOCS_DIR}/**/*.md", recursive=True)):
        if path.endswith(".da.md"):
            continue
        if re.search(r"/code/README\.md$", path):  # excluded from the site anyway
            continue
        yield path


def da_path(english_path: str) -> str:
    return english_path[:-3] + ".da.md"  # foo/README.md -> foo/README.da.md


def _self_test() -> int:
    sample = (
        "# Week 1 — Flashing Heart\n\n"
        "**Goal:** get comfortable with the editor.\n\n"
        "See the [official tutorial](https://makecode.microbit.org/projects/flashing-heart) "
        "and use `pick random` blocks.\n\n"
        "```\nlet x = 0\n```\n\n"
        "Bare link: https://microbit.org/projects/\n"
    )

    # A stub "translator" that only lowercases ASCII words, leaving tags and
    # entities alone — enough to prove protected spans are preserved.
    def stub(masked: str) -> str:
        return re.sub(r"[A-Za-z]+", lambda m: m.group(0).lower(), masked)

    out = translate_markdown(sample, stub)
    checks = {
        "fenced code preserved": "let x = 0" in out,
        "inline code preserved": "`pick random`" in out,
        "link url preserved": "https://makecode.microbit.org/projects/flashing-heart" in out,
        "bare url preserved": "https://microbit.org/projects/" in out,
        "no leftover <x> tags": "<x>" not in out and "</x>" not in out,
        "no leftover entities": "&amp;" not in out and "&lt;" not in out,
    }
    ok = all(checks.values())
    for name, passed in checks.items():
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    print("\n--- stub output ---\n" + out)
    return 0 if ok else 1


def main() -> int:
    if "--self-test" in sys.argv:
        return _self_test()

    dry_run = "--dry-run" in sys.argv
    targets = [(p, da_path(p)) for p in iter_english_pages() if not os.path.exists(da_path(p))]

    if not targets:
        print("All pages already have a curated Danish (.da.md) version — nothing to auto-translate.")
        return 0

    print(f"{len(targets)} page(s) missing Danish; will auto-translate:")
    for src, dst in targets:
        print(f"  {src} -> {dst}")

    if dry_run:
        return 0

    key = os.environ.get("DEEPL_API_KEY", "").strip()
    if not key:
        print("\nDEEPL_API_KEY not set — skipping auto-translation. "
              "These pages will fall back to English on the site.")
        return 0

    import deepl  # imported lazily so --dry-run/--self-test need no dependency

    translator = deepl.Translator(key)

    def deepl_translate(masked: str) -> str:
        return translator.translate_text(
            masked,
            target_lang=TARGET_LANG,
            tag_handling="xml",
            ignore_tags=["x"],
            preserve_formatting=True,
            split_sentences=deepl.SplitSentences.NO_NEWLINES,
        ).text

    failures = 0
    for src, dst in targets:
        with open(src, encoding="utf-8") as fh:
            english = fh.read()
        try:
            danish = translate_markdown(english, deepl_translate)
        except Exception as exc:  # noqa: BLE001 - never fail the build over one page
            failures += 1
            print(f"  ! translation failed for {src}: {exc} (falls back to English)")
            continue
        notice = "<!-- Auto-translated from English by DeepL at build time. -->\n"
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write(notice + danish)
        print(f"  translated {src} -> {dst}")

    print(f"\nDone. Translated {len(targets) - failures}/{len(targets)} page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
