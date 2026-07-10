---
title: Share Full Context; Every Action Carries Decisions
one_liner: When delegating to a subagent or spawning a parallel worker, include everything the agent needs to make good decisions — the goal, constraints, prior findings, and any decisions already made.
dimensions: orchestration
---

## What it is

Every action an agent takes is a decision. When an orchestrator spawns a subagent with only a narrow task description — "search for the five most recent commits" — the subagent makes decisions that the orchestrator would have made differently had it been present: what format to return results in, whether to include merge commits, whether to stop at exactly five or to include context, how to handle an empty result. These micro-decisions compound silently. The caller gets back results shaped by assumptions it never reviewed. The solution is to treat every delegation as a full-context handoff: include the goal being pursued, the constraints the orchestrator is working under, any decisions already made that constrain the answer, and any ambiguities the orchestrator has already resolved. The subagent should not need to invent context — it should receive it. This does not mean dumping the full conversation into every delegation. It means being deliberate about what context shapes decisions, identifying what context the subagent needs to make good decisions rather than arbitrary ones, and passing exactly that.

## When to reach for it

- When the subagent's output will be used to make a downstream decision — include enough context for the subagent to shape its output toward what that decision needs.
- When different subagents working in parallel might make conflicting micro-decisions that create inconsistency — give each agent the shared constraints that must hold across all of them.
- When delegating to a fresh agent that has no prior conversation history — it cannot infer constraints from what wasn't said; state them explicitly.
- When a subagent task touches a domain where the orchestrator has already learned something important (earlier steps, known limitations, user preferences stated earlier) — surface those learnings in the delegation.

## When NOT to

- When the subagent is running a fully self-contained operation with no decision surface — a pure computation, a format conversion, a lookup with a single deterministic answer — additional context adds cost with no benefit.
- When context volume is large enough to crowd out the instructions themselves — in that case, distill the decision-relevant subset rather than passing everything.
- When the subagent operates under its own established conventions and the orchestrator's context would override those conventions incorrectly.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: notes the potential for compounding errors as a key risk in autonomous multi-step agents — the risk that full-context delegation mitigates
- Amplifier — https://github.com/microsoft/amplifier — the delegate() API includes explicit context_depth and context_scope parameters to let orchestrators pass exactly the context relevant to a delegation without always dumping the full transcript (per the Amplifier team's white papers; these parameters are not visible in the current public repos)
- Walden Yan, "Don't Build Multi-Agents" (Cognition, June 2025) — https://cognition.com/blog/dont-build-multi-agents — names "Share context, and share full agent traces, not just individual messages" as one of two core principles; direct origin of this pattern's framing

## Related

- `patterns/clean-slate-delegation.md`
- `patterns/checkpoint-handoff-file.md`
- `patterns/context-over-prompt.md`
