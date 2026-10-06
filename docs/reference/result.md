# `Result`, `Ok`, and `Err`

Module `typekit.result`. A fallible function returns `Result[T, E]`: an `Ok` holding its value or an `Err` holding its
fault.

## Types

```text
type Result[T, E] = Ok[T] | Err[E]

@final class Ok[T]:   Ok(value: T)    .value -> T    __match_args__ = ("value",)
@final class Err[E]:  Err(error: E)   .error -> E    __match_args__ = ("error",)
```

- **Immutable.** Every write or delete of any attribute, the private slot included, raises
  `dataclasses.FrozenInstanceError`, and Pyright refuses an assignment.
- **Covariant.** Each exposes its content only through a read-only property, so an `Ok[bool]` is accepted where an
  `Ok[int]` or a `Result[int, str]` is expected, and an `Err[bool]` where an `Err[int]` is.
- **Equality.** An `Ok` equals only an `Ok` with an equal value, and an `Err` only an `Err` with an equal fault; an `Ok`
  never equals an `Err` or a bare value.
- **Unhashable.** Each defines `__eq__` without `__hash__`, so `hash(Ok(1))` raises `TypeError: unhashable type: 'Ok'`,
  and neither can be a set element or a dict key.
- **`repr`.** `Ok(1)` prints as `Ok(1)`, `Err("bad")` as `Err('bad')`.
- **`match`.** `case Ok(value)` and `case Err(error)` bind the content positionally.
- Both classes are `@final`.

## Methods

Each method acts on its own side and returns the other side unchanged.

| Method               | On `Ok(value)`                         | On `Err(error)`                        |
| -------------------- | -------------------------------------- | -------------------------------------- |
| `map(transform)`     | `Ok(transform(value))`                 | itself                                 |
| `map_err(transform)` | itself                                 | `Err(transform(error))`                |
| `flat_map(step)`     | `step(value)`, a `Result`              | itself; `step` does not run            |
| `flat_map_err(step)` | itself; `step` does not run            | `step(error)`, a `Result`              |
| `tap(action)`        | itself, after `action(value)` ran once | itself; `action` does not run          |
| `tap_err(action)`    | itself; `action` does not run          | itself, after `action(error)` ran once |

Signatures, on `Ok[T]` and `Err[E]`:

```text
Ok.map[U](transform: Callable[[T], U]) -> Ok[U]
Ok.flat_map[U, F](step: Callable[[T], Result[U, F]]) -> Result[U, F]
Ok.tap(action: Callable[[T], object]) -> Ok[T]
Ok.map_err(transform: Callable[[Never], object]) -> Ok[T]
Ok.flat_map_err(step: Callable[[Never], object]) -> Ok[T]
Ok.tap_err(action: Callable[[Never], object]) -> Ok[T]

Err.map_err[F](transform: Callable[[E], F]) -> Err[F]
Err.flat_map_err[U, F](step: Callable[[E], Result[U, F]]) -> Result[U, F]
Err.tap_err(action: Callable[[E], object]) -> Err[E]
Err.map(transform: Callable[[Never], object]) -> Err[E]
Err.flat_map(step: Callable[[Never], object]) -> Err[E]
Err.tap(action: Callable[[Never], object]) -> Err[E]
```

On a `Result[T, E]`, which is either, a call therefore types as the union of both sides: `map` gives `Ok[U] | Err[E]`,
which is `Result[U, E]`.

## Curried combinators

For `typekit.pipeline.pipe`. Each takes the function first, positionally, and returns a stage from a `Result` to a
`Result` that calls the method of the same name. Import the module: `from typekit import result`.

```text
result.map[T, U, E](f: Callable[[T], U], /) -> Callable[[Result[T, E]], Result[U, E]]
result.map_err[T, E, F](f: Callable[[E], F], /) -> Callable[[Result[T, E]], Result[T, F]]
result.flat_map[T, U, E](f: Callable[[T], Result[U, E]], /) -> Callable[[Result[T, E]], Result[U, E]]
result.flat_map_err[T, E, F](f: Callable[[E], Result[T, F]], /) -> Callable[[Result[T, E]], Result[T, F]]
result.tap[T, E](f: Callable[[T], object], /) -> Callable[[Result[T, E]], Result[T, E]]
result.tap_err[T, E](f: Callable[[E], object], /) -> Callable[[Result[T, E]], Result[T, E]]
```

For any `Result` `r` and function `f`, `pipe(r, result.<name>(f))` equals `r.<name>(f)`, and `f` sees the same calls.
