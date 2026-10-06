# Naming choices

## `attempt`

A name for "run this and capture its failure" had to avoid two traps. `try` is a keyword, and a name such as `catch` or
`safe` suggests that every failure is captured. `attempt` says what happens, an attempt that may not succeed, and pairs
with its required argument list: you attempt a call against the failures you name. It lives in `typekit.boundary`
because it is the boundary between code that raises and code that returns values.

## `pipe`

`pipe(value, f1, f2)` reads in the order the functions run, the opposite of `f2(f1(value))`, as a shell pipeline does.
Several functional libraries use the same name for the same left-to-right application, `toolz` in Python and `fp-ts` in
TypeScript among them, so a reader who knows it there knows it here.

## Module-qualified combinators

The curried combinators share their names with the methods they mirror: `result.map(f)` is the stage form of `r.map(f)`.
Exported bare, `map` would shadow Python's builtin `map` in any module that imports it, and `map` for a `Result` would
collide with `map` for an `Option`. So the combinators are reached only through their modules,
`from typekit import option, result`, and every concept has one spelling: `result.map`, `option.map`.

The ten names `typekit` does export bare (`Ok`, `Err`, `Result`, `Some`, `Option`, `from_optional`, `attempt`, `pipe`,
`result`, `option`) collide with no builtin, so `from typekit import *` is safe, if rarely wise.

## `Ok`, `Err`, and `Some`

These are the names Rust and many functional libraries use for the same ideas, short enough to read inside a `match`.
`None` needs no new name: it is Python's own.
