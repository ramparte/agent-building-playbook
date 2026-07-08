---
title: Composable Orchestration Patterns
one_liner: Build orchestration from a small set of named, reusable primitives — sequences, conditionals, fan-outs, and loops — rather than writing bespoke control flow for every workflow.
dimensions: orchestration
---

## What it is

Orchestration logic has a tendency to grow into unmaintainable procedural code: if-else trees nested inside loops inside callbacks, with workflow state threaded through as mutable variables. The alternative is to build from a small set of named orchestration primitives — sequence, conditional, fan-out, fan-in, loop, gate — and express any workflow as a composition of these patterns rather than as custom logic. A sequence runs steps in order. A conditional branches based on the output of a preceding step. A fan-out spawns parallel workers. A fan-in waits for parallel workers to complete and aggregates their results. A loop runs a step repeatedly until a condition is met. A gate waits for human approval before proceeding. These are not special-purpose constructs — they are the vocabulary of orchestration. Any workflow can be expressed as a tree of these patterns, and a workflow expressed this way can be read, modified, and debugged by anyone who knows the vocabulary. It can also be tested by substituting a pattern implementation with a test double, because each primitive is isolated from the others. When orchestration is instead written as bespoke procedural code, every new workflow is a new language and every debugging session requires understanding that language from scratch.

## When to reach for it

- When designing a new workflow of more than three or four steps — identify which orchestration patterns you need and express the structure as a composition of those patterns before writing code.
- When the control flow of an existing workflow is unclear — refactor it by extracting the recognizable patterns (loops, conditionals, gates) and making them explicit.
- When building a workflow authoring layer or DSL — start from a small set of composable primitives rather than a rich feature set; the primitives compose to cover the rich cases.
- When onboarding new team members to a workflow — a workflow expressed as composed primitives can be explained in terms of the primitive vocabulary rather than requiring a walkthrough of custom code.

## When NOT to

- When the workflow is a single step or two — composition overhead is not justified for workflows that are not actually complex.
- When the available orchestration system provides its own fixed set of primitives that cannot be composed freely — in that case, work within the system's model rather than inventing a parallel composition layer on top.
- When performance requirements demand tightly coupled control flow with minimal overhead — composable patterns carry abstraction cost, and in hot loops that cost can matter.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier-bundle-recipes — the recipe YAML format exposes composable primitives (sequenced steps, foreach loops, requires_approval gates) that allow complex workflows to be expressed declaratively as compositions
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: names five workflow primitives (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) as the composable building blocks from which production agentic systems are assembled
- Huang & Zhou, "A Two-Dimensional Framework for AI Agent Design Patterns: Cognitive Function and Execution Topology" (arXiv:2605.13850) — https://arxiv.org/abs/2605.13850 — formalizes: defines six execution topology archetypes (Chain, Route, Parallel, Orchestrate, Loop, Hierarchy) that map directly to the composable orchestration primitives described in this pattern; proposes a 7×6 matrix of 28 named patterns arising from combining topology with cognitive function

## Related

- `patterns/workflows-vs-agents.md`
- `patterns/three-primitives.md`
- `patterns/gate-the-phases.md`
- `patterns/recipe-not-conversation.md`
