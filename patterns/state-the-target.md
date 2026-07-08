---
title: State the Target, Not the Prohibition
one_liner: Telling a model what not to do activates the very concept you're suppressing — "list the planets but not the moon" tends to produce the moon — so phrase instructions as a positive description of the target, and enforce hard prohibitions with a deterministic check rather than louder "do NOT".
dimensions: context-engineering, reliability
---

## What it is

Negation is a weak signal in a transformer. When you write "don't mention the moon", the model attends heavily to the content word "moon" and only lightly to the negation modifying it, so the concept you wanted suppressed is now activated and competing with the instruction to suppress it — and you frequently get exactly what you asked to avoid. This is well documented: a model's internal representations of "X is Y" and "X is not Y" are surprisingly similar, and it is not only a text phenomenon — vision models asked for "a room with no elephants" tend to render elephants by the same mechanism. The remedy is to point at the target: reframe the request as a positive description of the behavior you want, so the unwanted concept never enters context at all. "Don't use global variables" becomes "use local variables and parameter passing"; "don't nest routes deeply" becomes "use a flat route structure". This is distinct from "be specific" — adding specificity to a negative instruction usually means adding *more* negations and over-constraining the solution space, which activates more of what you are trying to avoid; pointing the target changes *which concepts you activate*, at the same level of detail. And when a prohibition is genuinely non-negotiable — a banned API, a forbidden path — do not fight the mechanism with louder or repeated negation; enforce it with a deterministic check that fails the output, and spend your prompt tokens describing the target instead.

## When to reach for it

- Whenever you catch yourself writing "don't", "never", or "avoid" in an instruction — try restating it as the positive behavior you want.
- When a model keeps producing the exact thing you told it not to — the prohibition is probably activating the concept; flip it to a target.
- When a prompt has accumulated a list of "don't do X" clauses — each one seeds a concept; replace them with a description of the desired shape.
- When the same suppression matters across many runs — encode the positive target once rather than repeating escalating negations.

## When NOT to

- When a prohibition is safety- or policy-critical and must hold regardless of phrasing — state the target *and* enforce it with a deterministic gate; never rely on wording alone.
- When there is genuinely no positive way to express the constraint — some exclusions have no natural target, so bound them with a check rather than with emphasis.
- When the negation is load-bearing context a human reader needs — this is about instructions to the model, not documentation written for people.

## Exemplars

- Juan Michelini — https://github.com/lexler/augmented-coding-patterns/blob/main/documents/patterns/point-the-target.md — "Point the Target," the source this pattern is adapted from
- Juan Michelini — https://github.com/lexler/augmented-coding-patterns/blob/main/documents/obstacles/negative-bleedthrough.md — "Negative Bleedthrough," the companion obstacle write-up describing the underlying mechanism
- Kassner & Schütze (2020) — https://aclanthology.org/2020.acl-main.698/ — "Negated and Misprimed Probes for Pretrained Language Models," research (cited by the source) showing pretrained language models handle negation poorly

## Related

- `patterns/context-over-prompt.md`
- `patterns/anchor-on-canonical-names.md`
- `patterns/tools-for-agents.md`
- `patterns/guardrails-and-escalation.md`
