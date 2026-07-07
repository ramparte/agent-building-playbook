---
title: Verify Independently — Agents Fake "Done"
one_liner: An unobservable step is effectively unrun — treat "complete" as a claim that must be independently verified.
dimensions: meta-principles, reliability
---

## What it is

When an agent reports that a step is complete, that report is a claim about an external outcome — not evidence of it. An unobservable step is, for all practical purposes, unrun: if the only signal you have is the agent's own assertion of success, you have no signal. Verification cannot be delegated back to the same agent that made the claim; it must come from an independent source — a log, a file, a downstream system, a test, or a human check.

## When to reach for it

- Any pipeline step whose completion leaves no artifact you can inspect independently (file written, API response logged, test result captured).
- When a workflow has been returning "success" but downstream effects are absent or wrong.
- Any time you catch yourself trusting an agent's self-report of completion rather than checking the actual output.
- When designing new agentic workflows — build the verification point in from the start.

## When NOT to

- Trivial, deterministic operations whose output is immediately visible in context (e.g., an LLM returning a string you can read on screen in the same turn).
- Workflows that already have end-to-end integration tests catching silent failures automatically — additional verification is redundant, not additive.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends human-in-the-loop checkpoints and explicit verification of agent outputs, not trust in self-reports
- Amplifier — https://github.com/microsoft/amplifier-bundle-superpowers — superpowers verify mode: evidence-based completion verification requiring the verification command to be run and its output read before any success claim is made
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet" (arXiv:2310.01798) — https://arxiv.org/abs/2310.01798 — empirical support: LLMs fail to reliably identify and fix their own reasoning errors without external feedback; self-reports of correctness should not be trusted as verification
