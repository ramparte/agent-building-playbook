---
title: Depth Questions Deserve the Raw Source, Not the Summary
one_liner: When a follow-up asks for depth, refetch the primary source — the full transcript, the vendor's code, the git history — instead of elaborating on a summary that flattened it.
dimensions: context-engineering, knowledge
---

## What it is

A summary is not a smaller copy of its source. It is a compression performed for a purpose — and that purpose predates whatever question you are asking now. The AI meeting notes were compressed to answer "what happened in this meeting," not "what exactly did Amit propose and in what words." The vendor's documentation was compressed to onboard a typical integrator, not to reveal every endpoint the API actually serves. So when a depth question arrives and the agent elaborates on the summary instead of refetching the source, it is not recovering lost detail — it is compounding the summarizer's framing, confabulating specifics that the compression already discarded. The failure is quiet: the answer sounds fluent and grounded because it is grounded in *something*, just not in the thing being asked about.

The pattern is a simple rule of routing: summaries are fine for orientation, but the moment a question probes a dimension the summary was not built to preserve, go back to the primary artifact. In practice this shows up across at least four source types. Meeting transcripts — "it has a lot the summary flattened"; one derailed brainstorm was reset only when the user insisted the agent read the newest transcript, not the AI summary, after the agent admitted "I keep inventing scenarios instead of starting from your actual work." Vendor source code — reading the actual Worker source instead of trusting a docs-level understanding revealed `GET /edges` endpoints that fixed a search feature returning wrong results. Git history — rather than reconstruct a v1 onboarding flow from memory, pull the real file straight from the history and quote it. Flaky query layers — when the query tool returns inconsistent results, fetch the raw transcript directly and quote verbatim rather than reasoning over the tool's unreliable digest.

## When to reach for it

- A follow-up question probes specifics — exact wording, exact endpoints, exact prior implementations — rather than the gist a summary preserves.
- The agent's answers are drifting into plausible invention; resetting on the primary source ("start from the actual transcript") re-anchors the work.
- Your understanding of a dependency comes from docs or a README and behavior is contradicting it — read the vendor's actual source.
- You are about to reconstruct a past decision or artifact from memory when git history holds the real thing.
- An intermediate retrieval layer is returning inconsistent or lossy results — bypass it and fetch the raw record, then quote verbatim.

## When NOT to

- The question genuinely asks for the gist — orientation, triage, "should I care about this meeting" — which is exactly what the summary was compressed for.
- The raw source is enormous and the cost of loading it exceeds the value of the question; retrieve the relevant slice, not the whole corpus.
- The summary was purpose-built for this exact question (a structured extraction designed for it), in which case it is the right artifact, not a lossy stand-in.
- No primary source survives — then the honest move is to flag the summary's provenance and uncertainty, not to pretend refetching is possible.

## Exemplars

- Session history — home-directory sessions, session 301b87e1 (2026) — "Let me pull the full transcript so the breakdown draws on the actual conversation, not just the AI summary... it has a lot the summary flattened."
- Session history — home-directory sessions, session 621c1851 (2026) — reading the vendor's actual `index.ts` revealed `GET /edges` endpoints the docs-level understanding had missed, fixing a search that returned wrong "random Johns" results.
- Session history — askkaya sessions, session 364f9218 (2026) — user reset a derailed brainstorm: "look at the newest transcript... and not the ai summary"; the agent conceded it had been inventing scenarios instead of starting from the actual work.
- Session history — forever22web sessions, session 2d28aa48 (2026) — "The query tool is being inconsistent. Let me get the raw transcript directly"; disambiguated two "30 min with Amit" meetings and quoted his verbatim framing.

## Related

- `patterns/mine-transcripts.md`
- `patterns/just-in-time-retrieval.md`
- `patterns/context-over-prompt.md`
- `patterns/dont-verify-through-lossy-filters.md`
