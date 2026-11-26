"""Behaviour bindings for specs/behaviours/option.feature: option functions act on a Some and pass absence through."""

from dataclasses import dataclass

import pytest
from pytest_bdd import given, parsers, scenario, then, when

from typekit import option
from typekit.option import Option, Some
from typekit.result import Err, Ok


@dataclass
class World:
    """What the steps of one scenario share."""

    raw: int | None = None
    subject: Option[int] = None
    outcome: object = None


@pytest.fixture
def world() -> World:
    """A fresh world for each scenario."""

    return World()


def add_one(number: int) -> int:
    """The number plus one."""

    return number + 1


def double_into_some(number: int) -> Option[int]:
    """The number doubled, as a present value."""

    return Some(number * 2)


@given("the raw value is missing")
def raw_missing(world: World) -> None:
    """The raw value is absent."""

    world.raw = None


@given(parsers.parse("the raw value is {value:d}"))
def raw_value(world: World, value: int) -> None:
    """The raw value is the number."""

    world.raw = value


@given(parsers.parse("a Some holding {value:d}"))
def some_holding(world: World, value: int) -> None:
    """Set the subject to a Some holding the value."""

    world.subject = Some(value)


@given("an absent option")
def absent_option(world: World) -> None:
    """Set the subject to absence."""

    world.subject = None


@when("I wrap the raw value with from_optional")
def wrap_raw_value(world: World) -> None:
    """Pass the raw value to from_optional."""

    world.outcome = option.from_optional(world.raw)


@when("I map it with option.map and a function that adds 1")
def map_add_one(world: World) -> None:
    """Map the subject with option.map and a function that adds one."""

    world.outcome = option.map(add_one)(world.subject)


@when("I flat map it with option.flat_map and a step that doubles into a Some")
def flat_map_double(world: World) -> None:
    """Flat map the subject with option.flat_map and a step that doubles into a Some."""

    world.outcome = option.flat_map(double_into_some)(world.subject)


@when(parsers.parse('I apply option.ok_or with the error "{error}"'))
def apply_ok_or(world: World, error: str) -> None:
    """Apply option.ok_or with the error to the subject."""

    world.outcome = option.ok_or(error)(world.subject)


@then("the outcome is absent")
def outcome_is_absent(world: World) -> None:
    """The outcome is absence, None."""

    assert world.outcome is None


@then(parsers.parse("the outcome is Some holding {value:d}"))
def outcome_is_some(world: World, value: int) -> None:
    """The outcome is a Some holding the value."""

    assert world.outcome == Some(value)


@then(parsers.parse("the outcome is Ok holding {value:d}"))
def outcome_is_ok(world: World, value: int) -> None:
    """The outcome is an Ok holding the value."""

    assert world.outcome == Ok(value)


@then(parsers.parse('the outcome is Err holding "{text}"'))
def outcome_is_err(world: World, text: str) -> None:
    """The outcome is an Err holding the fault."""

    assert world.outcome == Err(text)


# @scenario specs/behaviours/option.feature: from_optional keeps absence and wraps a value
@scenario("../specs/behaviours/option.feature", "from_optional keeps absence and wraps a value")
def test_from_optional_keeps_absence_and_wraps_a_value() -> None:
    """PT-B06: from_optional turns None into None and a value into Some."""


# @scenario specs/behaviours/option.feature: option.map and option.flat_map act only on a Some
@scenario("../specs/behaviours/option.feature", "option.map and option.flat_map act only on a Some")
def test_option_map_and_flat_map_act_only_on_a_some() -> None:
    """PT-B07: option.map and option.flat_map apply to a Some, and None passes through."""


# @scenario specs/behaviours/option.feature: ok_or turns a Some into Ok and absence into Err
@scenario("../specs/behaviours/option.feature", "ok_or turns a Some into Ok and absence into Err")
def test_ok_or_turns_a_some_into_ok_and_absence_into_err() -> None:
    """PT-B08: ok_or turns Some into Ok and None into Err with the given error."""
