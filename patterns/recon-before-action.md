---
title: Lead With Recon Before Action
one_liner: Before taking any action that touches external state, first run a read-only reconnaissance pass to understand what exists, what constraints apply, and what the action will actually affect.
dimensions: orchestration
---

## What it is

Agents operating in real environments frequently take actions that are irreversible or hard to reverse: writing files, calling external APIs, creating database records, sending messages, modifying configurations. The naive approach is to proceed immediately: the task is to send an email, so call the email API; the task is to update a file, so write the file. The problem is that this skips the question of whether the action is correct in the current context. Is the file already at the correct version? Is the email already sent? Does the API endpoint have the shape the agent assumes? Does the target directory exist? Recon-before-action is the practice of running a lightweight, read-only investigation phase before any action that modifies state. The reconnaissance gathers ground truth: what exists now, what the invariants are, what the action space actually looks like from the current state. The agent then acts from known ground, not assumed ground. The cost is one additional step — usually cheap, often a single API call or file read. The payoff is a significant reduction in both erroneous actions and the work required to recover from them. Recon-before-action also produces a natural audit trace: the reconnaissance output is a record of what the agent knew before it acted, which makes post-hoc debugging far simpler.

## When to reach for it

- Before any write operation in an environment that the agent has not directly observed this session — verify the target exists and has the structure you expect before overwriting it.
- Before calling an external API with data — perform a lightweight check (a GET, a schema probe, a capability query) to confirm the endpoint, authentication, and shape before committing to the call with a payload.
- When the agent is operating in an environment shared with other processes or agents — the state may have changed since the last observation; recon before acting.
- When debugging a failing workflow — add a recon step to capture the state the agent saw before it took the action that failed.

## When NOT to

- When the action is idempotent and the cost of an unnecessary recon step exceeds the cost of any error that recon would catch — for example, writing a known-safe configuration file to a well-understood path.
- When the recon step itself has side effects or rate limits that make it as costly as the action — in that case, recon provides no advantage.
- When operating in a fully sandboxed environment where all actions are reversible — recon is a guard against irreversibility; if reversibility is guaranteed, the guard is unnecessary.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: emphasizes planning and verification steps before agents take actions with real-world consequences, particularly in agentic contexts where mistakes are difficult to reverse
- Amplifier — https://github.com/microsoft/amplifier-foundation — the foundation:explorer agent is a dedicated reconnaissance role: breadth-first exploration of code and docs producing citation-ready summaries, gathering ground truth for the orchestrator before modifying agents are dispatched
- Anthropic — https://code.claude.com/docs/en/best-practices — Claude Code best practices: defines an explicit four-phase Explore → Plan → Implement → Commit workflow where the first phase is strictly read-only; the guide calls this out as the primary defense against solving the wrong problem
- Xia et al., "Agentless: Demystifying LLM-based Software Engineering Agents" (arXiv:2407.01489) — https://arxiv.org/abs/2407.01489 — empirical support: achieves top results among open-source approaches on SWE-bench Lite with "a simplistic three-phase process of localization, repair, and patch validation, without letting the LLM decide future actions" — localization precedes any patch generation, recon structurally ahead of action

## Related

- `patterns/verify-independently.md`
- `patterns/auditable-artifacts.md`
- `patterns/fail-loud-harnesses.md`
- `patterns/prove-on-small-sample.md`
