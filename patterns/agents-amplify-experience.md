---
title: Agents Amplify Experience
one_liner: Agents multiply the output of whoever wields them — great judgment gets amplified into great results; poor judgment gets amplified into confident mistakes at scale.
dimensions: taste
---

## What it is

An agent is a force multiplier, not a substitute for judgment. When an experienced practitioner directs agents, their pattern recognition, their sense of what matters, and their ability to evaluate output get amplified across many more tasks than they could execute manually. When someone without that experience directs the same agents, they get more of what they can already produce — more volume, more speed, but the same quality of judgment, applied at higher velocity. This is the inversion that makes experience matter more in an AI-first world, not less: the agent removes the execution bottleneck and exposes the judgment bottleneck. A developer with deep knowledge of a domain can use agents to accomplish in a day what previously took a month — but that month's worth of work reflects the developer's judgment. A developer without domain knowledge using the same agents produces a month's worth of plausible-looking output, quickly, with the same limitations in understanding that would have produced poor work manually. Experience and taste are not made less important by agents — they are the limiting factor when agents remove everything else.

## When to reach for it

- When evaluating whether to delegate a task to an agent: ask whether you have enough experience to evaluate the output; if you do not, the agent will produce output you cannot meaningfully review.
- When agents are producing outputs that feel wrong but you cannot say why: that sense of wrongness is experience speaking; invest in diagnosing it rather than accepting the output.
- When onboarding to a new domain and considering using agents to accelerate: use agents for execution of understood tasks; use your own work for the tasks where you need to build understanding.
- When reviewing agent output: the quality of your review is the quality floor for the work; agents raise the ceiling but you set the floor.
- When designing a system that will involve less-experienced operators: design the feedback loops and guardrails that give experience its proxy — clear success criteria, independent verification, legible output.

## When NOT to

- This is not an argument against using agents before you have full mastery: agents are excellent for exploration and learning in unfamiliar domains — but treat their outputs as provisional until you have developed the judgment to evaluate them.
- Not an argument that only experts can use agents productively: experience in any aspect of the workflow — evaluation, domain knowledge, process understanding — gets amplified; you do not need mastery across the full stack.
- Not a reason to avoid delegation: the goal is to develop taste alongside agent use, not to defer agent use until taste is developed.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: notes that agent evaluation and the ability to recognize when agent output is wrong is as important as the agent's capability — the human's judgment is the system's quality gate
- Amplifier — https://github.com/microsoft/amplifier — The Amplifier philosophy emphasizes that agents should be used to execute specified tasks, not to make design decisions; keeping judgment in human hands while delegating execution is the design that makes experience amplification work correctly

## Related

- `patterns/develop-your-taste.md`
- `patterns/find-the-hard-stuff.md`
- `patterns/demand-independent-proof.md`
