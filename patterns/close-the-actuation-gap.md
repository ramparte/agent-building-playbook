---
title: Close the Actuation Gap — Don't Ship Guesses Around It
one_liner: When an agent can't physically drive the failing interaction, it must say so at the first fix attempt, bridge with disposable entry points, and eventually build the missing actuator.
dimensions: tool-design, verification, orchestration
---

## What it is

An actuation gap is the space between what an agent can observe and what it can physically do. An agent debugging a mobile app can read the code, take screenshots, and reason about the render tree — but if it cannot tap the button that triggers the bug, every "fix" it ships is an unverified hypothesis wearing the costume of a fix. The failure mode is not the gap itself; it is shipping guesses around it silently. In one real arc, an agent that could not tap an iOS simulator shipped three blind modal fixes that the human dutifully burned cycles testing ("paypal still froze", "still not wokring") before the agent finally admitted: "my last few modal fixes were educated guesses."

The pattern is three escalating moves, each proportional to how often the gap bites:

1. **Declare the limit at fix #1.** The moment the agent proposes a fix it cannot itself exercise, it must say so — out loud, before the human tests anything. This converts unlabeled hypotheses into labeled ones. The human can then decide whether to be the actuator, and knows what evidence their test run actually provides. Three blind fixes shipped before disclosure is the anti-pattern; the disclosure belongs at attempt one, not attempt four.

2. **Bridge with disposable scriptable entry points.** Before guessing again, build a throwaway route to the exact suspect state — a temporary deep-link route that mounts the failing component directly, a debug screen, a seeded fixture. In the sunday-money case, a temp `modaltest` route reachable via `smfs://modaltest` reproduced the real bug "no tap needed" and disproved the reigning "all modals are broken" theory in one shot: the sheet rendered perfectly when presented via deep-link, so the bug lived in the tap-triggered presentation path. Then delete the scaffolding — these entry points are instruments, not features.

3. **When the gap recurs, build the actuator and harvest it.** If the same class of gap keeps interrupting work, the durable fix is tooling, not more clever bridges. Here that meant idb tap injection plus a browser-streamed simulator — converting screenshots-and-hope into drive-and-verify — and then deliberately packaging it as a reusable skill so the investment pays out across projects, not just the session that hurt enough to build it.

## When to reach for it

- The agent is fixing behavior it cannot trigger: taps, gestures, hardware events, third-party OAuth redirects, anything gated behind an interaction surface it lacks.
- A human is acting as the test loop for the agent's changes — that loop is expensive, and every unlabeled guess spends the human's trust and time.
- The same "I can't reach that state" friction has appeared in two or more sessions on a project: that recurrence is the signal to stop bridging and start building the actuator.
- A bug hypothesis can be split into "does the component fail in isolation" versus "does the trigger path fail" — a disposable entry point answers the first half cheaply.

## When NOT to

- The agent can already drive the interaction end-to-end — this pattern is about gaps, not about adding ceremony to verifiable work.
- The disposable entry point would ship: a debug route left in a production build is a security hole, not a bridge. Delete it in the same session that created it.
- The gap is a one-off on a throwaway prototype — building tap injection infrastructure for a demo you will abandon next week fails the proportionality test. Declare the limit (move 1) and stop there.
- Actuating the real surface is destructive or irreversible (live payments, real user data) — declare the limit and route verification through a human or a staging replica instead of building an actuator against production.

## Exemplars

- Session history — sunday-money project, session 9d54acbc (2026) — after three blind modal fixes and repeated user friction, the agent disclosed "I can't tap or click on the simulator... my last few modal fixes were educated guesses," then built a temporary deep-link route that reproduced the real bug "no tap needed," disproved the broad theory, and removed the temp route afterward
- Session history — sunday-money project, session ea3205a0 (2026) — the recurring gap was closed with idb tap injection plus a browser-streamed simulator ("it finally gives me tap ability for testing instead of deep-links-only"), then generalized into a reusable sim-pilot skill developed test-first; the user contrasted it with the old loop: "Before Claude would make me a page with screenshots but I had no idea how the app felt, now with this it works"
- Session history — agent-building-playbook mining run, session 9d77cc45 (2026) — independently surfaced the same arc: temp route `app/(app)/modaltest.tsx` deep-linked via `smfs://modaltest`, noting "This finally cracked a bug that three prior blind fixes hadn't"

## Related

- `patterns/real-environment-execution.md`
- `patterns/agents-optimize-tools.md`
- `patterns/gene-transfer.md`
- `patterns/invest-the-expensive-model-in-the-harness.md`
- `patterns/interrogate-the-artifact.md`
