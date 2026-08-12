---
title: Version the Cache Keys on LLM Verdicts
one_liner: Caching model verdicts bounds cost but lets stale outputs silently masquerade as prompt failures; put a version constant in the cache key and bump it on every change.
dimensions: reliability, tool-design, verification
---

## What it is

When a pipeline calls a model to classify, triage, or summarize the same inputs repeatedly, caching the verdicts is correct engineering. An inbox opened twenty times a day should not trigger twenty triage calls — with a verdict cache it triggers roughly zero. But this good decision creates a failure mode unique to LLM pipelines: the cache does not know your prompt changed. In deterministic code, a cache keyed on inputs is safe because the same inputs always produce the same output. In a model pipeline, the "function" is the prompt, the model, and the output schema — and all three change constantly while you iterate. If the cache key ignores them, every prompt iteration is silently measured against stale output. You rewrite the classifier, rerun, and see the same wrong verdicts — not because the fix failed, but because the fix was never called. The result is a uniquely demoralizing debugging loop: real improvements appear to do nothing, and you start doubting changes that were actually correct.

The fix is a discipline, not a framework: an explicit version constant — `TRIAGE_VERSION`, `BRIEF_VERSION` — folded into the cache key, bumped on every prompt change, model change, or schema change. A bump invalidates the whole verdict population at once, so each iteration is measured fresh, and old entries age out instead of being laboriously hunted down. The version bump becomes part of the edit itself: change the prompt, bump the constant, in the same commit. Because busting the cache means re-paying for every verdict, this pattern pairs naturally with cost metering on the expensive operation — a per-day meter keeps spend bounded while accuracy iterates, and makes the cost of each version bump visible rather than surprising.

## When to reach for it

- Any pipeline that caches LLM outputs — classifications, triage verdicts, generated briefs, extraction results — keyed only on the input content.
- The moment you observe a fix that "did nothing": you changed the prompt, reran, and the output is byte-identical. Suspect the cache before you suspect the model.
- When a single stubborn misclassification survives multiple prompt rewrites — it is often one stale cached verdict, not a prompt problem at all.
- When you are about to add caching to a model call: design the versioned key now, while it costs one constant, rather than after the first ghost-debugging session.
- When cache-bust costs are nontrivial: add a per-day meter on the expensive call so iteration stays affordable and bumps stay guilt-free.

## When NOT to

- Deterministic computations cached on their full inputs — ordinary content-addressed caching already covers them; a version constant is redundant ceremony.
- Throwaway experiments with no cache layer at all — do not add caching (and its versioning) before repeated identical calls actually cost you something.
- When the real problem is that outputs should never be reused — verdicts on fast-moving data may need TTL-based expiry or no cache, not a version scheme that still serves stale answers within a version.
- As a substitute for evals: version bumps make each iteration measurable, but they do not tell you whether the new prompt is better — that still requires comparison against ground truth.

## Exemplars

- Session history — askkaya project, session 2e48cbbe (2026) — an OAuth email persistently marked "no-reply" turned out to be a stale cached verdict from an earlier prompt version; the fix was adding a `TRIAGE_VERSION` constant to the cache key and busting the verdict cache so everything re-classified. The discipline became routine within the same session: `BRIEF_VERSION` bumped v4 → v5 when a cached-empty brief kept serving, then v5 → v6 on the next prompt change.
- Session history — askkaya project, session ea9d9a0c (2026) — verdict cache paired with a per-day meter on the expensive model call, keeping cost bounded while classification accuracy was iterated.

## Related

- `patterns/fail-loud-harnesses.md`
- `patterns/scope-and-expire-memory.md`
- `patterns/prove-on-small-sample.md`
