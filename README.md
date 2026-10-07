# py-typekit

Typed functional primitives for Python, checked by strict pyright: a failure is a value the caller must handle, and an
absent value is one the type system tracks.

`v0.1.0` provides:

- `Result[T, E]` — `Ok[T] | Err[E]`, immutable and covariant, with the methods `map`, `map_err`, `flat_map`,
  `flat_map_err`, `tap`, and `tap_err`.
- `Option[T]` — `Some[T] | None`, with `from_optional` to build one from `T | None`.
- `attempt` — turns a raising call into a `Result` that names exactly the failures you expect.
- `pipe` — chains one to nine functions left to right, with curried combinators for `Result` and `Option` as its stages.

The package has no runtime dependencies, requires Python 3.14 only (`>=3.14,<3.15`), and ships `py.typed`. It is
imported as `typekit`.

## Status

`v0.1.0` is the first release. See [CHANGELOG.md](CHANGELOG.md) for what each tag holds.

## Install

Consume a release as a pinned Git dependency with [uv](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/wahidyankf/py-typekit --tag v0.1.0
```

uv records the tag under `[tool.uv.sources]` and pins the exact commit in `uv.lock`. Nothing is published to PyPI.

## Example

```python
from typing import assert_never

from typekit import Err, Ok, Result, attempt, pipe, result


def parse(text: str) -> Result[int, ValueError]:
    return attempt(lambda: int(text), ValueError)


def double(text: str) -> Result[str, ValueError]:
    return pipe(parse(text), result.map(lambda number: number * 2), result.map(str))


match double("21"):
    case Ok(value):
        print(value)
    case Err(error):
        print(error)
    case _ as unreachable:
        assert_never(unreachable)
```

Every `match` ends with `case _ as unreachable: assert_never(unreachable)`. When the cases above it cover every side,
`unreachable` is `Never` and the call type-checks; when one is missing, Pyright reports the call as an error, so a
forgotten `Err` or `None` fails the type check instead of slipping through at run time. The curried combinators are
reached through their modules, `from typekit import option, result`, so none shadows the builtin `map`.

## What Pyright catches

Three of the mistakes strict Pyright refuses, each with the rule and a trimmed message from a real run:

```python
from typing import assert_never

from typekit import Ok, Option, Result, attempt


def show(outcome: Result[int, str]) -> str:  # a match that forgets the failure side
    match outcome:
        case Ok(value):
            return f"ok {value}"
        case _ as unreachable:
            assert_never(unreachable)
            # Pyright error: Argument of type "Err[str]" cannot be assigned to parameter "arg" of type "Never"
            #   in function "assert_never" (reportArgumentType)


def read(found: Option[int]) -> int:  # an Option read as its value, None never handled
    return found.value
    # Pyright error: "value" is not a known attribute of "None" (reportOptionalMemberAccess)


def guarded() -> None:  # attempt with no exception type named
    attempt(lambda: 1)
    # Pyright error: Expected 1 more positional argument (reportCallIssue)
```

[What Pyright catches](docs/explanation/what-pyright-catches.md) shows all five, with the corrected code.

## Documentation

The full documentation lives in [`docs/`](docs/README.md), one kind of page per need:

- [Get started](docs/tutorials/get-started.md) — a first project, from install to an exhaustive match.
- [How-to guides](docs/how-to/README.md) — wrap exceptions, chain with `pipe`, handle an `Option`, match exhaustively,
  and pin the version.
- [Reference](docs/reference/README.md) — every public name, signature, and behaviour.
- [Explanation](docs/explanation/README.md) — why `Result` over exceptions, why `Option` has no methods, and the
  type-safety guarantees.

Every Python block in this README and in `docs/` is type-checked under strict Pyright by the `doc-snippets` gate.

## Development

Every gate runs from a plain terminal, each with one command:

```text
uv run pytest                          # tests, fast, no coverage
uv run --locked coverage run -m pytest && uv run --locked coverage report
uv run pyright
uv run ruff check && uv run ruff format --check
uv run --locked python scripts/check-doc-snippets.py   # every documented Python block type-checks as marked
npx --no-install prettier --check .
bash scripts/check-wheel.sh            # the wheel lists py.typed and declares no dependency
./rhino gate run --surface main        # everything before a pull request
```

`uv sync --locked` installs the Python dev dependencies, and `npm ci` installs the Markdown tooling and the git hooks;
Node is repository tooling only and never part of the library. The hooks and the hosted checks run the same gate
registry, `repo-config.yml`. Contribution rules, governance, and the agent setup are in [AGENTS.md](AGENTS.md).

## Related repositories

py-typekit is one of seven **`ose-projects`** repositories, with `hippo`, `ose-public`, `rhino`, `beaver-nest`,
`ose-rules`, and [`ose-private`](https://github.com/wahidyankf/ose-private) (Private). The label is navigation only:
each is versioned and released on its own. See [project context](docs/README.md#project-context) for each one's link and
relationship.

## License

[MIT](LICENSE)
