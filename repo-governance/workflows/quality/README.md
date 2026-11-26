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

- [API HTTP Propagation](api-http-propagation.md)
- [API HTTP Quality Gate](api-http-quality-gate.md)
- [CI Propagation](ci-propagation.md)
- [CI Quality Gate](ci-quality-gate.md)
- [Content Propagation](content-propagation.md)
- [Content Quality Gate](content-quality-gate.md)
- [Docs Propagation](docs-propagation.md)
- [Docs Quality Gate](docs-quality-gate.md)
- [Exploratory and Usability Review](exploratory-usability-review.md)
- [Gherkin Implementation Review](gherkin-implementation-review.md)
- [Harness Parity Verification](harness-parity-verification.md)
- [Harness Propagation](harness-propagation.md)
- [Harness Quality Gate](harness-quality-gate.md)
- [PDF to Markdown Propagation](pdf-to-md-propagation.md)
- [PDF to Markdown Quality Gate](pdf-to-md-quality-gate.md)
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
- [Specs Propagation](specs-propagation.md)
- [Specs Quality Gate](specs-quality-gate.md)
- [Tutorial Annotated Concept Propagation](tutorial-annotated-concept-propagation.md)
- [Tutorial Annotated Concept Quality Gate](tutorial-annotated-concept-quality-gate.md)
- [Tutorial By Example Propagation](tutorial-by-example-propagation.md)
- [Tutorial By Example Quality Gate](tutorial-by-example-quality-gate.md)
- [Tutorial In the Field Propagation](tutorial-in-the-field-propagation.md)
- [Tutorial In the Field Quality Gate](tutorial-in-the-field-quality-gate.md)
- [Tutorial Primer Propagation](tutorial-primer-propagation.md)
- [Tutorial Primer Quality Gate](tutorial-primer-quality-gate.md)
- [UI Web Propagation](ui-web-propagation.md)
- [UI Web Quality Gate](ui-web-quality-gate.md)
- [UX Review Fix Planning](ux-review-fix-planning.md)
- [UX Review Fix Planning Modules](ux-review-fix-planning/README.md)
