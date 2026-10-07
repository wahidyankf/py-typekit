"""``typekit.pipeline``: ``pipe`` chains functions left to right, each one's result the next one's argument.

``pipe(value, f1, f2)`` is ``f2(f1(value))`` written in the order it runs. It takes one to nine functions, each typed
from the one before, so a mismatched stage is a type error at the stage. A longer chain nests:
``pipe(pipe(value, f1, ..., f9), f10)`` loses no type. The curried combinators of ``typekit.result`` and
``typekit.option`` are the stages that make ``pipe`` chain a ``Result`` or an ``Option``.

Pyright solves each stage from the one before, so the input must carry its full type: a parameter, a function return,
or an annotation it has not narrowed. A bare ``Ok(2)`` carries no error type: strict mode reports a lambda stage, whose
parameter Pyright cannot infer, as partially unknown, and with a named function stage the result's error side stays an
unsolved type variable that strict mode does not report.
"""

from collections.abc import Callable
from typing import overload


@overload
def pipe[A, B](value: A, f1: Callable[[A], B], /) -> B: ...
@overload
def pipe[A, B, C](value: A, f1: Callable[[A], B], f2: Callable[[B], C], /) -> C: ...
@overload
def pipe[A, B, C, D](value: A, f1: Callable[[A], B], f2: Callable[[B], C], f3: Callable[[C], D], /) -> D: ...
@overload
def pipe[A, B, C, D, E](
    value: A, f1: Callable[[A], B], f2: Callable[[B], C], f3: Callable[[C], D], f4: Callable[[D], E], /
) -> E: ...
@overload
def pipe[A, B, C, D, E, F](
    value: A,
    f1: Callable[[A], B],
    f2: Callable[[B], C],
    f3: Callable[[C], D],
    f4: Callable[[D], E],
    f5: Callable[[E], F],
    /,
) -> F: ...
@overload
def pipe[A, B, C, D, E, F, G](
    value: A,
    f1: Callable[[A], B],
    f2: Callable[[B], C],
    f3: Callable[[C], D],
    f4: Callable[[D], E],
    f5: Callable[[E], F],
    f6: Callable[[F], G],
    /,
) -> G: ...
@overload
def pipe[A, B, C, D, E, F, G, H](
    value: A,
    f1: Callable[[A], B],
    f2: Callable[[B], C],
    f3: Callable[[C], D],
    f4: Callable[[D], E],
    f5: Callable[[E], F],
    f6: Callable[[F], G],
    f7: Callable[[G], H],
    /,
) -> H: ...
@overload
def pipe[A, B, C, D, E, F, G, H, I](
    value: A,
    f1: Callable[[A], B],
    f2: Callable[[B], C],
    f3: Callable[[C], D],
    f4: Callable[[D], E],
    f5: Callable[[E], F],
    f6: Callable[[F], G],
    f7: Callable[[G], H],
    f8: Callable[[H], I],
    /,
) -> I: ...
@overload
def pipe[A, B, C, D, E, F, G, H, I, J](
    value: A,
    f1: Callable[[A], B],
    f2: Callable[[B], C],
    f3: Callable[[C], D],
    f4: Callable[[D], E],
    f5: Callable[[E], F],
    f6: Callable[[F], G],
    f7: Callable[[G], H],
    f8: Callable[[H], I],
    f9: Callable[[I], J],
    /,
) -> J: ...


def pipe(value: object, /, *functions: Callable[..., object]) -> object:
    """Apply each function to the value left to right and return the last result.

    Every function runs exactly once, in argument order, on what the previous one returned. An exception a function
    raises propagates and the later functions do not run. The signature accepts one to nine functions; the
    implementation applies however many it is given.
    """

    for function in functions:
        value = function(value)

    return value
