---
title: Document Intent, Not Just Method
one_liner: Code describes how; comments and specs must describe why — the reasoning that code cannot encode.
dimensions: workflow-discipline
---

## What it is

Code is a complete, executable record of *what* the system does and *how* it does it. But code cannot express the reasoning behind its own existence: why this approach rather than an alternative, what constraint the implementation is satisfying, what invariant must hold even as the code changes. When documentation is limited to restating the code in prose, it adds no information. When documentation captures intent — the decision rationale, the constraint being satisfied, the design alternative rejected and why — it becomes the only place that information lives. Agents reading code without intent documentation must reverse-engineer the reasoning, which they do unreliably. Agents reading intent documentation can apply, extend, and correct the code without contaminating it with false assumptions.

## When to reach for it

- Any time a decision was made among meaningful alternatives — document which alternatives were considered and why this one was chosen.
- When a constraint is subtle and its violation would look like a valid improvement — comment the constraint and name the failure mode that removes it.
- When an API or interface is shaped by an external requirement, a protocol, a legacy assumption, or a third-party contract — make that dependency explicit in the spec, not just the code.
- Before handing a module to an agent for extension or refactoring — write a brief intent note so the agent preserves the reasoning, not just the structure.
- When a workaround exists — document what it works around, not just what it does.

## When NOT to

- Trivial, self-evident code where intent and method are identical ("add one to the counter") — documentation here adds noise that obscures the signal.
- Exploratory spike code that will be deleted — writing intent docs for throwaway work delays learning without adding value.
- When the intent documentation would simply duplicate an already-clear spec that will be kept in sync — avoid duplication that creates drift.

## Exemplars

- Every major open-source project that survives decades of contribution does so because its architecture documents record the *why* behind design choices — without them, contributors optimize away the very constraints the design was built to preserve.
- The Amplifier AGENTS.md convention stores intent at the agent level: not just what the agent does, but why it is scoped the way it is and what decisions shaped its behavior.
