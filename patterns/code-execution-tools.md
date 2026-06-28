---
title: Code Execution Beats Loading Hundreds of Tool Defs
one_liner: A single code-execution tool — bash, Python, a REPL — often replaces dozens of specialized tools and avoids the context cost of registering a large tool set that the agent must reason over on every call.
dimensions: tool-design, context-engineering
---

## What it is

Every tool registered in an agent's tool list occupies space in the context window through its name and description, and imposes a reasoning cost on the model that must evaluate each candidate tool before selecting one. A tool set that grows to 50 or 100 tools creates substantial overhead: the model attends to dozens of descriptions on every reasoning step, selection errors multiply as tools become harder to distinguish, and the total context budget consumed by tool definitions crowds out working content. Code execution tools — bash, a Python REPL, a JavaScript runtime — offer a different architecture: instead of registering a specialized tool for every operation, register one general-purpose executor and let the agent write the operation as code. Need to list files matching a pattern? Write a shell glob. Need to query a database? Write a SQL statement. Need to parse JSON? Write a jq expression or a Python one-liner. The tool definition cost is fixed at one description regardless of how many operations the agent needs to perform. The generality is bounded only by what the execution environment allows. This is not appropriate for all situations — code execution requires careful sandboxing, carries security implications, and is harder to audit than a predefined tool call — but when the alternative is a sprawling tool catalog that exceeds what a model can reliably reason over, code execution is the more reliable design.

## When to reach for it

- When the tool set has grown beyond 20–30 tools and selection errors are increasing — consolidate groups of related tools into a single code-execution endpoint and let the agent write code for the operations it needs.
- When tool definitions are consuming a significant fraction of the context window — measure the token cost of your tool list; if it exceeds 10–15% of available context, evaluate consolidation via code execution.
- When tasks require combinations of operations that no single tool supports — rather than adding a new tool for each combination, let the agent compose operations in code.
- When the operations needed by the agent are data transformations, file manipulation, or system queries — these map naturally to code and do not require custom tool logic.

## When NOT to

- When the execution environment cannot be safely sandboxed — unrestricted code execution gives the agent the ability to make irreversible changes; always define the blast radius before enabling code execution.
- When the operations require structured inputs and outputs that are harder to enforce through code than through a typed tool interface — tools with defined schemas provide guarantees that free-form code execution does not.
- When the agent population is not reliable enough to write correct code — code execution amplifies both the capability and the error surface; for high-stakes environments, predefined tools with constrained inputs are safer.
- When auditability is a hard requirement — a log of `bash("rm -rf /tmp/old-build")` is harder to audit than a log of `delete_build_artifacts(path="/tmp/old-build")` with a typed schema.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: discusses code execution as a high-leverage tool primitive that enables agent generality without proportional tool set growth
- Anthropic — https://github.com/anthropics/anthropic-cookbook — Anthropic Cookbook: computer use and tool use examples show how code execution reduces the need for a large fixed tool catalog

## Related

- `patterns/search-over-list.md`
- `patterns/tools-for-agents.md`
- `patterns/context-is-finite.md`
- `patterns/namespace-tools.md`
