---
title: Mine for Contradictions
one_liner: Contradictions are high-signal — they reveal where an organization has changed its mind without updating its artifacts or has never reconciled competing goals; run a detector across transcripts, specs, and decisions that surfaces conflicts for discussion rather than auto-fixing them.
dimensions: knowledge, intent, verification
---

## What it is

A contradiction inside an organization's body of knowledge is rarely a simple error to be patched — it is a high-signal indicator that two real things are in tension. Either the organization changed its mind and never updated the artifacts that encode the old position, or it never reconciled two goals it genuinely holds at once. A contradiction detector treats this as knowledge work: it runs across transcripts, notes, docs, specs, and decisions and asks a focused set of questions. Where are two incompatible things being asserted? Where did someone's mind change without the spec following? Where does a plan violate a stated value? Where are customer signals inconsistent with the stated product direction? Where do two teams use the same term to mean different things? The yield is concrete and uncomfortable: a team says speed matters but keeps approval gates that destroy autonomy; a product claims to serve operators but optimizes for executive dashboards; a company says it wants leverage but measures only headcount reduction; a spec declares a workflow deprecated while support tickets show users still depend on it; an agent is instructed not to use a workaround while that very workaround still lives in its own historical notes. The critical design constraint is that the output must make the contradiction discussable, not resolve it automatically. Auto-fixing a contradiction silently picks a winner between two positions a human deliberately or accidentally holds — which is exactly the judgment call that should surface to people, not be buried by a tool.

## When to reach for it

- When mining a transcript or document corpus — contradiction extraction is one of the highest-value derived artifacts you can produce from it.
- When a spec, plan, or set of stated values has drifted from observed behavior, and you suspect the artifacts no longer reflect reality.
- When two teams keep talking past each other — the same term used two ways is a contradiction worth surfacing explicitly.
- When validating that an agent's own instructions, notes, and policies are internally consistent before trusting it on a long-horizon task.
- When intent matters more than output: contradictions expose unreconciled intent that no amount of polishing the deliverable will fix.

## When NOT to

- When the contradiction is trivial or already known and tracked — surfacing it again is noise, not signal.
- As an auto-remediation step — never let the detector silently rewrite one side of a conflict to match the other; that destroys the very signal you mined for.
- When the two "contradictory" statements are context-dependent and both correct in their own scope — a detector that cannot distinguish scope will generate false positives that erode trust.
- When there is no human or forum prepared to actually discuss the surfaced conflicts — a contradiction list nobody triages is just another unread artifact.

## Related

- `patterns/keep-specs-in-sync.md`
- `patterns/mine-transcripts.md`
- `patterns/interview-to-a-spec.md`
