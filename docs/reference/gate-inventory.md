# Gate inventory

This page lists each gate in `repo-config.yml` that runs on a local hook or a CI surface, one row per gate id. The
registry is the source of this table: where the two differ, `repo-config.yml` is right. `Surface` lists the run-on keys
a gate declares, in the order pre-commit, commit-msg, pre-push, pull-request, and main. `Rule` is the C-number that the
gate reason names, or `-` when the registry gives none.

| Gate id                  | Surface                  | Command                                                | Rule |
| ------------------------ | ------------------------ | ------------------------------------------------------ | ---- |
| `format-staged`          | pre-commit, pull-request | `bash scripts/format-staged.sh <staged.paths>`         | -    |
| `commit-message`         | commit-msg, pull-request | `bash scripts/check-commit-message.sh`                 | -    |
| `public-safety`          | pull-request, main       | `bash scripts/public-safety/check.sh`                  | C6   |
| `public-safety-message`  | pull-request             | `bash scripts/public-safety/check.sh`                  | C6   |
| `public-safety-range`    | pre-push, pull-request   | `bash scripts/public-safety/check.sh`                  | -    |
| `markdown-format`        | pull-request, main       | `npx --no-install prettier --check .`                  | C6   |
| `markdown-line-length`   | pull-request, main       | `bash scripts/check-markdown-line-length.sh`           | C6   |
| `markdownlint`           | pull-request             | `npx --no-install markdownlint-cli2 "**/*.md"`         | C16  |
| `ruff-format`            | pull-request, main       | `uv run --locked ruff format --check`                  | C6   |
| `ruff-lint`              | pull-request, main       | `uv run --locked ruff check`                           | C6   |
| `pyright`                | pull-request, main       | `uv run --locked pyright`                              | C6   |
| `tests`                  | pull-request, main       | `uv run --locked coverage run -m pytest ...`           | C6   |
| `coverage`               | pull-request, main       | `uv run --locked coverage report`                      | C6   |
| `test-integration`       | pull-request             | `uv run --locked pytest tests/integration`             | C12  |
| `doc-snippets`           | pull-request, main       | `uv run --locked python scripts/check-doc-snippets.py` | C6   |
| `repo-config`            | pull-request, main       | `./rhino repo-config validate`                         | C6   |
| `gate-registry`          | pull-request, main       | `./rhino gate validate`                                | C6   |
| `artifact-metadata`      | pull-request, main       | `./rhino metadata validate`                            | C6   |
| `word-budget`            | pull-request, main       | `./rhino governance word-budget validate`              | C6   |
| `internal-links`         | pull-request, main       | `./rhino md internal-link validate`                    | C6   |
| `mermaid`                | pull-request, main       | `./rhino md mermaid validate`                          | C6   |
| `md-naming`              | pull-request, main       | `./rhino md naming validate`                           | C6   |
| `directory-map`          | pull-request, main       | `./rhino governance directory-map validate`            | C6   |
| `quality-gates`          | pull-request, main       | `./rhino governance quality-gates validate`            | C6   |
| `harness-adapters`       | pull-request, main       | `bash -c ...`                                          | C6   |
| `wheel-check`            | pull-request, main       | `bash scripts/check-wheel.sh`                          | -    |
| `public-safety-tests`    | pull-request, main       | `bash scripts/public-safety/tests/run.sh`              | -    |
| `behaviour-coverage`     | pull-request             | `./rhino behaviour coverage validate`                  | C13  |
| `agent-hippo-guard-test` | pull-request             | `bash scripts/agent-hippo-guard.test.sh`               | C21  |
| `e2e`                    | main                     | `uv run --locked pytest tests/e2e`                     | -    |

The table shortens two commands. Their full text follows.

- `tests`: `uv run --locked coverage run -m pytest --ignore tests/e2e --ignore tests/integration`.
- `harness-adapters`: `bash -c` runs these steps in order, joined with `&&`, and stops at the first failure:

```text
./rhino harness adapters validate
bash .commandcode/hooks/agent-policy-selector.test.sh
bash .muse/hooks/run-policy-hook.test.sh
exec bash .commandcode/hooks/git-fixture-isolation.test.sh
```

## Local surfaces

The `wiring.local-surfaces` block in `repo-config.yml` names the three gates that the local hooks run. Each hook calls
`./rhino gate run` with its own surface:

- `.husky/pre-commit` runs `./rhino gate run --surface pre-commit`, which runs `format-staged`: it formats the staged
  files with `scripts/format-staged.sh`.
- `.husky/commit-msg` runs `./rhino gate run --surface commit-msg --message-file "$1"`, which runs `commit-message`:
  Commitlint checks the commit message.
- `.husky/pre-push` runs `./rhino gate run --surface pre-push --push-updates-stdin`, which runs `public-safety-range`:
  the leak scan over the pushed range.

Every other gate runs at `pull-request` or `main` only, so the local hooks stay short.
