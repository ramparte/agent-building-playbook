---
title: "Long-Horizon Memory: Compaction, Notes, Isolation"
one_liner: Long-running tasks require three memory strategies — compacting history as it ages, maintaining running notes files, and isolating sub-tasks to separate sessions to prevent context collapse.
dimensions: context-engineering
---

## What it is

A single context window cannot hold the full history of a week-long project. Long-horizon memory is not a single technique; it is three complementary strategies applied in combination. Compaction: as conversation history ages and the details of early steps become less relevant than their outcomes, summarize the history aggressively — what was decided, not how the decision was reached; what was built, not every failed attempt along the way. The compact summary replaces the verbose transcript. Notes files: maintain a persistent running document outside the context window that accumulates decisions, open questions, discovered facts, and next actions; every session begins by reading this file and ends by updating it. Isolation: any sub-task with a well-defined output is a candidate for a fresh sub-agent session — that session inherits only the context it needs for the sub-task, completes the work, and returns a summary, leaving no residue in the main session's context. Together, compaction handles the past, notes handle the present state, and isolation handles the future work — and all three prevent the accumulation of stale, dense, low-signal history that degrades performance on long-running tasks.

Underneath these strategies sits a structural distinction: memory is not one undifferentiated store but a stack of layers, each with its own scope, lifetime, and contents. Naming the layers is what makes scoped retrieval possible.

| Layer | Scope | Examples |
|---|---|---|
| **Working context** | The current task or session | Prompt, immediate files, recent tool output |
| **Project state** | The current repo or initiative | Spec, plan, sprint docs, tests, decision log |
| **Session history** | Prior attempts and handoffs | Journals, summaries, failed paths, open questions |
| **Persona continuity** | A long-lived agent's style and role | Preferences, duties, norms, tone, recurring habits |
| **Organizational knowledge** | Team or company practice | Policies, domain glossary, architecture rules, support patterns |
| **External pattern library** | Shared ecosystem knowledge | Reusable patterns, skills, validators, workflow recipes |

The decisive rule is that the system should NOT inject all layers by default. It should retrieve the smallest useful set for the moment at hand — a code edit rarely needs the org glossary, and a persona-continuity preference rarely belongs in a one-off sub-task. Injecting every layer everywhere recreates exactly the stale, dense context that compaction and isolation exist to prevent.

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

- Packer et al., "MemGPT: Towards LLMs as Operating Systems" (arXiv:2310.08560) — https://arxiv.org/abs/2310.08560 — canonical formalization of virtual context management with tiered memory and OS-style paging between fast and slow storage; the theoretical model most directly underlying this pattern's compaction+notes+isolation stack
- Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (arXiv:2304.03442) — https://arxiv.org/abs/2304.03442 — empirical demonstration of a memory+reflection+retrieval architecture sustaining coherent behavior across a 25-agent simulation; an early practical grounding for long-horizon memory strategies
- Sumers et al., "Cognitive Architectures for Language Agents" (arXiv:2309.02427) — https://arxiv.org/abs/2309.02427 — CoALA framework: formalizes modular memory layers for language agents; the layered memory taxonomy in this pattern's table directly parallels CoALA's decomposition into working, episodic, semantic, and procedural memory
- Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — Effective Context Engineering for AI Agents (Sept 2025): describes compaction (summarize-and-reinitiate) and external note files as first-class strategies; the most directly applicable engineering reference for implementing this pattern

## Related

- `patterns/context-is-finite.md`
- `patterns/checkpoint-handoff-file.md`
- `patterns/persist-environment-facts.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/subagents-as-context-sinks.md`
- `patterns/scope-and-expire-memory.md`
