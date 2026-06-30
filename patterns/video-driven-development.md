---
title: Video-Driven Development
one_liner: Require agents to produce a before-and-after video of the real user scenario — a video sets a higher bar than a textual claim and forces the agent to exercise the actual product surface, not just the code; the rule is show, don't assert.
dimensions: verification, reliability, observability
---

## What it is

A textual claim of success — "the button now works," "the flow completes" — is the cheapest possible evidence, and an agent can emit it without ever having touched the running product. Video-driven development raises the floor: it requires the agent to produce a before-and-after video, or equivalent visual trace, of the real user scenario being completed in the actual interface. The discipline matters less for the artifact than for what producing it forces — to make a video of the scenario succeeding, the agent must drive the real product surface, observe the real behavior, and capture it, which is structurally harder to fake than a sentence. The pattern runs: define the user scenarios before implementation; ask the agent to exercise the current behavior and record it; implement the change; ask the agent to exercise the new behavior and record it; produce the video or visual trace; then review the evidence directly or hand it to a critic agent for inspection. It is especially valuable where the product's truth lives on a visual surface rather than in the code — UI changes, browser-based workflows, mobile and desktop app behavior, onboarding flows, visual regressions, customer-facing scenarios, design-system changes, and accessibility or usability review. Lighter-weight versions substitute screenshots with image diffs, or browser-automation traces, when full video is overkill. The exact medium is negotiable; the rule is not. The system must show, not just assert.

## When to reach for it

- When the change is visual or interactive — UI, onboarding, browser or app flows, design-system or accessibility work — where correctness is only fully visible by watching the scenario run.
- When you have been burned by an agent reporting a UI fix that did not actually work in the running product — a recorded scenario closes the gap between "the code looks right" and "the user can do the thing."
- When evidence will be reviewed by a critic agent rather than a human — a visual trace is a rich, inspectable artifact a critic can evaluate against the stated scenario.
- When a bug is a visual regression with no clean assertion — a before/after capture pins down exactly what changed on screen.
- As a routine acceptance artifact for customer-facing scenarios, so the proof of "it works" is durable and re-inspectable later.

## When NOT to

- For purely non-visual logic (data transforms, API contracts, backend invariants) where a test assertion is a stronger and cheaper proof than a recording.
- When a deterministic check or image diff already proves the same thing more cheaply and more reliably than a full video.
- When capturing the video is so expensive or flaky that the recording apparatus becomes its own source of false failures — use a lighter trace.
- When the scenario cannot be exercised in a realistic environment, so the video would only show a mock — a video of a mock proves nothing about the product.

## Exemplars

- Anthropic — https://www.anthropic.com/news/developing-computer-use — Claude's Computer Use: agents driving the real visual interface and capturing what happens on screen, the technical substrate that makes show-don't-assert evidence possible

## Related

- `patterns/demand-independent-proof.md`
- `patterns/critic-applications.md`
- `patterns/adversarial-parallel-review.md`
- `patterns/finishing-is-the-bottleneck.md`
