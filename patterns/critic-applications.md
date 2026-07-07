---
title: Critic Applications
one_liner: Build a deterministic tool — a binary, parser, validator, or CLI — that acts as law from the agent's perspective; it cannot be negotiated with, only satisfied, which compresses complex intent into a checkable affordance and compensates for model weakness.
dimensions: tool-design, verification, reliability
---

## What it is

A critic application is an external tool — a binary, parser, validator, or CLI — built specifically to act as law from the agent's perspective. The defining property is non-negotiability: a model can argue with a prompt, reinterpret an instruction, or talk itself into believing it satisfied a policy, but it cannot argue with a program that returns pass or fail. It must actually satisfy the program. This makes a critic application the most powerful available tool for compressing complex intent into a checkable affordance. Instead of asking a model to hold a long, intricate PDF-processing policy in its head and apply it consistently, you build a PDF utility that exposes exactly the affordances the policy requires and refuses everything else. Instead of asking a model to visually inspect a UI unaided — a known weakness — you give it object detection, screenshot comparison, accessibility checks, or browser automation that report ground truth. A critic application earns its keep by doing what models are bad at reliably: it can parse domain-specific artifacts, validate policy constraints, expose hidden state the model would otherwise have to guess at, compare before-and-after outputs, generate test fixtures, check invariants, score outputs against a rubric, and in general compensate for a specific model weakness with a deterministic mechanism. Crucially, a critic application is not a product for humans and need not be polished, discoverable, or pretty — it only needs to be useful to an agent and reliable enough to serve as a validator. The investment is in building the right unyielding surface, then letting the agent grind against it until it passes. The agent's job shifts from "convince me you're done" to "make the critic say yes," which is a far harder claim to fake. Where deterministic rails are about which steps in a workflow are model-driven and which are checked, a critic application is the check itself — the unyielding surface, built deliberately as a first-class artifact.

## When to reach for it

- When intent is complex enough that asking a model to remember and apply it reliably is the weak point — encode the policy in a tool the model must satisfy rather than recall.
- When the model has a known blind spot (visual inspection, precise parsing, numeric tolerances, format validation) — build a deterministic check that supplies ground truth where the model is unreliable.
- When you need verification that an agent cannot talk its way past — a program's pass/fail is far harder to hallucinate than a self-assessment.
- When the same class of correctness check recurs across many tasks — a reusable validator amortizes its build cost across every future run.
- When you need to expose hidden state (database contents, rendered output, runtime behavior) that the agent would otherwise have to infer — a tool that reports the real state removes the guesswork.
- When converting a recurring review finding into a permanent guardrail — turn the lesson into a check the agent must pass next time, not a note it might read.

## When NOT to

- When the judgment is genuinely subjective or open-ended (taste, tone, design quality) and no deterministic rule captures "correct" — forcing a brittle critic produces confident wrong verdicts.
- When the critic would be so expensive or complex to build that a cheaper check (a human glance, an existing test) gives equal assurance — proportion the tool to the risk.
- When the critic itself would become an unmaintained, drifting source of false pass/fail signals — an unreliable validator is worse than none because it launders bad work as verified.
- When the constraint changes faster than the tool can be kept correct — a stale critic enforces yesterday's policy.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends giving agents well-specified tools with carefully engineered definitions and verifying outputs against them
- Amplifier — https://github.com/microsoft/amplifier-bundle-superpowers — the superpowers verify mode requires evidence-based completion verification — run the verification command, read its output, then claim — treating the command as the authority rather than the agent's claim
- Chen et al., "Teaching Large Language Models to Self-Debug" (arXiv:2304.05128) — https://arxiv.org/abs/2304.05128 — classic antecedent: demonstrates that feeding execution results into the model's self-reflection loop ("rubber duck debugging") substantially improves code generation across benchmarks
- Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning" (arXiv:2303.11366) — https://arxiv.org/abs/2303.11366 — classic antecedent: external evaluation signals (test results) serve as the critic the agent iterates against, separate from the model's self-assessment

## Related

- `patterns/demand-independent-proof.md`
- `patterns/deterministic-rails.md`
- `patterns/video-driven-development.md`
- `patterns/test-what-not-how.md`
