---
description: >-
  Requires every change to assess the specifications it could affect, update each affected one with its contracts,
  tests, and documentation in the same change, and record a verified no-op when none is affected.
when_to_use: >-
  Use before changing code, configuration, tests, or user-facing documentation of a project keeping specifications, or
  when deciding whether a change must also update one.
---

# Specification Maintenance

A repository's specifications are canonical: they state what its software must do and which boundaries it keeps, and the
implementation follows them. Every change first answers: which specifications would this make wrong?

This standard implements the [documentation-first](../../../principles/documentation-first.md),
[one-source-per-fact](../../../principles/one-source-per-fact.md),
[explicitness](../../../principles/explicit-over-implicit.md), and
[evidence-over-assertion](../../../principles/evidence-over-assertion.md) principles.

Where specifications live is the adopter's choice;
[Specification Tree](../../../conventions/structure/specification-tree.md) offers one layout. Writing and binding
scenarios belongs to [Behaviour-Driven Development](../testing/behaviour-driven-development.md), keeping a model
as-built to [Architecture Specifications](../architecture/architecture-specifications.md); this standard ties both to
every change.

## Assess Before Every Change

Before changing production code, configuration, tests, or user-facing project documentation, inspect the specification
set of each owner the change reaches: behaviour specifications, the architecture model, served contracts, the corpus
index, and any other canonical schema, example, or reference kept there.

Assessing means reading every specification the change could plausibly affect, then saying which are affected and why
the others are not; scanning file names is not an assessment.

A specification is affected when the change would leave any of its statements inaccurate, incomplete, or contradictory:
about a behaviour, actor, boundary, responsibility, relationship, interface, data flow or store, constraint, example,
term, or owner.

## Update First, in the Same Change

Each affected specification changes in the same change as the implementation, and before it: a behaviour's scenario
comes first; a moved boundary is synchronized with the final as-built state.

Synchronization runs both ways: new behaviour with no scenario is drift, and so is a scenario kept after its behaviour
was removed, even while every binding resolves.

| The change                                                                                 | Specification update                                   |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| adds, removes, or renames an operation, command, page, or other entry point                | add, remove, or rename its scenarios                   |
| changes an input or output shape, an observable validation rule, or an access requirement  | update the scenarios that state it                     |
| adds or removes a data store, external integration, or runtime boundary                    | update the architecture model                          |
| renames or removes a project                                                               | rename or remove its corpus, and every index naming it |
| fixes a defect to match the existing specification                                         | none: the specification was already right              |
| fixes a defect by changing behaviour the specification stated wrongly                      | correct it to the fixed behaviour                      |
| refactors internals, upgrades a dependency, or tunes performance with no observable change | none                                                   |

## Complete Means Every Companion Artifact

A behaviour change is complete only when, in the same change, each related artifact agrees with it:

- its behaviour specifications;
- the contracts its owner serves, with generated code regenerated, never hand-edited, per
  [OpenAPI Contract-First](../architecture/openapi-contract-first.md);
- tests at every applicable layer, bound to the changed scenarios;
- documentation describing the behaviour;
- the architecture model, where a boundary moved; and
- the specification tree's indexes, where a file was added, moved, renamed, or removed, under
  [Directory Indexes](../../../conventions/structure/directory-indexes.md).

Shipping part of this set is unfinished work, not finished work with a follow-up.

A direct change carries the updates itself; a planned change states them before implementation under
[Plan Specification Changes](../../../conventions/structure/plan-specification-changes.md), and its execution meets the
same bar.

## No Churn, and a Record Either Way

Leave an unaffected specification alone, even beside a changed sibling. A scenario edited without a behaviour change
carries history that no longer shows when its behaviour moved.

The delivery report names every specification updated, or records that the assessment found none: a verified no-op. An
unrecorded assessment is indistinguishable from none.

When a scenario and the implementation disagree, deciding which is wrong belongs to
[Gherkin Implementation Review](../../../workflows/quality/gherkin-implementation-review.md).

## Out of Scope

Plans, which hold proposals; generated output, whose source changes instead; and governance documents describing no
project behaviour.

An adopter enforces the mechanical part, such as required corpus files, complete indexes, and strict bindings, in its
own gate or CI.
