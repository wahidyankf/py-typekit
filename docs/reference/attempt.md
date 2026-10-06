# `attempt`

Module `typekit.boundary`, exported as `typekit.attempt`. It turns a call that may raise into a `Result`.

## Signature

```text
attempt[T, E: Exception](call: Callable[[], T], error: type[E], /, *more: type[E]) -> Result[T, E]
```

## Behaviour

- Runs `call()` exactly once.
- Returns `Ok(value)` when the call returns `value`.
- Returns `Err(caught)` when the call raises an instance of `error` or of a type in `more`, a subclass included;
  `caught` is the exception object itself.
- Lets any other exception propagate unchanged. There is no default type and no catch-all.
- Requires at least one type: a call naming none is a Pyright error (`reportCallIssue`) and raises `TypeError` at run
  time.
- The bound is `Exception`, so Pyright refuses `KeyboardInterrupt`, `SystemExit`, and the other `BaseException`
  subclasses outside it, and an interrupt or an exit propagates.
- Pyright infers `E` as the union of the named types: `attempt(lambda: int(text), ValueError, TypeError)` is a
  `Result[int, ValueError | TypeError]`.

`call` takes no arguments; bind them with a `lambda` or `functools.partial`. `attempt` is the only `except` in the
package.
