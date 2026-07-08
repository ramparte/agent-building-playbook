---
title: Simulated Review Squad
one_liner: Before work reaches real users, run it past a panel of simulated perspectives — expert and novice users, compliance, support, executive sponsor, skeptical engineer, accessibility, security — built from real transcripts and tickets, to surface objections early and cheaply.
dimensions: intent, verification, reliability
---

## What it is

A simulated review squad is a panel of distinct perspectives — expert user, novice user, compliance reviewer, support operator, executive sponsor, skeptical engineer, accessibility reviewer, security reviewer, and whatever domain-specific personas the work demands — run against an artifact before it reaches real people. The goal is explicitly not to pretend these simulations are perfect substitutes for the humans they stand in for; it is to produce the objections those humans would raise earlier and far more cheaply than a real review cycle, so that the obvious problems are caught before work ever reaches a live user. Each persona reads the artifact through its own concerns: the novice trips on the thing the expert never notices, the compliance reviewer flags the step that creates exposure, the support operator predicts the ticket it will generate, the skeptical engineer questions the assumption nobody stated. The weak version invents these personas from imagination; the strong version builds them from real material — transcripts, support tickets, sales calls, shadowing sessions, and domain documents — so the simulated reactions are grounded in how the actual constituencies actually behave. This is distinct from a technical code audit: an auditor checks an artifact against a specification, while a review squad stages multi-stakeholder reaction, surfacing the human objections that no spec encodes.

## When to reach for it

- Work is about to reach real users and a full review cycle with every constituency would be slow or expensive.
- The artifact touches many stakeholders (compliance, support, accessibility, security) whose objections you want surfaced before, not after, launch.
- You have real material — transcripts, tickets, calls — to ground the personas in actual behavior rather than imagination.
- Early, cheap objections are worth more than late, authoritative ones for this stage of the work.
- You want to catch the obvious cross-perspective failures before spending a real reviewer's attention.

## When NOT to

- The decision genuinely requires a real human's authority or accountability (a legal sign-off, a regulatory approval) — a simulation cannot stand in.
- The personas would be pure invention with no grounding material, producing confident objections that misrepresent the real constituencies.
- The task is a technical correctness check against a spec — use an auditor agent, not a stakeholder panel.
- Treating squad approval as a substitute for ever talking to real users — it is a filter for cheap objections, not a release gate.

## Exemplars

- Li et al., "CAMEL: Communicative Agents for 'Mind' Exploration of Large Language Model Society" (arXiv:2303.17760) — https://arxiv.org/abs/2303.17760 — NeurIPS 2023; early work on sustaining distinct LLM personas through extended cooperative tasks via role-playing and inception prompting; a direct technical antecedent of multi-persona review.
- Qian et al., "ChatDev: Communicative Agents for Software Development" (arXiv:2307.07924) — https://arxiv.org/abs/2307.07924 — assigns specialized agent roles across the design, coding, and testing phases of a software lifecycle; demonstrates role-grounded multi-agent review in a production workflow context.
- Hong et al., "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework" (arXiv:2308.00352) — https://arxiv.org/abs/2308.00352 — encodes Standardized Operating Procedures into a panel of agents (product manager, architect, engineer, QA), each generating role-appropriate artifacts; shows how grounding simulated reviewers in domain process knowledge increases output quality.
- 2389 Research, review-squad — https://github.com/2389-research/review-squad — first-party: dispatches parallel review panels before launch — expert auditors (security, performance, SEO, accessibility), first-time visitors "across a sophistication spectrum", task-oriented regulars verifying real flows, and pedantic nitpickers — the expert-and-novice persona panel packaged as an installable plugin.

## Related

- `patterns/auditor-agent.md`
- `patterns/adversarial-parallel-review.md`
- `patterns/good-pile-bad-pile.md`
- `patterns/shadow-then-transform.md`
