"""Option: absence is `None`, presence is `Some`, and the curried combinators act on `Some` (AC-05, AC-06, AC-52)."""

from dataclasses import FrozenInstanceError

import pytest

from typekit import option
from typekit.option import Option, Some, from_optional
from typekit.pipeline import pipe
from typekit.result import Err, Ok


def some_two() -> Option[int]:
    """`Some(2)` typed as the whole `Option`, because `pipe` needs its input's full type to infer each stage."""

    return Some(2)


def nothing() -> Option[int]:
    """Absence typed as the whole `Option`, for the same reason."""

    return None


def times_ten(number: int) -> int:
    """The number times ten."""

    return number * 10


def to_nothing(number: int) -> Option[int]:
    """A step that always finds nothing."""

    return None


def successor(number: int) -> Option[int]:
    """The next number, present."""

    return Some(number + 1)


def test_from_optional_keeps_none_absent_and_wraps_anything_else() -> None:
    """`None` stays `None`; any other value, falsy ones included, becomes `Some`."""

    assert from_optional(5) == Some(5)
    assert from_optional(0) == Some(0)
    assert from_optional(None) is None


def test_some_none_is_present_and_none_is_absent() -> None:
    """A `Some` holding `None` is present, which is why `Option` is not just `T | None`."""

    nested = Some(None)

    assert nested is not None
    assert nested.value is None


def test_some_exposes_its_value_and_narrows_under_match() -> None:
    """The read-only `value` property holds the content, and `match` takes a `Some` apart or sees `None`."""

    def describe(subject: Option[int]) -> str:
        match subject:
            case Some(value):
                return f"some {value}"
            case None:
                return "none"

    assert Some(3).value == 3
    assert (describe(Some(3)), describe(None)) == ("some 3", "none")


def test_some_compares_by_content_and_prints_its_side() -> None:
    """A `Some` equals only a `Some` of an equal value, never the bare value or `None`; it prints as `Some(...)`."""

    assert Some(1) == Some(1)
    assert Some(1) != Some(2)
    assert Some(1) != 1
    assert Some(None) is not None
    assert repr(Some(1)) == "Some(1)"


@pytest.mark.parametrize("name", ["value", "_value", "extra"])
def test_some_refuses_every_write_and_delete(name: str) -> None:
    """A `Some` cannot be changed once made, not even through its private slot, as `Ok` cannot."""

    subject = Some(1)

    with pytest.raises(FrozenInstanceError):
        setattr(subject, name, 2)

    with pytest.raises(FrozenInstanceError):
        delattr(subject, name)

    assert subject == Some(1)


def test_ok_or_turns_some_into_ok_and_none_into_err() -> None:
    """`option.ok_or(error)` is the one bridge to `Result`: presence is a success, absence is the given fault."""

    assert pipe(Some(5), option.ok_or("missing")) == Ok(5)
    assert pipe(nothing(), option.ok_or("missing")) == Err("missing")


def test_map_acts_on_some_and_passes_none_through() -> None:
    """`option.map(f)` transforms a present value and leaves absence absent."""

    assert pipe(some_two(), option.map(times_ten)) == Some(20)
    assert pipe(nothing(), option.map(times_ten)) is None


def test_flat_map_continues_with_a_step_that_may_find_nothing() -> None:
    """`option.flat_map(f)` runs a step on a present value, whose own absence or presence is the outcome."""

    assert pipe(some_two(), option.flat_map(to_nothing)) is None
    assert pipe(some_two(), option.flat_map(successor)) == Some(3)
    assert pipe(nothing(), option.flat_map(successor)) is None


def test_tap_sees_a_present_value_and_passes_the_option_on() -> None:
    """`option.tap(f)` shows a present value to `f` and returns the option unchanged; absence never calls it."""

    seen: list[object] = []

    assert pipe(some_two(), option.tap(seen.append)) == Some(2)
    assert pipe(nothing(), option.tap(seen.append)) is None
    assert seen == [2]
