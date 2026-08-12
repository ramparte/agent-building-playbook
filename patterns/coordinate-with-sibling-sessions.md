---
title: Treat Sibling Sessions as First-Class Constraints
one_liner: Another session sharing your working tree is not under your control — detect it, avoid its hot files, isolate in a worktree, hold merges, and audit shared state.
dimensions: orchestration, workflow-discipline
---

## What it is

A sibling session is another agent — or the human themselves — working in the same repository at the same time, from a separate conversation you did not start and cannot steer. This makes it categorically different from a subagent. A subagent runs on your briefing: you scope its files, you read its report, you decide when its work lands. A sibling has its own operator, its own task list, and its own idea of what the working tree should look like. You cannot brief it, pause it, or read its intentions; you can only observe its effects. Coordinating with one is therefore not a delegation problem but a concurrency problem, and the discipline is defensive. First, detect: when concurrent work is possible or the human hints at it, actually check for other live sessions (a `ps` scan for other agent processes) rather than assuming you are alone. Second, maintain an explicit do-not-touch list — the hot files the sibling is known to be editing — and keep it current as the sibling moves ("the onboarding agent is editing AppOnboardingView now — I'll stay off it"). Third, do your own work in an isolated git worktree, so that even if your model of the sibling is wrong, you physically cannot clobber its uncommitted state. Fourth, hold merges and extractions until the sibling's pushes land: integrating against a branch that is about to move is how conflicts get manufactured. Fifth, audit shared state after any background agent finishes, because agents tangle with shared git plumbing in ways their own reports miss — in one observed incident, an agent's stash operation left a stray staged diff on a file entirely outside its assignment, discovered only by a post-hoc verification pass. And throughout, re-read any file immediately before editing it; the copy in your context may already be stale.

## When to reach for it

- When the human mentions, or you detect, another live coding session on the same repository — from that moment every file is potentially contested and the defensive posture applies.
- When the human says they may push changes from elsewhere mid-task — hold your merges and rebases until those pushes land rather than racing them.
- When a background agent has just finished in a shared tree — audit the tree's known-good state (staged diffs, stash residue, files outside the agent's assignment) before building on top of it.
- When you are about to edit a file you read a while ago and parallel work is in play — re-read it first; composing cleanly with a sibling's edits requires seeing them.
- When your work can tolerate isolation — an isolated worktree converts "I believe we won't collide" into "we cannot collide."

## When NOT to

- When the "other agents" are subagents you spawned — those are under your control, and the right tools are briefings, file partitions, and serialized commits, not detection and defense.
- When you have verified you are the only session and the human is not editing — worktree ceremony and hot-file bookkeeping for a sibling that does not exist is pure overhead.
- When the sibling's work and yours genuinely must interleave in the same files — defensive isolation cannot resolve that; escalate to the human to serialize the tasks or hand one session the whole file.
- When the shared state is not a working tree at all (separate repos, separate deploy targets) — there is no contested resource, so coordinate at the merge boundary instead.

## Exemplars

- Session history — askkaya project, session 364f9218 (2026) — user asked "can u check for any other claude code sessions right now?" and warned of pushes from another session; the agent stopped its own subagents, kept an explicit do-not-touch list (api/ask.ts, generation.ts, rag-v2.ts — "another agent is editing them"), and moved to an isolated worktree "so I can't clobber them regardless"
- Session history — askkaya project, session ea9d9a0c (2026) — a background agent "tangled with a git stash touching uaskme/page.tsx"; a post-hoc audit found the file content-correct but carrying a stray staged diff from the stash tangle, which was reset clean; the agent also tracked the sibling's moving hot file ("the onboarding agent is editing AppOnboardingView now — I'll stay off it")
- Session history — sunday-money project, session ea3205a0 (2026) — a subagent reported "a parallel session was editing the repo concurrently... I re-read affected files before touching them and my changes compose cleanly with theirs"

## Related

- `patterns/partition-files-serialize-commits.md`
- `patterns/supervise-many-agents.md`
- `patterns/recon-before-action.md`
- `patterns/single-threaded-default.md`
