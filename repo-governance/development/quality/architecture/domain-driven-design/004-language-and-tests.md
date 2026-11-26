---
description: >-
  Requires code, ports, and modules to use each context's ubiquitous language and name their context, and fixes what
  tests and behaviour specifications verify about the domain model.
when_to_use: >-
  Use when naming a type, module, or port in a context, or when writing tests or behaviour scenarios for aggregates,
  value objects, entities, or events.
---

# Language and Tests

## Code Speaks the Ubiquitous Language

Types, functions, modules, ports, and adapters use the terms the domain's experts use in that context, not generic
technical names. A model whose names differ from the business's words has to be translated in every conversation about
it, and each translation is a chance to get it wrong.

- The root module or package of each context names the context, so an import from one context into another is visible
  where it happens.
- A port that reaches another context names the domain concept it reaches. A reader who meets such a port inside a
  different context recognizes a cross-context dependency at once, instead of discovering it in review.

## Tests Cover the Model

Domain tests use real domain objects, never doubles, as [Test Doubles](../../testing/test-doubles.md) requires. They
cover:

- every aggregate invariant;
- the domain events an aggregate raises;
- the immutability of every value object, and its equality by value; and
- the identity-based equality of every entity.

An invariant without a test is a rule the next refactoring can remove without anything failing.

## Behaviour Specifications Follow Contexts

Where a repository writes behaviour specifications under
[Behaviour-Driven Development](../../testing/behaviour-driven-development.md):

- each feature describes one capability of one bounded context, and no feature spans contexts;
- scenarios use the context's ubiquitous language, so a domain expert can read them;
- scenarios verify the aggregate's business rules; and
- where an aggregate raises domain events, a scenario's outcome step verifies them.

A feature spanning two contexts mixes two languages in one specification and hides which context owns the behaviour it
describes.
