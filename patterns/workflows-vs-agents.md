---
title: Distinguish Workflows From Agents
one_liner: A workflow is a fixed sequence of steps with known branching; an agent decides dynamically what to do next. Conflating the two produces systems that are harder to test, monitor, and trust.
dimensions: orchestration
---

## What it is

Workflows and agents occupy different points on a control spectrum, and choosing the wrong abstraction produces real costs. A workflow is a predetermined control flow: step A runs, then step B, then a conditional that leads to either C or D. The path is known in advance; the model fills in content at each step but does not choose the path. An agent is a control loop where the model decides what to do next at each turn, selecting from available tools and actions based on the current state. The distinction matters operationally. Workflows are predictable, testable, and auditable — you can trace every execution against a fixed graph. Agents are adaptive and flexible — they can handle situations the designer did not anticipate — but they are also non-deterministic in their control flow, harder to test exhaustively, and more likely to go down unexpected paths. Most practical systems that are called agents are actually workflows: the model fills in text, makes a classification, or generates a plan, but the control flow is fixed by the code. Naming these correctly is not a semantic preference. If a team believes they are building an agent but they have actually wired a workflow, they will design for flexibility they cannot have and be surprised when the system cannot deviate from the programmed path. If they believe they have a workflow but the model is actually driving control flow, they will underestimate the surface area for unexpected behavior.

## When to reach for it

- When designing a new system: decide upfront whether you want predetermined control flow (workflow) or dynamic tool selection (agent). Name the architecture, write it down, and test against that model.
- When a workflow is growing complex branching logic driven by model output — before adding more conditionals, ask whether you should be building an agent with tool selection instead.
- When debugging: if the system is taking unexpected paths, check whether control flow is supposed to be determined by code or by model — the failure modes differ significantly.
- When staffing and testing: workflow logic can be unit-tested against known paths. Agent loops require behavioral testing across diverse prompts and inputs.

## When NOT to

- When the distinction does not matter operationally — some systems are simple enough that calling them workflow-or-agent is just taxonomy, not an architectural decision with consequences.
- When the system genuinely lives in the middle of the spectrum — a workflow with one or two agent-driven decisions is neither purely one nor the other, and forcing it into a label creates more confusion than it resolves.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: draws the workflow-agent distinction explicitly and provides examples of each, arguing that many "agent" systems are better implemented as pipelines
- Amplifier — https://github.com/microsoft/amplifier — the recipe system provides workflow primitives (step, stage, foreach, while) separate from agent delegation, making the distinction explicit in the authoring model
- LangChain, "Workflows and agents" (LangGraph docs) — https://docs.langchain.com/oss/python/langgraph/workflows-agents — defines the same distinction in framework terms: workflows have "predetermined code paths," agents "dynamically define their own processes and tool usage"; represents the distinction codified in a widely-used production framework

## Related

- `patterns/single-threaded-default.md`
- `patterns/composable-patterns.md`
- `patterns/recipe-not-conversation.md`
