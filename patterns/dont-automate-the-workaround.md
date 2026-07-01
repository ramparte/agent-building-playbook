---
title: Don't Automate the Workaround
one_liner: In legacy and bureaucratic domains the stated process is often itself a workaround for another broken process — automating it with an agent entrenches the dysfunction at speed; ask whether the workflow should still exist before you accelerate it.
dimensions: intent, workflow-discipline, meta-principles
---

## What it is

In legacy and bureaucratic domains, the process you are asked to automate is frequently not a process at all but a workaround — an accretion of steps people invented to route around some other broken process, preserved long after anyone remembers why. Automating such a workflow does not just fail to fix the dysfunction; it entrenches it, and because an agent executes faster and more consistently than the humans who tolerated the friction, automation accelerates the wrong thing and removes the very friction that kept the broken process visible and under pressure to change. The discipline is to ask, before accelerating any workflow, whether it should still exist — to treat the request to automate as a prompt to examine the workflow's reason for being rather than a mandate to encode it. This requires distinguishing essential behaviors, which serve a genuine need, from historical accidents, which survive only because no one has questioned them; the steps that exist because of a constraint that no longer holds, a system that was retired, or a person who left should be removed, not reproduced in code. An agent will faithfully implement whatever it is given, so the judgment about whether the workflow deserves to persist has to happen upstream of the automation, in the intent layer, where someone is still asking why. This is the sharpest special case of requirements being disguised solutions: where that pattern addresses an individual stated solution — a field, a rule, a report — this one addresses an entire workflow whose disguised purpose is to paper over a broken process it should not be perpetuating.

## When to reach for it

- A request asks you to automate an existing manual process, especially in a legacy, regulated, or bureaucratic domain.
- The workflow has steps nobody can fully justify, or that exist "because that's how it's always been done."
- Removing the friction of a manual process would also remove the pressure that might otherwise force the process to improve.
- You can distinguish steps that serve a real need from steps that survive only as historical accidents.
- The cost of entrenching a dysfunction at machine speed is higher than the cost of pausing to question the workflow.

## When NOT to

- The workflow is genuinely sound and the manual version is simply slow — automating it is pure win.
- A mandate (legal, regulatory, contractual) requires the workflow to exist exactly as specified, regardless of its origins.
- Questioning the workflow is out of scope or above your authority and would only stall delivery the stakeholder explicitly owns.
- The dysfunction is real but redesigning the process is a separate, larger effort that should not block a clearly-scoped automation.

## Related

- `patterns/requirements-are-disguised-solutions.md`
- `patterns/interview-to-a-spec.md`
- `patterns/fix-the-root-cause.md`
- `patterns/shadow-then-transform.md`
