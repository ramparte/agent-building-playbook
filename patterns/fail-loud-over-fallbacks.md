---
title: Fail Loud Over Fallbacks
one_liner: A fallback that hides a failure teaches the system nothing and costs the same as the failure it replaced — prefer a loud stop over a silent substitution.
dimensions: reliability
---

## What it is

When a pipeline step fails, there are two instincts: fail loud (surface the failure immediately with the name, the step, and the reason) or fall back silently (substitute a default, swallow the exception, and let the pipeline continue as if nothing happened). The fallback instinct optimizes for apparent continuity at the cost of actual reliability. A silent fallback hides the failure from the orchestrator, from monitoring, and from the human reviewing the output — producing results that look correct but are built on a substituted answer rather than the real one. Fail-loud means the pipeline stops at the point of failure, names the failure precisely, and refuses to proceed until the failure is addressed. This is harder to build and requires better error handling downstream, but it is the only design that keeps the system's self-knowledge accurate.

## When to reach for it

- Any pipeline step that produces output consumed by a subsequent step — a silent failure here propagates silently through every downstream step.
- Evaluation and testing harnesses of any kind — harnesses that swallow agent failures produce misleadingly high pass rates.
- Agentic workflows where tool calls may fail — surface the tool failure immediately rather than letting the agent reason around it as if it succeeded.
- When designing error handling: write the failure path before the happy path — the failure case is more important to get right than the success case.
- When an existing system has been producing wrong outputs and you cannot trace the origin — look for silent fallbacks; they are the most common cause.

## When NOT to

- User-facing products where a visible error is worse than a controlled degradation (e.g., displaying a cached result when the live API fails) — but even here, log the failure loudly internally so the degradation is observable.
- Genuinely optional enhancements where absence of the feature is explicitly acceptable and documented — the fallback is the intended behavior, not a hidden failure.
- Retry logic where the first failure is expected and the system is designed to retry before surfacing — fail loud on final exhaustion, not on the first attempt.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends that tools and agents surface errors explicitly rather than masking them, enabling the orchestrator and human reviewer to observe failures rather than receiving silent substitutions
- Amplifier — https://github.com/microsoft/amplifier — the honest-stopping principle in agent base instructions: when a required item cannot be satisfied with real evidence, the agent must stop and report rather than fabricate a plausible-looking result (per the Amplifier team's white papers; not visible in the current public repos)
- Shore, "Fail Fast" (IEEE Software, 2004) — https://www.jamesshore.com/v2/blog/2004/fail-fast — classic antecedent: the canonical software engineering articulation of why detecting and surfacing errors immediately produces more robust systems than attempting graceful continuation
