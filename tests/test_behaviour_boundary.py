"""Behaviour bindings for specs/behaviours/boundary.feature: attempt catches only the named exception types."""

from collections.abc import Callable
from dataclasses import dataclass

import pytest
from pytest_bdd import given, parsers, scenario, then, when

from typekit.boundary import attempt
from typekit.result import Err, Ok

EXCEPTION_TYPES: dict[str, type[Exception]] = {"ValueError": ValueError, "KeyError": KeyError}


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
def call_returns(world: World, value: int) -> None:
    """The call returns the number."""

    world.call = lambda: value


@given(parsers.parse("a call that raises a {kind}"))
def call_raises(world: World, kind: str) -> None:
    """The call raises the named exception type, with the message bad."""

    error = EXCEPTION_TYPES[kind]("bad")

    def call() -> object:
        raise error

    world.call = call


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
    """The outcome is an Ok holding the value."""

    assert world.outcome == Ok(value)


@then("the outcome is an Err holding that ValueError")
def outcome_is_err_of_value_error(world: World) -> None:
    """The outcome is an Err holding the ValueError that was raised."""

    match world.outcome:
        case Err(error=ValueError(args=("bad",))):
            return
        case _:
            pytest.fail(f"expected an Err holding the ValueError, got {world.outcome!r}")


@then("the call error propagates as a KeyError")
def call_error_propagates(world: World) -> None:
    """The KeyError was not caught, so it reached the caller."""

    assert isinstance(world.raised, KeyError)


# @scenario specs/behaviours/boundary.feature: attempt returns Ok when the call succeeds
@scenario("../specs/behaviours/boundary.feature", "attempt returns Ok when the call succeeds")
def test_attempt_returns_ok_when_the_call_succeeds() -> None:
    """PT-B09: attempt returns Ok with the value when the call succeeds."""


# @scenario specs/behaviours/boundary.feature: attempt catches a named type and propagates any other
@scenario("../specs/behaviours/boundary.feature", "attempt catches a named type and propagates any other")
def test_attempt_catches_a_named_type_and_propagates_any_other() -> None:
    """PT-B10: attempt returns Err for a listed exception type; any other exception propagates."""
