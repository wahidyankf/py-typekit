"""``typekit.result``: a failure is a value the caller must handle, never an exception it might miss.

A fallible function returns ``Result[T, E]``: ``Ok`` with its value, or ``Err`` with a named fault. The caller takes it
apart with ``match`` or an ``isinstance`` early return, or chains it: ``map`` and ``map_err`` change one side,
``flat_map`` and ``flat_map_err`` continue with a step that may itself fail, and ``tap`` and ``tap_err`` look at one
side and pass the result on unchanged. Each method acts on its own side and hands the other back as it is.

Both are hand-written rather than dataclasses: each exposes its content only through a read-only property, so pyright
infers them covariant, and an ``Ok[bool]`` is an ``Ok[int]``; a frozen dataclass would be invariant. Each still refuses
every write and delete at runtime, its private slot included, with ``FrozenInstanceError`` as a frozen dataclass does;
typing the value ``Never`` keeps pyright refusing a write to any other name too.

Below the classes, the module-level ``map``, ``map_err``, ``flat_map``, ``flat_map_err``, ``tap``, and ``tap_err`` are
the same six combinators curried for ``typekit.pipeline.pipe``: each takes the function and returns a callable from a
``Result`` to a ``Result``, and is its method of the same name by construction. They share their names with the methods
and with the builtin ``map``, so import the module, ``from typekit import result``, and write ``result.map(f)``.
"""

from collections.abc import Callable
from dataclasses import FrozenInstanceError
from typing import Never, final


@final
class Ok[T]:
    """A success, holding its value."""

    __slots__ = ("_value",)
    __match_args__ = ("value",)
    _value: T

    def __init__(self, value: T) -> None:
        """Hold the success's value."""

        object.__setattr__(self, "_value", value)

    @property
    def value(self) -> T:
        """The success's value."""

        return self._value

    @property
    def _content(self) -> object:
        """The held value, typed without ``T`` so another ``Ok`` can be compared with it."""

        return self._value

    def map[U](self, transform: Callable[[T], U]) -> Ok[U]:
        """The value, transformed."""

        return Ok(transform(self._value))

    def map_err(self, transform: Callable[[Never], object]) -> Ok[T]:
        """This success, unchanged: there is no fault to transform."""

        return self

    def flat_map[U, F](self, step: Callable[[T], Result[U, F]]) -> Result[U, F]:
        """What the next fallible step makes of the value."""

        return step(self._value)

    def flat_map_err(self, step: Callable[[Never], object]) -> Ok[T]:
        """This success, unchanged: there is no fault to recover from."""

        return self

    def tap(self, action: Callable[[T], object]) -> Ok[T]:
        """This success, unchanged, once ``action`` has seen its value."""

        action(self._value)

        return self

    def tap_err(self, action: Callable[[Never], object]) -> Ok[T]:
        """This success, unchanged: there is no fault to see."""

        return self

    def __setattr__(self, name: str, value: Never) -> Never:
        raise FrozenInstanceError(f"cannot assign to field {name!r}")

    def __delattr__(self, name: str) -> Never:
        raise FrozenInstanceError(f"cannot delete field {name!r}")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Ok) and self._content == other._content

    def __repr__(self) -> str:
        return f"Ok({self._value!r})"


@final
class Err[E]:
    """A failure, holding its fault."""

    __slots__ = ("_error",)
    __match_args__ = ("error",)
    _error: E

    def __init__(self, error: E) -> None:
        """Hold the failure's fault."""

        object.__setattr__(self, "_error", error)

    @property
    def error(self) -> E:
        """The failure's fault."""

        return self._error

    @property
    def _content(self) -> object:
        """The held fault, typed without ``E`` so another ``Err`` can be compared with it."""

        return self._error

    def map(self, transform: Callable[[Never], object]) -> Err[E]:
        """This failure, unchanged: there is no value to transform."""

        return self

    def map_err[F](self, transform: Callable[[E], F]) -> Err[F]:
        """The fault, transformed."""

        return Err(transform(self._error))

    def flat_map(self, step: Callable[[Never], object]) -> Err[E]:
        """This failure, unchanged: the next step does not run."""

        return self

    def flat_map_err[U, F](self, step: Callable[[E], Result[U, F]]) -> Result[U, F]:
        """What the recovering step makes of the fault."""

        return step(self._error)

    def tap(self, action: Callable[[Never], object]) -> Err[E]:
        """This failure, unchanged: there is no value to see."""

        return self

    def tap_err(self, action: Callable[[E], object]) -> Err[E]:
        """This failure, unchanged, once ``action`` has seen its fault."""

        action(self._error)

        return self

    def __setattr__(self, name: str, value: Never) -> Never:
        raise FrozenInstanceError(f"cannot assign to field {name!r}")

    def __delattr__(self, name: str) -> Never:
        raise FrozenInstanceError(f"cannot delete field {name!r}")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Err) and self._content == other._content

    def __repr__(self) -> str:
        return f"Err({self._error!r})"


type Result[T, E] = Ok[T] | Err[E]


def map[T, U, E](f: Callable[[T], U], /) -> Callable[[Result[T, E]], Result[U, E]]:
    """A function that transforms a success's value with ``f`` and passes a failure on, like ``Result.map``."""

    def apply(result: Result[T, E]) -> Result[U, E]:
        return result.map(f)

    return apply


def map_err[T, E, F](f: Callable[[E], F], /) -> Callable[[Result[T, E]], Result[T, F]]:
    """A function that transforms a failure's fault with ``f`` and passes a success on, like ``Result.map_err``."""

    def apply(result: Result[T, E]) -> Result[T, F]:
        return result.map_err(f)

    return apply


def flat_map[T, U, E](f: Callable[[T], Result[U, E]], /) -> Callable[[Result[T, E]], Result[U, E]]:
    """A function that continues a success with the fallible step ``f``, like ``Result.flat_map``."""

    def apply(result: Result[T, E]) -> Result[U, E]:
        return result.flat_map(f)

    return apply


def flat_map_err[T, E, F](f: Callable[[E], Result[T, F]], /) -> Callable[[Result[T, E]], Result[T, F]]:
    """A function that recovers a failure with the fallible step ``f``, like ``Result.flat_map_err``."""

    def apply(result: Result[T, E]) -> Result[T, F]:
        return result.flat_map_err(f)

    return apply


def tap[T, E](f: Callable[[T], object], /) -> Callable[[Result[T, E]], Result[T, E]]:
    """A function that shows a success's value to ``f`` and returns the result unchanged, like ``Result.tap``.

    ``f`` runs for its effect, once per success it receives; a failure passes through without calling it.
    """

    def apply(result: Result[T, E]) -> Result[T, E]:
        return result.tap(f)

    return apply


def tap_err[T, E](f: Callable[[E], object], /) -> Callable[[Result[T, E]], Result[T, E]]:
    """A function that shows a failure's fault to ``f`` and returns the result unchanged, like ``Result.tap_err``.

    ``f`` runs for its effect, once per failure it receives; a success passes through without calling it.
    """

    def apply(result: Result[T, E]) -> Result[T, E]:
        return result.tap_err(f)

    return apply
