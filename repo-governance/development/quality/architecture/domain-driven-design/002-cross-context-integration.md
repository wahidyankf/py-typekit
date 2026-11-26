---
description: >-
  Fixes how contexts communicate: published interfaces and events only, events through owned ports after persistence,
  anti-corruption layers in the consumer, a declared shared kernel, and orchestrated sagas.
when_to_use: >-
  Use when one context needs another's data or reacts to its events, when a type seems worth sharing, or when a process
  spans contexts.
---

# Cross-Context Integration

## Only Published Interfaces Cross

A context calls another only through that context's published application interfaces, such as its inbound ports or its
open host service, or reacts to the events it publishes. It never reaches into another context's domain objects,
repositories, or storage.

Everything a context has not published stays free to change. A direct reach into its internals turns an internal
refactoring into a break in a context nobody thought was affected.

## Events First

Contexts communicate through domain events wherever the business process tolerates eventual consistency. A synchronous
query to another context is used only when the downstream needs the data before it can finish its own use case.

- An event is published through an outbound port the originating context owns, never by calling a message broker from an
  application service, so the publishing contract stays testable and the broker replaceable.
- An event is published only after the change that raised it is persisted, never before the transaction commits.
- Event names and immutability follow [Aggregates, Entities, and Values](003-aggregates-entities-and-values.md).

## Anti-Corruption Layers Sit in the Consumer

Where a downstream context consumes a model that differs from its own, whether another context's or an external
system's, an anti-corruption layer adapter in the consuming context performs all translation. No translation logic sits
in an application service or a domain object.

Outside a declared conformist relationship, no upstream type reaches the downstream domain: a downstream aggregate never
holds a field typed as an upstream transfer object; the adapter translates into the downstream's own value type first.

## Open Host Services Stay Stable

A context serving several downstream consumers publishes a stable interface, versioned independently of its internal
model. Refactoring the internal model does not change that interface, and a breaking change to it needs a versioning
decision under [Public Contract](../public-contract.md).

## A Declared Shared Kernel Is the Only Sharing

Two contexts share no domain type, except through one declared shared kernel.

- A type used by two or more contexts, such as a monetary amount or an identifier carried in events, lives in the
  kernel, never copied into each context and never imported from another context's domain.
- Kernel types are immutable value types with no dependency on any single context's logic.
- The contexts that use the kernel co-own it explicitly, and the kernel is declared, so its existence is a recorded
  decision.

This is a deliberate choice between two rules found in practice. Forbidding every shared domain type makes two contexts
define incompatible versions of the same value, which silently disagree on precision or currency in every event passing
between them. Allowing sharing freely couples contexts nobody decided to couple. A declared, co-owned kernel of
immutable values keeps the one agreement that has to exist, and nothing else.

## Sagas Orchestrate Processes Across Contexts

A business process spanning several contexts is coordinated by an orchestrating saga:

- it lives in its own coordination module, outside every context, and is never part of an aggregate;
- it reacts to domain events and issues commands through inbound ports only, never by calling aggregate methods;
- each step is idempotent, and the saga persists its state after each step, so a restart resumes from the last completed
  step.

One coordinator holding the process state makes the whole process readable in one place and recoverable after a failure
part-way through.
