---
name: 001-design-fidelity-pass
description: >-
  Fixes what a design-fidelity pass compares a running render against, how it covers the surface, what it records, and
  what it leaves to other checks.
when_to_use: >-
  Use when running or reviewing the third pass of a UX review fix planning run, or when judging whether a design finding
  is in scope.
---

# Design-Fidelity Pass

The first two passes ask whether the surface behaves as specified and whether a newcomer can use it. Neither asks
whether what renders is what was designed. This pass does, and it looks at the live render, because a stylesheet correct
in source can still resolve to the wrong value in a browser.

## Ground Truth

A design-fidelity reviewer compares the render at `origin`, across `routes`, `viewports`, and `locales`, with every
source that applies:

| Source                                                                                                   | A finding when the render                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| approved designs, carried as [Plan UI Design](../../../conventions/structure/plan-ui-design.md) sets out | departs from the selected design at a declared viewport class                                                                                                                                                  |
| `design-source`, when given                                                                              | departs from that approved external design                                                                                                                                                                     |
| the token layer, as it resolves at runtime                                                               | shows a value no token defines, or the wrong token role, per [Design Tokens](../../../development/quality/user-interfaces/design-tokens.md)                                                                    |
| design-system primitives                                                                                 | rebuilds by hand an element a design names as a primitive, per [Authoring a User-Facing Plan](../../../development/quality/user-interfaces/user-facing-delivery-hardening/001-authoring-a-user-facing-plan.md) |
| published design practice                                                                                | is weak in hierarchy, alignment, spacing and density, typography, colour, or consistency across surfaces                                                                                                       |

A practice finding cites the published guidance it relies on. Preference without a source is not a finding.

## Coverage

Like the other two passes, this pass enumerates rather than samples: the consistent-styling function of
[Enumerated Coverage](../../../development/quality/manual-verification/007-enumerated-coverage.md) runs over every
interactive element on every surface, and every item on the run's carry-forward lists is rechecked.

## What Is Recorded

Each finding carries a stable identifier prefixed by this pass, the route, viewport class, locale, and state where it
appears, the ground-truth source it departs from, and a criticality per
[Finding Criticality and Confidence](../../../development/quality/evidence/finding-criticality-and-confidence.md).

On-design behaviour worth protecting becomes a proposed scenario labelled with this pass. It is triaged with the other
proposals when the plan is authored and never written into a specification directly.

## What It Leaves Alone

The pass judges the render, never component source; a static review of source is a separate check with its own findings.
Fetched markup or source inspection is a baseline, never a pass. It is passive under the same rules as the lenses of
[Exploratory and Usability Review](../../quality/exploratory-usability-review.md): nothing shared or live is changed,
and no record holds a private value. It fixes nothing it finds.
