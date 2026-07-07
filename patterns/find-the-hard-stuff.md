---
title: Find the Hard Stuff
one_liner: Deliberately seek the genuinely difficult parts of a problem — where the real work lives is almost never where it looks like it should be.
dimensions: taste
---

## What it is

Every problem has a surface difficulty and a real difficulty. The surface difficulty is what it looks like from the outside: a thing that needs to be built, a question that needs answering, a system that needs fixing. The real difficulty is what you discover after you start: the constraint you didn't know existed, the dependency that doesn't compose well, the edge case that breaks the clean model. Developers and AI agents alike are pulled toward the tractable parts — the parts that can be demonstrated quickly, that produce visible results, that fit neatly into existing patterns. The hard stuff lives elsewhere. Finding it requires active effort: you have to deliberately probe the places that feel uncomfortable, ask questions that don't have clean answers, and resist the pull toward the parts that are already well-understood. Taste, in engineering, is largely the ability to notice when you're doing the easy version of a problem and ask whether the hard version is actually what's required. Agents make this discipline more urgent, not less — an agent that optimizes hard on the tractable part will produce a large amount of output that does not touch the real problem.

## When to reach for it

- Before starting any implementation: ask what would make this fail and probe that area first, not the area where you're most confident.
- When early results look too good: visible progress early usually means work is concentrating in the tractable parts; look for what isn't moving.
- When scoping a task for an agent: identify the hard dependency or constraint first and verify it's solvable before generating code that assumes it.
- When debugging: the bug is almost never where you're looking first; ask where you haven't looked.
- When reviewing a design or plan: ask what it silently assumes will work, and verify those assumptions.

## When NOT to

- When the problem genuinely is tractable and the hard version is a different, unrelated problem — seeking difficulty for its own sake wastes time on problems that don't exist.
- When urgency requires shipping what works rather than what's optimal — pragmatic delivery sometimes means explicitly deferring the hard problem and documenting that choice.
- When the hard stuff is hard because it's genuinely out of scope — not every difficulty in the vicinity is the difficulty you need to solve.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: emphasizes that agent failure modes are almost always in the hard interactions at system boundaries (tool use, context management, ambiguous instructions), not in the model's core reasoning — the hard stuff is at the edges, not the center
- Amplifier — https://github.com/microsoft/amplifier — The multi-agent patterns in Amplifier emerge from repeated contact with the genuinely difficult parts of agent orchestration: context limits, delegation economics, state handoff — not from upfront architectural speculation
- Drew Breunig, "10 Lessons for Agentic Coding" — https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html — Lesson 6 "The hard work is where the value is": the essay this pattern most directly distills; agents pull attention toward tractable output, making deliberate navigation toward hard constraints essential

## Related

- `patterns/develop-your-taste.md`
- `patterns/implement-to-learn.md`
- `patterns/recon-before-action.md`
