---
description: >-
  Structures an application as a domain, an application layer that owns ports, and adapters at the edge, with every
  dependency pointing inward and adapters wired in one composition root.
when_to_use: >-
  Use when structuring a backend service, command-line tool, or web application into layers, or when deciding whether
  code belongs in the domain, the application layer, or an adapter.
---

# Hexagonal Architecture

Hexagonal architecture, also called ports and adapters, keeps business logic independent of how it is invoked and where
its data lives. The domain sits at the centre, and everything else adapts to it.

This standard implements [Pure Functions](../../../principles/pure-functions.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), and
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md).

## Modules

1. [Layers and the Dependency Rule](hexagonal-architecture/001-layers-and-dependency-rule.md)
2. [Ports and Adapters](hexagonal-architecture/002-ports-and-adapters.md)
3. [Composition Roots and Test Adapters](hexagonal-architecture/003-composition-and-testing.md)
4. [Application Shapes](hexagonal-architecture/004-application-shapes.md)

## The Rule in One Sentence

Dependencies point inward only. Adapters rely on the application layer, the application layer relies on the domain, and
the domain has no outward dependency at all.

Everything in the modules follows from that sentence. A layer that cannot import its neighbour cannot couple to it by
accident, so each inner layer can be tested and replaced without starting anything outside it.

## Scope

This standard fixes layering: which code belongs in which layer, what may cross between layers, and how adapters are
wired and tested.

It does not fix directory names, which are the adopter's and follow each stack's idiom. It does not govern how several
contexts inside one system relate to one another, which is a question of domain design rather than of layering.

## Enforcement

A layer boundary is enforced mechanically, because review alone lets the first leaking import through. An adopter checks
forbidden imports in its own lint or build gate, using whatever its stack offers: a compiler-enforced module boundary,
an import-boundary rule, or a dependency-direction check that fails the change.
