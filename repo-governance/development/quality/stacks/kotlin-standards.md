---
description: >-
  Fixes the Kotlin baseline: warnings as errors, explicit API mode for libraries, stable formatter and linter gates,
  nullability decided at Java boundaries, sealed states, owned coroutine scopes, and Kover coverage.
when_to_use: >-
  Use when creating, configuring, or reviewing a Kotlin JVM project, or choosing its compiler options, lint tools,
  failure shape, coroutine structure, test framework, or coverage rules.
---

# Kotlin Standards

Canonical for Kotlin on the JVM: the choices Kotlin and its Gradle plugin leave open; a Kotlin skill defers here per
rule. A Kotlin Gradle build script is build configuration, not a Kotlin project.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), [Pure Functions](../../../principles/pure-functions.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). The committed build wrapper, version catalog,
and plugin versions follow [Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Compiler:** every module sets `allWarningsAsErrors` and `extraWarnings` in `compilerOptions`
  ([compiler options](https://kotlinlang.org/docs/gradle-compiler-options.html)).
- **Explicit API:** a library module enables strict `explicitApi()`, so every public declaration states its visibility
  and type ([explicit API mode](https://kotlinlang.org/docs/whatsnew14.html#explicit-api-mode-for-library-authors)).
- **Format and lint:** a formatter-linter at the official code style and a static analyser, both on a pinned stable
  line, never a prerelease major, with no overlapping layout rules. Example: ktlint with `ktlint_official`
  ([ktlint](https://github.com/ktlint/ktlint)) and detekt ([detekt](https://github.com/detekt/detekt)).

Each suppression names its rule and reason where it applies, per [Lint Strictness](../checks/lint-strictness.md).

## Type and Boundary Safety

Kotlin maps [Type and Boundary Safety](../code/type-and-boundary-safety.md) as follows.

- A Java API value has an unchecked platform type; the first Kotlin line receiving it decides nullability by assigning
  an explicitly nullable or non-null type.
- `!!` appears only where a check the compiler cannot see proves presence, never to silence an error
  ([null safety](https://kotlinlang.org/docs/null-safety.html)). `lateinit` is only for a property a framework or test
  setup assigns before any read.
- External data is deserialized into typed classes and validated on arrival; inner code never reads an untyped map.
- A closed set of states is a sealed type, handled in a `when` without `else`, so a new state breaks every site that
  must decide about it.

## Coroutines

Each coroutine launches in a scope whose end something owns (a request, a component, or an injected scope cancelled on
shutdown), never a global scope. A `suspend` function never blocks its thread; blocking work moves to an injected
dispatcher built for it. A broad `catch` around suspending code rethrows `CancellationException`, which `runCatching`
also catches.

## Values

Properties are `val` and collections read-only unless mutation is the point; a data class changes through `copy`.
Boolean arguments are passed by name; code follows the
[official coding conventions](https://kotlinlang.org/docs/coding-conventions.html).

## Tests

Tests keep unit and integration layers apart per [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md).
Suspending code is tested on a virtual-time test dispatcher; the unit layer reads no real clock. Example: `runTest` from
kotlinx-coroutines-test.

Per [Meaningful Coverage](../testing/meaningful-coverage.md), Kover measures lines, instructions, and branches; its
verification task fails the build below a recorded rule. Generated classes are excluded by pattern or annotation, each
with a reason ([Kover](https://kotlin.github.io/kotlinx-kover/gradle-plugin/)). Any floor above the minimum is recorded
under [Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Documentation

Public declarations carry KDoc, from which a published library generates its reference, for example with Dokka
([KDoc](https://kotlinlang.org/docs/kotlin-doc.html)). A behaviour change updates KDoc with the code, as
[Specification Maintenance](../evidence/specification-maintenance.md) and
[Public Contract](../architecture/public-contract.md) require.

## Adopter Decisions

| Decision          | Option                              | Gains                                     | Costs                                  |
| ----------------- | ----------------------------------- | ----------------------------------------- | -------------------------------------- |
| test framework    | JUnit with `kotlin.test` assertions | one runner shared with Java tests         | plainer specification style            |
|                   | Kotlin-first, such as Kotest        | specification styles and property testing | a second idiom beside Java tests       |
| expected failures | exceptions                          | the JVM idiom; no library wrapping        | signatures hide what can fail          |
|                   | sealed result types                 | the compiler makes every caller decide    | every throwing library call is wrapped |

Record each choice once.

## Enforcement

An adopter runs the compiler, format, lint, and coverage gates in its pull-request gate. Review applies boundary
nullability, `!!` and `lateinit` claims, coroutine ownership, and coverage exclusions.
