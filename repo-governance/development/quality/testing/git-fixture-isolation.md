---
description: >-
  Requires every test that creates or changes a throwaway git repository to apply six independent isolation layers, so
  no git command a test runs can reach the enclosing real repository.
when_to_use: >-
  Use when writing or reviewing a test, fixture, or helper that runs git to create or modify a temporary repository, or
  after a test run has changed a real repository.
---

# Git Fixture Isolation

A git command finds its repository by searching upward from where it runs. A test that builds a temporary repository can
therefore commit, reset, or switch branches in the real checkout around it when one setup step silently fails, and every
exit code still reads success.

This standard implements [Fail Closed](../../../principles/fail-closed.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Reproducibility](../../../principles/reproducibility.md), and
[Root Cause Orientation](../../../principles/root-cause-orientation.md).

## Scope

In scope: any test, fixture, or helper, in any language, that invokes git to build or change a disposable repository.

Out of scope: read-only git queries against the real repository, production code whose purpose is to act on the real
repository, how tests are classified into layers, and environment hazards unrelated to git.

## Six Layers, All Required

No layer is sufficient alone, because each covers a failure the others miss. Every git invocation that can write gets
all six.

| Layer                                | Requirement                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 1. Cap discovery                     | set `GIT_CEILING_DIRECTORIES` to the fixture's temporary root, so upward search stops at that root and never climbs past it     |
| 2. Name the repository               | set `GIT_DIR` to the fixture's own `.git` directory instead of trusting the process working directory                           |
| 3. Neutralize configuration          | set `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM` to the platform null device, so host hooks, templates, and aliases never apply  |
| 4. Guard before writing              | before each writing subcommand, compare canonical `git rev-parse --show-toplevel` with the intended directory; fail on mismatch |
| 5. Check every exit status           | treat a non-zero status from any git call as a test failure; a process that started is not a command that succeeded             |
| 6. Diagnose away from real checkouts | investigate a misbehaving fixture only in a throwaway clone, never in the primary checkout                                      |

## Why Each Layer Exists

| Escape route                                                        | Stopped by |
| ------------------------------------------------------------------- | ---------- |
| fixture setup failed, so git searched upward into the real checkout | 1, 2, 4    |
| the working directory was wrong, or an earlier step changed it      | 2, 4       |
| host configuration changed behaviour, such as a hook that commits   | 3          |
| a failed `git init` went unnoticed and later commands ran elsewhere | 4, 5       |
| a command succeeded against the wrong repository                    | 4          |
| a person debugging the fixture repeated the escape by hand          | 6          |

Layer 4 exists because layer 5 cannot see the worst case: a commit to the wrong repository exits zero.

## Details That Defeat the Guard

- Leave `GIT_WORK_TREE` unset wherever the guard runs. When it is set, `--show-toplevel` reports that variable back
  instead of discovering anything, so the comparison passes whatever the truth is. It must also be absent for
  `git worktree add`.
- Canonicalize both paths before comparing. Temporary directories often sit behind symbolic links, and a raw string
  comparison then rejects a correct fixture or accepts a wrong one.
- Add the isolation variables to the inherited environment. Replacing the environment wholesale drops `PATH` and similar
  variables, and the resulting failures get misread as fixture defects.
- Remove the fixture root in guaranteed teardown, as [Test Data Isolation](test-data-isolation.md) requires of every
  resource a run owns.

## Enforcement

The adopter enforces the layers in its own gate or CI: a checker locates git subprocess calls in test code and confirms
each layer is present. A missing layer is a CRITICAL finding under
[Criticality Levels](../evidence/finding-criticality-and-confidence/001-criticality-levels.md), because the failure it
permits damages a real repository rather than a test result.
