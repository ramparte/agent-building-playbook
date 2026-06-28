---
title: Context Engineering Over Prompt Engineering
one_liner: The model's output quality is bounded by context quality — sculpting what the model sees matters more than sculpting the instruction text.
dimensions: context-engineering
---

## What it is

Prompt engineering focuses on the wording of the instruction: how you phrase the task, what persona you assign, what format you request. Context engineering shifts attention upstream — to the information, documents, history, and state placed in the window before the instruction is even read. The model can only reason over what it has been given; the richest instruction text in the world cannot compensate for missing facts, stale data, or a bloated context that drowns signal in noise. Treating context as the primary design surface — what to include, what to exclude, in what order, in what compressed form — consistently yields larger gains than refining prompt wording. Prompt engineering is polish; context engineering is architecture.

## When to reach for it

- When a model produces inconsistent or wrong outputs despite a carefully worded prompt — ask what it is and is not seeing, not how to rephrase the request.
- When designing a RAG system, agent memory, or any pipeline that injects retrieved content — the retrieval and compression strategy is the engineering problem, not the final instruction.
- When debugging an agent that "knows" something in some sessions and "forgets" it in others — the inconsistency is almost always in context construction, not in prompt wording.
- When a task requires the model to reason over real-world state (file contents, API responses, conversation history) — treat that state as a first-class engineering artifact to be curated before being placed in context.

## When NOT to

- Genuinely simple, self-contained tasks where all required information is in the instruction itself and the model has it in training — prompt wording improvements are appropriate here.
- Tasks where the model's refusal or format compliance is the issue — those are prompt-level problems, not context-construction problems.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: frames context construction and retrieval strategy as core agent design decisions, distinct from prompt crafting
- Anthropic — https://www.anthropic.com/news/contextual-retrieval — Contextual Retrieval: demonstrates that what you inject into context (and how you pre-process it) dominates retrieval quality, not just the query text

## Related

- `patterns/context-is-finite.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/just-in-time-retrieval.md`
