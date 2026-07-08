---
title: Parallel Attempts at One Task
one_liner: Because a model is non-deterministic, one attempt is a single die roll — for a hard or quality-sensitive task, run several implementations of the same task in parallel from one checkpoint, then pick the best or splice the strongest parts of each.
dimensions: orchestration, cost-routing, workflow-discipline
---

## What it is

A model's output is a roll of the dice; if you need a three and rarely get it on the first try, roll several dice. Parallel attempts run the same task multiple times simultaneously from a shared checkpoint — save the plan and commit, fork into separate working directories (git worktrees or the equivalent), launch several implementations at once, then review them all and either pick the best or combine the strongest elements across attempts. This is deliberately trading tokens, which are cheap, for human time and wall-clock, which are not. It serves two distinct modes. As *failure mitigation*, when the approach is uncertain and any single attempt might fail, running three to five in parallel means you move forward from whichever succeeds instead of debugging a sequence of dead ends one at a time. As *solution-space exploration*, when quality matters more than speed, several working versions let you compare genuinely different approaches and graft the best of each together — which is especially powerful for open-ended work like UIs, game mechanics, and designs, where "correct" is a range and variety is the point. It is important that this is not the same as fanning out independent, *different* subtasks to save wall-clock — here the attempts are redundant on purpose, and the value is in selection and recombination, not in dividing the labor.

## When to reach for it

- When a task is hard or the right approach is uncertain, and a single attempt is about as likely to fail as to succeed — run several and proceed from the one that works.
- When quality matters more than speed and the solution space is wide (UI, design, game mechanics, anything creative) — generate variety and combine the best pieces.
- When debugging a failed attempt would cost more than launching a few fresh ones — reroll instead of repairing.
- When you can cheaply isolate attempts (worktrees, branches, separate sandboxes) so parallel implementations do not collide.

## When NOT to

- When the task is deterministic or well understood and one attempt reliably succeeds — parallel rolls just burn tokens for no added quality.
- When the attempts cannot be isolated and would interfere with each other's state — set up isolation first, or do not parallelize.
- When reviewing N results costs more attention than it saves — best-of-N only pays off if selecting the winner is cheaper than getting it right once.
- When you actually have different, independent subtasks — that is fan-out for wall-clock, a different pattern; this one is redundant attempts at the *same* task.

## Exemplars

- Lada Kesseler (lexler) — https://github.com/lexler/augmented-coding-patterns/blob/main/documents/patterns/parallel-implementations.md — "Parallel Implementations," the source this pattern is adapted from, with worked examples in game and UI development (video walkthrough: https://www.youtube.com/watch?v=_LSK2bVf0Lc&t=2671s)

## Related

- `patterns/parallel-independent-tracks.md`
- `patterns/single-threaded-default.md`
- `patterns/delegation-token-economics.md`
- `patterns/match-model-to-stage.md`
