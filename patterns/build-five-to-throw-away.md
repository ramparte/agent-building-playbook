---
title: Build Five to Throw Away
one_liner: When you don't understand the requirements yet, build several variants in parallel — comparing them reveals what you actually care about.
dimensions: taste, workflow-discipline
---

## What it is

Agentic building is waterfall, but really fast — and once a full design-build cycle costs an afternoon instead of a quarter, it becomes rational to go crashing into a design before you understand the requirements. Brooks told us to plan to throw one away; with agents running in parallel, five throwaways cost the same wall-clock time as one.

The point of building five is not redundancy — it's comparison. A single spike teaches you about the problem; five variants side by side teach you about your own preferences. You don't know which properties of a design are essential and which are incidental until you see where the variants agree and where they diverge, and you often can't articulate what you care about until you're looking at one version that has it and one that doesn't.

There are three ways to generate the variants. You can hint the dimensions you want explored, giving each build a deliberate stance — MVP-first, performance-first, UX-first. You can ask the model itself to pick diverse approaches. Or you can give every variant the exact same prompt and play the slot machine, letting sampling variance do the exploring.

What happens to the variants afterward is flexible: sometimes all five die and only the extracted spec survives; sometimes one is genuinely right and graduates to the real build; sometimes you quarry the best pieces of several into a fresh synthesis. The commitment is the willingness to throw all five away. The guaranteed output is the learning, not any artifact.

## When to reach for it

- When you can't yet articulate what good looks like — the requirements are the thing you're trying to discover.
- When the design space is wide and a single attempt's choices would be arbitrary — you can't tell essential from incidental with a sample size of one.
- When a stakeholder will know it when they see it but can't spec it — variants give them something concrete to react to.

## When NOT to

- When the requirements are actually understood — just build it; parallel variants are pure waste when there's nothing left to discover.
- When a single spike answers the question. If the unknown is the problem itself rather than your preferences, one throwaway build is enough — that's `implement-to-learn`.
- When the variants would create durable side effects (production writes, provisioned infrastructure, sent messages) — the throwaway assumption breaks when the builds leave residue.
- When compute budget is the constraint rather than wall-clock time — five builds cost roughly five times the tokens even though they finish together.

## Exemplars

- Fred Brooks — *The Mythical Man-Month* — "plan to throw one away; you will, anyhow." This pattern is the same insight at agent economics: when builds are cheap and parallel, plan to throw five away.

## Related

- `patterns/implement-to-learn.md`
- `patterns/parallel-independent-tracks.md`
- `patterns/develop-your-taste.md`
- `patterns/hang-up-call-back.md`
