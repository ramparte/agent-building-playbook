---
title: Evidence Before Assertions
one_liner: A claim about a system's state is not knowledge — it is a hypothesis. Run the verification command and read the output before making any assertion about whether something worked.
dimensions: verification, reliability
---

## What it is

An assertion about a system's state that is not backed by independently gathered evidence is not a claim of fact — it is a guess with high confidence. "The tests pass" means something only if you ran the tests in this session, read the full output, and confirmed the count of passing and failing tests. "The file was written" means something only if you read the file back and verified its contents. "The service is healthy" means something only if you queried the health endpoint and read the response. The pattern seems obvious and yet fails constantly in agentic workflows: the agent performs an action, assumes the action had the intended effect, and proceeds to the next step on the basis of that assumption. When the assumption is wrong — which happens more often than intuition suggests, because errors are quiet and successes are loud — every subsequent step builds on a false foundation, and the resulting failure is both delayed and distant from its cause. Evidence before assertions breaks this by making the verification step non-optional: before any assertion is made (to an orchestrator, to a human, in a handoff artifact), the evidence that justifies the assertion must have been gathered and read in the current execution context.

## When to reach for it

- Before any completion claim: identify what command or read operation would prove the claim, run it, read the full output including the exit code, and then make the claim based on what you observed.
- After any tool call that modifies state (writes a file, calls an API, modifies a database): read back the result before assuming the action succeeded.
- When debugging: gather evidence from the system before forming a hypothesis. Hypothesis-first debugging with evidence-last confirmation produces fixes for the wrong problem.
- When reviewing an agent's output that claims success: ask "what is the evidence?" before accepting the claim. If the evidence is the agent's own assertion, it is not evidence.
- Before any irreversible action (send, delete, deploy): gather evidence that the pre-conditions are exactly what you believe they are. Evidence of the state before the action is as important as evidence of the state after.

## When NOT to

- When the evidence is immediately visible in the current context and requires no additional observation — a string returned by an LLM in the same turn is immediately observable and needs no additional verification step.
- When the cost of gathering evidence exceeds the cost of the error it would prevent, and the error is easily reversible — proportionality applies; not every action requires a full verification pass.
- When the evidence cannot be gathered because the system is not observable — in that case, the correct response is to flag the observability gap, not to proceed on assumption. Unobservable actions are dangerous regardless of how confident you are in their success.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends human-in-the-loop checkpoints and independent verification of agent outputs; "trust but verify" is replaced with "verify before asserting"
- Amplifier — https://github.com/microsoft/amplifier — the honest-stopping principle: when a required item cannot be satisfied with real evidence, the agent must stop and report rather than fabricate a plausible-looking result; a fabricated attestation is worse than an honest gap

## Related

- `patterns/demand-independent-proof.md`
- `patterns/verify-independently.md`
- `patterns/self-verification.md`
- `patterns/fail-loud-over-fallbacks.md`
