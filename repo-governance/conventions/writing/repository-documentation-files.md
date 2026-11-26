---
description: >-
  Fixes the standard repository documentation files — README, contributing guide, code of conduct, security policy,
  license, changelog — and immutable architecture decision records.
when_to_use: >-
  Use when setting up a repository's top-level documentation, or when writing a contributing guide, security policy,
  changelog, or architecture decision record.
---

# Repository Documentation Files

A repository's standard documentation files are its interface with everyone outside it: people evaluating it, using it,
contributing to it, or reporting a vulnerability in it. Each file answers one audience's question, in the place that
audience already looks.

| File                 | Location                          | Answers                             |
| -------------------- | --------------------------------- | ----------------------------------- |
| `README.md`          | root                              | what is this, and how do I start    |
| `CONTRIBUTING.md`    | root                              | how do I contribute                 |
| `CODE_OF_CONDUCT.md` | root                              | how do people here treat each other |
| `SECURITY.md`        | root                              | how do I report a vulnerability     |
| `LICENSE`            | root                              | may I use this                      |
| `CHANGELOG.md`       | root, once releases are versioned | what changed in each release        |
| decision records     | `docs/explanation/decisions/`     | why is it built this way            |

Decision records sit where the adopter's `ADR location` decision places them; the path above is its default.

What a README contains, and how it reads, is owned entirely by [README Quality](readme-quality.md). This convention
requires only that a root README exists.

## Modules

1. [Contributing and Conduct](repository-documentation-files/001-contributing-and-conduct.md)
2. [Security, License, and Changelog](repository-documentation-files/002-security-license-and-changelog.md)
3. [Architecture Decision Records](repository-documentation-files/003-architecture-decision-records.md)

## Why Fixed Names and Places

Hosting platforms, package registries, and readers all look for these files by name, at the root first. A security
policy under another name, or deep in a documentation tree, is one a researcher does not find, and the report that
should have been private arrives as a public issue.

## Scope

In scope: the files above, what each must contain, and how decision records are stored and change status.

Out of scope: product documentation, API reference, deployment guides, and internal development conventions. Each has a
home of its own and is linked from these files rather than folded into them.

## Keeping Them Current

| File              | Changes when                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| `README.md`       | a feature, command, or example it shows changes                            |
| `CONTRIBUTING.md` | setup, process, review expectations, or response times change              |
| `SECURITY.md`     | supported versions, the reporting channel, or the response process changes |
| `CHANGELOG.md`    | a change a user would notice is merged                                     |
| decision records  | never in substance — a changed decision is a new record                    |

The file changes in the same change as the thing it describes. A contributing guide that describes an old setup costs
every new contributor the time it takes to discover that.

## Enforcement

An adopter enforces the presence of these files and the integrity of their links with its own checks in its own gate — a
required-files check and a link checker — and leaves their content to review.
