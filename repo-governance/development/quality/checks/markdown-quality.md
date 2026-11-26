---
description: >-
  Formats Markdown with one pinned layout formatter and lints it with one pinned structural linter, both reading
  committed configuration, excludes frozen archives, and leaves the rule set to the adopter.
when_to_use: >-
  Use when setting up or changing how Markdown is formatted and linted, or when a Markdown formatting or lint gate
  blocks a change.
---

# Markdown Quality

Markdown in a repository is read by people, by agents, and by tools that parse its structure. It is formatted and linted
automatically, from configuration the repository commits, so the result does not depend on whichever editor last saved a
file.

This standard implements [Automation Over Manual](../../../principles/automation-over-manual.md) and
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md). Where gates run in general is owned by
[Automated Quality Gates](automated-quality-gates.md), and the failure threshold by
[Lint Strictness](lint-strictness.md).

## Two Tools, Two Jobs

| Tool              | Owns                                                            | Illustrative example                                                 |
| ----------------- | --------------------------------------------------------------- | -------------------------------------------------------------------- |
| layout formatter  | layout: wrapping, whitespace, list indentation, table alignment | [Prettier](https://prettier.io/docs/)                                |
| structural linter | structure and syntax: headings, links, fences, list markers     | [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) |

The split keeps each question with one tool. A formatter that also judged structure, or a linter that also rewrote
layout, would give a contributor two answers to one question.

Both read committed configuration files, and both run at a pinned version. Nothing depends on a global install or on
either tool's defaults.

## Where They Run

The formatter runs before every commit on the staged Markdown files and restages what it rewrote, and it runs again in
continuous integration where the repository has it. There, a check mode that fails on a file the formatter would change,
instead of rewriting it, is the usual way to run it.

The linter runs in the pull-request gate, and the link and index checks run there as a global scan, per C7 of
[Test and Gate Contract](test-and-gate-contract.md): moving or deleting one file can break a link or index entry in
another, so the scan cannot be limited to the files a change touches. No hook runs them. A finding of theirs is not
formatting that a hook can rewrite and restage, and a slow hook gets bypassed, while the pull-request gate runs them in
parallel on any machine. A repository without a pull-request gate runs them in its landing gate.

## The Rule Set Is the Adopter's

Which rules are enabled is an adopter decision. A larger set catches more inconsistency and raises more findings in long
documents that are correct as written; a smaller set is quieter and lets more variation through.

Whichever set is chosen, a comment in the configuration giving each disabled rule's reason is good practice. A rule
turned off without a reason is indistinguishable from one nobody evaluated, and the next contributor has to rediscover
why.

## Frozen Archives Are Excluded

Content kept as a historical record, such as completed plans and archived documents, is excluded from both tools. Its
links rot legitimately as the files they named are renamed or removed, and linting it raises findings that block current
work without improving anything.

The exclusion is declared in each tool's ignore configuration, and the two lists agree. Dependencies, build output, and
generated reports are excluded because nobody authors them. Everything else is checked without exception.

An adopter enforces the formatter in its own pre-commit hook and both tools in its pull-request gate.
