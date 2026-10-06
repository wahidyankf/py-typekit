# Reference

The complete public API of py-typekit `v0.1.0`, exact and in full. Each page describes one module's names.

## Public surface

`typekit.__all__` lists exactly ten names, and `from typekit import *` brings in only these:

- `Ok`, `Err`, `Result` — from `typekit.result`
- `Some`, `Option`, `from_optional` — from `typekit.option`
- `attempt` — from `typekit.boundary`
- `pipe` — from `typekit.pipeline`
- `result`, `option` — the modules themselves, which hold the curried combinators

The combinators are reached only through their modules, as `result.map(f)` or `option.map(f)`: a bare `map` would shadow
the builtin. The package declares no runtime dependency, requires Python 3.14 only (`>=3.14,<3.15`), and ships
`py.typed`. It defines no `__version__`; `importlib.metadata.version("py-typekit")` returns the installed version.

## Directory Map

- [`Result`, `Ok`, and `Err`](./result.md) — the success and failure types, their six methods, and the curried
  combinators of `typekit.result`.
- [`Option`, `Some`, and `from_optional`](./option.md) — the present-value type, the conversion from `T | None`, and the
  curried combinators of `typekit.option`.
- [`attempt`](./attempt.md) — the one place py-typekit catches an exception.
- [`pipe`](./pipe.md) — left-to-right function application with one to nine typed stages.
