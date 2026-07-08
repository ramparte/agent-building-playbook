---
title: Separate the Proposer From the Authority
one_liner: The entity that proposes an action is the worst authority to approve it — route approval through a role with no stake in the proposal's acceptance.
dimensions: reliability, orchestration
---

## What it is

In agentic systems, the agent that proposes an action — "here is the plan," "here is the code," "here is the command to run" — is structurally biased toward approval. It has already reasoned toward the proposal, its context is anchored to it, and any self-review operates from the same assumptions that generated it. Separating the proposer from the authority means the entity with the power to approve and execute does not have a stake in the proposal: it could be a second agent, a deterministic validator, a human, or a gated pipeline stage. The authority's job is to assess whether the proposal is safe, correct, and aligned with intent — and it must be able to say no. Proposals that route back to the proposer for approval are not proposals; they are executions with extra steps.

## When to reach for it

- Before any irreversible action (file deletion, deployment, external API call, message send) — the proposer drafts, the authority approves.
- When an agent is designing and implementing in the same turn — split the roles: one agent designs, a separate agent reviews before the first agent builds.
- When debugging a pipeline that approves its own work and produces consistently wrong outputs — the missing separation is the structural cause.
- When implementing human-in-the-loop workflows: the human is the authority; the agent is the proposer. Make that explicit in the orchestration design.
- When compliance or accountability requirements apply: documented proposer-authority separation is the audit trail.

## When NOT to

- Trivially reversible, low-stakes actions where the cost of the approval step exceeds the recovery cost if the action is wrong — not every file write needs a separate approver.
- Fully automated pipelines with robust rollback and revert mechanisms where separation is impractical and recovery is reliable — apply proportionality.
- Exploratory, draft, or ephemeral work where nothing irreversible happens until a later gated step — defer separation to the gate, not to every intermediate step.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: advocates for human-in-the-loop controls at decision points, explicitly separating the generation of proposed actions from their authorization and execution
- Amplifier — https://github.com/microsoft/amplifier-bundle-recipes — recipe steps can declare requires_approval: true, pausing the workflow for explicit approval before execution proceeds — the proposing step and the approving authority separated in the orchestration format itself
- Saltzer & Schroeder, "The Protection of Information in Computer Systems" (1975) — https://www.cs.virginia.edu/~evans/cs551/saltzer/ — classic antecedent: the "separation of privilege" design principle holds that a protection mechanism requiring two independent parties to unlock an action is more robust than one requiring only a single key; no single accident, deception, or breach of trust can then compromise the protected resource
