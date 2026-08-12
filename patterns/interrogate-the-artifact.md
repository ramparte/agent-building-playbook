---
title: Interrogate the Artifact, Not the Exit Code
one_liner: Before testing or demoing, verify the artifact itself is the fresh one you built — a zero exit code and a stale deployed function, binary, or process routinely coexist.
dimensions: verification, reliability
---

## What it is

A build or deploy pipeline reports on its own completion, not on what the consumer will actually run. Those are different facts, and the gap between them is one of the most reliable ways an agent ends up debugging a bug that no longer exists — or demoing a fix that was never loaded. A deploy can partially succeed and still exit 0, leaving one function updated and another silently skipped. `open` on macOS refocuses the already-running stale instance instead of launching the fresh build. A video player keeps serving frames from the pre-render copy of a file it already has open. A dev server serves its last good compile after the new one failed, or a bundler serves a wedged transform cache that cites code no longer on disk. In every one of these cases the pipeline's own signals — exit codes, "deploy complete" banners, the file's presence on disk — all say success, and the thing in front of the user is still old.

The pattern is to treat the artifact as a witness and interrogate it directly for identity and freshness before drawing any conclusion from its behavior. Ask the deployment platform for the function's actual update timestamp rather than trusting the deploy log. Grep the running binary for the new symbol you just added — if it isn't in there, you are not testing your change. Kill every stale process before relaunching, and make quit-and-relaunch a routine step rather than a debugging discovery. When a tool's error message references code that does not match the file on disk, distrust the tool's cache before distrusting the file. The question is never "did the pipeline say it worked?" but "is the thing that will be exercised the thing I just made?"

This is the concrete, pre-test half of independent verification: verify-independently establishes that "done" is a claim needing outside evidence; this pattern says the first piece of outside evidence to collect is the artifact's own identity, because every subsequent test result is meaningless if you are exercising the wrong artifact.

## When to reach for it

- Immediately after any build, deploy, or render, before running the first test against the result — especially when the next step is showing it to a human.
- When a fix "didn't work": before revisiting the diagnosis, confirm the fix is actually present in the running process, deployed function, or served bundle.
- When a deploy log was noisy, truncated, or retried — partial success with exit 0 is common; query the platform for each artifact's update time instead.
- When relaunching a long-lived app or player — assume a stale instance or cached copy is still holding the old version until you have killed it.
- When an error message cites code that doesn't match what is on disk — suspect a transform or compile cache and rebuild clean before touching the source.

## When NOT to

- Ephemeral one-shot executions where the artifact cannot be stale — a script run directly from the source file you just edited has no identity gap to check.
- Pipelines that already verify freshness structurally — immutable, content-addressed deploys where the running version hash is checked automatically make a manual interrogation redundant.
- Don't let it become ritual paranoia on every trivial iteration of a fast, proven-honest loop; apply it at the boundaries where a consumer (test, demo, user) is about to rely on the artifact.

## Exemplars

- Session history — askkaya project, session a4a7867f (2026) — deploy exited 0 despite 429 retries; querying deployed state via gcloud showed the function "was NOT updated by this deploy," and the installed app's binary had "0 references to cliAskStreamApi"
- Session history — askkaya project, session a6d5f567 (2026) — a relaunch "had silently used a stale binary because the build ran from the wrong folder"; the fix was verifying the new code "is actually inside the running binary" and killing every app process first
- Session history — askkaya project, session 2e48cbbe (2026) — "`open` just refocused the old instance instead of loading the new build"; quit-first relaunch became a routine step across roughly ten cycles
- Session history — askkaya project, session e070ad52 (2026) — dev server "served the last good compile, which didn't have section 4"
- Session history — montreal project, session f835ca51 (2026) — user's player showed a stuck frame; decoding all 1,161 frames proved "the file itself is fine... your player is holding a stale copy"
- Session history — sunday-money project, session 9d54acbc (2026) — Metro's error frame "doesn't match the file on disk"; a wedged transform cache, fixed twice by clean rebuild

## Related

- `patterns/verify-independently.md`
- `patterns/fail-loud-harnesses.md`
- `patterns/real-environment-execution.md`
