---
title: Partition by File Ownership, Serialize the Commits
one_liner: Parallelize agents only along disjoint file ownership, bind them with one shared written contract, let many read while exactly one commits, and reconcile the joints where outputs meet.
dimensions: orchestration
---

## What it is

"Independent enough to parallelize" is usually asserted, rarely tested. This pattern replaces the assertion with a concrete test: two agents may run concurrently if and only if the sets of files they will write are disjoint. Partition the work by exclusive file ownership up front, and integration stops being a judgment call — the merges are mechanical, and "all three merged cleanly into main, zero conflicts" is the expected outcome rather than a lucky one. If you cannot draw the partition, you have not decomposed the task yet; the failure to find disjoint file groups is itself the signal that the work is sequential.

The write partition is only half the rule. Reads are free: any number of read-only agents — reviews, audits, explorations — can run alongside the writers without joining the partition at all. Writes to the repository, however, are serialized to exactly one committing agent at a time; the next writer is held until the current commit lands, avoiding a git race where two agents mutate the tree simultaneously. N readers, one committer.

Disjoint files keep agents from colliding, but nothing yet makes them converge. That is the job of a shared written contract: a single artifact — a style contract file, a spec — that every parallel agent works from, plus a uniform finding schema so their outputs are mergeable rather than merely coexistent. In one session, four audit agents each covered about sixteen of an app's sixty-three view files and every finding came back in the same shape — file:line, current string, violated rule, suggested rewrite — so the fix agents that followed could consume all four reports identically. The brief also needs a conservative default for ambiguity: "if unsure, keep and flag." A sweep agent that deletes on doubt destroys information silently; one that keeps and flags routes the judgment call back to the caller, and the flagged keeps ("LEFT PER CONTRACT'S 'if unsure' rule") become a reviewable list instead of an invisible loss.

Finally, treat the joints as work. Agents built from the same spec still drift at the serialization level: in one run, a backend agent shipped `lastAskedAt` as an ISO string where the app agent expected epoch milliseconds, and `curatedAnswer` as an object where the app expected a plain string. The spec agreed; the wire did not. So the seams where parallel outputs meet get a mandatory reconciliation pass, and the orchestrator runs the authoritative verification on the combined tree itself — each agent's local green means nothing about the composition.

## When to reach for it

- Fanning a large mechanical change (style sweep, audit-and-fix, migration) across many files that cluster into disjoint groups.
- Multiple agents producing components that must interoperate — a backend and a frontend built from one spec — where the joint needs explicit reconciliation.
- You want concurrent reviews or explorations while implementation proceeds: readers scale freely; only the committer slot is contended.
- N agents' findings must be aggregated afterward — the uniform schema is what makes the merge a concatenation instead of a translation project.

## When NOT to

- The work does not partition: the same hot files sit on every path. Forcing a partition produces artificial seams; run it single-threaded instead.
- The task is one deep, stateful chain of edits where each step depends on the last — decomposition overhead buys nothing.
- Other sessions you do not control share the working tree; ownership you cannot enforce is not ownership (see coordinate-with-sibling-sessions).
- The overhead of writing the contract and schema exceeds the job — for two agents touching three files, a sentence of instruction suffices.

## Exemplars

- Session history — askkaya project, session 2e48cbbe (2026) — work partitioned by file ownership so agents "can run in parallel without colliding"; all three branches merged into main with zero conflicts because the partition held
- Session history — home project, session adc2776c (2026) — four audit agents over disjoint slices of 63 view files, all returning the same file:line / current / violated-rule / rewrite schema; four fix agents on disjoint groups from one written style contract, with "if unsure, keep and flag" keeps surfaced to the caller
- Session history — askkaya project, session 364f9218 (2026) — two writers in flight with no file overlap; a third task held "until it lands to avoid concurrent commits" while a read-only review ran freely alongside
- Session history — askkaya project, session a6d5f567 (2026) — same-spec agents drifted at the wire (ISO string vs epoch ms, object vs plain string); concurrent touches to index.ts forced verification of the merged build before proceeding
- Session history — sunday-money project, session ea3205a0 (2026) — work split into three disjoint clusters for parallel agents, followed by the authoritative verification run on the combined tree

## Related

- `patterns/coordinate-with-sibling-sessions.md`
- `patterns/parallel-independent-tracks.md`
- `patterns/clean-slate-delegation.md`
- `patterns/adversarial-parallel-review.md`
- `patterns/single-threaded-default.md`
- `patterns/supervise-many-agents.md`
