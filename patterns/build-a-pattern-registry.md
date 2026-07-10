---
title: Build a Pattern Registry
one_liner: Teams independently rediscover the same loops, validators, and review tricks — a pattern registry captures the reusable operating moves with usage guidance and contraindications, so practice transfers without forcing everyone onto the same stack; it is the package manager of agentic practice.
dimensions: knowledge, meta-principles, workflow-discipline
---

## What it is

Across an organization, teams keep reinventing the same wheels: the same agent loops, the same validators, the same review tricks, the same context layouts, the same agent-shaped tools — each discovered independently, at cost, and never shared. A pattern registry is the institutional response. It captures the reusable operating moves — the "genes" of agentic practice — without requiring every team to adopt the same organism, the same framework, or the same stack. The point is transfer of practice, not enforcement of uniformity. A useful registry entry is far more than a name and a description: it records the pattern name, the problem it solves, when to use it, when NOT to use it, the artifacts it requires, example prompts or workflow nodes, known failure modes, the method for evaluating whether it worked, implementation references, provenance, and the maintainers or endorsers who stand behind it. The contraindications are not optional politeness — they are what make the registry trustworthy. Heavy workflow graphs are wrong for many tasks; universal memory may poison context; human approval gates may destroy autonomy; a playful agent persona may delight one culture and alienate another. A registry that lists only when to use each pattern, and never when to avoid it, becomes a cargo-cult catalog. Done well, a pattern registry becomes the package manager of agentic practice: a shared, versioned, attributed index of operating moves that teams can pull from, adapt, and contribute back to.

## When to reach for it

- When multiple teams in an organization are independently solving the same agent-building problems and the solutions never propagate.
- When a practice that works well in one team should spread, but you do not want to force every team onto the originating team's framework or stack.
- When you keep rediscovering pattern candidates from transcript mining and need somewhere structured to put them.
- When onboarding new teams or agents who would benefit from the accumulated operating moves of the organization rather than starting from scratch.
- When a pattern's misuse is costly enough that its contraindications need to travel alongside it — the registry entry is where the "when NOT to" lives.

## When NOT to

- When there is no one to maintain it — an unowned registry rots into a graveyard of stale entries that misleads more than it helps.
- When the organization is too small or too early for cross-team reuse — premature registry-building is process for its own sake.
- When entries would lack contraindications and evaluation methods — a registry of unqualified recommendations is worse than no registry.
- When the registry is used to mandate uniformity rather than enable transfer — the moment it becomes a compliance checklist, it stops capturing the genes and starts cloning the organism.

## Exemplars

- Alexander et al., *A Pattern Language* (1977) — https://en.wikipedia.org/wiki/A_Pattern_Language — classic antecedent: the original registry of 253 named patterns, each with a problem statement, solution, and cross-references; established the template for named, contraindicated, cross-referenced entries that makes a registry trustworthy rather than a mere catalog.
- Gamma, Helm, Johnson, Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software* (1994) — https://en.wikipedia.org/wiki/Design_Patterns — classic antecedent: formalized the software pattern catalog with 23 named, categorized patterns, demonstrating that documented practices travel between practitioners without mandating a shared implementation.
- Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models" (arXiv:2305.16291) — https://arxiv.org/abs/2305.16291 — formalizes: Voyager's ever-growing skill library is a queryable pattern registry for an LLM agent, accumulating discrete, tested behaviors that compound capability across sessions without requiring the agent to rediscover them.
- 2389 Research, skills.2389.ai — https://skills.2389.ai — first-party: this playbook's sibling registry — a browsable marketplace of Claude Code plugins and MCP servers ("These are the tools we use every day"), each installable into any agent with one command; the pattern's package-manager metaphor made concrete.

## Related

- `patterns/gene-transfer.md`
- `patterns/personal-to-shared-topology.md`
- `patterns/composable-patterns.md`
- `patterns/mine-transcripts.md`
