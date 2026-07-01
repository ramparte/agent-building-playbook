---
title: Interview to a Spec Before Implementing
one_liner: Put a skeptical interviewer in front of intent — one that asks why before how, reflects back its understanding, refuses to implement until it can restate the goal cleanly, and emits a concise spec the human can reject — turning messy intent into an executable specification.
dimensions: intent, workflow-discipline, verification
---

## What it is

Before any code is written, intent should pass through a dialogue whose job is to compile messy human wishes into an executable specification. The right interaction is closer to a coaching or therapeutic conversation than a command line: the system does not rush to a solution but helps the human discover their own intent, asking why before how, separating goals from the implementations stakeholders propose, reflecting back its current understanding so misreadings surface early, asking for examples of good and bad outcomes, and naming the unknowns and contradictions it finds. The interviewer is skeptical by design — it refuses to start building until it can restate the goal cleanly in its own words, acting as a compiler from ambiguous intent to a specification, and it probes with questions like *what problem are we solving, who experiences it, what happens if we do nothing, what would make the solution unacceptable, what examples define success, what should not be changed, and what proof should the implementation produce.* What the dialogue emits is not a verbose transcript but a working artifact — a concise spec with acceptance criteria, user stories, scenarios, constraints, and open questions — small enough that the human can read it and reject or approve it. This guards against the common failure of treating the first prompt as the spec: the first prompt is an impulse, an input to the intent process, not the final instruction, and an agent that runs with it skips the step where intent is actually determined.

## When to reach for it

- A request arrives as a one-line prompt and you are tempted to start building — route it through the interviewer first to turn the impulse into a spec.
- The work is high-stakes or expensive enough that building the wrong thing costs more than the dialogue.
- The goal is ambiguous, contested, or stated as a solution rather than a need.
- You want a durable, inspectable artifact (spec, acceptance criteria, open questions) that downstream agents and humans can both work from.
- An agent keeps producing plausible-but-wrong output because nobody pinned the success criteria before execution.

## When NOT to

- The task is small, well-understood, and cheap to redo — a full interview is heavier than the work itself.
- The human genuinely wants exploration, not a spec — forcing premature precision kills the discovery the prototype is meant to provide.
- The interviewer becomes an interrogation that never terminates — if it cannot converge, the bottleneck is missing information, not more questions.
- Speed pressure makes a worse-but-shipped spec preferable to a perfect one that arrives too late.

## Related

- `patterns/document-intent.md`
- `patterns/requirements-are-disguised-solutions.md`
- `patterns/people-edit-better-than-they-author.md`
- `patterns/keep-specs-in-sync.md`
- `patterns/good-pile-bad-pile.md`
