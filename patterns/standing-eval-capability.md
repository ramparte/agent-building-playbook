---
title: Evals Are a Standing Capability, Not a One-Time Gate
one_liner: An eval suite that runs once at launch and is never run again is not an eval suite — it is a historical document that measured a system that no longer exists.
dimensions: verification
---

## What it is

Evals are most valuable not at initial launch but over time, when models change, prompts drift, data distributions shift, and the system evolves. A standing eval capability means the eval suite can be run at any time by any team member, produces the same measurement protocol each time, and produces results that are comparable across runs — so that changes in performance over time are detectable and attributable. This requires more than writing eval scripts: it requires that the eval suite is checked in to source control alongside the system it evaluates, that it runs in CI (or can be triggered on demand), that results are stored and compared rather than just printed, and that the team has a norm of running evals before shipping changes that might affect quality. An eval that cannot be run cheaply on demand will not be run when it would be most valuable — just before a change goes out. An eval whose results are not stored cannot be compared to prior runs. An eval that is not in version control becomes stale faster than the system it was meant to measure.

## When to reach for it

- When writing evals for the first time: design for repeatability from the start — parameterize the model, temperature, and input distribution; write results to a file; commit the suite alongside the system.
- Before any change to the prompt, model, or data pipeline: run the current eval suite to establish a baseline, make the change, run again, and compare — this is the minimum bar for "I checked that this didn't regress."
- After any unplanned quality degradation in production: run the eval suite to characterize the regression, add eval cases that reproduce it, then track the fix via eval results rather than informal inspection.
- When onboarding new team members: the eval suite is the fastest way to understand what the system is supposed to do and what "good" looks like — treat it as living documentation.
- Before upgrading models: run the existing eval suite against the candidate model before promoting it. Model upgrades that appear to improve quality often regress on specific task types that were not informally sampled during evaluation.

## When NOT to

- When the eval suite requires expensive external resources (human labelers, slow APIs, large GPU runs) that cannot be made lightweight for routine CI use — in those cases, maintain a fast lightweight version for routine checks and reserve the full suite for release gates.
- When the system is changing so rapidly that eval cases become stale within days — in early exploratory phases, lightweight human inspection may have better return on investment than maintaining a formal suite; commit to the standing capability once the system stabilizes.
- When eval results are not being used to make decisions — if the team runs evals but ignores the results, the problem is process, not tooling; fix the process before investing in more eval infrastructure.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes evals as a continuous practice, not a launch gate — the recommended approach is to build eval infrastructure early and run it repeatedly as the system evolves
- Anthropic — https://www.anthropic.com/news/developing-computer-use — Claude's Computer Use: reliability improvements were tracked across hundreds of eval runs over time, not measured once — the standing eval capability was what made iterative improvement legible

## Related

- `patterns/eval-driven-development.md`
- `patterns/test-what-not-how.md`
- `patterns/prove-on-small-sample.md`
