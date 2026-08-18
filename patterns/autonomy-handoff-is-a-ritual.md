---
title: The Autonomy Handoff Is a Ritual
one_liner: Granting an agent unsupervised execution is a structured speech act with preconditions, not a casual "go" — a plan must already exist, the tools and scope are named, the human leaves, and completion is the expected return; inside that contract a clarifying question is a breach, not caution.
dimensions: human-factors, workflow-discipline, orchestration
---

## What it is

There are two contracts a human can hold with an agent, and they invert one rule. In normal interactive work, an agent that pauses to ask a clarifying question is being careful, and caution is welcome. Inside an autonomy handoff — where the human has granted unsupervised execution and physically left — the same question is a breach: it means the run needed something it didn't have, and there is no one there to answer. The reliable handoff is therefore a ritual with a fixed grammar, observed consistently across a 14-month single-operator corpus: a plan already exists, the method or toolset is named ("use the subagents," "run the swarm"), the scope is bounded ("the only thing to watch is the app design"), the human removes themselves ("I'm going to bed, you got this"), and the agent is expected to return *completion*, not a progress report. The discipline is entirely front-loaded. Because the human is gone the moment autonomy is granted, everything the run needs must be settled before the grant — the ritual exists to force that settling. Skipping it produces the failure mode the operator complained about more than any other: an agent that stops mid-run to ask what it should already know.

## When to reach for it

- The work is bounded and planned, and you have already reviewed the plan — hand off against a spec, never into a vacuum.
- The cost of a mid-run interruption (waking you, blocking overnight progress) exceeds the cost of a wrong guess you can catch at review.
- Time pressure or an overnight window makes unattended execution the point, not a risk to be minimized.
- The agent has a named method to invoke and a stop condition to reach.

## When NOT to

- No plan exists yet. Handing off unbounded intent produces drift, and the agent will invent a stop condition you didn't want.
- Intent is genuinely ambiguous and a wrong guess is expensive or unrecoverable — here you *want* the interrupt, so stay in interactive mode.
- The work includes irreversible or high-blast-radius actions where a human checkpoint is the safeguard.
- You are running an unproven harness for the first time — earn trust in attended mode before you leave the room.

## Exemplars

- Handoff grammar — 14-month Claude Code session corpus — hand-offs cluster at 20:00–23:00 local and follow a fixed shape: "tbh i trust you and i am ready … no reason to have me here. don't stop until it is done."
- The inverse-contract cost — same corpus — "stop stopping" was the single most frequent correction (146 instances); mid-run questions during a handoff, not bad output, were the operator's top irritant.

## Related

- `patterns/clear-stop-condition.md`
- `patterns/autonomy-when-justified.md`
- `patterns/earn-the-interruption.md`
- `patterns/share-full-context.md`
