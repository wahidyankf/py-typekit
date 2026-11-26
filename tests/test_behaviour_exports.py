"""Behaviour binding for specs/behaviours/exports.feature: the package exports exactly its ten public names."""

import inspect

from pytest_bdd import given, scenario, then

import typekit
from typekit import option, result

PUBLIC_NAMES = {
    "Err",
    "Ok",
    "Option",
    "Result",
    "Some",
    "attempt",
    "from_optional",
    "option",
    "pipe",
    "result",
}


@given("the typekit package is imported")
def package_is_imported() -> None:
    """The package is imported at the top of this module, so there is nothing more to set up."""


@then("the package lists exactly the ten public names")
def package_lists_ten_names() -> None:
    """The package's __all__ holds exactly the ten public names, once each."""

    assert set(typekit.__all__) == PUBLIC_NAMES
    assert len(typekit.__all__) == 10


@then("option and result are reached as modules")
def option_and_result_are_modules() -> None:
    """option and result are modules, reached as attributes of the package."""

    assert inspect.ismodule(typekit.option)
    assert inspect.ismodule(typekit.result)
    assert typekit.option is option
    assert typekit.result is result


# @scenario specs/behaviours/exports.feature: the package exports exactly ten names
@scenario("../specs/behaviours/exports.feature", "the package exports exactly ten names")
def test_the_package_exports_exactly_ten_names() -> None:
    """PT-B12: the package exports exactly the ten names in __all__, and option and result are modules."""
