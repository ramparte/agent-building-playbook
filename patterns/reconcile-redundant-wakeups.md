---
title: Redundant Wakeups Need Stale-Safe Reconciliation
one_liner: Treat every wakeup as at-least-once delivery — reconcile against durable artifacts first, and declare a redundant trigger stale instead of redoing the work.
dimensions: orchestration, reliability
---

## What it is

When an agent kicks off long background work — a workflow run, a fleet of sub-agents, a CI pipeline — the completion notification is not guaranteed to arrive. Notifications get dropped, sessions end before the callback fires, and schedulers deliver late. The robust response is to schedule redundant fallback wakeups: cheap check-ins that fire whether or not the primary notification arrived. But redundancy converts one failure mode into another. Delivery is now at-least-once, which means most wakeups will arrive *after* the work they guard is already done — and an agent that treats every trigger as fresh instructions will redo completed work, duplicate side effects, or thrash state that a previous invocation already settled.

The pattern is a discipline with two halves. First, redundant triggers are only safe if loop state is reconstructible from durable artifacts — git history, ledger files, report documents, task checklists written to disk. If "where are we" lives only in a context window, a late wakeup has nothing to reconcile against and must guess. Second, every wakeup begins with reconciliation, not action: read the ledger, run `git log`, check whether the report file exists, verify nothing is actually stuck — and if the guarded work is complete, explicitly declare the trigger stale ("everything this is asking about is already done") and stop. The wakeup's job is to verify progress, and verification that finds nothing wrong is a successful, cheap outcome — not wasted effort.

The same discipline applies after context loss. When a session resumes from a compaction or continuation summary, the summary is a lossy notification about the past, not ground truth. Before reporting status or resuming work, audit the working tree: how many commits ahead of origin, what is uncommitted, which files changed. Sessions routinely discover the prior run built more (or less) than the summary recorded. The repo is the ground truth for "where are we"; the summary is just the latest at-least-once message about it.

## When to reach for it

- Any time you schedule a fallback check-in for detached background work — the moment you add the redundant trigger, add the reconcile-first discipline to whatever handles it.
- Long-running multi-phase loops where the same scheduled prompt may fire against different phases — each firing must locate the current phase from artifacts, not assume it.
- Resuming after compaction or a continuation summary — audit git and the working tree before trusting the summary's account of progress.
- Multi-agent orchestration where several completion signals converge on one coordinator — duplicates and stragglers are the normal case, not the exception.

## When NOT to

- Work with no durable artifacts to reconcile against — fix that first; redundant wakeups without reconstructible state are a duplication engine, not insurance.
- Short synchronous tasks where you stay attached until completion — there is no notification to lose, so a fallback wakeup is pure overhead.
- Triggers that carry genuinely new instructions (a human message, a changed spec) — reconcile to establish current state, but do not dismiss the trigger as stale; stale-declaration is for redundant *completion* signals only.

## Exemplars

- Session history — home-directory sessions, session 511791e2 (2026) — scheduled check-ins repeatedly arrived after Tasks 1–7 completed; each was answered by verifying nothing was stuck, then declaring the trigger stale rather than re-running the tasks
- Session history — home-directory sessions, session adc2776c (2026) — fallback wakeup scheduled in case a workflow notification never arrived; the notification did arrive, and the wakeup correctly resolved to "everything it was guarding against is already done"
- Session history — playbook sessions, session 9d77cc45 (2026) — after four mining agents finished and the synthesis was delivered, the fallback wakeup fired anyway and was recognized as firing after the fact, with nothing new to check
- Session history — askkaya sessions, session 2e48cbbe (2026) — post-context-loss variant: audited git ("3 commits ahead of origin, with uncommitted dedup work") before reporting, and discovered the prior session had built more than the continuation summary recorded

## Related

- `patterns/checkpoint-handoff-file.md`
- `patterns/clear-stop-condition.md`
- `patterns/long-horizon-memory.md`
- `patterns/hang-up-call-back.md`
- `patterns/gate-done-with-a-stop-hook.md`
