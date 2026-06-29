#!/usr/bin/env bash
# .wiki/scripts/publish.sh — render patterns/*.md into a static human-browsable
# HTML wiki under wiki/. Invoked by /wiki-publish.
#
# SOURCE   : patterns/*.md  (canonical, never modified)
# OUTPUT   : wiki/index.html + wiki/patterns/{kebab}.html  (generated)
# PACKAGE  : .wiki/dist/agent-building-playbook-wiki.zip   (generated, gitignored)
#
# Portable: bash + python3 stdlib only. No external/runtime deps. Fails loud.
set -euo pipefail

# Resolve repo root from this script's location (.wiki/scripts/ -> repo root).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

PATTERNS_DIR="${1:-patterns}"
WIKI_DIR="${2:-wiki}"
DIST_DIR=".wiki/dist"

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is required but was not found on PATH." >&2
    exit 1
fi

if [[ ! -d "$PATTERNS_DIR" ]]; then
    echo "ERROR: source pattern directory not found: $PATTERNS_DIR" >&2
    exit 1
fi

echo "Rendering $PATTERNS_DIR -> $WIKI_DIR ..." >&2

# All rendering logic lives in the embedded stdlib-only Python program below.
PATTERNS_DIR="$PATTERNS_DIR" WIKI_DIR="$WIKI_DIR" python3 - <<'PYEOF'
import html
import os
import re
import sys
from pathlib import Path

patterns_dir = Path(os.environ["PATTERNS_DIR"])
wiki_dir = Path(os.environ["WIKI_DIR"])

CSS = """
:root { --fg:#1b1b1f; --muted:#5b5b66; --accent:#3858a6; --bg:#fbfbfd; --card:#fff; --line:#e6e6ec; }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg);
  font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
.wrap { max-width:820px; margin:0 auto; padding:2.5rem 1.25rem 4rem; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
header.site { border-bottom:1px solid var(--line); margin-bottom:2rem; }
h1 { font-size:2rem; margin:0 0 .35rem; }
h2 { font-size:1.3rem; margin:2rem 0 .6rem; }
h3 { font-size:1.05rem; margin:1.4rem 0 .4rem; }
.lede { color:var(--muted); font-size:1.05rem; }
.tag { display:inline-block; font-size:.8rem; padding:.12rem .55rem; margin:0 .3rem .3rem 0;
  background:#eef1fa; color:var(--accent); border-radius:999px; }
.toc-tag { font-weight:600; }
ul.cards { list-style:none; padding:0; margin:.5rem 0 0; }
ul.cards li { background:var(--card); border:1px solid var(--line); border-radius:10px;
  padding:.7rem .9rem; margin:.45rem 0; }
ul.cards li .ttl { font-weight:600; }
ul.cards li .ol { color:var(--muted); font-size:.93rem; display:block; margin-top:.15rem; }
.nav { font-size:.9rem; color:var(--muted); margin-bottom:1.5rem; }
.pattern-body { background:var(--card); border:1px solid var(--line); border-radius:12px;
  padding:1.25rem 1.5rem; }
.pattern-body ul { padding-left:1.2rem; }
.pattern-body code { background:#f0f0f4; padding:.1rem .35rem; border-radius:5px; font-size:.9em; }
.dims { margin:.5rem 0 1.5rem; }
footer.site { margin-top:3rem; padding-top:1.25rem; border-top:1px solid var(--line);
  color:var(--muted); font-size:.85rem; }
hr { border:0; border-top:1px solid var(--line); margin:2rem 0; }
button.tag { border:1px solid var(--line); cursor:pointer; font:inherit; line-height:1.4; }
button.tag[aria-pressed="true"] { background:var(--accent); color:#fff; border-color:var(--accent); }
.card-tags { display:block; margin-top:.4rem; }
.card-tags .tag { font-size:.72rem; }
ul.cards li.hide { display:none; }
.count { color:var(--muted); font-size:.9rem; margin:.25rem 0 0; }
"""

FILTER_JS = """
<script>
(function () {
  var buttons = Array.prototype.slice.call(document.querySelectorAll('button[data-filter]'));
  var items = Array.prototype.slice.call(document.querySelectorAll('#pattern-list > li'));
  var count = document.getElementById('count');
  function apply(filter) {
    var shown = 0;
    items.forEach(function (li) {
      var dims = (li.getAttribute('data-dims') || '').split(' ');
      var show = filter === 'all' || dims.indexOf(filter) !== -1;
      li.classList.toggle('hide', !show);
      if (show) { shown += 1; }
    });
    buttons.forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === filter));
    });
    if (count) {
      count.textContent = 'Showing ' + shown + ' pattern' + (shown === 1 ? '' : 's') +
        (filter === 'all' ? '' : ' tagged \u201c' + filter + '\u201d');
    }
  }
  buttons.forEach(function (b) {
    b.addEventListener('click', function () { apply(b.getAttribute('data-filter')); });
  });
})();
</script>
"""


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_pattern(path: Path) -> dict:
    """Split flat frontmatter from body. Fail loud on malformed files."""
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.DOTALL)
    if not m:
        raise SystemExit(f"ERROR: {path} is missing a frontmatter block.")
    front_text, body = m.group(1), m.group(2)
    front = {}
    for line in front_text.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, val = line.partition(":")
        front[key.strip()] = val.strip()
    for required in ("title", "one_liner", "dimensions"):
        if not front.get(required):
            raise SystemExit(f"ERROR: {path} missing required frontmatter field: {required}")
    dims = [d.strip() for d in front["dimensions"].split(",") if d.strip()]
    return {
        "slug": path.stem,
        "title": front["title"],
        "one_liner": front["one_liner"],
        "dimensions": dims,
        "body": body.strip(),
    }


_INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_INLINE_CODE = re.compile(r"`([^`]+)`")
_INLINE_BOLD = re.compile(r"\*\*([^*]+)\*\*")


def render_inline(text: str) -> str:
    """Escape, then re-apply a safe markdown inline subset."""
    text = html.escape(text)
    text = _INLINE_CODE.sub(lambda m: f"<code>{m.group(1)}</code>", text)
    text = _INLINE_BOLD.sub(lambda m: f"<strong>{m.group(1)}</strong>", text)

    def link(m):
        label, url = m.group(1), m.group(2)
        safe = url if re.match(r"^(https?:|#|/|\.)", url) else "#"
        return f'<a href="{safe}">{label}</a>'

    text = _INLINE_LINK.sub(link, text)
    return text


def render_markdown(body: str) -> str:
    """Minimal stdlib markdown -> HTML for the pattern body subset.

    Handles: ##/### headings, '- ' unordered lists, paragraphs, and the inline
    subset (links, inline code, bold). Anything unrecognised degrades to a
    paragraph with escaped text. No external markdown dependency.
    """
    out: list[str] = []
    lines = body.splitlines()
    i = 0
    para: list[str] = []

    def flush_para():
        if para:
            out.append(f"<p>{render_inline(' '.join(para).strip())}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush_para()
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if h:
            flush_para()
            level = min(len(h.group(1)) + 1, 6)  # demote so page <h1> stays unique
            out.append(f"<h{level}>{render_inline(h.group(2))}</h{level}>")
            i += 1
            continue
        if re.match(r"^[-*]\s+", stripped):
            flush_para()
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i])
                items.append(f"<li>{render_inline(item)}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        para.append(stripped)
        i += 1
    flush_para()
    return "\n".join(out)


def page(title: str, inner: str, depth: int) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{inner}
<footer class="site">Generated from <code>patterns/</code> by
<code>.wiki/scripts/publish.sh</code> — do not hand-edit. Regenerate with
<code>/wiki-publish</code>. &middot; <a href="{prefix}index.html">Home</a></footer>
</div>
</body>
</html>
"""


def main():
    files = sorted(patterns_dir.glob("*.md"))
    if not files:
        raise SystemExit(f"ERROR: no pattern files found in {patterns_dir}")

    patterns = [parse_pattern(p) for p in files]
    by_slug = {p["slug"]: p for p in patterns}

    # Reset generated output dirs (leave wiki/README.md in place).
    out_patterns = wiki_dir / "patterns"
    if out_patterns.exists():
        for f in out_patterns.glob("*.html"):
            f.unlink()
    out_patterns.mkdir(parents=True, exist_ok=True)

    # Group by dimension tag (multi-value: a pattern appears under each tag).
    tags: dict[str, list[dict]] = {}
    for p in patterns:
        for tag in p["dimensions"]:
            tags.setdefault(tag, []).append(p)

    # ---- Landing page ----
    # Dimensions are multi-value, so a pattern can belong to several tags. Rather
    # than repeat a card under every tag (which reads as duplicates on a linear
    # scroll), render ONE canonical card per pattern — sorted by title, carrying
    # all its tags as chips — plus a dimension filter. The per-tag counts reflect
    # how many patterns carry each tag; the list itself stays de-duplicated.
    total = len(patterns)
    filter_buttons = [
        f'<button class="tag toc-tag" data-filter="all" aria-pressed="true">'
        f"All ({total})</button>"
    ]
    for t in sorted(tags):
        filter_buttons.append(
            f'<button class="tag toc-tag" data-filter="{slugify(t)}">'
            f"{html.escape(t)} ({len(tags[t])})</button>"
        )

    inner = [
        '<header class="site">',
        "<h1>Agent-Building Playbook</h1>",
        '<p class="lede">Patterns for building better in the agentic age. '
        "Generated from the curated <code>patterns/</code> source &mdash; each "
        "pattern is listed once; filter by dimension to narrow the list.</p>",
        "</header>",
        "<h2>Filter by dimension</h2>",
        '<p class="dims">' + "".join(filter_buttons) + "</p>",
        '<p class="count" id="count">Showing all ' + str(total) + " patterns</p>",
        '<ul class="cards" id="pattern-list">',
    ]
    for p in sorted(patterns, key=lambda x: x["title"].lower()):
        href = f"patterns/{p['slug']}.html"
        dim_slugs = " ".join(slugify(t) for t in p["dimensions"])
        card_tags = "".join(
            f'<span class="tag">{html.escape(t)}</span>' for t in p["dimensions"]
        )
        inner.append(
            f'<li data-dims="{dim_slugs}">'
            f'<a class="ttl" href="{href}">{html.escape(p["title"])}</a>'
            f'<span class="ol">{html.escape(p["one_liner"])}</span>'
            f'<span class="card-tags">{card_tags}</span></li>'
        )
    inner.append("</ul>")
    inner.append(FILTER_JS)
    (wiki_dir / "index.html").write_text(page("Agent-Building Playbook", "\n".join(inner), 0), encoding="utf-8")

    # ---- One page per pattern ----
    # Turn `patterns/{slug}.md` code-span references (used in the "Related"
    # section) into real links to the rendered sibling page, preserving the
    # original displayed text. Leave unknown slugs untouched.
    rel_re = re.compile(r"<code>patterns/([a-z0-9-]+)\.md</code>")

    def link_related(m):
        slug = m.group(1)
        if slug in by_slug:
            return f'<a href="{slug}.html">{m.group(0)}</a>'
        return m.group(0)

    for p in patterns:
        body_html = render_markdown(p["body"])
        body_html = rel_re.sub(link_related, body_html)
        dim_links = "".join(
            f'<a class="tag" href="../index.html#{slugify(t)}">{html.escape(t)}</a>'
            for t in p["dimensions"]
        )
        inner = (
            '<div class="nav"><a href="../index.html">&larr; All patterns</a></div>'
            '<header class="site">'
            f"<h1>{html.escape(p['title'])}</h1>"
            f'<p class="lede">{html.escape(p["one_liner"])}</p>'
            f'<div class="dims">{dim_links}</div>'
            "</header>"
            f'<article class="pattern-body">{body_html}</article>'
        )
        (out_patterns / f"{p['slug']}.html").write_text(
            page(p["title"], inner, 1), encoding="utf-8"
        )

    print(
        f"OK: rendered {len(patterns)} patterns across {len(tags)} dimensions -> {wiki_dir}/",
        file=sys.stderr,
    )


main()
PYEOF

# Package a distributable zip (regenerable; gitignored).
mkdir -p "$DIST_DIR"
ZIP_PATH="$DIST_DIR/agent-building-playbook-wiki.zip"
if command -v zip >/dev/null 2>&1; then
    rm -f "$ZIP_PATH"
    ( cd "$WIKI_DIR" && zip -qr "$REPO_ROOT/$ZIP_PATH" . -x 'README.md' )
    echo "Packaged: $ZIP_PATH" >&2
else
    echo "NOTE: 'zip' not found — skipped packaging step (HTML site still built in $WIKI_DIR/)." >&2
fi

echo "Done. Open $WIKI_DIR/index.html in a browser, or deploy $WIKI_DIR/ to GitHub Pages." >&2
