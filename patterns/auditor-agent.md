---
title: Use a Second Agent as Auditor
one_liner: The agent that did the work is the worst possible choice to verify the work — put a second agent in the audit seat with no stake in the original claim.
dimensions: reliability, orchestration
---

## What it is

When a task is completed by an agent, that agent's verification of its own output is structurally compromised: it is reasoning from the same assumptions, biases, and context that produced the original work. A second agent placed in the auditor role has none of those anchors. It reads the artifact cold — without the history of decisions that led to it — and applies independent judgment about whether the output matches the specification, whether required steps were actually taken, and whether claims of success are backed by evidence. The auditor agent is not asked to redo the work; it is asked to verify the work's outputs against stated requirements. The separation of roles is the mechanism that makes the verification meaningful.

## When to reach for it

- Any high-stakes pipeline step whose failure has significant downstream costs — add an auditor agent before the output is consumed by the next stage.
- When an agent has a history of falsely reporting completion — an auditor surfaces the pattern systematically rather than catching it case by case.
- Before any irreversible action (deploying, sending, deleting, publishing) — route through an auditor agent first.
- When implementing a multi-agent workflow: design the auditor role explicitly as part of the orchestration, not as an afterthought.
- When compliance or accountability is required: the auditor agent's verdict becomes the audit trail.

## When NOT to

- Simple deterministic steps where the output is machine-checkable without reasoning (e.g., file exists, test passes, HTTP status 200) — use a deterministic verifier instead of an agent.
- Tight interactive loops where the latency of a second agent call exceeds the acceptable feedback cycle — use auditor agents at checkpoints, not at every micro-step.
- When the audit itself is a conflict of interest (same model, same context, same prompt) — the second agent must be genuinely independent to provide meaningful verification.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes the evaluator-optimizer workflow — one model generates while a second evaluates against criteria in a loop — separating generation from evaluation to improve output quality
- Amplifier — https://github.com/microsoft/amplifier-bundle-superpowers — the superpowers bundle ships dedicated spec-reviewer and code-quality-reviewer agents as auditor roles downstream of the implementer agent; the spec-reviewer's sole job is to evaluate whether the implementation matches its specification, checking the work itself rather than the implementer's self-report
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet" (arXiv:2310.01798) — https://arxiv.org/abs/2310.01798 — empirical support: LLMs reviewing their own outputs degrade rather than improve performance, establishing why the auditor must be a structurally separate agent rather than a self-review pass
- Krakovna et al., "Specification Gaming: The Flip Side of AI Ingenuity" (2020) — https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ — empirical support: catalogs how agents satisfy literal objectives while failing intended outcomes — the failure mode an independent auditor exists to catch
- McAleese et al. (OpenAI), "LLM Critics Help Catch LLM Bugs" (arXiv:2407.00215) — https://arxiv.org/abs/2407.00215 — empirical support: the CriticGPT work — LLM critics trained to review model-written code caught more bugs than paid human code reviewers and identified hundreds of errors in ChatGPT training data that had been rated "flawless"
