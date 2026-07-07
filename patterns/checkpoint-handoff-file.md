---
title: Checkpoint to a Handoff File, Then Restart Clean
one_liner: When context grows unwieldy or a session must end, write a structured handoff file capturing exactly what the next session needs, then start fresh with only that file.
dimensions: context-engineering, workflow-discipline
---

## What it is

Long-running tasks accumulate context: decisions made, attempts tried, state discovered, errors encountered. As that history grows, two failure modes emerge. First, the model begins to weight early framing too heavily, even when later information should have updated its approach. Second, the context fills with noise — tool outputs, intermediate reasoning, failed branches — that competes with the signal that actually matters for the next step. A handoff file is the antidote: a deliberately structured document written at a checkpoint that captures only what the next session genuinely needs — the current goal, what has been completed, what is in progress, what was tried and abandoned and why, what the next concrete action is, and where the relevant artifacts live. The session that reads the handoff file starts with a clean context window containing exactly this curated briefing, not an inherited mess of accumulated history. The act of writing the handoff is itself a clarifying operation — it forces distillation of what matters from what merely happened.

The same file is what a journal entry should be. A good journal entry is a handoff packet, not a vague diary: it records the task goal, the final state, the decisions made, the failed attempts and why they were abandoned, the unresolved questions, the files changed, the tests run, the assumptions worth revisiting, and the recommendations for the next session. A bad journal entry narrates feelings and activity; a good one hands the next session everything it needs to resume cold. For long-lived agent personas the journal does more than transfer task state — it reinforces continuity of style, goals, and "vibe," letting a later session restart in character without replaying an entire transcript.

## When to reach for it

- When a task will span multiple sessions and context must be transferred without loss of essential state.
- When the current context window is more than two-thirds full and the task is not complete — the remaining work will be better served by a fresh context with a handoff than by continuing to compress into an overloaded window.
- When an agent loop is about to be reset (system restart, context limit, scheduled job end) — checkpoint before the reset, not after.
- When handing off work between agents or between a human and an agent — the handoff file is the interface.
- When debugging reveals that the model has anchored on early framing that is now stale — a handoff file forces re-grounding on current state.

## When NOT to

- Short tasks that complete within a single session with room to spare — the overhead of writing and reading a handoff file is not worth it for a task that will finish in the same context.
- Tasks where the full conversation history is genuinely required for continuity — some multi-turn interactions depend on the conversational thread itself, not just the state.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes writing to files and structured artifacts as a core agentic pattern for preserving state across context resets

## Related

- `patterns/context-is-finite.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/persist-environment-facts.md`
- `patterns/long-horizon-memory.md`
- `patterns/hang-up-call-back.md`
