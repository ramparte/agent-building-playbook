---
title: Default to Clean-Slate Delegation
one_liner: When spawning a subagent, start with an empty context and provide only what the task needs — shared history is a source of inherited confusion, not free context.
dimensions: orchestration, context-engineering
---

## What it is

When an orchestrator spawns a subagent, the default assumption is often that more shared context is better — give the subagent the full conversation history, all prior tool results, every decision made so far, and it will have everything it needs to succeed. This assumption is usually wrong. Context passed wholesale carries not just the relevant information but also the irrelevant, the contradictory, and the already-superseded. A subagent that inherits the orchestrator's full history also inherits every wrong turn, every discarded approach, and every provisional decision that the orchestrator since reversed. The subagent cannot distinguish the live signal from the noise. It fills its context window with what doesn't matter, has less space for what does, and may be actively confused by intermediate state that looks like a constraint but isn't. Clean-slate delegation inverts this: the default for any subagent is an empty context. The orchestrator explicitly constructs what the subagent needs — the task, the constraints, the conclusions to take as given — and passes only that. This is not less information; it is more accurate information, without the confounding matter. The orchestrator's responsibility is to distill, not to dump.

## When to reach for it

- When spinning up a subagent to perform a focused, self-contained task — give it a task-specific briefing rather than the full conversation history.
- When the orchestrator's conversation is long or contains exploratory content that a focused subagent would find confusing or distracting.
- When multiple subagents are running in parallel and each needs a consistent, accurate view of the same constraints — a per-agent briefing is more reliable than each inheriting the same long history and extracting from it independently.
- When a subagent will make decisions that need to be right on the first try — a clean-slate briefing reduces the chance that irrelevant inherited state contaminates the decision.

## When NOT to

- When the subagent genuinely needs the conversational history to reason correctly — for example, a summarization or analysis task where the full context is the subject being analyzed, not the background.
- When the cost of constructing the briefing exceeds the cost of passing the history — for very short conversations, distillation may be more work than it's worth.
- When the subagent is resuming a prior session and continuity with that session's state is explicitly required — clean-slate is the wrong default in a continuation context.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier — the delegate() API defaults to context_depth="none" (clean slate); passing history requires an explicit opt-in via context_depth="recent" or context_depth="all", making clean-slate delegation the path of least resistance
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: warns that context accumulation across long agent loops degrades performance; clean-slate subagent delegation is the structural solution to context window pressure

## Related

- `patterns/share-full-context.md`
- `patterns/checkpoint-handoff-file.md`
- `patterns/context-over-prompt.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/hang-up-call-back.md`
