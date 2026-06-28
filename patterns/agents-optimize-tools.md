---
title: Let Agents Evaluate and Optimize Your Tools
one_liner: Use an agent to test your tool set — have it attempt real tasks, observe where it selects incorrectly or fails, and feed those observations back into tool descriptions and interfaces before deploying.
dimensions: tool-design, verification
---

## What it is

Tool design is typically done from the designer's perspective: the author writes a description that seems clear, registers the tool, and considers it done. The model's perspective is different — it has no background context about the designer's intent, it reads the description literally in the middle of a task, and it makes selection decisions based only on what the description says. The gap between "seems clear to the author" and "produces reliable selection by the model" is where most tool design errors live. Letting agents evaluate tools closes this gap empirically rather than by inspection. The process: give an agent access to the full tool set and a set of realistic tasks. Observe which tools it selects, whether it selects correctly, where it hesitates or selects inconsistently, and what errors result from wrong selections. Treat each wrong selection as a bug report: the tool's name or description was not specific enough to distinguish it from the tool the agent should have called instead. Revise the description to add the missing specificity, rerun the evaluation, and iterate. This approach treats tool descriptions as a specification that must be validated against the model's behavior, not a documentation artifact that is correct by construction. The agent is the oracle: if it selects wrong, the description is wrong.

## When to reach for it

- When building a new tool set before deploying it to production — run an evaluation pass with representative tasks and observe tool selection behavior before agents encounter real workloads.
- When agents are failing tasks due to wrong tool selection or incorrect tool usage — use an evaluation run to identify which descriptions are ambiguous and revise them based on the observed failure pattern.
- When adding a new tool to an existing set — the new tool may cause selection confusion with existing tools; test the full set after the addition, not just the new tool in isolation.
- When migrating tools to a new model — selection behavior varies across models; re-evaluate the tool set against the target model rather than assuming descriptions that worked before will continue to work.

## When NOT to

- When the tool set has only one or two tools with clearly distinct purposes — the evaluation overhead is not justified when selection errors are structurally impossible.
- When the task distribution for evaluation is not representative of real workloads — an evaluation that only tests happy-path calls will not surface the edge-case ambiguities that matter in production.
- When tool descriptions are generated dynamically at runtime and cannot be revised statically — in this case, focus evaluation on the generation logic rather than individual description text.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends empirical evaluation of agent behavior over upfront design, including evaluation of tool selection reliability as a first-class concern
- Anthropic — https://www.anthropic.com/news/developing-computer-use — Claude's Computer Use: evaluation-driven iteration on the tool interface was central to making the computer-use capability reliable

## Related

- `patterns/tools-for-agents.md`
- `patterns/namespace-tools.md`
- `patterns/demand-independent-proof.md`
- `patterns/verify-independently.md`
