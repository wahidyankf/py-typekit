# How to chain steps with `pipe`

You have several steps, some of which can fail, and you want each to run on what the previous one produced, stopping at
the first failure.

## Chain a `Result` with its methods

Every `Result` carries `map`, `map_err`, `flat_map`, `flat_map_err`, `tap`, and `tap_err`. Use `map` for a step that
cannot fail and `flat_map` for one that returns a `Result` of its own:

```python
from typekit import Err, Ok, Result, attempt


def parse(text: str) -> Result[int, str]:
    return attempt(lambda: int(text), ValueError).map_err(str)


def positive(number: int) -> Result[int, str]:
    return Ok(number) if number > 0 else Err(f"{number} is not positive")


def doubled_label(text: str) -> Result[str, str]:
    return parse(text).flat_map(positive).map(lambda number: number * 2).map(str)
```

An `Err` passes through every later step untouched, so `doubled_label("-3")` is `Err("-3 is not positive")` and
`doubled_label("21")` is `Ok("42")`.

## Chain with `pipe`

`pipe(value, f1, f2, ...)` is `f2(f1(value))` written in the order it runs, with one to nine functions. The modules
`typekit.result` and `typekit.option` hold curried versions of the combinators, each taking the function and returning a
stage for `pipe`. Import the modules, not the names:

```python
from typekit import Err, Ok, Result, attempt, pipe, result


def parse(text: str) -> Result[int, str]:
    return attempt(lambda: int(text), ValueError).map_err(str)


def positive(number: int) -> Result[int, str]:
    return Ok(number) if number > 0 else Err(f"{number} is not positive")


def doubled_label(text: str) -> Result[str, str]:
    return pipe(
        parse(text),
        result.flat_map(positive),
        result.map(lambda number: number * 2),
        result.tap(print),
        result.map(str),
    )
```

Both styles give the same result; pick the one that reads better. An `Option` has no methods, so it chains only through
`pipe` with `option.map`, `option.flat_map`, `option.tap`, and `option.ok_or`; see
[Handle a value that may be absent](./handle-an-option.md).

## Give `pipe` a fully typed input

Pyright solves each stage from the one before, so the first argument must carry its full type: a function parameter, a
function's return, or an annotation Pyright has not narrowed. A bare `Ok(2)`, or a local declared `Result[int, str]` but
narrowed to `Ok[int]` by its assignment, carries no error type. With a lambda stage, Pyright then cannot infer the
lambda's parameter, and strict mode reports the lambda and the result as partially unknown. With a named function stage,
strict mode reports nothing, but the result's error side stays an unsolved type variable, `Err[E@map]`, instead of
`Err[str]`. Start from a typed function, as `parse(text)` does above.

## Chain more than nine steps

Nest the call: `pipe(pipe(value, f1, ..., f9), f10)` keeps every type.
