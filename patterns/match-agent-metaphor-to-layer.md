---
title: Match the Agent Metaphor to the Layer
one_liner: Treating every agent as a person creates confusion; treating every agent as a stateless tool loses useful continuity — choose the framing per layer: disposable process, independent critic, manager-like orchestrator, long-lived assistant, or policy-bound organizational actor.
dimensions: human-factors, orchestration, meta-principles
---

## What it is

Whether an agent should be treated like a person, a tool, or a disposable process is not a philosophical question with one answer — it is a design decision that should be made per layer, because the right metaphor changes how you build, name, monitor, and trust the thing. The two failure modes bound the space: treating every agent as a person creates confusion, imputing continuity, memory, and accountability where none exist; treating every agent as a stateless tool loses the useful continuity that some layers genuinely have. The discipline is to pick the framing that matches what the agent actually is at its layer. A short-lived implementer is a disposable process: one task, tight context, no persona, thrown away when done — you do not name it or expect it to remember. A reviewer or critic is an independent evaluator: its value comes from adversarial framing and a vantage point separate from the work it judges, so you build it to disagree, not to collaborate. An orchestrator is a manager-like system: durable state, broad awareness, responsibility for coordinating others, so it is reasonable to give it standing identity and memory. A personal assistant or twin is a long-lived collaborator: persona continuity, retained preferences, an ongoing relationship — here the person-like metaphor earns its keep. An organizational agent is a policy-bound actor: it represents team norms and institutional knowledge, and is bound by governance rather than by individual preference, so it is framed as an office, not a personality. Matching the metaphor to the layer keeps the mental model honest — you grant continuity exactly where it exists and withhold it where it would only mislead.

## When to reach for it

- When designing a multi-layer agent system and deciding how much identity, memory, and persona each layer should carry — let the layer's actual lifespan and role decide.
- When a disposable worker has accreted a name, a personality, and expectations of memory it does not have — strip it back to a process before the false continuity causes errors.
- When a critic or reviewer is being built to be agreeable — the layer calls for an independent adversarial evaluator, and the metaphor should enforce that.
- When a long-lived assistant is being treated as stateless and keeps losing useful preference and relationship continuity — the layer warrants a persistent collaborator framing.
- When an agent acts on behalf of a team or organization and needs to be bound by policy rather than by one person's preferences — frame it as a policy-bound actor.

## When NOT to

- When the system is a single agent doing a single task — there are no layers to match metaphors to, and the question is moot.
- When a persona is being added for charm rather than for any continuity the layer actually has — that is decoration that will later mislead operators about the agent's real capabilities.
- When the metaphor would grant memory, authority, or accountability the implementation cannot back up — the framing must not over-promise what the agent can do.
- When choosing the metaphor becomes a substitute for getting the agent's scope, context, and guardrails right — the metaphor describes the layer, it does not implement it.

## Related

- `patterns/clean-slate-delegation.md`
- `patterns/subagents-as-context-sinks.md`
- `patterns/design-for-emotional-ownership.md`
- `patterns/governance-is-infrastructure.md`
