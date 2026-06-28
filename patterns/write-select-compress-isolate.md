---
title: "Four Moves: Write, Select, Compress, Isolate"
one_liner: Every context management decision is one of four moves — write it out, select only the relevant part, compress the verbose into the essential, or isolate the detail into a sub-agent.
dimensions: context-engineering
---

## What it is

When facing a context management problem, there are exactly four moves available. Write: convert ephemeral reasoning or intermediate results into a persistent artifact (a file, a note, a checkpoint) so they can survive context resets and be read back precisely. Select: from a large body of available material, choose only the portion that is relevant to the current step — retrieve, filter, slice, excerpt. Compress: take verbose content (a long document, a full conversation history, a detailed plan) and reduce it to a dense summary that preserves signal while shedding token cost. Isolate: delegate a detail-heavy sub-task to a fresh agent so the work happens outside the main context window and only the result returns. These four moves are not arbitrary — they map exhaustively onto the ways context can be shaped. A well-engineered context pipeline can be described entirely in terms of which moves are applied, in what order, to what content.

## When to reach for it

- When diagnosing context management problems: identify which move is missing. Growing context? Need compress or isolate. Lost state across sessions? Need write. Too much retrieved content? Need select.
- When designing a multi-agent pipeline: specify which agent applies which move before passing content to the next stage.
- When writing a system prompt or injection: ask whether each piece of content is the raw artifact (write), the most relevant slice (select), a summary (compress), or something that should be offloaded entirely (isolate).
- When a long-running agent's outputs degrade: the four-move framework is a diagnostic — identify which move is absent or misapplied.

## When NOT to

- Simple single-turn tasks where the input naturally fits in context without any of the four moves — applying the framework to trivial tasks adds unnecessary overhead.
- Tasks where the full verbatim content is required by the model (legal text, contracts, code under review where every line matters) — compression would destroy necessary signal; selection would leave gaps; the move here is simply "include it."

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes context management patterns that correspond to all four moves: writing artifacts, selecting relevant content, summarizing history, and isolating sub-tasks to specialized agents

## Related

- `patterns/context-is-finite.md`
- `patterns/context-over-prompt.md`
- `patterns/just-in-time-retrieval.md`
- `patterns/subagents-as-context-sinks.md`
- `patterns/checkpoint-handoff-file.md`
