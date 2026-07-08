---
title: Start With the Least Agentic Thing
one_liner: Many problems that look like multi-agent workflows need only one well-crafted LLM call.
dimensions: meta-principles, orchestration
---

## What it is

The pull toward full autonomy, long-running loops, and multi-agent orchestration is strong — and usually premature. Most problems that reach for an autonomous agent actually need a single, well-structured prompt with a well-chosen model and good inputs. Start with the least agentic option: a direct LLM call with no loop, no tools, and no orchestration. Add complexity only when you have evidence that the simpler approach cannot close the gap, and add it one increment at a time, not by jumping to the most autonomous architecture available.

## When to reach for it

- When designing a new workflow: ask first whether a single well-crafted prompt could solve the problem before reaching for agents.
- When an agent loop exists and you can't explain why the single-call approach would be insufficient.
- When a multi-agent system is failing or producing inconsistent results — ask whether collapsing it to fewer, more reliable steps would help.
- As a cost and latency heuristic: every agent step multiplies latency, cost, and surface area for failure; start from zero and add only what's proven necessary.

## When NOT to

- Tasks that intrinsically require iterative feedback (code execution, tool use with result inspection, multi-turn negotiation with an external system) — these genuinely benefit from agentic loops.
- Long-horizon tasks that exceed what a single context window can hold without losing essential state — multi-step approaches are structurally necessary here, not a preference.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: explicitly recommends starting with the simplest prompt-based approach and only escalating to agents when simpler solutions are proven insufficient
- Amplifier — https://github.com/microsoft/amplifier-bundle-recipes — workflows declared as YAML steps executed in stages with approval gates and automatic checkpointing — deterministic, predefined orchestration to reach for before granting an agent open-ended autonomy
- Ward Cunningham, "The Simplest Thing That Could Possibly Work" (Artima, 2004) — https://www.artima.com/articles/the-simplest-thing-that-could-possibly-work — classic antecedent: the XP principle of always attempting the simplest viable solution first and adding complexity only when the simple version demonstrably fails
- Simon Willison — https://simonwillison.net/2024/Dec/20/building-effective-agents/ — practitioner commentary emphasizing the five workflow patterns as intermediate steps before reaching for agents; "find the simplest solution possible, and only increasing complexity when needed"

## Related

- `patterns/reliability-before-features.md`
- `patterns/code-is-cheap-maintenance-isnt.md`
