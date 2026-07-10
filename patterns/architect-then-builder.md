---
title: Two-Phase Build: Architect Then Builder
one_liner: Separate design from implementation by running an architect agent first to produce a complete specification, then a builder agent to implement it — never conflate the two roles in one pass.
dimensions: orchestration, workflow-discipline
---

## What it is

Design and implementation are cognitively distinct activities. A model that is simultaneously figuring out what to build and building it tends to make local decisions that look reasonable in isolation but are globally inconsistent — the early modules are designed differently from the late ones, the interfaces are discovered rather than specified, and refactoring is needed immediately because the design evolved as the code was written. The two-phase pattern separates these activities into distinct agent roles. The architect agent receives the goal and produces a specification: the module boundaries, the data models, the interface contracts, the sequencing of implementation tasks. The spec is the output — not code. Only when the spec is complete and reviewed does the builder agent begin. The builder implements exactly the spec. It does not redesign; it does not improve interfaces it considers suboptimal; it does not add features the spec did not include. If the builder discovers that the spec is incomplete or inconsistent, it surfaces that as a finding rather than silently resolving it through implementation choices. The architect and builder are cleanly separated, and the separation enforces a discipline that a single-agent approach cannot maintain: you cannot implement a design you have not finished making.

## When to reach for it

- When building anything with more than two or three modules — without a full design pass, interfaces drift as implementation proceeds.
- When the work will be executed by multiple agents or multiple team members — a shared spec ensures each builder is implementing the same design.
- When the scope is ambiguous enough that the implementer would need to make non-trivial design decisions — those decisions belong in the architect phase, not the implementation phase.
- When quality review is required before merging — a spec gives the reviewer a target to check the implementation against, rather than requiring the reviewer to reverse-engineer the intended design from the code.

## When NOT to

- When the task is a single, self-contained change with no meaningful design surface — adding a parameter to an existing function, fixing a bug in a well-understood component — the architect phase adds no value and only delays delivery.
- When the user or stakeholder has already provided a complete specification — the architect phase is complete; proceed directly to builder.
- When the workflow is exploratory and the design must emerge from implementation — some problems cannot be fully specified upfront; a strict architect-then-builder split forces false specificity in the spec.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier-foundation — the foundation agent roster explicitly separates the zen-architect agent (system design with ruthless simplicity) from the modular-builder agent (building code from specifications); design comes from one role, implementation from the other
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes the orchestrator-workers workflow, in which a central model breaks a complex task into subtasks and delegates them to workers, and checkpoints where agents can pause for human feedback; the architect-builder split turns that decomposition into an explicit role separation
- Harper Reed — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/ — "My LLM codegen workflow atm": practitioner account of a three-phase spec→plan→execute workflow for LLM codegen (produces spec.md, then prompt_plan.md + todo.md, then executes); popularized the discipline of completing design before touching implementation
- Wang et al., "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models" (arXiv:2305.04091) — https://arxiv.org/abs/2305.04091 — classic antecedent: formalizes plan-then-execute as a prompting strategy, showing that separating "devise a plan" from "carry out the plan" reduces errors; cognitive basis for the architect-then-builder split at the prompt level

## Related

- `patterns/bite-sized-tasks.md`
- `patterns/gate-the-phases.md`
- `patterns/proposer-authority-separation.md`
- `patterns/composable-patterns.md`
