# py-typekit

Typed functional primitives for Python, checked by strict pyright: a failure is a value the caller must handle, and an
absent value is one the type system tracks.

The first release, `v0.1.0`, is planned to provide:

- `Result[T, E]` — `Ok[T] | Err[E]`, immutable and covariant, with `map`, `map_err`, `flat_map`, `flat_map_err`, `tap`,
  and `tap_err`.
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

## Development

Every gate runs from a plain terminal, each with one command:

```text
uv run pytest                          # tests, fast, no coverage
uv run --locked coverage run -m pytest && uv run --locked coverage report
uv run pyright
uv run ruff check && uv run ruff format --check
npx --no-install prettier --check .
./rhino gate run --surface main        # everything before a pull request
```

`uv sync --locked` installs the Python dev dependencies, and `npm ci` installs the Markdown tooling and the git hooks;
Node is repository tooling only and never part of the library. The hooks and the hosted checks run the same gate
registry, `repo-config.yml`. Contribution rules, governance, and the agent setup are in [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE)
