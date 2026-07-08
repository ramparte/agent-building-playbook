---
title: Anchor on Canonical Names
one_liner: A single well-known domain term — "TDD, London School", "arc42" — activates a whole coherent methodology the model already learned in training, far more reliably than a paragraph paraphrasing the same idea, so name the concept instead of describing it.
dimensions: context-engineering, meta-principles
---

## What it is

Models interpret vague descriptions inconsistently — "Write isolated tests with mocks" resolves differently across models, runs, and contexts, and a long prompt that tries to pin down every facet is fragile, token-heavy, and still ambiguous. A canonical name is a stronger instrument. A term the model encountered thousands of times in training — "TDD, London School", "arc42", "hexagonal architecture", "the Feynman technique" — acts as a semantic anchor: naming it activates a specific, stable cluster of associated practices that a paraphrase does not reach. The lever here is *activation of latent knowledge*, not retrieval of external content — you are reaching into what the model already knows and pulling a coherent methodology into context with a few high-signal tokens. The more canonical the term (widely used, unambiguous, well-documented in public sources), the stronger and more stable the anchor. The payoff is fewer tokens and more precise, more repeatable results, and the failure mode it replaces is the fragile mega-prompt that reconstructs a well-known methodology from scratch on every run. When a good name exists, prefer it; and when one genuinely does not, that absence is itself information — the model may have no stable prior for what you want, and you will need to describe or demonstrate it instead.

## When to reach for it

- When you are about to write a paragraph describing a methodology, architecture, or technique that already has a well-known name — use the name.
- When results vary run-to-run on the same instruction — an ambiguous description may be resolving differently each time, and a canonical term stabilizes it.
- When the token budget is tight and a full description is expensive — a strong anchor compresses an entire methodology into a few words.
- When onboarding an agent to a domain convention that has an established term of art — name it and let training do the work.

## When NOT to

- When no canonical term exists, or the term is ambiguous or contested — a weak anchor activates the wrong cluster; describe it, or define the term first.
- When your intended meaning deliberately differs from the standard one the name evokes — the anchor pulls the model toward the convention, not your variant.
- When the concept is genuinely novel to the field — there is no trained prior to activate, so you must describe or demonstrate it.
- When precision matters more than a strong prior guarantees — verify the activated behavior; a name is a powerful default, not a contract.

## Exemplars

- Ralf D. Müller (rdmueller) — https://github.com/lexler/augmented-coding-patterns/blob/main/documents/patterns/semantic-anchors.md — "Semantic Anchors," the source this pattern is adapted from; reports a systematic test — 63 anchors, 193 multiple-choice questions, 3 models scoring 96–99% — where describing the Feynman Technique without naming it dropped two of the three models to 0%
- Semantic Anchors Catalog — https://llm-coding.github.io/Semantic-Anchors/ — companion catalog of anchor terms referenced by the source pattern

## Related

- `patterns/context-over-prompt.md`
- `patterns/context-is-finite.md`
- `patterns/just-in-time-retrieval.md`
- `patterns/state-the-target.md`
- `patterns/embed-guidance-in-tool-output.md`
