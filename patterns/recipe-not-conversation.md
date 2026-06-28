---
title: Encode Multi-Step Work as a Recipe
one_liner: A conversation is a trace of what happened once — a recipe is a specification that can be replayed, inspected, versioned, and recovered from.
dimensions: reliability, workflow-discipline
---

## What it is

Multi-step work expressed as ad-hoc conversation — "now do X, now do Y, now do Z" — is inherently fragile: it cannot be replayed from a checkpoint, it has no schema to validate, it accumulates context silently until something breaks, and its state is invisible to anyone who wasn't present for the conversation. A recipe encodes the same work as a declarative specification: each step is named, its inputs and outputs are defined, its dependencies are explicit, and its execution can be resumed after interruption. Recipes are checkpointed, auditable, and version-controlled. They transform a one-time conversation into a reproducible workflow that a different agent, on a different day, can execute with the same result.

## When to reach for it

- Any multi-step workflow that will run more than once — encode it as a recipe the first time, not after the third failure.
- When a workflow involves more than two sequential steps with handoffs between agents — conversation becomes a liability at this scale.
- When you need recoverability: a recipe that checkpoints between steps can resume after interruption; a conversation cannot.
- When a workflow must be auditable — a recipe YAML is a version-controlled artifact; a chat history is not.
- When onboarding another agent or person to execute a workflow — a recipe is the specification; a conversation recap is a reconstruction from memory.

## When NOT to

- Truly one-off, exploratory, and immediately disposable interactions where the overhead of authoring a recipe exceeds the value of the work — quick questions, single-turn queries, throwaway experiments.
- Work that is inherently interactive and responsive, where the next step cannot be known until the previous result is seen and human judgment is required at every branch — in those cases, the recipe is the human-in-the-loop checkpoint design, not the full specification.
- Steps so trivially atomic that a recipe adds no structural value over a single function call.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends structured workflow specifications over ad-hoc agent conversation for complex tasks, citing recoverability and auditability as primary benefits
- Amplifier — https://github.com/microsoft/amplifier — the Amplifier recipe system (YAML-declared steps, staged execution, approval gates, and automatic checkpointing) is the canonical implementation of this pattern: conversation-time instructions become recipe-time specifications
