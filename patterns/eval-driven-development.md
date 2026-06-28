---
title: Eval-Driven Development
one_liner: Build evals before building features — you cannot improve what you cannot measure, and you cannot trust improvements you have not defined a measurement for.
dimensions: verification, workflow-discipline
---

## What it is

Eval-driven development (EDD) applies the test-driven development discipline to agentic and LLM-based systems: define the evaluation criteria before building the capability, build the eval harness that measures against those criteria, and then implement the capability until it passes. The eval is the specification made executable. Without an eval, capability development proceeds by intuition and informal inspection — the developer runs the system, looks at the output, and decides it "looks right." This works for demos and fails at scale because "looks right" cannot be automated, reproducibly measured, or tracked across model changes, prompt changes, or data distribution shifts. Evals make improvement legible: you can say "this change improved success rate on the test set from 71% to 84%" and mean it. They also make regression visible: a change that breaks previously-passing evals is visible immediately rather than discovered in production. Building evals first forces the developer to define success concretely — the same discipline that writing tests first forces concrete interface design. If you cannot write the eval, you do not yet know what the capability is supposed to do.

## When to reach for it

- Before building any capability that will be measured by human judgment — translate that judgment into an automated eval before writing the capability. If you cannot automate it, define at least a structured rubric for human evaluators.
- When making a prompt change that is supposed to improve quality — write an eval that would detect the improvement before making the change, not after. Otherwise you cannot distinguish genuine improvement from regression in a different direction.
- Before upgrading to a new model version — run your existing evals against the new model first. Do not assume the upgrade is an improvement; measure it.
- When a capability that worked in development is failing in production — build an eval that reproduces the failure before attempting to fix it. A fix without a reproducing eval may fix the wrong thing.
- When the team has disagreement about whether a change is an improvement — an eval resolves the disagreement with evidence.

## When NOT to

- For one-off outputs that will never be produced again — building an eval harness for a capability you will use once has a poor return on investment.
- When the capability is exploratory and the success criteria genuinely cannot be defined yet — run the exploration first, observe what good and bad look like, then define the eval before productionizing.
- When the only credible evaluator is human judgment on genuinely subjective output (creative writing for a specific audience, for example) — in those cases, build a structured human evaluation protocol rather than forcing automation that cannot capture the real quality signal.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: describes the evaluator as a core agentic primitive and recommends building eval harnesses as the foundation of reliable agent development, not as an afterthought
- Anthropic — https://www.anthropic.com/news/developing-computer-use — Claude's Computer Use: the reliability of computer use was built through eval-driven iteration — defining success criteria for each task type and measuring against them systematically

## Related

- `patterns/standing-eval-capability.md`
- `patterns/test-what-not-how.md`
- `patterns/prove-on-small-sample.md`
