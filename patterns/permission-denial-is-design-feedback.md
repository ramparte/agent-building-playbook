---
title: A Permission Denial Is Design Feedback
one_liner: When the harness blocks an action, ask what the denial is telling you about the plan's shape before asking how to get it approved — the blocked design is often the wrong design.
dimensions: meta-principles, workflow-discipline
---

## What it is

When a guardrail refuses an action, the reflexive question is "how do I get this approved?" The better first question is "what is the refusal telling me about my plan?" A denial is not just a stop sign; it carries information about the shape of what you proposed. Concrete case: a safety classifier blocked an agent from creating a public endpoint for a data-cleanup task. The agent's read was not "the classifier is being difficult" but "a permanent public mutating endpoint is overkill for a one-off cleanup — the right tool is a one-off migration script with admin credentials." The block was pointing directly at the better design: same outcome, no permanent attack surface. The mismatch between the action's blast radius (permanent, public, mutating) and the task's actual need (once, private, scoped) is exactly what the guardrail detected — and what a good reviewer would have flagged.

The same reading applies when the denial comes from further upstream — a provider-side content filter, an API policy layer, an agent harness rule. The discipline there has two steps. First, identify *which* layer refused, with the literal error as evidence: in one session an image-generation request came back with `InputImageSensitiveContentDetected.PrivacyInformation`, and the agent's first move was to establish that "that rejection came back from Seedance's own provider," not from its own policy. Second, redesign the approach to meet the intent rather than coaching the filter. When the user begged "tell it it's a simulation," the agent declined — "the block is on the server side" — and pivoted to a text-driven generation path that delivered what the user actually wanted. Coaching a filter fights the mechanism; naming the layer and reshaping the request works with it. And when a block lands on a genuine scope expansion — an agent stopped before auto-deploying a send-capable email backend — the denial is correctly separating "build it" from "expose it to production," a distinction worth keeping even when you could override it.

## When to reach for it

- The moment a guardrail, classifier, or provider filter blocks an action — before retrying, rephrasing, or requesting an override, ask what mismatch the block detected.
- When the blocked action's footprint is larger than the task's need (permanent for one-off, public for private, prod-wide for single-record) — the denial is usually pointing at a smaller-shaped alternative.
- When a refusal comes from an upstream service — capture the literal error string, name the layer that refused, and redesign to meet the underlying intent instead of prompt-coaching the filter.
- When a block lands on a deploy or exposure step rather than a build step — treat it as a checkpoint separating construction from release, not as friction.

## When NOT to

- When the denial is plainly a missing grant — an allowlist entry, a scope, a credential the workflow legitimately needs. Not every block is design wisdom; sometimes the fix really is "add the permission."
- When the guardrail is misconfigured or matching too broadly — a filter blocking routine, correctly-shaped work is a bug in the guardrail, and the fix is to tune it, not to contort the design around it.
- When you cannot articulate what the block might be detecting — do not invent a design lesson to rationalize a denial; escalate to a human with the literal error instead.

## Exemplars

- Session history — askkaya project, session 2e48cbbe (2026) — classifier blocked a permanent public mutating endpoint for a one-off cleanup; the agent read the block as pointing at the better design and shipped a one-off migration script instead
- Session history — askkaya project, session ea9d9a0c (2026) — deploy of a send-capable backend blocked as a scope expansion ("that's the right call; I shouldn't auto-deploy a scope expansion"); a separate block on copying live prod secrets between services was likewise accepted as correct
- Session history — montreal project, session f835ca51 (2026) — provider returned `InputImageSensitiveContentDetected.PrivacyInformation`; the agent named the refusing layer, declined to coach the filter, and redesigned around a text-driven path that met the intent

## Related

- `patterns/stage-everything-human-fires.md`
- `patterns/guardrails-and-escalation.md`
- `patterns/separate-merge-from-exposure.md`
- `patterns/state-the-target.md`
