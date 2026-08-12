---
title: Propagate the Bug Class, Not Just the Fix
one_liner: Treat each fixed bug as a class — sweep siblings for the same defect, name it in later briefs and reviews, and verify it as a spec checklist item.
dimensions: workflow-discipline, knowledge, reliability
---

## What it is

A found defect is rarely a point event. It is evidence about a habit — the codebase's habit of writing a certain shape of mistake, or the plan's habit of not guarding against it — and a habit that produced the bug once has almost certainly produced it elsewhere and will produce it again. The default agent behavior is to fix the instance, report success, and move on; the pattern is to refuse to close the loop until the *class* has been propagated through three channels. First, the **lateral sibling sweep**: the moment a fix lands, hunt for the identical anti-pattern in adjacent code. An agent that fixed an unbounded scan on one collection immediately checked its siblings, found the same full-table load on articles, measured it at roughly the same latency, and fixed it in the same pass — the second bug never got the chance to become next week's incident. Second, **forward injection**: a bug class discovered in one phase of work becomes a named constraint in the briefs for later phases and a named focus for their reviews. A cross-tenant leak found during one pillar of a build turned into an explicit design rule ("the service takes a caller-resolved tenantId; endpoints enforce scoping") in the next pillar's briefs, and the consolidated review of that pillar was pointed squarely at tenant scoping — and could then certify, in so many words, that the earlier bug class was not repeated. Third, **spec encoding**: the class is written into the spec as a checklist item that a later pass must actively verify, not merely remember. After a 256MiB out-of-memory failure, the spec gained a line requiring 1GiB for any endpoint on the heavy path; the next sprint explicitly checked it off ("both draft endpoints are already at 1GiB — checklist item satisfied"). One fix repairs one line of code; propagation converts the incident into a rule the whole project now runs under.

## When to reach for it

- The moment any nontrivial fix lands — the sibling sweep is cheapest right then, while the anti-pattern's exact shape is loaded in context.
- When the codebase has structural repetition — parallel collections, sibling endpoints, per-tenant handlers — where one instance of a mistake strongly predicts others.
- When work is phased or delegated: a class found in phase two should arrive in phase four's briefs as a named design rule and in its review as a named focus, or the fresh-context agent will happily reintroduce it.
- When a failure was resource- or configuration-shaped (memory limits, quotas, scoping rules) — encode it as a spec checklist item, because "remember the OOM" does not survive a context boundary but "checklist #13: 1GiB on any endpoint calling processAsk" does.
- When a reviewer signs off — ask the review to confirm the known bug classes explicitly, so "not repeated" is a verified claim rather than an assumption.

## When NOT to

- The bug is genuinely singular — a typo with no structural twin. Sweeping for siblings of a one-off is theater; note it and move on.
- The class is already fenced by an automated check (a lint rule, a test, a type). Prefer promoting the class into the machine over adding another human-verified checklist line.
- The checklist is becoming a graveyard — if items accumulate without ever being verified on a later pass, the third channel has silently failed, and the fix is fewer, sharper items, not more.
- Time-critical mitigation comes first; propagate the class as scheduled follow-up, not as a reason to delay stopping the bleeding.

## Exemplars

- Session history — askkaya project, session a4a7867f (2026) — after fixing an unbounded chunk scan, the agent immediately flagged "the identical anti-pattern I just fixed" on the articles collection, measured it (~5s), and fixed it in the same pass
- Session history — askkaya project, session 364f9218 (2026) — a cross-tenant leak from Pillar 2 became a named design rule in Pillar 4 briefs and a named review focus; the review then confirmed "the Pillar 2 bug class is not repeated"
- Session history — askkaya project, session 2e48cbbe (2026) — a 256MiB OOM was encoded as a spec checklist item (1GiB for any endpoint calling processAsk) and explicitly verified the next sprint

## Related

- `patterns/fix-the-root-cause.md`
- `patterns/good-pile-bad-pile.md`
- `patterns/agent-struggle-is-a-signal.md`
- `patterns/review-the-whole-diff.md`
- `patterns/untracked-state-does-not-travel.md`
