---
title: Use Sub-Agents as Context Sinks
one_liner: Delegate detail-heavy work to sub-agents so the orchestrator's context stays clean — the sub-agent absorbs the complexity and returns only a summary.
dimensions: context-engineering, orchestration
---

## What it is

Every task an orchestrator handles in its own context accumulates tokens: the tool calls, the intermediate reasoning, the verbose outputs, the failed branches. Over a long workflow this accumulation degrades the orchestrator's ability to reason about the whole — early decisions get crowded out by recent noise, and the window fills with content relevant only to a sub-task that is now complete. Sub-agents as context sinks invert this dynamic: when a task is detail-heavy but its outcome is a clear artifact or summary, delegate it entirely to a fresh agent. That agent runs with an empty context window, absorbs all the detail of the sub-task, and returns only its result — a file path, a structured summary, a pass/fail verdict, a generated artifact. The orchestrator's context accumulates a summary, not a transcript. The detail is permanently off the orchestrator's books. This is not primarily a performance optimization; it is a cognitive architecture decision about what the orchestrator needs to hold in mind to make good decisions about the next step.

## When to reach for it

- When a sub-task has a clear, expressible output but a complex execution path (file analysis, code review, research, synthesis) — delegate it and receive the output, not the process.
- When the orchestrator is approaching context limits partway through a plan — identify the next heavy task and route it to a sub-agent before context fills further.
- When the same type of sub-task recurs across multiple steps (reviewing N files, processing N records) — each instance is a separate context sink; parallelize if the tasks are independent.
- When an error or failure in a sub-task should not pollute the orchestrator's context with retry loops and diagnostic output — isolate the failure in the sub-agent, receive a structured failure report, and decide at the orchestrator level what to do.

## When NOT to

- Tasks where the orchestrator must reason over the details of the sub-task's execution, not just its outcome — some debugging or exploratory tasks require the orchestrator to see the intermediate steps, not just the result.
- When the sub-task is trivially small — creating a sub-agent for a single file read or a one-line transformation adds latency and coordination cost with no context benefit.
- When the sub-task's result is so large that the summary returned to the orchestrator is nearly as expensive as running the task in the orchestrator's own context — apply compress before choosing between in-context and delegated execution.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes sub-agent delegation as a primary pattern for managing context in orchestrator-worker architectures
- Amplifier — https://github.com/microsoft/amplifier — the task tool is designed precisely for this pattern: it spawns a child session that runs its own orchestrator loop, absorbs the work in a separate context, and returns its result to the calling session
- Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system — origin: describes subagents explicitly as context compression mechanisms—"subagents facilitate compression by operating in parallel with their own context windows... before condensing the most important tokens for the lead research agent"
- LangChain Team — https://www.langchain.com/blog/context-engineering-for-agents — formalizes: names "isolate" as one of the four canonical context-engineering moves; splitting context across agents or environments is the mechanism that prevents orchestrator accumulation
- Yan, "Don't Build Multi-Agents" — https://cognition.com/blog/dont-build-multi-agents — counterpoint: argues dispersed decision-making across sub-agents fragments context in ways that cause inconsistency; read alongside the "When NOT to" criteria for tasks requiring shared intermediate state

## Related

- `patterns/context-is-finite.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/thin-pointers.md`
- `patterns/start-least-agentic.md`
