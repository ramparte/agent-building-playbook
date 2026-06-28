---
title: Code Is Cheap, Maintenance Isn't
one_liner: AI-generated code is free as in puppies — someone still has to feed it, secure it, and maintain it for as long as it lives.
dimensions: meta-principles
---

## What it is

The marginal cost of generating code with AI is near zero. The marginal cost of owning that code is not. Every function added to a codebase creates ongoing obligations: security patches, dependency updates, bug reports, on-call pages, onboarding burden for the next engineer, and cognitive load for the next AI session that reads the file. The "free as in puppies" framing captures this precisely: the puppy costs nothing to acquire and everything to keep. AI-assisted development lowers the creation cost to near zero while leaving the maintenance cost exactly where it was, making it dangerously easy to accumulate obligations faster than you can service them.

## When to reach for it

- Before accepting an AI-generated feature, module, or abstraction: ask who will maintain it, for how long, and at what ongoing cost.
- When an AI has suggested a "nice to have" addition that wasn't in the spec — resist it even if the code is free.
- When planning capacity: AI accelerates creation; plan staffing and process for maintenance at the same time, not afterward.
- When deciding whether to keep or delete generated code that "might be useful later."

## When NOT to

- Exploratory throwaway code with an explicit expiry date — scripts that run once, prototypes that will be deleted after the demo, analysis notebooks that live for a sprint.
- Code maintained by automated tooling with no human obligation (fully generated from a schema and regenerated on each schema change, for example).

## Related

- `patterns/start-least-agentic.md`
