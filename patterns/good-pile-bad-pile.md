---
title: Good Pile, Bad Pile
one_liner: In domains where stakeholders say "it depends," stop asking for abstract rules and start collecting labeled examples in the domain's own language — good, bad, acceptable-but-awkward, compliant, risky — because examples become intent training data agents can learn the dependency structure from.
dimensions: intent, verification, knowledge
---

## What it is

In many domains the honest answer to "what is the rule?" is "it depends," and the dependency is real — but the experts who live it can rarely state it as a clean rule, even though they can classify any concrete case in seconds. The technique is to stop demanding the rule and start building piles of labeled examples: this is good, this is bad, this is acceptable but awkward, this is technically correct but unacceptable to users, this is compliant, this is risky, this is the old workaround, this is the desired future state. The labels matter as much as the examples, and they should use the domain's own language rather than an abstraction imposed from outside, because the local vocabulary carries the distinctions the experts actually reason with. In regulated, operational, and legacy domains this is frequently more effective than any attempt to elicit abstract rules, because the rule may not exist in any stateable form while the judgment that produces the classification is sharp and consistent. The payoff is that the piles become intent training data: a corpus of labeled cases that can feed specs, reviewers, validators, user-story generators, and test scenarios, encoding the dependency structure through examples even when no one can write the rule the examples obey.

## When to reach for it

- Stakeholders answer requirement questions with "it depends" and cannot produce the rule it depends on.
- The domain is regulated, operational, or legacy, where tacit judgment outruns any written policy.
- You need material to drive reviewers, validators, or acceptance tests but have no rubric to start from.
- Experts can instantly classify a case as right or wrong even though they cannot explain the criterion.
- You want intent that survives handoff — labeled examples travel to downstream agents better than prose rules.

## When NOT to

- A clean, stateable rule already exists — collecting examples to rediscover it is wasted effort.
- The examples cannot be labeled with consistent judgment because the experts genuinely disagree — resolve the disagreement first or you will train on noise.
- The case space is so large or adversarial that a finite pile gives false confidence the dependency has been captured.
- Privacy, compliance, or confidentiality constraints make the real examples unusable and synthetic ones would misrepresent the domain.

## Exemplars

- Michael Polanyi, *The Tacit Dimension* (1966) — https://en.wikipedia.org/wiki/Tacit_knowledge — classic antecedent: the foundational philosophical argument that "we can know more than we can tell" — experts reliably classify cases they cannot reduce to a stateable rule, which is exactly why collecting labeled examples beats demanding abstract rules.

## Related

- `patterns/interview-to-a-spec.md`
- `patterns/simulated-review-squad.md`
- `patterns/decision-theater.md`
- `patterns/document-intent.md`
