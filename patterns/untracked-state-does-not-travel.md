---
title: Untracked State Doesn't Travel
one_liner: Isolated copies and redeploys carry only tracked, declared state — enumerate the gitignored-but-required inputs as a set and move config into what the deploy carries.
dimensions: reliability, workflow-discipline
---

## What it is

A repository is not a complete description of a working system. Real builds depend on artifacts that are deliberately gitignored — credentials in a `.env`, generated code, prebuilt frameworks, local certificates — and real deployed services depend on configuration that was set imperatively, by hand, on the running instance. Both are invisible state: the system works where it was assembled, and nothing records what made it work. The failure surfaces the moment state has to travel. A fresh worktree, a clean clone, or a repository extracted for another team carries only tracked files, so every gitignored-but-required input is silently absent; a redeploy or a newly created service instance carries only what the deploy artifact declares, so every manually-set environment variable is silently stripped. These are two faces of one mechanism — a copy that inherits only declared state, dropped into a role that requires undeclared state.

The trap is fixing it one missing file at a time. The first build failure names one absent framework; restore it and the next failure names a missing generated source; restore that and the deploy quietly bakes in empty credentials because the `.env` never traveled — a failure that only surfaces at runtime, in production. Whack-a-mole is the symptom-level response. The pattern has two moves that address the class. First, when an isolated copy fails, stop and enumerate the complete set of untracked-but-required inputs — read the `.gitignore`, list what the build actually consumes, and transfer or regenerate all of it in one pass rather than letting each omission fail in sequence. Second, for deployed configuration, move the state into whatever the deploy mechanism itself carries — a config file the deploy tool auto-loads, secrets referenced by the artifact — so that every future deploy re-establishes it without anyone remembering to. The test of the durable fix is that it makes the next copy self-healing, not that it makes the current copy work.

## When to reach for it

- When a build or test fails in a fresh worktree, clone, or CI environment but passes in the original checkout — assume a class of missing untracked inputs, not one missing file.
- When extracting code into a new repository for another team or an open-source release — enumerate the gitignored dependencies before the handoff, because the recipient's first build is a fresh clone.
- When a redeploy makes previously working configuration vanish, or a newly created service instance lacks settings its siblings have — the config was set imperatively and never declared.
- When you catch yourself, or an agent, re-running the same "set the env vars again" script after every deploy — that script is the whack-a-mole loop made visible.
- When automating releases from isolated workspaces (agent worktrees, ephemeral runners), where every run is by construction a fresh copy.

## When NOT to

- When state is untracked precisely because it must not travel — production secrets excluded from a repo shared with contractors should stay out; the fix is a declared secrets mechanism, not committing them.
- When the copy is genuinely disposable and single-purpose — a scratch clone for reading code doesn't need its build inputs reconstructed.
- When the missing input really is a one-off — a single absent file with no siblings in the gitignore doesn't warrant a full enumeration pass, though a second miss means it does.

## Exemplars

- Session history — askkaya project, session 364f9218 (2026) — release from a fresh worktree failed on a gitignored xcframework, then on generated Swift sources, then deployed a function with no keys because `.env` never traveled; the turn was enumerating all gitignored build inputs as a set instead of chasing them one by one
- Session history — askkaya project, session ea9d9a0c (2026) — Firebase redeploys stripped manually-set env vars, and a newly created function never received them at all; after three rounds of a re-set script, a gitignored `.env` the deploy tool auto-loads made every future deploy self-heal

## Related

- `patterns/persist-environment-facts.md`
- `patterns/propagate-the-bug-class.md`
- `patterns/repository-shape-is-cognitive-architecture.md`
