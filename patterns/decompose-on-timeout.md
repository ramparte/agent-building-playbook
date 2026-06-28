---
title: Decompose and Retry on Timeout
one_liner: When a task times out, the answer is almost never to raise the timeout — it is to break the task into smaller pieces.
dimensions: workflow-discipline, orchestration
---

## What it is

A timeout is a signal that a task is too large for the time budget the system has allocated. The instinct to fix it by raising the timeout is almost always wrong. Longer timeouts increase latency for every run, make failure detection slower, and hide the underlying decomposition problem rather than solving it. When a task times out, the correct response is to decompose it: break it into smaller units that complete reliably within the original time budget, and orchestrate those units rather than running the whole as a single monolith. This applies to LLM calls, agent runs, batch jobs, API requests, and database queries equally. Decomposition also enables parallelism that would otherwise be impossible in a monolithic run.

## When to reach for it

- When a task, agent run, or LLM call times out repeatedly — the task is too large, not the timeout too short.
- When a batch job is consistently slow — decompose into smaller batches, process each independently, and aggregate results.
- When an agent loop times out mid-task — design the loop so each iteration completes a meaningful, checkpointable unit, not an arbitrarily large slice.
- When a single LLM call is producing low-quality output on a complex task — the task may be too large for a single call; break it into a pipeline of smaller calls.
- When diagnosing a timeout: before touching any configuration, ask whether decomposition is feasible.

## When NOT to

- When the timeout is caused by external infrastructure (network latency, slow third-party API, disk I/O) rather than task size — decomposition won't fix latency imposed by systems outside your control.
- When the task is genuinely atomic and cannot be meaningfully decomposed — in those cases, document why, accept the longer timeout as a known exception, and add monitoring so it doesn't silently grow further.
- When decomposition would break required transactional semantics — some tasks must complete as a unit and partial completion is worse than timeout; know which category you are in before decomposing.

## Exemplars

- Database query optimization almost always involves decomposition: a slow full-table scan becomes a sequence of indexed lookups; a monolithic query becomes a staged pipeline. The timeout is the signal; decomposition is the fix.
- Anthropic's building-effective-agents guidance recommends breaking long-horizon tasks into explicit steps with checkpointing — decompose-on-timeout is that principle applied reactively when a step proves too large.
