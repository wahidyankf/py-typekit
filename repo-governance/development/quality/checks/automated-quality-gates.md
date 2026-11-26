---
description: >-
  Assigns each kind of automated quality check to its gate surface: staged-file formatting before a commit, the message
  at commit time, the leak scan before a push, every other check in the pull-request gate, and end-to-end on main.
when_to_use: >-
  Use when wiring a check into a hook or pipeline, deciding which surface a check belongs on, or when a gate is slow,
  scans too much, or cannot fail.
---

# Automated Quality Gates

A quality rule a contributor must remember is enforced only on the days they remember it, so every mechanical check runs
by itself and blocks.

This standard implements [Automation Over Manual](../../../principles/automation-over-manual.md) and
[Fail Closed](../../../principles/fail-closed.md). What a surface is, and which gates may change files, is owned by
[Surfaces and Mutation](../../../conventions/structure/repository-configuration/003-surfaces-and-mutation.md); this
standard decides what belongs on each surface, as rule C6 of the
[Test and Gate Contract](test-and-gate-contract/002-surface-placement.md) states it.

## Where Each Check Runs

| Surface                | Runs                                                                  | Never runs                        |
| ---------------------- | --------------------------------------------------------------------- | --------------------------------- |
| before a commit        | formatters that rewrite and restage staged files                      | any check, test, or scan          |
| at commit-message time | validation of the message against the repository's commit format      | anything about file contents      |
| before a push          | the deterministic leak scanner over the pushed range                  | tests, lint, or document checks   |
| pull request           | every other blocking check, end-to-end excepted, hook checks replayed | a step whose failure is discarded |
| main or scheduled      | end-to-end suites                                                     | a layer nothing else runs         |

The table is the default. A repository may declare, in its gate registry, which entries each local surface holds, and
its wiring check refuses any other.

## Hooks Stay Thin

Only three kinds of work must run on the author's machine: a rewrite of files, which a hosted job cannot make; the
message lint, because a bad message found at the pull request forces rewriting pushed history; and the leak scan, which
must finish before history leaves the machine.

Everything else, tests and lint included, runs in the pull-request gate rather than before a push. Work there can be
dispatched from any machine, spreads over runners, and runs in parallel per project and per level; work in a hook runs
serially on one machine before anyone can look at the change, and a slow hook gets bypassed.

A repository with no pull-request gate keeps the same hooks and runs its registry's pull-request surface locally over
the change before landing or pushing, recording the result.

## Staged, Not the Whole Tree

A formatter before a commit rewrites only what is being committed. Formatting the entire tree on every commit is slow
enough to resent, and rewrites and stages untouched files, so the commit carries changes nobody reviewed.

A formatter that rewrites a staged file restages it, so the commit holds the formatted version rather than needing a
follow-up fix. The pull-request gate replays each formatter in verify-clean mode.

## Scope by Dependence

A pull-request check may run over only the affected projects when its result cannot change because of edits outside
them; otherwise it runs over the whole tree. Links, anchors, indexes, and registry wiring are global, because a deletion
in one project can break another. The classification is in
[Pull-Request Scope](test-and-gate-contract/003-pull-request-scope.md).

## The Pipeline Fails the Build

The pull-request gate runs the complete blocking set and a violation fails the run. It is the one control a contributor
cannot skip locally, so it is a superset of the hooks, never a subset.

A step written so it cannot fail, its exit status discarded or its tool told to succeed regardless, is not a gate: it
reports green over exactly the state it exists to catch.

## Hooks Travel With the Repository

Hook definitions are committed and installed by the documented setup step, so every contributor and every fresh checkout
runs the same gates. Hooks dispatch the repository's declared gate list rather than transcribing it — see
[Gate Entries](../../../conventions/structure/repository-configuration/002-gate-entries.md).

## Decided Elsewhere

- Each gate returns one terminal result against a frozen snapshot:
  [Quality Gate Results](../manual-verification/001-quality-gate-results.md).
- The severity at which a linter fails, and how a lint gate is introduced: [Lint Strictness](lint-strictness.md).
- A gate that was already failing before a change:
  [Preexisting Error Resolution](../evidence/preexisting-error-resolution.md).
- Which formatter and linter a stack uses belongs to that stack's own standard.

An adopter enforces this in its own hooks and pipeline configuration.
