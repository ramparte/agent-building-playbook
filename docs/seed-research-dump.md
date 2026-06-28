# The Agent-Building Playbook

> A dense, living reference of best practices and techniques for building **with** and **for** AI agents.
> Meant to be read by humans and by agents. Each entry is a 1–3 sentence meta-strategy. Sources are tagged.

**Status:** preliminary research dump (v0.1) — assembled from external literature, Sam's own Amplifier session history, and the team ecosystem. Next step is to brainstorm structure, prune, and decide what this becomes.

**Source tags:**
`[dbreunig]` Drew Breunig, *10 Lessons for Agentic Coding* · `[anthropic]` · `[openai]` · `[langchain]` · `[cognition]` · `[willison]` Simon Willison · `[deepeval]` ·
`[sessions]` distilled from Sam's own 68-session Amplifier history (battle-tested, not theoretical) · `[ecosystem]` observed in the Amplifier team's tooling.

---

## 0. The Meta-Principles (if you keep only a handful)

1. **Verify independently — agents fake "done."** An unobservable step is an unrun step; treat "complete" as a claim to verify, never a fact. `[sessions]`
2. **A failing agent silently does the work itself.** When tooling breaks, the agent abandons the harness and improvises the output — build harnesses that *fail loud* rather than let the agent paper over them. `[sessions]`
3. **Fix reliability before features.** Flakiness, not capability, is the enemy; a broken machine just wastes tokens generating broken output. `[sessions]`
4. **Code is cheap, maintenance isn't.** Agentic code is "free as in puppies" — build fast, but mind the support, security, and maintenance burden you silently adopt. `[dbreunig]`
5. **Context is a finite resource with diminishing returns.** Curate the smallest set of high-signal tokens; don't stuff the window. `[anthropic]`
6. **Start with the least agentic thing that works.** Many problems need one good LLM call with retrieval, not an autonomous agent. `[anthropic]`

---

## 1. Workflow Discipline

- **Implement to learn.** Spec-driven design takes you far, but writing code surfaces decisions you missed — when code is cheap, build early to improve the spec. `[dbreunig]`
- **Keep specs in sync.** Treat the markdown spec as a living artifact updated as code and tests advance; a frozen pre-work spec loses every learning gained during implementation. `[dbreunig]`
- **Document intent, not just method.** Tests capture goals and code captures how; neither captures *why* — persist intent so you and the agent compound decisions in one direction. `[dbreunig]`
- **Rebuild often.** Cheap code means you can fork, recode, and run crazy experiments to discover how far a feature can go. `[dbreunig]`
- **Gate the phases explicitly: brainstorm → plan → build → review.** Phase transitions are intentional, not accidental; invoke them deliberately. `[sessions]`
- **Prove the pipeline on 2 units before running 20.** Review on a small sample before committing to scale. `[sessions]`
- **When a task times out, decompose and retry — don't retry whole.** Break the plan into smaller pieces. `[sessions]`
- **Bite-sized tasks (2–5 min each).** "Write the failing test," "run it," "implement minimal code," "verify," "commit" — each is one step. `[ecosystem]`
- **Hand long autonomous runs off cleanly with a clear stop condition** ("do that without checking back unless it's an emergency"). `[sessions]`

## 2. Reliability & Anti-Cheating (Sam's strongest recurring theme)

- **Demand independent proof, not a status report.** Agents will quietly shortcut work; an auditable artifact at every stage is the only defense. `[sessions]`
- **Make every pipeline stage produce an auditable artifact** — it must EXIST, WORK, BE TESTED, and BE AUDITABLE. `[sessions]`
- **Use a second agent as auditor/observer of the first.** Supervision beats trust; a watcher session that "throws a fit" when the machine isn't properly run. `[sessions]`
- **Separate the proposer from the authority.** A generative component proposes; a deterministic component adjudicates (DM proposes, rule engine is final truth; editor proposes, human/engine approves). `[sessions]`
- **Mark un-run / skipped steps inline for human review** rather than hiding them — visible gaps beat silent omissions. `[sessions]`
- **Encode reliable multi-step work as a recipe, not a conversation.** Determinism and resumability live in recipes, not chat. `[sessions]`
- **Fail loud over fallbacks; trust the model over instructions.** (Restless-old-brian lens.) `[ecosystem]`

## 3. Context Engineering

- **Context engineering > prompt engineering.** Manage the *entire* state — system prompt, tools, history, retrieved data — not just the instruction. `[anthropic]`
- **Four moves: Write, Select, Compress, Isolate.** Persist context outside the window; pull only what's relevant; summarize to the minimum; split across sub-agents to keep each lean. `[langchain]`
- **Just-in-time retrieval over pre-loading.** Let the agent pull data when needed instead of front-loading everything. `[anthropic]`
- **Checkpoint to a handoff file before context bloats, then restart clean.** Treat big-context (e.g. 387K tokens) as a signal to write out and reset. `[sessions]`
- **Persist environment facts so you stop re-teaching them.** Every repeated correction (gh user, machine identity, model role) is a missing persistent fact → AGENTS.md / context file. `[sessions]`
- **Use sub-agents as context sinks.** They absorb the token cost of exploration and return only distilled insights, keeping the root session lean for orchestration. `[anthropic]` `[ecosystem]`
- **Thin pointers, zero poisoning.** Root sessions get a thin "this capability exists, delegate to X"; heavy docs live in the specialist agent's context. `[ecosystem]`
- **For long-horizon tasks: compaction, structured note-taking/external memory, and sub-agent isolation.** `[anthropic]`

## 4. Tool Design

- **Design tools for *agents*, not humans.** Consolidate workflows into a few high-impact tools instead of wrapping every API endpoint. `[anthropic]`
- **Prefer search/filter tools over list-everything tools** that flood context; return high-signal, token-efficient responses. `[anthropic]`
- **Namespace tools by domain, write unambiguous descriptions, make them robust to error.** `[anthropic]`
- **Let agents evaluate and optimize your tools** — have the model critique and improve its own tool definitions against realistic eval tasks. `[anthropic]`
- **Code execution beats loading hundreds of tool defs.** Present tools as a code API the model calls programmatically; results stay in the execution environment instead of flooding context. `[anthropic]`

## 5. Orchestration & Multi-Agent

- **Default to a single-threaded linear agent with continuous context.** Naive multi-agent setups fail because sub-agents lack awareness of each other's work. `[cognition]`
- **Two principles for any multi-agent design: (1) share full context/traces, (2) every action carries implicit decisions** — parallel agents making conflicting decisions produce incoherent results. `[cognition]`
- **Distinguish workflows from agents.** Workflows = predefined code paths orchestrating LLMs; agents = LLMs directing their own tools. Choose by task predictability. `[anthropic]`
- **Composable patterns:** prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer. `[anthropic]`
- **Default to clean-slate delegation** (context_depth=none); give sub-agents a bounded task, not your whole history. Reserve inherited context for agents that genuinely need the thread. `[sessions]`
- **Lead investigations with recon before action** (an explorer/survey phase distinct from execution). `[sessions]`
- **Run independent agents in parallel; decompose into independent tracks and fan out.** `[sessions]`
- **Two-phase build: architect → builder.** Design the spec, then implement against it — don't improvise both at once. `[sessions]` `[ecosystem]`
- **Add agentic autonomy only when flexibility justifies the latency, cost, and failure surface.** `[anthropic]` `[openai]`
- **Build from three primitives: a capable model, well-scoped tools, explicit instructions.** Start with the most capable model, then optimize cost. `[openai]`
- **Layer guardrails (input/output validation, safety) and human-in-the-loop escalation around the agent** rather than trusting the model alone. `[openai]`

## 6. Verification & Evals

- **Designing the agentic loop is the core new skill.** Set up a tight, safe loop where the agent acts, observes results, and self-corrects without constant gating. `[willison]`
- **Give agents the ability to verify their own work** (tests, type checks, runnable output) so the loop converges instead of drifting. `[willison]`
- **Invest in end-to-end tests of *what* the product does, not *how*.** Behavioral contracts give you the freedom to rebuild without fear. `[dbreunig]`
- **Eval-driven development: define success → measure → iterate continuously.** Same loop as TDD, but for non-deterministic systems. `[anthropic]` `[deepeval]`
- **Evals must handle non-determinism AND post-deployment drift** — evaluation is a standing capability, not a one-time gate; combine offline (dev) and online (runtime) eval in a closed loop. `[deepeval]`
- **Tests are code too — update them FIRST when an API changes.** `[ecosystem]`
- **Incremental validation: the 3-file rule.** After modifying ~3 files, pause to run quality checks and affected tests before continuing; issues found early are trivial, issues found at session end cascade. `[ecosystem]`
- **Evidence before assertions.** Never claim "done/fixed/passing" without running the verification command and confirming output. `[ecosystem]`

## 7. Cost & Model Routing

- **Match model to stage; don't draft on the expensive model.** Reserve the top-tier model for the few stages that need it (cheap model for drafting, premium for final synthesis). `[sessions]`
- **Pull models from provisioned roles, not hardcoded names**, so pipelines survive model/provider churn. (Maps to role-based routing — coding, reasoning, fast, etc.) `[sessions]` `[ecosystem]`
- **Delegation is token-economics: ~20k tokens of exploration in YOUR context vs ~500-token summary returned.** `[ecosystem]`

## 8. Environment & Observability

- **Run real workloads in their proper environment** (Linux/containers/isolated twins), not improvised locally. `[sessions]`
- **If it's important, emit an event.** A single JSONL log as source of truth; hooks observe without blocking. `[ecosystem]`
- **Build an awareness layer that watches your actual work** (panes, live sessions) and keeps task state honest — coalesce duplicate/stale tasks aggressively. `[sessions]`
- **Use session history as primary evidence ("session archaeology").** Reference prior sessions by ID to reconstruct what really happened; a first-class debugging tool, not a last resort. `[sessions]`

## 9. Taste & Expertise (the human's role)

- **Find the hard stuff.** Anyone can vibe the boilerplate; the value lives in the ugly work — intuitive design, performance, security, resilience, architecture. `[dbreunig]`
- **Develop your taste.** When code arrives fast but external feedback lags, your own judgment is the only feedback that keeps pace. `[dbreunig]`
- **Agents amplify experience.** Expert framing — right terms, right specificity — saves countless debugging cycles and cuts needless agent exploration; expertise + taste is the unbeatable combo. `[dbreunig]`
- **Automate everything that's easy** — distill learnings into skills, build loops, automate review so tools compound — **but avoid the "Mystery House"** of over-automation you no longer understand. `[dbreunig]`

---

## Repos, Tools & Frameworks (link library)

| Tool | URL | One-liner |
|---|---|---|
| OpenAI Agents SDK | https://github.com/openai/openai-agents-python | Lightweight production agent framework (100+ models). |
| LangGraph | https://github.com/langchain-ai/langgraph | Graph/state-machine orchestration for controllable stateful agents. |
| LangChain context_engineering | https://github.com/langchain-ai/context_engineering | Reference repo for write/select/compress/isolate. |
| CrewAI | https://github.com/crewAIInc/crewAI | Role-based multi-agent crews. |
| AutoGen / AG2 | https://github.com/microsoft/autogen | Conversational multi-agent problem-solving. |
| Semantic Kernel | https://github.com/microsoft/semantic-kernel | Enterprise SDK for orchestrating LLMs, plugins, agents. |
| Google ADK | https://github.com/google/adk-python | Google's agent development kit. |
| Smolagents (HF) | https://github.com/huggingface/smolagents | Minimal code-writing agents (act by emitting Python). |
| Pydantic AI | https://github.com/pydantic/pydantic-ai | Type-safe agent framework with structured validation. |
| DeepEval | https://github.com/confident-ai/deepeval | Open-source LLM/agent evaluation harness. |
| Model Context Protocol | https://github.com/modelcontextprotocol | Open standard for connecting agents to tools/data. |
| Amplifier (ours) | https://github.com/microsoft/amplifier | Modular kernel + bundle ecosystem — a living reference implementation of most of the above. |

## Primary Sources (read-the-original list)

- Drew Breunig — *10 Lessons for Agentic Coding* — https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html
- Anthropic — *Effective context engineering for AI agents* — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic — *Writing effective tools for AI agents* — https://www.anthropic.com/engineering/writing-tools-for-agents
- Anthropic — *Code execution with MCP* — https://www.anthropic.com/engineering/code-execution-with-mcp
- Anthropic — *Building effective agents* — https://www.anthropic.com/research/building-effective-agents
- Anthropic — *Demystifying evals for AI agents* — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- LangChain — *Context Engineering for Agents* — https://www.langchain.com/blog/context-engineering-for-agents
- Cognition — *Don't Build Multi-Agents* — https://cognition.com/blog/dont-build-multi-agents
- OpenAI — *A practical guide to building agents* — https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- Simon Willison — *Agentic Engineering Patterns / Designing Agentic Loops* — https://simonwillison.net/guides/agentic-engineering-patterns/
- DeepEval — *Eval-Driven Development* — https://deepeval.com/blog/eval-driven-development · EDDOps paper — https://arxiv.org/abs/2411.13768

---

## Open Questions for the Brainstorm

- **Format:** flat dense list (current) vs. categorized cards vs. a graph/linked structure? What's most useful for an *agent* to consume mid-task?
- **Provenance weighting:** should hard-won `[sessions]` lessons be visually elevated above `[external]` literature?
- **Agent-readability:** add a machine-parseable layer (YAML/frontmatter, IDs per entry) so an agent can cite "PB-3.4"?
- **Scope boundary:** building-with-agents (workflow/orchestration) vs. building-agents (frameworks/tools) — one repo or two sections?
- **Living maintenance:** who/what updates this, and how do new lessons get distilled in (a recipe? a skill?)?
- **Distribution:** private notes, public repo, or an Amplifier skill/bundle others compose?
