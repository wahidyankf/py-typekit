---
description: >-
  Fixes how bounded contexts map to applications, forbids one core model spanning two contexts, and requires a context
  map whose every relationship becomes a named integration contract.
when_to_use: >-
  Use when deciding which application holds a context, splitting or merging contexts, or recording how two contexts
  relate.
---

# Bounded Contexts and Context Maps

## Contexts Guide Application Boundaries

A bounded context is the primary guide for where application boundaries fall. It is a guide, not a one-to-one rule:

| Mapping                           | Fits when                                                              |
| --------------------------------- | ---------------------------------------------------------------------- |
| one context, one application      | the default starting point: one business capability, one deployable    |
| one context, several applications | a large context is split for scale or so separate teams can work on it |
| several contexts, one application | small, closely related contexts are still young and change together    |

Whatever the mapping, each context keeps its own model. Where [Hexagonal Architecture](../hexagonal-architecture.md)
applies, each context within one application is exactly one hexagon, and several contexts in one deployable follow its
[multi-context shape](../hexagonal-architecture/004-application-shapes.md).

## No Core Model Spans Two Contexts

An application's core domain model never mixes two contexts, and two contexts never share one domain core.

Each context has one ubiquitous language. Put two in one model and a term such as "account" or "order" silently carries
two meanings, so the model can no longer be reasoned about, tested, or changed one context at a time. With a shared
core, neither context has a clean dependency direction.

## Keep a Context Map

The relationships between contexts are recorded in a context map, using the standard relationship patterns. The map is
not documentation alone: each relationship is expressed in code, so the map and the code can be compared.

| Relationship          | Meaning                                                       | Expressed in code as                                                                  |
| --------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| customer and supplier | the downstream needs data or behaviour the upstream provides  | an outbound port in the downstream, implemented by an adapter that calls the upstream |
| conformist            | the downstream adopts the upstream's published model as it is | the upstream's published contract types, used without translation                     |
| anti-corruption layer | the downstream protects its model from a different one        | an outbound port whose adapter holds all translation                                  |
| open host service     | the upstream serves several downstream contexts               | a stable interface the upstream publishes and versions                                |
| published language    | the upstream emits events in a stable schema                  | a shared event schema, and a consuming adapter in each downstream                     |
| partnership           | two contexts evolve together, with neither upstream           | each context's own ports, coupled only through shared events                          |
| shared kernel         | contexts co-own a small model fragment                        | one declared shared module, under the rules in the next module                        |

A translation between two context models always sits behind a named port. An adapter that translates without one hides
the contract, so replacing the integration technology means reading the adapter's internals.

## Why the Map Drives Code

Context mapping is a strategic decision, and ports and adapters are where it is implemented. Without a rule joining the
two, a map drawn correctly erodes in code: contexts share adapters, merge repositories, or skip translation, and the
separate models collapse into one distributed model.
