---
description: >-
  Requires functions whose phases are visibly separated, names chosen for what they mean to a caller, and comments that
  record intent and non-obvious decisions rather than narrate syntax.
when_to_use: >-
  Use when writing or reviewing executable source, tests, or scripts, or when deciding whether a comment earns its
  place.
---

# Code Clarity

Code is read most carefully when something has gone wrong, by someone who did not write it and cannot ask. Every rule
here serves that reader.

This standard implements [Documentation First](../../../principles/documentation-first.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md).

## Separate the Phases

Setup, validation, decision, mutation, and return are separated with blank lines, so a function's shape is visible
before any statement is read.

A formatter does not do this. It decides where lines break, not which statements belong together, and a fully formatted
function can still be one undifferentiated block. The boundary a reader chasing a failure looks for first is where
validation ended and mutation began.

A function whose phases cannot be separated is usually doing two jobs, and splitting it is the fix.

## Name for the Caller

A name says what a thing means to whoever calls it, not how it is implemented. A validator is named for the rule it
enforces, because that word appears in the finding, in the configuration, and in the document a maintainer opens when
the finding appears.

Choose the name a caller would search for, then keep it. An exported name belongs to the
[Public Contract](../architecture/public-contract.md), and a rename for taste costs every consumer while buying nothing.

## Comment Intent, Not Syntax

Executable source, tests, and scripts carry brief comments a reader needs to reconstruct the reasoning. Explain why the
code is needed or shaped this way, not what the code already shows. Comment:

- the intent and boundary of a module, function, or test, where its name alone does not state them;
- why a non-trivial flow separates or orders its stages and data transformations;
- invariants, safety and correctness checks, lifecycle boundaries, and failure behaviour;
- why a dependency is injected, substituted, cached, or deliberately avoided;
- a decision whose alternative looks equally reasonable, and an ordering that matters for a reason the code cannot show;
- non-obvious behaviour of a shell construct, a regular expression, a parser, or a library; and
- a workaround, naming what it works around so the next reader can tell whether it is still needed.

A deliberate simplification that accepts a known ceiling names the ceiling and the path past it, as
[Scope of a Change](../../../principles/minimal-sufficiency/001-scope-of-a-change.md) requires.

Place a comment immediately before the decision it explains, where a maintainer changing that line will see it.

## What a Comment Must Not Do

It must not narrate. A comment restating the statement beneath it is a second thing to keep true, and the first to
become false when the statement changes.

It must not repeat what a precise name already says, and it must not label ordinary simple code as a compromise.

A stale comment is a defect, corrected in the change that made it stale. Configuration, generated output, lockfiles, and
plain data stay free of explanatory comments unless their format supports comments and a reader genuinely needs one.

## Prefer the Expected Shape

Given two correct shapes, take the one a reader expects over the one that is shorter. Brevity that forces a reader to
simulate the code in their head is paid for on every read, and most reads happen under pressure.

## Enforcement

A linter can require a summary sentence on named or exported declarations and a stated reason on every suppression. An
adopter enforces that minimum in its own lint gate.

The check establishes shape, not quality. It cannot tell whether a summary is true, useful, or current, or whether a
private helper's reasoning deserved explaining. Review of the surrounding flow stays required, and a passing linter
never replaces it.
