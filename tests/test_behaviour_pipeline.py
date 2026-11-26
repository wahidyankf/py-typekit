"""Behaviour binding for specs/behaviours/pipeline.feature: pipe applies its stages from left to right."""

from collections.abc import Callable
from dataclasses import dataclass

import pytest
from pytest_bdd import given, parsers, scenario, then, when

from typekit.pipeline import pipe


@dataclass
class World:
    """What the steps of one scenario share."""

    text: str = ""
    outcome: str = ""


@pytest.fixture
def world() -> World:
    """A fresh world for each scenario."""

    return World()


def append(letter: str) -> Callable[[str], str]:
    """A stage that adds one letter to the end of the text."""

    def stage(text: str) -> str:
        return text + letter

    return stage


@given(parsers.parse('the text "{text}"'))
def text_is(world: World, text: str) -> None:
    """The text the pipe starts from."""

    world.text = text


@when("I pipe the text through nine stages that each add one letter")
def pipe_nine_stages(world: World) -> None:
    """Pipe the text through nine stages, a to i, in order."""

    world.outcome = pipe(
        world.text,
        append("a"),
        append("b"),
        append("c"),
        append("d"),
        append("e"),
        append("f"),
        append("g"),
        append("h"),
        append("i"),
    )


@then(parsers.parse('the outcome is "{text}"'))
def outcome_is_text(world: World, text: str) -> None:
    """The outcome is the text."""

    assert world.outcome == text


# @scenario specs/behaviours/pipeline.feature: pipe runs nine stages from left to right
@scenario("../specs/behaviours/pipeline.feature", "pipe runs nine stages from left to right")
def test_pipe_runs_nine_stages_from_left_to_right() -> None:
    """PT-B11: pipe applies one to nine stages from left to right and returns the last value."""
