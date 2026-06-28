---
title: Tests Are Code — Update Them First on API Change
one_liner: When an API changes, update its tests before updating its implementation — the tests are the specification, and updating them first forces you to define what the change means before you build it.
dimensions: verification, workflow-discipline
---

## What it is

Tests are not annotations on working code — they are executable specifications of what the code is supposed to do. When an API changes, the tests express the new contract. Updating the tests first — before touching the implementation — forces a concrete decision about what the changed API should do, surfaces the callers that will break (because the test updates reveal them), and produces a failing test suite that guides the implementation. The alternative order — change the implementation first, then update the tests to match — allows the implementation to define the spec rather than the spec defining the implementation. This is the primary way that tests accumulate "test drift": the tests describe what the code does, not what it should do, and they never catch the difference. Updating tests first on API change is the same discipline as writing tests before code in TDD, applied to the modify case: the test is the spec, and the spec precedes the build. It also produces a clear commit boundary — "update tests to reflect new API shape" is a reviewable artifact that says what the change is before "update implementation to match new spec" says how the change was made.

## When to reach for it

- Any time an API signature changes (parameters added, removed, renamed, or retyped) — update callers' test expectations first, then update the implementation, then verify that callers not yet updated are caught by the newly failing tests.
- When refactoring an interface: write the tests against the intended post-refactor interface first, verify they fail against the current implementation, then do the refactor until they pass.
- When fixing a bug that is caused by incorrect behavior: write a test that proves the current behavior is wrong (it fails), then fix the implementation until the test passes. Do not fix first and add a regression test after.
- When reviewing another person's API change: ask whether the tests were updated before the implementation. If not, the tests describe what was built rather than what was intended.
- When the test suite is stale and not running in CI: the first task is to make it run, not to skip tests. Tests that cannot run are not tests — they are comments.

## When NOT to

- When tests are not yet written for the API being changed — in that case, write tests for the current behavior first, then update them for the intended new behavior, then implement. Do not skip to implementation.
- When the change is a pure internal refactor with no observable behavior change — the tests should not change and should continue to pass throughout. If the tests change during a refactor, the refactor is also changing behavior.
- When the API being changed has no tests and cannot be tested without significant infrastructure work — prioritize building the infrastructure so the discipline can be applied, rather than making an unprincipled exception.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: treats evals as specifications — "your eval suite is your specification, and it should be updated to reflect your intent before your system is updated to implement it"
- Amplifier — https://github.com/microsoft/amplifier — the superpowers TDD discipline: "write the failing test first" applied in the modify case is "update the test to reflect the new contract first, then update the code to pass the test"

## Related

- `patterns/eval-driven-development.md`
- `patterns/test-what-not-how.md`
- `patterns/keep-specs-in-sync.md`
