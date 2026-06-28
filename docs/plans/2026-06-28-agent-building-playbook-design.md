# Agent-Building Playbook Design

## Goal

Stand up a public GitHub repo that is a curated, growing collection of *patterns* for building better in the agentic age — "Programming Pearls, but actionable and for the cognitive-architecture era." It is deliberately holistic: the subject is "how to build better," not narrowly "how to build agents."

The repo serves two audiences from a single canonical source:

1. **Agents** — a dense, token-efficient index they read at task-start to find relevant patterns and tools, then follow links into specifics.
2. **Humans** — a rich, explorable wiki/website generated from the same content.

Hard deadline: advanced practitioners must be able to contribute via GitHub PRs starting at an offsite **tomorrow (2026-06-29)**.

## Audiences & Forms

One canonical source (markdown files in the repo) produces two consumption forms:

| Audience | Form | Optimized for |
|----------|------|---------------|
| Agents | `INDEX.md` — a single very dense ~1-page list of 1–3-sentence pattern descriptions, each linking to its pattern file | Token efficiency, skim-and-select, fast task-start orientation |
| Humans | A generated wiki/website built from `patterns/` | Exploration, depth, browsability |

Day-one contribution and reading does **not** depend on the generated human site — GitHub natively renders the markdown and PRs work immediately.

## Chosen Approach

**Approach A: Content-first, minimal scaffolding, reuse existing wiki tooling.**

- The repo itself is the canonical source — markdown files, no database, no platform lock-in.
- The dense agent `INDEX.md` is **generated** from per-pattern files.
- Contribution rides entirely on **GitHub PR mechanics** — no custom intake tooling.
- The rich human website is produced as a **first run** from the content pile using **existing** tooling — no new tooling is built.

The discipline of this approach: prove the content's shape first, build machinery only once it is justified.

### Rejected Alternatives

- **B — Tooling-first (build a both-forms generator up front).** Rejected: risks building machinery before the content has proven its shape; the generator would likely be reworked once real patterns reveal which fields matter.
- **C — Adopt a wiki platform as the canonical home.** Rejected: couples the content format to a platform and fights the hand-tuned, dense agent-facing page requirement.

## Architecture & Content Model

### Repo Layout

```
agent-building-playbook/
├── README.md            # what this is; links to INDEX + SUBMISSIONS + how to contribute
├── INDEX.md             # THE dense agent page — GENERATED from patterns/, not hand-edited
├── SUBMISSIONS.md       # agent-authoring guide for a well-formed pattern PR
├── patterns/            # one file per pattern: light frontmatter + markdown "pearl" body
│   ├── leverage-dev-factory.md
│   ├── eval-centered-development.md
│   └── ...
└── scripts/
    └── build-index.sh   # tiny generator: patterns/*.md flat frontmatter (title, one_liner, dimensions) → INDEX.md
```

### Pattern File — the Atomic Unit

Each pattern is one file. **The filename is the canonical identifier** (there is no `id` field) — convention `{kebab-title}.md`. The file is flat frontmatter plus a markdown "pearl" body.

**Frontmatter (intentionally light — flat scalars / inline values only, so the bash generator stays trivial):**
- `title`
- `one_liner`
- `dimensions` — a **comma-separated inline list** of tags, e.g. `dimensions: context-engineering, reliability`. A pattern may carry multiple tags.

**Body (the "pearl"):** what the pattern is, when to reach for it, when **not** to, plus:
- **Exemplars** — a markdown list of concrete implementations/tools, each `name — url — one-line note`. Exemplars live in the **body**, not in frontmatter.
- **Related** — advisory cross-references to sibling patterns. Lives in the body (or a simple comma-separated frontmatter line); **not validated in v1**.

Keeping frontmatter flat (only `title`, `one_liner`, `dimensions`) means `build-index.sh` parses three simple lines and never has to walk nested YAML objects.

Schema is intentionally light — "good enough for now." Density and curation matter more than schema rigor.

### INDEX.md — the Hero Artifact

A single **very dense ~1-page** list of 1–3-sentence, plain/common-language pattern descriptions, each linking to its pattern file, **grouped by tag (`dimensions`)**. Because `dimensions` is multi-value, a pattern appears under **every** tag it carries — patterns are sortable/filterable by tag, and a single pattern may show under multiple headings. It is **generated** by `build-index.sh` from each pattern's `title`, `one_liner`, and `dimensions` (+ link), never hand-edited. Plain phrasing so a model can skim and select. Regenerating after a merge is one command.

No provenance elevation: personal, battle-tested lessons and external literature are treated as peers.

### Shelf Hierarchy — the `dimensions` Taxonomy

Seeded from the 10 themes already in the research dump, and allowed to grow:

1. meta-principles
2. workflow discipline
3. reliability / anti-cheating
4. context engineering
5. tool design
6. orchestration
7. verification / evals
8. cost / routing
9. observability
10. taste

## Contribution & Curation Flow

This is the data flow for how new patterns enter and get curated.

- **Submission rail = GitHub PRs.** No custom intake tooling.
- **`SUBMISSIONS.md` is an agent-authoring guide.** A contributor points their agent at it ("read this, produce a properly formatted pattern file and open a PR"). The README links to it.
- **Maintainer triage = a maintainer-agent flow (no new tooling).** The maintainer points their agent at the open PRs and gets back a dense triage:
  - which are new
  - where each fits in the hierarchy
  - a 2-sentence summary each
  - is it redundant, does it extend an existing pattern, or is it a secondary implementation of a known pattern

  so accept/reject is fast. The human maintainer decides; on merge, regenerate `INDEX.md`.
- **Curation discipline lives in PR review** at this scale — not in automation.

## SUBMISSIONS.md Specification

`SUBMISSIONS.md` is the **agent-authoring guide**: a contributor points their agent at it and the agent produces a valid pattern PR with zero ambiguity. The repo is **public under `ramparte`**, so anyone can fork and PR. `SUBMISSIONS.md` must contain all of the following.

### 1. Filename convention

- One pattern per file under `patterns/`.
- Filename = `{kebab-title}.md` (lowercase, hyphen-separated). **The filename is the canonical identifier** — there is no `id` field.
- Example: a pattern titled "Leverage the Dev Factory" → `patterns/leverage-dev-factory.md`.

### 2. Required frontmatter vs optional body

**Required frontmatter (flat YAML, three fields only):**

| Field | Type | Notes |
|-------|------|-------|
| `title` | string | Human-readable pattern name |
| `one_liner` | string | 1 sentence, plain language — feeds INDEX.md |
| `dimensions` | comma-separated inline list | One or more tags from the vocabulary below |

**Optional body sections:**

- **Exemplars** — markdown list, each `name — url — one-line note`.
- **Related** — advisory cross-references to sibling patterns (by filename or title). Not validated in v1.

### 3. Dimension tag vocabulary

`dimensions` is **multi-value** — comma-separated. Seed vocabulary (the 10 themes):

1. `meta-principles`
2. `workflow-discipline`
3. `reliability` (anti-cheating)
4. `context-engineering`
5. `tool-design`
6. `orchestration`
7. `verification` (evals)
8. `cost-routing`
9. `observability`
10. `taste`

**Rule:** if no existing tag fits, **propose a new one in the PR description** — never invent a tag silently in the file. Maintainers fold approved new tags into the vocabulary.

### 4. Body / "pearl" structure

The body is the pearl. In order:

1. **What it is** — the pattern in a few sentences.
2. **When to reach for it** — the trigger / context where it applies.
3. **When NOT to** — the anti-pattern boundary; where it misleads or costs more than it saves.
4. **Exemplars** — concrete implementations/tools as links (`name — url — one-line note`).
5. **Related** *(optional)* — sibling patterns.

### 5. One complete worked example (agents copy this)

````markdown
---
title: Eval-Centered Development
one_liner: Write the eval before the implementation so the agent optimizes against a measurable target instead of vibes.
dimensions: verification, workflow-discipline, reliability
---

## What it is

Treat the evaluation harness as the primary artifact. Before building a capability,
define how you will measure whether it works — a runnable eval with pass/fail cases —
then let the agent iterate against that target.

## When to reach for it

Any task where "looks right" is not the same as "is right": code generation, extraction,
classification, multi-step agent flows. Especially valuable when the agent will iterate
unattended.

## When NOT to

One-off throwaway scripts, or exploratory spikes where the goal is still being discovered
and a premature eval would lock in the wrong target.

## Exemplars

- promptfoo — https://github.com/promptfoo/promptfoo — declarative LLM eval runner.
- Amplifier eval recipes — internal — eval-first recipe scaffolding.

## Related

- leverage-dev-factory
- systematic-debugging
````

### 6. Contribution flow

1. **Fork** the public `ramparte` repo.
2. **Add** `patterns/{kebab-title}.md` following the spec above.
3. **Open a PR.**
4. **Do NOT edit `INDEX.md`** — it is generated by `build-index.sh` (and refreshed automatically by the GitHub Action on merge).

## Human-Readable Site (Tooling Pick + First Run)

- **Tooling pick:** use the `llm-wiki` bundle (bkrabach's, in Amplifier) to generate the human-readable website from `patterns/`.
- **Fallback:** if `llm-wiki` output isn't browsable enough for the offsite, use `amplifier-stories` (storyteller HTML). Try `llm-wiki` first. No new tooling is built.
- **Deadline de-risking:** day-one contribution does **not** depend on the generated site. GitHub natively renders `patterns/*.md`, `INDEX.md`, and `SUBMISSIONS.md`, and PRs work immediately. The generated wiki is a **first run** done once content is seeded, and **regenerated on demand** thereafter.

### Keeping INDEX.md Fresh — GitHub Action

A small (~10-line) GitHub Action keeps the hero artifact from going stale while contributions land at the offsite. It uses the **existing `build-index.sh`** — not new tooling:

- **Trigger:** push/merge to the `main` branch (under `paths: patterns/**`).
- **Steps:** check out the repo → run `scripts/build-index.sh` → if `INDEX.md` changed, commit and push the regenerated `INDEX.md` back to `main`.
- **Effect:** every merged pattern PR yields an up-to-date `INDEX.md` automatically; contributors never hand-edit it.

## Seed Content Plan

The research dump already exists at `/home/ramparte/dev/ANext/agent-building-playbook/README.md` (to be repurposed), holding ~40 distilled patterns across the 10 themes — this is the starting ore.

Execution work is mostly:

1. Split the dump into one `patterns/*.md` file each (pattern-per-concept, light frontmatter).
2. Write `build-index.sh` and generate `INDEX.md`.
3. Write `SUBMISSIONS.md` and the new `README.md`.
4. `git init` + first commit + create the GitHub repo.
5. One `llm-wiki` first-run to produce the site.

## Error Handling

- **Required fields:** `build-index.sh` requires `title`, `one_liner`, and `dimensions` in each pattern's frontmatter. If any is missing it must **fail loudly and name the offending file** rather than silently dropping it.
- **Atomic write:** the generator writes to a temp file and `mv`s it into place, so a mid-run failure never leaves a corrupt `INDEX.md`.
- **Stays simple:** because frontmatter is flat (three inline fields), no defensive nested-YAML parsing is needed. `related:` cross-references are **not validated in v1** (advisory only; deferred to a later post-pass).
- If the `llm-wiki` first run fails or produces an unbrowsable artifact, fall back to GitHub-rendered markdown for the offsite (contribution still works) and try the storyteller fallback afterward.

## Testing Strategy

This is content plus a tiny shell generator, so testing is lightweight and evidence-based:

1. Run `build-index.sh` and confirm `INDEX.md` regenerates with every seeded pattern present and grouped by dimension.
2. Confirm a deliberately malformed pattern file makes `build-index.sh` fail loudly.
3. Confirm the repo renders correctly on GitHub (README links resolve, patterns browse).
4. Confirm the `llm-wiki` first run produces a browsable site, or that the documented fallback path works.

No unit-test framework is needed for v1.

## Out of Scope (v1 / Deferred Post-Offsite)

Explicitly deferred — YAGNI:

- Automated triage tooling
- Periodic "librarian" reorganization passes
- Schema enforcement / validation tooling
- Custom site generators
- Strict provenance weighting
- `related:` cross-reference validation — advisory only in v1; a later post-pass may validate that referenced patterns exist

PR review plus the maintainer-agent triage cover curation by hand at this scale.

## Open Questions

- Exact repo name (the repo is **public, under the `ramparte` GitHub account** — visibility is decided; only the final name remains).
- Final `dimensions` taxonomy labels (seed from the 10 themes; expect to refine as patterns land).
- Whether `build-index.sh` stays bash or graduates to a small script later (bash is fine for v1).
