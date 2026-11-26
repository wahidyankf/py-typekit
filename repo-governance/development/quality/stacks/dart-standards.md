---
description: >-
  Fixes the Dart baseline: the SDK formatter and analyzer as failing gates with strict type modes and infos fatal, typed
  decoding at boundaries, handled futures and closed streams, failure and value shapes, and coverage scope.
when_to_use: >-
  Use when creating, configuring, or reviewing a Dart or Flutter project, or choosing its analysis options, failure
  shape, value classes, test clock, or coverage collection.
---

# Dart Standards

Canonical for Dart and Flutter application code, this standard holds the choices Dart and its SDK leave open; a Dart
programming skill defers here.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), [Pure Functions](../../../principles/pure-functions.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). The SDK constraint in `pubspec.yaml` and the
committed `pubspec.lock` follow [Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Format:** [`dart format --output=none --set-exit-if-changed .`](https://dart.dev/tools/dart-format).
- **Type check and lint:** [`dart analyze --fatal-infos`](https://dart.dev/tools/dart-analyze). Lint rules report as
  infos, so without `--fatal-infos` an enabled rule never fails: the advisory tier
  [Lint Strictness](../checks/lint-strictness.md) removes.
- **Analysis options:** a committed `analysis_options.yaml` includes a maintained rule set and sets `strict-casts`,
  `strict-inference`, and `strict-raw-types` under `analyzer: language:`
  ([analysis options](https://dart.dev/tools/analysis)). Example: `package:lints/recommended.yaml`, plus
  `unawaited_futures`.

An `// ignore:` comment names the rule and its reason on the same line.

## Type and Boundary Safety

Dart maps [Type and Boundary Safety](../code/type-and-boundary-safety.md) as follows:

- Strict modes stop `dynamic` silently reaching typed code. A signature never declares `dynamic`; an unknown-type value
  is `Object?`, checked before use ([design](https://dart.dev/effective-dart/design)).
- Decoded JSON and other external data become typed values on arrival, through a constructor checking each field's type
  (for example, by pattern match) that returns or throws a named failure; inner code never indexes a decoded map.
- A type is nullable only where absence means something to callers. `!` and `late` never silence the analyzer: `!`
  appears only where a check the compiler cannot see proves presence, and `late` only for a value a lifecycle step
  assigns before any read.

## Asynchrony

Every future is awaited, returned, or passed to `unawaited` with a comment naming why it may run on. Whoever creates a
stream controller closes it, and a listener cancels its subscription when its lifetime ends (in Flutter, in the owning
widget's `dispose`).

## Failures and Values

A `catch` names the type it handles with `on`, and code never catches `Error`, which marks a programming fault
([usage](https://dart.dev/effective-dart/usage)). Anything not reassigned is `final`, a constructor is `const` where
every field allows it, and a value class states its equality deliberately, since classes compare by identity by default.

## Tests

`package:test` runs the tests via `dart test` or, in Flutter, `flutter test`, with integration tests kept apart as
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md) requires. The unit layer reads no real clock: code
takes a clock as a parameter, and timers run under a fake clock. Example: package:fake_async.

Coverage follows [Meaningful Coverage](../testing/meaningful-coverage.md); the tooling reports lines by default,
functions and branches when asked; example: `coverage:test_with_coverage --branch-coverage`
([package:coverage](https://pub.dev/packages/coverage)). Generated sources are excluded with their reason, and any floor
above the minimum is recorded under
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Documentation

A public declaration carries a `///` doc comment opening with a one-sentence summary
([documentation](https://dart.dev/effective-dart/documentation)); a published package also enables
`public_member_api_docs`. A behaviour change updates the comments with the code, per
[Specification Maintenance](../evidence/specification-maintenance.md) and
[Public Contract](../architecture/public-contract.md).

## Adopter Decisions

| Decision          | Option                            | Gains                                       | Costs                                                                                 |
| ----------------- | --------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------- |
| expected failures | exceptions                        | the core libraries' idiom                   | signatures hide what can fail                                                         |
|                   | a sealed result hierarchy         | an exhaustive `switch` makes callers decide | every throwing library call needs wrapping                                            |
| value classes     | hand-written equality and copying | no build step                               | members drift from the fields                                                         |
|                   | generated, such as with freezed   | members track the fields                    | a code generator, weighed per [Dependency Selection](../code/dependency-selection.md) |

Record each choice once.

## Enforcement

An adopter's pull-request gate runs the format, analyze, and test gates. Review applies boundary decoding, the `!` and
`late` claims, future and stream ownership, and the coverage exclusions.
