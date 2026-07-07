---
title: Ablate the Harness as Models Improve
one_liner: Periodically have a stronger model inspect your workflow and delete steps that are no longer needed, shorten prompts, and merge nodes — because model capability changes faster than workflow habits, and yesterday's scaffolding becomes today's tax.
dimensions: workflow-discipline, meta-principles, cost-routing
---

## What it is

Every scaffolding step in a workflow was added to compensate for something a model could not yet do reliably: a verbose prompt to prevent a known mistake, an extra review node to catch a class of error, an approval gate to guard a fragile step, a decomposition to keep a task inside the model's reach. But model capability moves faster than workflow habits, so the compensations outlive the deficiencies they were built for, and yesterday's load-bearing scaffolding silently becomes today's tax — extra tokens, extra latency, extra surface to maintain, and extra places for the workflow to drift. The self-ablating harness is the discipline of periodically asking a stronger model to inspect the workflow and identify what is no longer earning its place: steps that can be deleted, prompts that can be shortened, nodes that can be combined. You then run the ablation as an experiment — remove the node, shorten the prompt, swap in a cheaper model, drop the approval gate — and compare output quality against the unablated version. If quality holds, the scaffolding was tax and you keep it deleted; if it drops, you have just re-justified the step empirically. The graph is a living system to be pruned, not a shrine to be preserved.

## When to reach for it

- On a cadence, not just when something breaks — schedule ablation passes the way you schedule dependency upgrades.
- Right after a model upgrade: the new model likely no longer needs scaffolding the old one required.
- When a workflow has accreted nodes and prompt text over many incremental changes — the aggregate is almost certainly carrying dead weight.
- When per-run cost or latency creeps up without a matching gain in quality — ablate to find the steps no longer paying for themselves.
- When a prompt has grown into a wall of defensive instructions — many of its clauses are guarding against mistakes the current model no longer makes.

## When NOT to

- Without a quality comparison — deleting nodes by intuition and shipping is how you discover, in production, that the step was load-bearing.
- For steps whose value is compliance, audit, or accountability rather than capability — those gates exist for reasons that model improvement does not retire.
- In the middle of high-stakes delivery — ablate against a baseline in a safe context, not on the run you cannot afford to get wrong.
- When you cannot roll back — only ablate what you can restore if quality drops.

## Exemplars

- Huang and Sun, "Does the Harness Matter? Lessons from ALE-Claw on Agents' Last Exam" (2025) — https://agents-last-exam.org/blogs/harness-matters — empirical support: stripping a product-layer harness to its minimal form maintained accuracy while cutting 44% of input tokens and 41% of cost; the authors observe that "much of today's scaffolding exists to compensate for current model limitations," directly motivating scheduled ablation passes.
- Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses" (arXiv:2604.25850) — https://arxiv.org/abs/2604.25850 — empirical support: closed-loop system that evolves harness components over iterations via component, experience, and decision observability, demonstrating that harnesses are living artifacts to be pruned rather than fixed structures to preserve.

## Related

- `patterns/invest-the-expensive-model-in-the-harness.md`
- `patterns/rebuild-often.md`
- `patterns/match-topology-to-the-work.md`
- `patterns/match-model-to-stage.md`
