---
title: Add Autonomy Only When Justified
one_liner: Every degree of autonomy you give an agent must be paid for with oversight proportional to the risk — add it only when the cost-benefit calculation is explicit and positive.
dimensions: orchestration
---

## What it is

Autonomy in agentic systems is not free. Every capability you give an agent to act without human review creates a surface for unreviewed mistakes. Every loop you add that lets the agent retry on its own initiative creates a surface for runaway behavior. Every permission you grant to call external APIs or modify state without confirmation creates a surface for irreversible errors. Autonomy is a cost that must be paid for with trust earned through verified behavior, proportionate oversight, and reversible actions wherever possible. The correct posture is: assume no autonomy by default, and add it incrementally when the benefit is demonstrated and the risk is managed. "Demonstrated" means the agent has shown reliable behavior on the task type in question, not that the designer believes it should be reliable. "Risk managed" means either that the actions taken autonomously are reversible, or that oversight mechanisms are in place that would catch errors before they compound. The most common failure mode is granting autonomy because it is technically possible, because it seems efficient, or because the task type looks routine. Routine tasks fail in non-routine ways; it is exactly the cases the designer did not anticipate that autonomous behavior is most likely to go wrong.

## When to reach for it

- When a task type has demonstrated reliable behavior across a large sample of similar inputs and the failure modes are well-characterized and reversible — that is the justified case for autonomous handling.
- When the task is high-frequency, low-variance, and the human review cost exceeds the expected error cost — the math favors autonomy, but only after the variance has been measured, not assumed.
- When every action the autonomous agent would take can be reversed within a short window — reversibility converts an irreversible mistake into a recoverable one, dramatically reducing the cost of a wrong call.

## When NOT to

- When the task involves actions that cannot be undone: sending communications, deleting data without a trash/recovery path, making financial commitments, or modifying production systems without a rollback plan — these require human confirmation regardless of how routine the task appears.
- When the agent's reliability on the task type has not been verified empirically — "it should work" is not a justification for removing oversight.
- When the task involves personal data, sensitive information, or compliance-sensitive domains — the risk surface is higher and the justification bar for autonomy should be correspondingly higher.
- When the system is new or recently modified — autonomy should be reduced when reliability assumptions have not been re-validated after changes.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends that agents minimize their footprint (request only necessary permissions, prefer reversible actions, confirm with users when scope is unclear) as a default posture; autonomy beyond this requires explicit justification
- Amplifier — https://github.com/microsoft/amplifier — the recipe system's approval gate primitive (staging) provides the mechanism for adding human checkpoints before autonomous execution proceeds; autonomy is opt-in at each stage boundary
- Feng, McDonald & Zhang, "Levels of Autonomy for AI Agents" (arXiv:2506.12469) — https://arxiv.org/abs/2506.12469 — formalizes: proposes five escalating autonomy levels characterized by the user's role (operator → collaborator → consultant → approver → observer); treats autonomy as a deliberate design decision separate from capability, providing a structured vocabulary for "how much autonomy is justified here"

## Related

- `patterns/guardrails-and-escalation.md`
- `patterns/start-least-agentic.md`
- `patterns/gate-the-phases.md`
- `patterns/reliability-before-features.md`
