---
title: Rebuild Often
one_liner: Regular rebuilds from scratch catch accumulated drift that incremental changes normalize.
dimensions: workflow-discipline
---

## What it is

Systems built through incremental changes accumulate invisible assumptions. Each change is local and correct in isolation; the aggregate is a system that works under conditions that have not been tested together from a clean state. Rebuilding often — re-running the full build from scratch, re-provisioning environments from their definitions, re-generating outputs from source — forces hidden dependencies to surface as explicit failures rather than silent breakage. In AI workflows, this applies directly to prompt pipelines, context assemblies, and agent configurations: if the system has never been tested cold, you do not know what it actually depends on.

## When to reach for it

- Before declaring a workflow stable: run it from a clean state, not from a warm environment that has accumulated setup history.
- When onboarding a new machine, environment, or agent: the first run from scratch reveals everything that was undocumented.
- After any period of incremental patching: stop and rebuild from the canonical definition to see what the patches have obscured.
- Periodically as a health check in long-running systems: scheduled cold runs detect drift before it becomes an incident.
- When a workflow works on one machine and fails on another: the discrepancy is almost always state that the working machine accumulated and did not document.

## When NOT to

- When rebuild time is prohibitive and the system's reproducibility is already verified through other means (e.g., fully reproducible builds with pinned dependencies and artifact caching).
- In exploratory development where the goal is to accumulate working state rapidly — defer rebuild discipline until the system is stable enough to formalize.
- When the rebuild process itself has side effects (billing, provisioning external resources, contacting external APIs) that make frequent rebuilds expensive or disruptive.

## Exemplars

- Infrastructure-as-code practitioners treat "destroy and recreate" as a first-class hygiene operation — the environment definition is only real if it survives a rebuild from scratch.
- The Amplifier pattern of running `amplifier reset` to clear cached state and verify the system works from a clean installation is rebuild discipline applied to the toolchain itself.
