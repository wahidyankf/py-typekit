---
description: >-
  Names the delivery-grammar choices an adopter fixes once for all its plans — phase gates, a baseline phase, test-first
  item splitting, and defects found after archival — with each option's trade-off.
when_to_use: >-
  Use when adopting the plan system and fixing the local delivery grammar, or when an archived plan turns out to be
  defective.
---

# Phase Boundaries and Delivery Choices

The [Delivery Contract](004-delivery-contract.md) fixes what every checklist item contains. Six questions stay open;
repositories answer them differently for sound reasons. An adopter answers each once, records the answer with its
[Portability](009-portability.md) statuses, and applies it to every plan. A single plan does not choose for itself.

## 1. How a Phase Ends

| Option                  | Requires                                                                                      | Trade-off                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| phase gate              | every phase closes on a `### Phase N Gate` of commands and criteria, then a pause-safety note | auditable, resumable boundaries; one more gate per phase          |
| plan-level pause safety | only the delivery contract's pause-safety declaration                                         | shorter; a resumed executor re-derives the last phase's coherence |

Under a phase gate, phase N+1 waits while any item of phase N's gate fails; the failure is repaired inside phase N. Gate
items carry executor labels like any other item. The pause-safety note names the coherent state the phase reached and
the one command that re-verifies it. A phase whose gate cannot be written as commands has not been thought through.

## 2. Whether a Baseline Phase Exists

| Option           | Requires                                                                          | Trade-off                                                         |
| ---------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Phase 0 baseline | a first phase installing dependencies and recording green gates before any change | later failures attributable to the work; costs a phase every time |
| no baseline      | the first phase changes the repository                                            | faster start; a pre-existing failure looks like one the work made |

Either way, a predating failure is fixed, never exempted — see [Execution](../../../workflows/plan/plan-execution.md).
The baseline only keeps its origin visible.

## 3. How a Test-First Item Is Written

| Option      | Requires                                                                                           | Trade-off                                  |
| ----------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| split cycle | a code-shipping item becomes RED, GREEN, REFACTOR, each naming test path, command, and expectation | proves the test failed first; more items   |
| single item | one item proved by the passing test                                                                | shorter; nothing shows the test could fail |

Builders of validators or gates have the strongest reason to split: an unobserved-failing check is unshown.

## 4. What Happens When an Archived Plan Is Defective

| Option         | Requires                                                                             | Trade-off                                                                      |
| -------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| follow-up plan | the defect becomes a brief or plan linking the archived one; `done/` stays untouched | keeps the single reverse edge; the repair lives apart from the corrected claim |
| reopen         | move the folder back, strip the date prefix, and add a dated note on what broke      | the correction sits beside the claim; adds a recorded second reverse edge      |

Follow-up is the [Lifecycle and Folders](001-lifecycle-and-folders.md) rule; reopening adapts it, so the adopter records
the adaptation and reason.

Neither permits quietly editing `done/`. A silent correction reads as though the plan had been right.

## 5. How Test-First Cycles Are Batched in Planned Delivery

| Option         | Requires                                                                                                                                                                                                                                                     | Trade-off                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| batched cycles | one RED and GREEN per delivery batch per [Batched Cycles](../../../development/quality/testing/test-driven-development/001-cycle-and-evidence/002-batched-cycles-in-planned-delivery.md); single-scenario cycles only for small changes and single bug fixes | planned work skips per-scenario ceremony; an oversized batch hides which scenario failed |
| strict cycles  | RED, GREEN, REFACTOR per scenario, always                                                                                                                                                                                                                    | every scenario proves its own red; full ceremony per scenario                            |

Batched is the rule; strict is a recorded adaptation with its reason. Unrelated failures in one RED run mean the batch
is too large: split it.

## 6. How Delivery Units Reach Review

| Option                  | Requires                                                                     | Trade-off                      |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------ |
| minimal PRs per plan    | units sharing a boundary land together; each split names its hard constraint | fewest reviews; larger PRs     |
| one PR per natural seam | each cohesive unit lands in its own PR at its boundary                       | small reviewable PRs; more PRs |

An adopter answers once and applies it to every plan.
