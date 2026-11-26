---
name: plan-parity-planning
description: >-
  Plans one objective across parity repositories: surveys each side, decides every difference in a recorded deviation
  matrix, and authors one separately gated plan per repository.
when_to_use: >-
  Use before planning one change for several repositories that keep a declared boundary in agreement.
---

# Parity Planning

## Entry

An objective must hold across two or more repositories in a parity relationship per
[Related Repositories](../../conventions/structure/related-repositories.md), and the request for plans is explicit per
[Authorization and Execution Record](../../conventions/structure/plans/010-authorization-and-execution-record.md).

- `objective` (`string`, required): the shared change.
- `repositories` (`string`, required): the parity set, at least two members.
- `target-stage` (`enum`: `backlog`, `in-progress`; optional, default the adopter's recorded stage).

## Sequence

1. **Record the parity identity before any mutation.** One plan identifier, worktree name, and branch name serve every
   repository; one whose route needs neither records `not applicable` and why. Reuse an existing worktree or branch only
   with proof it belongs to this objective; otherwise choose one free common name.
2. **Survey each repository from its files,** never memory, reading the state the objective touches. Rerun a survey
   older than its repository's latest change.
3. **Build the deviation matrix.** Each difference found is one row: the dimension, each repository's current state, and
   candidate resolutions (align, deviate deliberately, or drop). Two rows are always present: where each repository
   keeps its rationale, and which local constraints, such as access or delivery, bind each side.
4. **Run the first decision gate.** Every row gets a decision and justification per
   [Decision Gates](../../development/agents/planning-capabilities/003-decision-gates.md); a row needing outside
   evidence is flagged. No plan is authored while a row is undecided.
5. **Research the flagged rows,** citing authoritative sources; with none flagged, record skipping research and why.
6. **Run the second decision gate** on the research. A contradicting finding reopens its row; authoring waits until
   every row is redecided.
7. **Author one plan per repository** through [Planning](plan-planning.md) under the shared identifier. Each carries the
   full matrix with decisions, links to its siblings, an item writing the rationale where the matrix placed it, an item
   updating any governance the decisions change, and its own knowledge capture. No plan says how a sibling performs its
   work, per
   [Delivery Seams and Ownership](../../development/agents/planning-capabilities/005-delivery-seams-and-ownership.md).
8. **Gate each plan separately** with the [Quality Gate](../quality/plan-quality-gate.md); one plan's verdict never
   stands in for another's.
9. **Land each plan by its repository's route** once its actual worktree and branch names match the identity record.
   Each repository resolves delivery independently; its own checks prove only its side.
10. **Report the deviation count:** deliberate and silent deviations, silent being zero.

## Exit

Every repository holds a plan with a terminal quality-gate verdict; every matrix row carries a decision and
justification.

Outputs: `plans` (`directory` per repository, `plans/<target-stage>/<identifier>/`), `deviation-matrix` (`table`,
embedded in each plan), `identity` (`record`: identifier, worktree, and branch per repository), and the deviation count.

Partial outcome: a repository whose plan failed keeps its draft and blocking finding; the other plans stand. An
uncovered difference found after authoring reopens step 3 for every plan. The run fails when a gate is abandoned with a
row undecided.

## Example Usage

```text
Run plan-parity-planning with objective "align the error codes" and repositories "web-app mobile-app".
```

## Related Workflows

- [Execution](plan-execution.md) runs each landed plan in its repository.
- [Multi-Plans Execution](multi-plans-execution.md) schedules the plans together.

## Adopter Decision: Plans Only or Through Delivery

| Option                  | After the plans land                                                                                                                  | Trade-off                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| plans only              | each plan waits for its own Execution run                                                                                             | each plan is reviewable before work starts; one more hand-off |
| continue into execution | Execution starts once every plan lands and a decision gate settles order, failure policy, open decisions, and human-step availability | one run from matrix to delivered parity; no review pause      |

Record the default. Either way, each repository keeps its own delivery route, gates, and cleanup.

## Why Every Difference Is a Row

Parity drifts through differences nobody chose. Recording each with a decision makes divergence reviewable: a later
reader can tell a deliberate deviation from a lapse. Each run is bounded by its matrix and two gates. This workflow
implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md) and
[Evidence Over Assertion](../../principles/evidence-over-assertion.md).
