# How to handle a value that may be absent

You have a value that may be missing, such as a dictionary lookup or an optional setting, and you want Pyright to make
every caller deal with the missing case.

## Build an `Option`

`Option[T]` is `Some[T] | None`. Wrap a present value in `Some`, or convert a `T | None` with `from_optional`, which
keeps `None` absent and wraps anything else, falsy values included:

```python
from typekit import Option, Some, from_optional


def find_port(settings: dict[str, int], name: str) -> Option[int]:
    return from_optional(settings.get(name))


def default_port() -> Option[int]:
    return Some(8080)
```

`from_optional(0)` is `Some(0)`, not `None`: only `None` means absent.

## Narrow it before you read it

An `Option` has no methods, so read its value only after ruling out `None`, with `is None` or a `match`:

```python
from typekit import Option


def port_or_default(found: Option[int]) -> int:
    if found is None:
        return 8080
    return found.value
```

Reading `found.value` before that check is a Pyright error; see
[What Pyright catches](../explanation/what-pyright-catches.md).

## Transform it with `pipe`

`option.map`, `option.flat_map`, and `option.tap` act on a present value and pass `None` through. `option.ok_or` turns
the `Option` into a `Result`, with the error you give for absence:

```python
from typekit import Option, Result, Some, option, pipe


def find_port(settings: dict[str, int], name: str) -> Option[int]:
    port = settings.get(name)
    return None if port is None else Some(port)


def privileged(port: int) -> Option[int]:
    return Some(port) if port < 1024 else None


def require_port(settings: dict[str, int], name: str) -> Result[str, str]:
    return pipe(
        find_port(settings, name),
        option.flat_map(privileged),
        option.map(lambda port: f"port {port}"),
        option.ok_or(f"no privileged port named {name!r}"),
    )
```

`require_port({"http": 80}, "http")` is `Ok("port 80")`, and `require_port({"dev": 3000}, "dev")` is
`Err("no privileged port named 'dev'")`. As with a `Result`, start the `pipe` from a typed function's return, so Pyright
can infer each stage.

To take an `Option` apart with every case handled, see [Match exhaustively](./match-exhaustively.md).
