---
title: Prove the Pipeline on 2 Before 20
one_liner: Run the full pipeline on two items end-to-end before scaling to the full dataset.
dimensions: workflow-discipline, reliability
---

## What it is

Scaling a workflow before it has proven correct on a small sample multiplies errors, not productivity. When a pipeline is run on 20 items and fails on item 7, you have wasted the cost of items 1–6, must diagnose a failure in a partially-executed state, and may have produced partial outputs that are now inconsistent with each other. Running the full pipeline on 2 items first costs a fraction of the full run, proves the pipeline correct end-to-end before scaling, and makes any failure cheap to diagnose and cheap to retry. The "2 before 20" framing is concrete because teams reliably convince themselves that 5 is enough, that the first one passing means all will pass, or that they can diagnose failures at scale — they cannot, reliably.

## When to reach for it

- Any batch job, bulk processing pipeline, or dataset transformation: run 2 items completely before the full set.
- When deploying a new LLM call or agent step to production: run 2 real examples through the full path before enabling for all traffic.
- Before a long-running agentic task: run the task against the first 2 items in the work list, review all outputs, then proceed.
- When uncertain whether downstream consumers will handle the output format: prove format compatibility on 2 items before generating all outputs.
- After any change to a pipeline: re-prove on 2 items before re-running the full set.

## When NOT to

- When the pipeline is provably idempotent and has already been proven on small samples in a prior run that has not changed — don't re-prove what has already been established.
- When a single item fully exercises the pipeline and item-to-item variation is provably irrelevant to correctness — one is sufficient in those cases, not two.
- Truly trivial transformations with no external I/O, no branching logic, and no LLM call — but be skeptical of claims that a pipeline is truly trivial.

## Exemplars

- Anthropic's building-effective-agents guidance explicitly recommends starting with simple use cases and scaling only after proven reliability — proving on small samples is the operational expression of that principle.
- Every database migration script should be tested against a staging environment with representative data before running against production — the same principle, applied to schema changes.
- John Gall, *Systemantics* (1975) — https://personalmba.com/galls-law/ — classic antecedent (link is Josh Kaufman's Personal MBA summary; the 1975 book has no stable web home): Gall's Law holds that a complex system that works invariably evolved from a simple system that worked; proving a pipeline on two items before scaling is the operational form of this principle.
