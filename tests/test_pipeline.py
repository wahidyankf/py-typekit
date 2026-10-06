"""pipe applies its functions left to right and returns the last result (AC-49)."""

from collections.abc import Callable

from typekit.pipeline import pipe


def make_step(calls: list[str], label: str) -> Callable[[str], str]:
    """A function that records its call in `calls`, then returns the text it was given with `label` appended."""

    def step(text: str) -> str:
        calls.append(label)
        return text + label

    return step


def test_pipe_applies_one_function() -> None:
    """One function runs once on the value, and its result is the result of the pipe."""

    calls: list[str] = []

    assert pipe("", make_step(calls, "a")) == "a"
    assert calls == ["a"]


def test_pipe_applies_two_functions_left_to_right() -> None:
    """The second function receives what the first returned, and the pipe returns what the second returned."""

    calls: list[str] = []

    assert pipe("", make_step(calls, "a"), make_step(calls, "b")) == "ab"
    assert calls == ["a", "b"]


def test_pipe_applies_nine_functions_left_to_right_once_each() -> None:
    """Nine functions, the most a pipe takes, each run exactly once and in argument order."""

    calls: list[str] = []
    a, b, c, d, e, f, g, h, i = (make_step(calls, label) for label in "abcdefghi")

    assert pipe("", a, b, c, d, e, f, g, h, i) == "abcdefghi"
    assert calls == list("abcdefghi")


def test_pipe_passes_a_value_of_any_type_through_functions_of_changing_types() -> None:
    """Each stage may change the type the next one receives."""

    assert pipe(12, str, len, float) == 2.0
