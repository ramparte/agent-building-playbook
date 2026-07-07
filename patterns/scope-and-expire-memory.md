---
title: Scope and Expire Memory
one_liner: A single global memory pool causes context poisoning, obsession, and stagnation — agents cling to discarded architectures and stale assumptions; default to scoped, expiring memory (project-, role-, task-specific), because forgetting is a feature, not a bug.
dimensions: context-engineering, knowledge, reliability
---

## What it is

A model that remembers everything, indiscriminately, is not more capable — it is harder to steer. When all persisted information flows into one universal memory pool, the agent over-indexes on prior information: it becomes attached to an architecture you already discarded, repeatedly returns to a concern you already deprioritized, and preserves assumptions across sessions that stopped being true two sessions ago. The failure taxonomy is specific. Context poisoning: bad or stale information keeps reappearing and shaping new output. Obsession: the agent fixates on an issue the human has already moved past. Stagnation: early ideas become attractors that crowd out new directions. Token waste: irrelevant history consumes the working window. False continuity: the system looks coherent while silently carrying wrong assumptions forward. Privacy and policy leakage: context meant for one scope surfaces in another. The "one giant memory file" anti-pattern is the same disease in concentrated form — undifferentiated memory becomes context sludge that is hard to retrieve from, hard to audit, and easy to poison. The safe default is scoped memory: persistence partitioned by project, by role, and by task rather than pooled into a single global store, with decay and deletion treated as first-class operations. Mark memories stale, expire or archive context that has outlived its relevance, and keep a decision history without forcing that history into every prompt. Forgetting is not a defect to be engineered away; it is the mechanism that prevents stale ideas from dominating new work.

## When to reach for it

- When designing any persistence layer for an agent that runs across multiple sessions, projects, or users — choose the narrowest scope that still serves the task before reaching for a global store.
- When an agent keeps resurrecting a rejected approach, a closed question, or an assumption the team has since revised — the memory is poisoning the context and needs scoping or expiry.
- When context cost climbs across a long-running engagement without a matching gain in quality — undifferentiated history is being carried that should have decayed.
- When the same memory store spans multiple clients, teams, or trust boundaries — scoping is a privacy and policy control, not just a performance one.
- When you find yourself maintaining a single ever-growing memory or instructions file — split it by scope and add expiry before it becomes sludge.

## When NOT to

- Audit, legal, and compliance workflows where the full decision history must be retained — scope and partition it, but archive rather than delete; expiry must not destroy the record.
- Short, single-session tasks with no carry-over — the overhead of scope partitioning and decay policy is not warranted.
- Genuinely durable facts that should persist indefinitely (a stable domain glossary, an architectural invariant) — these belong in a long-lived scope, not on a decay timer.
- When the real problem is retrieval quality, not retention — adding aggressive expiry to a store you simply query badly will hide useful information without fixing the selection logic.

## Exemplars

- Packer et al., "MemGPT: Towards LLMs as Operating Systems" (arXiv:2310.08560) — https://arxiv.org/abs/2310.08560 — classic antecedent: introduces OS-inspired tiered memory (main context vs. archival storage) with interrupt-based paging, the foundational architecture for scoped memory management in LLM agents
- Breunig, "How Long Contexts Fail" — https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html — empirical support: names and documents the four failure modes (poisoning, distraction, confusion, clash) that accumulation in an unscoped global memory store produces
- Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — formalizes: structured note-taking to scoped external memory as the safe default for preserving state across context resets without poisoning the active window

## Related

- `patterns/long-horizon-memory.md`
- `patterns/just-in-time-retrieval.md`
- `patterns/auditable-artifacts.md`
- `patterns/self-modifying-context-needs-review.md`
