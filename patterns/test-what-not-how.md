---
title: Test What the Product Does, Not How
one_liner: Tests that describe externally observable behavior survive refactoring; tests that describe internal implementation become a maintenance tax that grows with every change.
dimensions: verification
---

## What it is

A test that checks how the system achieves an outcome is coupled to the implementation — when the implementation changes, the test breaks even if the behavior is still correct. A test that checks what the system does from the outside is decoupled from the implementation — it only breaks when the behavior changes, which is when it should break. The distinction is not subtle: "assert that this function was called with these arguments" is a how-test; "assert that after calling this API, the database contains this record" is a what-test. What-tests describe the product's observable contract. How-tests describe the product's current internal wiring. Agentic systems fail this discipline most visibly because agents are opaque — their internal reasoning is not inspectable — which tempts developers to test the tools the agent called rather than the outcome the agent produced. Testing which tools an agent called is a how-test. Testing whether the artifact the agent was supposed to produce exists, is correct, and is usable is a what-test. The former breaks whenever tool implementations or selection logic changes; the latter breaks only when the agent stops doing its job.

There is a sharper risk when the tests themselves are agent-generated. A test the agent writes against code the agent wrote can overfit to the implementation it happens to see, or encode the very same misunderstanding that produced the code — in which case the test passes, the code is wrong, and the test certifies the bug. More tests do not fix this; they can multiply the shared blind spot. Each test type carries its own version of the failure, and a finishing system should treat the choice as a tradeoff rather than a default: unit tests can overfit to implementation detail; integration tests are often brittle; end-to-end tests are slow and flaky; mutation tests are costly and noisy; property tests are only as good as the invariants they assert; adversarial tests are easy to under-specify; visual tests need good baselines and tolerances. The agentic opportunity is therefore not merely to write more tests. It is to make test generation, critique, execution, and revision into nodes of the workflow graph — so a separate critic challenges the tests, the suite is actually run against real behavior, and failures feed back into revising both the code and the tests, rather than a single agent grading its own homework.

## When to reach for it

- When writing tests for any function, agent, or pipeline step: identify the externally observable outcome first, write the assertion against that, then verify the test fails before adding implementation.
- When tests are frequently breaking due to refactoring even though behavior has not changed — this is the signature of how-tests; replace them with what-tests.
- When testing agentic behavior: define the artifact the agent should produce (file written, database state, API call made with the right payload to an external system) rather than the sequence of internal tool calls.
- When a codebase has tests but developers still fear refactoring — the tests are almost certainly how-tests. Rewriting them as what-tests restores the safety they were supposed to provide.
- When debugging a system with high test pass rates but unreliable production behavior — how-tests pass easily because they test internal consistency, not external correctness.

## When NOT to

- When the implementation detail IS the observable behavior — in performance-critical code where the number of database queries is the externally contracted guarantee, testing the query count is a what-test, not a how-test.
- When you are specifically testing integration paths and need to verify that a particular external service was called (rather than that the effect of the call occurred) — in that case the call is the observable contract, not an implementation detail.
- When testing security properties that are inherently about what the system does NOT do — absence of certain calls or state changes is a valid what-test.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends evaluating agents on task completion (did the agent finish the task correctly?) rather than on process (did the agent call the right tools in the right order?), because task completion is the product's actual contract
- Amplifier — https://github.com/microsoft/amplifier-bundle-superpowers — the superpowers verify mode checks real command output, not whether the agent reported that it ran the right commands — "Run the command. Read the output. THEN claim."
- Kent C. Dodds — https://kentcdodds.com/blog/testing-implementation-details — origin: names and argues the harm of testing implementation details; "the more your tests resemble the way your software is used, the more confidence they can give you" (2020)
- Freeman & Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — https://www.informit.com/store/growing-object-oriented-software-guided-by-tests-9780321503626 — classic antecedent: "unit-test behavior, not methods" — outside-in acceptance tests as the primary design driver, not internal state

## Related

- `patterns/eval-driven-development.md`
- `patterns/evidence-before-assertions.md`
- `patterns/demand-independent-proof.md`
