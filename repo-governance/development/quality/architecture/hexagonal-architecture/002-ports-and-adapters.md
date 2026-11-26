---
description: >-
  Fixes port ownership and granularity, what inbound and outbound adapters may and may not do, and where mapping between
  domain and infrastructure representations lives.
when_to_use: >-
  Use when declaring a port, implementing an adapter, or reviewing an adapter for business logic or an overly wide
  interface.
---

# Ports and Adapters

## The Application Owns Every Port

A port is a named interface, whether an interface type, a trait, a function type, or a record of functions. The
application layer declares it, or the domain does for an outbound need it expresses itself. A port says what the
application needs without saying how the need is met.

- **Inbound ports** are the entry points adapters call: use cases and application services.
- **Outbound ports** are what the application requires from outside: repositories, notifiers, and gateways.

An adapter never declares its own port. An adapter that owns its contract cannot be replaced without rewriting that
contract, and being replaceable is the point.

## One Concern per Outbound Port

Each outbound port serves exactly one external concern. A port that bundles persistence, supplier notification, and
email is three ports behind one name, and a test that needs one of them must satisfy all three.

A repository port declares only the operations some use case actually calls, not a complete create, read, update, and
delete surface. A use case that only queries gets a port that only queries.

## Inbound Adapters Translate and Delegate

An inbound adapter does three things, in order:

1. translates the external representation, such as a request body, command-line arguments, or a message payload, into an
   application command or query;
2. calls the inbound port; and
3. translates the result or the error back into the external representation.

It evaluates no business rule, calls no outbound port directly, and constructs domain objects only as far as mapping
requires.

## Outbound Adapters Implement Exactly One Port

An outbound adapter implements exactly the one port it satisfies. It maps domain objects to the infrastructure
representation, and maps what comes back into domain objects or result values.

It holds no business logic and enforces no invariant. It calls no other adapter, and it neither owns nor changes domain
state.

## Mappers Live in Adapters

Mapping between a domain object and an infrastructure representation, whether a storage record, a wire payload, or a
generated contract type, lives in the adapter. It never lives in the domain or the application layer.

The domain then carries no persistence annotation or serialization attribute, and changing a storage schema or a wire
format never touches business code.
