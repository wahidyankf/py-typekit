---
description: >-
  Applies hexagonal layering to multi-context services, command-line tools, and web applications, and records the
  adopter's choice between hexagonal layering and a functional core for web applications.
when_to_use: >-
  Use when applying hexagonal layering to a particular kind of application, or when choosing how a web application is
  structured.
---

# Application Shapes

The layers and their rules are the same in every kind of application. What changes is which adapter is the entry point,
and where the pressure to leak a layer comes from.

## Services With Several Contexts

Where a service holds several contexts, each context owns its complete set of layers and its own composition root.
Infrastructure that several contexts share, such as a connection pool, a migration runner, or common middleware, sits in
a shared infrastructure location and carries no business logic. Shared infrastructure that acquires a business rule has
become a context nobody declared.

## Command-Line Tools

For a command-line tool, the arguments are the inbound signal, just as a request is for a service.

- Argument parsing lives only in the command inbound adapter, and the parsing library is imported nowhere else.
- That adapter checks argument types and required values, maps parsed arguments to application input types, maps
  application errors to human-readable messages and exit codes, and writes results to standard output and standard
  error.
- The domain and application layers never see a flag, an exit code, or terminal output. They receive typed input and
  return values or errors.
- Filesystem access, external calls, and subprocesses are outbound adapters behind ports.

A tool built this way tests its domain without a command-line harness, and its exit codes are decided in one place, as
its [Public Contract](../public-contract.md) needs.

## Web Applications

In a web application, interface components, pages, routes, and layout form a presentation layer. It is an inbound
adapter: it calls application use cases, holds no business rules, and the application layer knows nothing about
components or routing.

A full-stack web application that serves its own API from the same codebase, rather than consuming a separate backend
service, is layered as a web application. Its API routes are presentation-side inbound adapters, not a second backend.

## Hexagonal Layering or a Functional Core for the Web

How web applications are structured is an adopter decision, recorded once and applied to every web application in the
repository.

| Option                                                                                  | Gains                                                                                                      | Costs                                                                                                             |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| hexagonal layering with a presentation layer                                            | one vocabulary shared with backend services; an API client or browser storage is replaceable behind a port | four layers, ports, and a composition root in applications whose logic is mostly presentation                     |
| [Functional Core, Imperative Shell](../functional-core-imperative-shell.md) per feature | two zones and no wiring; the shell imports the core directly                                               | no dedicated port or composition root for replacing infrastructure; a second vocabulary beside hexagonal services |

Both keep decisions free of effects and testable without a runtime. The choice decides whether replacing infrastructure
is worth ports and wiring in applications of that kind.
