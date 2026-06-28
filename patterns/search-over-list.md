---
title: Prefer Search/Filter Over List-Everything
one_liner: Give agents a search or filter interface rather than a tool that returns a full list — agents that list everything then scan results are burning context on data they'll mostly discard.
dimensions: tool-design, context-engineering
---

## What it is

A common tool design mistake is providing a "list all" operation and expecting the agent to iterate through the results to find what it needs. The agent calls `list_files()`, receives 400 file paths, loads them into context, and then scans for the two files it actually cares about. The 398 irrelevant paths consume tokens, crowd out working content, and force the model to attend across a large noisy payload to extract a small useful signal. Search-over-list replaces this pattern with a targeted interface: instead of `list_files()`, provide `find_files(pattern=...)` or `search_files(query=...)`. The agent specifies what it is looking for; the tool does the filtering; the response contains only the relevant results. This moves work from the model's context to the tool's implementation — exactly the right direction. The cost of filtering at the tool layer is near zero; the cost of filtering inside a model's context window is measured in tokens, latency, and reasoning quality. The principle extends beyond file systems: any tool that could return a large collection benefits from a search or filter parameter. Databases should expose queries, not table dumps. Event logs should support time range and type filters, not full dumps. Configuration stores should support key lookup, not serialization of the entire config.

## When to reach for it

- When designing any tool whose natural response is a collection — add at minimum one filter parameter that limits results to what the caller declared it needs.
- When an agent is calling a list tool and then reasoning about which items to use — this is the signal that the list tool should have been a search tool.
- When context is filling up with intermediate collection results that the agent only partially uses — replace the list-and-scan pattern with a targeted search at the tool layer.
- When paginating through large result sets — pagination is often a sign that the tool should expose richer query parameters so the agent can get the right N items in one call instead of fetching pages until it finds them.

## When NOT to

- When the agent genuinely needs the full collection to reason about it — a tool that lists all open issues so an agent can triage and prioritize legitimately needs the full list; replacing it with a search would prevent the agent from seeing the whole picture.
- When the collection is small and stable enough that returning everything costs less context than the overhead of a query parameter — a tool that returns five configuration keys doesn't need a filter interface.
- When the agent has explicitly asked to browse or explore — exploration tasks where the agent doesn't yet know what it's looking for benefit from broader enumeration followed by progressive filtering, not upfront keyword search.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends tools that return targeted results rather than requiring agents to filter large payloads in context
- Anthropic — https://www.anthropic.com/news/contextual-retrieval — Contextual Retrieval: the retrieval design principle of returning high-signal-per-token results applies equally to tool outputs as to RAG retrieval

## Related

- `patterns/just-in-time-retrieval.md`
- `patterns/context-is-finite.md`
- `patterns/tools-for-agents.md`
- `patterns/code-execution-tools.md`
