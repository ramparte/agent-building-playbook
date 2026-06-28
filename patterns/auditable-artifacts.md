---
title: Make Every Stage Produce an Auditable Artifact
one_liner: A stage with no artifact is a stage that cannot be audited — and a stage that cannot be audited is a stage you must trust blindly.
dimensions: reliability, observability
---

## What it is

Every stage in a multi-step pipeline should produce an output artifact that is independently inspectable: a file written to disk, a structured log entry, a database record, a message in a queue, or a test result captured to a report. The artifact is not a side effect — it is the mechanism by which the stage communicates its result to the rest of the system without routing through the agent's self-report. Stages that produce only internal state, transient in-memory results, or nothing at all create auditing gaps: you cannot replay them, inspect their output, or verify that they ran correctly without re-running them. Artifacts are the substrate of observability in agentic pipelines.

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
- Amplifier — https://github.com/microsoft/amplifier — the context-intelligence hook captures a structured artifact (JSONL event stream) at every session turn, making every agent action independently inspectable and replayable
