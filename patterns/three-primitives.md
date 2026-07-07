---
title: Build From Three Primitives
one_liner: Every agentic system is built from three primitives — LLM call, tool call, and loop. Understand these primitives completely before reaching for higher-level abstractions.
dimensions: orchestration, tool-design
---

## What it is

Agentic systems — no matter how sophisticated they appear — reduce to three core operations: an LLM call (send context to the model, receive generated text), a tool call (execute a function and return the result), and a loop (repeat some combination of the above based on a condition). Everything else is composition: a workflow is a sequence of LLM calls and tool calls. An agent loop is an LLM call that selects a tool call inside a loop. A multi-agent system is multiple agent loops where some tool calls trigger other LLM calls. A retrieval-augmented pipeline is an LLM call whose inputs are populated by a tool call that runs a search. Understanding these three primitives deeply changes how you design systems. When a workflow is not working, you can reason about it at the primitive level: which LLM call produced the wrong output? Which tool call returned unexpected results? Where is the loop condition failing? You don't need to understand the abstraction layer — you can strip it away and look at the primitives. This matters for debugging, for performance analysis, and for designing the right level of abstraction. A system built on named, explicit primitives is transparent. A system that hides these primitives behind many abstraction layers is opaque when something goes wrong.

## When to reach for it

- When designing a new agentic system from scratch — begin with the three primitives and compose upward from there, rather than adopting a framework and working downward from its abstractions.
- When a workflow is failing and the cause is unclear — reduce it to its primitive operations, examine each one in isolation, and find which primitive is producing incorrect behavior.
- When evaluating a framework or orchestration library — understand what primitives it exposes and what it hides; prefer frameworks that let you access primitive behavior directly when needed.
- When building tools for agents — a tool call is one of the three primitives; tool design is a first-class concern, not a configuration detail.

## When NOT to

- When the system is complex enough that managing primitives directly is error-prone and higher-level abstractions are well-validated — at scale, working at the primitive level for every operation is not productive; use abstractions for routine orchestration and drop to primitives when debugging or optimizing.
- When the team building the system needs the guide rails that a framework's abstractions provide — not every team has the time or context to manage primitives directly for every interaction pattern.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: identifies the fundamental building blocks (augmented LLM, tool use, multi-agent networks) and argues that composing simple, well-understood building blocks outperforms building monolithic complex systems
- Amplifier — https://github.com/microsoft/amplifier — the kernel exposes three core mechanisms: model calls, tool dispatch, and recipe loops; all higher-level behaviors in the framework compose these three primitives
- OpenAI, "A practical guide to building agents" — https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ — decomposes every agent into three structural components: model, tools, and instructions; an analogous primitive-decomposition framing from a different axis (configuration vs. execution)

## Related

- `patterns/composable-patterns.md`
- `patterns/tools-for-agents.md`
- `patterns/workflows-vs-agents.md`
- `patterns/start-least-agentic.md`
