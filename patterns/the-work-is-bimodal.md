---
title: The Work Is Bimodal — Snipers and Foremen
one_liner: A mature single-operator agent practice splits into two populations that barely overlap — a flood of short, machine-spawned sessions and a thin tail of long, human-driven ones that does most of the work — so stop averaging them and stop reading session count as human effort.
dimensions: orchestration, observability, human-factors
---

## What it is

Plot the sessions of a heavy agent operator by length and you don't get a bell curve — you get two clumps that hardly touch. In a 14-month corpus, 82% of sessions ran under five minutes and were roughly 92% machine-only (no human ever typed into them), while a 7% tail of sessions running three hours to days generated 82% of all transcript output and 88% of all subagent traffic, each steered by a median of about ten human prompts. These are two different animals. The short sessions are the fleet: dispatches, loops, self-evaluations — often fired by a harness with no human in the loop at all. The long sessions are the craft: the human in the chair, setting direction a handful of times while agents run. The trap is treating "sessions" as one population. Averaging them describes nothing real. Worse, reading session *count* as a measure of human effort or progress is a category error once your harnesses spawn their own sessions — a single closed-loop evaluator produced over a thousand sessions from two human prompts. Count measures how often the loop ticked. Manage the two populations separately: the fleet needs aggregate health signals (throughput, failure rate, cost per run) and zero per-session human attention; the craft needs the human present, and that is where review, correction, and taste belong.

## When to reach for it

- You run both automated loops and hands-on work — the moment both exist, the distribution is bimodal and should be instrumented as two things.
- You are building a dashboard or observability layer — split the fleet metrics from the craft metrics; a blended average hides both.
- Someone cites session count, run count, or message volume as a productivity or effort number — separate machine-spawned from human-driven before believing it.
- You are deciding where to spend attention — put it on the long tail, where the work and the corrections actually concentrate.

## When NOT to

- Early in a practice, before you have any automation — everything is hands-on, the second mode hasn't emerged, and there's nothing to separate yet.
- When a single population genuinely does describe your work (one operator, no harnesses, uniform task size).
- Don't over-fit the split into rigid tiers; the boundary is a distribution, not a schema — the point is "don't average," not "build exactly two buckets."

## Exemplars

- Bimodal distribution — 14-month Claude Code session corpus — 5,154 sub-minute sessions (54.6%) vs. 673 marathon sessions (7.1%); the 7% tail holds 82% of all transcript lines.
- Session count decoupled from effort — same corpus — one closed-loop self-evaluation harness logged 1,106 sessions over 73 days from 2 human prompts; 91% of all sub-minute sessions had no human input at all.

## Related

- `patterns/supervise-many-agents.md`
- `patterns/attention-is-the-scarce-resource.md`
- `patterns/single-threaded-default.md`
- `patterns/match-topology-to-the-work.md`
