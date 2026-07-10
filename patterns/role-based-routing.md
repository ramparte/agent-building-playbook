---
title: Pull Models From Provisioned Roles
one_liner: Reference abstract capability roles in code rather than model names — let external configuration map roles to models, so routing decisions survive model changes without code changes.
dimensions: cost-routing
---

## What it is

Hardcoding model names in orchestration code creates a brittle dependency: every time a provider releases a better model, deprecates an old one, or changes pricing, every reference in the codebase must be updated. The pattern is to decouple routing intent from model identity by expressing capability requirements as named roles — "fast", "reasoning", "writing", "coding" — and resolving those roles to specific model names at runtime from a provisioned configuration. The calling code expresses what it needs ("I need a model with reasoning capability here"), not which model satisfies that need. Configuration maps the role to the current best model for that capability tier. When a better model becomes available or a cheaper equivalent covers the same role, the configuration changes; the calling code does not. This separation also enables per-environment overrides: a development environment can map all roles to a single cheap model; a production environment can map each role to the optimal choice for that tier. The role is the stable identity. The model is the implementation.

## When to reach for it

- When a pipeline uses more than one model tier — define roles at design time and let configuration drive the mapping to actual models.
- When models change frequently (new releases, deprecations, pricing shifts) — role-based routing means the change is a configuration update, not a code change.
- When the same workflow runs in different environments with different cost constraints — map roles to different models per environment without touching the pipeline logic.
- When a team wants to experiment with model substitutions (A/B testing, cost benchmarking) — changing a role mapping is a single config edit, not a code refactor.

## When NOT to

- When a task has a hard requirement on a specific model's unique capability that no other model in the role can substitute — direct model selection may be necessary to make the constraint explicit rather than hiding it behind a role.
- When the pipeline is a simple single-model workflow and the overhead of role configuration adds complexity without benefit.
- When model selection must be dynamic at request time based on inputs that configuration cannot anticipate — role-based routing assumes the role can be determined statically at the call site.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier-bundle-routing-matrix — declarative model routing: agents declare a semantic model_role describing what they do, and externally-managed matrices (13 semantic roles, 8 curated matrices) resolve each role to a provider and model at runtime — callers express capability requirements, not model names, and routing changes without touching orchestration code
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: identifies model selection per task type as a first-class design decision in agent pipelines; decoupling the selection decision from the calling code is the natural extension of this recommendation
- Chen, Zaharia & Zou, "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance" (arXiv:2305.05176) — https://arxiv.org/abs/2305.05176 — classic antecedent: introduces cost-aware routing and cascading across models of different capability tiers — the economic rationale that stable capability roles operationalize in configuration
- Ong et al., "RouteLLM: Learning to Route LLMs with Preference Data" (arXiv:2406.18665) — https://arxiv.org/abs/2406.18665 — formalizes: learned routing policies that generalize when underlying models change at test time, empirically validating the stable-role / swappable-model separation this pattern advocates

## Related

- `patterns/match-model-to-stage.md`
- `patterns/delegation-token-economics.md`
- `patterns/start-least-agentic.md`
