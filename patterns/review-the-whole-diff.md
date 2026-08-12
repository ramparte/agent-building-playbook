---
title: Per-Task Review Can't Catch Plan Bugs — Review the Whole Diff Too
one_liner: Reviewers scoped to "faithful to the brief" cannot catch bugs in the brief itself or defects between tasks — run one consolidated whole-diff review on the strongest model.
dimensions: verification, orchestration, cost-routing
---

## What it is

In plan-driven subagent pipelines, each task ships with a brief, and each per-task reviewer answers one question: is this implementation faithful to its brief? That is a compliance gate, and it is worth running — it catches implementer shortcuts, deviations, and sloppiness cheaply, task by task. But it is structurally incapable of catching two other classes of defect. First, bugs in the plan itself: if the plan's own reference code contains a correctness error, a faithful implementation of that error passes the compliance gate by definition — the reviewer is judging conformance to the very artifact that carries the bug. Second, integration defects: mismatched contracts between tasks, missing tenant scoping across a service boundary, behavior that unit tests "verified" only because a faked collaborator hid the real interaction. These defects live *between* briefs, in territory no single-task reviewer was ever handed.

The pattern is to treat these as two different gates and run both. Per-task review stays compliance-scoped, cheap, and frequent. Then, at the end of the plan — or per pillar/phase in a large one — run one consolidated review over the entire integrated diff, with a mandate that explicitly includes challenging the plan: not "did the implementer follow the brief?" but "is this branch correct?" Because this pass is where the subtle, high-stakes findings surface, it warrants the most capable model you have — this is exactly the reviewer/critic row of stage-based model routing. In the observed sessions, the final whole-diff pass found a Critical both times it ran, after every per-task review had approved.

## When to reach for it

- You are orchestrating a plan-driven pipeline where subagents implement tasks against written briefs and per-task reviewers check brief compliance.
- The plan itself contains reference code, schemas, or contracts that implementers copy — plan-authored bugs will be faithfully reproduced and per-task review will bless them.
- Tasks touch a shared boundary — a common API, a multi-tenant datastore, a wire contract — where the defect only exists once the pieces meet.
- Per-task unit tests rely on faked collaborators; the consolidated pass is the first look at whether the real interaction behaves.
- Findings from earlier phases (e.g., a known bug class like tenant scoping) should be a named focus of the consolidated review, so the pass verifies the class is not repeated.

## When NOT to

- Single-task changes with no plan and no task boundaries — there is only one diff, and an ordinary review already covers it; a second "consolidated" pass is the same pass.
- As a replacement for per-task review. Dropping the compliance gates and relying on one final pass turns the whole-diff review into a giant, late, expensive catch-all — defects that were cheap to fix at task time now arrive all at once at the end.
- When the integrated diff is too large for any reviewer to hold. That is a signal to consolidate per pillar or phase rather than once at the very end — the observed sessions converged on one consolidated review per pillar.
- When a deterministic check (integration test suite, contract test) already exercises the boundary in question — run it first; spend the strong-model review on what only judgment can catch.

## Exemplars

- Session history — home-directory sessions, session 511791e2 (2026) — after six approved per-task reviews, the final whole-branch review ("running on Opus — most capable model, per the skill's guidance") caught a real Critical: the judge client indexed `content[0]` assuming a text block — "a correctness bug in my own plan's reference code"; earlier findings in the same run were likewise "plan-inherited gaps... present in the plan's own reference code, not implementer shortcuts"
- Session history — askkaya/Bestmate sessions, session 364f9218 (2026) — the consolidated Pillar 2 review found "one Critical cross-tenant data leak in cliEvalsApi... exactly the kind of integration bug per-task review misses"; a final review also "caught a real Important bug that the faked-collaborator unit tests couldn't"; the orchestrator standardized on "one consolidated review per pillar (opus, whole-pillar diff — which is what caught the Pillar 1 integration bug) rather than per-task"

## Related

- `patterns/adversarial-parallel-review.md`
- `patterns/match-model-to-stage.md`
- `patterns/architect-then-builder.md`
- `patterns/gate-the-phases.md`
- `patterns/review-findings-are-hypotheses.md`
- `patterns/propagate-the-bug-class.md`
