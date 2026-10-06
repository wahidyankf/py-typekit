---
name: quality
description: >-
  Indexes the review workflows that judge finished work against criteria stated before the work began, the bounded,
  advisory quality gates with the one propagation that writes for each family, and the red-green-refactor cycle.
when_to_use: >-
  Use when a review is due and you need the procedure that governs it, when a quality gate or its propagation applies,
  or when implementing a behaviour increment test-first.
---

# Quality Workflows

A review compares what exists against what was specified. These workflows exist so that the comparison is made the same
way each time, and so that its result is a verdict rather than an impression.

Every `<family>-quality-gate` follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md),
and its `<family>-propagation` sits beside it as the family's sole writer, per
[Sole-Writer Propagation](../../development/workflow/sole-writer-propagation.md). An adopting repository copies or
relinks each gate's companions, and runs its searches, per the contract's
[Adoption](../../development/workflow/quality-gate-contract/004-adoption.md) module.

## Directory Map

- [Docs Propagation](docs-propagation.md)
- [Docs Quality Gate](docs-quality-gate.md)
- [Plan Propagation](plan-propagation.md)
- [Plan Quality Gate](plan-quality-gate.md)
- [PR Leak Review](pr-leak-review.md)
- [PR Leak Review Modules](pr-leak-review/README.md)
- [PR Review](pr-review.md)
- [PR Review Propagation](pr-review-propagation.md)
- [PR Review Quality Gate](pr-review-quality-gate.md)
- [PR Review Quality Gate Modules](pr-review-quality-gate/README.md)
- [Red, Green, Refactor](red-green-refactor.md)
- [Rules Propagation](rules-propagation.md)
- [Rules Propagation Modules](rules-propagation/README.md)
- [Rules Quality Gate](rules-quality-gate.md)
