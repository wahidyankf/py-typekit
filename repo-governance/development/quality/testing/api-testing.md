---
description: >-
  Requires an API change to carry automated contract proof at each applicable test layer plus a direct request against
  the exact served origin, recorded as redacted evidence.
when_to_use: >-
  Use when a change can alter an HTTP, GraphQL, streaming, or other externally reachable API operation, or when deciding
  what evidence closes such a change.
---

# API Testing

An API is a promise to callers the author never meets. A change to it is proven twice: by automated checks pinning the
contract, and by one real request against the origin those callers use.

This standard implements [Evidence Over Assertion](../../../principles/evidence-over-assertion.md) and
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md).

## Scope Follows the Contract

It applies when a change can affect an operation a client outside the process can reach: its method or operation name,
path, parameters, headers, payload, status, response shape, errors, authorization, or side effects.

A change affecting no such operation records `API impact: none` with its reason and runs no unrelated probe, as
[Manual Verification](../manual-verification.md) requires for any inapplicable layer.

## Each Layer Proves What Only It Can

| Layer       | Proves                                                                                                                | Never                                                  |
| ----------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| unit        | business rules, input validation, authorization decisions, mapping, and error translation, with dependencies injected | opens a socket, touches the filesystem, or the network |
| integration | routing, parsing, schema validation, serialization, and middleware against isolated local stores                      | goes through the served public origin                  |
| end-to-end  | the operation as a caller meets it, through the exact served origin                                                   | substitutes an in-process call for the network request |

Whether an integration test may open a loopback listener is an adopter decision, recorded under
[Layers and Adapters](behaviour-driven-development/002-layers-and-adapters.md).

## Assert the Whole Contract

A contract assertion checks every part a caller depends on: operation, path, request headers and content type, payload
or variables, response status, response headers, response shape, declared error forms, and the promised side effect.

Cover success, invalid input, each expected failure, missing and insufficient authorization where authorization applies,
and duplicate delivery wherever the operation promises idempotency. Placing each at the narrowest layer that can prove
it is good practice, leaving slower layers for what only they show.

For GraphQL, assert the HTTP status and both the `data` and `errors` members of the body. A response can carry status
200 and an `errors` array at once, so status alone never shows success.

Generated schema checks and generated clients catch drift between a declaration and the code. They supplement these
assertions and never replace them, because a schema can be internally consistent and still wrong.

## One Real Request Before Completion

Before an API change is reported complete, invoke every affected HTTP operation directly with a command-line client,
`curl` by default or an equivalent, against the exact isolated served origin — not a nearby port, an alias, or a mock.
Exercise the successful path and every error or authorization path the change materially altered. When authentication or
authorization is in scope, use one authorized and one unauthorized synthetic identity from
[Test Data Isolation](test-data-isolation.md) and confirm both outcomes.

For streams, WebSockets, and subscriptions, `curl` confirms the handshake or upgrade; a client that speaks the protocol
then confirms the message lifecycle of open, deliver, error, and close.

Automation proves what it was told to check. A direct request catches what nobody thought to encode: a proxy rewriting a
header, a route missing from the served build, an error body no client can parse.

## Record Evidence Nobody Can Misuse

For each request, record the command shape with credentials replaced by placeholders such as `<api-token>`, a
non-sensitive description of the origin, the operation, the observed status, the response shape, the side effect, and
the result. Never record a secret, a session, or real personal data;
[Evidence Safety](../manual-verification/005-evidence-safety.md) owns how evidence is sanitized.

## A Request Never Overrides a Gate

A successful request never authorizes bypassing, skipping, or weakening a failed automated check. The two are
independent obligations, and each can fail on its own.

A plan whose work affects an API lists the direct request as a delivery item, so it is scheduled rather than remembered.
The adopter enforces the mechanical part, a changed operation with no contract assertion, in its own gate or CI.
