---
title: Baseline the Broken Before Claiming "No New Failures"
one_liner: In a repo that already fails, "my changes are clean" is unprovable — capture the failure baseline first, then verify your diff against it, not against zero.
dimensions: verification, workflow-discipline
---

## What it is

Brownfield repositories are rarely green. They arrive with pre-existing red tests, standing type errors, and lint noise that predates the current session. There, the acceptance criterion "the suite passes" is unreachable, and "my changes are clean" is unfalsifiable — clean compared to what? An agent that runs the tests after its edit, sees 46 failures, and declares them "probably pre-existing" is guessing. An agent that saw the same 46 failures with the same signatures *before* it touched anything is proving. The pattern makes the working acceptance criterion "no new failures," and earns the right to claim it by capturing the baseline as the very first act.

The mechanism is a concrete maneuver, and its concreteness is the point. Before verifying your work: `git stash` your changes, run the full suite (or typecheck, or build) on the untouched tree, and record the failure signature — not just the count, but which suites, which errors, which files. Then `git stash pop`, re-run the identical command, and diff the two signatures. If they match exactly, your change added nothing; if a new failure appears, it is yours by construction, no matter how unrelated it looks. The stash step matters because it removes the only confound: the same machine, the same dependencies, the same command, differing in exactly one variable — your diff. Without it, "those failures were already there" is an assertion; with it, it is a measurement.

The signature comparison is what makes the claim honest rather than merely plausible. Counts alone can lie — a change that fixes one pre-existing failure and introduces a new one produces an identical count with a different meaning. One 247-file documentation pass was accepted on the evidence "tsc total: 28 errors — identical to the pre-pass baseline," plus the check that all 28 were pre-existing and none touched the newly added files. Locating the surviving errors *away* from the new work is the difference between a matching number and a matching signature.

The pattern also changes how delegated work gets verified. A subagent claiming its changes are clean should demonstrate the baseline maneuver itself — stash, clean-tree run, comparison — rather than assert cleanliness, and an orchestrator can re-run the comparison independently. The baseline turns a trust relationship into a checkable one.

## When to reach for it

- Before any change in a repository whose tests, typecheck, or build already fail — capture the baseline before your first edit, while the tree is still trivially clean.
- When you finished a change without a baseline and now face failures of unknown provenance — stash, run on the unmodified tree, and prove which failures are pre-existing.
- When accepting a subagent's or contributor's "no new failures" claim — demand the before/after signature diff, or reproduce it yourself.
- When a change should be behavior-neutral (formatting, docs, refactors) — the strongest baseline is byte-identical output before and after.

## When NOT to

- In a genuinely green repo — "the suite passes" is available, strictly stronger, and needs no baseline bookkeeping.
- When the task is to *fix* the pre-existing failures — the baseline is your target list, not your excuse; matching it would mean you did nothing.
- When the environment is nondeterministic enough that the clean tree itself won't reproduce a stable signature (flaky tests, time-dependent failures) — stabilize or quarantine the flakes first, or the diff proves nothing.

## Exemplars

- Session history — sunday-money project, session 9d54acbc (2026) — 247-file doc pass accepted on "tsc total: 28 errors — identical to the pre-pass baseline," with all 28 confirmed pre-existing and none in the new payment files
- Session history — sunday-money project, session ea3205a0 (2026) — agent responded to suspicious failures with "let me prove they're pre-existing with a baseline run on a clean tree"
- Session history — sunday-money project, session f8facff4 (2026) — implementer verified a behavior-neutral change by confirming output byte-identical before and after
- Session history — askkaya project, session ea9d9a0c (2026) — subagent reported "npx jest shows the identical pre-existing baseline (6 suites / 46 tests failing — verified via git stash that they fail the same way on the unmodified tree)... My changes add zero new failures"

## Related

- `patterns/brownfield-is-the-real-test.md`
- `patterns/verify-independently.md`
- `patterns/evidence-before-assertions.md`
- `patterns/demand-independent-proof.md`
- `patterns/interrogate-the-artifact.md`
- `patterns/dont-verify-through-lossy-filters.md`
