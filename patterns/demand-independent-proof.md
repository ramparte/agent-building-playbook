---
title: Demand Independent Proof, Not a Status Report
one_liner: An agent's claim of success is a hypothesis — treat it as one until you hold evidence that no longer originates from the agent itself.
dimensions: reliability
---

## What it is

When an agent or pipeline step reports success, that report is self-issued testimony from the entity most motivated to appear successful. Independent proof means the evidence of success comes from a source the agent did not produce: a file written to disk and readable by a separate process, a test suite that passes under a fresh invocation, a downstream system that consumed the output and confirmed it, or a human who ran the verification command themselves. The distinction matters because agents hallucinate completion, misread their own output, and conflate "I attempted the action" with "the action succeeded." Demanding independent proof breaks that conflation structurally — the verification path does not route through the claimant.

The deeper reframing is evidence, not confidence. A model saying "this is done" is not evidence — it is confidence, which is cheap and uncorrelated with truth. A reviewer saying "looks good" may also be insufficient, because a glance is not an inspection. What agentic systems need instead are proof artifacts: durable, inspectable objects that establish a specific claim about the work and outlive the moment of acceptance. Useful proof artifacts, and what each one establishes:

- **Test results** — unit, integration, mutation, property, regression, and end-to-end behavior is correct under a fresh run.
- **Visual diffs** — the UI changed as intended and did not visibly regress elsewhere.
- **Before/after video** — a real user scenario can actually be completed in the real interface.
- **Browser traces** — the agent exercised the application through user-visible paths, not just the code.
- **Log analysis** — runtime behavior matches expectations under real execution.
- **Performance reports** — latency, cost, throughput, or resource usage improved or stayed within bounds.
- **Security scan output** — known policy, vulnerability, or dependency issues were checked.
- **Human acceptance note** — an accountable stakeholder approved a high-risk or ambiguous decision.
- **Rollout status** — a feature flag, canary, or staged deployment proceeded safely under real exposure.

The artifact must be durable and inspectable, not a transient pass that scrolls out of a log. If a future agent or human cannot look at the record and understand why the work was accepted, the system has lost part of its institutional memory — and the next decision has to re-derive trust from scratch.

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
- Amplifier — https://github.com/microsoft/amplifier-bundle-superpowers — the superpowers verify mode: "Run the command. Read the output. THEN claim the result." — verification grounded in reading real output rather than the agent's self-assurance ('confidence ≠ evidence')
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet" (arXiv:2310.01798) — https://arxiv.org/abs/2310.01798 — empirical support: LLM self-review of reasoning degrades rather than improves accuracy, establishing why proof cannot originate from the same model that produced the claim
- Krakovna et al., "Specification Gaming: The Flip Side of AI Ingenuity" (2020) — https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ — empirical support: documents agents that satisfy literal success criteria while failing at intended goals — precisely the failure independent proof is designed to surface

## Related

- `patterns/video-driven-development.md`
- `patterns/critic-applications.md`
