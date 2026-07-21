---
title: Terseness Is Earned Context
one_liner: In a maturing collaboration, instruction length should fall over time — a rising trend means your context substrate is failing and you're re-explaining what should have been persisted, so fix the substrate instead of writing longer prompts.
dimensions: context-engineering, human-factors
---

## What it is

How many words it takes to give an instruction is a readout, not a style. When the shared context is doing its job — persistent memory, environment files, a stable plan, an established house style, a track record the agent can assume — the human can compress each instruction because the agent already holds the rest. In a 14-month corpus the operator's median prompt fell from 11 words to 8 while the correction rate held flat at roughly 6–7%: he learned to say less without losing accuracy, because the context had moved out of the prompt and into durable substrate. The actionable inversion is the useful half. If your prompts are getting *longer* over a project's life, that is a warning light, not diligence — you are re-explaining, turn after turn, what should have been written down once. The fix is not a better prompt; it is a better substrate. Put the recurring context into memory, a project instructions file, or a spec, and the prompts collapse back to a sentence. Terseness measures how much context you have successfully externalized. This sits in deliberate tension with repeating critical constraints: repeat the few things that must hold across layers, and compress everything the agent already reliably knows. Confusing the two — repeating the known, or compressing the critical — is the mistake the tension is there to prevent.

## When to reach for it

- On long-lived projects or a long-running working relationship, watch instruction length as a health metric for your memory and context setup.
- When you notice yourself re-typing the same background every session — that friction is the signal to move it into persistent substrate.
- When onboarding a new project into an existing practice — invest early in the context files so instructions can stay short from the start.

## When NOT to

- First-contact or one-off tasks, where no shared context exists yet — verbosity is correct until the substrate is built.
- For the handful of constraints that must never be dropped — those get repeated across layers on purpose; brevity is not the goal there.
- High-stakes or irreversible instructions where explicitness beats economy — say it in full even if the agent "should" know.

## Exemplars

- Compression under stable accuracy — 14-month Claude Code session corpus — median prompt length dropped 11→8 words across the window while the correction rate stayed flat, evidence that context moved into substrate rather than instruction.
- Assumed-context openers — same corpus — ~16% of prompts opened with a bare acknowledge-and-redirect ("ok." / "perfect." then the next order), a shape that only works when the agent is trusted to hold everything else.

## Related

- `patterns/context-over-prompt.md`
- `patterns/persist-environment-facts.md`
- `patterns/scope-and-expire-memory.md`
