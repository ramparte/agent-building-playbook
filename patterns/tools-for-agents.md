---
title: Design Tools for Agents, Not Humans
one_liner: Agent tools should be structured for machine parsing — unambiguous outputs, complete information in every response, no UI affordances that only make sense for humans.
dimensions: tool-design
---

## What it is

Tools built for human use are optimized for legibility: they paginate, they truncate long output with "..." ellipsis, they format for terminal width, they return user-friendly error messages that assume the caller can ask a follow-up question. When agents use these same tools, each of those human affordances becomes a failure mode. Truncated output means the agent acts on an incomplete picture. Pagination means the agent must know to fetch the next page — and may not realize it didn't see the whole thing. User-friendly error messages are ambiguous strings that must be parsed to extract the actual failure code. "Design tools for agents, not humans" means rethinking the contract at the level of what a machine needs: complete, structured, deterministic outputs. An agent tool should return all relevant data in a single call unless the data is genuinely too large. Error cases should be expressed as structured fields — a code, a reason, a recoverable flag — not as prose. Success cases should include the metadata the agent needs to decide what to do next, not just the primary payload. The caller is not a human who can glance at the output and intuit the context; it is a model with a fixed context window that will treat whatever it receives as complete truth.

## When to reach for it

- When designing tools that will be registered in an agent's tool list — every design decision should assume the caller is a model, not a human reading output in a terminal.
- When adapting existing CLI tools or APIs for agent use — identify all the human affordances (truncation, pagination, user-friendly error messages) and replace them with machine-readable equivalents.
- When agents are making incorrect decisions because they're acting on partial or ambiguous tool output — the tool's output contract, not the agent's reasoning, is usually the root cause.
- When writing tool descriptions: the description is not a tooltip for a human hovering over a button, it is the sole specification the model uses to decide when and how to call the tool.

## When NOT to

- When the tool is genuinely dual-use — consumed by both humans in a terminal and by agents in a loop. In this case, add a machine-readable output mode (`--format json`, `--output structured`) rather than replacing the human-readable default.
- When the tool wraps an external API that you don't control — you cannot redesign the contract, so focus on the wrapper layer that translates the external response into an agent-friendly structure.
- When the "human affordance" is actually useful to an agent — a summary section at the top of a long response can help the agent reason without attending to every detail; don't remove structure that aids reasoning just because it was originally designed for humans.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: identifies tool design as a primary lever for agent reliability and calls out structured, unambiguous outputs as a key requirement
- Anthropic — https://github.com/anthropics/anthropic-cookbook — Anthropic Cookbook: tool use examples demonstrate returning structured JSON with explicit success/error fields rather than prose messages
- Anthropic, "Writing Effective Tools for AI Agents" — https://www.anthropic.com/engineering/writing-tools-for-agents — origin: comprehensive guide on designing tool contracts for machine parsing — structured outputs, unambiguous descriptions, meaningful context in place of human-readable affordances
- Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools" (arXiv:2302.04761) — https://arxiv.org/abs/2302.04761 — classic antecedent: established the paradigm of models using external tools via simple APIs, motivating the need for well-designed agent-facing tool interfaces

## Related

- `patterns/namespace-tools.md`
- `patterns/search-over-list.md`
- `patterns/agents-optimize-tools.md`
