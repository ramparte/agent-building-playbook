---
title: Stage Everything, Hand the Human the Trigger
one_liner: When a guardrail blocks the final step, do all the work up to it, hand the human the exact one-line command to fire in-band, and verify the result from its output.
dimensions: workflow-discipline, human-factors, orchestration
---

## What it is

Some final steps are correctly guarded against the agent: the production deploy, the push to an external collaborator's repo, the edit to a protected config file. The two obvious responses to such a gate are both unproductive — negotiate with the guardrail until it yields, or dump the problem back on the human as an unstructured "I can't do this, over to you." Staging everything is the third response: do every piece of work up to the boundary, then hand the human a trigger so small it takes seconds to pull. That means four moves. First, stage to the boundary — build the finished artifact in an unprotected location (a cleaned config in a sibling file, a release in a staging directory) so the guarded step is reduced to a single motion. Second, hand over the exact command — not "you'll need to move the file," but the literal one-line invocation, copy-paste ready. Third, keep the firing in-band — in Claude Code, the human types the command with a `!` prefix so it runs inside the session and its output lands in the conversation, letting the agent read the result and verify the step actually worked instead of taking success on faith. Fourth, narrate what the trigger does — the human's yes should be informed consent, not a rubber stamp, so explain precisely what the command will change before asking anyone to run it. Underlying all of this is a fact worth internalizing: approval given in chat does not transfer executability. Some gates are unclearable while the agent is the one running, no matter how enthusiastically the human says "go ahead" — and that is the design working, not failing. The secrets corollary follows the same shape: secrets may transit the workflow, but they must never land in the transcript, in files, or in logs — piped inline without materializing, sent straight into a secret manager, or typed by the human directly into their own terminal.

## When to reach for it

- When a permission boundary, safety classifier, or protected path blocks the last step of otherwise-finished work — stage the artifact and reduce the human's contribution to one command.
- When the human's approval cannot clear the gate because the gate binds the actor, not the intent — the agent running with permission is still the agent running.
- When you need to verify that the guarded step succeeded — have the human fire it in-band so the output returns to the conversation and the agent can check it rather than assume it.
- When a credential or API key must move through the workflow — route it around the transcript entirely: inline pipes, secret managers, or the human's own keyboard.
- When the human faces several such gates in a session — narrating each command keeps consent informed instead of degrading into reflexive approval.

## When NOT to

- When the gate is wrong rather than right — if a guardrail is blocking work the agent should legitimately do, fix the permission configuration instead of building a permanent human-relay workaround.
- When the "staging" is really circumvention — writing to a shadow copy that a script later swaps into the protected location defeats the gate rather than respecting it.
- When the handed-off step is large or judgment-laden — this pattern hands over a trigger, not a task; if the human must make decisions mid-command, that is a review, not a firing.
- When the block itself is telling you the plan is misshapen — sometimes the answer is not to relay the action but to redesign it (see permission-denial-is-design-feedback).

## Exemplars

- Session history — home-directory sessions, session 447cdff3 (2026) — harness correctly guarded `~/.claude/settings.json`; agent staged the cleaned config to a separate file and handed over the exact `mv` command, which the user ran
- Session history — askkaya sessions, session 364f9218 (2026) — "type these two lines here with a ! prefix (that runs them in-session)"; agent noted the gate "explicitly can't be cleared by your approval while I'm the one running it"
- Session history — askkaya sessions, session 894c86de (2026) — "run them right here by typing them with a leading ! (their output will land in our conversation and I'll verify the results)"
- Session history — sunday-money sessions, session 9d54acbc (2026) — classifier blocked a write; agent narrated "here's exactly the situation so you can decide," handling four-plus blocks with narration for informed consent
- Session history — home-directory sessions, session 511791e2 (2026) — "the API key secret needs to be typed directly into your terminal (never through chat)"; companion askkaya sessions piped a key straight into curl without materializing it

## Related

- `patterns/approval-does-not-transfer.md`
- `patterns/permission-denial-is-design-feedback.md`
- `patterns/earn-the-interruption.md`
- `patterns/governance-is-infrastructure.md`
- `patterns/guardrails-and-escalation.md`
