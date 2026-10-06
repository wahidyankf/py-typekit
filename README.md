# py-typekit

Typed functional primitives for Python, checked by strict pyright: a failure is a value the caller must handle, and an
absent value is one the type system tracks.

`v0.1.0` provides:

- `Result[T, E]` — `Ok[T] | Err[E]`, immutable and covariant, with the methods `map`, `map_err`, `flat_map`,
  `flat_map_err`, `tap`, and `tap_err`.
- `Option[T]` — `Some[T] | None`, with `from_optional` to build one from `T | None`.
- `attempt` — turns a raising call into a `Result` that names exactly the failures you expect.
- `pipe` — chains one to nine functions left to right, with curried combinators for `Result` and `Option` as its stages.

The package has no runtime dependencies, requires Python 3.14 or newer, and ships `py.typed`. It is imported as
`typekit`.

## Status

`v0.1.0` is the first release. See [CHANGELOG.md](CHANGELOG.md) for what each tag holds.

## Install

Consume a release as a pinned Git dependency with [uv](https://docs.astral.sh/uv/):

```bash
uv add git+https://github.com/wahidyankf/py-typekit --tag v0.1.0
```

uv records the tag under `[tool.uv.sources]` and pins the exact commit in `uv.lock`. Nothing is published to PyPI.

## API

The package exports ten names, and no others:

- `Ok`, `Err`, `Result` — a success, a failure, and their union. Both sides refuse every write.
- `Some`, `Option`, `from_optional` — a present value, its union with `None`, and the conversion from `T | None`.
- `attempt(call, *errors)` — runs `call()` and returns `Ok(value)`, or `Err(caught)` when the call raises an instance of
  a named type. Any other exception propagates; naming no type is refused. Pyright infers the error type from the names,
  so `attempt(lambda: int(text), ValueError, TypeError)` is a `Result[int, ValueError | TypeError]`.
- `pipe(value, f1, ..., f9)` — applies the functions left to right and returns the last result.
- `result`, `option` — the modules holding the curried combinators: `result.map`, `result.map_err`, `result.flat_map`,
  `result.flat_map_err`, `result.tap`, `result.tap_err`, and `option.map`, `option.flat_map`, `option.tap`,
  `option.ok_or`.

Import the two modules, `from typekit import option, result`, never the combinators by name: `map` would shadow the
builtin, and one spelling per concept keeps `result.map(f)` and `option.map(f)` apart.

```python
from typing import assert_never

from typekit import Err, Ok, Option, Result, Some, attempt, option, pipe, result


def parse(text: str) -> Result[int, ValueError]:
    return attempt(lambda: int(text), ValueError)


def double(text: str) -> Result[str, ValueError]:
    return pipe(parse(text), result.map(lambda number: number * 2), result.map(str))


def label(found: Option[int]) -> Result[int, str]:
    return pipe(found, option.map(abs), option.ok_or("missing"))


def show(found: Option[int]) -> str:
    match found:
        case Some(value):
            return f"found {value}"
        case None:
            return "absent"
        case _ as unreachable:
            assert_never(unreachable)


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
forgotten `Err` or `None` fails the type check instead of slipping through at run time.

A `Result` also chains through its methods: `parse(text).map(abs).map_err(str)`. An `Option` has no methods, because
Python cannot add them to `None`, so it chains only through `pipe` and narrows with `match` or `is None`.

### What Pyright catches

Each mistake below is a type error under strict Pyright. The comment under it quotes the rule and a trimmed message from
a real run. `tests/test_typing.py` keeps every one of them as a refused line under `# pyright: ignore[<rule>]`, which
Pyright itself fails once the ignore is no longer needed, so this list cannot drift from what Pyright reports.

```python
from typing import assert_never

from typekit import Ok, Option, Result, Some, attempt, pipe


def to_text(number: int) -> str:
    return str(number)


def show(outcome: Result[int, str]) -> str:  # 1. a match that forgets the failure side
    match outcome:
        case Ok(value):
            return to_text(value)
        case _ as unreachable:
            assert_never(unreachable)
            # Pyright error: Argument of type "Err[str]" cannot be assigned to parameter "arg" of type "Never"
            #   in function "assert_never" (reportArgumentType)


def describe(found: Option[int]) -> str:  # 1. the same for an Option that forgets absence
    match found:
        case Some(value):
            return to_text(value)
        case _ as unreachable:
            assert_never(unreachable)
            # Pyright error: Argument of type "None" cannot be assigned to parameter "arg" of type "Never"
            #   in function "assert_never" (reportArgumentType)


def render(outcome: Result[int, str]) -> str:  # 2. a Result used as its value, never narrowed
    return to_text(outcome)
    # Pyright error: Argument of type "Result[int, str]" cannot be assigned to parameter "number" of type "int"
    #   ... "Err[str]" is not assignable to "int" (reportArgumentType)


def read(found: Option[int]) -> int:  # 3. an Option read as its value, None never handled
    return found.value
    # Pyright error: "value" is not a known attribute of "None" (reportOptionalMemberAccess)


def stages() -> str:  # 4. a pipe stage whose parameter does not match the value before it
    return pipe("text", to_text)
    # Pyright error: Argument of type "(number: int) -> str" cannot be assigned to parameter "f1" ...
    #   Parameter 1: type "str" is incompatible with type "int" (reportArgumentType)


def guarded() -> None:  # 5. attempt with no exception type named
    attempt(lambda: 1)
    # Pyright error: Expected 1 more positional argument (reportCallIssue)
```

Corrected, each one handles every case before it uses a value:

```python
from typing import assert_never

from typekit import Err, Ok, Option, Result, Some, attempt, pipe


def to_text(number: int) -> str:
    return str(number)


def show(outcome: Result[int, str]) -> str:
    match outcome:
        case Ok(value):
            return to_text(value)
        case Err(error):
            return error
        case _ as unreachable:
            assert_never(unreachable)


def describe(found: Option[int]) -> str:
    match found:
        case Some(value):
            return to_text(value)
        case None:
            return "absent"
        case _ as unreachable:
            assert_never(unreachable)


def read(found: Option[int]) -> int:
    return 0 if found is None else found.value


def stages() -> str:
    return pipe(2, to_text)


def guarded(text: str) -> Result[int, ValueError]:
    return attempt(lambda: int(text), ValueError)
```

### Typed input for `pipe`

Pyright solves each stage from the one before, so the input must carry its full type: a function parameter, a function's
return, or an annotation Pyright has not narrowed. A bare `Ok(2)`, or a local declared `Result[int, str]` but narrowed
to `Ok[int]` by its assignment, leaves the error type unsolved, which strict mode reports as partially unknown. Build
inputs through typed functions, as `parse` does above.

## Development

Every gate runs from a plain terminal, each with one command:

```text
uv run pytest                          # tests, fast, no coverage
uv run --locked coverage run -m pytest && uv run --locked coverage report
uv run pyright
uv run ruff check && uv run ruff format --check
npx --no-install prettier --check .
bash scripts/check-wheel.sh            # the wheel lists py.typed and declares no dependency
./rhino gate run --surface main        # everything before a pull request
```

`uv sync --locked` installs the Python dev dependencies, and `npm ci` installs the Markdown tooling and the git hooks;
Node is repository tooling only and never part of the library. The hooks and the hosted checks run the same gate
registry, `repo-config.yml`. Contribution rules, governance, and the agent setup are in [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE)
