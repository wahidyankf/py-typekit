---
description: >-
  Fixes the Java baseline: long-term-support runtimes only, a committed, verified build wrapper, build-failing formatter
  and coverage gates, and Java rules for data types, injection, and failures.
when_to_use: >-
  Use when creating, building, or reviewing a Java project, choosing its runtime line, build wrapper, or formatter gate,
  or deciding how a class holds data, receives dependencies, or reports a failure.
---

# Java Standards

This standard is canonical for the choices Java and its build tools leave open; a Java programming skill defers here.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), [Pure Functions](../../../principles/pure-functions.md), and
[Reproducibility](../../../principles/reproducibility.md).

## Long-Term-Support Runtimes Only

Every project runs on a long-term-support release; a new project starts on the current one. Interim feature releases are
not adopted: each loses updates when its successor ships, forcing per-cycle upgrades or unpatched running. Contributors
and the pipeline install the same JDK distribution, recorded with its release in build files.

## The Committed Build Wrapper

The build tool runs only through its committed wrapper, whose properties record the distribution checksum, so a
substituted download fails before building. The build names its JDK through the toolchain setting, so the declared JDK
compiles. This is how Java meets [Native-First Toolchain](../../workflow/native-first-toolchain.md); dependency pins
follow [Dependency Bump Policy](../../workflow/dependency-bump-policy.md).

Example: Gradle's `distributionSha256Sum` and a toolchain block.

## Gates

- **Formatting:** one formatter rewrites staged Java files on commit; the pipeline fails on any file it would still
  change. No file carries a formatter suppression. Example: google-java-format via a build plugin.
- **Coverage:** verification runs inside the unit-test target, and the build fails below the floor in
  [Meaningful Coverage](../testing/meaningful-coverage.md), or below a higher floor the adopter records under
  [Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md). Exclusions follow
  [Exclusions](../testing/meaningful-coverage/001-exclusions-and-exemptions.md).
- **Warnings:** compiler and lint findings fail at the [Lint Strictness](../checks/lint-strictness.md) threshold.

Work proceeds test-first under [Test-Driven Development](../testing/test-driven-development.md); each contract
behaviour, error paths included, is a [Behaviour-Driven Development](../testing/behaviour-driven-development.md)
scenario before code exists. A reformat outside the change's purpose is out of scope under
[File-Touch Discipline](../../workflow/file-touch-discipline.md).

## Code Shape

- **Package by feature.** A feature's handler, logic, and types share a package. No package collects one layer across
  features, except one package of framework-free configuration logic.
- **Records and final fields.** Identity-free data is a `record`. A stateful class assigns `final` fields in its
  constructor; a domain type has no setters, since a mutable value can change between check and use.
- **Constructor injection only.** Never inject into a field. A constructor keeps fields `final`, fails at startup on a
  missing dependency, and lets a test build the class frameworkless.
- **Decisions outside the framework.** Logic worth a test lives in a class importing no framework, per
  [Functional Core, Imperative Shell](../architecture/functional-core-imperative-shell.md). A hand-written request
  handler only translates; its request and response models are generated from the contract, per
  [OpenAPI Contract First](../architecture/openapi-contract-first.md).
- **Declared configuration.** Behaviour the service relies on is set explicitly even where a default matches, since
  defaults change between major versions. Operational and diagnostic endpoints are exposed only via an explicit allow
  list; a test asserts the rest unreachable. An invalid supplied value stops startup, per
  [Environment Variable Contract](../../../conventions/security/environment-variable-contract.md).

## Failures

- An outcome the immediate caller branches on (a missing resource, bad input) is a return value. A specific unchecked
  exception serves an outcome handled at an outer boundary, so no intermediate caller repeats `throws`.
- A programming error propagates; catching `Exception` to return a default turns a defect into wrong data. Catch the
  narrowest type where a decision lies, never discard an exception, pass the cause when wrapping, and never catch
  `Throwable`.
- A message names the expected value, what arrived, and which input.
- An error response carries no stack trace, exception class, path, host, configuration value, or secret: the client gets
  a stable status and generic message; the log gets the detail.

Test sleeps, retries, and loosened assertions fall under
[Intermittent Failures](../testing/test-driven-development/004-intermittent-failures.md).

## Enforcement

Formatter, coverage, and compiler settings enforce the gates in the adopter's build and pull-request gate; review
applies the code shape and failure rules.
