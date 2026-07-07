---
title: Put Deterministic Rails Around Model Judgment
one_liner: The strongest agentic workflows interleave deterministic steps and model-mediated steps so neither layer must be perfect — the model translates intent into checkable state, and scripts, tests, and validators catch drift.
dimensions: orchestration, reliability, verification, tool-design
---

## What it is

A productive agentic workflow is rarely "all AI." The strongest systems alternate between nondeterministic model judgment and deterministic computation, pairing each model step with a check it cannot talk its way past. A model writes a plan; a script verifies that every file it references actually exists. A model implements a sprint; the test suite deterministically passes or fails. A model reviews a diff; a linter enforces style and types underneath it. A model judges whether a user story is satisfied; browser automation records the evidence. A human approves a compliance-sensitive step; a workflow runner logs the decision immutably. A model summarizes production logs; a time-series system supplies the raw telemetry it is summarizing. This hybrid structure is powerful precisely because it reduces the burden on any single layer: the model need not be perfect, because the surrounding graph catches its drift, and the deterministic systems need not understand intent, because the model nodes translate intent into checkable state for them. The interleaving is the design — model where ambiguity, synthesis, diagnosis, and language understanding are required; deterministic rails everywhere a fact can simply be checked. Building the individual check the agent cannot argue with — the unyielding validator itself — is its own discipline; this pattern is about the interleaving, about which steps are model and which are rail (see Critic Applications).

## When to reach for it

- Whenever a model step emits something verifiable — a file path, a passing test, a type, a status code — bolt a deterministic check directly onto it rather than trusting the prose.
- When model output feeds an irreversible or expensive downstream action: put a deterministic gate (test, schema check, policy engine) on the edge.
- When you need evidence, not assertion — have automation capture proof (screenshots, logs, recorded runs) that the model's claim is true.
- When a workflow must satisfy compliance or audit: pair human and model judgment with a deterministic runner that logs every decision.
- When debugging why a workflow fails intermittently — the missing deterministic rail is usually where the drift slips through.

## When NOT to

- Open-ended creative or exploratory work with no checkable success condition — there is no deterministic rail to build, and forcing one constrains the work falsely.
- When a cheap deterministic check would simply duplicate a stronger one already on the edge — add rails where drift actually escapes, not everywhere.
- When the check is harder to maintain than the failure it catches is costly — a brittle validator that breaks more often than the model does is negative leverage.
- Before the work is stable enough to know what "checkable state" even means — rails encode an understood contract, not a guess.

## Exemplars

- Dex Horthy, "12-Factor Agents" — https://github.com/humanlayer/12-factor-agents — origin: Factor 8 ("Own Your Control Flow") formalizes the interleaving philosophy; the guide argues that successful agents are "mostly deterministic software with LLM steps sprinkled in at just the right points" and that owning control flow enables the transparency between tool selection and invocation needed for human oversight

## Related

- `patterns/shape-work-as-an-attractor.md`
- `patterns/auditor-agent.md`
- `patterns/recipe-not-conversation.md`
- `patterns/start-least-agentic.md`
