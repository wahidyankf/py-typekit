---
name: 002-findings-and-the-plan
description: >-
  Fixes the shape of a UX review fix planning report, how merge mode keeps finding identifiers stable, and what the fix
  plan authored from the report must carry.
when_to_use: >-
  Use when writing the report of a UX review fix planning run, extending an earlier findings plan, or reviewing the plan
  such a run authors.
---

# Findings and the Plan

## The Report

One report per run, written as [Temporary Files](../../../conventions/structure/temporary-files.md) describes:

| Part                 | Holds                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| missing perspectives | first, each pass that could not run and why, or an explicit none                                                |
| one section per pass | exploratory, usability, then design fidelity, each finding with a stable identifier prefixed by its pass        |
| proposed scenarios   | kept by pass: spec-aware gaps, spec-blind suggestions, and design protections                                   |
| cross-references     | findings from different passes that share a root cause, each pointing at the others                             |
| coverage             | every pass's enumerated matrices, the completeness critic's result, and each gap left uncovered with its reason |

Sections never merge. A contradicted specification, first-use friction, and design drift call for different fixes and
different confirmation, so a reader must always be able to tell which pass saw what.

Cross-references let one fix close several findings. Without them, the plan schedules one root cause once per pass that
saw it, and the later fixes collide with the first.

## Merge Mode

Under `merge`, prior findings keep their identifiers, and each gains this run's re-verification result: still present,
or fixed. New findings continue their pass's numbering. Nothing is renumbered, because delivery items, commits, and
evidence already cite the old identifiers.

## What the Plan Carries

[Planning](../../plan/plan-planning.md) authors the plan from the report. Its pre-write gate resolves at least which
findings are in scope and which are deferred, any disputed severity, the fix approach wherever more than one is valid,
and which proposed scenarios are accepted. The plan then carries:

- in its technical shape, the findings by pass, and for each finding or cluster its root cause and the chosen fix,
  naming the components and design-system primitives affected;
- in `delivery.md`, a test-first item per fix, per [Red, Green, Refactor](../red-green-refactor.md), with each accepted
  scenario landing before its fix per
  [Specification Maintenance](../../../development/quality/evidence/specification-maintenance.md);
- in `README.md`, each top risk labelled with the pass that found it;
- the design exploration [Plan UI Design](../../../conventions/structure/plan-ui-design.md) requires, whenever a fix
  adds or changes a screen or component; and
- the near-end retest
  [Closing a User-Facing Plan](../../../development/quality/user-interfaces/user-facing-delivery-hardening/002-closing-a-user-facing-plan.md)
  requires, for a plan that changes a user-facing surface.

A deferred finding stays in the technical shape with its reason, so a later run's carry-forward lists still see its
class.
