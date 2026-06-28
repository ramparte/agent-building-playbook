---
title: "Long-Horizon Memory: Compaction, Notes, Isolation"
one_liner: Long-running tasks require three memory strategies — compacting history as it ages, maintaining running notes files, and isolating sub-tasks to separate sessions to prevent context collapse.
dimensions: context-engineering
---

## What it is

A single context window cannot hold the full history of a week-long project. Long-horizon memory is not a single technique; it is three complementary strategies applied in combination. Compaction: as conversation history ages and the details of early steps become less relevant than their outcomes, summarize the history aggressively — what was decided, not how the decision was reached; what was built, not every failed attempt along the way. The compact summary replaces the verbose transcript. Notes files: maintain a persistent running document outside the context window that accumulates decisions, open questions, discovered facts, and next actions; every session begins by reading this file and ends by updating it. Isolation: any sub-task with a well-defined output is a candidate for a fresh sub-agent session — that session inherits only the context it needs for the sub-task, completes the work, and returns a summary, leaving no residue in the main session's context. Together, compaction handles the past, notes handle the present state, and isolation handles the future work — and all three prevent the accumulation of stale, dense, low-signal history that degrades performance on long-running tasks.

## When to reach for it

- When a task will span more than a few sessions and cannot be completed in a single context window.
- When the working context is mostly composed of history from steps that are now complete — compaction time.
- When facts discovered in one session need to be reliably available in the next — start a notes file now, before the first session ends.
- When a major sub-task has a clear output that can be described to a fresh agent without needing the full history — isolate it.
- When agent performance degrades over a long session — usually a sign that context compaction is overdue.

## When NOT to

- Short tasks that complete in a single session with no carry-over — the overhead of a notes file and compaction strategy is not warranted.
- Tasks where the full history is required to make correct decisions at every step (some legal, compliance, or audit workflows) — compaction must not destroy the audit trail; archive it instead of replacing it.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: explicitly recommends compaction and external memory files for long-running agent tasks as a first-class context management strategy

## Related

- `patterns/context-is-finite.md`
- `patterns/checkpoint-handoff-file.md`
- `patterns/persist-environment-facts.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/subagents-as-context-sinks.md`
