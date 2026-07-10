---
title: Make Every Stage Produce an Auditable Artifact
one_liner: A stage with no artifact is a stage that cannot be audited — and a stage that cannot be audited is a stage you must trust blindly.
dimensions: reliability, observability
---

## What it is

Every stage in a multi-step pipeline should produce an output artifact that is independently inspectable: a file written to disk, a structured log entry, a database record, a message in a queue, or a test result captured to a report. The artifact is not a side effect — it is the mechanism by which the stage communicates its result to the rest of the system without routing through the agent's self-report. Stages that produce only internal state, transient in-memory results, or nothing at all create auditing gaps: you cannot replay them, inspect their output, or verify that they ran correctly without re-running them. Artifacts are the substrate of observability in agentic pipelines.

The same property makes durable artifacts the most reliable form of near-term memory — far more reliable than anything mystical. The practical memory of an agentic system is its specs, plans, sprint docs, acceptance criteria, test results, browser videos, screenshots, session summaries, decision logs, postmortems, journals, learned rules, workflow state files, domain glossaries, and transcript-derived summaries. These work as memory precisely because they are artifacts: they can be inspected, versioned, pruned, passed to another agent, reviewed by a human, and evaluated. That makes them less magical than implicit, model-internal memory, but far more governable — you can see what the system believes and correct it. A good artifact is not just any file, though. It is small enough to fit a later context window, explicit enough for a different agent or human to resume from cold, versioned enough to support rollback and comparison, structured enough for tools to inspect mechanically, and semantically rich enough to preserve intent rather than just outcome. An artifact that fails these criteria — a sprawling log no window can hold, an undated blob that cannot be diffed, prose too vague to resume from — is storage, not memory.

## When to reach for it

- When designing any multi-step pipeline: assign a concrete artifact to each stage before writing any stage logic.
- When a pipeline produces unexpected downstream results and you cannot trace where the corruption began — missing artifacts made the investigation impossible.
- When you need to replay a pipeline from a specific stage — artifacts at each boundary make selective replay possible.
- When multiple agents or systems contribute to a workflow — artifacts are the hand-off mechanism that decouples producer from consumer.
- When adding a new agentic step: specify what artifact it will produce before implementing the step.

## When NOT to

- Single-step, ephemeral transformations where the result is consumed immediately and the cost of writing an artifact exceeds the cost of rerunning the step (e.g., a quick string transformation inside a single-turn response).
- Streaming outputs where intermediate state is inherently transient and the final artifact captures the complete result — don't produce artifacts for every token if the final file is the meaningful unit.
- Highly sensitive data where persisting intermediary artifacts creates storage or compliance risk — in those cases, substitute structured in-memory audit logs with appropriate retention controls.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes how agentic pipelines should maintain visibility of intermediate results, not just final outputs, to enable debugging and human oversight
- Amplifier — https://github.com/microsoft/amplifier — event-first observability is a core philosophy: significant actions emit events to a JSONL log, making agent actions independently inspectable and replayable (per the Amplifier team's white papers; in the public repos, the amplifier-foundation session-analyst agent works from these events.jsonl streams)
- Martin Fowler, "Event Sourcing" (2005) — https://martinfowler.com/eaaDev/EventSourcing.html — classic antecedent: formalizes the principle of capturing every state change as an immutable, replayable event record — the same property the pattern requires of pipeline stage artifacts

## Related

- `patterns/long-horizon-memory.md`
- `patterns/scope-and-expire-memory.md`
