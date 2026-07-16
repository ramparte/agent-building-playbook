---
title: Don't Pipe Verification Through Lossy Filters
one_liner: A check whose signal passed through tail, head, or any truncating filter is not a valid check — run verification commands raw and capture exit codes explicitly.
dimensions: verification, observability
---

## What it is

Agents under context pressure develop a reflex: pipe long command output through `tail -40` or `head -100` so a noisy build log doesn't flood the window. For exploration, this reflex is correct — you are sampling, and any representative slice will do. But at the moment of proof, the same reflex silently destroys the evidence the command exists to produce, through four distinct mechanisms.

First, **exit code masking**: in a shell pipeline, `$?` reflects the last command in the pipe. `npm run build | tail -40` reports `tail`'s exit status — which is success — regardless of whether the build failed. The one bit of information the verification was supposed to yield is overwritten by the filter itself. Second, **evidence truncation**: the failing test, the function that didn't deploy, the error three hundred lines up — these land in exactly the portion of output the filter discards. A deploy summary that fits in forty lines is precisely the kind of output where the one anomalous line falls outside the window. Third, **buffering distortion**: piped output is often block-buffered rather than line-buffered, so a long-running command shows nothing until it completes — the agent stares at silence, misreads it as a hang or a pass, and acts on the misreading. Fourth, **signal consumption**: a `head` pipe closes its input after N lines, and can eat the very message you were waiting for — a server's "ready" line — or kill the producing process with SIGPIPE.

The discipline: when a command's purpose is to prove something, run it raw. If the output is genuinely too large for context, `tee` it to a file, then read the file — the file is complete and re-inspectable; the pipe slice is gone forever. Capture the exit code explicitly (`echo "exit: $?"` immediately after, or `set -o pipefail` if a pipe is unavoidable) rather than inferring success from whatever fragment survived the filter. The distinction to hold is not "long output vs. short output" but "am I exploring or am I proving?" Context thrift is a virtue in the first mode and evidence destruction in the second.

## When to reach for it

- Any command whose output you are about to cite as proof: the final build before claiming "it compiles," the deploy that precedes "it shipped," the test run behind "all green."
- When a verification "passed" but downstream behavior contradicts it — check whether the passing signal ever actually reached you, or whether a filter manufactured it.
- When waiting on a readiness signal (server start, migration completion) — filters and buffering can delay or consume the exact line you're polling for.
- When writing agent harnesses or skills that run checks: build in the tee-to-file-then-read pattern so the agent never has to choose between context budget and evidence integrity.

## When NOT to

- Exploration and reconnaissance. Skimming a log to get oriented, sampling a file's shape, checking whether output is roughly what you expect — `tail` and `head` are exactly right here, and refusing to truncate would waste context on noise. The pattern governs the moment of proof, not every command.
- Commands whose full output genuinely fits in context — there is nothing to filter, so run them raw and read everything.
- Filters that select without discarding the verdict: `grep -c FAIL` on a completed, tee'd log file is fine, because the complete artifact still exists and the exit status was captured separately.

## Exemplars

- Session history — askkaya project, session a4a7867f (2026) — "The piped `tail -40` truncated the log, so I can't see cliAskApi or the final summary": the deploy evidence needed was exactly what the filter removed
- Session history — askkaya project, session a6d5f567 (2026) — a reviewing subagent flagged that "my earlier interim build piped through `tail`, masking the exit code, so it wasn't a valid check"
- Session history — askkaya project, session e070ad52 (2026) — "Deploy output is buffered (I piped it through tail), so nothing shows until it finishes"; "the `head` pipe just ate the ready message"

## Related

- `patterns/verify-independently.md`
- `patterns/context-is-finite.md` (the tension this pattern resolves)
- `patterns/auditable-artifacts.md`
- `patterns/evidence-before-assertions.md`
- `patterns/interrogate-the-artifact.md`
- `patterns/baseline-the-broken.md`
