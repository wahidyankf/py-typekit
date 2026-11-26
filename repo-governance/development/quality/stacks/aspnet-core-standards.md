---
description: >-
  Fixes ASP.NET Core stack choices on top of the .NET language baseline: validated options that fail at startup,
  validated requests and typed results, deliberate service lifetimes, pooled outbound HTTP clients, and in-process host
  tests for the request pipeline.
when_to_use: >-
  Use when building, configuring, or reviewing an ASP.NET Core application in C# or F#, or when binding its options,
  validating its requests, choosing a service lifetime, or testing through its host.
---

# ASP.NET Core Standards

This standard is canonical for ASP.NET Core and holds only the choices the framework leaves open. It inherits the
project's .NET language standard, [C# Standards](csharp-standards.md) or [F# Standards](fsharp-standards.md), whose
gates, runtime line, build defaults, and failure rules apply unchanged. An ASP.NET Core skill defers here per rule; a
functional layer on the framework, such as [Giraffe Standards](giraffe-standards.md), adds its own rules on top.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Fail Closed](../../../principles/fail-closed.md), and [Reproducibility](../../../principles/reproducibility.md).

## Gates

ASP.NET Core adds no gate; the language standard's gates cover framework code, and the framework version follows the
runtime line that standard fixes.

## Type and Boundary Safety

ASP.NET Core maps [Type and Boundary Safety](../code/type-and-boundary-safety.md) as follows.

- **Options are validated at startup.** Each settings group binds to one
  [options](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options) type, validated by data
  annotations or a validator class and registered with validation on start, so an invalid value stops the host instead
  of failing on first use. Code reads settings through that type, never by string key.
- **Requests are validated before the handler decides.** Bound request models pass built-in validation, or the adopter's
  recorded validation library, before business logic runs; a failure becomes a problem-details response.
- **Responses are typed.** A minimal API endpoint returns
  [typed results](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/responses), declaring the
  union it can produce, so the compiler checks each return and the published description stays accurate.

## Request Pipeline

These follow the framework's
[best practices](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices).

- **The request context stays on its request.** The HTTP context is never stored in a field or used from another thread
  or after the request ends; handed-off work copies the values it needs.
- **Service lifetimes are deliberate.** A singleton never holds a scoped service. A background service creates a scope
  per unit of work and resolves scoped services inside it.
- **Outbound HTTP uses the client factory.** Clients come from the framework's factory, typed per upstream service,
  never constructed per request (exhausting sockets) nor held as one static instance (missing DNS changes).
- **Middleware order is declared once.** One composition root assembles the pipeline in an order checkable against the
  framework's documented sequence, as
  [Composition Roots and Test Adapters](../architecture/hexagonal-architecture/003-composition-and-testing.md) requires.
- **Endpoints only translate.** An endpoint, controller, or handler binds input, calls one application function, and
  maps its result; it holds no business rule.

## Tests

Layers follow [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Application logic is unit-tested
without the host. A test running the request pipeline starts the application in-process through the framework's
[integration test host](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests), lives in its own test
project, and is an integration test.

- The test host's service registration replaces only outbound adapters; routing, binding, validation, authorization, and
  serialization run as in production.
- A database test runs against the real provider, or an in-memory relational database where the adopter records that
  choice, never a non-relational in-memory stand-in, which skips constraints and translation.
- Each authorization policy has a test refusing a caller who lacks it.

Coverage follows [Meaningful Coverage](../testing/meaningful-coverage.md); host startup wiring and generated contract
code are named exclusions when no test layer usefully reaches them.

## Documentation

An HTTP contract follows [OpenAPI Contract First](../architecture/openapi-contract-first.md). A framework-generated
description is checked against the authored contract, never published in its place.

## Enforcement

The language standard's compiler, analyzer, and formatter gates enforce in the adopter's build and pull-request gate; a
startup test proves invalid options stop the host. Review applies lifetimes, client creation, context handling, and
endpoint thinness.
