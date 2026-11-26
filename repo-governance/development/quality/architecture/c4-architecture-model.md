---
description: >-
  Fixes the C4 discipline for architecture models: a context view for every system, a container view once there are two
  deployable units, component views only for complex containers, consistent labels, and diagrams kept as text.
when_to_use: >-
  Use when drawing or reviewing a C4 context, container, or component view, or when showing bounded contexts, shared
  modules, or state machines in one.
---

# C4 Architecture Model

[Architecture Specifications](architecture-specifications.md) requires one as-built architecture model per application,
organized by the levels of the [C4 model](https://c4model.com/), and fixes what that model covers and when it changes.
This standard fixes how its views are drawn, so any reader reads every system's views the same way.

This standard implements [Reproducibility](../../../principles/reproducibility.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md).

## Which Views Exist

| Level          | Required                                                 | Skip when                                                            |
| -------------- | -------------------------------------------------------- | -------------------------------------------------------------------- |
| system context | always, for every system                                 | never                                                                |
| container      | once the system has two or more deployable units         | the system is a single deployable, such as one command-line tool     |
| component      | only for a container whose internal structure is complex | the container's structure is obvious, such as a thin interface layer |
| code           | almost never                                             | a class relationship is not itself architecturally significant       |

A component view earns its place when a container holds many major components, commonly six or more, or when their
responsibilities or internal integration are not evident from the code's structure. Where class-level detail is needed,
prefer a view generated from the code, which cannot drift from it.

## Every Element Says What It Is

- **A person** is labelled with the role, not a name.
- **A software system** is labelled with its name, and marked external when it is not the system being described.
- **A container** is labelled with its name, its kind and technology, and one line on what it does or stores.
- **A component** is labelled with its responsibility, its kind, and one line on what it does.

A container without its technology hides the fact its readers most often need; a name-only box makes every reader guess,
each differently.

## Every Relationship Is Labelled

Every relationship states the action it performs and the protocol or mechanism it uses, such as an authenticated HTTP
request, a database query, or a queued message. An unlabelled arrow claims a dependency without saying what crosses it.

## The Same Kind Looks the Same Everywhere

Each element kind has one visual style used in every view of every system: people, the system described, external
systems, containers, data stores, core components, infrastructure components, and planned elements that do not exist
yet. Colours come from [Colour Accessibility](../../../conventions/writing/color-accessibility.md), and the label always
carries the kind, so no distinction depends on colour alone. A planned element appears only in a prospective document,
always visibly distinct, because the as-built model describes what exists.

## Bounded Contexts in the Model

Where a repository applies [Domain-Driven Design](domain-driven-design.md):

- a context view covering several bounded contexts shows each context as one element, with relationships labelled by
  their context-map pattern;
- a container holding one bounded context is named for it, and a relationship between contexts names its pattern;
- each context's data store appears as its own, and no data store is drawn as shared by two contexts;
- a declared shared kernel appears as a supporting module, its dependency drawn in a line style distinct from runtime
  communication.

A state machine that is architecturally significant may appear in a component view as a component, with its states and
transitions, following [Finite-State Machines](finite-state-machines.md).

## Diagrams Are Text

Every view is kept as text in version control, beside the prose that states its claims. A binary drawing cannot be
diffed, reviewed in a change, or checked mechanically, so it drifts once someone forgets to redraw it.

The diagram form is the adopter's, recorded once under the repository's
[Diagrams](../../../conventions/writing/diagrams.md) rule, which also fixes accessibility and size limits.

## Enforcement

Review checks each view against the table and the labelling rules. An adopter enforces what is mechanical in its own
documentation gate: relationship labels present, the style of each element kind, and the diagram rule's accessibility
and size checks.
