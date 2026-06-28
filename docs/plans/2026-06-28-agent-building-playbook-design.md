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
    └── build-index.sh   # tiny generator: patterns/*.md frontmatter → INDEX.md
```

### Pattern File — the Atomic Unit

Each pattern is one file: light frontmatter plus a markdown "pearl" body.

**Frontmatter (intentionally light):**
- `id`
- `title`
- `one_liner`
- `dimensions`
- `exemplars` — each = name + url + one-line note
- `related`

**Body (the "pearl"):** what the pattern is, when to reach for it, and a couple of exemplar implementations/tools as links.

Schema is intentionally light — "good enough for now." Density and curation matter more than schema rigor.

### INDEX.md — the Hero Artifact

A single **very dense ~1-page** list of 1–3-sentence, plain/common-language pattern descriptions, each linking to its pattern file, **grouped by `dimension`**. It is **generated** by `build-index.sh` from each pattern's `title` + `one_liner` (+ link), never hand-edited. Plain phrasing so a model can skim and select. Regenerating after a merge is one command.

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

## Human-Readable Site (Tooling Pick + First Run)

- **Tooling pick:** use the `llm-wiki` bundle (bkrabach's, in Amplifier) to generate the human-readable website from `patterns/`.
- **Fallback:** if `llm-wiki` output isn't browsable enough for the offsite, use `amplifier-stories` (storyteller HTML). Try `llm-wiki` first. No new tooling is built.
- **Deadline de-risking:** day-one contribution does **not** depend on the generated site. GitHub natively renders `patterns/*.md`, `INDEX.md`, and `SUBMISSIONS.md`, and PRs work immediately. The generated wiki is a **first run** done once content is seeded, and **regenerated on demand** thereafter.

## Seed Content Plan

The research dump already exists at `/home/ramparte/dev/ANext/agent-building-playbook/README.md` (to be repurposed), holding ~40 distilled patterns across the 10 themes — this is the starting ore.

Execution work is mostly:

1. Split the dump into one `patterns/*.md` file each (pattern-per-concept, light frontmatter).
2. Write `build-index.sh` and generate `INDEX.md`.
3. Write `SUBMISSIONS.md` and the new `README.md`.
4. `git init` + first commit + create the GitHub repo.
5. One `llm-wiki` first-run to produce the site.

## Error Handling

- `build-index.sh` must **fail loudly and name the offending file** if a pattern is missing required frontmatter (`title`, `one_liner`) rather than silently dropping it.
- Pattern `id` collisions and broken `related:` links should be **surfaced by the build step** (warn, name the file).
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

PR review plus the maintainer-agent triage cover curation by hand at this scale.

## Open Questions

- Exact repo name and GitHub org/visibility (assume public; confirm at execution).
- Final `dimensions` taxonomy labels (seed from the 10 themes; expect to refine as patterns land).
- Whether `build-index.sh` stays bash or graduates to a small script later (bash is fine for v1).
