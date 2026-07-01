---
title: Governance Is Infrastructure, Not a Document
one_liner: In agentic organizations governance can't be a policy doc that sits outside the workflow — it must be embedded in tools, prompts, validators, logs, and approval edges; the common substrate is an LLM proxy/gateway that logs usage, tracks cost, enforces policy, and provides observability.
dimensions: human-factors, observability, orchestration
---

## What it is

Governance written as a policy document that sits outside the workflow does not govern anything an agent does; by the time a human reads the policy, the agent has already acted. In an agentic organization governance has to be infrastructure — embedded into the tools agents call, the prompts that frame them, the validators that check their output, the logs that record what happened, and the approval edges that gate their high-stakes transitions — so that policy is enforced at the moment of action rather than reviewed after it. The concerns this infrastructure carries are broad and concrete: token budgets, audit logs, model and provider routing, data access scopes, production permissions, supply-chain risk, IP and licensing, compliance constraints, security policy, human approval thresholds, rollback authority, user privacy, and the provenance of generated work. The anti-pattern is treating governance as after-the-fact review — checking only at the end, when violations are already incidents — because policies that are not embedded in the workflow are not constraints, they are hopes. A handful of infrastructure patterns make embedded governance practical. The common substrate is an LLM proxy or gateway that every call routes through, which logs usage, tracks cost, enforces routing and access policy, and provides observability across the whole fleet — one chokepoint where governance is real rather than advisory. A workflow runner that records artifacts and approvals gives every consequential action an auditable trail and an enforceable approval edge. And a pattern library that standardizes safe operating moves turns governance from prohibition into a set of reusable defaults people reach for. Governance designed this way is invisible when it is working and load-bearing when it matters.

## When to reach for it

- When agents take consequential actions — spending tokens, touching production, accessing data, generating shippable work — and policy needs to bind at the moment of action, not in a review afterward.
- When you need an enforcement chokepoint — an LLM proxy or gateway every call passes through — to log usage, track cost, route models, and apply access policy uniformly.
- When audit, compliance, IP, or privacy requirements demand provenance and an audit trail for what agents did and who approved it — a workflow runner that records artifacts and approvals provides it.
- When high-stakes transitions need a real approval edge with rollback authority, rather than a documented expectation that someone will check.
- When the organization keeps rediscovering the same safe operating moves — a pattern library standardizes them as defaults instead of leaving each team to relearn the rules.

## When NOT to

- When the system is a sandboxed prototype with no access to production, data, or spend — heavyweight governance infrastructure adds friction with nothing yet to govern.
- When a lightweight inline check or guardrail covers the actual risk — do not stand up a gateway and a policy engine for a single reversible action.
- When governance infrastructure would become bureaucracy that people route around — embedded governance only works if it is the path of least resistance, not an obstacle to circumvent.
- When the policies themselves are unsettled — encoding governance into tools and validators before you know the rules just hardens the wrong constraints.

## Related

- `patterns/guardrails-and-escalation.md`
- `patterns/proposer-authority-separation.md`
- `patterns/emit-events.md`
- `patterns/self-modifying-context-needs-review.md`
