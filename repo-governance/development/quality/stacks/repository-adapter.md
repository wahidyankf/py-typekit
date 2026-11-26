---
description: >-
  Records the stack packs py-typekit adopted, the agent procedures and quality-gate families it kept, the decisions the
  Python standard leaves open, and every deviation from the catalog.
when_to_use: >-
  Use when working on the typekit library, adopting or retiring a stack pack, or changing a recorded stack, procedure,
  or gate decision.
---

# Repository Adapter

This is py-typekit's adopter-owned record. It holds repository-wide decisions and deviations only. The root
[README](../../../../README.md) names the commands, and [`repo-config.yml`](../../../../repo-config.yml) declares no
`extensions.software-development` inventory, so Project Applicability names the project instead.

## Adopted Packs

| Pack     | Status  | Reason                                                            |
| -------- | ------- | ----------------------------------------------------------------- |
| `python` | adopted | the library targets Python 3.14 and has zero runtime dependencies |
| `shell`  | adopted | the `.husky/` hooks and the `scripts/` gates are Bash             |

## Adopter Decisions

| Source                 | Decision            | Choice                          | Reason                             |
| ---------------------- | ------------------- | ------------------------------- | ---------------------------------- |
| `python-standards.md`  | boundary validation | standard-library checks         | zero runtime dependencies          |
| `python-standards.md`  | expected failures   | returned `Result` and `Option`  | the library is the mechanism       |
| `python-standards.md`  | union returns       | `Result` and `Option` only      | read with expected failures        |
| `python-standards.md`  | coverage floor      | 100% branch, no exclusion       | measured over `typekit`            |
| `specs/behaviours/`    | scenario corpus     | bound by pytest-bdd             | behaviour is the contract          |
| `repo-config.yml`      | test layers         | unit, integration, end-to-end   | end-to-end uses the built wheel    |
| `pyproject.toml`       | unit hermeticity    | TID251 banned-API lint          | C21: unit tests are hermetic       |
| `.husky/pre-commit`    | formatting          | `format-staged`                 | staged paths only                  |
| `.husky/commit-msg`    | message check       | commitlint                      | Conventional Commits               |
| `.husky/pre-push`      | leak scan           | `public-safety-range` only      | nothing else runs before a push    |
| `repo-config.yml`      | gate families       | seven declared (below)          | the declared families              |
| catalog families       | not adopted         | eight families (below)          | no subject in this Python library  |
| SWE procedures         | kept                | `swe-architect` Design and Lens | a library's design and review      |
| SWE procedures         | kept                | `swe-developer` Build           | test-first build applies           |
| SWE procedures         | kept                | `swe-developer` Apply Findings  | re-validation applies              |
| SWE procedures         | kept                | `swe-reviewer` code checks      | code and test checks apply         |
| SWE procedures         | removed             | no `swe-web-tester` agent       | no web UI; no such agent           |
| `harness-*`, `specs-*` | internal links      | link markup removed             | named skills and maker not adopted |
| SWE procedures         | UI/API paragraphs   | kept, not applied               | no interface in this repository    |

The three test layers are unit (`tests/test_*.py`), integration (`tests/integration/`), and end-to-end (`tests/e2e/`),
which installs the built wheel into a fresh virtual environment. Coverage is measured by coverage.py over the unit run.
The floor is 100 percent branch coverage, and no line, branch, or file is excluded.

The behaviour corpus is `specs/behaviours/*.feature`. pytest-bdd binds it under `tests/`, and
`./rhino behaviour coverage validate` checks the binding. TID251 keeps subprocess, socket, network, temporary-file,
sleep, wall-clock, environment, and random calls out of `tests/test_*.py`.

The declared gate families are plan, docs, rules, harness, ci, pr-review, and specs. The catalog families api-http,
content, pdf-to-md, tutorial-annotated-concept, tutorial-by-example, tutorial-in-the-field, tutorial-primer, and ui-web
are not adopted, because this Python library has no subject for them (no web UI, HTTP API, tutorial content, or PDF
input). Hippo never held them. Their sixteen propagation and quality-gate documents were removed in this commit.

The kept procedure files are `swe-architect-modes.md`, `swe-developer-build.md`, `swe-developer-apply-findings.md`, and
`swe-reviewer-code-checks.md`, indexed by the [SWE Agent Procedures](../../agents/swe-agent-procedures/README.md)
README. The web-tester procedure is deleted, since no `swe-web-tester` agent exists here.

## Skill Names

Adopted `swe-*` agents keep catalog skill names. `swe-releaser` lists `cutting-releases`, which `.agents/skills/` holds.

## Deviations

- **Procedure steps.** The kept files match the catalog text, except that the Evolving Database Schemas, UI Web
  Propagation, and API HTTP Propagation links are plain text, as those are not adopted, and the web tester procedure is
  deleted.
- **Python standard.** No other deviation. Its union rule reads with the expected-failures row.

## Project Applicability

- `typekit`: the library in `src/typekit/`, its unit, integration, and end-to-end tests, and the behaviour corpus.
  Commands are in the root README.
- `scripts/` and `.husky/`: the shell gates. A shell test sits beside its script as `*.test.sh`.

## Version Sources

- `python`: `.python-version` (3.14.7) and `requires-python` in `pyproject.toml`.
- `shell`: the interpreter line of each script.
