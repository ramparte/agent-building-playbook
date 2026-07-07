---
title: Work Backward From the Shipping Dock
one_liner: Start from where work becomes real — production, approval, operator adoption, user comprehension — and ask what proof would convince you it's ready; the proof system then shapes the workflow, instead of asking "can the model build this?"
dimensions: workflow-discipline, verification, reliability
---

## What it is

Most teams design an agentic workflow forward — from the idea toward the model — and ask "can the model build this?" The more reliable move is to design it backward, starting from the shipping dock: the place where work actually becomes real. That place differs by domain — for software it may be production deployment; for a regulated domain, regulatory approval; for an internal tool, adoption by operators; for design work, user comprehension; for infrastructure, stable operation under load — but in every case it is a concrete acceptance boundary, not the moment of generation. Working backward from that boundary means asking a specific battery of questions before any code is written: What evidence would prove this works? Who must accept it? What tests should fail if it is wrong? What logs or telemetry must be visible? What rollback path exists? What user scenarios must be demonstrated? What compliance or security conditions apply? What feedback loop begins after release? The answers are not documentation — they become the structure of the workflow itself: graph nodes, validators, acceptance criteria, and escalation rules. The decisive consequence is sequencing. If the system does not know what proof is required before it starts, it will invent proof after the fact — retrofitting acceptance criteria to whatever it happened to produce, which is no proof at all. Defining the dock first turns "done" from a judgment call at the end into a contract specified at the beginning.

## When to reach for it

- When designing a new agentic workflow — define the shipping dock and its acceptance evidence first, then build the generation steps to satisfy it.
- When "done" is contested or keeps slipping — the cure is to make the acceptance boundary and its required proof explicit and agreed before work starts.
- When the domain has a hard external gate (regulatory approval, security sign-off, an operator who must adopt the tool) — work backward from that gate's actual requirements, not from an imagined one.
- When converting acceptance criteria into machine-checkable form — each backward question maps to a validator, a test that should fail, a telemetry requirement, or an escalation rule.
- When a workflow keeps producing work that gets rejected late — late rejection usually means the dock's requirements were discovered too late; surface them at design time.

## When NOT to

- During genuine open-ended exploration where the destination is unknown — you cannot work backward from a dock you have not yet found.
- When the acceptance boundary is truly trivial and self-evident (a one-line internal script with no stakeholders) — full backward analysis is overhead with no payoff.
- When over-specifying the dock would lock in the wrong target — if the real acceptance criteria are still being learned, fix them before encoding them rigidly.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends defining success criteria and verification before building the agent loop, the design-from-acceptance-backward stance applied to agents
- Colin Bryar and Bill Carr, *Working Backwards* (2021) — https://workingbackwards.com/concepts/working-backwards-pr-faq-process/ — classic antecedent: Amazon's PR/FAQ method requires writing a customer-facing press release before any development begins, forcing teams to define the acceptance boundary first; the management precursor to designing agentic workflows backward from their shipping dock.

## Related

- `patterns/finishing-is-the-bottleneck.md`
- `patterns/demand-independent-proof.md`
- `patterns/separate-merge-from-exposure.md`
- `patterns/guardrails-and-escalation.md`
