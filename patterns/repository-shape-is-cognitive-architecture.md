---
title: Repository Shape Is Cognitive Architecture
one_liner: A repository is not just code storage — it is the working memory and context boundary of an agentic workflow; too broad and it poisons context, too narrow and the agent starves, so repo shape is a design decision, not an accident.
dimensions: context-engineering, workflow-discipline, meta-principles
---

## What it is

A repository looks like storage — a place files live — but in an agentic workflow it functions as working memory and a context boundary. What is inside the repo is what the agent can see, search, and reason over; what is outside it is, for practical purposes, invisible. That makes repo shape a context-engineering decision with a sharp tradeoff in both directions. Make the repo too broad — a sprawling mono-repo where the agent can reach everything — and you poison the context: the agent retrieves irrelevant files, conflates unrelated concerns, and burns its attention budget on noise. Make it too narrow — a tightly scoped slice that excludes a needed dependency, a shared schema, or the doc that explains a convention — and the agent starves, hallucinating the information it cannot reach. The mono-repo-versus-narrow-repo question is therefore not an org-chart or build-system question alone; it is a question about what the agent should hold in working memory for a given class of work. Repository boundaries become part of the cognitive architecture of the system, and like any architecture they should be chosen deliberately, sized to the work, and revised when the work changes — not inherited by accident from how the code happened to be split.

## When to reach for it

- When an agent keeps pulling in irrelevant files or conflating concerns — the repo is too broad and is poisoning context; narrow the boundary.
- When an agent repeatedly hallucinates facts that live just outside its repo — it is starving; widen the boundary or bring the dependency in.
- When designing a new agentic workflow: decide the repo boundary as part of the design, the way you would decide what goes in a prompt.
- When choosing mono-repo versus split-repo for agent-driven work — treat it as a context-engineering decision, not only a build or ownership one.
- When the work itself changes shape — revisit the boundary, because the right context boundary for one class of task is wrong for another.

## When NOT to

- When humans, not agents, are the primary consumers and the repo layout is optimized for human workflows that work fine as they are.
- When reshaping the repo would break builds, ownership, or tooling more than it helps the agent — fix context scope with retrieval or sub-repo views instead of physically resplitting.
- When the agent's context problems are really prompt or retrieval problems wearing a repo costume — diagnose before you reorganize the filesystem.

## Related

- `patterns/long-horizon-memory.md`
- `patterns/context-is-finite.md`
- `patterns/attention-is-the-scarce-resource.md`
- `patterns/recipe-not-conversation.md`
