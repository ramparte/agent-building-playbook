---
title: Shadow the User, Then Transform the Transcript
one_liner: Tacit knowledge — workarounds, local norms, exception paths, institutional memory — lives in how people actually work, so sit with users and record them; agentic tooling doesn't remove the observation, it accelerates what happens after it.
dimensions: intent, knowledge, human-factors
---

## What it is

Many domains — government, insurance, healthcare-like workflows, planning, enterprise operations — run on tacit knowledge that never appears in any document: the workarounds people have built, the local norms, the exception paths, the political constraints, the institutional memory that lives only in how the work is actually done. That knowledge cannot be elicited by asking, because the people who hold it do not experience it as knowledge; it is just how things are. The recurring human move, unchanged by agents, is to sit with users and watch them work — shadow the session, ask questions in the moment, record what happens, capture the transcript. What agentic tooling changes is not the observation but everything after it: where transforming a raw shadowing session into usable artifacts was once slow manual labor, transcripts can now be summarized into user stories, mined for contradictions, parsed for domain terms, modeled into workflows, turned into personas that review future work, used to generate prototypes immediately, and read to derive acceptance criteria from observed behavior. The human observation remains the irreplaceable input — there is no substitute for watching the work — but the processing pipeline that converts observation into intent artifacts becomes fast enough to run while the memory of the session is still fresh. The discipline is to actually transform: a captured transcript that is never converted into structured artifacts is dead weight, not intent.

## When to reach for it

- The domain runs on tacit knowledge — workarounds, exception paths, institutional memory — that no document captures and no one can recite on request.
- Stakeholders describe an idealized process that you suspect differs from what they actually do.
- You are entering an unfamiliar operational domain and need ground-truth behavior before specifying anything.
- You have shadowing or interview recordings and want to extract maximum intent from them quickly.
- The exception paths and edge cases matter as much as the happy path, and only observation reveals them.

## When NOT to

- The work is already well-documented and the documentation is trusted to match reality.
- You will capture the session but lack the time or intent to transform it — an unprocessed transcript is not an artifact.
- Observation would violate privacy, confidentiality, or consent constraints that cannot be satisfied.
- The behavior you would observe is itself a broken workaround you are about to faithfully encode — pair this with checking whether the workflow should exist at all.

## Exemplars

- Beyer & Holtzblatt, Contextual Inquiry — https://www.nngroup.com/articles/contextual-inquiry/ — the foundational HCI field-research method: observe users performing their actual work and ask questions in the moment to surface tacit knowledge they cannot articulate when removed from context; the original systematic form of the shadowing step this pattern describes.
- Michael Polanyi, *The Tacit Dimension* (1966) — https://en.wikipedia.org/wiki/Tacit_knowledge — philosophical grounding for why shadowing is necessary: domain practitioners hold knowledge they do not experience as knowledge ("we can know more than we can tell"), making observation an irreplaceable elicitation method.

## Related

- `patterns/mine-transcripts.md`
- `patterns/contradiction-extraction.md`
- `patterns/good-pile-bad-pile.md`
- `patterns/simulated-review-squad.md`
- `patterns/dont-automate-the-workaround.md`
