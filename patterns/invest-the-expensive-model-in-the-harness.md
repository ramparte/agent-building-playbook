---
title: Invest the Expensive Model in the Harness
one_liner: Spend your strongest, most expensive model on improving the harness itself — then run cheaper models through the better harness — because better orchestration is second-order leverage that makes weaker models more useful.
dimensions: cost-routing, orchestration, meta-principles
---

## What it is

Model routing is usually discussed as a first-order cost trade: put the expensive model on the hard tasks, the cheap model on the easy ones, pay only for the capability you use. That framing misses a more powerful move. The harness — the orchestration graph, the prompts, the skills, the validators, the artifact formats — is itself a thing the expensive model can improve, and improving it pays off on every run that follows. So you spend your strongest model not directly on the work, but on the system that produces the work: have it sharpen the prompts, restructure the graph, design the checks, and tighten the handoff artifacts, and then route cheaper models through that better harness to do the actual production. This is second-order leverage. A first-order investment makes one output better; a harness investment makes every subsequent output better, including the outputs of weaker models. Better orchestration can make a cheap model behave like an expensive one for the task at hand, because the scaffolding now carries the structure the cheap model would otherwise have to supply itself. The expensive model's highest-value work is often not the deliverable — it is the factory.

## When to reach for it

- When a workflow will run many times: the harness improvement amortizes across every future run, so the expensive model's time is best spent there first.
- When cheaper models almost work but drift on structure — invest the strong model in scaffolding that supplies the structure, then let the cheap model fill it in.
- When designing prompts, skills, or graph nodes that many later runs will inherit — author and refine them with your best model.
- When token budget is tight: one expensive harness-improvement pass can lower the per-run cost of everything downstream.
- When you find yourself reaching for the expensive model on every individual task — that is a signal the leverage belongs one level up, in the harness.

## When NOT to

- For genuinely one-shot work that will never recur — there is no downstream to amortize the harness investment against.
- When the harness is already good enough and the bottleneck is the task's intrinsic difficulty — then the expensive model belongs on the task, not the scaffolding.
- When you cannot measure whether the harness change helped — blind harness tinkering with the expensive model burns budget without the second-order payoff.

## Related

- `patterns/match-model-to-stage.md`
- `patterns/self-ablating-harness.md`
- `patterns/leverage-over-efficiency.md`
- `patterns/match-topology-to-the-work.md`
