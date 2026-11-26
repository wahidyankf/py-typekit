---
description: >-
  Fixes the Elixir baseline: warnings-as-errors format, compile, test-load, and lint gates; Dialyzer over typespecs;
  tagged-tuple failures; processes only for a runtime reason; line-only coverage.
when_to_use: >-
  Use when creating, configuring, or reviewing an Elixir project or choosing its static analysis, failure shape, process
  design, test isolation, or coverage.
---

# Elixir Standards

Canonical for Elixir, this settles what Elixir and Mix leave open; an Elixir programming skill defers here for each
rule.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), [Pure Functions](../../../principles/pure-functions.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). Version files and `mix.lock` follow
[Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Format:** `mix format --check-formatted`, reading a committed `.formatter.exs`.
- **Compile:** `mix compile --warnings-as-errors` ([docs](https://mix.hexdocs.pm/Mix.Tasks.Compile.Elixir.html)), also
  the type check, since the type checker reports through warnings.
- **Test load:** `mix test --warnings-as-errors`: a warning while loading the suite fails the run
  ([docs](https://mix.hexdocs.pm/Mix.Tasks.Test.html)).
- **Lint:** one linter at its strictest level, failing per [Lint Strictness](../checks/lint-strictness.md). Example:
  `mix credo --strict`.
- **Success typing:** Dialyzer over the declared typespecs, its persistent lookup table cached between runs. Example:
  dialyxir as a development-only dependency with `:unmatched_returns` and `:error_handling`.

A suppression, Dialyzer ignore entries included, states its reason where it applies.

## Type and Boundary Safety

Mapping [Type and Boundary Safety](../code/type-and-boundary-safety.md):

- The compiler infers types and warns on contradictions but does not yet read user-written signatures
  ([gradual types](https://elixir.hexdocs.pm/gradual-set-theoretic-types.html)), so it never checks a declared contract.
- Typespecs are that contract: every public function of a library, or of an application's boundary module, declares a
  `@spec`. The compiler ignores typespecs ([typespecs](https://elixir.hexdocs.pm/typespecs.html)), so a spec Dialyzer
  never analyses is documentation, not evidence.
- External data is cast and validated once, where it arrives, into a known shape (for example an Ecto changeset); no
  write bypasses that step.
- External input never becomes an atom, since atoms are never collected and the table is finite: convert with
  `String.to_existing_atom/1` against a known set, or keep the string.

## Failures

An actionable failure returns `{:ok, value}` or `{:error, reason}`, and a `with` chain's `else` matches every error
shape it produces; a defect raises. A function offering both forms names the tuple form `name` and the raising form
`name!`. `rescue` never drives control flow, and in a supervised process never hides an unexpected failure: the process
crashes and its supervisor restarts it from a known state.

Access is assertive: read a required key with `map.key` or a match, never `map[:key]` falling back to `nil`
([anti-patterns](https://elixir.hexdocs.pm/code-anti-patterns.html)).

## Processes

A process exists for changing state, concurrency, or failure isolation, never to organise code. A GenServer callback
stays thin, passing message and state to a pure function and returning its decision, per
[Functional Core, Imperative Shell](../architecture/functional-core-imperative-shell.md). Dynamic processes are named
through a registry `:via` tuple, never generated atoms. A supervisor's restart strategy follows its children's
dependencies.

## Tests

ExUnit is the framework. Integration tests carry a tag the test helper excludes from the unit run, per
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). A module is `async: true` only when it touches no
application environment, named process, shared file, or unsandboxed database; each database test runs in its own
sandboxed transaction. Doctests are unit tests.

`mix test --cover` measures lines only. Under [Meaningful Coverage](../testing/meaningful-coverage.md), generated
modules go under `:ignore_modules` with their reason, partitioned runs merge with `mix test.coverage` before judging,
and any floor above the minimum is recorded under
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Hermetic Unit Tests

A repository-owned Credo check bans impure calls in unit tests: a module using `Credo.Check`, loaded through `requires`
in `.credo.exs` and scoped by its `files: %{included: [...]}` parameter to unit-test paths, flags calls to `File`,
`System`, `Port`, `:os`, `:httpc`, `:gen_tcp`, `DateTime.utc_now`, and `:rand`. The check has its own tests, and
integration tests keep their excluded tag.

## Documentation

Each public module carries `@moduledoc` and each public function `@doc`, with examples as doctests so they stay true
([docs](https://elixir.hexdocs.pm/writing-documentation.html)). `@doc false` hides a detail from the reference but never
makes it private. A behaviour change updates these with the code, per
[Specification Maintenance](../evidence/specification-maintenance.md) and
[Public Contract](../architecture/public-contract.md).

## Enforcement

An adopter runs the five gates in its own pull-request gate. Review applies the boundary specs, failure and process
rules, test isolation, and coverage exclusions.
