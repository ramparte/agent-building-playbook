# Agent-Building Playbook Implementation Plan

> **Execution:** Use the subagent-driven-development workflow to implement this plan.

**Goal:** Stand up the public `ramparte/agent-building-playbook` content repo — seed patterns, a generated dense `INDEX.md`, a fully-specified `SUBMISSIONS.md`, a project `README.md`, and a merge-time GitHub Action — so advanced practitioners can read and PR-contribute at the offsite tomorrow (2026-06-29).

**Architecture:** Markdown is the single canonical source. Each pattern is one file under `patterns/` with flat YAML frontmatter (`title`, `one_liner`, `dimensions`) plus a markdown "pearl" body. A tiny bash generator (`scripts/build-index.sh`) reads that frontmatter and emits the dense `INDEX.md`, grouped by tag (multi-value: a pattern appears under every tag it carries). GitHub renders everything natively; a ~10-line Action keeps `INDEX.md` fresh on merge.

**Tech Stack:** Plain bash + coreutils (awk/sed/sort/grep), GitHub Actions, GitHub-flavored markdown. No new runtime dependencies.

**Source of truth for content:** the existing research dump (currently `README.md`, preserved in Task A1 as `docs/seed-research-dump.md`) — ~65 distilled pattern bullets across 10 themed sections.

---

## How to use this plan

- Work top to bottom. Each task is 2–5 minutes. Do not skip the run/verify steps.
- `cd /home/ramparte/dev/ANext/agent-building-playbook` before starting. All paths below are relative to that repo root.
- Commit after every task using the exact message given (conventional commits).
- **Do NOT** create the GitHub repo or `git push` anywhere in this plan — that is the `/finish` phase (see the final section).
- Phases: **A** scaffold → **B** the generator (TDD) → **C** seed content → **D** generate INDEX + finalize README → **E** the Action.

---

## Phase A — Repo Scaffold

### Task A1: Create directories, preserve the research dump, add .gitignore

**Files:**
- Create dir: `patterns/`
- Create dir: `scripts/`
- Create dir: `tests/`
- Create dir: `.github/workflows/`
- Move: `README.md` → `docs/seed-research-dump.md` (preserve the dump; it is the seed ore for Phase C and must survive before we write the new README)
- Create: `.gitignore`

**Step 1: Make the directories and keep dirs tracked**

Run:
```bash
mkdir -p patterns scripts tests .github/workflows
touch patterns/.gitkeep
```
(`.gitkeep` keeps the empty `patterns/` dir in git until Phase C fills it; delete it in Task C1.)

**Step 2: Preserve the research dump**

Run:
```bash
git mv README.md docs/seed-research-dump.md
```
Expected: `README.md` no longer at repo root; `docs/seed-research-dump.md` now exists.

**Step 3: Write `.gitignore`**

Write `.gitignore`:
```gitignore
# OS / editor cruft
.DS_Store
*.swp

# Amplifier working dirs
.amplifier/
.superpowers/

# build-index scratch
*.tmp
```

**Step 4: Verify the structure**

Run:
```bash
ls -la patterns scripts tests .github/workflows docs/seed-research-dump.md
```
Expected: all four directories listed and `docs/seed-research-dump.md` present.

**Step 5: Commit**

Run:
```bash
git add -A && git commit -m "chore: scaffold dirs, preserve research dump, add .gitignore"
```

---

### Task A2: Write `SUBMISSIONS.md` (full spec, copy verbatim)

**Files:**
- Create: `SUBMISSIONS.md`

This content is the authoritative agent-authoring guide from the design's "SUBMISSIONS.md Specification" section. Reproduce it exactly.

**Step 1: Write `SUBMISSIONS.md`**

Write `SUBMISSIONS.md`:
````markdown
# Submitting a Pattern

This repo is a curated, growing collection of **patterns** for building better in the
agentic age. This guide tells you (or your agent) how to produce a well-formed pattern and
open a PR with zero ambiguity. The repo is **public** — anyone can fork and PR.

Point your agent at this file: *"Read SUBMISSIONS.md, then produce a properly formatted
pattern file and open a PR."*

## 1. Filename convention

- One pattern per file under `patterns/`.
- Filename = `{kebab-title}.md` (lowercase, hyphen-separated).
  **The filename is the canonical identifier** — there is no `id` field.
- Example: a pattern titled "Leverage the Dev Factory" → `patterns/leverage-dev-factory.md`.

## 2. Required frontmatter vs optional body

**Required frontmatter (flat YAML, three fields only):**

| Field | Type | Notes |
|-------|------|-------|
| `title` | string | Human-readable pattern name |
| `one_liner` | string | 1 sentence, plain language — feeds `INDEX.md` |
| `dimensions` | comma-separated inline list | One or more tags from the vocabulary below |

Keep frontmatter **flat** — three inline scalar lines only. Do not nest YAML; the index
generator parses these three lines and nothing else.

**Optional body sections:**

- **Exemplars** — markdown list, each `name — url — one-line note`.
- **Related** — advisory cross-references to sibling patterns (by filename or title).
  Not validated in v1.

## 3. Dimension tag vocabulary

`dimensions` is **multi-value** — comma-separated. A pattern appears in `INDEX.md` under
**every** tag it carries. Seed vocabulary (the 10 themes):

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

**Rule:** if no existing tag fits, **propose a new one in the PR description** — never
invent a tag silently in the file. Maintainers fold approved new tags into the vocabulary.

## 4. Body / "pearl" structure

The body is the pearl. In order:

1. **What it is** — the pattern in a few sentences.
2. **When to reach for it** — the trigger / context where it applies.
3. **When NOT to** — the anti-pattern boundary; where it misleads or costs more than it saves.
4. **Exemplars** — concrete implementations/tools as links (`name — url — one-line note`).
5. **Related** *(optional)* — sibling patterns.

## 5. One complete worked example (copy this shape)

```markdown
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
```

## 6. Contribution flow

1. **Fork** this public repo.
2. **Add** `patterns/{kebab-title}.md` following the spec above.
3. **Open a PR.**
4. **Do NOT edit `INDEX.md`** — it is generated by `scripts/build-index.sh` and refreshed
   automatically by the GitHub Action on merge.
````

**Step 2: Verify it rendered as intended (no broken fences)**

Run:
```bash
grep -c '^#' SUBMISSIONS.md
```
Expected: a non-zero count (several headings present).

**Step 3: Commit**

Run:
```bash
git add SUBMISSIONS.md && git commit -m "docs: add SUBMISSIONS.md agent-authoring guide"
```

---

### Task A3: Write the new project `README.md`

**Files:**
- Create: `README.md` (the old one is now `docs/seed-research-dump.md`, so this is a fresh file)

**Step 1: Write `README.md`**

Write `README.md`:
```markdown
# Agent-Building Playbook

A curated, growing collection of **patterns** for building better in the agentic age —
"Programming Pearls, but actionable and for the cognitive-architecture era." The subject is
**how to build better**, not narrowly how to build agents.

One canonical source (markdown in this repo) serves two audiences:

- **Agents** read [`INDEX.md`](./INDEX.md) — a dense, token-efficient list of every pattern
  with a one-line description, grouped by tag, each linking to its full file.
- **Humans** browse the `patterns/` directory directly on GitHub, or a generated wiki built
  from the same content.

## Repo layout

| Path | What it is |
|------|------------|
| [`INDEX.md`](./INDEX.md) | The dense agent-facing index. **Generated — do not hand-edit.** |
| [`SUBMISSIONS.md`](./SUBMISSIONS.md) | How to write a pattern and open a PR. |
| `patterns/` | One file per pattern: flat frontmatter + a markdown "pearl" body. |
| `scripts/build-index.sh` | Regenerates `INDEX.md` from `patterns/`. |

## Contributing

1. Read [`SUBMISSIONS.md`](./SUBMISSIONS.md) — or point your agent at it.
2. Add `patterns/{kebab-title}.md`.
3. Open a PR. **Don't edit `INDEX.md`** — it regenerates automatically on merge.

## Regenerating the index locally

```bash
scripts/build-index.sh
```

This reads every `patterns/*.md` and rewrites `INDEX.md`. A GitHub Action runs the same
script on merge to `main`, so the index stays fresh as patterns land.

## Provenance

Patterns are distilled from external literature, battle-tested session history, and the
Amplifier team ecosystem. Personal lessons and external literature are treated as peers —
no provenance weighting in v1. The original research dump that seeded this repo is preserved
at [`docs/seed-research-dump.md`](./docs/seed-research-dump.md).
```

**Step 2: Verify links point at files that exist or will exist**

Run:
```bash
grep -o '](\./[^)]*)' README.md
```
Expected: references to `./INDEX.md`, `./SUBMISSIONS.md`, `./docs/seed-research-dump.md`. (`INDEX.md` doesn't exist yet — it's generated in Phase D. That's fine.)

**Step 3: Commit**

Run:
```bash
git add README.md && git commit -m "docs: add project README"
```

---

## Phase B — `build-index.sh` (the only real code; full TDD)

This is the single testable unit. We write the test first, watch it fail, implement the
happy path, watch it pass, then drive the fail-loud validation with a second failing test.
Keep the script **simple — flat frontmatter only, no nested-YAML parsing.** Do **not**
validate `related:` (deferred).

### Task B1: Write the happy-path test and watch it fail

**Files:**
- Create: `tests/test_build_index.sh`

**Step 1: Write the failing test**

Write `tests/test_build_index.sh`:
```bash
#!/usr/bin/env bash
# Happy-path test for build-index.sh.
# Builds INDEX from 3 fixture patterns and asserts multi-value tagging works:
# a pattern with two dimensions appears under BOTH tag headings.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$SCRIPT_DIR/scripts/build-index.sh"

fail() { echo "FAIL: $1" >&2; exit 1; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
PATTERNS="$WORK/patterns"
mkdir -p "$PATTERNS"

cat > "$PATTERNS/alpha-pattern.md" <<'EOF'
---
title: Alpha Pattern
one_liner: Alpha does the first thing clearly.
dimensions: meta-principles, reliability
---
## What it is
Alpha.
EOF

cat > "$PATTERNS/beta-pattern.md" <<'EOF'
---
title: Beta Pattern
one_liner: Beta handles the second case.
dimensions: reliability
---
## What it is
Beta.
EOF

cat > "$PATTERNS/gamma-pattern.md" <<'EOF'
---
title: Gamma Pattern
one_liner: Gamma covers the third path.
dimensions: orchestration
---
## What it is
Gamma.
EOF

OUT="$WORK/INDEX.md"

"$BUILD" "$PATTERNS" "$OUT" || fail "build-index.sh exited non-zero on valid fixtures"
[ -f "$OUT" ] || fail "INDEX.md was not created"

grep -q "## meta-principles" "$OUT" || fail "missing '## meta-principles' heading"
grep -q "## reliability"     "$OUT" || fail "missing '## reliability' heading"
grep -q "## orchestration"   "$OUT" || fail "missing '## orchestration' heading"

# Multi-value: Alpha carries two tags, so its title must appear at least twice.
alpha_count="$(grep -c "Alpha Pattern" "$OUT")"
[ "$alpha_count" -ge 2 ] || fail "Alpha Pattern should appear under both its tags (found $alpha_count)"

grep -q "Alpha does the first thing clearly." "$OUT" || fail "Alpha one_liner missing"
grep -q "Beta handles the second case."       "$OUT" || fail "Beta one_liner missing"
grep -q "Gamma covers the third path."         "$OUT" || fail "Gamma one_liner missing"
grep -q "alpha-pattern.md" "$OUT" || fail "Alpha link missing"

echo "HAPPY-PATH TEST PASSED"
```

**Step 2: Make it executable and run it to verify it FAILS**

Run:
```bash
chmod +x tests/test_build_index.sh
bash tests/test_build_index.sh; echo "exit=$?"
```
Expected: FAIL — `build-index.sh` does not exist yet, so the test prints
`FAIL: build-index.sh exited non-zero on valid fixtures` (or a "No such file" error) and
`exit=1`.

**Step 3: Commit the failing test**

Run:
```bash
git add tests/test_build_index.sh && git commit -m "test: add happy-path test for build-index.sh"
```

---

### Task B2: Implement the happy-path generator and watch the test pass

**Files:**
- Create: `scripts/build-index.sh`

> Implement **only the happy path here — no required-field validation yet.** The validation
> is driven by the failing test in Task B3 (genuine red→green).

**Step 1: Write `scripts/build-index.sh`**

Write `scripts/build-index.sh`:
```bash
#!/usr/bin/env bash
# build-index.sh — generate INDEX.md from patterns/*.md flat frontmatter.
#
# Usage: scripts/build-index.sh [PATTERNS_DIR] [OUTPUT_FILE]
#   PATTERNS_DIR defaults to "patterns"
#   OUTPUT_FILE  defaults to "INDEX.md"
#
# Each pattern file has flat frontmatter between the first two '---' lines:
#   title: ...
#   one_liner: ...
#   dimensions: tag-a, tag-b
# A pattern appears under EVERY tag in its comma-separated `dimensions`.
set -euo pipefail

PATTERNS_DIR="${1:-patterns}"
OUTPUT_FILE="${2:-INDEX.md}"

if [ ! -d "$PATTERNS_DIR" ]; then
  echo "ERROR: patterns directory not found: $PATTERNS_DIR" >&2
  exit 1
fi

rows="$(mktemp)"
tmp_out="$(mktemp)"
trap 'rm -f "$rows" "$tmp_out"' EXIT

# extract_field FIELD FILE — print the value of a flat frontmatter field, trimmed.
# Only scans inside the frontmatter block (first '---' to next '---').
extract_field() {
  awk -v field="$1" '
    NR==1 && $0=="---" { infm=1; next }
    infm && $0=="---" { exit }
    infm {
      if (index($0, field ":") == 1) {
        val = substr($0, length(field) + 2)
        sub(/^[ \t]+/, "", val)
        sub(/[ \t]+$/, "", val)
        print val
        exit
      }
    }
  ' "$2"
}

shopt -s nullglob
files=("$PATTERNS_DIR"/*.md)
if [ ${#files[@]} -eq 0 ]; then
  echo "ERROR: no pattern files found in $PATTERNS_DIR" >&2
  exit 1
fi

for f in "${files[@]}"; do
  title="$(extract_field title "$f")"
  one_liner="$(extract_field one_liner "$f")"
  dimensions="$(extract_field dimensions "$f")"

  IFS=',' read -ra tags <<< "$dimensions"
  for tag in "${tags[@]}"; do
    tag="$(echo "$tag" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')"
    [ -z "$tag" ] && continue
    # row: tag <TAB> title <TAB> path <TAB> one_liner
    printf '%s\t%s\t%s\t%s\n' "$tag" "$title" "$f" "$one_liner" >> "$rows"
  done
done

{
  echo "# INDEX — Agent-Building Playbook"
  echo
  echo "> GENERATED FILE — do not edit by hand. Regenerate with \`scripts/build-index.sh\`."
  echo "> Dense, skim-and-select pattern list. Patterns appear under every tag they carry."
  echo
} > "$tmp_out"

tags_sorted="$(cut -f1 "$rows" | sort -u)"
while IFS= read -r tag; do
  [ -z "$tag" ] && continue
  {
    echo "## $tag"
    echo
  } >> "$tmp_out"
  awk -F'\t' -v t="$tag" '$1==t' "$rows" | sort -t"$(printf '\t')" -k2,2 \
    | while IFS="$(printf '\t')" read -r _tag title path one_liner; do
        printf -- '- [%s](%s) — %s\n' "$title" "$path" "$one_liner" >> "$tmp_out"
      done
  echo >> "$tmp_out"
done <<< "$tags_sorted"

mv "$tmp_out" "$OUTPUT_FILE"
echo "Wrote $OUTPUT_FILE" >&2
```

**Step 2: Make it executable and run the happy-path test — expect PASS**

Run:
```bash
chmod +x scripts/build-index.sh
bash tests/test_build_index.sh; echo "exit=$?"
```
Expected: `HAPPY-PATH TEST PASSED` and `exit=0`.

**Step 3: Commit**

Run:
```bash
git add scripts/build-index.sh && git commit -m "feat: add build-index.sh generator (happy path)"
```

---

### Task B3: Drive fail-loud validation with a second failing test

**Files:**
- Create: `tests/test_build_index_malformed.sh`
- Modify: `scripts/build-index.sh` (add the required-field validation block)

**Step 1: Write the failing malformed-input test**

Write `tests/test_build_index_malformed.sh`:
```bash
#!/usr/bin/env bash
# Malformed-input test: a pattern missing `one_liner` must make build-index.sh
# exit non-zero AND name the offending file.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$SCRIPT_DIR/scripts/build-index.sh"

fail() { echo "FAIL: $1" >&2; exit 1; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
PATTERNS="$WORK/patterns"
mkdir -p "$PATTERNS"

# Missing `one_liner`.
cat > "$PATTERNS/broken-pattern.md" <<'EOF'
---
title: Broken Pattern
dimensions: taste
---
## What it is
No one_liner here.
EOF

ERROUT="$("$BUILD" "$PATTERNS" "$WORK/INDEX.md" 2>&1)"
RC=$?

[ "$RC" -ne 0 ] || fail "build-index.sh should exit non-zero on a pattern missing required fields"
echo "$ERROUT" | grep -q "broken-pattern.md" || fail "error message must name the offending file (broken-pattern.md)"

echo "MALFORMED-INPUT TEST PASSED"
```

**Step 2: Run it — expect FAIL**

Run:
```bash
chmod +x tests/test_build_index_malformed.sh
bash tests/test_build_index_malformed.sh; echo "exit=$?"
```
Expected: FAIL — the current script does not validate, so it exits 0 (or writes a row with an
empty one_liner). The test prints
`FAIL: build-index.sh should exit non-zero on a pattern missing required fields` and `exit=1`.

**Step 3: Add the fail-loud validation block to `scripts/build-index.sh`**

In `scripts/build-index.sh`, find this block:
```bash
  title="$(extract_field title "$f")"
  one_liner="$(extract_field one_liner "$f")"
  dimensions="$(extract_field dimensions "$f")"

  IFS=',' read -ra tags <<< "$dimensions"
```
and insert the validation between the `dimensions=` line and the `IFS=','` line so it reads:
```bash
  title="$(extract_field title "$f")"
  one_liner="$(extract_field one_liner "$f")"
  dimensions="$(extract_field dimensions "$f")"

  if [ -z "$title" ] || [ -z "$one_liner" ] || [ -z "$dimensions" ]; then
    echo "ERROR: $f is missing one or more required frontmatter fields (title, one_liner, dimensions)" >&2
    exit 1
  fi

  IFS=',' read -ra tags <<< "$dimensions"
```

**Step 4: Run BOTH tests — expect PASS**

Run:
```bash
bash tests/test_build_index.sh; echo "happy exit=$?"
bash tests/test_build_index_malformed.sh; echo "malformed exit=$?"
```
Expected: `HAPPY-PATH TEST PASSED` (`happy exit=0`) and `MALFORMED-INPUT TEST PASSED`
(`malformed exit=0`). The validation does not break the happy path.

**Step 5: Commit**

Run:
```bash
git add scripts/build-index.sh tests/test_build_index_malformed.sh && \
  git commit -m "feat: fail loud and name file on missing required frontmatter"
```

---

## Phase C — Seed Content

Split `docs/seed-research-dump.md` into one `patterns/{kebab-title}.md` per bullet. This is
**authoring** work, not TDD. One task per themed section of the dump.

**Shared rules for every pattern file (apply to all of Phase C):**

- Filename = `{kebab-title}.md` exactly as given in each task's table.
- Frontmatter is the three flat fields only: `title`, `one_liner`, `dimensions`.
  - `one_liner` = the bullet's lead idea in one plain sentence (you may lightly reword the
    dump's sentence; keep it skimmable for an agent).
  - `dimensions` = the tags given in the table (comma-separated, multi-value where listed).
- Body, in order: `## What it is`, `## When to reach for it`, `## When NOT to`
  (write a sensible boundary from the bullet's intent; if genuinely unknown, write one honest
  sentence — do not invent specifics), then `## Exemplars`.
- `## Exemplars` — draw from the dump's "Repos, Tools & Frameworks" table and "Primary
  Sources" list where the bullet maps to one. Format each line `name — url — one-line note`.
  If no concrete exemplar fits, cite the relevant primary source for that theme (URLs below),
  or omit the section (it is optional). **Do not fabricate URLs.**
- Do **not** write an `INDEX.md` — it is generated in Phase D.

**Primary-source URLs (use as exemplars; copied from the dump — do not invent others):**

| Tag shorthand | URL |
|---|---|
| Drew Breunig — 10 Lessons | https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html |
| Anthropic — context engineering | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Anthropic — writing tools | https://www.anthropic.com/engineering/writing-tools-for-agents |
| Anthropic — code execution w/ MCP | https://www.anthropic.com/engineering/code-execution-with-mcp |
| Anthropic — building effective agents | https://www.anthropic.com/research/building-effective-agents |
| Anthropic — demystifying evals | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| LangChain — context engineering | https://www.langchain.com/blog/context-engineering-for-agents |
| Cognition — Don't Build Multi-Agents | https://cognition.com/blog/dont-build-multi-agents |
| OpenAI — practical guide to agents | https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ |
| Simon Willison — agentic patterns | https://simonwillison.net/guides/agentic-engineering-patterns/ |
| DeepEval — eval-driven development | https://deepeval.com/blog/eval-driven-development |
| Amplifier | https://github.com/microsoft/amplifier |

### Task C1: Seed section 0 — Meta-Principles (6 files)

**Files (create each under `patterns/`):**

| Filename | title | dimensions | Source bullet (dump section 0) |
|----------|-------|------------|-------------------------|
| `verify-independently.md` | Verify Independently — Agents Fake "Done" | `meta-principles, reliability` | #1 unobservable step is unrun; "complete" is a claim to verify |
| `fail-loud-harnesses.md` | Fail-Loud Harnesses | `meta-principles, reliability, tool-design` | #2 a failing agent silently does the work itself; build harnesses that fail loud |
| `reliability-before-features.md` | Fix Reliability Before Features | `meta-principles, reliability` | #3 flakiness, not capability, is the enemy |
| `code-is-cheap-maintenance-isnt.md` | Code Is Cheap, Maintenance Isn't | `meta-principles` | #4 free as in puppies; mind support/security/maintenance |
| `context-is-finite.md` | Context Is a Finite Resource | `meta-principles, context-engineering` | #5 curate smallest high-signal token set |
| `start-least-agentic.md` | Start With the Least Agentic Thing | `meta-principles, orchestration` | #6 many problems need one good LLM call, not an autonomous agent |

**Step 1:** First remove the placeholder: `git rm patterns/.gitkeep` (if it exists).

**Step 2:** Author each file per the shared rules above. Worked example — write
`patterns/verify-independently.md` exactly like this to set the shape for the rest:
```markdown
---
title: Verify Independently — Agents Fake "Done"
one_liner: Treat an agent's "complete" as a claim to verify, never a fact — an unobservable step is an unrun step.
dimensions: meta-principles, reliability
---

## What it is

Agents will report success they have not earned. Every step that cannot be independently
observed should be treated as unrun until a verification command confirms it. "Done" is a
hypothesis; evidence is the test.

## When to reach for it

Any unattended or multi-step agent run, especially pipelines where one stage's output feeds
the next. The higher the autonomy, the more this matters.

## When NOT to

Trivial, fully-observable single actions where the result is its own proof — verifying them
adds ceremony without reducing risk.

## Exemplars

- Amplifier verification-before-completion discipline — https://github.com/microsoft/amplifier — evidence-before-assertions gate before any "done" claim.
```

**Step 3: Commit**

Run:
```bash
git add patterns/ && git commit -m "content: seed meta-principles patterns"
```

### Task C2: Seed section 1 — Workflow Discipline (9 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `implement-to-learn.md` | Implement to Learn | `workflow-discipline` |
| `keep-specs-in-sync.md` | Keep Specs in Sync | `workflow-discipline` |
| `document-intent.md` | Document Intent, Not Just Method | `workflow-discipline` |
| `rebuild-often.md` | Rebuild Often | `workflow-discipline` |
| `gate-the-phases.md` | Gate the Phases Explicitly | `workflow-discipline` |
| `prove-on-small-sample.md` | Prove the Pipeline on 2 Before 20 | `workflow-discipline, reliability` |
| `decompose-on-timeout.md` | Decompose and Retry on Timeout | `workflow-discipline, orchestration` |
| `bite-sized-tasks.md` | Bite-Sized Tasks | `workflow-discipline` |
| `clear-stop-condition.md` | Hand Off With a Clear Stop Condition | `workflow-discipline, orchestration` |

Author each per the shared rules (source = dump section 1 bullets, in order). Then:
```bash
git add patterns/ && git commit -m "content: seed workflow-discipline patterns"
```

### Task C3: Seed section 2 — Reliability & Anti-Cheating (7 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `demand-independent-proof.md` | Demand Independent Proof, Not a Status Report | `reliability` |
| `auditable-artifacts.md` | Make Every Stage Produce an Auditable Artifact | `reliability, observability` |
| `auditor-agent.md` | Use a Second Agent as Auditor | `reliability, orchestration` |
| `proposer-authority-separation.md` | Separate the Proposer From the Authority | `reliability, orchestration` |
| `mark-skipped-steps.md` | Mark Un-Run Steps Inline for Review | `reliability, observability` |
| `recipe-not-conversation.md` | Encode Multi-Step Work as a Recipe | `reliability, workflow-discipline` |
| `fail-loud-over-fallbacks.md` | Fail Loud Over Fallbacks | `reliability` |

Author each per the shared rules (source = dump section 2). Then:
```bash
git add patterns/ && git commit -m "content: seed reliability patterns"
```

### Task C4: Seed section 3 — Context Engineering (8 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `context-over-prompt.md` | Context Engineering Over Prompt Engineering | `context-engineering` |
| `write-select-compress-isolate.md` | Four Moves: Write, Select, Compress, Isolate | `context-engineering` |
| `just-in-time-retrieval.md` | Just-in-Time Retrieval Over Pre-Loading | `context-engineering` |
| `checkpoint-handoff-file.md` | Checkpoint to a Handoff File, Then Restart Clean | `context-engineering, workflow-discipline` |
| `persist-environment-facts.md` | Persist Environment Facts | `context-engineering` |
| `subagents-as-context-sinks.md` | Use Sub-Agents as Context Sinks | `context-engineering, orchestration` |
| `thin-pointers.md` | Thin Pointers, Zero Poisoning | `context-engineering, orchestration` |
| `long-horizon-memory.md` | Long-Horizon Memory: Compaction, Notes, Isolation | `context-engineering` |

Author each per the shared rules (source = dump section 3). Then:
```bash
git add patterns/ && git commit -m "content: seed context-engineering patterns"
```

### Task C5: Seed section 4 — Tool Design (5 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `tools-for-agents.md` | Design Tools for Agents, Not Humans | `tool-design` |
| `search-over-list.md` | Prefer Search/Filter Over List-Everything | `tool-design, context-engineering` |
| `namespace-tools.md` | Namespace Tools, Write Unambiguous Descriptions | `tool-design` |
| `agents-optimize-tools.md` | Let Agents Evaluate and Optimize Your Tools | `tool-design, verification` |
| `code-execution-tools.md` | Code Execution Beats Loading Hundreds of Tool Defs | `tool-design, context-engineering` |

Author each per the shared rules (source = dump section 4). Then:
```bash
git add patterns/ && git commit -m "content: seed tool-design patterns"
```

### Task C6: Seed section 5 — Orchestration & Multi-Agent (11 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `single-threaded-default.md` | Default to a Single-Threaded Linear Agent | `orchestration` |
| `share-full-context.md` | Share Full Context; Every Action Carries Decisions | `orchestration` |
| `workflows-vs-agents.md` | Distinguish Workflows From Agents | `orchestration` |
| `composable-patterns.md` | Composable Orchestration Patterns | `orchestration` |
| `clean-slate-delegation.md` | Default to Clean-Slate Delegation | `orchestration, context-engineering` |
| `recon-before-action.md` | Lead With Recon Before Action | `orchestration` |
| `parallel-independent-tracks.md` | Run Independent Agents in Parallel | `orchestration` |
| `architect-then-builder.md` | Two-Phase Build: Architect Then Builder | `orchestration, workflow-discipline` |
| `autonomy-when-justified.md` | Add Autonomy Only When Justified | `orchestration` |
| `three-primitives.md` | Build From Three Primitives | `orchestration, tool-design` |
| `guardrails-and-escalation.md` | Layer Guardrails and Human Escalation | `orchestration, reliability` |

Author each per the shared rules (source = dump section 5). Then:
```bash
git add patterns/ && git commit -m "content: seed orchestration patterns"
```

### Task C7: Seed section 6 — Verification & Evals (8 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `design-the-loop.md` | Designing the Agentic Loop Is the Core Skill | `verification` |
| `self-verification.md` | Give Agents the Ability to Verify Their Own Work | `verification, reliability` |
| `test-what-not-how.md` | Test What the Product Does, Not How | `verification` |
| `eval-driven-development.md` | Eval-Driven Development | `verification, workflow-discipline` |
| `standing-eval-capability.md` | Evals Are a Standing Capability, Not a One-Time Gate | `verification` |
| `tests-first-on-api-change.md` | Tests Are Code — Update Them First on API Change | `verification, workflow-discipline` |
| `three-file-rule.md` | Incremental Validation: The 3-File Rule | `verification, workflow-discipline` |
| `evidence-before-assertions.md` | Evidence Before Assertions | `verification, reliability` |

Author each per the shared rules (source = dump section 6). Then:
```bash
git add patterns/ && git commit -m "content: seed verification patterns"
```

### Task C8: Seed section 7 — Cost & Model Routing (3 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `match-model-to-stage.md` | Match Model to Stage | `cost-routing` |
| `role-based-routing.md` | Pull Models From Provisioned Roles | `cost-routing` |
| `delegation-token-economics.md` | Delegation Is Token Economics | `cost-routing, context-engineering, orchestration` |

Author each per the shared rules (source = dump section 7). Then:
```bash
git add patterns/ && git commit -m "content: seed cost-routing patterns"
```

### Task C9: Seed section 8 — Environment & Observability (4 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `real-environment-execution.md` | Run Real Workloads in Their Proper Environment | `observability` |
| `emit-events.md` | If It's Important, Emit an Event | `observability` |
| `awareness-layer.md` | Build an Awareness Layer That Watches Your Work | `observability` |
| `session-archaeology.md` | Use Session History as Primary Evidence | `observability` |

Author each per the shared rules (source = dump section 8). Then:
```bash
git add patterns/ && git commit -m "content: seed observability patterns"
```

### Task C10: Seed section 9 — Taste & Expertise (4 files)

| Filename | title | dimensions |
|----------|-------|------------|
| `find-the-hard-stuff.md` | Find the Hard Stuff | `taste` |
| `develop-your-taste.md` | Develop Your Taste | `taste` |
| `agents-amplify-experience.md` | Agents Amplify Experience | `taste` |
| `automate-but-avoid-mystery-house.md` | Automate the Easy, Avoid the Mystery House | `taste, workflow-discipline` |

Author each per the shared rules (source = dump section 9). Then:
```bash
git add patterns/ && git commit -m "content: seed taste patterns"
```

---

## Phase D — Generate `INDEX.md` and finalize

### Task D1: Generate the real `INDEX.md` and sanity-check it

**Files:**
- Create: `INDEX.md` (generated)

**Step 1: Run the generator over the real patterns**

Run:
```bash
scripts/build-index.sh
```
Expected: prints `Wrote INDEX.md` to stderr; `INDEX.md` now exists at repo root.

**Step 2: Sanity-check the output**

Run:
```bash
echo "patterns:"; ls patterns/*.md | wc -l
echo "index entries:"; grep -c '^- \[' INDEX.md
echo "tag headings:"; grep -c '^## ' INDEX.md
```
Expected: `patterns` count ~65 (the number of files you authored in Phase C); `index entries`
>= patterns count (multi-tagged patterns appear more than once); `tag headings` <= 10 (the
seed vocabulary actually used). Confirm a multi-tag pattern (e.g. "Verify Independently")
appears under more than one heading:
```bash
grep -c "Verify Independently" INDEX.md
```
Expected: >= 2.

**Step 3: Confirm there are no missing-field failures**

(If `build-index.sh` had exited non-zero in Step 1, it would have named the offending file.
Re-run if you fixed any file.) Run:
```bash
scripts/build-index.sh && echo "INDEX OK"
```
Expected: `INDEX OK`.

**Step 4: Commit**

Run:
```bash
git add INDEX.md && git commit -m "content: generate INDEX.md from seeded patterns"
```

---

## Phase E — GitHub Action to keep `INDEX.md` fresh

### Task E1: Add the merge-time index-rebuild workflow

**Files:**
- Create: `.github/workflows/build-index.yml`

**Step 1: Write the workflow**

Write `.github/workflows/build-index.yml`:
```yaml
name: Build INDEX

on:
  push:
    branches: [main]
    paths:
      - "patterns/**"
      - "scripts/build-index.sh"

permissions:
  contents: write

jobs:
  build-index:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Regenerate INDEX.md
        run: bash scripts/build-index.sh
      - name: Commit if changed
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: regenerate INDEX.md [skip ci]"
          file_pattern: INDEX.md
```

**Step 2: Validate the YAML parses**

Run:
```bash
python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/build-index.yml')); print('YAML OK')"
```
Expected: `YAML OK`.

**Step 3: Commit**

Run:
```bash
git add .github/workflows/build-index.yml && \
  git commit -m "ci: regenerate INDEX.md on merge to main"
```

> Note: the design specifies the trigger branch as `main`. This repo's current local branch is
> `master`. The Action targets `main`; align the published default branch to `main` at publish
> time (see below), or change `branches: [main]` to match the chosen default branch.

---

## Final verification (run before declaring the plan complete)

Run, from the repo root:
```bash
bash tests/test_build_index.sh
bash tests/test_build_index_malformed.sh
scripts/build-index.sh && echo "INDEX regenerated clean"
git status --short
ls README.md SUBMISSIONS.md INDEX.md scripts/build-index.sh .github/workflows/build-index.yml docs/seed-research-dump.md
```
Expected: both tests print `... TEST PASSED`; `INDEX regenerated clean`; a clean working tree
(everything committed); all listed files present.

---

## Publishing (do in `/finish`, NOT in execution)

These steps create the public repo and push — they are **out of the execution body** and must
be done in the finish phase, after the plan above is complete and verified:

1. Create the public repo under the `ramparte` account:
   `gh repo create ramparte/agent-building-playbook --public --source . --remote origin`
2. Set the default branch to `main` (to match the Action trigger), then `git push -u origin main`.
3. Confirm GitHub renders `README.md`, `SUBMISSIONS.md`, `INDEX.md`, and `patterns/*.md`, and
   that the contribution links resolve.

## Follow-up (post-seed, manual — NOT a task in this plan)

Once content is seeded and pushed, do a **single first run** of the human-readable site using
the existing `llm-wiki` bundle over `patterns/` (fallback: `amplifier-stories` storyteller
HTML; final fallback: GitHub-rendered markdown, which already works for the offsite). This is a
manual generation run, not part of this code plan, and is regenerated on demand thereafter.

## Out of scope (v1 / deferred)

Not planned here: automated triage tooling, periodic librarian reorganization passes,
schema-enforcement tooling, custom site generators, `related:` cross-reference validation. PR
review plus the maintainer-agent triage cover curation by hand at this scale.
