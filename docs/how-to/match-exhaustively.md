# How to match exhaustively

You take a `Result` or an `Option` apart with `match`, and you want Pyright to reject the code if a case is ever
missing.

## End every match with `assert_never`

List one case per side, then a final `case _ as unreachable:` that passes its subject to `typing.assert_never`:

```python
from typing import assert_never

from typekit import Err, Ok, Option, Result, Some


def describe(outcome: Result[int, str]) -> str:
    match outcome:
        case Ok(value):
            return f"ok {value}"
        case Err(error):
            return f"failed: {error}"
        case _ as unreachable:
            assert_never(unreachable)


def show(found: Option[int]) -> str:
    match found:
        case Some(value):
            return f"found {value}"
        case None:
            return "absent"
        case _ as unreachable:
            assert_never(unreachable)
```

When the cases above cover every side, Pyright narrows `unreachable` to `Never`, and `assert_never` accepts it. When one
is missing, the leftover type reaches `assert_never` and Pyright reports `reportArgumentType` at that call:

```python
from typing import assert_never

from typekit import Ok, Result


def describe(outcome: Result[int, str]) -> str:
    match outcome:
        case Ok(value):
            return f"ok {value}"
        case _ as unreachable:
            assert_never(unreachable)
            # Pyright error: Argument of type "Err[str]" cannot be assigned to parameter "arg" of type "Never"
            #   in function "assert_never" (reportArgumentType)
```

`Ok`, `Err`, and `Some` each match their content positionally, so `case Ok(value)` binds the value and `case Err(error)`
the fault. Absence is the plain `None`, matched by `case None`.

## Prefer an early return for one side

When only one side needs special handling, an `isinstance` check reads more simply and Pyright narrows the rest:

```python
from typekit import Err, Result


def value_or_zero(outcome: Result[int, str]) -> int:
    if isinstance(outcome, Err):
        return 0
    return outcome.value
```

The same works for an `Option` with `if found is None: ...`. Use `match` with `assert_never` when every side matters, so
adding a case later cannot be forgotten silently.
