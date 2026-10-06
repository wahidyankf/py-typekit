"""Result: each combinator acts on its own side and hands the other back unchanged (AC-01, AC-02, AC-03, AC-51)."""

from collections.abc import Callable
from dataclasses import FrozenInstanceError

import pytest

from typekit import result
from typekit.pipeline import pipe
from typekit.result import Err, Ok, Result


def check_positive(number: int) -> Result[int, str]:
    """A number above zero, or a fault naming it."""

    return Ok(number) if number > 0 else Err(f"{number} is not positive")


def test_map_and_map_err_change_only_their_own_side() -> None:
    """`map` transforms a value and passes a fault on; `map_err` transforms a fault and passes a value on."""

    assert Ok(2).map(lambda number: number * 10) == Ok(20)
    assert Err("bad").map(lambda number: number * 10) == Err("bad")
    assert Err("bad").map_err(len) == Err(3)
    assert Ok(2).map_err(len) == Ok(2)


def test_flat_map_and_flat_map_err_continue_with_a_fallible_step() -> None:
    """`flat_map` runs the next fallible step on a value and skips it on a fault; `flat_map_err` recovers a fault."""

    assert Ok(2).flat_map(check_positive) == Ok(2)
    assert Ok(-1).flat_map(check_positive) == Err("-1 is not positive")
    assert Err("bad").flat_map(check_positive) == Err("bad")
    assert Err("bad").flat_map_err(lambda fault: check_positive(len(fault))) == Ok(3)
    assert Ok(2).flat_map_err(lambda fault: check_positive(len(fault))) == Ok(2)


def test_tap_and_tap_err_see_their_own_side_and_pass_the_result_on() -> None:
    """`tap` shows a value to its action and `tap_err` a fault to its own; each returns the result unchanged, and
    neither action runs on the other side."""

    seen_values: list[object] = []

    assert Ok(2).tap(seen_values.append) == Ok(2)
    assert Err("bad").tap(seen_values.append) == Err("bad")
    assert Err("bad").tap_err(seen_values.append) == Err("bad")
    assert Ok(2).tap_err(seen_values.append) == Ok(2)
    assert seen_values == [2, "bad"]


def test_ok_and_err_expose_their_content_and_narrow_under_match() -> None:
    """The read-only properties hold the content, and `match` takes each side apart through its match arguments."""

    def describe(result: Result[int, str]) -> str:
        match result:
            case Ok(value):
                return f"ok {value}"
            case Err(error):
                return f"err {error}"

    assert (Ok(3).value, Err("bad").error) == (3, "bad")
    assert (describe(Ok(3)), describe(Err("bad"))) == ("ok 3", "err bad")


def test_ok_and_err_compare_by_side_and_content() -> None:
    """An `Ok` equals only an `Ok` of an equal value, an `Err` only an `Err` of an equal fault; each prints its side."""

    assert Ok(1) == Ok(1)
    assert Err("bad") == Err("bad")
    assert Ok(1) != Err(1)
    assert Err(1) != Ok(1)
    assert Ok(1) != Ok(2)
    assert Err(1) != Err(2)
    assert Ok(1) != 1
    assert (repr(Ok(1)), repr(Err("bad"))) == ("Ok(1)", "Err('bad')")


@pytest.mark.parametrize("subject", [Ok(1), Err("bad")])
@pytest.mark.parametrize("name", ["value", "error", "_value", "_error", "extra"])
def test_ok_and_err_refuse_every_write_and_delete(subject: Result[int, str], name: str) -> None:
    """Neither side can be changed once made, not even through its private slot, as a frozen dataclass cannot."""

    with pytest.raises(FrozenInstanceError):
        setattr(subject, name, 2)

    with pytest.raises(FrozenInstanceError):
        delattr(subject, name)

    assert subject in (Ok(1), Err("bad"))


def ok_two() -> Result[int, str]:
    """`Ok(2)` typed as the whole `Result`, because `pipe` needs its input's full type to infer each stage."""

    return Ok(2)


def err_bad() -> Result[int, str]:
    """`Err("bad")` typed as the whole `Result`, for the same reason."""

    return Err("bad")


SUBJECTS = [pytest.param(ok_two(), id="ok"), pytest.param(err_bad(), id="err")]


def add_ten(number: int) -> int:
    """The number plus ten."""

    return number + 10


def length(text: str) -> int:
    """The length of the text."""

    return len(text)


def recover(fault: str) -> Result[int, str]:
    """A fallible recovery: the fault's length, when that is above zero."""

    return check_positive(len(fault))


def recording[T, U](calls: list[object], function: Callable[[T], U]) -> Callable[[T], U]:
    """`function`, but each argument it receives is first appended to `calls`."""

    def record(argument: T) -> U:
        calls.append(argument)
        return function(argument)

    return record


@pytest.mark.parametrize("subject", SUBJECTS)
def test_curried_map_equals_the_map_method(subject: Result[int, str]) -> None:
    """`pipe(subject, result.map(f))` equals `subject.map(f)`, and `f` sees the same calls."""

    piped_calls: list[object] = []
    method_calls: list[object] = []

    piped = pipe(subject, result.map(recording(piped_calls, add_ten)))
    method = subject.map(recording(method_calls, add_ten))

    assert piped == method
    assert piped_calls == method_calls


@pytest.mark.parametrize("subject", SUBJECTS)
def test_curried_map_err_equals_the_map_err_method(subject: Result[int, str]) -> None:
    """`pipe(subject, result.map_err(f))` equals `subject.map_err(f)`, and `f` sees the same calls."""

    piped_calls: list[object] = []
    method_calls: list[object] = []

    piped = pipe(subject, result.map_err(recording(piped_calls, length)))
    method = subject.map_err(recording(method_calls, length))

    assert piped == method
    assert piped_calls == method_calls


@pytest.mark.parametrize("subject", SUBJECTS)
def test_curried_flat_map_equals_the_flat_map_method(subject: Result[int, str]) -> None:
    """`pipe(subject, result.flat_map(f))` equals `subject.flat_map(f)`, and `f` sees the same calls."""

    piped_calls: list[object] = []
    method_calls: list[object] = []

    piped = pipe(subject, result.flat_map(recording(piped_calls, check_positive)))
    method = subject.flat_map(recording(method_calls, check_positive))

    assert piped == method
    assert piped_calls == method_calls


@pytest.mark.parametrize("subject", SUBJECTS)
def test_curried_flat_map_err_equals_the_flat_map_err_method(subject: Result[int, str]) -> None:
    """`pipe(subject, result.flat_map_err(f))` equals `subject.flat_map_err(f)`, and `f` sees the same calls."""

    piped_calls: list[object] = []
    method_calls: list[object] = []

    piped = pipe(subject, result.flat_map_err(recording(piped_calls, recover)))
    method = subject.flat_map_err(recording(method_calls, recover))

    assert piped == method
    assert piped_calls == method_calls


@pytest.mark.parametrize("subject", SUBJECTS)
def test_curried_tap_equals_the_tap_method(subject: Result[int, str]) -> None:
    """`pipe(subject, result.tap(f))` equals `subject.tap(f)`, and `f` sees the same calls."""

    piped_calls: list[object] = []
    method_calls: list[object] = []

    piped = pipe(subject, result.tap(piped_calls.append))
    method = subject.tap(method_calls.append)

    assert piped == method
    assert piped_calls == method_calls


@pytest.mark.parametrize("subject", SUBJECTS)
def test_curried_tap_err_equals_the_tap_err_method(subject: Result[int, str]) -> None:
    """`pipe(subject, result.tap_err(f))` equals `subject.tap_err(f)`, and `f` sees the same calls."""

    piped_calls: list[object] = []
    method_calls: list[object] = []

    piped = pipe(subject, result.tap_err(piped_calls.append))
    method = subject.tap_err(method_calls.append)

    assert piped == method
    assert piped_calls == method_calls
