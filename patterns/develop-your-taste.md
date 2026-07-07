---
title: Develop Your Taste
one_liner: Taste — the ability to recognize quality and know when something is wrong — is a craft that must be deliberately built; it does not emerge from volume of output alone.
dimensions: taste
---

## What it is

Taste is the capacity to recognize the difference between good and good-enough, between an output that is correct and an output that is right. It is distinct from skill: skill is the ability to execute; taste is the ability to evaluate. In traditional software engineering, taste develops over years of encountering real systems in production — seeing what breaks, what ages poorly, what stays maintainable, and what doesn't. In AI-assisted development, the cycle is faster but the feedback is noisier. Volume of output increases dramatically; the discipline of evaluating that output must increase proportionally or taste atrophies. Developing taste requires deliberate exposure to both good and bad examples, the practice of explaining why something is better, and a habit of dissatisfaction with outputs that are merely adequate. It also requires honesty with yourself: taste is not preference or habit, it is calibrated judgment. An agent that always tells you what it produced is good is not developing your taste — it is flattening it. A precise way to name what taste becomes in an agentic setting is consistent judgment under acceleration: when agents generate many options at once, the person who can choose well becomes more valuable, and that judgment spans many dimensions — product taste, architectural judgment, security paranoia, domain intuition, organizational sensitivity, the willingness to stop a bad path, the ability to see when something is almost right but not finished, and the ability to select the right level of process for the stakes. As generation becomes cheap, editing becomes the scarce function: the human's role shifts toward curation and selection, exercising editorial judgment at the system level — deciding what gets into the product, rejecting plausible-but-wrong work, preserving coherence across many generated artifacts, and ensuring outputs serve strategy rather than local optimization. Seek out the exemplars, study the failures, and build the internal model that tells you when something is off before you can articulate exactly why.

## When to reach for it

- When reviewing outputs from your own agent runs: do not just verify that they are correct — ask whether they are good, and develop a vocabulary for the difference.
- When designing systems: ask not just whether a design will work but whether it is the right design, and practice explaining why.
- When evaluating tools, patterns, and approaches: use each comparison as an opportunity to sharpen the internal model, not just to make a selection.
- When something feels off but you cannot say why: that sense of wrongness is taste in its early form — slow down, name what is bothering you, and refine the judgment.
- When reading others' code, writing, or designs: treat every encounter with excellent work as a calibration opportunity.

## When NOT to

- Taste is not perfectionism: do not use the pursuit of quality as a reason to not ship. Taste should accelerate judgment, not induce paralysis.
- When speed genuinely trumps quality: there are contexts where adequate is the correct target, and applying taste-level scrutiny is disproportionate to the stakes.
- When taste masquerades as aesthetic preference: distinguish between developed judgment about what works and personal preference for what you are used to.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: the ability to distinguish agentic patterns that are genuinely reliable from those that look reliable in demos is a form of taste that develops through direct evaluation experience, not from reading descriptions of the patterns
- Amplifier — https://github.com/microsoft/amplifier — The philosophy documents in the Amplifier ecosystem (LANGUAGE_PHILOSOPHY.md, MODULAR_DESIGN_PHILOSOPHY.md) represent distilled taste — not just rules, but calibrated judgment about what produces good outcomes over time
- Drew Breunig, "10 Lessons for Agentic Coding" — https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html — Lesson 8: as agent output volume outpaces external feedback, taste becomes the primary quality gate; the essay this pattern distills most directly

## Related

- `patterns/find-the-hard-stuff.md`
- `patterns/agents-amplify-experience.md`
- `patterns/eval-driven-development.md`
- `patterns/leverage-over-efficiency.md`
- `patterns/coaches-and-players.md`
- `patterns/build-five-to-throw-away.md`
