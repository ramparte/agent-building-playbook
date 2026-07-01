---
title: Separate Merge From Exposure
one_liner: Feature flags are one of the most important controls for agent-generated work because they separate merging code from exposing it — default risky changes to staged exposure with explicit rollout criteria and automated rollback, so merge no longer means everyone is affected.
dimensions: reliability, workflow-discipline, orchestration
---

## What it is

The reason feature flags are one of the most important controls for deploying agent-generated work is structural: they break the assumption that merging code is the same act as exposing it to users. Without flags, those two events are fused — the moment an agent's change lands on the main branch and deploys, every user is affected, and the blast radius of a mistake is the entire user base at once. With flags, merge and exposure are decoupled, which lets the system default risky agent-generated changes to staged exposure rather than all-at-once release. Staged exposure is a graduated dial: internal-only rollout, then a dogfood cohort, then a canary group, then a percentage rollout, then customer opt-in — each step expanding the population only after the previous one held. Bound to that dial are two more controls that turn a flag from a switch into a safety system: automated rollback triggers that pull exposure back when error rates, latency, or other signals breach a threshold, and a feedback channel bound to the feature so the people newly exposed to it have a direct path to report what breaks. An agent can help manage this rollout — turning the dial, watching the signals, proposing the next step — but the rollout criteria themselves must be explicit and human-owned: what cohort is next, what signal advances or reverts exposure, what threshold trips rollback. The agent operates the staged release; it does not get to decide on its own that the change is safe for everyone. The result is that "the agent's change merged" stops meaning "everyone is now affected," which is precisely the property that makes agent-generated work safe to ship at volume.

## When to reach for it

- When deploying any agent-generated change whose failure would affect real users — default it to staged exposure rather than fusing merge with full release.
- When the volume of agent-generated changes has outgrown the team's ability to deeply review each one before release — flags let merged-but-unexposed code accumulate safely behind explicit gates.
- When you want an agent to help operate a rollout — let it turn the dial and watch the signals, but pin the advancement and rollback criteria as explicit, human-owned rules.
- When a change is plausibly correct but not yet proven in production — internal, dogfood, and canary stages buy real-world evidence at bounded blast radius.
- When you need a fast, automatic way to undo a bad change — bind automated rollback triggers to the flag so reverting exposure does not wait on a human noticing.

## When NOT to

- When the change is genuinely trivial and low-risk, and the flag's own complexity (the branch, the cleanup, the stale-flag debt) exceeds the risk it mitigates.
- When the infrastructure cannot actually support per-cohort exposure or reliable rollback — a flag that cannot really stage or revert is false reassurance.
- When flags are created but never retired — accumulated stale flags become their own source of confusing, untested code paths; pair every flag with a removal plan.
- When the rollout criteria are left implicit or delegated wholesale to the agent — an unsupervised agent advancing its own exposure defeats the control.

## Exemplars

- Martin Fowler / Pete Hodgson — https://martinfowler.com/articles/feature-toggles.html — the canonical treatment of feature toggles, including the separation of deployment from release and the lifecycle cost of stale flags
- DORA / Accelerate — https://dora.dev — research linking small batches and staged, reversible exposure to lower change-failure rates and faster recovery

## Related

- `patterns/production-feedback-loop.md`
- `patterns/guardrails-and-escalation.md`
- `patterns/work-backward-from-the-shipping-dock.md`
