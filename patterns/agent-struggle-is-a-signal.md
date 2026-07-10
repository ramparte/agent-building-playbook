---
title: The Agent's Struggle Is a Signal
one_liner: When an AI agent starts thrashing on a codebase — missing duplicated call sites, running out of context mid-change, making excuses about failing tests — read it as an early warning that maintainability is decaying, and refactor, instead of just fighting the agent.
dimensions: observability, taste
---

## What it is

As a codebase grows tangled, agents degrade on it — and that degradation is a usable instrument, not just a frustration. When an agent updates one of several duplicated call sites and silently misses the others, runs out of context trying to hold a change together, declares itself done with tests still red, or insists failures are "expected" and then contradicts itself, those are not random model failures; they are a canary in the code mine. The properties that make code hard for an agent — duplication, poor cohesion, things that should change together living far apart, complexity that forces too much context to be loaded at once — are the same properties that make it hard for humans. So instead of treating the agent's difficulty as a reason to fight it or to blame the model, treat it as an early-warning signal that code quality is sliding, and act on it: have the agent review the code, name the maintainability problems, and plan a refactor; review that plan and steer it; and if the agent cannot clean the code well enough on its own, do the structural refactor with a proper refactoring tool. The move reframes an annoyance as feedback. An agent that suddenly needs three tries where it used to need one is telling you something about the code, and the cheap response is to listen.

## When to reach for it

- When an agent that used to handle a codebase well starts thrashing, stalling, or needing many attempts — treat the change in its performance as a diagnostic, not just bad luck.
- When you see the classic tells — a change applied to one duplicate but not its siblings, "I'm done" reported with tests failing, self-contradiction about what works — read them as duplication and complexity smells.
- When you are tempted to blame the model for a task it handled fine on a cleaner codebase — check the code before you swap the tool.
- As a standing habit: watch agent effort as a leading indicator of maintainability, the way you would watch build times or incident rates.

## When NOT to

- When the struggle is genuinely the model's limitation, or a hard task on clean code — not every failure is a code smell; confirm the signal before ordering a refactor.
- When the real fix is a targeted prompt or a missing piece of context, not a structural problem — do not refactor working code because one instruction was underspecified.
- When you cannot yet afford the refactor — record the signal anyway; do not let "can't refactor now" quietly become "the signal was noise."

## Exemplars

- Ivett Ördög (devill) — https://github.com/lexler/augmented-coding-patterns/blob/main/documents/patterns/canary-in-the-code-mine.md — "Canary in the Code Mine," the source this pattern is adapted from, with concrete tells (inconsistent updates across duplicated components, context exhaustion, "I'm done" with tests still failing, self-contradiction)

## Related

- `patterns/code-is-cheap-maintenance-isnt.md`
- `patterns/reliability-before-features.md`
- `patterns/rebuild-often.md`
- `patterns/awareness-layer.md`
- `patterns/develop-your-taste.md`
