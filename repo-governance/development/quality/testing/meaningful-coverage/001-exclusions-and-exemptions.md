---
description: >-
  Limits coverage exclusions to generated files and test-support programs, records each with its reason in one place,
  and admits no exemption: code a unit test cannot reach moves behind a port.
when_to_use: >-
  Use when adding or reviewing a coverage exclusion, deciding whether code may leave the measured set, or handling code
  a unit test cannot reach.
---

# Exclusions

An exclusion removes authored code from the denominator, so each one makes the floor in
[Meaningful Coverage](../meaningful-coverage.md#the-floor) easier to clear. Few kinds are allowed, and each is written
down once.

## Two Allowed Exclusions

- **Generated files.** Each carries a generated-code header, and the generator's own tests cover it.
- **Test-support programs.** Programs that only support tests, such as fixture builders and the coverage tool itself,
  are test code, not production code.

No other kind is excluded.

## One Place, One Reason

Each exclusion sits in the gating run's coverage configuration with its reason beside it. No other document restates the
list; the project README links to the configuration. A second list is a second copy that drifts.

## Unreachable Code Is Not Excluded

There is no exemption. Code a unit test cannot reach, such as a resource or a process boundary, stays in the measured
set and moves behind a port until a unit test backed by a [test double](../test-doubles.md) reaches it, following
[Hexagonal Architecture](../../architecture/hexagonal-architecture.md) and
[Functional Core, Imperative Shell](../../architecture/functional-core-imperative-shell.md), as
[Coverage Floor](../../checks/test-and-gate-contract/006-coverage-floor.md) requires. An integration or end-to-end test
never stands in for the unit figure. Difficulty, schedule, and unfinished work are never reasons, and choosing a core
package to measure is a wholesale exclusion that none of these categories allows.

## Enforcement

Gated by the adopter's coverage configuration check, which fails on an exclusion that has no reason and on an excluded
path that is neither generated nor test support. Unenforced by decision: whether a file is generated or test support is
a review judgement, applied as [Software Quality Enforcement](../../checks/software-quality-enforcement.md) requires.
