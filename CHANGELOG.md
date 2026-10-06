# Changelog

All notable changes to py-typekit are recorded here. This project follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html), and a released tag is immutable: it is never moved or
replaced, and a defect becomes the next version.

Entries describe what a consumer can observe: names, signatures, types, and behaviour. They are not a commit list.

## [v0.1.0] - 2026-10-06

The first release: a zero-dependency, strictly typed library for Python 3.14 only (`>=3.14,<3.15`), imported as
`typekit`, consumed as a pinned uv Git-tag dependency.

### Added

- `Result[T, E]`, the union `Ok[T] | Err[E]`. Both sides are immutable and covariant, so an `Ok[bool]` is accepted where
  a `Result[int, str]` is expected. The methods `map`, `map_err`, `flat_map`, `flat_map_err`, `tap`, and `tap_err` each
  act on their own side and return the other unchanged. Ported from the account-ledger library.
- `Option[T]`, the union `Some[T] | None`, with `from_optional` to build one from `T | None`. `Some(None)` is present
  and holds `None`; `None` is absent. `Option` has no methods: it chains through `pipe`.
- `attempt(call, *errors)`, which turns a raising call into a `Result`: `Ok` with the call's value, or `Err` holding
  the exception raised when it is an instance of a named type. Any other exception propagates, there is no catch-all,
  and naming no type is a type error.
- `pipe(value, f1, ..., f9)`, which applies one to nine functions left to right, each typed from the one before, so a
  mismatched stage is a type error at the stage.
- Curried combinators for `pipe` stages: `typekit.result.map`, `map_err`, `flat_map`, `flat_map_err`, `tap`, and
  `tap_err`, and `typekit.option.map`, `flat_map`, `tap`, and `ok_or`, the one bridge from `Option` to `Result`. Import
  the modules, `from typekit import option, result`, because a bare `map` would shadow the builtin.
- A typed package: the wheel ships `py.typed`, and the public surface is exactly the ten names `Ok`, `Err`, `Result`,
  `Some`, `Option`, `from_optional`, `attempt`, `pipe`, `result`, and `option`.
