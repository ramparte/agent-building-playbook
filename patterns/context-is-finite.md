---
title: Context Is a Finite Resource
one_liner: Curate the smallest high-signal token set — every token of noise degrades every token of signal.
dimensions: meta-principles, context-engineering
---

## What it is

The context window is a budget, not a dump. Every token you place in context competes with every other token for the model's attention, and that attention is not uniformly distributed — low-signal content (boilerplate, repetition, irrelevant history) actively degrades the quality of the model's engagement with high-signal content. Curation is not optional; it is the discipline of keeping the budget allocated to the content that most changes the output. Agents and orchestrators that accumulate everything they have ever seen into context are not being thorough — they are squandering the most limited resource in the system.

## When to reach for it

- When designing what goes into a system prompt, a tool response, or a memory injection: ask what you can remove without hurting outcomes.
- When agent pipelines pass full conversation history between steps — most of it is noise by the time the next step runs.
- When a long-running agent starts producing worse outputs over time — context bloat is a common culprit.
- When evaluating retrieval strategies: retrieve for relevance, not completeness.

## When NOT to

- Exploratory conversations where you genuinely need the full thread to maintain continuity — truncating early context breaks reasoning in ways hard to diagnose.
- Tasks where provenance and auditability of every prior step matters (legal, compliance, regulated domains) — don't curate context if doing so destroys the audit trail.

## Exemplars

- Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (arXiv:2307.03172) — https://arxiv.org/abs/2307.03172 — empirical support: demonstrates a U-shaped performance curve where models perform worst on information in the middle of long contexts, showing that context position and volume actively degrade retrieval quality
- Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — Effective Context Engineering for AI Agents: frames context as an attention budget, references "context rot" — the finding from needle-in-a-haystack benchmarking that performance degrades as context grows — and treats curation as the core discipline for maintaining signal quality
