---
title: Brownfield Is the Real Test
one_liner: Greenfield prototypes are easy to celebrate; brownfield systems expose whether a workflow can handle legacy constraints, hidden dependencies, and production risk — the mature move is to characterize existing behavior and write regression tests before any rewrite, never a blind rewrite.
dimensions: workflow-discipline, reliability, verification
---

## What it is

Greenfield work flatters an agentic system. A fresh prototype has no legacy constraints, no production behavior to preserve, no hidden dependencies, no institutional knowledge buried in the code, and no risk if it is wrong — which is exactly why a slick greenfield demo proves so little about whether a workflow can actually finish work. Brownfield is the real test of agentic maturity, because brownfield is where all of those pressures are present at once: a working system that real users depend on, behaviors that nobody documented but everybody relies on, dependencies that surface only when broken, and a cost of failure measured in incidents. The encouraging finding is that agents can be genuinely useful in brownfield, often more so than expected, because the brownfield environment is rich in exactly the artifacts agents are good at consuming and producing: they can analyze existing behavior, generate user stories from the code as it actually is, create regression tests before any rewrite, produce compatibility layers, run old and new implementations side by side to compare outputs, generate migration plans, inspect logs and incident history for the behaviors that matter, and rewrite components while preserving behavior. The line between the dangerous use and the mature use is sharp. The dangerous version is the blind rewrite — point the agent at the old system, ask for a new one, and hope. The mature version starts from acceptance evidence and asks the load-bearing question first: what must remain true after the rewrite? It characterizes the existing behavior, pins it down with regression tests, and only then changes the implementation — so that "it still works" is a checked claim, not a hope.

## When to reach for it

- When modifying or replacing any system that real users already depend on — treat preserving current behavior as the primary requirement, not an afterthought.
- When you are tempted by a clean rewrite — first invest in characterizing and pinning down what the existing system actually does, then change it under the protection of those tests.
- When the existing system's behavior is undocumented — use the agent to generate user stories, regression tests, and behavioral descriptions from the code, logs, and incident history before touching it.
- When evaluating whether an agentic workflow is actually mature — test it on a brownfield task with real constraints, not a greenfield demo that hides every hard part.
- When migrating between implementations — run old and new side by side and diff their outputs, so divergence is caught as data rather than discovered as an outage.

## When NOT to

- For genuine throwaway prototypes where there is no existing behavior to preserve and no production risk — the brownfield discipline is overhead with nothing to protect.
- When the existing behavior is known to be wrong and the explicit goal is to change it — in that case preserving it is the bug, not the requirement; pin the behaviors you intend to keep, not the ones you intend to fix.
- When characterization is impossible because the legacy system cannot be exercised or observed at all — escalate the risk to a human rather than letting the agent rewrite blind under a false sense of coverage.

## Exemplars

- Michael Feathers — https://www.oreilly.com/library/view/working-effectively-with/0131177052/ — Working Effectively with Legacy Code: the foundational discipline of putting characterization tests around existing behavior before changing it, the human practice this pattern hands to agents
- Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" (arXiv:2310.06770) — https://arxiv.org/abs/2310.06770 — empirical support: real-repository evaluation reveals that models performing well on toy benchmarks resolve only ~2% of authentic brownfield GitHub issues, confirming that greenfield capability does not transfer to legacy codebases

## Related

- `patterns/gene-transfer.md`
- `patterns/demand-independent-proof.md`
- `patterns/test-what-not-how.md`
- `patterns/work-backward-from-the-shipping-dock.md`
