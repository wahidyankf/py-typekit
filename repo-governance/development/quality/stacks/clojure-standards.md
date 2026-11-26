---
description: >-
  Fixes the Clojure baseline: format and lint gates, reflection warnings as failures, data specifications validated at
  external input, namespace and laziness rules, and line and form coverage.
when_to_use: >-
  Use when creating, configuring, or reviewing a Clojure project, or choosing how it validates boundary data, reports
  failures, runs tests, or measures coverage.
---

# Clojure Standards

Canonical for Clojure on the JVM, this standard fixes what the language and its CLI leave open; a Clojure programming
skill defers here for each rule.

It implements the [explicitness](../../../principles/explicit-over-implicit.md),
[immutability](../../../principles/immutability.md), [pure-function](../../../principles/pure-functions.md), and
[automation](../../../principles/automation-over-manual.md) principles. `deps.edn` coordinates and tool versions follow
[Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Format:** the formatter checks against committed settings and fails on any unformatted file. Example:
  [cljfmt](https://github.com/weavejester/cljfmt) `check` reading `.cljfmt.edn`.
- **Lint:** a static analyser fails on warnings in source and test paths, reading committed configuration. Example:
  [clj-kondo](https://github.com/clj-kondo/clj-kondo) with `--fail-level warning` and `.clj-kondo/config.edn`.
- **Reflection:** every namespace using Java interop sets `*warn-on-reflection*` to true, and the build loading them
  fails on any reflection warning; a type hint resolves each
  ([Java interop](https://clojure.org/reference/java_interop)).

Each suppression names its reason in place, per [Lint Strictness](../checks/lint-strictness.md).

## Type and Boundary Safety

Clojure maps [Type and Boundary Safety](../code/type-and-boundary-safety.md) thus:

- With no static type checker, the type check target is omitted with that reason; the linter's type-mismatch checks
  catch some errors but prove nothing ([types](https://github.com/clj-kondo/clj-kondo/blob/master/doc/types.md)).
- External data is validated against an explicit data specification where it arrives; inner code relies on the validated
  shape. Production code calls validation or coercion explicitly, never instrumentation, which checks arguments only and
  suits development and tests ([spec guide](https://clojure.org/guides/spec)).

## Namespaces and Effects

One namespace per file, named after its path. A namespace requires others under an alias or refers named symbols, never
`:refer :all` or `use`. A function never calls `def`, and a dynamic var's name carries earmuffs, per the
[style guide](https://guide.clojure.style/).

Decisions are functions over immutable data. I/O, atoms, and every other state change live in shell namespaces, per
[Functional Core, Imperative Shell](../architecture/functional-core-imperative-shell.md).

## Laziness

No effect runs inside a lazy sequence: effects use `run!` or `doseq`. A lazy sequence built inside `with-open` or a
dynamic binding is realized within that scope, never returned unrealized.

## Tests

`clojure.test` is the framework, run through a recorded runner; integration tests stay out of the unit run, per
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Tests inject collaborators as arguments, never via
`with-redefs` in a test that may run in parallel. A behaviour holding across an input range also gets a generative test,
such as test.check.

Coverage follows [Meaningful Coverage](../testing/meaningful-coverage.md) and measures lines and forms, not branches;
example: [cloverage](https://github.com/cloverage/cloverage), excluding generated namespaces by pattern with each reason
recorded. The unit figure carries the floor, and
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md) records any higher one.

## Documentation

Public vars carry docstrings; implementation details are private through `defn-` or `^:private`. A behaviour change
updates docstrings and specifications with the code, per
[Specification Maintenance](../evidence/specification-maintenance.md) and
[Public Contract](../architecture/public-contract.md).

## Adopter Decisions

| Decision          | Option                                                                          | Gains                                 | Costs                                                                             |
| ----------------- | ------------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------- |
| boundary data     | the bundled spec library                                                        | no added dependency                   | its namespace is still alpha                                                      |
|                   | a data-driven schema library, such as [Malli](https://github.com/metosin/malli) | schemas are plain, transformable data | a dependency, weighed per [Dependency Selection](../code/dependency-selection.md) |
| test runner       | `clojure.test` through a CLI alias                                              | the fewest tools                      | fewer reporters, no watch mode                                                    |
|                   | a dedicated runner, such as Kaocha                                              | watch mode, plugins, and focused runs | one more tool to pin                                                              |
| expected failures | `ex-info` carrying a data map                                                   | keeps the stack trace                 | callers must know what to catch                                                   |
|                   | a returned result map                                                           | failures stay ordinary data           | every caller branches on it                                                       |

Record each choice once.

## Enforcement

Adopters run the format, lint, reflection, and test gates in their own pull-request gate; review applies boundary
validation, namespace and effect placement, laziness, and test isolation.
