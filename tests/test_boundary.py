"""attempt: a raising call becomes a Result that names exactly the failures the caller expects (AC-45, AC-46)."""

from typing import Never

import pytest

from typekit.boundary import attempt
from typekit.result import Err, Ok, Result


def raising(error: BaseException) -> Never:
    """A call that always raises the exception it is given."""

    raise error


def fault_of[T, E](outcome: Result[T, E]) -> E:
    """The fault of an `Err`; an `Ok` fails the test."""

    match outcome:
        case Err(error):
            return error
        case Ok():
            pytest.fail(f"expected an Err, got {outcome!r}")


def test_attempt_returns_ok_with_the_value_of_a_call_that_returns() -> None:
    """A call that returns normally becomes `Ok` holding its value."""

    assert attempt(lambda: int("12"), ValueError) == Ok(12)


def test_attempt_runs_the_call_once_with_no_arguments() -> None:
    """The call is invoked exactly once, with nothing passed to it."""

    calls: list[str] = []

    def call() -> str:
        calls.append("called")
        return "done"

    assert attempt(call, ValueError) == Ok("done")
    assert calls == ["called"]


def test_attempt_returns_err_holding_the_very_exception_a_named_type_raised() -> None:
    """The fault is the exception object the call raised, not a copy or its message."""

    boom = ValueError("not a number")

    assert fault_of(attempt(lambda: raising(boom), ValueError)) is boom


def test_attempt_catches_any_of_several_named_types() -> None:
    """Every type named after the first widens what is caught, and the fault is the one raised."""

    lookup: dict[str, int] = {}

    fault = fault_of(attempt(lambda: lookup["k"], ValueError, KeyError))

    assert isinstance(fault, KeyError)
    assert fault.args == ("k",)


def test_attempt_catches_a_subclass_of_a_named_type() -> None:
    """A `UnicodeDecodeError` is a `ValueError`, so naming `ValueError` catches it."""

    fault = fault_of(attempt(lambda: b"\xff".decode("utf-8"), ValueError))

    assert isinstance(fault, UnicodeDecodeError)


def test_attempt_lets_an_exception_it_was_not_told_to_catch_propagate() -> None:
    """A `ValueError` is raised to the caller, not returned as an `Err`, when only `KeyError` is named."""

    with pytest.raises(ValueError, match="invalid literal"):
        attempt(lambda: int("x"), KeyError)


def test_attempt_never_catches_an_interrupt() -> None:
    """An exception outside `Exception`, such as an interrupt, ends the process however many types are named."""

    with pytest.raises(KeyboardInterrupt):
        attempt(lambda: raising(KeyboardInterrupt()), Exception)


def test_attempt_naming_no_type_is_refused_at_run_time() -> None:
    """Python itself raises `TypeError` for the missing argument, so the library carries no branch for it."""

    # The refusal this test proves: attempt has no default type and no catch-all, so naming none is an error.
    with pytest.raises(TypeError):
        attempt(lambda: 1)  # pyright: ignore[reportCallIssue]
