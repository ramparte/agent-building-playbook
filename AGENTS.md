# AGENTS.md — Operational Cycle

This repo is a curated collection of patterns. One canonical source feeds two
generated views. **Edit only the source; never hand-edit generated files.**

## Source of truth

- `patterns/*.md` — the curated pattern files. Flat frontmatter
  (`title`, `one_liner`, `dimensions`) + a markdown "pearl" body. The filename
  (`{kebab-title}.md`) is the identifier. Patterns arrive via GitHub PRs.
  See `SUBMISSIONS.md` for the authoring contract; `.wiki/context/schema.md`
  for the machine schema.

## Generated views (do not hand-edit)

| View | File(s) | Generator | Audience |
|---|---|---|---|
| Agent index | `INDEX.md` | `scripts/build-index.sh` | agents (dense, token-efficient) |
| Human wiki | `wiki/` (static HTML) | `.wiki/scripts/publish.sh` | humans (browsable by tag) |

## Cycle

1. **Add / edit a pattern** in `patterns/` (PR flow).
2. **Rebuild the agent index:** `bash scripts/build-index.sh` → `INDEX.md`
   (a GitHub Action also runs this on merge to `main`).
3. **Render the human wiki:** `bash scripts/build-index.sh`'s human counterpart,
   `/wiki-publish` (→ `.wiki/scripts/publish.sh`) → `wiki/`.

`INDEX.md` and `wiki/` are two renderings of the SAME `patterns/` source — they
never diverge from it, and neither is edited by hand.

## Wiki commands

- `/wiki-publish` — render `patterns/*.md` into `wiki/` (and package a zip under
  `.wiki/dist/`). Portable: bash + python3 stdlib only.
