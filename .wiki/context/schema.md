# Wiki Schema — `pattern` entity

> Machine-oriented contract for the llm-wiki adoption in this repo.
> This repo is an **existing, curated, published** collection. The wiki layer
> is a **render/publish** step (markdown → human-browsable HTML), **not** an
> ingest-and-synthesize loop. The source files are already authored; the wiki
> renders them.

## Source of truth

- `patterns/` — 65+ curated pattern files. **This directory IS the source**
  (it plays the role of `raw/` in the standard three-zone convention). It is
  canonical and human-authored. The wiki publish step **reads** it and never
  writes back into it.
- `INDEX.md` — GENERATED **agent-facing** dense page, built by
  `scripts/build-index.sh` (grouped by dimension tag). It is the agent view of
  the same source. The wiki publish step does **not** touch it.
- `wiki/` — GENERATED **human-facing** static HTML site, built by
  `.wiki/scripts/publish.sh`. This is the artifact this schema governs.

The same `patterns/` source feeds two renderers:

```
                       scripts/build-index.sh  ->  INDEX.md   (agents)
patterns/*.md  ------<
                       .wiki/scripts/publish.sh ->  wiki/     (humans)
```

## Entity: `pattern`

There is exactly **one** entity type. Each file under `patterns/` is one
`pattern`. There is no `id` field — **the filename is the canonical identifier.**

### Filename rule

`patterns/{kebab-title}.md` — all lowercase, words hyphen-separated. The kebab
slug is the identifier used for cross-links and for the rendered page name
(`wiki/patterns/{kebab-title}.html`).

### Frontmatter contract (flat — exactly three scalar lines)

```yaml
---
title: Human-readable name of the pattern
one_liner: One plain-language sentence — feeds INDEX.md and the wiki listing.
dimensions: tag-one, tag-two
---
```

- `title` — required, scalar string.
- `one_liner` — required, scalar string (single sentence).
- `dimensions` — required, **multi-value, comma-separated**. A pattern appears
  under **every** tag it carries. This is the sole faceting/grouping axis.
- Frontmatter MUST stay flat — three inline scalar lines, no nested YAML.

### Body structure (the "pearl")

Markdown after the frontmatter, conventionally in this order:

1. `## What it is`
2. `## When to reach for it`
3. `## When NOT to`
4. `## Exemplars` — markdown list, each item `name — url — one-line note`
5. `## Related` — optional advisory cross-refs to other `patterns/*.md` (not validated)

The publish renderer treats the body as ordinary markdown; the section names
above are conventional, not enforced.

## Dimension tag vocabulary

`dimensions` is the grouping facet for both INDEX.md and the wiki landing page.
Seed vocabulary (10 tags):

| # | Tag |
|---|---|
| 1 | `meta-principles` |
| 2 | `workflow-discipline` |
| 3 | `reliability` |
| 4 | `context-engineering` |
| 5 | `tool-design` |
| 6 | `orchestration` |
| 7 | `verification` |
| 8 | `cost-routing` |
| 9 | `observability` |
| 10 | `taste` |

**Rule:** If no existing tag fits, propose a new one in the PR description.
**Never invent a tag silently.** The vocabulary grows deliberately, by review.

## Cross-references

- Patterns are grouped by `dimensions`; any two patterns sharing a tag are
  related by that facet and co-listed under the tag on the landing page.
- A pattern's optional `## Related` list names sibling `patterns/*.md` files.
  The renderer may turn these into links to the corresponding rendered pages;
  source files remain untouched.
