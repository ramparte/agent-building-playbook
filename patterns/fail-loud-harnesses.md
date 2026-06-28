---
title: Fail-Loud Harnesses
one_liner: Build harnesses that fail visibly — a harness that silently substitutes its own answer hides the agent's failure from you.
dimensions: meta-principles, reliability, tool-design
---

## What it is

A test harness that handles agent failures "helpfully" — by falling back to a default answer, swallowing exceptions, or completing the task itself when the agent cannot — teaches you nothing about the agent. Worse, it creates the illusion of success where none exists. Fail-loud harnesses are designed with the opposite instinct: when an agent step fails, the harness surfaces that failure immediately and loudly, naming the file, the step, and the reason, rather than papering over it.

## When to reach for it

- Any eval or test harness that wraps an LLM or agent call: make the failure path loud before the happy path clean.
- When a silent failure mode exists in your harness (e.g., a `try/except` that swallows errors and returns a default).
- When you discover that a harness has been masking failures — your pass rate looks high but the agent outputs are wrong.
- When integrating a new tool call: write the error path first, before the success path.

## When NOT to

- User-facing products where silent degradation (a sensible fallback) is preferable to an error surface visible to the end user — but even then, log loudly internally.
- When the harness is a safety net and controlled fallback is intentional and documented — but this is a product decision, not an evaluation one.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: discusses tool design including the principle that tools should surface errors clearly rather than masking them
