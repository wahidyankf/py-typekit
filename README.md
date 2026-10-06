# py-typekit

Typed functional primitives for Python, checked by strict pyright: a failure is a value the caller must handle, and an
absent value is one the type system tracks.

The first release, `v0.1.0`, is planned to provide:

- `Result[T, E]` — `Ok[T] | Err[E]`, immutable and covariant, with `map`, `map_err`, `flat_map`, `flat_map_err`,
  `tap`, and `tap_err`.
- `Option[T]` — `Some[T] | None`, with helpers to convert between it, plain `T | None`, and `Result`.

The package has no runtime dependencies and requires Python 3.14 or newer. It is imported as `typekit`.

## Status

Under construction: no release has been tagged yet.

## Install

Once `v0.1.0` is tagged, consume it as a pinned Git dependency with [uv](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/wahidyankf/py-typekit --tag v0.1.0
```

uv records the tag under `[tool.uv.sources]` and pins the exact commit in `uv.lock`.

## License

[MIT](LICENSE)
