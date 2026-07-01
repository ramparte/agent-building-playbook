---
title: Supervise Many Agents Through One Interface
one_liner: As agents multiply, the limiting factor is the human's ability to see them — build the supervision surface — a dashboard of what's running, stuck, done, costly, or waiting; status exhaust; an attention firewall; a review queue; a cost monitor; and the ability to resurrect and hold old sessions accountable.
dimensions: observability, human-factors, orchestration
---

## What it is

Once a person is running more than a handful of agents — coding sessions, cloud workflows, review squads, bots, background monitors — the bottleneck stops being machine work and becomes the human's ability to see the machine work. Too much output arrives without the right interface: finished sessions pile up unreviewed, status is unclear across sessions, notifications fire at the wrong time, and nobody can tell which agent actually needs help. The supervision surface is the single interface that makes a fleet of agents legible to one human, and it is assembled from a small kit of attention tools. An agent dashboard shows which sessions are running, stuck, done, costly, or waiting for review, so the state of the fleet is visible at a glance. Status exhaust is the stream each agent emits — summaries, artifacts, costs, risks, and proposed next steps — so a session can be understood without re-deriving its history. An attention firewall filters noisy channels and surfaces only relevant changes, so the human is not buried in routine chatter. An interrupt policy governs when agents may ask for help. Session resurrection lets a human resume an old session and hold it accountable to its prior state, rather than losing the thread when context expires. A background auditor watches running agents and summarizes anomalies the operator would otherwise miss. A review queue prioritizes finished outputs by risk, importance, and confidence. And a cost monitor tracks token spend against value produced, so runaway loops are caught by economics, not just by errors. The point is not any single widget; it is that supervising many agents is itself a design problem, and the interface is the product.

## When to reach for it

- When one person is responsible for more concurrent agents than they can hold in their head — the dashboard and status exhaust turn an unknowable fleet into a readable one.
- When finished work outpaces review and you cannot tell which output to look at first — a review queue ordered by risk and confidence is the missing surface.
- When agents run unattended for long stretches — a background auditor and a cost monitor catch drift, runaway loops, and silent failures the operator is not watching for.
- When sessions are abandoned mid-task and their context is lost — session resurrection makes long-running work resumable and accountable instead of disposable by accident.
- When notification noise has trained the team to ignore agent output — an attention firewall plus an interrupt policy restores signal.

## When NOT to

- When you run one or two agents at a time and can watch them directly — building a supervision surface for a fleet you do not have is premature infrastructure.
- When the agents are short-lived and self-contained, finishing within a single observable context — there is no fleet to supervise.
- When the supervision tooling would consume more attention to maintain than it saves — start with the one surface that addresses your actual bottleneck (usually the review queue or the dashboard), not the whole kit.
- When the underlying problem is that agents shouldn't be running at all — a dashboard makes bad work visible, it does not make it good.

## Related

- `patterns/awareness-layer.md`
- `patterns/emit-events.md`
- `patterns/earn-the-interruption.md`
- `patterns/attention-is-the-scarce-resource.md`
