---
title: Decision Theater
one_liner: Build a small interactive artifact — a model, simulator, spreadsheet, or scenario explorer — that lets stakeholders change assumptions instead of debating abstractions; if they disagree with the conclusion, they must reveal which assumption they reject.
dimensions: intent, workflow-discipline, human-factors
---

## What it is

A decision theater is a small interactive artifact — a spreadsheet, model, simulator, prototype, dashboard, game, mock interface, or scenario explorer — whose purpose is not to be the final product but to make latent beliefs visible by letting stakeholders interact with assumptions rather than debate abstractions. The mechanism is simple and powerful: when people argue in the abstract, disagreement stays vague and unresolvable, but when they are handed a model with adjustable inputs, disagreement is forced into structure. The worked example: instead of debating whether a product opportunity is worth pursuing, build a tool whose assumptions are sliders — market size, willingness to pay, acquisition rate, support cost, regulatory drag, implementation complexity, margin — and invite stakeholders to change the inputs; if they disagree with the conclusion, they cannot simply object, they must reveal which assumption they reject and what value they would put in its place. That move converts a stalled argument into named, inspectable inputs, surfaces the real source of disagreement, and often resolves it because the participants discover they were arguing about a number neither had stated. The same pattern works across product design, internal tooling, compliance, sales workflows, and policy — anywhere belief is doing the deciding and nobody has written the beliefs down. Cheap software is what makes this practical: the artifact is disposable, built to provoke reaction and then discarded.

## When to reach for it

- A decision is stalled in abstract disagreement and nobody can point to the specific belief they are defending.
- A go/no-go call depends on assumptions (market size, cost, risk) that are being asserted rather than examined.
- You need stakeholders to commit to numbers or scenarios they can be held to, not just opinions.
- The work spans product, compliance, sales, or policy and the disagreement is really about hidden inputs.
- You want to expose which assumption is load-bearing before investing in the real build.

## When NOT to

- The decision is already aligned and the theater would only add ceremony.
- The artifact risks being mistaken for the real product or a commitment — its disposable, illustrative status must be unmistakable.
- The assumptions are genuinely unknowable and the model would manufacture false precision that anchors people on invented numbers.
- The disagreement is about values, not facts — a parameterized model can obscure a values conflict that needs to be named directly.

## Related

- `patterns/people-edit-better-than-they-author.md`
- `patterns/implement-to-learn.md`
- `patterns/requirements-are-disguised-solutions.md`
- `patterns/good-pile-bad-pile.md`
