# What Pyright catches

py-typekit's guarantee is that strict Pyright refuses a program that ignores a failure or an absence. This page shows
that guarantee instead of asserting it: five mistakes, each a type error, with the rule and message Pyright reports.

## The mistakes

Each comment under a mistake quotes the rule and a trimmed message from a real strict Pyright run. The `doc-snippets`
gate type-checks this block on every push and requires exactly these errors, and `tests/test_typing.py` keeps each one
as a refused line under `# pyright: ignore[<rule>]`, which Pyright fails once the ignore is no longer needed, so this
page cannot drift from what Pyright reports. The error comments read `# Pyright error:` because Pyright parses any
comment starting `# pyright:` as a directive.

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

## The corrected code

Each one handles every case before it uses a value:

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

## What the guarantees rest on

- **Exhaustive matches.** A `match` that ends with `case _ as unreachable: assert_never(unreachable)` type-checks only
  when every side is handled; see [Match exhaustively](../how-to/match-exhaustively.md).
- **No unnarrowed reads.** A `Result` is not its value and an `Option` may be `None`, so neither reaches code expecting
  the value until a `match`, an `isinstance`, or an `is None` check has narrowed it.
- **Typed stages.** `pipe` types each stage from the one before, so a mismatch is reported at the stage, not at run
  time; see [`pipe`](../reference/pipe.md).
- **Named failures.** `attempt` requires the exception types it converts, so the error side of its `Result` is exactly
  their union; see [`attempt`](../reference/attempt.md).

These hold under strict Pyright. In basic mode some of them, such as the partially unknown types `pipe` reports for an
untyped input, are not checked, so a consumer gets the full guarantee with `typeCheckingMode = "strict"`.
