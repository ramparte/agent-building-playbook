---
title: Run Independent Agents in Parallel
one_liner: When two or more tasks have no ordering dependency and no shared mutable state, run them in parallel agents rather than sequentially — wall-clock latency is the only cost that matters.
dimensions: orchestration
---

## What it is

Independent tasks — tasks with no ordering dependency and no shared mutable state — are the genuine case for parallel execution. When an orchestrator has a set of tasks that each need a separate context window and do not depend on each other's outputs, running them sequentially is pure waste: the orchestrator waits for each to finish before beginning the next, while compute sits idle. The correct pattern is to dispatch all independent tasks simultaneously, then wait for all results before proceeding. This is not premature optimization; for any non-trivial independent task set, the wall-clock speedup is linear in the number of tasks. The critical discipline is verifying independence before dispatching. Two tasks are independent if: task B does not need any output from task A; task A and task B do not write to the same shared resource; and the order in which their results are integrated does not matter. If any of these is false, the tasks are not independent and sequential execution is required. The most common failure mode in parallel orchestration is asserting independence that does not exist — declaring tasks parallel because they look separate, then discovering mid-run that they share a file, a database row, or a context assumption. Independence must be verified before dispatch, not assumed.

## When to reach for it

- When the orchestrator has three or more analysis tasks to run on the same input (e.g., three different types of code review on the same file) — all can start simultaneously.
- When the orchestrator must gather information from multiple independent sources before making a decision — dispatch all lookups in parallel, then aggregate.
- When running tests across multiple modules that share no state — dispatch the test agents in parallel and wait for all results.
- When the per-task latency is dominated by model response time or external I/O — parallelism reclaims the majority of that wall-clock cost.

## When NOT to

- When tasks have any dependency — if task B needs task A's output to form its inputs, they must run in sequence.
- When tasks write to shared mutable resources and there is no conflict-detection mechanism — concurrent writes without coordination corrupt state.
- When the number of parallel agents would exceed resource limits (rate limits, API quotas, system concurrency caps) — throttle the fan-out to stay within bounds.
- When the total compute cost matters more than wall-clock latency — parallel execution consumes the same compute as sequential but faster; if compute budget is the constraint, parallelism does not help.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: identifies parallelization as a core orchestration pattern, specifically when tasks can be broken into independent subtasks; notes the speedup is linear in the number of parallel workers for truly independent tasks
- Amplifier — https://github.com/microsoft/amplifier — recipes run iteration sets sequentially by default, with concurrent execution as an explicit opt-in (parallel: true) reserved for task sets that are genuinely independent
- Hadfield et al. / Anthropic — https://www.anthropic.com/engineering/multi-agent-research-system — How we built our multi-agent research system: empirical case study where parallel subagents each explore independent research streams, yielding a 90.2% performance gain over single-agent; authors explicitly note this advantage weakens for coding tasks with fewer truly parallelizable units

## Related

- `patterns/single-threaded-default.md`
- `patterns/composable-patterns.md`
- `patterns/architect-then-builder.md`
- `patterns/build-five-to-throw-away.md`
