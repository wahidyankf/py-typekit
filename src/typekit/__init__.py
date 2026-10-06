"""Typed functional primitives, checked by strict Pyright.

``Result`` (``Ok[T] | Err[E]``) and ``Option`` (``Some[T] | None``) make a failure or an absence a value the caller
must handle. ``attempt`` turns a raising call into a ``Result``, and ``pipe`` chains functions left to right, with
the curried combinators of the ``result`` and ``option`` modules as its stages. Import the modules, not their
combinators: ``from typekit import option, result``.
"""

from typekit import option, result
from typekit.boundary import attempt
from typekit.option import Option, Some, from_optional
from typekit.pipeline import pipe
from typekit.result import Err, Ok, Result

__all__ = [
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
]
