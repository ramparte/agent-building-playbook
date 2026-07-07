---
title: Use Session History as Primary Evidence
one_liner: When something went wrong — or right — in a prior run, the session transcript is the primary evidence; reading it is the first act of diagnosis, not a fallback after other approaches fail.
dimensions: observability
---

## What it is

When a system behaves unexpectedly, the immediate instinct is to look at the current state and reason forward: inspect the output, check the config, re-run the command. This is hypothesis-first diagnosis — constructing a model of what might have happened and then looking for confirming evidence. Session history inverts this: the transcript of what actually happened already exists. The model's reasoning, the tool calls it made, the outputs it received, the decisions it took and the context in which it took them — all of this is recorded, available, and deterministic. Reading it is not archaeology in the pejorative sense; it is reading the primary source. A session that ended in failure contains the failure event, its immediate context, and the chain of decisions that led to it. A session that succeeded unexpectedly contains the same. Treating session history as primary evidence means making transcript reading the first act of diagnosis for any question about a past run, not something attempted after other approaches fail. The record is more reliable than reconstruction from current state, faster than reproduction from scratch, and more informative than any hypothesis about what probably happened.

## When to reach for it

- When diagnosing a failure in a prior run: read the session transcript before re-running, before inspecting current state, and before forming hypotheses. The cause is more likely already in the record than inferrable from current state.
- When validating that a prior run actually did what it claimed: agent completion claims are assertions; the session record is the evidence that supports or contradicts them.
- When handing a task between agents or sessions: the receiving agent should read the prior session's history as its first act, not rely on the summary that the prior agent produced about itself.
- When debugging a recurring failure: compare the session histories of multiple failing runs to find the common pattern. Individual run inspection finds local causes; cross-run comparison finds structural causes.
- When evaluating agent behavior for quality or safety: the session transcript is the ground truth of what the agent actually did, not what it reported doing.

## When NOT to

- When the session record does not exist — the system did not emit events, the transcript was not persisted, or the session predates the logging infrastructure. In this case, acknowledge the observability gap and flag it, rather than treating inference as equivalent to evidence.
- When the session transcript is too large to read directly and the relevant section is unknown — use tooling to search and filter (grep, structured event queries) rather than loading the entire record; extremely large transcripts can exhaust context before the relevant section is reached.
- When the question is about current system state, not past behavior — session history tells you what happened, not what is happening now. For current state, inspect the live system directly.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier — the session-analyst agent and context-intelligence graph server: session history is the primary source of truth for diagnosing agent failures, tracing delegation chains, and understanding tool call behavior across runs; the entire observability architecture is built around making session history queryable
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends logging and reviewing agent transcripts as the primary mechanism for debugging unexpected behaviors in multi-step agentic pipelines
- Wang et al., "From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents" (arXiv:2606.04990) — https://arxiv.org/abs/2606.04990 — surveys the discipline of using agent execution traces as primary evidence; formalizes provenance, trace sources, and representation forms that underpin treating session history as ground truth
- Nian et al., "Auditable Agents" (arXiv:2604.05485) — https://arxiv.org/abs/2604.05485 — defines five dimensions of agent auditability including evidence integrity and lifecycle coverage; treats the session record as the required substrate for accountability, responsibility attribution, and recovery

## Related

- `patterns/emit-events.md`
- `patterns/awareness-layer.md`
- `patterns/evidence-before-assertions.md`
