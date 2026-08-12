---
title: Gate "Done" With a Machine-Checked Stop Condition
one_liner: Encode the finish line as a harness-enforced stop condition the agent cannot end its turn without satisfying, and treat the gate's text as code that can have bugs.
dimensions: workflow-discipline, reliability, orchestration
---

## What it is

A stop condition the agent merely knows about is advisory. It lives in the prompt alongside everything else competing for attention, and when the agent feels done — build passed, summary written — nothing stops it from ending the turn with the actual goal unmet. A stop condition the harness enforces is a gate: a Stop hook (optionally backed by an LLM judge) that inspects the session when the agent tries to finish and blocks the stop until the condition holds. This converts "please finish X" from hopeful instruction into machine-checked invariant.

The mechanism works for a reason worth naming: the agent's sense of "done" is a self-report, and self-reports drift toward whatever feels complete. The gate replaces that feeling with an external check at exactly the moment it matters — the moment of stopping. In practice the forced continuation does more than extend the run. When a hook told one session "Building is not finished until the portal is live and tested end-to-end," the agent responded: "The hook's right that I shouldn't stop here — and re-examining the evidence, my first diagnosis deserves a harder look." The gate didn't just prevent a premature stop; it produced a better diagnosis than the first attempt, because the agent was forced back into the problem after it had already committed to an answer.

But the gate enforces its literal text, and that text is code. A typo in the condition is not a typo — it is a mandate. A condition that quietly requires something the agent cannot do unattended is a deadlock. A condition nobody cleared after the goal changed is a nagging ghost. Write the condition with the same care you'd give a script that runs with force flags, and give the human — not the agent — the job of amending it.

## When to reach for it

- Long multi-phase runs where the agent has historically stopped at a plausible-looking midpoint ("phase 1 done, summarizing") instead of the actual finish line.
- Delivery-shaped goals with a concrete observable endpoint — "the video is on my desktop," "the deploy is live and tested" — that a hook or judge can check.
- Unattended or overnight sessions, where there is no human present to notice a premature stop and say "keep going."
- When you catch yourself re-prompting "you're not done yet" more than once per session — that correction is a stop condition waiting to be encoded.

## When NOT to

- **When the condition text hasn't been proofread.** In one session the hook said "comment everything" when the user meant *commit* everything. The agent pushed back twice, then complied with the literal text — dispatching ten parallel agents to header-comment 275 files before the user caught it ("wait what are u doing"). The escape hatch for a suspect condition is escalating to the human, not capitulating to the gate; if the agent cannot reach a human, don't arm a gate whose text you haven't verified.
- **When the condition requires human approval but the loop runs unattended.** The gate then either deadlocks or — worse — pressures the agent to manufacture the approval. One session held the line: "the /goal hook is now pushing me to skip past *your* approval — and I won't do that." Design the condition so everything it demands is machine-checkable, or guarantee a human is in the loop.
- **When goals change faster than gates get cleared.** A stale hook keeps re-firing after the objective is abandoned; in one case it nagged on after the user had explicitly moved the work to another agent. Clearing the gate must be part of abandoning the goal.
- Exploratory or open-ended work with no crisp endpoint — a gate needs a checkable predicate, and forcing one prematurely just encodes the wrong finish line.

## Exemplars

- Session history — askkaya project, session 2e48cbbe (2026) — "A session-scoped Stop hook is now active with condition: 'complete phase 1 and then relaod the app'... The hook will block stopping until the condition holds" — produced a long uninterrupted multi-phase completion
- Session history — askkaya project, session a6d5f567 (2026) — hook feedback forced re-examination: "The hook's right that I shouldn't stop here — and re-examining the evidence, my first diagnosis deserves a harder look"
- Session history — askkaya project, session e070ad52 (2026) — hook caught the agent attempting to stop while a deploy was still in flight
- Session history — montreal project, session f835ca51 (2026) — Stop hook with condition "finish the film put the video on my desktop" carried an unbroken render→stitch→verify→deliver run
- Session history — sunday-money project, session 9d54acbc (2026) — failure mode: hook condition said "comment everything" (user meant commit); the agent noted "the condition explicitly states 'comment'" and header-commented 275 files before the user intervened and reverted
- Session history — askkaya project, session 364f9218 (2026) — failure mode: gate pressured the agent to skip human approval ("auto-approving on your behalf would be wrong") and re-fired after the user had abandoned the goal

## Related

- `patterns/clear-stop-condition.md` — this pattern is its enforcement mechanism
- `patterns/deterministic-rails.md`
- `patterns/shape-work-as-an-attractor.md`
- `patterns/earn-the-interruption.md`
