---
title: Just-in-Time Retrieval Over Pre-Loading
one_liner: Don't fill context with everything that might be relevant — retrieve only what is needed, exactly when it is needed, and discard it after use.
dimensions: context-engineering
---

## What it is

Pre-loading is the impulse to front-load context with all potentially relevant documents, tools, history, and reference material before work begins. The cost compounds: a large pre-loaded context crowds out working memory, forces the model to attend across irrelevant content, and spends tokens that could hold later-stage results. Just-in-time retrieval inverts the pattern — keep the context minimal at the start, and pull in specific content only at the step that needs it. A code review agent does not need the full API documentation in its context from turn one; it needs the relevant section when it encounters the relevant function. A planning agent does not need every prior conversation; it needs the summary of the last decision. Just-in-time retrieval treats information like a dependency that should be loaded at the moment of use, not pre-declared at the top of the program.

"Memory" is the wrong word for this until it is specified. The grand metaphor — give the agent a memory — invites pre-loading and obscures the actual design decision. The practical question is much narrower: what should this agent know at this moment to improve this outcome? That question reframes the problem as context governance rather than generic memory, and it is the question just-in-time retrieval answers per step. This is also why calling a RAG pipeline "memory" and stopping there is an anti-pattern: retrieval is genuinely useful, but it is only one component of memory. Real memory also requires selection (deciding what to pull), decay (letting stale material expire), correction (fixing what was wrong), and evaluation (checking that the retrieved context actually helped). A retriever with none of those is a lookup, not a memory — and treating it as the whole solution leaves the hard governance work undone.

## When to reach for it

- When designing agent tool-use: each tool call should retrieve exactly the content needed for the current step, not a superset of potentially useful content.
- When building RAG pipelines: retrieve per-query at inference time rather than pre-filling context with all indexed chunks that scored above a threshold.
- When an agent runs across many steps and the early steps' context becomes irrelevant to later steps — defer retrieval of later-step material until those steps are reached.
- When latency or cost of retrieval is low relative to the cost of carrying unused tokens across many inference calls — almost always true for file reads, vector search, and database lookups.

## When NOT to

- Tasks where the full corpus must be visible simultaneously to reason correctly — a document comparison task where the model must hold both documents in mind while generating cannot defer retrieval without breaking the task structure.
- When the retrieval system itself is slow or expensive and the same content will be needed at every step — a single pre-load may be cheaper than repeated retrievals of the same material.
- Exploratory or creative tasks where the model benefits from broad context to generate associations that span the retrieved material — selective just-in-time retrieval can artificially narrow the space.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: advocates for targeted tool invocation at the moment of need rather than pre-loading context with all available resources
- Anthropic — https://www.anthropic.com/news/contextual-retrieval — Contextual Retrieval: demonstrates retrieval systems designed for per-query, per-step relevance rather than pre-indexed bulk injection
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (arXiv:2005.11401) — https://arxiv.org/abs/2005.11401 — the original RAG paper (NeurIPS 2020): established retrieve-at-inference-time as the foundational model for injecting external knowledge only when needed, rather than baking it into weights
- Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (arXiv:2307.03172) — https://arxiv.org/abs/2307.03172 — empirical evidence that performance degrades when relevant information is buried in a pre-loaded long context; supports the case for selective, per-step retrieval over front-loading
- Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — Effective Context Engineering for AI Agents (Sept 2025): describes maintaining lightweight identifiers (file paths, URLs, stored queries) and loading content at runtime as the canonical JIT implementation

## Related

- `patterns/context-is-finite.md`
- `patterns/context-over-prompt.md`
- `patterns/write-select-compress-isolate.md`
