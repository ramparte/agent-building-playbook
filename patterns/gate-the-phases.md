---
title: Gate the Phases Explicitly
one_liner: Declare a hard transition between design and build, and between build and ship — phases that blur produce work that cannot be reviewed or rolled back.
dimensions: workflow-discipline
---

## What it is

Development work passes through recognizable phases: understanding the problem, designing the solution, implementing it, verifying it, and shipping it. In AI-assisted workflows, these phases collapse easily — an agent asked to "figure it out" will design, implement, and claim completion in a single uninterrupted turn, producing work that is impossible to review at the phase boundaries where problems are cheapest to catch. Gating the phases explicitly means declaring a visible checkpoint between each phase where progress is assessed, assumptions are surfaced, and the decision to proceed is made deliberately rather than by default. The gate does not have to involve a human — it can be a test, a validation script, or a structured agent handoff — but it must be a real decision point, not a formality.

## When to reach for it

- Any multi-step workflow where the output of one phase becomes the input to the next — gate between them so errors propagate no further than one phase.
- When delegating to an agent: specify explicitly which phase the agent is responsible for, and what artifact marks the end of its phase.
- When requirements are partially known: gate after the design phase to verify the design before building, not after building to discover the design was wrong.
- When multiple agents or humans are involved: gates are the coordination mechanism that keeps their work aligned without requiring constant synchronization.
- When debugging a broken pipeline: identify which gate was missing or skipped; that is almost always where the error originated.

## When NOT to

- Simple, well-understood tasks where all phases are trivial and phase blurring poses no meaningful risk — not every file rename needs a formal gate.
- Tight feedback loops where the cost of gating exceeds the cost of rework — quick exploratory iterations where the whole thing is thrown away if the direction is wrong.
- When the phases genuinely cannot be separated (e.g., certain types of design require running implementation to discover constraints) — in those cases, gate around the combined step.

## Exemplars

- The Amplifier superpowers workflow structures phases explicitly: brainstorm → human approval → plan → human approval → implement → verify. Each arrow is a gate.
- Staged deployment pipelines gate between build, test, staging, and production — the discipline is identical, applied to infrastructure rather than development workflow.
- Robert G. Cooper, "Stage-Gate Systems: A New Tool for Managing New Products" (*Business Horizons*, 1990) — https://ideas.repec.org/a/eee/bushor/v33y1990i3p44-54.html — classic antecedent: introduced the stage-gate system of formal checkpoints requiring explicit go/kill decisions before work advances to the next phase
