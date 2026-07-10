---
title: Keep Specs in Sync
one_liner: A spec that diverges from the implementation is worse than no spec — it actively misleads every agent that reads it.
dimensions: workflow-discipline
---

## What it is

Specifications and implementations drift the moment they are separated. A spec written before implementation is an aspiration; after implementation begins, it is a liability if not updated. When an agent (or a human) reads a stale spec and builds on it, the resulting work diverges from reality in ways that compound — each layer of work built on the wrong foundation multiplies the rework cost. Keeping specs in sync means treating specification updates as part of the implementation task, not as documentation cleanup to be deferred. The spec is the source of truth for what the system is *supposed* to do; the code is the evidence of what it *actually* does. Both must be current.

Drift has a second, subtler source: intent itself is not static. As stakeholders react to concrete artifacts, their understanding of what they want changes, so a spec written cleanly at the start can be wrong by the middle of the project — not because anyone made an error, but because the goal moved. A workflow that keeps the spec faithful to the *original* intent while the *actual* intent has shifted is optimizing against a dead artifact. The remedy is deliberate **intent refresh points** — moments where the spec is re-checked against what the organization now wants:

- after a prototype review;
- after user testing;
- after discovering a technical constraint that changes what is feasible;
- after a regulatory or compliance interpretation;
- after production feedback;
- after a significant bug report reveals a wrong assumption;
- after a model generates something surprising but better than what was asked for.

The goal is not endless churn — most of these checkpoints will confirm the spec is still right. The goal is to make sure that when intent has genuinely moved, the spec moves with it, rather than letting the team build faithfully toward a target no one wants anymore.

## When to reach for it

- Every time implementation reveals that a specified behavior is wrong, ambiguous, or impossible — update the spec before writing the fix, not after.
- When adding or removing a feature: spec change and code change must ship in the same commit.
- When an agent is given a spec to work from — verify the spec reflects the current state of the codebase before handing it over.
- When reviewing completed work: check that the spec, not just the code, accurately reflects what was built.
- After any refactor that changes public interfaces, file paths, or module boundaries.

## When NOT to

- Throwaway spike implementations that are explicitly scoped as exploratory and will be deleted — spending time updating a spec for work that won't survive past the spike wastes the learning budget.
- Early brainstorming phases where the spec is explicitly a working draft and all readers understand it is not authoritative — but mark it clearly as such.

## Exemplars

- The most common source of multi-agent divergence is one sub-agent working from a spec version the orchestrator already invalidated. Sync discipline prevents this class of failure entirely.
- Amplifier TASKS.md conventions treat the task file as a living document updated by agents as tasks progress — the same sync principle applied to project management.
- Gojko Adzic, *Specification by Example* (2011) — https://gojko.net/books/specification-by-example/ — formalizes: living documentation as specifications kept synchronized with implementation through automated tests that serve as the single authoritative reference; 2012 Jolt Award winner
- Cyrille Martraire, *Living Documentation* (2019) — https://www.pearson.com/en-ca/subject-catalog/p/living-documentation-continuous-knowledge-sharing-by-design/P200000009531/9780134689364 — formalizes: extends living documentation from executable tests to all knowledge artifacts; shows how automated reconciliation mechanisms prevent spec drift across the full codebase
- 2389 Research, documentation-audit — https://github.com/2389-research/documentation-audit — first-party: verifies documentation against codebase reality — drift hunted deliberately ("caught a lie in your docs") rather than discovered by the next reader who builds on the stale spec
