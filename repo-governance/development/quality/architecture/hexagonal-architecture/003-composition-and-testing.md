---
description: >-
  Requires one composition root per context as the only place adapters are built, a separate test composition root, an
  in-memory adapter for each output port, and one contract suite run against every adapter.
when_to_use: >-
  Use when wiring adapters to ports, setting up unit tests for an application layer, or adding an adapter for an
  existing port.
---

# Composition Roots and Test Adapters

## One Composition Root per Context

Each context has exactly one composition root, and it is the only place adapter implementations are constructed and
bound to ports. Nothing else, whether a use case, a domain object, or an adapter, constructs an adapter or a wired
service. Domain values and commands are not wired components and are exempt.

A single root makes the active set of adapters readable in one file, and it makes swapping an adapter for a migration or
a test a one-file change. Wiring spread across services or framework annotations collapses the boundary without any
visible sign: the application starts depending on concrete adapters through discovery instead of through ports.

Where one deployable holds several contexts, each context keeps its own root, and a top-level root assembles them.

## A Separate Test Composition Root

Unit tests wire through a test composition root that binds test adapters in place of production ones. It never imports
the production root, so a unit test cannot start real infrastructure by accident.

## An In-Memory Adapter per Output Port

Every output port used in unit tests has an in-memory adapter kept with the tests. It implements the port's complete
contract, it is the only persistence the unit tests use, and it is never deployed to any environment.

## One Contract Suite for Every Adapter

Each output port has one shared contract suite that describes its behaviour. It is written once and run against every
adapter of that port, at the test level that matches the adapter's strongest real boundary:

| Adapter                                                         | Runs the contract suite at                                       |
| --------------------------------------------------------------- | ---------------------------------------------------------------- |
| the in-memory adapter                                           | unit level                                                       |
| a real adapter over an isolated local resource, with no network | integration level                                                |
| a real adapter reached over the network                         | end-to-end level only, through the application's public boundary |

The port's contract is a specification, and every adapter is a candidate implementation of it. Running one suite against
each is what makes swapping adapters in the composition root safe, and it is the reason the in-memory adapter can be
trusted in unit tests at all.

## What Each Level Covers

- **Domain logic** is tested as pure functions, with no adapter involved.
- **Application use cases** are tested through the test composition root, with no infrastructure started.
- **Real adapters** are tested by the contract suite at the level the table assigns them.

Choosing among kinds of test double beyond the in-memory adapter is a testing decision rather than a layering one, and
it is outside this standard.
