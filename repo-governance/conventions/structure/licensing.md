---
description: >-
  Requires one explicit licensing model at the repository root, preserved third-party terms, documented exceptions, and
  a recorded compliance decision for every dependency outside the permissive set.
when_to_use: >-
  Use when vendoring code, adding a directory, taking on a dependency with a copyleft or restricted license, or auditing
  licensing.
---

# Licensing

Anyone holding a file needs to know what they may do with it, without asking. That answer is reliable only when it is
stated once at the root and every exception is stated beside the thing it excepts.

## Modules

1. [Repository Licensing](licensing/001-repository-licensing.md) — the root model, third-party terms, exceptions, and
   where license files live.
2. [Dependency-License Decisions](licensing/002-dependency-license-decisions.md) — recording and re-auditing a decision
   for each dependency whose license needs one.

Read in order: the second assumes the root model the first establishes, because a dependency's license is judged against
it.

## Scope

In scope: the terms under which a repository's own content is offered, the terms carried by code it vendors, and the
compatibility of its dependencies' licenses with how it uses them.

Out of scope: contributor agreements, patent and trademark policy, and legal advice. A decision recorded under this
convention is a reviewable reasoning trail, not a legal opinion.

## Principles

This convention implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because a repository's
terms are stated rather than left to silence or a tool's default.
