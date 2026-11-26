"""End-to-end bindings: each scenario's unit binding runs against the built wheel, not against src/."""

from collections.abc import Callable


# @scenario specs/behaviours/result.feature: Ok maps its value
def test_wheel_ok_maps_its_value(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_result.py::test_ok_maps_its_value")


# @scenario specs/behaviours/result.feature: Err map leaves its error unchanged
def test_wheel_err_map_leaves_its_error_unchanged(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_result.py::test_err_map_leaves_its_error_unchanged")


# @scenario specs/behaviours/result.feature: Flat map chains an Ok and keeps an Err
def test_wheel_flat_map_chains_an_ok_and_keeps_an_err(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_result.py::test_flat_map_chains_an_ok_and_keeps_an_err")


# @scenario specs/behaviours/result.feature: Tap and tap err see their own side
def test_wheel_tap_and_tap_err_see_their_own_side(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_result.py::test_tap_and_tap_err_see_their_own_side")


# @scenario specs/behaviours/result.feature: Curried functions transform only their own side
def test_wheel_curried_functions_transform_only_their_own_side(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_result.py::test_curried_functions_transform_only_their_own_side")


# @scenario specs/behaviours/option.feature: from_optional keeps absence and wraps a value
def test_wheel_from_optional_keeps_absence_and_wraps_a_value(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_option.py::test_from_optional_keeps_absence_and_wraps_a_value")


# @scenario specs/behaviours/option.feature: option.map and option.flat_map act only on a Some
def test_wheel_option_map_and_flat_map_act_only_on_a_some(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_option.py::test_option_map_and_flat_map_act_only_on_a_some")


# @scenario specs/behaviours/option.feature: ok_or turns a Some into Ok and absence into Err
def test_wheel_ok_or_turns_a_some_into_ok_and_absence_into_err(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_option.py::test_ok_or_turns_a_some_into_ok_and_absence_into_err")


# @scenario specs/behaviours/boundary.feature: attempt returns Ok when the call succeeds
def test_wheel_attempt_returns_ok_when_the_call_succeeds(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_boundary.py::test_attempt_returns_ok_when_the_call_succeeds")


# @scenario specs/behaviours/boundary.feature: attempt catches a named type and propagates any other
def test_wheel_attempt_catches_a_named_type_and_propagates_any_other(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_boundary.py::test_attempt_catches_a_named_type_and_propagates_any_other")


# @scenario specs/behaviours/pipeline.feature: pipe runs nine stages from left to right
def test_wheel_pipe_runs_nine_stages_from_left_to_right(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_pipeline.py::test_pipe_runs_nine_stages_from_left_to_right")


# @scenario specs/behaviours/exports.feature: the package exports exactly ten names
def test_wheel_the_package_exports_exactly_ten_names(
    run_in_wheel: Callable[[str], None],
) -> None:
    run_in_wheel("test_behaviour_exports.py::test_the_package_exports_exactly_ten_names")
