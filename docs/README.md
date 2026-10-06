# py-typekit documentation

py-typekit makes a failure and an absence values that strict Pyright makes you handle: `Result` (`Ok[T] | Err[E]`),
`Option` (`Some[T] | None`), `attempt`, which turns a raising call into a `Result`, and `pipe`, which chains functions
left to right with every stage typed. It has no runtime dependencies and is imported as `typekit`.

## Start here

New to py-typekit? [Get started](./tutorials/get-started.md) adds it to a fresh project, writes a function that returns
a `Result`, and lets Pyright catch a forgotten case.

Already know what you want to do? Jump to the [how-to guides](./how-to/README.md).

## Directory Map

This documentation follows the [Diátaxis framework](https://diataxis.fr/), so each page serves one kind of need:

- [Tutorials](./tutorials/README.md) — you are new and want to learn by doing.
- [How-to guides](./how-to/README.md) — you have a specific goal and need the steps.
- [Reference](./reference/README.md) — you need the exact signature and behaviour of a name.
- [Explanation](./explanation/README.md) — you want to understand why py-typekit is built this way, and what Pyright
  guarantees.

Every Python block in these pages is type-checked under strict Pyright by the `doc-snippets` gate. A block that shows a
mistake marks each error with a `# Pyright error:` comment, and the gate requires exactly those errors and no others.

## Project context

The [README](../README.md) is the short front door, and [CHANGELOG.md](../CHANGELOG.md) records what each tag holds.
Contribution rules and the gates live in [AGENTS.md](../AGENTS.md); they govern changing the repository, not using it.
