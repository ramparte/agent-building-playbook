---
title: Automate the Easy, Avoid the Mystery House
one_liner: Automate what you understand completely; never automate your way into a system where nobody knows why it works or what it does.
dimensions: taste, workflow-discipline
---

## What it is

Automation is a multiplier on understanding. When you automate something you understand completely — the exact inputs, the exact transformation, the exact expected outputs, and all the failure modes — you get a reliable, fast, inspectable process that runs with less effort than its manual counterpart. When you automate something you do not fully understand, you build a mystery house: a system that produces outputs, usually correctly, through a process nobody can explain. The mystery house grows over time because automation invites extension. New cases get added to a system that already isn't understood; the automation handles them because it handles everything; nobody inspects why; the system becomes larger and less intelligible. In agentic systems, mystery houses are especially dangerous because agents operate with autonomy — a mystery-house agent can run for a long time, producing outputs that look reasonable, while doing something subtly wrong in ways that are difficult to diagnose precisely because the underlying process is opaque. The discipline: automate aggressively in areas where you have complete understanding, and resist automation in areas where the understanding is incomplete. If you cannot explain the full logic to someone else in ten minutes, you do not yet understand it well enough to automate it.

## When to reach for it

- When considering automating any non-trivial process: write out the full logic manually first; if you cannot, get that understanding before writing the automation.
- When an existing automated system starts behaving unexpectedly: before fixing the behavior, verify you understand why the fix works; a fix you don't understand is another layer of mystery.
- When an agent is automating a workflow: ensure you can trace its decisions for any representative input; if you cannot, the automation is ahead of your understanding.
- When reviewing automation built by others (or by an AI agent): ask "can I explain what this does in full?" before accepting it as a dependency.
- When the system has been running long enough that people have forgotten why certain parts work: treat that as a debt to be paid, not a feature to be extended.

## When NOT to

- Not an argument against automating complex things: complexity and opacity are not the same thing. A complex process that is fully understood is a good candidate for automation; a simple process that is not understood is not.
- Not an argument for perfectionism before automation: "complete understanding" does not mean perfect understanding — it means you can articulate the logic, the failure modes, and the expected behavior. Paralysis is the failure mode in the opposite direction.
- Not applicable to exploratory automation: prototyping automation to learn what a process actually does is legitimate and useful — treat the prototype as throwaway, not as production infrastructure.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: warns that autonomous agents can compound errors and cause hard-to-reverse mistakes, recommending extensive testing in sandboxed environments before deployment
- Amplifier — https://github.com/microsoft/amplifier-bundle-recipes — recipes declare workflows as YAML steps executed in stages with automatic checkpointing and requires_approval gates — the workflow's structure and each stage's status stay inspectable rather than sealed inside an opaque autonomous run
- Drew Breunig, "The Cathedral, the Bazaar, and the Winchester Mystery House" — https://www.dbreunig.com/2026/03/26/winchester-mystery-house.html — coins the metaphor this pattern is built around: AI-cheapened code production generates sprawling, idiosyncratic systems that are inscrutable to outsiders and usually lack documentation — the original source for the "mystery house" framing in AI-era software

## Related

- `patterns/auditable-artifacts.md`
- `patterns/develop-your-taste.md`
- `patterns/reliability-before-features.md`
- `patterns/find-the-hard-stuff.md`
