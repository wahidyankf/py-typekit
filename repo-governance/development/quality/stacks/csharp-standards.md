---
description: >-
  Fixes the C# on .NET baseline: nullable references, analyzers, warnings, and the formatter as failing gates, the
  long-term-support runtime line, shared build files, async and failure defaults, and C# domain and test shapes.
when_to_use: >-
  Use when creating, configuring, or reviewing a C# project on .NET, or when choosing its runtime line, analyzer
  settings, async and failure handling, or the shape of a C# domain type or test.
---

# C# Standards

This standard is canonical for C# on .NET, holding the choices C# and the SDK leave open; a C# skill defers here per
rule.

It implements [Automation Over Manual](../../../principles/automation-over-manual.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), and [Pure Functions](../../../principles/pure-functions.md). SDK
version files, toolchain pins, and lockfiles follow [Native-First Toolchain](../../workflow/native-first-toolchain.md)
and [Reproducibility](../../../principles/reproducibility.md).

## Gates

`Directory.Build.props` at the solution root switches every gate on once, so no project escapes one by omission.

- **Nullable reference types:** `<Nullable>enable</Nullable>`.
- **Analyzers:** the built-in .NET analyzers at a recommended analysis level, with `EnforceCodeStyleInBuild`, plus one
  further analyzer set the adopter records in the same file.
- **Warnings:** `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>` in every build configuration, per
  [Lint Strictness](../checks/lint-strictness.md); a warning enforced only in release builds passes every local run.
- **Formatting:** `dotnet format --verify-no-changes`, reading a committed `.editorconfig`.

A `#pragma warning disable`, a null-forgiving `!`, and `null!` are waivers, each beside a comment saying why it is safe.
A property that must be set is `required` or assigned in the constructor.

## Runtime Line

A new project targets the current .NET long-term-support release; an existing one stays on a supported long-term-support
release and upgrades before support ends. A short-term-support release is limited to experiments and internal tooling,
since a production service on one upgrades on the shorter cycle or runs unpatched. The adopter records release numbers
in its SDK version file.

## Build Defaults

- Projects are SDK-style only, with implicit usings enabled and any project-wide global usings in one file.
- NuGet Central Package Management is on: `Directory.Packages.props` declares each version once and project files
  reference packages without one, so projects cannot drift apart. The pin form follows
  [Dependency Bump Policy](../../workflow/dependency-bump-policy.md).
- Restore, build, test, and publish run through the `dotnet` command line, alike for contributors and pipeline.

## Language Defaults

- Data without identity, such as a request, result, or event, is a `record`; exposed collections are read-only
  interfaces.
- Namespaces are file-scoped and follow the folder path.
- A monetary amount is `decimal`, never `float` or `double`, whose binary fractions round. Domain and application code
  declares no `object` or `dynamic` and reads time through an injected time provider, so a test controls the clock.

## Asynchronous Code

- Nothing blocks on `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()`, which can deadlock, and only an event handler
  is `async void`.
- An asynchronous method's name ends in `Async` and it returns `Task` or `Task<T>`; `ValueTask` is only for a hot path
  where the method often completes synchronously.
- Library and infrastructure code awaits with `ConfigureAwait(false)`, since it cannot know its caller's synchronization
  context.
- A public asynchronous method accepts a `CancellationToken` and passes it to every input or output call, so work stops
  when its caller gives up; a cancellation exception is caught only at the outermost boundary.

## Failures

- An expected business failure is returned as a result value by default. A broken domain rule inside an aggregate may
  throw a domain exception instead; any other exception signals a broken invariant or infrastructure fault.
- Every application-defined exception type derives from one base type carrying a stable error code, so handlers map
  codes, not messages.
- Entry points guard arguments with the built-in throw helpers; input passes schema validation before business logic
  runs.
- A catch block rethrows, translates, or handles, never discards. A failure becomes a transport response once, per
  [Errors Cross Once](../architecture/hexagonal-architecture/001-layers-and-dependency-rule.md); an HTTP error response
  uses the standard problem-details shape.

## Modules

1. [Domain Types and Tests](csharp-standards/001-domain-types-and-tests.md)

## Enforcement

The compiler, analyzers, and formatter enforce the gates in the adopter's build and pull-request gate; an architecture
test holds the module's layer rule. Review applies the language, asynchronous, and failure defaults.
