# Get started with py-typekit

In this tutorial you add py-typekit to a new project, write a function that returns a `Result` instead of raising, and
handle both outcomes with a `match` that strict Pyright checks for completeness. Then you delete one case and watch
Pyright refuse the program. You need [uv](https://docs.astral.sh/uv/) and Python 3.14 only (`>=3.14,<3.15`).

## Create the project

Make a new application and add py-typekit at its first release:

```bash
uv init --app --python 3.14 greet-ages
cd greet-ages
uv add git+https://github.com/wahidyankf/py-typekit --tag v0.1.0
```

uv records the tag in `pyproject.toml` and the exact commit in `uv.lock`.

## Write a function that can fail

Create `main.py` in the project directory with this content:

```python
# pyright: strict
from typing import assert_never

from typekit import Err, Ok, Result


def parse_age(text: str) -> Result[int, str]:
    if not text.isdigit():
        return Err(f"{text!r} is not a whole number")
    return Ok(int(text))


for text in ["42", "forty-two"]:
    match parse_age(text):
        case Ok(age):
            print(f"age {age}")
        case Err(reason):
            print(f"rejected: {reason}")
        case _ as unreachable:
            assert_never(unreachable)
```

`parse_age` never raises. Its return type says it gives back either an `Ok` holding the age or an `Err` holding the
reason, and the caller takes the two apart with `match`. The first line turns on Pyright's strict mode for the file.

Run it:

```bash
uv run python main.py
```

```text
age 42
rejected: 'forty-two' is not a whole number
```

## Let Pyright check it

```bash
uv run --with pyright pyright --pythonversion 3.14 main.py
```

```text
0 errors, 0 warnings, 0 informations
```

The last case, `case _ as unreachable`, receives whatever the cases above it did not match. Both sides are handled, so
nothing is left: Pyright types `unreachable` as `Never`, and `assert_never` accepts it.

## Forget a case

Delete the two lines of the `case Err(reason):` branch and run Pyright again:

```bash
uv run --with pyright pyright --pythonversion 3.14 main.py
```

```text
  …/greet-ages/main.py:18:26 - error: Argument of type "Err[str]" cannot be assigned to parameter "arg" of type
  "Never" in function "assert_never"
    Type "Err[str]" is not assignable to type "Never" (reportArgumentType)
1 error, 0 warnings, 0 informations
```

The path is shortened and the long line wrapped to fit this page. An `Err` can now reach `assert_never`, so the program
no longer type-checks: a forgotten failure is caught before it runs, not when it happens. Put the two lines back.

## What you have now

A function whose failures are part of its type, and a caller Pyright holds to handling every one of them. From here:

- [Wrap a raising call with `attempt`](../how-to/wrap-exceptions-with-attempt.md) when the failure comes from code that
  raises.
- [Chain steps with `pipe`](../how-to/chain-with-pipe.md) when one result feeds the next.
- [What Pyright catches](../explanation/what-pyright-catches.md) for every mistake the types refuse.
