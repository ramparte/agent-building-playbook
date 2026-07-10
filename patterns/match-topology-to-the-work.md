---
title: Match the Topology to the Work
one_liner: Choose your agentic topology deliberately — from one-shot prompt to slash-goal loop to skill to graph to hierarchy to studio — by the cost of failure, clarity of intent, size of the work, and degree of repeatability.
dimensions: orchestration, workflow-discipline, meta-principles
---

## What it is

Agentic workflows sit on a spectrum from lightweight to heavyweight, and each point on it is the right answer for some work and the wrong answer for the rest. A one-shot prompt is ideal for tiny tasks, prototypes, local edits, and ideation, and it fails when you overtrust plausible output that has no durable state behind it. A slash-goal or Ralph loop fits a clear goal with moderate ambiguity where you want a simple autonomous push, and it fails by running too long without enough checkpoints. A skill-driven workflow captures a repeatable human-shaped process — brainstorming, planning, review, implementation — and fails when the skill hides complexity or goes stale and overly broad. A graph workflow suits multi-stage work with separable planning, execution, validation, and feedback, and fails by demanding heavy setup that becomes a harness-maintenance project of its own. A hierarchical agent organization handles large programs needing many subagents, specialist roles, and long-running supervision, and fails through attention overload, unclear accountability, and excessive token burn. A studio or production system fits complex, creative, high-mix work where every project differs but reuses roles and tools, and fails without strong human direction and good artifact discipline. The selection criteria are the cost of failure, the clarity of the intent, the size of the work, and the degree of repeatability — and the discipline is to choose intentionally rather than by habit or fashion. Two failure directions make that discipline concrete: the obvious one is reaching for a heavy graph when a simple loop would do; the subtler inverse is that after a team discovers heavy tools it often regresses into feature-by-feature prompting, because the small rewards of one-off prompts are immediate while the payoff of structure is deferred. Both are failures of intentionality — the work, not the dopamine, picks the topology.

## When to reach for it

- At the start of any new workstream, before reaching for whatever topology you used last time — pick by the four criteria, not by muscle memory.
- When a workflow keeps overrunning or burning tokens: you are probably one tier too heavy and should drop to a lighter topology.
- When a lightweight loop keeps producing wrong-but-plausible output with no state to inspect: you are one tier too light and should add structure.
- When work is repeatable enough to be worth encoding — promote it from ad-hoc prompting up to a skill or graph.
- When standardizing a team's approach: name the topology explicitly so people stop defaulting unconsciously.

## When NOT to

- For a genuine one-off where any deliberation about topology costs more than just running the one-shot prompt.
- When the team has no slack to maintain a heavy harness — a graph or studio you cannot maintain is worse than a loop you can.
- As an excuse to over-architect: if a simple loop will do, building a graph is the failure mode, not the goal.

## Exemplars

- Hadfield et al. / Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system — How we built our multi-agent research system: distinguishes tasks that benefit from multi-agent parallelism (breadth-first research) from those that require shared sequential context (most coding work), making the topology-to-work match concrete and empirically grounded
- Walden Yan / Cognition — https://cognition.com/blog/dont-build-multi-agents — Don't Build Multi-Agents: argues that parallel subagents fail on interdependent work because actions carry implicit decisions, and conflicting decisions carry bad results; advocates a single sequential agent with full context for those workloads
- Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (arXiv:2503.13657) — https://arxiv.org/abs/2503.13657 — empirical taxonomy of 14 failure modes across 7 MAS frameworks; many failures trace to topology-task mismatch (system-design issues and inter-agent misalignment categories)

## Related

- `patterns/recipe-not-conversation.md`
- `patterns/shape-work-as-an-attractor.md`
- `patterns/start-least-agentic.md`
- `patterns/self-ablating-harness.md`
