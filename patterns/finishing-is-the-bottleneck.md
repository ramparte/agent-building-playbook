---
title: Finishing Is the Bottleneck, Not Starting
one_liner: Models make starting easy — a plausible 80% appears fast — but plausible work is not finished work, and the final 20% consumes most of the attention and risk; the real metric is convergence — work that reliably reaches an accepted, shipped, observed state.
dimensions: workflow-discipline, reliability, meta-principles
---

## What it is

The economics of agentic work have inverted: starting has become nearly free while finishing remains expensive. A model can produce a plausible 80% solution — code, a demo, a document, a prototype — in minutes, and the very speed of that production is the trap, because plausible work and finished work are not the same thing. Finished work has passed tests, survived independent review, produced evidence, handled edge cases, met user expectations, complied with constraints, shipped safely, and generated feedback that can be acted on. The final 20% — the part the model makes look almost-done — is where most of the attention, risk, and organizational cost actually live. Worse, agentic systems generate unfinished work faster than humans can inspect it, so without a finishing discipline the organization silently accumulates demos, branches, prototypes, unmerged code, half-fixed bugs, shallow tests, and "almost done" artifacts that look like progress and are really debt. The bottleneck is therefore not code generation. It is convergence: the property that work reliably reaches an accepted state — implemented, reviewed, tested, documented, deployed, observed, and incorporated into the product or organization. A demo is the most seductive false signal here, because a demo shows possibility, not readiness; treating "it demoed" as "it is done" is the canonical way teams mistake an 80% artifact for a finished one. The right metric for an agentic system is not how much it can start but how reliably it can converge.

## When to reach for it

- When evaluating an agentic workflow's value: measure convergence (percentage of started work that reaches an accepted, shipped, observed state), not throughput of generated artifacts.
- When a team feels productive but nothing is shipping — the symptom of a starting-rich, finishing-poor pipeline is a backlog of impressive, unmerged, "almost done" work.
- When deciding where to invest engineering effort in a harness: the finishing stages (validation, review, evidence, deployment, feedback) usually deserve more investment than generation.
- When someone proposes shipping on the strength of a demo — pause and ask what would have to be true for this to be finished, not just shown.
- When the volume of agent output has outgrown human inspection capacity — that is the signal that you need finishing discipline encoded into the workflow, not more reviewers.

## When NOT to

- For genuinely throwaway exploration — spikes, sketches, and one-day prototypes that will be discarded — where reaching an accepted state was never the goal.
- When the work product genuinely is the start (a brainstorm, an options memo, a research scan) and no convergence is expected downstream.
- When forcing premature finishing discipline onto an exploratory phase would kill the cheap iteration that exploration depends on — converge once the problem is understood, not before.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: emphasizes measuring task completion and verified outcomes over the appearance of progress, the operational core of treating convergence as the metric
- Eliyahu M. Goldratt, *The Goal* (1984) — https://en.wikipedia.org/wiki/Theory_of_constraints — classic antecedent: introduces the principle that system throughput is determined by its slowest constraint; optimizing non-bottleneck stations produces no improvement in overall output
- DORA — https://dora.dev/guides/dora-metrics-four-keys/ — empirical support: defines lead time for changes (commit to production) and deployment frequency as concrete throughput metrics for delivery velocity

## Related

- `patterns/work-backward-from-the-shipping-dock.md`
- `patterns/demand-independent-proof.md`
- `patterns/video-driven-development.md`
- `patterns/production-feedback-loop.md`
