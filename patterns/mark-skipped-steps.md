---
title: Mark Un-Run Steps Inline for Review
one_liner: A skipped step that is not explicitly marked is indistinguishable from a completed step — make the gap visible or it will be treated as a gap that was filled.
dimensions: reliability, observability
---

## What it is

In multi-step workflows, some steps are skipped — due to conditions not being met, time constraints, scope decisions, or errors in prior steps. When those skips are not explicitly marked in the output or artifact, they become invisible: downstream consumers and reviewers have no way to distinguish a step that was completed from a step that was never run. Marking skipped steps inline — with a label, a flag, a comment, or a structured record — makes the incompleteness visible and auditable. The review can then address the gap explicitly: decide to complete it, defer it, or accept it as intentional. Unmarked skips become silent technical debt that compounds invisibly until a downstream system fails.

## When to reach for it

- Any pipeline or workflow output that may contain steps not fully executed — annotate each un-run step inline, at the point where it would have appeared.
- When generating reports, checklists, or structured outputs that represent multi-step processes: every unchecked item should carry a label explaining why it is unchecked, not simply remain blank.
- When handing off incomplete work to another agent or human reviewer: the handoff artifact must surface what was skipped and why, so the recipient can make an informed decision.
- When debugging a pipeline failure: the first check is whether any step was silently skipped rather than executed and failed.
- When designing agentic workflows: specify the skip-annotation format before implementing any conditional branching.

## When NOT to

- Steps that are excluded by design based on well-documented conditions and where the conditions themselves are visible in the output — the absence is explained by context, not obscured by it.
- Highly granular micro-steps within a single operation where annotating every skipped branch would make the artifact unreadable — apply at the meaningful unit of work, not at every execution branch.
- When a separate audit log captures skipped steps with full context and that log is always inspected alongside the primary output.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends that agents surface their reasoning and the state of their work explicitly, enabling reviewers to identify where work was omitted rather than completed
- Amplifier — https://github.com/microsoft/amplifier — the context-intelligence hook records every tool call attempt, including those that returned errors or were not executed, creating a complete inline record of what ran and what did not in each session
- Atul Gawande, *The Checklist Manifesto: How to Get Things Right* (2009) — http://atulgawande.com/book/the-checklist-manifesto/ — classic antecedent: the book's central argument is that leaving a checklist item blank is ambiguous (skipped? not reached?), and that the discipline of marking each item explicitly — done or deliberately deferred — is what makes complex professional work safe to audit and hand off
