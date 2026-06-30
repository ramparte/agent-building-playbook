---
title: Design for Recovery, Not Just Completion
one_liner: A workflow should behave like an attractor — pulled back toward the desired state after the model drifts, stalls, or produces something plausible but wrong — so success means recovery, not merely that a step finished.
dimensions: orchestration, reliability, workflow-discipline
---

## What it is

In conventional automation, success means the script completed: it ran to the end without throwing. Agentic automation cannot inherit that definition, because the model can finish a step and still be wrong — it can misunderstand the intent, drift off the spec, overfit to one example, stall in a loop, or produce a plausible artifact that does not actually do the job. The right mental model is the attractor: a workflow that tends to stabilize toward a desired state even after perturbation, the way a marble rolls back to the bottom of a bowl no matter where you nudge it. You build an attractor by wiring recovery loops into the graph rather than assuming forward progress — implementation can fall back to planning; review can send work back to implementation; a test failure triggers diagnosis instead of blind patching; a stale assumption triggers a spec revision; an uncertainty threshold triggers a human interview; and repeated failure triggers a postmortem rather than an infinite loop. The design goal is not to prevent every error — that is hopeless with a nondeterministic actor — but to make error states visible, bounded, and recoverable, so the system is judged by whether it returns to the desired state, not by whether any single step reported success.

## When to reach for it

- Any multi-stage workflow where a step can "succeed" while producing a wrong-but-plausible artifact — the failure mode deterministic automation does not have.
- When a loop can run long: bound it with a postmortem edge so repeated failure becomes a diagnosis, not an infinite retry.
- When the cost of a silent wrong answer downstream is high — wire review and test edges that can route work backward, not just forward.
- When intent is ambiguous enough that the model will sometimes guess wrong — add an uncertainty-threshold edge that escalates to a human interview instead of committing to the guess.
- When assumptions made early can go stale mid-run — let a discovered contradiction trigger a spec revision rather than carrying the bad assumption to completion.

## When NOT to

- Genuinely deterministic, machine-checkable steps where "it completed" really is success — adding recovery machinery is overhead with no error mode to catch.
- Throwaway one-shot tasks where you will eyeball the output yourself and rerun by hand if it's wrong — you are the recovery loop.
- When recovery edges would mask a root-cause bug that should be fixed instead of routed around — recovery is for model drift, not for papering over a broken tool or spec.
- When the bounded-retry budget is set so high it becomes the infinite loop it was meant to prevent — an unbounded "recovery" loop is just a stall with extra steps.

## Related

- `patterns/match-topology-to-the-work.md`
- `patterns/deterministic-rails.md`
- `patterns/recipe-not-conversation.md`
- `patterns/fix-the-root-cause.md`
- `patterns/earn-the-interruption.md`
