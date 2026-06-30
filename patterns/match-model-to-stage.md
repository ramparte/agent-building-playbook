---
title: Match Model to Stage
one_liner: Different stages of a workflow warrant different model capability levels — route expensive models to complex reasoning stages and cheap models to mechanical stages, not the other way around.
dimensions: cost-routing
---

## What it is

Every multi-stage AI pipeline contains a mix of task types: some stages require deep reasoning, nuanced judgment, or creative synthesis; others are mechanical — parsing, classification, formatting, extraction, routing decisions. Treating all stages as equivalent and running them through the most capable (and expensive) model is not a conservative choice — it is a wasteful one that often produces no better outcomes for the mechanical stages while inflating costs linearly with task count. The pattern is to map each stage's cognitive demand to the appropriate model tier. High-stakes reasoning stages — evaluating ambiguous requirements, synthesizing conflicting evidence, making architectural decisions — warrant the most capable model. Mechanical stages — extracting structured fields from well-formed input, reformatting output, classifying a request into a known taxonomy — can be delegated to a fast, cheap model without quality loss. The calibration question for each stage is not "which model do we have?" but "what is the minimum capability level that produces acceptable output here?" Running the minimum sufficient model at each stage is not a compromise; it is the correct engineering decision.

Routing models by stage is often framed as a way to save money, and it does — but the deeper reason to do it is that the model assigned to a role shapes how that role behaves, which makes routing a design decision about the workflow itself. The roles in a typical graph each call for a different kind of model:

| Role | Model choice pattern |
|---|---|
| **Planner** | A stronger, more expensive model when global coherence across the whole task matters. |
| **Executor** | A cheaper or faster model for well-scoped implementation where the structure is already decided. |
| **Reviewer** | A *different* model family from the implementer, to reduce shared blind spots. |
| **Critic** | Adversarial framing, fresh context, or several models — independence is the point. |
| **Summarizer** | A cheaper model when the output is bounded and the result is validated downstream. |
| **Researcher** | Models or tools with retrieval, browsing, or large context windows. |

The Reviewer and Critic rows are the ones most often gotten wrong: routing them to the *same* model that did the work saves nothing meaningful and quietly destroys the independence that makes review worth running. Choosing a different family there is a workflow decision wearing a cost-routing disguise.

## When to reach for it

- When designing a multi-step pipeline with distinct task types — identify at design time which stages are reasoning-heavy and which are mechanical, then assign model tiers accordingly.
- When a pipeline's inference cost is a concern — audit each stage's model assignment before optimizing code; model-tier mismatches are the most common source of unnecessary cost.
- When a high-cost pipeline is producing outputs no better than a lower-cost equivalent — this is often a sign that expensive models are being used for stages that don't benefit from the extra capability.
- When routing between a small set of model tiers (e.g., fast, standard, reasoning) based on a lightweight classifier — the classifier itself runs on a cheap model, and its routing decision determines the model tier for the subsequent stage.

## When NOT to

- When stage boundaries are unclear or the task type varies unpredictably within a stage — model-switching overhead and routing complexity may outweigh cost savings.
- When the workflow runs only occasionally and inference cost is irrelevant to the budget — the engineering complexity of tiered routing is not justified by savings that are small in absolute terms.
- When model capability differences at the mechanical stages produce correctness differences that matter — some "mechanical" tasks are more capability-sensitive than they appear; verify this before downgrading.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: notes that model selection is a design decision at each step of a pipeline, not a global setting; using smaller models for sub-tasks that don't require full capability is called out as a cost management pattern
- Amplifier — https://github.com/microsoft/amplifier — the delegate() API accepts a model_role parameter that decouples the caller's routing intent ("I need reasoning capability here") from the specific model assigned; role definitions are configured externally, enabling stage-by-stage routing without hardcoding model names

## Related

- `patterns/role-based-routing.md`
- `patterns/delegation-token-economics.md`
- `patterns/start-least-agentic.md`
- `patterns/invest-the-expensive-model-in-the-harness.md`
- `patterns/adversarial-parallel-review.md`
