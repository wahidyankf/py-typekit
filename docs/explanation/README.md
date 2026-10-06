# Explanation

Why py-typekit is built the way it is, and what its types guarantee. Read these to understand, not to get a task done.

## Directory Map

- [Why a `Result` instead of an exception](./why-result-over-exceptions.md) — what a failure in the return type buys,
  and where exceptions still belong.
- [Why `Option` is `Some[T] | None`](./why-option-is-some-or-none.md) — absence as the native `None`, the reason for
  `Some`, and why `Option` has no methods.
- [What Pyright catches](./what-pyright-catches.md) — the type-safety guarantees, shown as five mistakes strict Pyright
  refuses, each with the error it reports.
- [Naming choices](./naming-choices.md) — why `attempt`, `pipe`, and module-qualified combinators.

## Next steps

- [Reference](../reference/README.md) for the exact API.
- [How-to guides](../how-to/README.md) to put it to work.
