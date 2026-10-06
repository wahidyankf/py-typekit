# How-to guides

Directions for a goal you already have. Each guide assumes you know what you want and gets you there.

If you are still learning what py-typekit does, start with the [tutorial](../tutorials/README.md) instead.

## Directory Map

- [Wrap a raising call with `attempt`](./wrap-exceptions-with-attempt.md) — turn code that raises into a `Result` that
  names exactly the failures you expect.
- [Chain steps with `pipe`](./chain-with-pipe.md) — run fallible steps one after another with the methods or with `pipe`
  and the curried combinators.
- [Handle a value that may be absent](./handle-an-option.md) — build an `Option` from `T | None`, transform it, and turn
  it into a `Result`.
- [Match exhaustively](./match-exhaustively.md) — take a `Result` or an `Option` apart so Pyright rejects a forgotten
  case.
- [Pin or upgrade the version](./pin-or-upgrade-the-version.md) — depend on a release tag and move to a later one.

## Next steps

- [Reference](../reference/README.md) for exact signatures and behaviour.
- [Explanation](../explanation/README.md) for why py-typekit behaves this way.
