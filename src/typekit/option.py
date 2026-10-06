"""``typekit.option``: absence is ``None``, presence is ``Some``, and a value that may be absent is an ``Option``.

``Option[T]`` is ``Some[T] | None``. Absence is the native ``None``, so a consumer narrows with ``match`` or
``is None``, and strict Pyright refuses to read through a value that may be ``None`` until it has. ``Option`` has no
methods: Python cannot add methods to ``NoneType``. It chains through ``typekit.pipeline.pipe`` with the curried
``map``, ``flat_map``, ``tap``, and ``ok_or`` of this module, each of which acts on a ``Some`` and passes ``None``
through unchanged.

``Some`` exists, rather than ``Option[T] = T | None``, so that nested absence stays expressible: ``Some(None)`` is
present and holds ``None``, while ``None`` is absent. It is built like ``Ok``: each ``Some`` exposes its value only
through a read-only property, so pyright infers it covariant, and each refuses every write and delete at runtime, its
private slot included, with ``FrozenInstanceError``.

The module-level combinators share their names with the builtin ``map`` and with ``typekit.result``'s, so import the
module, ``from typekit import option``, and write ``option.map(f)``.
"""

from collections.abc import Callable
from dataclasses import FrozenInstanceError
from typing import Never, final

from typekit.result import Err, Ok, Result


@final
class Some[T]:
    """A present value."""

    __slots__ = ("_value",)
    __match_args__ = ("value",)
    _value: T

    def __init__(self, value: T) -> None:
        """Hold the present value."""

        object.__setattr__(self, "_value", value)

    @property
    def value(self) -> T:
        """The present value."""

        return self._value

    @property
    def _content(self) -> object:
        """The held value, typed without ``T`` so another ``Some`` can be compared with it."""

        return self._value

    def __setattr__(self, name: str, value: Never) -> Never:
        raise FrozenInstanceError(f"cannot assign to field {name!r}")

    def __delattr__(self, name: str) -> Never:
        raise FrozenInstanceError(f"cannot delete field {name!r}")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Some) and self._content == other._content

    def __repr__(self) -> str:
        return f"Some({self._value!r})"


type Option[T] = Some[T] | None


def from_optional[T](value: T | None, /) -> Option[T]:
    """``None`` stays absent; any other value, a falsy one included, becomes present as ``Some(value)``."""

    return None if value is None else Some(value)


def map[T, U](f: Callable[[T], U], /) -> Callable[[Option[T]], Option[U]]:
    """A function that transforms a present value with ``f`` and leaves absence absent."""

    def apply(option: Option[T]) -> Option[U]:
        if option is None:
            return None

        return Some(f(option.value))

    return apply


def flat_map[T, U](f: Callable[[T], Option[U]], /) -> Callable[[Option[T]], Option[U]]:
    """A function that continues a present value with the step ``f``, whose own outcome is the result."""

    def apply(option: Option[T]) -> Option[U]:
        if option is None:
            return None

        return f(option.value)

    return apply


def tap[T](f: Callable[[T], object], /) -> Callable[[Option[T]], Option[T]]:
    """A function that shows a present value to ``f`` and returns the option unchanged.

    ``f`` runs for its effect, once per present value it receives; absence passes through without calling it.
    """

    def apply(option: Option[T]) -> Option[T]:
        if option is None:
            return None

        f(option.value)

        return option

    return apply


def ok_or[T, E](error: E, /) -> Callable[[Option[T]], Result[T, E]]:
    """A function that turns a present value into ``Ok`` and absence into ``Err(error)``."""

    def apply(option: Option[T]) -> Result[T, E]:
        if option is None:
            return Err(error)

        return Ok(option.value)

    return apply
