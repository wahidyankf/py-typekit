---
description: >-
  Where an HTTP API is described with OpenAPI, makes that document the only authored source of its contract, with
  clients and server interfaces generated from it and never edited, and leaves committing generated output to the
  adopter.
when_to_use: >-
  Use when adding or changing an HTTP API described with OpenAPI, generating code from that description, or diagnosing
  drift between a description and generated code.
---

# OpenAPI Contract-First

The [OpenAPI](https://spec.openapis.org/oas/latest.html) document is written before the implementation, and it is the
only place the API contract is authored. Code follows from the description; the description never follows from the code.

That removes a whole class of defect: a client and a server that disagree about a field name, a type, or a status code
because each was written from its author's memory of the other.

It applies where the adopter describes an HTTP API with OpenAPI; it does not choose that description format for every
API.

This standard implements [One Source Per Fact](../../../principles/one-source-per-fact.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Automation Over Manual](../../../principles/automation-over-manual.md), and
[Reproducibility](../../../principles/reproducibility.md).

## The Description Comes First

1. **Design.** Author or change the OpenAPI document: every operation, request body, response, and error.
2. **Review.** Agree the change with the API's consumers before anyone implements it.
3. **Validate and bundle.** Lint the document, then resolve its references into one self-contained bundle. Every
   generator reads the bundle, never the split source files.
4. **Generate.** Produce typed clients, server interfaces, and validation schemas from the bundle.
5. **Implement.** Write handlers that conform to the generated server interface, and consumers that call the generated
   client.

A backend with no client still generates its server interface, so an operation added to the description fails the build
or type check, where the stack has one, until something serves it.

## Generated Code Is Never Edited

Generated files are derived artifacts. When the output is wrong, fix the description or the generator's configuration
and regenerate. A hand edit is lost at the next generation, and until then it is a contract nobody declared.

Where generated output is not committed, every step that consumes generated code, including type checking, building, and
any test that compiles against it, depends on generation from the current description, so no step reads stale output.
Where it is committed, the regenerate-and-compare check in the decision below is the guarantee.

## Generated Types Stay at the Boundary

Generated request and response types live in the inbound adapter of a
[Hexagonal Architecture](hexagonal-architecture.md) application, or in the shell of a
[Functional Core, Imperative Shell](functional-core-imperative-shell.md) module. Domain types are written by hand and
never generated, and the adapter maps between the two. A domain that imports generated types has let the wire format
decide its model.

## Committing Generated Output Is an Adopter Decision

The adopter records one option and the drift control that comes with it:

| Option                      | Drift control                                                               | Gains                                                                                              | Costs                                                                                                                       |
| --------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| commit the generated output | a gate regenerates and fails when the result differs from what is committed | generated changes are reviewable in the diff; a fresh checkout and an editor resolve types at once | a drift gate to keep green; generated noise in diffs and merge conflicts                                                    |
| do not commit it            | every consuming step depends on generation, so committed drift cannot exist | no drift gate and no generated diffs                                                               | a fresh checkout or editor must generate before types resolve; the generator must be deterministic and available everywhere |

The rule is the same either way: generated code always matches the current description, and a mismatch fails a check
before merging rather than surfacing at runtime.

## Enforcement

An adopter enforces description linting, the generation dependency where generated output is not committed, and the
regenerate-and-compare drift check where it is, in its own build configuration and continuous integration.
