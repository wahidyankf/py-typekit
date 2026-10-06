# py-typekit

A zero-dependency, strictly typed Python 3.14 library of functional primitives, imported as `typekit`: `Result`
(`Ok[T] | Err[E]`), `Option` (`Some[T] | None`), `attempt`, and `pipe` with curried combinators. See
[README.md](README.md).

## Consumption

Releases are annotated semver tags only; nothing is uploaded to PyPI. A consumer pins a tag as a uv Git dependency
(`uv add git+https://github.com/wahidyankf/py-typekit --tag vX.Y.Z`), and `uv.lock` records its commit. The package
ships `py.typed`. A released tag never moves, per [Release Cut](repo-governance/workflows/maintenance/release-cut.md).

## Library

`src/typekit/` holds `result.py` (`Ok`, `Err`, `Result`, and the curried `map`, `map_err`, `flat_map`, `flat_map_err`,
`tap`, `tap_err`), `option.py` (`Some`, `Option`, `from_optional`, and the curried `map`, `flat_map`, `tap`, `ok_or`),
`boundary.py` (`attempt`, the one `except` in the package), and `pipeline.py` (`pipe`, one to nine stages, one
`@overload` each). `__all__` lists exactly ten names; consumers reach the combinators through their modules,
`from typekit import option, result`, so none shadows the builtin `map`. A runtime dependency is never added.

## Gates

```text
uv run pytest                          # tests, fast, no coverage
uv run --locked coverage run -m pytest && uv run --locked coverage report
uv run pyright
uv run ruff check && uv run ruff format --check
npx --no-install prettier --check .
bash scripts/check-wheel.sh            # the wheel lists py.typed and declares no dependency
./rhino gate run --surface main        # everything before a pull request
```

`repo-config.yml` is the one gate registry. The husky hooks, the hosted workflow, and the aggregate command dispatch it
through `./rhino gate run --surface <surface>`, so a gate added there reaches every surface it declares. `pre-push`
refuses a push whose tests fail or whose branch coverage is below 100%, and one that breaks a link, a word budget, the
120-column limit, Prettier formatting, or a generated adapter, or adds a Mermaid block.

`./rhino` installs the RHINO release `rhino.lock` pins and verifies it before running; exit `125` is the wrapper
refusing. This repository pins RHINO only: no HIPPO and no FERRET.

## Testing

Work test-first under [Test-Driven Development](repo-governance/development/quality/testing/test-driven-development.md).
The suite is unit tests only; behaviour-driven development and Gherkin bindings are not adopted. Branch coverage over
`typekit` stays at 100%, measured with coverage.py directly, and its one exclusion is the `@overload` stubs. Pyright
runs in strict mode. The [repository adapter](repo-governance/development/quality/stacks/repository-adapter.md) records
these decisions.

## Tooling

uv provisions Python and the dev dependencies: pytest, coverage, pyright, and ruff. Node carries repository tooling only
— Prettier, markdownlint-cli2, and husky, as `devDependencies` of a private `package.json` — and is never part of the
library, its wheel, or its Python dependencies. `npm ci` installs it and the hooks.

## Delivery

Every change starts in a task worktree at `worktrees/<task>`, never a sibling directory, and lands through a pull
request merged by rebase under [Pull Request Merge](repo-governance/development/workflow/pull-request-merge.md), once
the `quality` and `leak-review` checks pass on its head. The
[PR Leak Review](repo-governance/workflows/quality/pr-leak-review.md) records its verdict on that exact head. Everything
pushed is public, so commits, branch names, and pull-request text pass the screen in `scripts/public-safety/` first.
After the merge, [Dev Artifact Clean-Up](repo-governance/workflows/maintenance/dev-artifact-clean-up.md) removes the
worktree and the task branch and fast-forwards `main`.

## Documents

- Every Markdown line is at most 120 columns, and every diagram is ASCII art in a `text` block, per
  [Markdown Line Length](repo-governance/conventions/markdown-line-length.md) and
  [Markdown Visualizations](repo-governance/conventions/markdown-visualizations.md): no Mermaid, image, or inline HTML.
- `AGENTS.md`, `CLAUDE.md`, and each `repo-governance/**/*.md` and `.agents/**/*.md` file hold 750 words at most.
- Governed documents declare `description` and `when_to_use` front matter, per
  [Artifact Metadata](repo-governance/conventions/structure/artifact-metadata.md).
- Before any rule edit, follow [Rules Propagation](repo-governance/workflows/quality/rules-propagation.md). A later
  catalog change is taken only through [Adopt Artifact](repo-governance/workflows/adoption/adopt-artifact.md).
- Plans live under `plans/`, per the [Plans Convention](repo-governance/conventions/structure/plans.md).

## Governance and Agents

| Path               | Holds                                                                          |
| ------------------ | ------------------------------------------------------------------------------ |
| `repo-governance/` | principles, conventions, development standards, and workflows from `ose-rules` |
| `.agents/agents/`  | canonical agent definitions                                                    |
| `.agents/skills/`  | canonical skills, one directory each with a `SKILL.md`                         |

`./rhino harness adapters generate` renders the `.claude/`, `.codex/`, and `.opencode/` adapters from `.agents/` and
`repo-config.yml`; they are never edited by hand. Dispatch coding work to the fitting `swe-*` agent, except a trivial
edit, a harness without subagents, or a tool repin, per
[SWE Delegation](repo-governance/development/agents/swe-delegation.md). The `pr-review-*` agents run the PR Review gate,
and the plan and docs agents run their workflows.
