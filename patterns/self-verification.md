---
title: Give Agents the Ability to Verify Their Own Work
one_liner: An agent that can detect its own errors is orders of magnitude more reliable than one that can only produce output — build verification into the agent before shipping it.
dimensions: verification, reliability
---

## What it is

An agent without verification capability is a single-pass system: it produces output and stops, with no way to detect that the output is wrong before delivering it. An agent with self-verification capability runs its output through a verification step before reporting completion — checking the result against the specification, running a test, reading back a file it wrote, or invoking a secondary check that doesn't share the agent's assumptions. Self-verification does not require a separate agent or a human in the loop, though either can be added. At minimum it means the agent's workflow includes an explicit verification step between "I performed the action" and "I report success." The verification step must have access to ground truth or an independent check — asking the same model to confirm its own reasoning is not verification, it is repetition. Verification that catches errors requires a different information source: the actual output artifact on disk, a test suite that runs the code, a downstream system that consumes the output, or a comparison against a known-correct reference.

## When to reach for it

- Any agent that writes files, modifies state, or calls external APIs — after the action, read back the artifact or check the state to confirm the action had the intended effect before reporting success.
- Any agent that generates structured output (code, JSON, configurations) — run the output through a parser, linter, or validator before delivery to catch formatting errors the agent cannot see in its own text.
- Any multi-step agent where later steps depend on earlier results — verify each step's output before the next step consumes it. A compounding error is far more expensive than a caught error.
- When the downstream cost of a wrong output is high — calibrate the intensity of verification to the consequence of failure. Irreversible actions require stronger verification than reversible ones.
- When designing a new agent from scratch — design the verification step at the same time as the action step. Adding verification after the fact is harder and often reveals that the action step produced no verifiable artifact.

## When NOT to

- When the output is immediately visible to the user in the same turn and the user will review it before acting on it — the user is the verifier in that case.
- When the verification step would cost more than catching and correcting errors after the fact — apply proportionality; not every text generation needs a formal verification pass.
- When the only available verification is asking the same model the same question in a different phrasing — this is not verification, it is repetition with added latency. If no independent check is available, flag the limitation rather than performing verification theater.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: the evaluator pattern is a first-class agentic primitive — an LLM or programmatic check that inspects the generator's output and provides feedback before the result is accepted
- Amplifier — https://github.com/microsoft/amplifier — the verification-before-completion skill: requires running verification commands and reading their output before any completion claim is made — the agent self-verifies rather than claiming success based on having performed the action

## Related

- `patterns/demand-independent-proof.md`
- `patterns/verify-independently.md`
- `patterns/evidence-before-assertions.md`
- `patterns/fail-loud-over-fallbacks.md`
