---
title: Close the Loop From Production Back to Fix
one_liner: Finishing doesn't end at deployment — route support messages, incidents, metrics, and user reports into a triage loop that proposes a fix, validates it, ships it behind a flag, and watches whether the signal disappears; this is the agentic version of a Toyota production system.
dimensions: orchestration, observability, workflow-discipline
---

## What it is

Deployment is not the end of finishing; it is where the most valuable feedback starts arriving, and an agentic system can be wired to consume it. The signals are already there — support messages, Slack threads, production incidents, user reports, metric anomalies — and ordinarily they sit in a queue waiting for a human to notice, triage, reproduce, fix, and ship. A production feedback loop closes that distance by routing the signal directly into an agentic workflow: a user report, support message, incident, or metric anomaly appears; an agent triages it against known issues and recent changes; the agent determines whether it is actionable; if it is low risk, the agent opens a branch and proposes a fix; a validation workflow runs against that fix; a human approves or rejects depending on the assessed risk; the fix ships behind a feature flag or staged rollout; the system watches whether the originating feedback actually disappears; and the learning is captured into the knowledge base so the same class of problem is recognized faster next time. What makes this powerful is that it compresses the loop between user pain and product change, and what makes it safe is that the loop never skips its controls — validation, risk-gated human approval, staged exposure, and a watch for whether the signal cleared. This is the agentic version of a Toyota-style production system: observe defects at the source, reduce batch size so fixes flow continuously rather than in large risky releases, close the feedback loop so problems train the system, and improve the process itself rather than just patching outputs.

## When to reach for it

- When real user-facing signal (support, Slack, incidents, error rates, metric anomalies) is already accumulating faster than humans triage it — route it into an agent loop that proposes triaged, validated fixes.
- When you want to shorten the distance between a reported defect and a shipped fix without removing the human approval gate for risky changes.
- When the same classes of issue recur — wire the loop to capture each resolution into the knowledge base so recognition and triage improve over time.
- When you can bind a fix to its originating signal and watch whether the signal disappears — closed-loop confirmation that the fix actually worked, not just merged.
- When you want continuous small corrections rather than large batched releases — the loop favors small, reversible, observed changes.

## When NOT to

- When fixes cannot ship safely behind a flag or staged rollout, or have no rollback — without exposure controls, an automated fix loop is an automated incident loop.
- When the feedback signal is too noisy or ambiguous to triage reliably — a loop that acts on misread signals manufactures churn and erodes trust.
- For high-risk changes where every fix needs deep human judgment regardless — the loop's value is in compressing low-risk, well-understood fixes, not in bypassing judgment on dangerous ones.
- When there is no telemetry to confirm whether the originating signal cleared — without the closing watch, you have an open loop that ships fixes blind.

## Exemplars

- Toyota Production System — https://en.wikipedia.org/wiki/Toyota_Production_System — the lean discipline this pattern adapts: observe defects at the source, reduce batch size, stop-the-line on signal, and improve the process rather than the symptom
- DORA, "Working in small batches" — https://dora.dev/capabilities/working-in-small-batches/ — empirical support: names small batches as essential wherever feedback loops matter — reducing the time to get feedback on changes and making problems easier to triage and remediate
- Xia et al., "Evaluation-Driven Development and Operations of LLM Agents: A Process Model and Reference Architecture" (arXiv:2411.13768) — https://arxiv.org/abs/2411.13768 — formalizes production feedback as a continuous governing loop (EDDOps): offline evaluation, online monitoring, and iterative redevelopment form a closed cycle rather than a terminal pre-deployment checkpoint

## Related

- `patterns/separate-merge-from-exposure.md`
- `patterns/mine-transcripts.md`
- `patterns/fix-the-root-cause.md`
- `patterns/finishing-is-the-bottleneck.md`
