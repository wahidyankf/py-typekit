---
description: >-
  Fixes the portable rules of domain-driven design: bounded contexts guide application boundaries, no core model spans
  two contexts, a context map is kept, and code speaks each context's ubiquitous language.
when_to_use: >-
  Use when drawing or changing a bounded context, integrating two contexts, or modelling aggregates, entities, value
  objects, and domain events.
---

# Domain-Driven Design

Domain-driven design keeps the language of the business, its rules, and the boundaries of the code aligned. A model is
coherent only inside a boundary where each term has one meaning. Across boundaries the same word means different things,
and code that ignores this couples what the business keeps apart.

This standard implements [Pure Functions](../../../principles/pure-functions.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Immutability](../../../principles/immutability.md).

## Modules

1. [Bounded Contexts and Context Maps](domain-driven-design/001-bounded-contexts-and-context-maps.md)
2. [Cross-Context Integration](domain-driven-design/002-cross-context-integration.md)
3. [Aggregates, Entities, and Values](domain-driven-design/003-aggregates-entities-and-values.md)
4. [Language and Tests](domain-driven-design/004-language-and-tests.md)

## The Rules in Brief

- A bounded context is the primary guide for application boundaries, and no application's core model spans two contexts.
- A context map records how contexts relate, and each relationship becomes a named integration contract in code.
- Contexts reach each other only through published interfaces and events, and share domain types only through a declared
  shared kernel.
- Every business invariant is enforced inside the domain model, by the aggregate that owns it.
- Names in code, specifications, and tests come from the context's ubiquitous language.

## Scope

This standard holds stack-neutral modelling rules. Layering inside one context, meaning which code belongs to the
domain, the application layer, or an adapter, belongs to [Hexagonal Architecture](hexagonal-architecture.md), and the
port rules in these modules apply where a repository uses it. Lifecycles with meaningful transitions follow
[Finite-State Machines](finite-state-machines.md). A modelling choice that only one stack makes, such as how a language
declares an immutable record, belongs to that stack's standard.

Worked domain examples stay out. A rule is stated once here, and each repository illustrates it in its own domain.

## Enforcement

Review with someone who knows the domain checks names against the ubiquitous language and boundaries against the context
map. An adopter enforces the mechanical parts in its own gates: import boundaries between contexts, no upstream type
inside a downstream domain outside a declared conformist relationship, and a test for every invariant.
