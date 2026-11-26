---
description: >-
  Fixes the Python baseline: every signature annotated and checked by strict Pyright, format and lint gates, pathlib
  paths, validated boundaries, narrow exception handling, and branch coverage.
when_to_use: >-
  Use when creating, configuring, or reviewing a Python project, or choosing its type checker settings, lint rules,
  boundary validation, failure style, or coverage measurement.
---

# Python Standards

Canonical for Python, this standard fixes what the language and its tools leave open; a Python programming skill defers
here for each rule.

It implements the [explicitness](../../../principles/explicit-over-implicit.md),
[immutability](../../../principles/immutability.md), and [automation](../../../principles/automation-over-manual.md)
principles. The interpreter version and lockfile follow
[Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Type check:** strict Pyright over every authored package, in committed configuration with
  `reportUnnecessaryTypeIgnoreComment` enabled so a stale waiver is a finding
  ([configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)). A path outside strict mode is
  a waiver with its reason.
- **Format:** one formatter in check mode. Example: `ruff format --check`.
- **Lint:** a committed rule selection, sorting imports where the formatter does not and excluding rules the formatter
  documents as conflicting. Example: `ruff check` with the `I` rules
  ([formatter conflicts](https://docs.astral.sh/ruff/formatter/)).

Findings fail at the threshold [Lint Strictness](../checks/lint-strictness.md) sets.

## Type and Boundary Safety

Pyright is the checker under [Type and Boundary Safety](../code/type-and-boundary-safety.md). Python checks no
annotation at runtime, so an unannotated signature is an unverified contract. Therefore:

- Every parameter and every return is annotated.
- `Any` is never written: an unknown shape is `object`, narrowed before use; a structural need is a `Protocol`.
- `cast()`, `# type: ignore`, and `# pyright: ignore` are waivers, each with its reason beside it.
- Annotations use `X | None` and built-in generics. Parameters accept abstract types, returns are concrete, and no
  function returns a union its callers must untangle
  ([typing best practices](https://typing.python.org/en/latest/reference/best_practices.html)).
- An untyped dependency gets a stub rather than spreading unknown types inward.
- Annotating parsed input is not validating it: external data becomes a typed value through a check where it arrives.
- A filesystem path is a `pathlib.Path` from where it enters the program, never a hand-assembled string.

## Code Shape

- Comparisons to `None` use `is`, type checks use `isinstance`, a named function is a `def` rather than a bound lambda,
  and either every return in a function states a value or none does ([PEP 8](https://peps.python.org/pep-0008/)).
- A value object is a frozen dataclass. A list or dictionary default is built per instance through a factory, since a
  literal default is shared.
- A handler catches the narrowest exception type. A bare `except:`, which also catches interrupts, is never written; a
  deliberately ignored exception names its type and reason.

## Tests

Suites are separated by layer. A fixture creating a temporary directory or setting an environment variable crosses a
boundary the unit layer excludes, so a test using one is integration, per
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Example: pytest's `tmp_path` and
`monkeypatch.setenv`.

The unit run measures coverage with branches on. An untakeable partial branch is removed or restructured, never
exempted, per [Exclusions](../testing/meaningful-coverage/001-exclusions-and-exemptions.md). Example: coverage.py with
`branch = true` and `fail_under` ([branch coverage](https://coverage.readthedocs.io/en/latest/branch.html)). Any floor
above the minimum is recorded under
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Hermetic Unit Tests

The linter bans impure modules and calls in unit-test modules. Example: Ruff's `banned-api` rule (`TID251`, from
flake8-tidy-imports) lists `os.environ`, `subprocess`, `socket`, `urllib.request`, `time.time`, and `random` under
`lint.flake8-tidy-imports.banned-api`, and a negated `lint.per-file-ignores` pattern, `"!<unit-test glob>"`, ignores
`TID251` everywhere else.

## Documentation

Public modules, classes, and functions carry docstrings stating behaviour, not the types annotations already give. A
change to observable behaviour updates them per [Specification Maintenance](../evidence/specification-maintenance.md)
and [Public Contract](../architecture/public-contract.md).

## Adopter Decisions

| Decision            | Option                                  | Gains                                     | Costs                                                                     |
| ------------------- | --------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| boundary validation | standard-library dataclasses and checks | no dependency                             | hand-written validation and serialization                                 |
|                     | a library; example: Pydantic            | declared rules, parsing, serialization    | a dependency, per [Dependency Selection](../code/dependency-selection.md) |
| expected failures   | exceptions                              | the standard library's idiom              | signatures hide what can fail                                             |
|                     | returned result values                  | the checker forces every caller to handle | every raising library call needs wrapping                                 |

Record each choice in the repository adapter [Stack Packs](../../../conventions/structure/stack-packs.md) defines.

## Enforcement

Pyright, the formatter, the linter, and the coverage floor run in the adopter's own pull-request gate; review applies
boundary validation, code shape, and failure handling.
