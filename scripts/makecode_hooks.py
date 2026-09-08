"""MkDocs hook: a reusable ``makecode`` fenced block.

Authors write, anywhere in a lesson page::

    ```makecode
    _abc123
    ```

where ``_abc123`` is the **share id** from MakeCode (Share -> Publish gives
you a link like ``https://makecode.microbit.org/_abc123`` -- paste either the
full link or just the id). It renders a responsive, theme-aware embed that
shows the code next to a running simulator (the ``---codeembed`` view), plus an
"Open & edit in MakeCode" button so kids can fork it into their own version.

If the id is missing or still a placeholder, it renders a friendly "coming
soon" note instead of a broken frame, so pages build cleanly before every
project has been published.

Registered via ``hooks:`` in mkdocs.yml -- loaded by path relative to the
config file, so there is no import-path fiddling.
"""

import html
import pathlib
import re

EMBED_BASE = "https://makecode.microbit.org"
_PLACEHOLDERS = {"", "_", "todo", "tbd", "xxx", "pending", "auto"}

# Language for the "Open & run" editor link, set per page in on_page_markdown
# (mkdocs builds pages sequentially, so a module global is safe). The inline
# ---codeembed blocks follow the viewer's own browser language and can't be
# pinned, but the full editor honours ?lang — so a Danish page opens MakeCode
# in Danish and an English page in English. See the makecode-embed language note.
_PAGE_LANG = "en"

# Page source path, so _formatter can find the sibling code/ folder (for
# pre-rendered Danish block images and share ids). Set per page.
_PAGE_SRC = None

# Pages that ship PRE-RENDERED, language-pinned block images. The codeembed
# view can't be pinned to Danish (it follows the viewer's browser), so for these
# pages we swap in a harvested PNG (scripts/harvest_blocks.py) whenever one
# exists as code/<name>.<lang>.png — otherwise we fall back to the live embed.
_PIN_IMG_PATHS = ("week-02-name-tag-smiley-buttons",)

# A ```makecode fence with a single-line body: a share id, ``auto`` (the
# week's main program) or ``auto:<name>`` (a named program, e.g. a ladder rung).
# The closing fence may be indented when the block is nested in a tab/admonition.
_FENCE = re.compile(r"(```makecode[^\n]*\n)([^\n]*)(\n[ \t]*```)")

# A ```kahoot fence with a single-line body: a week key (``week-1``) resolved
# from the term's quiz/kahoots.txt, or a full https URL. Rendered as a button.
_KAHOOT_FENCE = re.compile(r"```kahoot[^\n]*\n([^\n]*)\n[ \t]*```")


def _normalise(source: str) -> str:
    """Pull a bare share id out of whatever the author pasted."""
    if not source:
        return ""
    first = next((ln.strip() for ln in source.splitlines() if ln.strip()), "")
    # Accept a full URL (…/_abc123 or …#pub:_abc123) or a bare id.
    first = first.split("#pub:")[-1]
    first = first.rstrip("/").rsplit("/", 1)[-1]
    return first.strip()


def _img_embed(name: str) -> str:
    """Embed a pre-rendered, language-pinned block image (guaranteed Danish).

    Reads code/<name>.<lang>.png next to the page and inlines it as a data URI
    (so it works identically on the English/Danish trees and inside collapsed
    admonitions, with no extra network calls). The "Open & run" button still
    opens the live editor in the page language via the sibling shares.txt.
    """
    import base64
    code_dir = pathlib.Path(_PAGE_SRC).parent / "code"
    png = code_dir / f"{name}.{_PAGE_LANG}.png"
    data = base64.b64encode(png.read_bytes()).decode("ascii")
    share = _shares_for(_PAGE_SRC).get(name, "")
    pub = (share if share.startswith("_") else "_" + share) if share else ""
    editor = (f'<a class="makecode-embed__edit md-button md-button--primary" '
              f'href="{EMBED_BASE}/?lang={_PAGE_LANG}#pub:{html.escape(pub, quote=True)}" '
              f'target="_blank" rel="noopener">'
              f'{"▶️ Åbn &amp; kør i MakeCode ↗" if _PAGE_LANG == "da" else "▶️ Open &amp; run in MakeCode ↗"}'
              "</a>") if pub else ""
    return (
        '<div class="makecode-embed makecode-embed--img" markdown="0">'
        f'<img class="makecode-embed__img" alt="MakeCode blokke" '
        f'loading="lazy" src="data:image/png;base64,{data}">'
        f"{editor}"
        "</div>"
    )


def _formatter(source, language, css_class, options, md, **kwargs):
    first = next((ln.strip() for ln in (source or "").splitlines()
                  if ln.strip()), "")
    if first.startswith("img:"):
        return _img_embed(first.split(":", 1)[1].strip() or "main")
    share = _normalise(source)
    if share.lower() in _PLACEHOLDERS:
        return (
            '<div class="makecode-embed makecode-embed--pending" markdown="0">'
            "<p>▶️ <strong>Live MakeCode program coming soon.</strong> "
            "Follow the “Try it in MakeCode” steps below to build it "
            "yourself in the meantime.</p>"
            "</div>"
        )
    pub = share if share.startswith("_") else "_" + share
    pub = html.escape(pub, quote=True)
    # Inline view uses ---codeembed: it always renders BLOCKS (in the viewer's
    # language), so kids never land on the JavaScript view. It's static, so the
    # "Open & run in MakeCode" button opens the full editor to run, zoom and edit.
    blocks_src = f"{EMBED_BASE}/---codeembed#pub:{pub}"
    # ?lang pins the full editor's UI language (Blokke/Hent…) to the page's
    # language, so kids opening from the Danish page get a Danish editor.
    editor_src = f"{EMBED_BASE}/?lang={_PAGE_LANG}#pub:{pub}"
    label = ("▶️ Åbn &amp; kør i MakeCode ↗" if _PAGE_LANG == "da"
             else "▶️ Open &amp; run in MakeCode ↗")
    return (
        '<div class="makecode-embed" markdown="0">'
        f'<iframe class="makecode-embed__frame" src="{blocks_src}" '
        'title="MakeCode program (blocks)" '
        'allowfullscreen loading="lazy" '
        'sandbox="allow-popups allow-forms allow-scripts allow-same-origin">'
        "</iframe>"
        f'<a class="makecode-embed__edit md-button md-button--primary" '
        f'href="{editor_src}" target="_blank" rel="noopener">'
        f"{label}</a>"
        "</div>"
    )


def _shares_for(src_path: str) -> dict:
    """Read cached share ids from the page's sibling ``code/shares.txt``.

    Each non-comment line is ``<name> <id> [sha256:...]`` (written by
    scripts/publish_makecode.py). ``main`` is the week's primary program;
    other names (e.g. ``rung-1``) are extra programs on the same page.
    Returns {} if there is no cache yet.
    """
    out = {}
    if not src_path:
        return out
    share = pathlib.Path(src_path).parent / "code" / "shares.txt"
    if not share.is_file():
        return out
    for line in share.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = s.split()
        if len(parts) >= 2:
            out[parts[0]] = parts[1]
    return out


def _kahoots_for(src_path: str) -> dict:
    """Read the term's ``quiz/kahoots.txt`` map (walking up from the page).

    Each non-comment line is ``<week-key> <url>`` (e.g.
    ``week-1 https://create.kahoot.it/details/...``). Returns {} if absent.
    """
    out = {}
    if not src_path:
        return out
    p = pathlib.Path(src_path).parent
    for _ in range(6):
        cand = p / "quiz" / "kahoots.txt"
        if cand.is_file():
            for line in cand.read_text(encoding="utf-8").splitlines():
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                parts = s.split()
                if len(parts) >= 2:
                    out[parts[0]] = parts[1]
            return out
        p = p.parent
    return out


def _kahoot_button(url: str, danish: bool) -> str:
    """HTML for the per-week 'Start Kahoot' call-to-action (localized)."""
    if not url.startswith("http"):
        note = ("🎉 <strong>Kahoot kommer snart</strong> — denne uges quiz er "
                "ikke linket endnu."
                if danish else
                "🎉 <strong>Kahoot coming soon</strong> — this week's quiz "
                "isn't linked yet.")
        return (f'<div class="kahoot-cta kahoot-cta--pending" markdown="0">'
                f"<p>{note}</p></div>")
    label = ("🎉 Start Kahoot med børnene ↗" if danish
             else "🎉 Start the Kahoot with the kids ↗")
    url_e = html.escape(url, quote=True)
    return (
        '<div class="kahoot-cta" markdown="0">'
        f'<a class="kahoot-cta__btn md-button md-button--primary" href="{url_e}" '
        f'target="_blank" rel="noopener">{label}</a>'
        "</div>"
    )


def on_page_markdown(markdown, page, config, **kwargs):
    """Fill ``auto`` / ``auto:<name>`` makecode fences from code/shares.txt.

    Pages write a single source line::

        ```makecode
        auto            # -> the week's "main" program
        ```

        ```makecode
        auto:rung-1     # -> a named program in the same week's code/ folder
        ```

    Both the English and Danish versions of a week resolve to the same ids
    (they share the week's ``code/`` folder). An explicit ``_id`` is left
    untouched, so manual overrides still work. Body indentation is preserved so
    the fence keeps rendering when nested inside a tab or admonition.
    """
    if "```makecode" not in markdown and "```kahoot" not in markdown:
        return markdown
    src = getattr(getattr(page, "file", None), "abs_src_path", None)

    global _PAGE_LANG, _PAGE_SRC
    _PAGE_LANG = "da" if (src and src.endswith(".da.md")) else "en"
    _PAGE_SRC = src

    if "```makecode" in markdown:
        shares = _shares_for(src)
        # On a pinned page, prefer a pre-rendered code/<name>.<lang>.png if it
        # has been harvested; programs without one keep the live codeembed, so
        # the image rollout can be incremental.
        code_dir = pathlib.Path(src).parent / "code" if src else None
        pin = bool(src) and any(frag in src for frag in _PIN_IMG_PATHS)

        def repl(m):
            body = m.group(2)
            token = body.strip()
            low = token.lower()
            if low == "auto" or low.startswith("auto:"):
                name = token.split(":", 1)[1].strip() if ":" in token else "main"
                indent = body[: len(body) - len(body.lstrip())]
                if pin and code_dir and (code_dir / f"{name}.{_PAGE_LANG}.png").is_file():
                    filled = f"img:{name}"
                else:
                    filled = shares.get(name) or "_"
                return m.group(1) + indent + filled + m.group(3)
            return m.group(0)

        markdown = _FENCE.sub(repl, markdown)

    if "```kahoot" in markdown:
        kahoots = _kahoots_for(src)
        danish = bool(src) and src.endswith(".da.md")

        def krepl(m):
            token = m.group(1).strip()
            url = token if token.startswith("http") else kahoots.get(token, "")
            return _kahoot_button(url, danish)

        markdown = _KAHOOT_FENCE.sub(krepl, markdown)

    return markdown


def on_config(config, **kwargs):
    """Wire the custom fence and stylesheet into the running build."""
    sf = config["mdx_configs"].setdefault("pymdownx.superfences", {})
    fences = sf.setdefault("custom_fences", [])
    if not any(f.get("name") == "makecode" for f in fences):
        fences.append(
            {"name": "makecode", "class": "makecode", "format": _formatter}
        )
    css = "assets/makecode.css"
    if css not in config["extra_css"]:
        config["extra_css"].append(css)
    return config
