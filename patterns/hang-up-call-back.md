---
title: Hang Up, Call Back
one_liner: When an agent conversation goes down the wrong path, don't course-correct — rewind history and re-prompt so the model never sees the bad idea.
dimensions: context-engineering, workflow-discipline
---

## What it is

When a session heads down a fundamentally wrong path, the instinct is to correct it in place: explain what's wrong, redirect, keep the conversation going. This usually fails, for two reasons. First, the rejected approach stays alive in context — the model anchors on those tokens and keeps drifting back toward the bad design no matter how firmly you correct it. Second, the dead-end transcript burns context budget, so even a correction that sticks leaves the fresh attempt running with less room and degraded attention.

The fix is what you do when a customer service call goes off the rails: hang up and call back. The next agent has no memory of the botched call, and you now know exactly how to phrase your ask. In an agent session the move is a rewind, not a fresh start — roll the conversation back to before the wrong turn, keeping everything that was still on track, and re-prompt from there. The learning from the failed path survives in the re-prompt: a revised prompt that encodes what you now know, or a changed success criterion that redefines what done means. The bad transcript itself dies. The model that does the real work never sees the bad idea and is never polluted by the wrong tokens.

## When to reach for it

- When the approach is fundamentally wrong, not sloppily executed — a bad design premise, a misread requirement, a wrong architecture.
- When corrections keep failing to stick: you redirect, the model complies briefly, then drifts back toward the rejected approach.
- When you have gone far enough down the path to know what you would say differently from the start — the failure is legible enough to encode in a re-prompt.
- When multiple corrections have accumulated and the context is now a layered argument with the model rather than a clean statement of the task.

## When NOT to

- For small, local mistakes — a wrong variable name, a missed edge case, a style issue. Corrections that don't invalidate the design are cheap; rewinding throws away good context for nothing.
- When the path hasn't taught you anything yet. If you can't articulate what you would prompt differently, you have nothing to encode in the rewind — keep going until the failure is legible.
- When the session isn't wrong, just full. Context exhaustion on a healthy path is a handoff problem, not a rewind problem — see `patterns/checkpoint-handoff-file.md`.

## Exemplars

- Claude Code `/rewind` (double-escape) — first-class support for rewinding the conversation to an earlier point and editing the prompt, rather than appending a correction.
- Drew Breunig — https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html — "How Long Contexts Fail" (June 2025): names context poisoning — when a hallucination or error embeds in context and compounds across steps — as the failure mode this pattern addresses; parallel identification of the same root problem from practitioner observation

## Related

- `patterns/clean-slate-delegation.md`
- `patterns/checkpoint-handoff-file.md`
- `patterns/implement-to-learn.md`
- `patterns/build-five-to-throw-away.md`
