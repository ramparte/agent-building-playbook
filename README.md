# Agent-Building Playbook

> 📖 **Browse the patterns as a human-readable site: [ramparte.github.io/agent-building-playbook](https://ramparte.github.io/agent-building-playbook/)**

A curated, growing collection of patterns for building better in the agentic age — *Programming Pearls, but actionable and for the cognitive-architecture era.*

The subject is **how to build better**, not narrowly how to build agents. Patterns here cover cognitive architecture, agentic workflow design, prompt engineering, orchestration, tooling, and the everyday craft of working productively alongside AI systems.

## Two audiences, one source

One canonical source (markdown) serves two audiences:

- **Agents** read [INDEX.md](./INDEX.md) — a dense, token-efficient list with one-line descriptions grouped by tag, each linking to its full file.
- **Humans** browse the `patterns/` directory directly on GitHub or a generated wiki, reading full pattern pages at their leisure.

## Repo layout

| Path | Description |
|---|---|
| [`INDEX.md`](./INDEX.md) | Dense agent-facing index. **Generated — do not hand-edit.** |
| [`SUBMISSIONS.md`](./SUBMISSIONS.md) | How to write a pattern and open a PR. |
| `patterns/` | One file per pattern: flat frontmatter + markdown pearl body. |
| `scripts/build-index.sh` | Regenerates `INDEX.md` from `patterns/`. |

## Contributing

1. Read [SUBMISSIONS.md](./SUBMISSIONS.md).
2. Add `patterns/{kebab-title}.md`.
3. Open a PR — **don't edit `INDEX.md`** (it is generated).

## Regenerating the index locally

`scripts/build-index.sh` reads every `patterns/*.md` and rewrites `INDEX.md`:

```sh
bash scripts/build-index.sh
```

A GitHub Action runs the same script on every merge to `main`, so `INDEX.md` is always up-to-date in the repo.

## Provenance

Patterns here are distilled from three sources: external literature, battle-tested session history, and the Amplifier team ecosystem. Personal lessons and external literature are treated as peers — there is no provenance weighting in v1. The original research dump that seeded this collection is preserved at [`docs/seed-research-dump.md`](./docs/seed-research-dump.md).
