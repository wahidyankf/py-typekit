# Why a `Result` instead of an exception

A Python function's signature says what it returns, not what it raises. `def parse(text: str) -> int` may raise
`ValueError`, and nothing in its type tells a caller so. Pyright cannot check what a signature does not state, so a
forgotten `except` is found when the failure happens, in production, not when the code is written.

## A failure in the type is a failure the caller must handle

`def parse(text: str) -> Result[int, str]` states both outcomes. The caller cannot reach the `int` without first ruling
out the `Err`: Pyright refuses to pass the `Result` where an `int` is expected, and an exhaustive `match` ending in
`assert_never` stops type-checking the moment a case is missing. The failure path becomes code the type checker reads,
like any other value.

It also composes. `map`, `flat_map`, and their curried forms in `pipe` run each step on success and carry the first
failure through to the end, so a chain of fallible steps reads as a straight line with no nested `try` blocks, and the
final type names every way it can fail.

## Where exceptions still belong

Not every failure is an outcome a caller can act on. A bug, a violated invariant, or an interrupt should stop the
program, and an exception does that well. py-typekit therefore converts only what you name: `attempt` catches the types
you list and lets everything else propagate, so expected failures become values and unexpected ones stay loud. It has no
catch-all on purpose.

Exceptions also remain at the edges you do not own. Standard-library and third-party calls raise; `attempt` is the
boundary where their expected failures enter your typed code, and it is the only `except` py-typekit itself contains.

## The cost

A `Result` asks the caller to unwrap every value, which is more ceremony than letting an exception fly. That cost is the
point where the failure is real and expected: the ceremony is exactly the handling a caller would otherwise forget. For
a failure no caller can handle, it is not worth paying, and an exception is the right tool.

See [What Pyright catches](./what-pyright-catches.md) for the guarantees in action.
