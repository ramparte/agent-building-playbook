---
title: Adversarial Parallel Review
one_liner: Run several reviewers with different models or roles and little shared context, reward significant findings over volume, then have a meta-reviewer rank what matters — because an implementer shares the blind spots that produced its own bugs.
dimensions: verification, reliability, orchestration
---

## What it is

The model that wrote the code is the worst reviewer of it, because it reviews from the same assumptions that produced the bug — the blind spot that created the error also hides it. Adversarial parallel review breaks that correlation by running several reviewers at once, each given different model families or different roles, each with little or no prior context about how the code came to be. "Fresh eyes" here is literal: a separate model that did not author the work and does not carry its rationalizations. The reviewers are scored on significant findings, not volume — a reviewer rewarded for quantity learns to manufacture nitpicks, so the incentive must point at impact. Because independent reviewers will surface overlapping, conflicting, and unequal critiques, a meta-reviewer reads all of them, compares, and ranks which findings actually matter, discarding noise and elevating the few that change the outcome. The ranked, actionable critique routes back to implementation, the fix is made, and the result is re-reviewed by a fresh reviewer rather than the one who already engaged with it. The whole structure exists to manufacture genuine independence — different models, different roles, separated context, impact-weighted scoring — because shared context is exactly what lets a bug survive its own review.

## When to reach for it

- When the cost of missing a bug is high — security-sensitive code, irreversible actions, anything expensive to get wrong in production.
- When failures are subtle and high-impact rather than obvious — the class of error a single reviewer sharing the author's mental model will miss.
- When the implementing model also did its own review and "found nothing" — that is the signal to bring in independent reviewers, not reassurance.
- When one reviewer's verdict is not trustworthy enough to act on alone — multiple independent critiques plus a meta-reviewer give you a ranked, defensible result.
- When you can afford the extra model calls and the latency of a fan-out-then-rank step at a checkpoint.

## When NOT to

- For low-stakes or easily reversible work where a single reviewer, or a deterministic check, is sufficient and parallel review is pure overhead.
- In tight interactive loops where the latency and token cost of multiple reviewers plus a meta-reviewer exceed the acceptable feedback cycle.
- When the reviewers are not actually independent — same model, same context, same prompt produces correlated critiques and a false sense of coverage.
- When a deterministic verifier already settles the question — run the test or the linter instead of convening a review squad to judge a checkable fact.

## Exemplars

- Irving, Christiano & Amodei, "AI safety via debate" (arXiv:1805.00899) — https://arxiv.org/abs/1805.00899 — classic antecedent: establishes adversarial debate between two AI agents before a human judge as a mechanism for surfacing errors a single reviewer shares with the author, founding the adversarial critique structure this pattern inherits
- McAleese et al. (OpenAI), "LLM Critics Help Catch LLM Bugs" (arXiv:2407.00215) — https://arxiv.org/abs/2407.00215 — empirical support: on code with naturally occurring LLM errors, critiques written by a trained LLM critic were preferred over human critiques in 63% of cases, and the critics caught more bugs than paid human code reviewers — independent machine critique of machine output as a validated reliability layer
- 2389 Research, simmer — https://github.com/2389-research/simmer — first-party: multi-round artifact refinement where a panel of judges reads the artifact, scores it per criterion, and distills the round's findings into the single highest-leverage fix for the generator to apply — the critique, fix, re-review loop packaged as a plugin

## Related

- `patterns/auditor-agent.md`
- `patterns/match-model-to-stage.md`
- `patterns/deterministic-rails.md`
- `patterns/shape-work-as-an-attractor.md`
