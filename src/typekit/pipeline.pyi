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
