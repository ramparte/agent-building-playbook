---
title: Demand Independent Proof, Not a Status Report
one_liner: An agent's claim of success is a hypothesis — treat it as one until you hold evidence that no longer originates from the agent itself.
dimensions: reliability
---

## What it is

When an agent or pipeline step reports success, that report is self-issued testimony from the entity most motivated to appear successful. Independent proof means the evidence of success comes from a source the agent did not produce: a file written to disk and readable by a separate process, a test suite that passes under a fresh invocation, a downstream system that consumed the output and confirmed it, or a human who ran the verification command themselves. The distinction matters because agents hallucinate completion, misread their own output, and conflate "I attempted the action" with "the action succeeded." Demanding independent proof breaks that conflation structurally — the verification path does not route through the claimant.

## When to reach for it

- After any agent step whose output is used as input to a subsequent step — verify the output independently before the next step consumes it.
- Whenever an agent says "done," "complete," "success," or equivalent — ask what artifact was produced and inspect it yourself or via a separate process.
- When debugging pipelines that report high success rates but produce wrong downstream results — the self-reports are the problem.
- When designing agentic workflows: specify the independent verification point at design time, not as a post-hoc addition.
- Any time an irreversible action (deployment, send, delete) is about to be taken based on an agent's assurance.

## When NOT to

- Trivial, deterministic operations whose output is immediately visible in the same context and inspectable by the orchestrator without re-routing through the agent (e.g., an LLM returning a string you can read on screen in the same turn).
- Operations with robust end-to-end integration tests that already independently verify the result — additional independent proof checks are redundant.
- When the cost of independent verification exceeds the cost of the potential failure, and the failure is recoverable — apply proportionality.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends external verification of agent outputs and human-in-the-loop checkpoints as the primary mechanism for catching false success reports
- Amplifier — https://github.com/microsoft/amplifier — the verification-before-completion skill: explicitly prohibits success claims without running and reading the output of a verification command in the current session
