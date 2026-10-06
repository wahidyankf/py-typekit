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

- [Meaningful Coverage](meaningful-coverage.md) — what numeric coverage may measure, what stays outside it, and native
  verification where no instrument is reliable
- [Test Boundaries and Gates](test-boundaries-and-gates.md) — what each test boundary excludes, separate suites, gates
  composed from named targets, the fast gate, and gating coverage
- [Test Doubles](test-doubles.md) — in-memory fakes over mocks, stubbed external services, and real domain objects
- [Test-Driven Development](test-driven-development.md) — test-first red, green, and refactor cycles for behaviour
  changes and bug fixes, with scope and exemptions
- [Test-Driven Development Modules](test-driven-development/README.md) — cycle evidence, test design, regression tests,
  and intermittent failures
