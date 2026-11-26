---
description: >-
  Indexes the architecture and contract standards: the as-built architecture model, how an application, its domain
  model, its lifecycles, and its decisions are structured, and how an interface others depend on is declared and
  changed.
when_to_use: >-
  Use when structuring an application, its domain model, or a lifecycle; documenting its architecture; or declaring or
  changing an interface that other code or tools depend on.
---

# Architecture and Contracts Standards

Architecture and contract standards. They answer how an application is structured and documented, and how an interface
others rely on is declared and kept compatible.

## Directory Map

- [Architecture Specifications](architecture-specifications.md) — one as-built architecture model per application, kept
  in sync
- [Architecture Specifications Modules](architecture-specifications/README.md) — model content, and scaling and change
  discipline
- [C4 Architecture Model](c4-architecture-model.md) — which C4 views exist, element and relationship labels, consistent
  styles
- [Domain-Driven Design](domain-driven-design.md) — bounded contexts, context maps, a declared shared kernel, and the
  ubiquitous language
- [Domain-Driven Design Modules](domain-driven-design/README.md) — contexts and maps, integration, the tactical model,
  language and tests
- [Finite-State Machines](finite-state-machines.md) — when a lifecycle needs a declared machine, and what it declares
  and records
- [Functional Core, Imperative Shell](functional-core-imperative-shell.md) — a pure decision core, a thin effect shell,
  one-way imports
- [Hexagonal Architecture](hexagonal-architecture.md) — inward layers, application-owned ports, adapters, composition
  roots
- [Hexagonal Architecture Modules](hexagonal-architecture/README.md) — layers, ports and adapters, composition and
  testing, application shapes
- [OpenAPI Contract-First](openapi-contract-first.md) — an API description as the only authored contract, generated code
  untouched
- [Public Contract](public-contract.md) — a tool's declared surface, and compatible versus breaking changes
