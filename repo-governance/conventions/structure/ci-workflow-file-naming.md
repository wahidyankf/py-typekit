---
description: >-
  Requires each GitHub Actions workflow to declare a name and to live in the file whose name derives mechanically, in
  kebab-case, from that declared name.
when_to_use: >-
  Use when adding or renaming a GitHub Actions workflow file, or when changing the name a workflow displays.
---

# CI Workflow File Naming

A GitHub Actions workflow is seen by its `name`: in the Actions tab, in the checks on a pull request, and in run logs. A
reader looking at a failing run needs the file behind it, and should reach it by applying a rule rather than by
searching.

This convention is stack-scoped to GitHub Actions workflow files.

## The Rule

Every workflow file declares `name`. Its filename is that name, derived in this order:

1. Lowercase it.
2. Replace each space with a hyphen.
3. Remove every character that is not a lowercase ASCII letter, a digit, or a hyphen.
4. Collapse each run of hyphens into one, and remove hyphens from both ends.
5. Append the extension the repository uses for every workflow file.

| Declared `name`           | Filename                  |
| ------------------------- | ------------------------- |
| `CI`                      | `ci.yml`                  |
| `Docs and Link Check`     | `docs-and-link-check.yml` |
| `Release - Build (Linux)` | `release-build-linux.yml` |
| `E2E Tests`               | `e2e-tests.yml`           |

The derivation runs from name to filename because only that direction is mechanical: punctuation and capitals are lost
on the way to the filename and cannot be recovered from it. A pair passes when deriving the declared name gives exactly
the filename, path excluded.

`name` is declared rather than left out. Without it, GitHub displays the file path in place of a name — see the
[workflow `name` syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#name) —
and that workflow then reads differently from every named one beside it.

## What the Rule Leaves Open

The words a name uses, their order, any domain-first prefix, and whether the repository keeps a fixed set of workflow
files are the repository's own choices. The rule binds only the correspondence between name and filename, which is why
it holds in any repository while those choices do not.

## Renaming

The declared name and the filename change together, in one change. Changing either alone produces exactly the mismatch
the rule exists to prevent. The same change updates everything that refers to the old file path, such as status badges
and callers of a reusable workflow.

An adopter enforces the rule with its own check in the pull-request gate that derives each file's expected filename from
its declared name and fails on any difference.

## Principles

This convention implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because every workflow
declares the name it displays, and [Automation Over Manual](../../principles/automation-over-manual.md), because the
file behind a run is found by a rule a check can apply.
