---
title: People Edit Better Than They Author
one_liner: Most stakeholders cannot write a clean requirement, but shown a concrete artifact they can instantly say what's wrong — so elicit intent by giving people something to react to, because cheap software has made a throwaway artifact the fastest way to extract intent.
dimensions: intent, workflow-discipline, human-factors
---

## What it is

The limiting resource in an agentic organization is no longer the ability to build — it is the ability to say what to build, for whom, under which constraints, with what proof. Model capability has outrun organizational ability to express goals, and this intent bottleneck does not yield to asking people to try harder at writing requirements, because people are reliably better editors than authors. A customer, executive, operator, or regulator who cannot draft a clean spec from a blank page can look at a concrete artifact and immediately say "that's not how the office actually works," "the approval step is missing," "this would create a compliance problem," or "this is the thing I meant." Cheap software changes the economics that make this possible: in the old world prototypes were expensive enough that teams tried to extract intent before building, but when an agent can produce a throwaway artifact in minutes, the artifact itself becomes the fastest instrument for extracting intent. The discipline is to stop demanding that humans author perfect requirements and instead manufacture concrete things — mockups, scenarios, models, drafts — for them to correct. Two failure modes lurk here: asking users to write like product managers (they are not, and the blank page produces vague or wrong specs — give them artifacts to react to instead), and overfitting to the loudest stakeholder, because agentic speed amplifies whoever supplies the most concrete instructions, so the elicitation must deliberately preserve whose needs are being served and whose constraints matter rather than encoding only the person who happened to talk most.

## When to reach for it

- A stakeholder struggles to articulate what they want but clearly recognizes wrong answers when shown them — build something wrong on purpose to get the correction.
- The requirement-gathering meeting keeps circling abstractions without converging — replace the discussion with an artifact people can mark up.
- You are eliciting intent in a domain you do not deeply understand and need the experts to react rather than teach.
- The cost of generating a throwaway draft is now lower than the cost of one more clarifying meeting.
- Multiple stakeholders disagree and you need to surface the disagreement against something concrete rather than in the abstract.

## When NOT to

- The intent is already crisp and agreed — manufacturing artifacts to react to just adds a step.
- The artifact would be mistaken for a commitment or shipped product, creating expectations you cannot meet — make its throwaway status unmistakable first.
- Only one stakeholder is ever consulted and their reactions are treated as ground truth — you will overfit to a single voice and miss whose constraints actually matter.
- Producing the artifact has durable side effects (writing to production, notifying real customers) that the "throwaway" framing does not survive.

## Related

- `patterns/interview-to-a-spec.md`
- `patterns/decision-theater.md`
- `patterns/requirements-are-disguised-solutions.md`
- `patterns/implement-to-learn.md`
- `patterns/document-intent.md`
