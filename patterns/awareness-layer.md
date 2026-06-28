---
title: Build an Awareness Layer That Watches Your Work
one_liner: A separate process or agent that monitors the primary agent's actions in real time catches drift, failures, and unexpected behavior before they compound — the watcher that the working agent cannot be for itself.
dimensions: observability
---

## What it is

An agent executing a task cannot simultaneously evaluate whether the task is going wrong. The working agent's attention is committed to the task; it interprets each step in the context of its plan, making it structurally blind to patterns that span steps — a gradual drift from the goal, a repeated failure that each iteration rationalizes differently, a resource metric that has been climbing since step three. The awareness layer is a second observer that watches the primary agent from outside its execution context: it reads the event stream, monitors metrics, compares current state against the expected trajectory, and intervenes when the gap becomes significant. This is not a supervisor in the workflow sense — it does not direct the agent's next action. It is a sentry: a process with a different vantage point and a different agenda whose sole job is to notice things the working agent is not positioned to notice. The awareness layer is what makes long-running autonomous work recoverable. Without it, agents run until they succeed or exhaust their resources, with no mechanism to catch the case where they are confidently heading in the wrong direction.

## When to reach for it

- When an agent will run for more than a few steps on a task where errors compound: a watcher that checks intermediate state catches problems while they are still recoverable.
- When the primary agent has a known bias or blind spot: a planner agent focused on generating steps benefits from a watcher that checks whether the generated steps are drifting from the original intent.
- When resource consumption matters: an awareness layer monitoring token usage, API call counts, or wall-clock time can interrupt work that is running away before it causes damage.
- When building systems that run unattended over long periods: human operators cannot watch continuously; an automated awareness layer is the substitute.
- When the failure mode of the system is silent success — completing without error but producing wrong output: a watcher that validates output properties independently catches this class of failure.

## When NOT to

- When the task is short and the entire execution is observable in a single context window — the awareness layer's value comes from its external vantage point; for short tasks, that vantage point is not needed.
- When adding a watcher would double the compute cost of a task whose budget is tight and whose failure modes are already cheap and visible — awareness layers are investments; not every task justifies the cost.
- When the watcher itself introduces more complexity than it resolves — a poorly specified awareness layer that fires false alarms or interrupts correct work is worse than no watcher. Start with monitoring, not intervention.

## Exemplars

- Amplifier — https://github.com/microsoft/amplifier — the context-intelligence graph-analyst agent: watches session event streams, detects delegation trees, and surfaces patterns that the executing agents cannot observe about themselves; it is an awareness layer over the Amplifier runtime
- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: recommends human-in-the-loop checkpoints and monitoring for long-running agentic tasks as a form of awareness that the agent cannot provide for itself

## Related

- `patterns/emit-events.md`
- `patterns/session-archaeology.md`
- `patterns/real-environment-execution.md`
