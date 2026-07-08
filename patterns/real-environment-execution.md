---
title: Run Real Workloads in Their Proper Environment
one_liner: Agents that run workloads in simulated or sandboxed environments discover only simulated problems — run the real thing in the real place if you want real answers.
dimensions: observability
---

## What it is

An agent that tests a deployment by running it against a mock, a stub, or a reduced local facsimile is not testing the deployment — it is testing the mock. The environment is load-bearing. Production systems depend on specific network topology, real service versions, actual resource constraints, real latency, and the accumulated configuration drift of a system that has been running for months. None of these show up in simulation. An agent that executes workloads in the proper environment discovers issues that are invisible in any other context: the service that works under low load but falls apart under realistic concurrency; the file path that exists on the real machine but not in the CI image; the API response shape that changed in a minor update but whose test double was never updated. Running workloads in their proper environment is not a preference — it is the only way to generate evidence that carries information about the real system. Simulated runs generate confidence, not knowledge.

## When to reach for it

- When verifying that a deployment actually serves traffic: run a real request through the real stack, not a synthetic assertion that the service started.
- When performance characteristics matter: benchmarks run outside the target environment measure the wrong machine, the wrong memory bus, and the wrong contention patterns.
- When integration between services is the question: integration issues manifest in the real network, not in local mocks that bypass serialization, authentication, and routing.
- When debugging production failures: reproduce the failure in an environment that matches production. Diagnosing a production crash in a local development environment is hypothesis generation, not debugging.
- When evaluating agent tool output: if an agent's tool runs a command, that command should run against the actual target system — not a local approximation — before the output is used to make decisions.

## When NOT to

- When the real environment is destructive to use for testing — against production databases, live financial systems, or shared infrastructure where a test run causes real effects. Use staging environments that are structurally identical but isolated.
- When the proper environment is unavailable during early development and a local approximation is the only option — accept that early results are provisional and flag them as such; do not treat them as evidence about the real system.
- When the cost of running real workloads in the real environment is prohibitive relative to the value of the test — proportionality applies. Not every code change needs a full end-to-end production replica run.
- When the environment itself is the subject of a configuration change and running real workloads would corrupt state before the change is verified.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: emphasizes that agents should gain ground truth from the environment at each step — tool call results and code execution output — to assess actual progress
- Amplifier — https://github.com/microsoft/amplifier-bundle-digital-twin-universe — the Digital Twin Universe bundle stands up complete, isolated container environments on demand that 'simulate the world the code will live in' — the code itself runs for real, with external services mocked as sidecar containers — so an agent can clone, install, run, and experience a change like a real user before production; a deliberate approximation of the proper environment, not the environment itself
- Adam Wiggins, "The Twelve-Factor App: X. Dev/Prod Parity" — https://12factor.net/dev-prod-parity — the canonical 2011 articulation: "Keep development, staging, and production as similar as possible"; the foundational SE principle this pattern applies to agent workload environments
- Cindy Sridharan, "Testing in Production: the hard parts" — https://copyconstruct.medium.com/testing-in-production-the-hard-parts-3f06cefaf592 — extends dev/prod parity to distributed systems; argues that many failure modes are invisible outside real distributed systems, and that blast radius management — not avoidance — is the right response to running real workloads in real places

## Related

- `patterns/evidence-before-assertions.md`
- `patterns/self-verification.md`
- `patterns/emit-events.md`
