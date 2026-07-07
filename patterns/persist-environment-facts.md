---
title: Persist Environment Facts
one_liner: Facts about the environment — directory layout, versions, credentials, topology — belong in files the agent can re-read, not floating in context that disappears on reset.
dimensions: context-engineering
---

## What it is

Every agent run begins with a context window that knows nothing. Facts that were discovered in a previous session — the repository structure, the installed tool versions, the API endpoint, the cluster topology, which ports are open, where the config lives — must be re-discovered or re-stated every time unless they have been written down. Persisting environment facts is the practice of capturing this discovery work in structured files that any session can read as its first act: a `WORKSPACE.md` describing directory layout and conventions, an `env.yaml` capturing tool versions and cluster state, a `.env` or secrets file with endpoint addresses. These files are the agent's memory of the world it is operating in. Without them, every session re-discovers what the last session already knew, paying in tokens and latency for information that is stable across runs. With them, the agent begins from a grounded, accurate model of its environment rather than a blank slate.

## When to reach for it

- When setting up a new project that an agent will work in across multiple sessions — write the environment facts file as part of project initialization, not after the fact.
- When an agent discovers something non-obvious about the environment (an unusual directory layout, a pinned version, a quirk of the deployed service) — write it down immediately before context resets.
- When debugging an agent that keeps making the same wrong assumptions about the environment — the fix is persistent documentation, not better prompting.
- When handing a project to a new agent or a new operator — the environment facts file is the onboarding document.
- When the environment changes (new machine, new config, new topology) — update the persisted facts as the first step after the change.

## When NOT to

- Rapidly changing environments where the persisted facts would be stale by the time they are read — volatile state belongs in real-time tool reads, not stale files.
- Short-lived, single-session tasks where the environment is fully defined in the prompt and will never be revisited — the overhead of writing a facts file is not justified.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends writing to files as a primary persistence mechanism for agentic systems that need to preserve state across context resets
- Anthropic — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — formalizes: structured note-taking to external memory as the primary mechanism for preserving environment facts when the active context window resets
- Chatlatanagulchai et al., "Agent READMEs: An Empirical Study of Context Files for Agentic Coding" (arXiv:2511.12884) — https://arxiv.org/abs/2511.12884 — empirical support: shows AGENTS.md and CLAUDE.md files are the dominant mechanism practitioners use to persist project-level environment facts across agent sessions

## Related

- `patterns/checkpoint-handoff-file.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/long-horizon-memory.md`
