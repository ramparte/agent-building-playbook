---
title: Nonce-Tag Synthetic Test Data
one_liner: Every synthetic record an agent injects into a live system carries a unique searchable token, so it can be found, scoped, dry-run deleted, and provably purged to zero.
dimensions: verification, reliability, workflow-discipline
---

## What it is

Agents that test against real systems constantly create synthetic entities — probe documents, fake workspaces, timing entries, invite-flow test users. Untagged, these probes are indistinguishable from real data. They leak into user-facing surfaces, pollute search results, and become unfindable the moment the session that created them ends. The user discovers them as junk in production; the agent has no reliable way to enumerate what it made.

The pattern is to stamp every synthetic record with a unique nonce — an improbable token like `ZARDOZ` or a `ZZ-verify-` prefix — chosen so that it cannot collide with any real data in the store. The nonce buys the whole cleanup lifecycle, and the lifecycle is the point:

1. **Mint the nonce** before injecting anything, and put it in every field a search can reach.
2. **Grep-scope** the entire store for the token to enumerate exactly what the test created — nothing more, nothing less.
3. **Print every match** for review before touching anything, so a human or the agent itself can confirm the scoping caught only test data.
4. **Dry-run the delete** against that reviewed match list.
5. **Delete.**
6. **Verify zero** — re-run the same search and confirm it returns no matches. "Cleaned up" is a claim; zero matches is evidence.

There is a bonus effect: disciplined cleanup is itself a test. The delete pass exercises deletion paths that normal testing never touches, and an entity that refuses to die is a real bug, found for free.

## When to reach for it

- Any time an agent injects test entities into a live or production system — a knowledge base, a CRM, a user directory, a message queue — where real data lives alongside the probes.
- End-to-end tests of create/invite/signup flows that necessarily write real records to prove the flow works.
- When a previous session's test data has already leaked into a user-facing surface and you need to purge it with confidence that you removed all of it and only it.
- When multiple agents or sessions probe the same store — per-session nonces make each session's residue separately enumerable.
- When the blast radius of a cleanup matters: a delete scoped to a unique token cannot touch real records, no matter how the query is otherwise written.

## When NOT to

- Ephemeral test environments that are wholesale destroyed after the run — a database that gets dropped needs no per-record tagging.
- Systems with first-class test-data isolation (sandbox tenants, test-mode flags, separate staging stores) — use the structural boundary instead of a string convention.
- Data the test must make indistinguishable from real data by design, such as an eval of a spam classifier — tagging would contaminate the measurement; isolate at the environment level instead.
- Read-only probes that write nothing — there is nothing to purge.

## Exemplars

- Session history — askkaya project, session ea9d9a0c (2026) — user screenshot of junk "timing probe" entries in the live knowledge base; agent tightened the scoping to the unique ZARDOZ token, printed each match for review before deleting, deleted all 16, then re-searched: "Clean — 0 matches."
- Session history — askkaya project, session 2e48cbbe (2026) — end-to-end invite-flow test against production with all test data ZZ-verify-prefixed; the three real workspaces were untouched, and the cleanup pass surfaced a real bug — a team twin that could not be deleted via the API.

## Related

- `patterns/real-environment-execution.md`
- `patterns/auditable-artifacts.md`
- `patterns/verify-independently.md`
