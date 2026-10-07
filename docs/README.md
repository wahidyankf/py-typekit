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

py-typekit is one of the seven **`ose-projects`** repositories — the repositories
[Open Sharia Enterprise](https://github.com/wahidyankf/ose-public) is built and maintained in. Each entry gives the
repository's role, then how it relates to py-typekit:

- **[`py-typekit`](https://github.com/wahidyankf/py-typekit)** — typed functional primitives for Python. This
  repository.
- [`ose-public`](https://github.com/wahidyankf/ose-public) — the OSE product platform and research. Upstream
  consumption: its FERRET command-line tool pins a py-typekit release.
- [`rhino`](https://github.com/wahidyankf/rhino) — repository hygiene. Upstream consumption: py-typekit's gates pin a
  RHINO release.
- [`ose-rules`](https://github.com/wahidyankf/ose-rules) — the reference catalog of governance, planning, agent, and
  skill artifacts. Knowledge sharing: py-typekit adopts its artifacts by explicit one-off copy and owns each copy.
- [`hippo`](https://github.com/wahidyankf/hippo) — host resource coordination. None: py-typekit pins no HIPPO, so it is
  named here only because it is a member.
- [`beaver-nest`](https://github.com/wahidyankf/beaver-nest) — an independent family product. None: named only because
  it is a member.
- _(unnamed, private)_ — authorized operations. None: named only because it is a member. It stays unnamed because this
  repository is public, and naming a private repository publishes what its owner did not.

**That label is navigation, not coupling.** `ose-projects` is a routing label only — not an organization, a parent
repository, a parity group, or a shared release. The seven are developed, versioned, gated, and released independently.
Membership obliges each member only to name the others, so a reader who finds one can find the other six, and nothing
more. py-typekit is usable entirely on its own.
