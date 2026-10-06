# Why `Option` is `Some[T] | None`

## Absence is the `None` Python already has

Python code marks a possibly missing value as `T | None`, and strict Pyright already refuses to use such a value before
it is narrowed. py-typekit keeps that: an absent `Option` is the plain `None`, so `is None` and `case None` narrow it
with no new vocabulary, and code that already handles `None` keeps working.

## Why `Some` exists at all

If `Option[T]` were just `T | None`, absence could not nest. A lookup that may miss, in a table whose values may
themselves be `None`, has two different kinds of nothing: the key is absent, or the key is present and holds `None`.
`T | None` collapses them into one. With `Some`, they stay apart: `None` is absent, and `Some(None)` is present and
holds `None`. `from_optional` converts the common case, where `None` does mean absent.

`Some` is built like `Ok`: immutable, covariant, and matched by `case Some(value)`, so the two types read alike.

## Why `Option` has no methods

A `Result` chains through its methods because both of its sides are py-typekit classes. An `Option`'s absent side is
`None`, and Python cannot add methods to `NoneType`, so `found.map(f)` cannot work when `found` is `None`. Making
absence a py-typekit class instead would give up the native `None` and its narrowing.

So `Option` chains only through `pipe`, with the curried `option.map`, `option.flat_map`, `option.tap`, and
`option.ok_or`, each a function that handles `None` itself. The `pipe` style also works for a `Result`, so one way of
chaining covers both types.

## Why there is a bridge to `Result`

Absence often stops being acceptable partway through a chain: a missing setting is fine to look up and an error to run
without. `option.ok_or(error)` turns `None` into `Err(error)` and `Some(value)` into `Ok(value)` at the point where that
happens, so the rest of the chain carries a named failure instead of an unexplained `None`.
