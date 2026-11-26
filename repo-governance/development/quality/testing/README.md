---
description: >-
  Indexes the testing standards: which layer and gate a test belongs to, how tests come first, what API, behaviour, and
  end-to-end tests assert, how tests isolate data and fixtures, and which test doubles replace what.
when_to_use: >-
  Use when deciding how a change is tested, which test layer or gate applies, how a test isolates its data and fixtures,
  or which test double replaces a collaborator.
---

# Testing Standards

Testing standards. They answer which test proves a behaviour, where it runs, and what a test may replace or touch.

## Directory Map

- [API Testing](api-testing.md) — contract assertions per test layer, and a direct request before closing
- [Behaviour-Driven Development](behaviour-driven-development.md) — scenario or plain test, one Gherkin corpus per owner
  of runtime code, scenario-first changes, strict bindings, scoped exemptions
- [Behaviour-Driven Development Modules](behaviour-driven-development/README.md) — discovery, layers, bindings and
  exemptions, compliance
- [End-to-End Testing](end-to-end-testing.md) — public-boundary observation, per-case fixtures, gate placement, browser
  cleanup
- [Git Fixture Isolation](git-fixture-isolation.md) — six layers keeping test git commands out of real repositories
- [Meaningful Coverage](meaningful-coverage.md) — the 99% floor on unit coverage over the whole project, what stays
  outside it, and native verification where no instrument is reliable
- [Meaningful Coverage Modules](meaningful-coverage/README.md) — the allowed exclusions, with no exemption for
  unreachable code
- [Test Boundaries and Gates](test-boundaries-and-gates.md) — what each test boundary excludes, separate suites, gates
  composed from named targets, the fast gate, and gating coverage
- [Test Data Isolation](test-data-isolation.md) — synthetic data inside a per-run boundary, removed exactly
- [Test Doubles](test-doubles.md) — in-memory fakes over mocks, stubbed external services, and real domain objects
- [Test-Driven Development](test-driven-development.md) — test-first red, green, and refactor cycles for behaviour
  changes and bug fixes, with scope and exemptions
- [Test-Driven Development Modules](test-driven-development/README.md) — cycle evidence, test design, regression tests,
  and intermittent failures
