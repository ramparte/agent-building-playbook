---
title: Requirements Are Disguised Solutions
one_liner: Stakeholders ask for a field, a button, a report, or a workflow change — but agents will happily implement the stated solution even when it's a workaround for a broken process, so the intent layer must ask what the request is actually trying to accomplish.
dimensions: intent, workflow-discipline
---

## What it is

Stakeholders rarely state needs; they state implementations. They ask for a field, a validation rule, a report, a button, or a workflow change — each of which is already a guess at the solution, shaped by the tools they have, the system they remember, and the workaround they have learned to live with. In conventional product work, the job of seeing past the stated solution to the underlying need belongs to product management, design research, and implementation teams. In an agentic organization it becomes a first-class part of the machine interface, because an agent will happily and quickly build exactly what was asked — and if the stated solution is a workaround for a broken process, the agent simply accelerates the wrong thing. The intent layer's job is to ask why before how: to translate "add this field" into *what decision depends on this field?*, "validate this differently" into *what failure are we preventing?*, "build this dashboard" into *who changes their behavior after seeing it?*, "automate this workflow" into *should this workflow still exist?*, "make it like the old system" into *which behaviors are essential and which are historical accidents?*, and "the answer depends" into *what variables make it depend, and can we collect examples?* The request is a clue to the need, not the need itself; treating it as the spec encodes the stakeholder's diagnosis as if it were the requirement.

## When to reach for it

- A stakeholder requests a specific implementation detail (a field, a button, a rule) — convert it to the decision or failure it is meant to serve before building.
- The request references "the old system" or "how we've always done it" — separate essential behaviors from historical accidents before reproducing them.
- A request would automate an existing manual workflow — first ask whether that workflow should survive at all.
- The stated answer "depends" — pull on the dependency: which variables, and can the stakeholder supply labeled examples instead of a rule?
- You notice an agent is about to implement exactly what was asked with no model of why — pause and recover the intent.

## When NOT to

- The requested solution genuinely is the need (a legal mandate, a fixed external contract, a hard interface) — interrogating it wastes everyone's time.
- The cost of building the literal request is trivial and reversible — sometimes shipping the asked-for thing is the cheapest way to learn whether it was right.
- Repeatedly asking "but why do you really want this?" has become an obstruction that erodes the stakeholder's trust — read the room and commit.

## Related

- `patterns/interview-to-a-spec.md`
- `patterns/dont-automate-the-workaround.md`
- `patterns/document-intent.md`
- `patterns/good-pile-bad-pile.md`
