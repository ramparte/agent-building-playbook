---
title: Hand Off With a Clear Stop Condition
one_liner: An agent without a stop condition will find one itself — and it will not be the one you wanted.
dimensions: workflow-discipline, orchestration
---

## What it is

When a task is handed to an agent, a human, or a downstream system without a defined stop condition, the recipient will determine their own stopping point — based on their local sense of "done," their budget, their context, or their default behavior. That self-determined stop condition is almost never aligned with the orchestrator's intent. A clear stop condition specifies exactly what constitutes completion: a specific file produced, a test passing, a threshold reached, a signal emitted, or an explicit count of items processed. Without it, handoffs become open-ended, work expands to fill available capacity, and the orchestrator has no reliable way to detect completion without re-inspecting the full output.

## When to reach for it

- Every time a task is delegated to a sub-agent: include the stop condition in the instruction, not just the task description.
- When designing agentic loops: define the termination condition before writing any loop logic.
- When a pipeline step could legitimately stop at multiple points: specify which one is correct for this invocation.
- When handoffs involve LLM calls: LLMs will complete their own stop condition if none is provided, and it will be some local notion of "the answer is done," not your orchestration-level definition.
- When debugging an agent that ran too long or too far: the missing stop condition is the most common root cause.

## When NOT to

- Tasks so small and atomic that the stop condition is identical to the task description itself — "return the count" has an inherent stop condition.
- Exploratory agentic tasks where the stop condition is explicitly "stop when you have formed a judgment" and that judgment is the output — but even here, specify a time or cost budget as a practical bound.
- When the downstream system enforces its own stop condition correctly and you have verified it — don't duplicate a constraint that is already reliably enforced.

## Exemplars

- Amplifier delegate() calls include an instruction that specifies what the agent should return and when it should stop — agents without that instruction will continue until context is exhausted (per the Amplifier team's white papers; the delegate() API is not visible in the current public repos).
- Loop termination in formal specification languages (TLA+, Alloy) is defined before the loop body — the discipline of specifying stop conditions before behavior is the same principle applied to formal verification.
- Anthropic, "Building Effective Agents" — https://www.anthropic.com/research/building-effective-agents — formalizes: recommends including explicit stopping conditions (such as a maximum number of iterations) in agent loops so orchestrators maintain control rather than relying on the agent's own sense of done
