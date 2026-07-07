---
title: Delegation Is Token Economics
one_liner: Every delegation decision is a token investment — the tokens spent spawning and briefing a subagent must be justified by the value of offloading the work from the orchestrator's context budget.
dimensions: cost-routing, context-engineering, orchestration
---

## What it is

Delegation is not free. When an orchestrator spawns a subagent, it spends tokens to construct the briefing, pays for the subagent's full execution (including its own context, reasoning, and output), and then pays again to consume the result back into the orchestrator's context. The decision to delegate is always a token expenditure — the question is whether that expenditure is the cheapest way to get the work done, relative to executing the work in the orchestrator's own context. For short, mechanical tasks, the delegation overhead can exceed the cost of simply doing the work inline; for long, detail-heavy tasks, delegation is almost always cheaper because it prevents the orchestrator's context from filling with process content that is irrelevant once the task completes. The economic model is: delegate when (briefing cost + subagent execution cost + result ingestion cost) < (cost of running the task in orchestrator context + the opportunity cost of the context tokens consumed). Understanding this tradeoff explicitly prevents two failure modes: over-delegation, where orchestrators spawn subagents for trivially small tasks and pay overhead for no benefit; and under-delegation, where orchestrators run everything inline, exhaust their context, and degrade in quality as the window fills with irrelevant detail.

## When to reach for it

- When designing a multi-agent pipeline, model the token economics of each delegation decision: estimate the briefing size, expected subagent cost, and result size, and compare to the cost of inline execution.
- When a task's execution produces significant intermediate detail that the orchestrator does not need — log lines, intermediate reasoning, verbose tool outputs — and delegation would keep that detail out of the orchestrator's context entirely.
- When choosing between running three tasks in parallel subagents vs. sequentially inline — the parallel option may be cheaper in wall-clock time, but each subagent pays its own context startup cost; verify the economics before assuming parallel delegation is always better.
- When a subagent can use a cheaper model than the orchestrator — the model-tier savings may offset the delegation overhead, making delegation economically superior even for tasks that could have run inline.

## When NOT to

- When the task is trivially small (a single lookup, a one-line transformation) — delegation overhead dominates, and inline execution is cheaper in both tokens and latency.
- When the briefing required to bring a subagent up to speed would be nearly as large as the orchestrator's current context — there is no context savings, and the overhead is pure waste.
- When the result the subagent returns must be consumed in full by the orchestrator — if the orchestrator needs every token the subagent produces, delegation achieves no context benefit and only adds overhead.
- When the workflow is running in a cost-insensitive environment where token economics do not constrain design — optimize for simplicity over economic efficiency in this case.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier — the delegate() API is the primary mechanism for token-economic delegation decisions; the context_depth parameter controls briefing cost (none = minimal briefing, all = full history briefing), and the model_role parameter controls subagent execution cost; making both explicit encourages engineers to reason about the economics of each delegation call
- Anthropic Engineering, "How we built our multi-agent research system" — https://www.anthropic.com/engineering/multi-agent-research-system — empirical support: production data quantifying multi-agent delegation overhead (agents use ~4× more tokens than chat; multi-agent pipelines ~15×); shows the economics require tasks with sufficient value to justify delegation cost

## Related

- `patterns/match-model-to-stage.md`
- `patterns/role-based-routing.md`
- `patterns/subagents-as-context-sinks.md`
- `patterns/context-is-finite.md`
- `patterns/clean-slate-delegation.md`
