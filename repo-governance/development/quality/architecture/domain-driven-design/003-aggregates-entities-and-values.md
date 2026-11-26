---
description: >-
  Fixes the tactical model: aggregates enforce every invariant and bound a transaction, value objects are immutable and
  validated, entities compare by typed identity, and domain events are past-tense and immutable.
when_to_use: >-
  Use when designing an aggregate, deciding between an entity and a value object, naming or publishing a domain event,
  or placing an invariant.
---

# Aggregates, Entities, and Values

## Aggregates Own Invariants

Every business invariant is enforced by the aggregate root that owns it, inside the domain model. It is never enforced
in an adapter, an application service, or a port implementation.

The application layer orchestrates: it loads the aggregate through a repository that hides storage, calls the method
that enforces the rule, and saves the result through that repository. A rule checked anywhere else can be bypassed by
the next caller that goes around it, and it cannot be tested without the infrastructure that surrounds it.

- **One aggregate per transaction.** A transaction changes one aggregate. A change that must reach another aggregate
  travels as a domain event and is eventually consistent.
- **Small aggregates.** An aggregate holds few entities, typically no more than five. A large aggregate loads slowly and
  turns unrelated edits into concurrency conflicts.

## Ports Follow Aggregates

Where [Hexagonal Architecture](../hexagonal-architecture.md) applies:

- each command that changes an aggregate is exposed as exactly one inbound port, and no inbound adapter calls aggregate
  methods directly;
- each aggregate root that needs persistence has exactly one repository port, two roots never share one, and each port
  is sized by use case as [Ports and Adapters](../hexagonal-architecture/002-ports-and-adapters.md) requires;
- list, summary, and dashboard views read through a separate query port and never load aggregates, because loading an
  aggregate for a read-only projection pays for consistency the read does not need.

## Value Objects

Every domain primitive, such as an amount with its currency, a date in a business calendar, or a rate, is an immutable
value object.

- Its constructor validates its invariants, so an invalid value cannot exist.
- It has no setters. A change produces a new value.
- Two value objects are equal when their values are equal.

## Entities

- An entity is compared by identity, never by its attributes, because its attributes change while it stays the same
  thing.
- Identities are strongly typed. An identifier of one kind cannot be passed where another kind is expected, which a bare
  string or number cannot prevent.
- A lifecycle whose transitions carry business meaning follows [Finite-State Machines](../finite-state-machines.md).

## Domain Events

- Every significant business occurrence raises a domain event.
- An event is named for the entity and a past-tense verb, such as `PaymentReceived`. Present and future tense are
  refused: an event records something that already happened.
- An event is immutable once raised.
- An event is published only after the aggregate's change is persisted, as
  [Cross-Context Integration](002-cross-context-integration.md) requires.
