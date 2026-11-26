---
description: >-
  Requires each application to keep one canonical, as-built architecture model, updated in the same change that moves a
  documented boundary, with the diagram form left to the adopter.
when_to_use: >-
  Use before changing production code, configuration, tests, or specifications that can move an architectural boundary,
  or when creating or splitting an architecture model.
---

# Architecture Specifications

An architecture model is a specification, not a diagram gallery. It states the boundaries a system is required to have,
and readers trust it enough to reason from it. That trust is why a wrong model is worse than no model.

This standard implements [Documentation First](../../../principles/documentation-first.md),
[One Source Per Fact](../../../principles/one-source-per-fact.md), and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Modules

1. [Model Content](architecture-specifications/001-model-content.md)
2. [Scaling and Change Discipline](architecture-specifications/002-scaling-and-change-discipline.md)

## One Canonical Model per Application

Each application's specification set, its behaviour specifications and architecture model kept together, holds exactly
one canonical architecture model, organized by the levels of the [C4 model](https://c4model.com/): system context,
containers, and components where they help. An implementation and a separate end-to-end test project that share one
specification set share its model; neither keeps a copy.

## As-Built, Not As-Intended

The model describes the system that exists. A boundary drawn because it was planned, and never built, sends a reader
reasoning about a system that is not there. A proposed design belongs in a plan or another explicitly prospective
document until it is implemented.

## Diagram Form Is an Adopter Decision

The requirement does not vary: views exist, and prose carries every claim they make. Only the form of the diagrams
varies, and the adopter records one under its [Diagrams](../../../conventions/writing/diagrams.md) authoring rule.

| Option                      | Gains                                                                                 | Costs                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| rendered Mermaid            | automatic layout; reads well wherever a renderer runs; label lengths a tool can check | source is hard to read in a terminal or plain diff; needs an accessible title and description |
| plain text in fenced `text` | reads identically in a terminal, a diff, and a review tool, with no renderer          | layout is maintained by hand, and wide views reach the line width sooner                      |

Whichever form is chosen, every relationship a diagram shows also appears in searchable prose, so a reader who cannot
see the diagram loses nothing. See [Accessibility First](../../../principles/accessibility-first.md).
