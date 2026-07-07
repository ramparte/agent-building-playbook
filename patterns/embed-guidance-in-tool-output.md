---
title: Embed Guidance in Tool Output
one_liner: Instead of front-loading every project gotcha into a giant instructions file the model forgets, put the guidance in the outputs of scripts and tools — error and success messages — so the reminder appears exactly where and when it is relevant.
dimensions: context-engineering, tool-design
---

## What it is

Every project has small recurring gotchas, and the reflex is to document them all upfront in a CLAUDE.md or system prompt — but that path bloats the instruction file, and the more you cram in, the less reliably any single line lands. A better delivery mechanism is to push the guidance into the environment itself: embed it in the outputs of the scripts and tools the agent already runs — error messages, success messages, CLI responses — so the reminder surfaces at the exact moment it is relevant and nowhere else. This is precisely what good software has always done for humans: a well-written error message guides you to the fix, and the same design works for agents. Instead of a standing line that says "always run migrations before deploying", have the deploy script detect pending migrations and print "pending migrations detected — run `./migrate.sh production` before deploying". Instead of a note that a permissions script is production-only, have the script check its environment and answer "this script should only be run on the production server". The guidance is now unmissable, self-scoping, and costs nothing until it is needed — and it serves people and agents with the same artifact, instead of a separate rulebook that both have to remember to read. It inverts the usual context economy: rather than paying for every gotcha on every run by carrying it in the prompt, you pay for a gotcha only when the situation that triggers it actually occurs.

## When to reach for it

- When you are tempted to add yet another gotcha to CLAUDE.md — ask whether the tool that trips over it could just say so at the point of failure instead.
- When both humans and agents keep hitting the same obscure error — fix it once in the tool's output, and both are guided.
- When an instruction only matters in a specific situation (an environment, a state, a command) — let the tool detect that situation and emit the guidance then, rather than always-on.
- When the instructions file has grown large enough that individual lines are losing reliability — move situational guidance out of the file and into the outputs where it fires.

## When NOT to

- When the guidance is genuinely global and always applies — some things do belong in the standing instructions, not behind a specific tool invocation.
- When you do not control the tool's output and cannot wrap it — you may have to keep the reminder in context or in a wrapper script.
- When adding messaging to a tool would clutter output that humans rely on — design the message to help both audiences, not to spam one for the other.

## Exemplars

- Ivett Ördög (devill) — https://github.com/lexler/augmented-coding-patterns/blob/main/documents/patterns/contextual-prompts.md — "Contextual Prompts," the source this pattern is adapted from (embedding migration and environment gotchas in deploy/permissions script output)

## Related

- `patterns/just-in-time-retrieval.md`
- `patterns/persist-environment-facts.md`
- `patterns/tools-for-agents.md`
- `patterns/fail-loud-harnesses.md`
- `patterns/context-is-finite.md`
