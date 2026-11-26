"""Integration bindings for specs/behaviours/boundary.feature: attempt runs its call against real files."""

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenario, then, when

from typekit.boundary import attempt
from typekit.result import Err, Ok

EXCEPTION_TYPES: dict[str, type[Exception]] = {"ValueError": ValueError}


@dataclass
class World:
    """What the steps of one scenario share."""

    call: Callable[[], object] | None = None
    outcome: object = None
    raised: Exception | None = None


@pytest.fixture
def world() -> World:
    """A fresh world for each scenario."""

    return World()


@given(parsers.parse("a call that returns {value:d}"))
def call_returns(world: World, tmp_path: Path, value: int) -> None:
    """The call reads a real file of value bytes and returns how many bytes it read."""

    path = tmp_path / "payload.bin"
    path.write_bytes(b"\x00" * value)
    world.call = lambda: len(path.read_bytes())


@given(parsers.parse("a call that raises a {kind}"))
def call_raises(world: World, tmp_path: Path, kind: str) -> None:
    """The call reads a real file whose content makes the call raise the named type."""

    if kind == "ValueError":
        # Bytes that are not UTF-8 make read_text raise UnicodeDecodeError, which is a ValueError.
        path = tmp_path / "not-utf8.txt"
        path.write_bytes(b"\xff\xfe")
        world.call = lambda: path.read_text(encoding="utf-8")
    elif kind == "KeyError":
        # A JSON object without the key makes the lookup raise KeyError.
        path = tmp_path / "settings.json"
        path.write_text("{}", encoding="utf-8")
        world.call = lambda: json.loads(path.read_text(encoding="utf-8"))["missing"]
    else:
        pytest.fail(f"no real call in this binding raises a {kind}")


@when(parsers.parse("I attempt the call naming {kind}"))
def attempt_the_call(world: World, kind: str) -> None:
    """Run attempt on the call, naming the exception type, and keep any exception that escapes it."""

    assert world.call is not None, "a Given step must set the call first"
    try:
        world.outcome = attempt(world.call, EXCEPTION_TYPES[kind])
    except Exception as caught:
        world.raised = caught


@then(parsers.parse("the outcome is Ok holding {value:d}"))
def outcome_is_ok(world: World, value: int) -> None:
    """The outcome is an Ok holding the byte count the real read returned."""

    assert world.outcome == Ok(value)


@then("the outcome is an Err holding that ValueError")
def outcome_is_err_of_value_error(world: World) -> None:
    """The outcome is an Err holding the ValueError that the real call raised."""

    match world.outcome:
        case Err(error=ValueError()):
            return
        case _:
            pytest.fail(f"expected an Err holding a ValueError, got {world.outcome!r}")


@then("the call error propagates as a KeyError")
def call_error_propagates(world: World) -> None:
    """The KeyError that the real call raised was not caught, so it reached the caller."""

    assert isinstance(world.raised, KeyError)


# @scenario specs/behaviours/boundary.feature: attempt returns Ok when the call succeeds
@scenario("../../specs/behaviours/boundary.feature", "attempt returns Ok when the call succeeds")
def test_attempt_returns_ok_when_the_call_succeeds() -> None:
    """PT-B09: attempt returns Ok with the value of a real read that succeeds."""


# @scenario specs/behaviours/boundary.feature: attempt catches a named type and propagates any other
@scenario("../../specs/behaviours/boundary.feature", "attempt catches a named type and propagates any other")
def test_attempt_catches_a_named_type_and_propagates_any_other() -> None:
    """PT-B10: attempt returns Err for a real call that raises a named type; any other exception propagates."""
