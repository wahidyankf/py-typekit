"""Typing contracts: what strict Pyright accepts and refuses about typekit (AC-04, AC-07, AC-47, AC-48, AC-50, AC-53).

Pyright is the judge of this module and `reportUnnecessaryTypeIgnoreComment` is on, so an ignore comment that stops
being needed is itself a finding. Pytest imports the module, so its runtime statements are measured too.
"""

from typekit import option, result
from typekit.boundary import attempt
from typekit.option import Option, Some
from typekit.pipeline import pipe
from typekit.result import Err, Ok, Result


def accept_value_side(subject: Result[int, str]) -> Result[int, str]:
    """A `Result[int, str]`, handed back, to prove what the checker lets a caller pass in."""

    return subject


def accept_fault_side(subject: Result[str, int]) -> Result[str, int]:
    """A `Result[str, int]`, handed back, to prove covariance of the fault side."""

    return subject


def test_ok_and_err_are_covariant() -> None:
    """An `Ok[bool]` is accepted where a `Result[int, str]` is expected, as is an `Err[bool]` for `Err[int]`."""

    flag_ok: Ok[bool] = Ok(True)
    flag_err: Err[bool] = Err(False)

    assert accept_value_side(flag_ok) == Ok(True)
    assert accept_fault_side(flag_err) == Err(False)


def to_text(number: int) -> str:
    """The number as text."""

    return str(number)


def size(text: str) -> int:
    """The length of the text."""

    return len(text)


def test_pipe_types_every_arity_from_one_to_nine() -> None:
    """Each arity's result is assigned to its expected type: text after an odd count of stages, a number after even."""

    one: str = pipe(1, to_text)
    two: int = pipe(1, to_text, size)
    three: str = pipe(1, to_text, size, to_text)
    four: int = pipe(1, to_text, size, to_text, size)
    five: str = pipe(1, to_text, size, to_text, size, to_text)
    six: int = pipe(1, to_text, size, to_text, size, to_text, size)
    seven: str = pipe(1, to_text, size, to_text, size, to_text, size, to_text)
    eight: int = pipe(1, to_text, size, to_text, size, to_text, size, to_text, size)
    nine: str = pipe(1, to_text, size, to_text, size, to_text, size, to_text, size, to_text)

    assert (one, two, three, four, five, six, seven, eight, nine) == ("1", 1, "1", 1, "1", 1, "1", 1, "1")


def mismatched_stage() -> str:
    """Never called: `to_text` takes a number, so a text value passed to it is a type error."""

    # The refusal this test proves: the stage's parameter type does not match the value piped into it.
    return pipe("text", to_text)  # pyright: ignore[reportArgumentType]


def adjust_result(subject: Result[int, str]) -> Result[int, int]:
    """Curried `Result` combinators in a pipe: Pyright infers each stage from the typed parameter."""

    return pipe(subject, result.map(lambda number: number + 1), result.map_err(len))


def test_pipe_infers_curried_result_combinators_from_a_typed_input() -> None:
    """The lambda's `number` is an `int` and `len` takes the fault, so the pipe is a `Result[int, int]`."""

    adjusted_ok: Result[int, int] = adjust_result(Ok(1))
    adjusted_err: Result[int, int] = adjust_result(Err("bad"))

    assert (adjusted_ok, adjusted_err) == (Ok(2), Err(3))


def read_without_narrowing(subject: Option[int]) -> int:
    """Never called: an `Option[int]` may be `None`, so reading `.value` from it without narrowing is a type error."""

    # The refusal this test proves: Option has no methods or attributes of its own, so access needs narrowing first.
    return subject.value  # pyright: ignore[reportOptionalMemberAccess]


def double_or_report(subject: Option[int]) -> Result[int, str]:
    """Curried `Option` combinators in a pipe: Pyright infers each stage from the typed parameter."""

    return pipe(subject, option.map(lambda number: number * 2), option.ok_or("missing"))


def test_pipe_infers_curried_option_combinators_from_a_typed_input() -> None:
    """The lambda's `number` is an `int`, and `ok_or` bridges to a `Result[int, str]`."""

    present: Result[int, str] = double_or_report(Some(2))
    absent: Result[int, str] = double_or_report(None)

    assert (present, absent) == (Ok(4), Err("missing"))


def test_attempt_infers_the_error_type_from_the_named_types() -> None:
    """Naming `ValueError` and `TypeError` types the fault side as exactly their union."""

    outcome: Result[int, ValueError | TypeError] = attempt(lambda: int("1"), ValueError, TypeError)

    assert outcome == Ok(1)


def unnamed_error() -> None:
    """Never called: `attempt` takes at least one error type, so a call that names none is a type error."""

    # The refusal this test proves: attempt has no default error type and no catch-all, so naming none is refused.
    attempt(lambda: 1)  # pyright: ignore[reportCallIssue]
