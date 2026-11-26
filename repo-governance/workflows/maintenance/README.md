---
name: maintenance
description: >-
  Indexes the workflows that keep a repository clean, current, and releasable: artifact clean-up, dependency bumps,
  release cuts, and rules grooming.
when_to_use: >-
  Use after finishing a task, plan, or investigation that created scratch files, branches, or worktrees, when planning
  dependency bumps or a release, or when sweeping rules for reductions.
---

# Maintenance Workflows

Work produces debris: scratch files, reports, branches, worktrees, generated output. None of it is a mistake while the
work is happening. All of it is a mistake once the work is done.

A repository also drifts while nobody works in it: dependencies age, releases wait, and rules pile up copies. The rest
of these workflows keep it current, releasable, and governed by rules written in one place. The propagations that write
rules and documents sit in [`quality/`](../quality/README.md), beside the gates that judge them.

## Directory Map

- [Dev Artifact Clean-Up](dev-artifact-clean-up.md)
- [Dev Artifact Clean-Up Modules](dev-artifact-clean-up/README.md)
- [Dependency Bump Planning](dependency-bump-planning.md)
- [Release Cut](release-cut.md)
- [Rules Grooming](rules-grooming.md)
