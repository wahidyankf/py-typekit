"""``typekit.boundary``: the one place typekit catches an exception, so a consumer writes no ``except`` of its own.

``attempt`` turns a call that may raise into a ``Result``. It lives apart from ``typekit.result`` because that module is
a verbatim port of the ledger's, and because catching is the boundary between code that raises and code that returns
values.
"""

from collections.abc import Callable

from typekit.result import Err, Ok, Result


def attempt[T, E: Exception](call: Callable[[], T], error: type[E], /, *more: type[E]) -> Result[T, E]:
    """Run ``call()`` once, returning ``Ok`` with its value, or ``Err`` holding an exception it raised of a named type.

    The exception types are named at the call site: ``error`` and any in ``more``. Only an instance of one of them,
    a subclass included, becomes ``Err``, and the fault is the exception object itself. Any other exception
    propagates unchanged: there is no default type and no catch-all, so naming no type is refused, as a type error
    under Pyright and as a ``TypeError`` at run time. The bound is ``Exception``, so an interrupt or an exit is never
    caught.

    ``call`` takes no arguments; bind them with a ``lambda`` or ``functools.partial``. ``attempt`` runs the caller's
    call, so any effect that call has happens here, once.
    """

    try:
        value = call()
    except (error, *more) as caught:
        return Err(caught)

    return Ok(value)
