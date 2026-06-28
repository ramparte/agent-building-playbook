---
title: Implement to Learn
one_liner: The fastest way to understand a problem is to build a small, throwaway version of the solution.
dimensions: workflow-discipline
---

## What it is

Understanding a problem well enough to specify it correctly almost always requires building something first. When a task is new or poorly understood, writing a full specification before touching code inverts the learning order — you are trying to reason abstractly about something you have not yet made concrete. Implementing a small, intentionally throwaway version forces the real questions to surface: which inputs are ambiguous, which outputs are hard to define, which assumptions were wrong. The throwaway implementation is not the deliverable; it is a research instrument that produces a better specification for the real deliverable.

## When to reach for it

- Before writing a detailed specification for a task you have never done before — implement a rough version first, then write the spec from what you learned.
- When a task description sounds clear but the outputs keep coming out wrong — the spec probably has a hidden assumption that only implementation will reveal.
- When asked to estimate effort for an unfamiliar task — build a spike first, throw it away, and estimate from the spike.
- When an agent is producing poor results on a task — try a hand-built implementation of a small slice to understand where the difficulty actually lives.

## When NOT to

- When the task is well-understood and the specification is genuinely complete — implementation-to-learn wastes time when you already know the problem.
- When a throwaway implementation creates external side effects that are hard to undo (writing to production systems, sending emails, charging accounts) — the throwaway assumption breaks when side effects are durable.
- When time pressure requires shipping the first attempt — accept a worse specification rather than spending time on a spike you cannot afford.

## Exemplars

- The term "spike" in Extreme Programming names this pattern explicitly: a time-boxed experiment to gain knowledge, with the explicit expectation that the spike code is discarded when the knowledge is gained.
- Amplifier session workflows — implementation attempts that fail and are then retried with a better task definition are a form of implement-to-learn at the orchestration level.
