---
title: "Thin Pointers, Zero Poisoning"
one_liner: Pass file paths and references between agents instead of full content — let each agent pull only what it needs, only when it needs it.
dimensions: context-engineering, orchestration
---

## What it is

When agents hand off work to one another, the temptation is to inline the content — to pass the full file, the complete document, the entire tool output — so the receiving agent has "everything it might need." The result is context poisoning: the receiving agent's window fills with content it may not need, cannot easily distinguish the relevant from the irrelevant, and pays the token cost of carrying the full payload through every subsequent reasoning step. Thin pointers replace content with references: a file path, a document ID, a section heading, a tool invocation pattern, a structured description of where the content lives and how to retrieve only the part that matters. The receiving agent reads the pointer, retrieves exactly the slice it needs at the moment it needs it, and never loads the rest. Thin pointers apply the just-in-time retrieval principle to inter-agent communication: pass the address, not the object. Zero poisoning is the goal — no agent should start with content in its context that it did not itself choose to load.

## When to reach for it

- When passing large artifacts (files, documents, datasets, code) from one agent to another — pass the path and relevant section markers, not the content.
- When an orchestrator agent's context contains accumulated tool outputs from prior steps that are no longer directly needed — replace them with a pointer to the file where they were written, then continue.
- When designing inter-agent protocols in a multi-agent pipeline — specify the exchange format as structured references, not embedded payloads.
- When a sub-agent returns a large result and only a summary is needed by the orchestrator — receive the summary plus a pointer to the full result on disk; the orchestrator decides whether to dereference.

## When NOT to

- When the referenced content is small enough that inlining it costs no meaningful tokens and the round-trip retrieval overhead is not justified — thin pointers have coordination cost; don't apply them to single-line values.
- When the receiving agent will predictably need the full content immediately and the retrieval adds latency without saving tokens — inline when you are certain the full content will be consumed.
- When the content cannot be written to a stable location (ephemeral in-memory results with no persistence mechanism) — thin pointers require a dereferenceable address.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends file-based artifacts and tool-call references as the primary mechanism for inter-agent state transfer, avoiding in-context content accumulation
- Amplifier — https://github.com/microsoft/amplifier — the delegate() pattern returns summaries by default, with the full result written to artifacts the orchestrator can read by reference if needed
- Curme and Daugherty (LangChain) — https://www.langchain.com/blog/context-management-for-deepagents — formalizes: Deep Agents replaces tool responses exceeding 20k tokens with a filesystem path and 10-line preview, then truncates older writes at 85% context utilization—a direct implementation of thin pointers for inter-step context management
- Breunig, "How to Fix Your Context" — https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html — formalizes: names "Context Offloading" (storing data outside the LLM context via external tools) as a first-class technique — the thin-pointer move applied to agent-to-storage transfer

## Related

- `patterns/subagents-as-context-sinks.md`
- `patterns/just-in-time-retrieval.md`
- `patterns/write-select-compress-isolate.md`
- `patterns/context-is-finite.md`
