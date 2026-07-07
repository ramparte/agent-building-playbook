---
title: Incremental Validation: The 3-File Rule
one_liner: Before processing a full batch, verify the pipeline works correctly on three representative files — catching bugs at three is dramatically cheaper than catching them at three thousand.
dimensions: verification, workflow-discipline
---

## What it is

When building or running a pipeline that will process a batch of inputs — files, records, API calls, documents — the temptation is to launch the full batch immediately and inspect results at the end. The 3-file rule says: run three representative inputs first, verify the outputs manually, confirm the pipeline is doing what you intended, and only then launch the full run. Three is not magic — it is the minimum sample that reveals whether the pipeline works at all (one input), whether it generalizes beyond the happy case (second input, slightly different structure), and whether it handles an edge case (third input, known problem variant). Three is also small enough that if the outputs are wrong, you have wasted three runs instead of three thousand, and the bug is fresh and local rather than buried in a pile of corrupted output. This pattern applies to any batch operation with a setup cost: data pipelines, evaluation harnesses, agent workflows running over a corpus, file transformations, generation pipelines. It is a specific application of fail-early discipline to the batch context.

## When to reach for it

- Any time you are about to launch a batch job over more than a handful of inputs — stop, identify three representative inputs (one typical, one structurally different, one edge case), run those three, verify the outputs manually, then proceed.
- When setting up a new pipeline or running an existing one against new data — the pipeline may have assumptions that hold for the old data but not the new; the 3-file validation will reveal this before it corrupts a full batch.
- After any change to the pipeline logic — regression on the full batch is expensive; regression on three files is cheap and fast.
- When the pipeline's output is hard to validate in aggregate — if you cannot easily tell from summary statistics whether the full batch ran correctly, the 3-file manual spot-check is the only practical way to catch subtle errors.
- When running evaluation over an agent or model output corpus — verify three evals manually before trusting the aggregate score, because systematic bugs in the eval harness produce confident-looking but wrong results.

## When NOT to

- When the batch is small enough that running all of it costs less than running three and then the rest — if the full batch has five items, just run all five.
- When the pipeline is already well-validated by prior runs on identical data structure — the 3-file check is most valuable when there is genuine uncertainty about whether the pipeline will handle the data correctly.
- When the outputs cannot be practically verified manually even for three items (outputs require automated analysis to interpret) — in that case, invest in the automated verification tooling first, then apply the 3-file rule using that tooling.

## Exemplars

- Anthropic — https://www.anthropic.com/research/building-effective-agents — Building Effective Agents: advocates starting with simple prompts and adding multi-step complexity only when simpler solutions fall short, rather than building the full system at once
- Amplifier — https://github.com/microsoft/amplifier — the prove-on-small-sample pattern is the same discipline at the pipeline design level; the 3-file rule is its operational application at the batch execution level (per the Amplifier team's white papers; not visible in the current public repos)

## Related

- `patterns/prove-on-small-sample.md`
- `patterns/eval-driven-development.md`
- `patterns/fail-loud-over-fallbacks.md`
- `patterns/gate-the-phases.md`
