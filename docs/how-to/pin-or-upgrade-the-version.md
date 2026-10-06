# How to pin or upgrade the version

You depend on py-typekit and want a fixed, reproducible version, or you want to move to a later release.

## Pin a release tag

py-typekit is not on PyPI. Each release is an annotated Git tag, and a released tag never moves. Add the tag as a uv Git
dependency:

```bash
uv add git+https://github.com/wahidyankf/py-typekit --tag v0.1.0
```

uv writes the source to `pyproject.toml`:

```toml
[tool.uv.sources]
py-typekit = { git = "https://github.com/wahidyankf/py-typekit", tag = "v0.1.0" }
```

and records the tag's exact commit in `uv.lock`, so every install of that lockfile gets the same code. Commit both
files. Install from the lockfile with `uv sync --locked`, which fails instead of re-resolving when the two disagree.

## Upgrade to a later tag

Read the [changelog](../../CHANGELOG.md) for what the new tag changes, then run the same command with that tag:

```bash
uv add git+https://github.com/wahidyankf/py-typekit --tag <new-tag>
```

uv rewrites the `tag` in `pyproject.toml` and the commit in `uv.lock`. Run your type checker and tests before you commit
the change. `v0.1.0` is the first release, so no upgrade has been run against this repository yet; the command form is
uv's documented one for a Git tag source.

## Avoid a branch or an unpinned URL

`--branch main`, or a Git URL without `--tag`, follows whatever the branch holds when the lockfile is next resolved. Pin
a tag, so your build changes only when you change it.
