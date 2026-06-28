---
title: Bite-Sized Tasks
one_liner: Break work into units small enough that each completes, commits, and can be reviewed independently.
dimensions: workflow-discipline
---

## What it is

A task that is too large to review is too large to trust. When a unit of work spans multiple files, multiple behaviors, and multiple decisions in a single block, every one of those decisions is invisible to review — the reviewer must either accept the whole or audit it entirely, and the agent or author must hold all of it in working memory at once. Bite-sized tasks are units of work small enough that a single person can read the change in full in five minutes and verify the intent from the commit message. In agentic workflows, bite-sized tasks map directly to agent capability: an agent given a five-hour task will context-exhaust, hallucinate, or produce an unreviewed monolith. An agent given a focused thirty-minute task will complete it, commit it, and hand off cleanly. The constraint is not about effort — it is about reviewability and recoverability.

## When to reach for it

- At planning time: if a task cannot be described in two sentences, it is too large — decompose it.
- When an agent produces a large, unreviewed diff: the next task should be a review of what was produced, not the next feature.
- When a task requires understanding context from three or more separate locations before starting: the context load is too large; split the task.
- When progress is measured in days rather than hours: the granularity is wrong; break it down.
- When a rollback would require reverting multiple independent behaviors: the unit of work was too large.

## When NOT to

- When the smallest coherent unit of work is genuinely large — some refactors or data migrations cannot be meaningfully subdivided without leaving the codebase in a broken intermediate state. In those cases, use a feature branch and gate review at the end.
- When all the work is trivially reviewable even at larger scale (e.g., a mechanical rename across a large number of files where the pattern is obvious and the diff is uniform).
- When the overhead of decomposition exceeds the benefit — very short-lived prototypes where the entire thing will be thrown away.

## Exemplars

- The Amplifier superpowers workflow requires tasks to be small enough for TDD: write one failing test, implement minimally, commit. That cycle enforces bite-sized task discipline at the implementation level.
- Conventional commit messages that need more than one line in the subject to describe the change are a reliable signal that the commit contains more than one task.
