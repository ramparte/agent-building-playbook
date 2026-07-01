# INDEX — Agent-Building Playbook

> GENERATED FILE — do not edit by hand. Regenerate with `scripts/build-index.sh`.
> Dense, skim-and-select pattern list. Patterns appear under every tag they carry.

## context-engineering
- ["Four Moves: Write, Select, Compress, Isolate"](write-select-compress-isolate.md) — Every context management decision is one of four moves — write it out, select only the relevant part, compress the verbose into the essential, or isolate the detail into a sub-agent.
- ["Long-Horizon Memory: Compaction, Notes, Isolation"](long-horizon-memory.md) — Long-running tasks require three memory strategies — compacting history as it ages, maintaining running notes files, and isolating sub-tasks to separate sessions to prevent context collapse.
- ["Thin Pointers, Zero Poisoning"](thin-pointers.md) — Pass file paths and references between agents instead of full content — let each agent pull only what it needs, only when it needs it.
- [Anchor on Canonical Names](anchor-on-canonical-names.md) — A single well-known domain term — "TDD, London School", "arc42" — activates a whole coherent methodology the model already learned in training, far more reliably than a paragraph paraphrasing the same idea, so name the concept instead of describing it.
- [Checkpoint to a Handoff File, Then Restart Clean](checkpoint-handoff-file.md) — When context grows unwieldy or a session must end, write a structured handoff file capturing exactly what the next session needs, then start fresh with only that file.
- [Code Execution Beats Loading Hundreds of Tool Defs](code-execution-tools.md) — A single code-execution tool — bash, Python, a REPL — often replaces dozens of specialized tools and avoids the context cost of registering a large tool set that the agent must reason over on every call.
- [Context Engineering Over Prompt Engineering](context-over-prompt.md) — The model's output quality is bounded by context quality — sculpting what the model sees matters more than sculpting the instruction text.
- [Context Is a Finite Resource](context-is-finite.md) — Curate the smallest high-signal token set — every token of noise degrades every token of signal.
- [Default to Clean-Slate Delegation](clean-slate-delegation.md) — When spawning a subagent, start with an empty context and provide only what the task needs — shared history is a source of inherited confusion, not free context.
- [Delegation Is Token Economics](delegation-token-economics.md) — Every delegation decision is a token investment — the tokens spent spawning and briefing a subagent must be justified by the value of offloading the work from the orchestrator's context budget.
- [Embed Guidance in Tool Output](embed-guidance-in-tool-output.md) — Instead of front-loading every project gotcha into a giant instructions file the model forgets, put the guidance in the outputs of scripts and tools — error and success messages — so the reminder appears exactly where and when it is relevant.
- [Just-in-Time Retrieval Over Pre-Loading](just-in-time-retrieval.md) — Don't fill context with everything that might be relevant — retrieve only what is needed, exactly when it is needed, and discard it after use.
- [Persist Environment Facts](persist-environment-facts.md) — Facts about the environment — directory layout, versions, credentials, topology — belong in files the agent can re-read, not floating in context that disappears on reset.
- [Prefer Search/Filter Over List-Everything](search-over-list.md) — Give agents a search or filter interface rather than a tool that returns a full list — agents that list everything then scan results are burning context on data they'll mostly discard.
- [State the Target, Not the Prohibition](state-the-target.md) — Telling a model what not to do activates the very concept you're suppressing — "list the planets but not the moon" tends to produce the moon — so phrase instructions as a positive description of the target, and enforce hard prohibitions with a deterministic check rather than louder "do NOT".
- [Use Sub-Agents as Context Sinks](subagents-as-context-sinks.md) — Delegate detail-heavy work to sub-agents so the orchestrator's context stays clean — the sub-agent absorbs the complexity and returns only a summary.

## cost-routing
- [Delegation Is Token Economics](delegation-token-economics.md) — Every delegation decision is a token investment — the tokens spent spawning and briefing a subagent must be justified by the value of offloading the work from the orchestrator's context budget.
- [Match Model to Stage](match-model-to-stage.md) — Different stages of a workflow warrant different model capability levels — route expensive models to complex reasoning stages and cheap models to mechanical stages, not the other way around.
- [Parallel Attempts at One Task](parallel-attempts-at-one-task.md) — Because a model is non-deterministic, one attempt is a single die roll — for a hard or quality-sensitive task, run several implementations of the same task in parallel from one checkpoint, then pick the best or splice the strongest parts of each.
- [Pull Models From Provisioned Roles](role-based-routing.md) — Reference abstract capability roles in code rather than model names — let external configuration map roles to models, so routing decisions survive model changes without code changes.

## meta-principles
- [Anchor on Canonical Names](anchor-on-canonical-names.md) — A single well-known domain term — "TDD, London School", "arc42" — activates a whole coherent methodology the model already learned in training, far more reliably than a paragraph paraphrasing the same idea, so name the concept instead of describing it.
- [Code Is Cheap, Maintenance Isn't](code-is-cheap-maintenance-isnt.md) — AI-generated code is free as in puppies — someone still has to feed it, secure it, and maintain it for as long as it lives.
- [Context Is a Finite Resource](context-is-finite.md) — Curate the smallest high-signal token set — every token of noise degrades every token of signal.
- [Fail-Loud Harnesses](fail-loud-harnesses.md) — Build harnesses that fail visibly — a harness that silently substitutes its own answer hides the agent's failure from you.
- [Fix Reliability Before Features](reliability-before-features.md) — Flakiness, not capability, is the enemy — a system that only sometimes works is harder to improve than one that reliably fails.
- [Start With the Least Agentic Thing](start-least-agentic.md) — Many problems that look like multi-agent workflows need only one well-crafted LLM call.
- [Verify Independently — Agents Fake "Done"](verify-independently.md) — An unobservable step is effectively unrun — treat "complete" as a claim that must be independently verified.

## observability
- [Build an Awareness Layer That Watches Your Work](awareness-layer.md) — A separate process or agent that monitors the primary agent's actions in real time catches drift, failures, and unexpected behavior before they compound — the watcher that the working agent cannot be for itself.
- [If It's Important, Emit an Event](emit-events.md) — If a decision, state change, or outcome matters to understanding what happened, it should produce a structured event — not a log line, not a comment, not a hope that someone was watching.
- [Make Every Stage Produce an Auditable Artifact](auditable-artifacts.md) — A stage with no artifact is a stage that cannot be audited — and a stage that cannot be audited is a stage you must trust blindly.
- [Mark Un-Run Steps Inline for Review](mark-skipped-steps.md) — A skipped step that is not explicitly marked is indistinguishable from a completed step — make the gap visible or it will be treated as a gap that was filled.
- [Run Real Workloads in Their Proper Environment](real-environment-execution.md) — Agents that run workloads in simulated or sandboxed environments discover only simulated problems — run the real thing in the real place if you want real answers.
- [The Agent's Struggle Is a Signal](agent-struggle-is-a-signal.md) — When an AI agent starts thrashing on a codebase — missing duplicated call sites, running out of context mid-change, making excuses about failing tests — read it as an early warning that maintainability is decaying, and refactor, instead of just fighting the agent.
- [Use Session History as Primary Evidence](session-archaeology.md) — When something went wrong — or right — in a prior run, the session transcript is the primary evidence; reading it is the first act of diagnosis, not a fallback after other approaches fail.

## orchestration
- ["Thin Pointers, Zero Poisoning"](thin-pointers.md) — Pass file paths and references between agents instead of full content — let each agent pull only what it needs, only when it needs it.
- [Add Autonomy Only When Justified](autonomy-when-justified.md) — Every degree of autonomy you give an agent must be paid for with oversight proportional to the risk — add it only when the cost-benefit calculation is explicit and positive.
- [Build From Three Primitives](three-primitives.md) — Every agentic system is built from three primitives — LLM call, tool call, and loop. Understand these primitives completely before reaching for higher-level abstractions.
- [Composable Orchestration Patterns](composable-patterns.md) — Build orchestration from a small set of named, reusable primitives — sequences, conditionals, fan-outs, and loops — rather than writing bespoke control flow for every workflow.
- [Decompose and Retry on Timeout](decompose-on-timeout.md) — When a task times out, the answer is almost never to raise the timeout — it is to break the task into smaller pieces.
- [Default to a Single-Threaded Linear Agent](single-threaded-default.md) — Run one task at a time in sequence unless you have a concrete reason to fan out — parallelism is an optimization, not a starting point.
- [Default to Clean-Slate Delegation](clean-slate-delegation.md) — When spawning a subagent, start with an empty context and provide only what the task needs — shared history is a source of inherited confusion, not free context.
- [Delegation Is Token Economics](delegation-token-economics.md) — Every delegation decision is a token investment — the tokens spent spawning and briefing a subagent must be justified by the value of offloading the work from the orchestrator's context budget.
- [Distinguish Workflows From Agents](workflows-vs-agents.md) — A workflow is a fixed sequence of steps with known branching; an agent decides dynamically what to do next. Conflating the two produces systems that are harder to test, monitor, and trust.
- [Hand Off With a Clear Stop Condition](clear-stop-condition.md) — An agent without a stop condition will find one itself — and it will not be the one you wanted.
- [Layer Guardrails and Human Escalation](guardrails-and-escalation.md) — Build in multiple layers of guardrails — input validation, output checking, action limits, and explicit escalation paths — so errors are caught before they compound and humans are brought in before damage is done.
- [Lead With Recon Before Action](recon-before-action.md) — Before taking any action that touches external state, first run a read-only reconnaissance pass to understand what exists, what constraints apply, and what the action will actually affect.
- [Parallel Attempts at One Task](parallel-attempts-at-one-task.md) — Because a model is non-deterministic, one attempt is a single die roll — for a hard or quality-sensitive task, run several implementations of the same task in parallel from one checkpoint, then pick the best or splice the strongest parts of each.
- [Run Independent Agents in Parallel](parallel-independent-tracks.md) — When two or more tasks have no ordering dependency and no shared mutable state, run them in parallel agents rather than sequentially — wall-clock latency is the only cost that matters.
- [Separate the Proposer From the Authority](proposer-authority-separation.md) — The entity that proposes an action is the worst authority to approve it — route approval through a role with no stake in the proposal's acceptance.
- [Share Full Context; Every Action Carries Decisions](share-full-context.md) — When delegating to a subagent or spawning a parallel worker, include everything the agent needs to make good decisions — the goal, constraints, prior findings, and any decisions already made.
- [Start With the Least Agentic Thing](start-least-agentic.md) — Many problems that look like multi-agent workflows need only one well-crafted LLM call.
- [Two-Phase Build: Architect Then Builder](architect-then-builder.md) — Separate design from implementation by running an architect agent first to produce a complete specification, then a builder agent to implement it — never conflate the two roles in one pass.
- [Use a Second Agent as Auditor](auditor-agent.md) — The agent that did the work is the worst possible choice to verify the work — put a second agent in the audit seat with no stake in the original claim.
- [Use Sub-Agents as Context Sinks](subagents-as-context-sinks.md) — Delegate detail-heavy work to sub-agents so the orchestrator's context stays clean — the sub-agent absorbs the complexity and returns only a summary.

## reliability
- [Demand Independent Proof, Not a Status Report](demand-independent-proof.md) — An agent's claim of success is a hypothesis — treat it as one until you hold evidence that no longer originates from the agent itself.
- [Encode Multi-Step Work as a Recipe](recipe-not-conversation.md) — A conversation is a trace of what happened once — a recipe is a specification that can be replayed, inspected, versioned, and recovered from.
- [Evidence Before Assertions](evidence-before-assertions.md) — A claim about a system's state is not knowledge — it is a hypothesis. Run the verification command and read the output before making any assertion about whether something worked.
- [Fail Loud Over Fallbacks](fail-loud-over-fallbacks.md) — A fallback that hides a failure teaches the system nothing and costs the same as the failure it replaced — prefer a loud stop over a silent substitution.
- [Fail-Loud Harnesses](fail-loud-harnesses.md) — Build harnesses that fail visibly — a harness that silently substitutes its own answer hides the agent's failure from you.
- [Fix Reliability Before Features](reliability-before-features.md) — Flakiness, not capability, is the enemy — a system that only sometimes works is harder to improve than one that reliably fails.
- [Give Agents the Ability to Verify Their Own Work](self-verification.md) — An agent that can detect its own errors is orders of magnitude more reliable than one that can only produce output — build verification into the agent before shipping it.
- [Layer Guardrails and Human Escalation](guardrails-and-escalation.md) — Build in multiple layers of guardrails — input validation, output checking, action limits, and explicit escalation paths — so errors are caught before they compound and humans are brought in before damage is done.
- [Make Every Stage Produce an Auditable Artifact](auditable-artifacts.md) — A stage with no artifact is a stage that cannot be audited — and a stage that cannot be audited is a stage you must trust blindly.
- [Mark Un-Run Steps Inline for Review](mark-skipped-steps.md) — A skipped step that is not explicitly marked is indistinguishable from a completed step — make the gap visible or it will be treated as a gap that was filled.
- [Prove the Pipeline on 2 Before 20](prove-on-small-sample.md) — Run the full pipeline on two items end-to-end before scaling to the full dataset.
- [Separate the Proposer From the Authority](proposer-authority-separation.md) — The entity that proposes an action is the worst authority to approve it — route approval through a role with no stake in the proposal's acceptance.
- [State the Target, Not the Prohibition](state-the-target.md) — Telling a model what not to do activates the very concept you're suppressing — "list the planets but not the moon" tends to produce the moon — so phrase instructions as a positive description of the target, and enforce hard prohibitions with a deterministic check rather than louder "do NOT".
- [Use a Second Agent as Auditor](auditor-agent.md) — The agent that did the work is the worst possible choice to verify the work — put a second agent in the audit seat with no stake in the original claim.
- [Verify Independently — Agents Fake "Done"](verify-independently.md) — An unobservable step is effectively unrun — treat "complete" as a claim that must be independently verified.

## taste
- [Agents Amplify Experience](agents-amplify-experience.md) — Agents multiply the output of whoever wields them — great judgment gets amplified into great results; poor judgment gets amplified into confident mistakes at scale.
- [Automate the Easy, Avoid the Mystery House](automate-but-avoid-mystery-house.md) — Automate what you understand completely; never automate your way into a system where nobody knows why it works or what it does.
- [Develop Your Taste](develop-your-taste.md) — Taste — the ability to recognize quality and know when something is wrong — is a craft that must be deliberately built; it does not emerge from volume of output alone.
- [Find the Hard Stuff](find-the-hard-stuff.md) — Deliberately seek the genuinely difficult parts of a problem — where the real work lives is almost never where it looks like it should be.
- [The Agent's Struggle Is a Signal](agent-struggle-is-a-signal.md) — When an AI agent starts thrashing on a codebase — missing duplicated call sites, running out of context mid-change, making excuses about failing tests — read it as an early warning that maintainability is decaying, and refactor, instead of just fighting the agent.

## tool-design
- [Build From Three Primitives](three-primitives.md) — Every agentic system is built from three primitives — LLM call, tool call, and loop. Understand these primitives completely before reaching for higher-level abstractions.
- [Code Execution Beats Loading Hundreds of Tool Defs](code-execution-tools.md) — A single code-execution tool — bash, Python, a REPL — often replaces dozens of specialized tools and avoids the context cost of registering a large tool set that the agent must reason over on every call.
- [Design Tools for Agents, Not Humans](tools-for-agents.md) — Agent tools should be structured for machine parsing — unambiguous outputs, complete information in every response, no UI affordances that only make sense for humans.
- [Embed Guidance in Tool Output](embed-guidance-in-tool-output.md) — Instead of front-loading every project gotcha into a giant instructions file the model forgets, put the guidance in the outputs of scripts and tools — error and success messages — so the reminder appears exactly where and when it is relevant.
- [Fail-Loud Harnesses](fail-loud-harnesses.md) — Build harnesses that fail visibly — a harness that silently substitutes its own answer hides the agent's failure from you.
- [Let Agents Evaluate and Optimize Your Tools](agents-optimize-tools.md) — Use an agent to test your tool set — have it attempt real tasks, observe where it selects incorrectly or fails, and feed those observations back into tool descriptions and interfaces before deploying.
- [Namespace Tools, Write Unambiguous Descriptions](namespace-tools.md) — Group tools under a clear namespace and write descriptions that tell the model exactly when to call this tool and when to call a similar one instead — ambiguous tool selection is a primary source of agent errors.
- [Prefer Search/Filter Over List-Everything](search-over-list.md) — Give agents a search or filter interface rather than a tool that returns a full list — agents that list everything then scan results are burning context on data they'll mostly discard.

## verification
- [Designing the Agentic Loop Is the Core Skill](design-the-loop.md) — The quality of an agentic system is determined almost entirely by the design of its loop — how the agent perceives, decides, acts, and verifies before cycling again.
- [Eval-Driven Development](eval-driven-development.md) — Build evals before building features — you cannot improve what you cannot measure, and you cannot trust improvements you have not defined a measurement for.
- [Evals Are a Standing Capability, Not a One-Time Gate](standing-eval-capability.md) — An eval suite that runs once at launch and is never run again is not an eval suite — it is a historical document that measured a system that no longer exists.
- [Evidence Before Assertions](evidence-before-assertions.md) — A claim about a system's state is not knowledge — it is a hypothesis. Run the verification command and read the output before making any assertion about whether something worked.
- [Give Agents the Ability to Verify Their Own Work](self-verification.md) — An agent that can detect its own errors is orders of magnitude more reliable than one that can only produce output — build verification into the agent before shipping it.
- [Incremental Validation: The 3-File Rule](three-file-rule.md) — Before processing a full batch, verify the pipeline works correctly on three representative files — catching bugs at three is dramatically cheaper than catching them at three thousand.
- [Let Agents Evaluate and Optimize Your Tools](agents-optimize-tools.md) — Use an agent to test your tool set — have it attempt real tasks, observe where it selects incorrectly or fails, and feed those observations back into tool descriptions and interfaces before deploying.
- [Test What the Product Does, Not How](test-what-not-how.md) — Tests that describe externally observable behavior survive refactoring; tests that describe internal implementation become a maintenance tax that grows with every change.
- [Tests Are Code — Update Them First on API Change](tests-first-on-api-change.md) — When an API changes, update its tests before updating its implementation — the tests are the specification, and updating them first forces you to define what the change means before you build it.

## workflow-discipline
- [Automate the Easy, Avoid the Mystery House](automate-but-avoid-mystery-house.md) — Automate what you understand completely; never automate your way into a system where nobody knows why it works or what it does.
- [Bite-Sized Tasks](bite-sized-tasks.md) — Break work into units small enough that each completes, commits, and can be reviewed independently.
- [Checkpoint to a Handoff File, Then Restart Clean](checkpoint-handoff-file.md) — When context grows unwieldy or a session must end, write a structured handoff file capturing exactly what the next session needs, then start fresh with only that file.
- [Decompose and Retry on Timeout](decompose-on-timeout.md) — When a task times out, the answer is almost never to raise the timeout — it is to break the task into smaller pieces.
- [Document Intent, Not Just Method](document-intent.md) — Code describes how; comments and specs must describe why — the reasoning that code cannot encode.
- [Encode Multi-Step Work as a Recipe](recipe-not-conversation.md) — A conversation is a trace of what happened once — a recipe is a specification that can be replayed, inspected, versioned, and recovered from.
- [Eval-Driven Development](eval-driven-development.md) — Build evals before building features — you cannot improve what you cannot measure, and you cannot trust improvements you have not defined a measurement for.
- [Gate the Phases Explicitly](gate-the-phases.md) — Declare a hard transition between design and build, and between build and ship — phases that blur produce work that cannot be reviewed or rolled back.
- [Hand Off With a Clear Stop Condition](clear-stop-condition.md) — An agent without a stop condition will find one itself — and it will not be the one you wanted.
- [Implement to Learn](implement-to-learn.md) — The fastest way to understand a problem is to build a small, throwaway version of the solution.
- [Incremental Validation: The 3-File Rule](three-file-rule.md) — Before processing a full batch, verify the pipeline works correctly on three representative files — catching bugs at three is dramatically cheaper than catching them at three thousand.
- [Keep Specs in Sync](keep-specs-in-sync.md) — A spec that diverges from the implementation is worse than no spec — it actively misleads every agent that reads it.
- [Parallel Attempts at One Task](parallel-attempts-at-one-task.md) — Because a model is non-deterministic, one attempt is a single die roll — for a hard or quality-sensitive task, run several implementations of the same task in parallel from one checkpoint, then pick the best or splice the strongest parts of each.
- [Prove the Pipeline on 2 Before 20](prove-on-small-sample.md) — Run the full pipeline on two items end-to-end before scaling to the full dataset.
- [Rebuild Often](rebuild-often.md) — Regular rebuilds from scratch catch accumulated drift that incremental changes normalize.
- [Tests Are Code — Update Them First on API Change](tests-first-on-api-change.md) — When an API changes, update its tests before updating its implementation — the tests are the specification, and updating them first forces you to define what the change means before you build it.
- [Two-Phase Build: Architect Then Builder](architect-then-builder.md) — Separate design from implementation by running an architect agent first to produce a complete specification, then a builder agent to implement it — never conflate the two roles in one pass.
