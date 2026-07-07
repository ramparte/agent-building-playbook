---
title: Fix Reliability Before Features
one_liner: Flakiness, not capability, is the enemy — a system that only sometimes works is harder to improve than one that reliably fails.
dimensions: meta-principles, reliability
---

## What it is

The instinct to add capabilities before fixing reliability is almost always wrong. A system that succeeds 70 percent of the time is not a 70-percent solution — it is an unreliable system that produces unreliable data, unreliable user trust, and unreliable signal for further improvement. Flakiness masks every other problem: you cannot tell whether a prompt change helped or hurt if the baseline is already noisy. A system that reliably fails is infinitely more useful than one that intermittently succeeds, because reliable failure is measurable, diagnosable, and improvable.

## When to reach for it

- Before adding any new capability, confirm the existing capabilities run cleanly and repeatably.
- When an eval or workflow shows high variance across runs with no change in inputs — fix that before moving on.
- When stakeholders are asking for more features and the current system is already flaky — the conversation about reliability must come first.
- After any infrastructure change: verify reliability has not regressed before building on top.

## When NOT to

- Early prototyping where the goal is to discover what is even possible — some flakiness is acceptable when you are still exploring the problem space.
- When reliability requires infrastructure that doesn't exist yet and the prototype is strictly time-boxed — but document the debt and plan to pay it.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends starting simple and only adding complexity once the simpler system is reliable
- Beyer et al., *Site Reliability Engineering*, "Embracing Risk" (Google, 2016) — https://sre.google/sre-book/embracing-risk/ — classic antecedent: error budgets operationalize the trade-off — when the reliability budget is exhausted, new releases halt until it is restored, encoding reliability as the gate on feature velocity
