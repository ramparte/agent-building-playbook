---
title: If It's Important, Emit an Event
one_liner: If a decision, state change, or outcome matters to understanding what happened, it should produce a structured event — not a log line, not a comment, not a hope that someone was watching.
dimensions: observability
---

## What it is

A system that does important work but emits no record of it is a black box. Post-hoc reconstruction from outputs — trying to infer what happened from what currently exists — is archaeology, not observability. Emitting structured events at moments that matter is the practice of making a system narrate its own execution: when a tool call completes, emit a completion event with inputs and outputs; when a decision branch is taken, emit a decision event with the context that drove it; when a retry happens, emit a retry event with the failure reason. These events are not log lines — they are typed, structured records that carry enough information to reconstruct the system's reasoning after the fact. The crucial difference is intent: log lines are notes to developers; events are first-class output of the system, designed to be consumed by other systems, agents, dashboards, and analysis pipelines. An agent that emits events is observable. An agent that prints to stdout is guessable.

## When to reach for it

- At every significant state transition: session start, session end, task assignment, task completion, handoff, failure, retry. Each transition that matters to understanding the run should produce a record.
- When a decision is made that affects subsequent behavior: which branch was taken, which tool was selected, which model was chosen. Decisions without records are invisible.
- When an external call is made: tool invocations, API calls, database writes. Record the inputs, the outputs, the latency, and the outcome. External calls are the highest-value events because they are the points where the system interacts with the world.
- When building any pipeline that will run unattended: unattended systems with no event stream cannot be diagnosed when they fail. Event emission is not optional for autonomous operation.
- When designing the handoff between agents in a multi-agent system: the events from one agent's execution are the working memory for the next agent and the audit trail for the orchestrator.

## When NOT to

- When the volume of events would overwhelm downstream consumers without filtering: emit at the right granularity. Emitting every token of inference output as an event is not observability — it is noise that hides signal.
- When events contain sensitive data that should not be persisted — credentials, PII, or security tokens should not appear in event payloads. Scrub before emission or use structured redaction.
- When the system is truly ephemeral and disposable and no analysis of its behavior will ever be needed — but be honest about this judgment; most systems that seem disposable turn out to have consequences that matter.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier — event-first observability: "if it's important, emit an event" — significant agent actions emit structured events to a single JSONL log serving as source of truth, with tracing IDs enabling correlation and hooks observing without blocking
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends instrumenting agentic pipelines with monitoring and logging at each step to enable debugging of complex multi-step behaviors that are otherwise uninterpretable
- Martin Fowler, "Event Sourcing" — https://martinfowler.com/eaaDev/EventSourcing.html — the canonical 2005 software-engineering formulation: "Capture all changes to application state as a sequence of events"; the classic SE pattern this directly echoes, including reconstruction, temporal queries, and audit capabilities
- AlSayyad et al., "AgentTrace: A Structured Logging Framework for Agent System Observability" (arXiv:2602.10133) — https://arxiv.org/abs/2602.10133 — formalizes structured event capture across operational, cognitive, and contextual surfaces for LLM agents; directly implements this pattern as foundational layer for security, accountability, and real-time monitoring

## Related

- `patterns/awareness-layer.md`
- `patterns/real-environment-execution.md`
- `patterns/session-archaeology.md`
