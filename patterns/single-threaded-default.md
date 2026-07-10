---
title: Default to a Single-Threaded Linear Agent
one_liner: Run one task at a time in sequence unless you have a concrete reason to fan out — parallelism is an optimization, not a starting point.
dimensions: orchestration
---

## What it is

The instinct when designing multi-step workflows is to run as much as possible in parallel. Resist that instinct as the default. A single-threaded, linearly sequenced agent — step one completes, step two begins — is far easier to reason about, debug, and modify than a concurrent fan-out. You know exactly what happened in what order. You can read the trace top to bottom. When something goes wrong, the failure site is localized and the prior context is intact. Parallelism introduces race conditions, conflicting writes, interleaved context, and compound failure modes. These are solvable problems, but solving them costs complexity, and complexity in agentic systems tends to compound. Before reaching for parallel execution, ask: does the current bottleneck actually come from serial execution? In many cases the answer is no — the bottleneck is I/O latency, model response time, or human review cycles that no amount of internal concurrency resolves. Start linear. Profile before optimizing.

## When to reach for it

- When building a new workflow and you have not yet demonstrated that serialization is the bottleneck — start here.
- When the steps in a workflow have implicit ordering constraints: step two needs step one's output, step three needs step two's judgement, and so on down the chain.
- When debugging a multi-agent system that is behaving unexpectedly — collapse to linear execution to isolate the failure before reintroducing parallelism.
- When the workflow runs infrequently or the latency budget is not tight — the maintenance cost of parallel orchestration is not justified.

## When NOT to

- When you have a set of tasks that are demonstrably independent (same inputs, no shared state, no ordering dependency) and the wall-clock latency of serial execution materially affects the outcome or user experience — that is the genuine case for parallelism.
- When the tasks are embarrassingly parallel and identical in structure (e.g., running the same analysis on fifty documents) — fan-out is the right model here, and the orchestration pattern for it is well-understood.
- When external I/O operations dominate (multiple API calls, file fetches, or search queries) and the model is idle waiting for results — concurrency here is often cheap to implement and high-value in latency savings.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends beginning with the simplest architecture that could work and adding orchestration complexity only when evidence demands it
- Amplifier — https://github.com/microsoft/amplifier — the framework's recipe system defaults to sequential step execution; fan-out and parallel tracks are explicit opt-ins, not the baseline
- Walden Yan, "Don't Build Multi-Agents" (Cognition, June 2025) — https://cognition.com/blog/dont-build-multi-agents — explicitly advocates single-threaded linear agents as the default architecture: the simplest way to follow the context-sharing and implicit-decisions principles, and one that 'will get you very far'

## Related

- `patterns/parallel-independent-tracks.md`
- `patterns/start-least-agentic.md`
- `patterns/autonomy-when-justified.md`
