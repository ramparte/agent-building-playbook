---
title: Verify the Human's Step Like an Agent's Claim
one_liner: When a human performs a step — a GUI download, a release, "I already did that" — verify their report the way you verify an agent's "done," with a machine check.
dimensions: verification, human-factors
---

## What it is

Verification patterns in this playbook mostly point one direction: don't trust an agent's self-report of completion; check the artifact. But agentic workflows routinely contain steps only the human can perform — clicking through a GUI installer, approving a release in a web console, toggling a setting the agent can't reach — and the human's "done" is a claim of exactly the same kind. It fails for different reasons: the agent fabricates or overstates, while the human is misled by the interface. Settings panes report success while the underlying resource is unusable; memory conflates "I tagged the release" with "the release shipped"; a download completes but the asset it delivered is silently broken. The failure mode is identical either way — an assertion of completion with no independent evidence behind it.

The pattern has two halves. First, when handing a step to the human, deep-link them to the exact pane or screen where the action happens, so their step is as unambiguous as a tool call. Second, after each "done," run the machine check at the surface where the work becomes real — not the settings UI that claims the voice was installed, but whether the speech command actually produces sound; not the tag on the source repo, but whether the auto-update feed actually serves the new version. This is symmetric respect, not distrust: the check is cheap, it closes the loop the same way it would for any agent, and it frequently surfaces constraints the UI never showed. When the human insists "bro i already did that," the productive response is not to argue or to re-explain — it is to check the actual state, because usually both parties are about to learn something the interface hid from them.

## When to reach for it

- A workflow step can only be performed by the human through a GUI, web console, or physical action, and downstream work depends on it having actually taken effect.
- The human reports a step complete but downstream behavior suggests otherwise — verify the real surface before debugging anything else.
- The system of record and the surface that matters can diverge (a release tagged at the source but absent from the distribution feed, a setting saved but not applied).
- You are about to build on top of "I already did that" — a ten-second programmatic check is cheaper than an hour diagnosing a phantom bug.
- The UI confirms success in terms of its own state ("download complete," "saved") rather than in terms of the outcome you actually need.

## When NOT to

- Don't turn every human report into an interrogation. Repeatedly double-checking a collaborator's trivial, self-evident actions reads as distrust and erodes the working relationship; run the check where it is cheap and silent, or where the stakes genuinely warrant it.
- When the human's step is immediately observable in the shared context anyway — the file appeared, the diff is visible — an extra verification pass adds ceremony, not evidence.
- When no machine-checkable surface exists (a purely offline or judgment-based step), asking the human targeted questions beats pretending a check is possible.
- When the check itself is expensive or disruptive relative to the cost of the step being wrong — reserve the loop for steps that downstream work actually depends on.

## Exemplars

- Session history — montreal project, session f835ca51 (2026) — Instead of trusting the macOS voice-settings UI, the agent tested "whether `say` can speak" after each human download step; three verification loops revealed that voices reported as installed went completely silent on Japanese text.
- Session history — askkaya project, session ea9d9a0c (2026) — User: "bro i already did that THO"; agent checked the actual state and found the auto-update feed still on v2.6.0 — releases 2.7.0 and 2.8.0 were tagged on the source repo but never reached the feed.

## Related

- `patterns/verify-independently.md`
- `patterns/demand-independent-proof.md`
- `patterns/earn-the-interruption.md`
- `patterns/interrogate-the-artifact.md`
