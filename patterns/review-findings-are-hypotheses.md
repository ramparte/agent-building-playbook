---
title: Review Findings Are Hypotheses, Not Orders
one_liner: Treat every review finding as a claim to verify against the code, adjudicate reviewer-fixer contradictions with an isolated reproduction, and route plan-mandated flaws to the plan's owner.
dimensions: verification, orchestration, workflow-discipline
---

## What it is

A review finding is a claim with a provenance, not an instruction. The reviewer that produced it saw one slice of the work, under one brief, with one set of assumptions — so the finding inherits that reviewer's blind spots exactly the way the code inherited its author's. An orchestrator that pipes findings straight into fix agents is laundering unverified claims into code changes. The discipline has three moves.

First, **verify the finding against the code before dispatching a fix**. The orchestrator typically holds cross-task context that no single reviewer has — how the pieces integrate, what an earlier task already guarantees, which invariants hold by construction. Read the flagged code yourself with that context loaded. Findings get confirmed, but they also get rejected: a flagged gap that a sibling task already closes is a non-gap by construction, and fixing it would add code for a problem that does not exist.

Second, **adjudicate contradictions with an isolated reproduction, not by authority**. When a fixer comes back saying the reviewer's premise was wrong, you have two agents making opposite claims about the same behavior, and neither recency nor role tells you who is right. Do not pick a winner — dispatch an adjudicator that rebuilds the disputed condition in a clean environment, outside the working checkout, and probes what actually happens. In practice this resolves the dispute in ways neither party predicted: the observed case found the reviewer's premise wrong *and* the fixer's stated mechanism partly wrong, even though the fixer's outcome was correct. Only reproduction surfaces that third answer.

Third, **route confirmed findings by decision owner**. A flaw the implementer introduced by deviating from its brief is the orchestrator's to fix directly — no ceremony needed. But a flaw the approved plan itself mandated is different in kind: the plan was a human decision, and silently "fixing" it overrides that decision without the decider knowing. Plan-mandated findings go to the plan's owner for a call; implementer deviations get fixed on the spot. The question that sorts every finding is not "is this wrong?" but "whose decision produced it?"

Together the moves turn review from a command channel into an evidence channel: reviewers generate hypotheses; the orchestrator tests them, resolves conflicts empirically, and escalates the ones that touch decisions above its pay grade.

## When to reach for it

- When you orchestrate reviewer and fixer subagents and their outputs feed each other — any pipeline where a finding can become a code change without a human in between.
- When the orchestrator holds integration context individual reviewers lack — cross-task contracts, sibling-task guarantees, plan-level intent — and can therefore reject findings reviewers had no way to reject.
- When a fixer disputes a reviewer's premise — that contradiction is a signal to reproduce, not a tiebreak to eyeball.
- When the work follows an approved plan — some fraction of findings will trace to the plan itself, and those need the plan owner's call, not a silent patch.
- When review volume is high enough that acting on every finding uncritically would churn the codebase with fixes for phantom problems.

## When NOT to

- When a deterministic check settles the finding — a failing test or a compiler error is not a hypothesis; run it and act.
- When there is no plan and no delegation — a solo developer reading their own reviewer's comment can just check the code; the routing move has no owner to route to.
- When the finding is trivially cheap to fix and trivially safe — adjudication machinery on a typo is pure overhead.
- When you lack the context to verify — an orchestrator with no more visibility than the reviewer adds nothing by second-guessing it; escalate or reproduce instead of vibing a verdict.

## Exemplars

- Session history — home-directory sessions, session 511791e2 (2026) — reviewer flagged an Important issue that was plan-mandated ("my own plan specified sequential inserts... a plan-mandated finding needs your call, not a silent override") and was escalated, while three other Important findings were implementer deviations fixed directly
- Session history — home-directory sessions, session 511791e2 (2026) — a fixer contradicted the original reviewer's localStorage premise; an adjudicator built an isolated reproduction outside the checkout and found the reviewer's premise wrong and the fixer's stated mechanism partly wrong too, with only the fixer's outcome correct
- Session history — askkaya sessions, session a4a7867f (2026) — two reviewers disagreed on a Critical; the controller read the code directly, confirmed the Critical for the exact failing path, and rejected other flagged gaps as "non-gaps by construction" using cross-task context no reviewer held

## Related

- `patterns/review-the-whole-diff.md`
- `patterns/adversarial-parallel-review.md`
- `patterns/auditor-agent.md`
- `patterns/critic-applications.md`
