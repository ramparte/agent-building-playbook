---
title: Earn the Interruption
one_liner: Human attention is scarce, so an agent should not interrupt merely because it hit a normal checkpoint — it should interrupt only when human judgment is now the bottleneck; insert humans at specific edges (risky deploy, unclear intent, high-cost loop, compliance exception, repeated nonconvergence), not everywhere.
dimensions: human-factors, orchestration, workflow-discipline
---

## What it is

Human attention is the scarce resource in an agentic system, and every interruption spends it; the mistake most pipelines make is to treat human approval as a mode — a checkpoint the agent hits after every stage — rather than as an edge in the workflow graph that only specific transitions cross. Earning the interruption means an agent does not pause because it reached a routine boundary; it pauses because human judgment has genuinely become the bottleneck, the one thing the agent cannot supply for itself. The design work is to identify the small set of edges where a human actually belongs — a risky or irreversible deployment, an intent that turned out ambiguous, a loop whose cost is climbing without convergence, a compliance or policy exception the agent is not authorized to resolve, a user-facing decision with taste or accountability stakes, or a repeated failure to converge after several attempts — and to insert the human there and nowhere else. Two artifacts make this concrete: an interrupt policy that declares when agents may ask humans for help, so the decision to interrupt is governed rather than improvised; and a review queue that prioritizes finished outputs by risk, importance, and confidence, so the human spends attention on what matters most first. The anti-pattern this replaces is interrupting humans constantly — surfacing every checkpoint, every uncertainty, every finished session as an equal claim on attention — which trains people to ignore the agent entirely. Route interruptions by risk and necessity, and each one that arrives is worth reading.

## When to reach for it

- When agents finish faster than humans can review, and the review backlog is the binding constraint on throughput — prioritize by risk and confidence rather than first-in-first-out.
- When the workflow contains a few genuinely high-stakes edges (irreversible deploys, compliance exceptions, large spends) surrounded by many routine ones — gate the high-stakes edges and let the rest run.
- When an agent keeps asking for confirmation at routine checkpoints and humans have started rubber-stamping — that reflex means the interrupt policy is miscalibrated, not that the human is needed.
- When intent is ambiguous enough that guessing wrong is expensive — an interrupt to clarify intent is earned because the agent cannot resolve it alone.
- When a loop is failing to converge after repeated attempts — escalate rather than burning more budget on the same nonconvergence.

## When NOT to

- When the action is cheap, reversible, and low-stakes — interrupting for it spends scarce attention on a decision the agent should simply make and report.
- When a human is already approving every action inline — adding a separate interrupt policy on top adds latency without adding judgment.
- When the real problem is a missing guardrail, not a missing human — if the risk can be bounded by a validator or an action limit, bound it there instead of routing it to a person.
- When interrupts are used to offload accountability for a decision the agent was designed to own — that is not earning the interruption, it is abdicating the task.

## Related

- `patterns/guardrails-and-escalation.md`
- `patterns/autonomy-when-justified.md`
- `patterns/supervise-many-agents.md`
- `patterns/attention-is-the-scarce-resource.md`
