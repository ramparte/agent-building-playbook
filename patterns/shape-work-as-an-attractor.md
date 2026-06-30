---
title: Shape the Workflow as an Attractor
one_liner: Design the workflow so the correct outcome is its stable equilibrium — the state it converges toward from a wide range of starting points and returns to after the model drifts — and judge success by that convergence, not by whether a step reported done.
dimensions: orchestration, workflow-discipline, meta-principles
---

## What it is

An attractor is a state a system settles into from many different starting points and returns to after it is perturbed — a marble in a bowl rolls back to the bottom no matter where you nudge it. The most reliable agentic workflows are shaped this way on purpose: the correct, accepted outcome is the low point of the bowl, and the graph is carved so that wherever the model starts and however it wanders, the work tends back toward that outcome. This is a claim about the topology of the whole workflow, not a feature of any single step. It also redefines what "done" means. Conventional automation is finished when the script completes — it ran to the end without throwing. That definition cannot survive a nondeterministic actor, because a model can finish a step and still be wrong: it can misunderstand the intent, drift off the spec, overfit to one example, stall, or hand back a plausible artifact that does not do the job. An attractor-shaped workflow is judged by a different question — did the system converge to the desired state? — so a step that "succeeds" while producing a wrong-but-plausible result is a perturbation the workflow is built to absorb, not a finish line. The design goal is not to prevent every error, which is hopeless, but to make the desired state the one the system keeps falling back into, and to make sure no plausible failure can roll the marble out over the rim with nothing to catch it.

You carve the bowl with feedback edges: wire the graph so a failed check routes work back to the phase that can fix it rather than forcing forward progress. Review sends work back to implementation; a failing test triggers diagnosis instead of a blind patch; a discovered contradiction triggers a spec revision; an uncertainty threshold escalates to a human instead of committing to a guess; repeated failure triggers a postmortem rather than an unbounded retry. Most of those edges are built from patterns the library already has — escalation, root-cause diagnosis, bounded stop conditions, independent review. What the attractor framing adds is the question you ask of the workflow as a whole: does every plausible way this can go wrong have an edge that bends it back toward the desired state, or are there failures that simply run off the rim? Making steps idempotent and resumable serves the same end — if re-running a step converges toward the outcome instead of compounding the mess, the basin is wider and the equilibrium is more stable.

## When to reach for it

- Any multi-stage workflow where a step can "succeed" while producing a wrong-but-plausible artifact — the failure mode deterministic automation does not have.
- When work runs with enough autonomy that no human watches every step — convergence has to be engineered in, because no one is there to nudge the marble back by hand.
- When the cost of a silent wrong answer reaching the end is high — make sure each phase has an edge that can route work backward, not only forward.
- When a workflow sometimes finishes "done" but wrong — look for the failure mode that has no feedback edge bending it back toward the desired state.
- When designing how to judge a workflow — measure whether it converges to an accepted state, not whether its final step returned success.

## When NOT to

- Genuinely deterministic, machine-checkable work where "it completed" really is success — there is no drift to converge away from, and the machinery is pure overhead.
- Throwaway one-shot tasks where you are the recovery loop — you will eyeball the result and rerun by hand if it is wrong.
- When a feedback edge would route around a root-cause bug that should be fixed instead — an attractor is meant to absorb model drift, not broken tools or specs.
- When the convergence budget is unbounded — a basin with no edge is just an infinite loop with a nicer name; bound it with an explicit stop condition.

## Related

- `patterns/guardrails-and-escalation.md`
- `patterns/fix-the-root-cause.md`
- `patterns/clear-stop-condition.md`
- `patterns/decompose-on-timeout.md`
- `patterns/adversarial-parallel-review.md`
- `patterns/earn-the-interruption.md`
- `patterns/match-topology-to-the-work.md`
