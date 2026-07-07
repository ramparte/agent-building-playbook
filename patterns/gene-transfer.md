---
title: Gene Transfer — Port the Behavior, Not the Code
one_liner: The reusable unit between systems is rarely a whole tool but a trait — a review prompt, a validation loop, a context-file structure, a CLI affordance — so separate phenotype from organism and transfer what's valuable; at system scale this becomes semantic porting of behavior across stacks.
dimensions: knowledge, tool-design, meta-principles
---

## What it is

When a practice works well in one system, the instinct is to copy the whole tool that embodied it. That is usually the wrong unit. The valuable thing is rarely the full tool — it is a single trait that can be extracted and moved into another system the way a gene transfers between organisms. The reusable unit might be a review prompt, a validation loop, a planning sequence, a context-file structure, a CLI affordance, a test-generation pattern, a transcript-processing step, a model-routing strategy, a policy check, or a persona design. Gene transfer is the discipline of separating phenotype from organism: identifying which behavior is actually valuable versus which implementation merely happened to produce it, and carrying only the former across. This applies to code, prompts, skills, workflows, validators, and organizational practices alike. At system scale the same idea becomes semantic porting: if a library, system, or workflow embodies useful behavior, an agent can recreate that behavior in another language, stack, or policy environment without copying the original code — a kind of behavioral memory that preserves what a system does rather than the exact way it did it. Semantic porting earns its keep in clean-room and internal-policy settings, where it reduces dependency risk, and in modernization, where it preserves behavior while the architecture changes underneath. But porting behavior rather than code carries legal, security, and semantic-fidelity risk — the recreated behavior can subtly diverge, leak, or violate a license — so it needs governance, not just a clever prompt.

## When to reach for it

- When a pattern works in one team or system and you want its value elsewhere without dragging the entire originating tool along with it.
- When the genuinely reusable unit is a trait — a prompt, a loop, a file structure, an affordance — rather than a deployable artifact.
- When modernizing a legacy system: preserve what it does behaviorally while replacing how it does it.
- When a clean-room or internal-policy constraint forbids copying source but permits recreating behavior from a specification of what it does.
- When building a pattern registry — gene transfer is the mechanism by which registry entries actually move between teams.

## When NOT to

- When licensing, copyright, or contractual terms govern the original behavior — semantic porting does not launder legal obligations, and "we rewrote it" is not always a defense.
- When exact fidelity is safety-critical and the recreated behavior cannot be proven equivalent — subtle semantic drift in a reimplementation can be worse than an honest dependency.
- When the original tool is cheap to adopt wholesale and extraction buys nothing — do not decompose a dependency you could simply use.
- When the transfer would bypass security review — behavior recreated across a trust boundary still needs the same scrutiny as imported code.

## Exemplars

- Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models" (arXiv:2305.16291) — https://arxiv.org/abs/2305.16291 — formalizes: Voyager's skill library operationalizes gene transfer at agent scale — discrete, executable behaviors extracted from one task context and reused in novel situations without copying the full agent, with retrieval by natural-language description rather than exact path.

## Related

- `patterns/build-a-pattern-registry.md`
- `patterns/brownfield-is-the-real-test.md`
- `patterns/governance-is-infrastructure.md`
