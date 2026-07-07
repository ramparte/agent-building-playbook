---
title: Fix the Root Cause, Demand a Diagnosis
one_liner: Agents tend to patch the visible symptom without pulling the thread to the cause — for recurring, production, or architecture-level issues, require a diagnosis artifact that explains the root cause before any fix is accepted.
dimensions: reliability, verification, workflow-discipline
---

## What it is

Left to their own momentum, agents fix bugs in isolation: they find the visible symptom, make it go away with the smallest local change, and report success — without ever pulling the thread back to the cause. This is not laziness; it is the default behavior of a system optimizing to make the failing signal stop, and a symptom patch makes the signal stop just as effectively as a real fix, right up until the cause resurfaces somewhere else. The countermeasure is to refuse to accept a fix on the strength of "the symptom is gone" and instead require a diagnosis artifact: an explicit account of why the failure happened — the actual mechanism, not the surface — that precedes and justifies the fix. The diagnosis names the root cause, explains how it produced the observed symptom, identifies what else the same cause could affect, and only then proposes a change addressed to the cause rather than the surface. This discipline is not free, so it is applied where the cost of a recurring symptom is high: issues that recur (the same bug keeps coming back under new disguises), issues found in production (where the blast radius of a misdiagnosis is real users), and issues at the architecture level (where a local patch can entrench a structural flaw). For a one-off cosmetic glitch a direct fix is fine; for a bug that has now appeared three times, demanding the diagnosis is what converts an endless stream of patches into a single durable fix. The artifact also pays forward — a written root-cause diagnosis is exactly the kind of evidence a future agent or human needs to understand why the system behaves as it does.

## When to reach for it

- When the same bug, or the same class of bug, keeps recurring — recurrence is the signal that prior fixes hit symptoms, not the cause.
- When a defect is found in production, where misdiagnosing the cause means the real failure is still live and waiting to resurface.
- When the issue touches architecture-level behavior, where a local patch can paper over and entrench a structural flaw.
- When an agent proposes a fix that makes the symptom disappear but cannot explain why the symptom occurred — require the diagnosis before accepting the change.
- When you want fixes to compound into durable institutional knowledge — a recorded root-cause diagnosis is reusable evidence, not just a closed ticket.

## When NOT to

- For genuinely one-off, low-stakes, cosmetic issues where the symptom and the cause are the same thing and a direct fix is obviously correct.
- When the cost of full root-cause analysis exceeds the cost of the failure and the failure is cheaply reversible — proportion the rigor to the risk.
- During time-critical incident response where stopping the bleeding comes first — apply the symptom mitigation now, but schedule the root-cause diagnosis as required follow-up rather than dropping it.

## Exemplars

- Toyota / Taiichi Ohno — https://en.wikipedia.org/wiki/Five_whys — the "five whys" practice of repeatedly asking why until the chain reaches the root cause rather than stopping at the first visible symptom
- Lunney & Lueder, "Postmortem Culture: Learning from Failure" — https://sre.google/sre-book/postmortem-culture/ — applies the pattern at organizational scale: Google SRE's blameless postmortem practice requires a written root-cause diagnosis before closing any incident, structurally preventing symptom patches from being accepted as complete fixes

## Related

- `patterns/session-archaeology.md`
- `patterns/demand-independent-proof.md`
- `patterns/production-feedback-loop.md`
