"""The public surface: ten names, one spelling each, none shadowing a builtin (AC-54)."""

import builtins

import typekit
from typekit import option, result
from typekit.option import Option, Some
from typekit.result import Err, Ok, Result

PUBLIC_NAMES = {"Ok", "Err", "Result", "Some", "Option", "from_optional", "attempt", "pipe", "result", "option"}


def ok_one() -> Result[int, str]:
    """`Ok(1)` typed as the whole `Result`, so a curried combinator can infer its fault type."""

    return Ok(1)


def add_one(number: int) -> int:
    """The number plus one."""

    return number + 1


def nothing() -> Option[int]:
    """Absence typed as the whole `Option`, for the same reason."""

    return None


def test_all_is_exactly_the_ten_public_names_once_each() -> None:
    """`__all__` lists the five types, `from_optional`, `attempt`, `pipe`, and the `result` and `option` modules."""

    assert set(typekit.__all__) == PUBLIC_NAMES
    assert len(typekit.__all__) == len(PUBLIC_NAMES)


def test_every_name_in_all_resolves_on_the_package() -> None:
    """Each listed name is an attribute of `typekit`, so `from typekit import <name>` works."""

    assert [name for name in typekit.__all__ if not hasattr(typekit, name)] == []


def test_no_public_name_is_the_name_of_a_builtin() -> None:
    """A star import or a named import can never shadow a Python builtin."""

    assert [name for name in typekit.__all__ if hasattr(builtins, name)] == []


def test_star_import_brings_in_no_combinator() -> None:
    """`map`, `flat_map`, `tap`, and the rest are reachable only through their modules, each with one spelling."""

    namespace: dict[str, object] = {}

    exec("from typekit import *", namespace)

    assert set(namespace) - {"__builtins__"} == PUBLIC_NAMES


def test_the_modules_hold_the_curried_combinators() -> None:
    """`typekit.result.map` and `typekit.option.ok_or` are the curried combinators, not the classes' methods."""

    assert result.map(add_one)(ok_one()) == Ok(2)
    assert option.ok_or("missing")(nothing()) == Err("missing")
    assert typekit.result is result
    assert typekit.option is option
    assert typekit.Some is Some
