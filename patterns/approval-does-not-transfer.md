---
title: Approval Doesn't Transfer
one_liner: Consent is scoped — a yes to the plan does not cover the production release inside it, and authorization given to the orchestrator is invisible to its subagents.
dimensions: human-factors, reliability, workflow-discipline
---

## What it is

Approval is not a status an agent acquires and then carries around; it is scoped consent, and it fails to transfer along three specific axes. **Across blast radius:** a bundled "yes" to a plan does not cover the individually consequential actions inside it — a production release that auto-updates real users, or an identity grant that binds an account while bypassing SMS verification, each needs its own named consent, even when the surrounding work was approved wholesale. The inverse holds too, and calibrates the rule: when the human physically attempts the deploy command themselves, that act *is* consent — "you attempting the deploy is a clear green light" — so the point is scope, not ceremony. **Across actors:** authorization given to the orchestrator is not visible to the permission layer evaluating a subagent's actions. A subagent that deploys a Cloud Function will be flagged for "deploying to production without any explicit user request" even when the human explicitly authorized it two messages upstream, because that authorization lives in the orchestrator's context, not the subagent's. The practical responses: carry the authorization into the subagent's brief, run the gated step in the orchestrator itself, or expect the flag and interpret it correctly rather than treating it as a new prohibition. **Across time and ambiguity:** consent decays and can be walked back by later messages — a classifier reasonably read "ok no, I meant..." as revoking an earlier "just merge the PR," so an approval separated from its action by confusion or contradiction should be re-confirmed, not replayed. There is a visibility corollary: a pending approval gate must be loudly signposted. A design sign-off gate that gets silently parked does not read to the human as "waiting on you" — it surfaces later as a bug report ("i do not see the paywall"), because from the outside an un-signposted gate is indistinguishable from a broken feature.

## When to reach for it

- When a plan approved as a whole contains steps with larger blast radius than the plan's framing implied — production releases, identity or permission grants, spend commitments — surface each for its own named yes.
- When delegating a gated action to a subagent whose permission layer cannot see the human's authorization — put the authorization in the brief, keep the gated step in the orchestrator, or pre-explain the expected flag.
- When an approval and its execution are separated by time, a context compaction, or an ambiguous message that might have walked it back — re-confirm rather than replay.
- When work is blocked on a human sign-off — say so explicitly and repeatedly; a silently parked gate becomes a bug report.
- When a security warning fires on an action the human did authorize — adjudicate it as a visibility gap, not a violation, and say which it was.

## When NOT to

- When the action is cheap, reversible, and inside the approved scope — re-asking for consent the human already gave spends attention and trains rubber-stamping.
- When the human is attempting the action themselves — the attempt is the consent; demanding a verbal yes on top is ceremony.
- When a standing policy explicitly pre-authorizes a class of actions — the fix for repetitive approvals is a declared policy, not per-instance nagging.
- When the real gap is a missing guardrail rather than missing consent — if a validator or action limit can bound the risk, bound it there.

## Exemplars

- Session history — askkaya project, session a6d5f567 (2026) — production deploy flagged because the user "hadn't explicitly asked for a deploy"; the user then attempting the deploy command themselves was read as a clear green light; a Telegram identity grant bypassing SMS verification required its own sign-off
- Session history — askkaya project, session e070ad52 (2026) — "a production release to real users needs your explicit go-ahead rather than a bundled 'yes'"
- Session history — askkaya project, session 364f9218 (2026) — subagent's authorized prod deploy still triggered a security warning because the human's go-ahead was invisible to the subagent's permission layer; a classifier read "ok no, I meant..." as walking back an earlier merge instruction
- Session history — askkaya project, session 8d2e6d9a (2026) — "i do not see the paywall": a design sign-off gate parked without signposting surfaced as a bug report
- Session history — home project, session 511791e2 (2026) — orchestrator declined to delegate creating a real Cloudflare D1 database to an autonomous subagent without the human's go-ahead

## Related

- `patterns/earn-the-interruption.md`
- `patterns/autonomy-when-justified.md`
- `patterns/governance-is-infrastructure.md`
- `patterns/stage-everything-human-fires.md`
- `patterns/gate-done-with-a-stop-hook.md`
