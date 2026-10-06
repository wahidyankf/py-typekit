# `Option`, `Some`, and `from_optional`

Module `typekit.option`. A value that may be absent is an `Option[T]`: a `Some` holding it, or `None`.

## Types

```text
type Option[T] = Some[T] | None

@final class Some[T]:  Some(value: T)   .value -> T    __match_args__ = ("value",)
```

- **Absence is `None`.** There is no `Nothing` class; narrow with `is None` or `case None`.
- **Nested absence.** `Some(None)` is present and holds `None`; only `None` itself is absent.
- **`Some`** is built like `Ok`: immutable (every write or delete raises `dataclasses.FrozenInstanceError`), covariant,
  equal only to a `Some` with an equal value, printed as `Some(1)`, matched by `case Some(value)`, and `@final`.
- **Unhashable.** `Some` defines `__eq__` without `__hash__`, so `hash(Some(1))` raises
  `TypeError: unhashable type: 'Some'`, and a `Some` cannot be a set element or a dict key.
- **No methods.** `Option` has none, because Python cannot add them to `None`; it chains through `pipe` with the
  combinators below.

## `from_optional`

```text
from_optional[T](value: T | None, /) -> Option[T]
```

`None` stays `None`; any other value, a falsy one such as `0` or `""` included, becomes `Some(value)`.

## Curried combinators

For `typekit.pipeline.pipe`. Each acts on a `Some` and passes `None` through without calling its function. Import the
module: `from typekit import option`.

```text
option.map[T, U](f: Callable[[T], U], /) -> Callable[[Option[T]], Option[U]]
option.flat_map[T, U](f: Callable[[T], Option[U]], /) -> Callable[[Option[T]], Option[U]]
option.tap[T](f: Callable[[T], object], /) -> Callable[[Option[T]], Option[T]]
option.ok_or[T, E](error: E, /) -> Callable[[Option[T]], Result[T, E]]
```

| Stage                | On `Some(value)`                      | On `None` |
| -------------------- | ------------------------------------- | --------- |
| `option.map(f)`      | `Some(f(value))`                      | `None`    |
| `option.flat_map(f)` | `f(value)`, an `Option`               | `None`    |
| `option.tap(f)`      | the same `Some`, after `f(value)` ran | `None`    |
| `option.ok_or(e)`    | `Ok(value)`                           | `Err(e)`  |

`option.ok_or` is the one bridge from `Option` to `Result`.
