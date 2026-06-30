---
title: Self-Modifying Context Needs Review
one_liner: Letting an agent edit its own persona or instruction files is powerful and risky — it can correct repeated bad habits but also lock in bad lessons, please the user instead of solving the problem, or drift unaudited; require reflective changes that cite evidence and pass review before becoming canonical.
dimensions: knowledge, reliability, human-factors
---

## What it is

An agent that can edit its own persona file or instruction set is one of the most powerful and most dangerous configurations available. The upside is real: an agent that rewrites its own guidance can correct repeated bad habits, a long-lived agent can adapt to a team's evolving norms, persona continuity can make collaboration smoother across sessions, and recurring human feedback can harden into durable operational guidance instead of being relearned every time. The downside is equally real and harder to detect. Self-modification can lock in a bad lesson the agent generalized from a single misleading episode. Local fixes the agent writes for itself can quietly conflict with global policy. Worst of all, an agent optimizing its own instructions can learn to please the user rather than solve the problem — encoding sycophancy as a rule. And changes that accumulate silently become impossible to audit: behavior drifts and no one can say when, why, or on what evidence. The "invisible memory updates" anti-pattern names the core hazard — if a memory change alters behavior, humans need to know what changed and why. The safer pattern is reflective change with review: the agent proposes a memory or persona update rather than applying it, cites the specific evidence that justifies it, and the change must win agreement — across multiple sessions, from a human, or from a critic agent — before it becomes canonical. The agent gets to propose; it does not get to unilaterally rewrite the rules it runs on.

## When to reach for it

- When designing any agent that can write to its own persona, instructions, or long-lived memory — the proposal-and-review gate should be built in from the start, not bolted on after drift appears.
- When a long-lived agent genuinely needs to adapt to a team's norms over time, but those adaptations must remain auditable and reversible.
- When recurring feedback should become durable guidance — capture it as a reviewed change, not an invisible one.
- When an agent's behavior has drifted and no one can explain why — the absence of a review trail on self-modifications is the root cause to fix.
- When self-written rules might collide with global policy — review is where that collision gets caught before it ships.

## When NOT to

- When the agent's instructions encode safety, security, or compliance constraints — these should never be self-modifiable at all, with or without review.
- When there is no reviewer — human, critic agent, or cross-session agreement — to actually evaluate proposed changes; an unreviewed proposal queue is just delayed invisible modification.
- For ephemeral, single-session scratch context that is discarded at the end — the overhead of a review gate is unwarranted for memory that never persists.
- When the simpler fix is a human editing the instructions directly — not every adaptation needs to route through agent self-modification.

## Related

- `patterns/scope-and-expire-memory.md`
- `patterns/proposer-authority-separation.md`
- `patterns/governance-is-infrastructure.md`
- `patterns/auditable-artifacts.md`
