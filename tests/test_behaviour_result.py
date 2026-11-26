"""Behaviour bindings for specs/behaviours/result.feature: each Result combinator acts on its own side."""

from dataclasses import dataclass, field

import pytest
from pytest_bdd import given, parsers, scenario, then, when

from typekit import result
from typekit.result import Err, Ok, Result


@dataclass
class World:
    """What the steps of one scenario share."""

    subject: Result[int, str] | None = None
    outcome: object = None
    seen: list[object] = field(default_factory=list[object])


@pytest.fixture
def world() -> World:
    """A fresh world for each scenario."""

    return World()


def subject_of(world: World) -> Result[int, str]:
    """The subject that a Given step set."""

    assert world.subject is not None, "a Given step must set the subject first"

    return world.subject


def add_one(number: int) -> int:
    """The number plus one."""

    return number + 1


def add_exclamation_mark(text: str) -> str:
    """The text with an exclamation mark added."""

    return text + "!"


def double_into_ok(number: int) -> Result[int, str]:
    """The number doubled, as a success."""

    return Ok(number * 2)


def recover_as_ok_zero(fault: str) -> Result[int, str]:
    """Any fault recovered as the success 0."""

    return Ok(0)


@given(parsers.parse("an Ok holding {value:d}"))
def ok_holding(world: World, value: int) -> None:
    """Set the subject to an Ok with the value."""

    world.subject = Ok(value)
    world.seen = []


@given(parsers.parse('an Err holding "{text}"'))
def err_holding(world: World, text: str) -> None:
    """Set the subject to an Err with the fault."""

    world.subject = Err(text)
    world.seen = []


@when("I map it with a function that adds 1")
def map_add_one(world: World) -> None:
    """Map the subject with a function that adds one."""

    world.outcome = subject_of(world).map(add_one)


@when("I flat map it with a step that doubles the value into an Ok")
def flat_map_double(world: World) -> None:
    """Flat map the subject with a step that doubles the value into an Ok."""

    world.outcome = subject_of(world).flat_map(double_into_ok)


@when("I tap it with a recording action")
def tap_with_recorder(world: World) -> None:
    """Tap the subject's value with an action that records it."""

    world.outcome = subject_of(world).tap(world.seen.append)


@when("I tap its fault with a recording action")
def tap_err_with_recorder(world: World) -> None:
    """Tap the subject's fault with an action that records it."""

    world.outcome = subject_of(world).tap_err(world.seen.append)


@when("I apply result map err with a function that adds an exclamation mark")
def apply_result_map_err(world: World) -> None:
    """Apply the curried result.map_err to the subject."""

    world.outcome = result.map_err(add_exclamation_mark)(subject_of(world))


@when("I apply result flat map err with a step that recovers as Ok 0")
def apply_result_flat_map_err(world: World) -> None:
    """Apply the curried result.flat_map_err to the subject."""

    world.outcome = result.flat_map_err(recover_as_ok_zero)(subject_of(world))


@when("I apply result tap err with a recording action")
def apply_result_tap_err(world: World) -> None:
    """Apply the curried result.tap_err to the subject, recording the fault."""

    world.outcome = result.tap_err(world.seen.append)(subject_of(world))


@then(parsers.parse("the outcome is Ok holding {value:d}"))
def outcome_is_ok(world: World, value: int) -> None:
    """The outcome is an Ok holding the value."""

    assert world.outcome == Ok(value)


@then(parsers.parse('the outcome is Err holding "{text}"'))
def outcome_is_err(world: World, text: str) -> None:
    """The outcome is an Err holding the fault."""

    assert world.outcome == Err(text)


@then(parsers.parse("the action saw {value:d}"))
def action_saw_number(world: World, value: int) -> None:
    """The action was called once, with the number."""

    assert world.seen == [value]


@then(parsers.parse('the action saw "{text}"'))
def action_saw_text(world: World, text: str) -> None:
    """The action was called once, with the text."""

    assert world.seen == [text]


@then("the action saw nothing")
def action_saw_nothing(world: World) -> None:
    """The action was never called."""

    assert world.seen == []


# @scenario specs/behaviours/result.feature: Ok maps its value
@scenario("../specs/behaviours/result.feature", "Ok maps its value")
def test_ok_maps_its_value() -> None:
    """PT-B01: Ok.map applies the function and keeps the Ok."""


# @scenario specs/behaviours/result.feature: Err map leaves its error unchanged
@scenario("../specs/behaviours/result.feature", "Err map leaves its error unchanged")
def test_err_map_leaves_its_error_unchanged() -> None:
    """PT-B02: Err.map leaves the error unchanged."""


# @scenario specs/behaviours/result.feature: Flat map chains an Ok and keeps an Err
@scenario("../specs/behaviours/result.feature", "Flat map chains an Ok and keeps an Err")
def test_flat_map_chains_an_ok_and_keeps_an_err() -> None:
    """PT-B03: Ok.flat_map chains a second Result, and Err.flat_map keeps the error."""


# @scenario specs/behaviours/result.feature: Tap and tap err see their own side
@scenario("../specs/behaviours/result.feature", "Tap and tap err see their own side")
def test_tap_and_tap_err_see_their_own_side() -> None:
    """PT-B04: Ok.tap runs an action and keeps the value; Err.tap_err runs on the error and keeps it."""


# @scenario specs/behaviours/result.feature: Curried functions transform only their own side
@scenario("../specs/behaviours/result.feature", "Curried functions transform only their own side")
def test_curried_functions_transform_only_their_own_side() -> None:
    """PT-B05: the curried map_err, flat_map_err, and tap_err transform only Err."""
