---
title: Namespace Tools, Write Unambiguous Descriptions
one_liner: Group tools under a clear namespace and write descriptions that tell the model exactly when to call this tool and when to call a similar one instead — ambiguous tool selection is a primary source of agent errors.
dimensions: tool-design
---

## What it is

When an agent has access to many tools, tool selection becomes a reasoning task: the model must read each tool's name and description and decide which one applies to the current situation. Ambiguous names and vague descriptions make this reasoning unreliable. A tool named `read` and another named `fetch` will produce inconsistent selection behavior because the model must infer from context which applies to files versus URLs. A tool described as "gets information about a resource" can match almost any retrieval operation and will be selected unpredictably. Namespacing and precise descriptions eliminate this ambiguity at the source. Namespacing groups related tools under a common prefix — `file_read`, `file_write`, `file_list` rather than `read`, `write`, `list` — so the model can use the namespace as a first-pass classifier before reading the description. Precise descriptions go further: they name the specific cases this tool handles, explicitly call out adjacent tools it is NOT appropriate for, and describe what the output looks like. A good tool description reads like a contract: "Call this tool when you need to read the contents of a local file by path. Do NOT use this to fetch remote URLs — use `http_get` for that. Returns the file content as a string." This level of specificity is not over-engineering; it is the minimum specification the model needs to select reliably in a diverse tool set.

## When to reach for it

- When adding a new tool to a set that already has tools with overlapping names or purposes — add a clear namespace prefix and write a description that distinguishes this tool from the most similar existing tools.
- When agents are calling the wrong tool for a situation — read the description as if you are the model and ask whether the description unambiguously points to this tool and away from the adjacent ones.
- When building a tool set with more than five or six tools — at this scale, namespace prefixes pay off by giving the model a hierarchical classification structure before it reads individual descriptions.
- When a tool has a common name that could mean different things in different contexts (`search`, `get`, `update`, `delete`) — rename it with a namespace or add explicit exclusion language to the description.

## When NOT to

- When the tool set is very small (two or three tools) and the purposes are genuinely distinct — namespacing adds visual noise without clarity benefit when there is no risk of confusion.
- When tools are registered dynamically and the namespace prefix would vary across invocations — in this case, invest in the description specificity rather than the naming structure.
- When conforming to an existing tool naming convention that the model was trained on — overriding well-known names like `bash` or `read_file` that models have strong priors for can introduce more confusion than it resolves.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: calls out tool definitions as deserving the same prompt-engineering attention as system prompts, with clear boundaries between tools
- Anthropic, "Writing effective tools for agents — with agents" — https://www.anthropic.com/engineering/writing-tools-for-agents — formalizes: recommends grouping related tools under common prefixes and using unambiguously named parameters to reduce selection confusion

## Related

- `patterns/tools-for-agents.md`
- `patterns/agents-optimize-tools.md`
- `patterns/code-execution-tools.md`
