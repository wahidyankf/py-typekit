# How to wrap a raising call with `attempt`

You call code that raises, such as `int()`, a dictionary lookup, or a library function, and you want its failure as a
value your caller must handle.

## Name the exceptions you expect

Pass `attempt` a function of no arguments and every exception type you expect. Pyright infers the error side from the
types you name:

```python
from functools import partial

from typekit import Result, attempt


def parse_port(text: str) -> Result[int, ValueError]:
    return attempt(lambda: int(text), ValueError)


def ratio(text: str, divisor: int) -> Result[int, ValueError | ZeroDivisionError]:
    return attempt(lambda: int(text) // divisor, ValueError, ZeroDivisionError)


def lookup(table: dict[str, int], key: str) -> Result[int, KeyError]:
    return attempt(partial(table.__getitem__, key), KeyError)
```

The call runs once, inside `attempt`. When it returns, you get `Ok` with its value. When it raises an instance of a
named type, a subclass included, you get `Err` holding that very exception object.

## Let everything else propagate

An exception of a type you did not name is not caught; it propagates out of `attempt` unchanged. There is no catch-all,
and `attempt` refuses to run with no type named, both as a Pyright error and as a `TypeError` at run time. Name only
what the caller can act on, so a bug still fails loudly.

## Replace an existing `except`

When `attempt` replaces a `try`/`except` block, it must catch every failure the old block caught.

- Name every exception type the `except` caught, not only the type the call documents. `json.loads` documents
  `json.JSONDecodeError`, a `ValueError`, but deeply nested input can also raise `RecursionError`. If the old block
  caught both, write `attempt(lambda: json.loads(text), ValueError, RecursionError)`. If you name fewer types, an input
  the old code handled now raises.
- Check callbacks that raise to stop the work early. A hook, such as a `json` `object_pairs_hook` that raises on a
  duplicate key, ends the call at the first problem, so a later failure in the same input never happens. If you change
  the hook to record the problem and continue, the call can now reach that later failure. Name that failure in `attempt`
  as well, or the input that used to fail in the hook now fails with a different exception.

## Bind arguments

The function takes no arguments. Bind them with a `lambda`, as `parse_port` does, or with `functools.partial`, as
`lookup` does.

## Use the result

Handle it like any other `Result`: [match on it exhaustively](./match-exhaustively.md), or keep going with
[`map` and `flat_map`](./chain-with-pipe.md). The error side is the exception itself, so `Err(error)` gives you its
message and type:

```python
from typing import assert_never

from typekit import Err, Ok, Result, attempt


def parse_port(text: str) -> Result[int, ValueError]:
    return attempt(lambda: int(text), ValueError)


match parse_port("80a"):
    case Ok(port):
        print(f"port {port}")
    case Err(error):
        print(f"not a port: {error}")
    case _ as unreachable:
        assert_never(unreachable)
```

See [`attempt` in the reference](../reference/attempt.md) for the full contract.
