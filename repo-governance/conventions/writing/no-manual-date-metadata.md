---
description: >-
  Forbids hand-maintained last-changed dates in Markdown — fields, footers, and annotation lines — because version
  control records them, and names the two exemptions an adopter decides.
when_to_use: >-
  Use when a document is about to gain a date field, footer, or annotation, or when deciding whether a reader-facing
  tree may keep a last-updated value.
---

# No Manual Date Metadata

A Markdown document carries no hand-maintained record of when it last changed. Version control already records that,
exactly and for every edit, and a second record kept by hand is a copy that starts drifting on the next commit.

## What Is Forbidden

| Form                | Example                                                                 |
| ------------------- | ----------------------------------------------------------------------- |
| a frontmatter field | `updated: YYYY-MM-DD`, `last_updated: YYYY-MM-DD`                       |
| a footer            | a closing rule followed by `**Last Updated**: YYYY-MM-DD`               |
| an annotation line  | `- **Last Updated**: YYYY-MM-DD`, including inside a "Document History" |
| a version-date line | `**Version**: 1.2 — YYYY-MM-DD`                                         |

Position does not matter: mid-document or at the end, it is the same defect.

## Why It Is Forbidden

- **It drifts.** Nothing reminds anyone to update it, and the first forgotten bump makes it silently wrong.
- **It misleads.** A stale date says the content is old when the file may simply not have needed changing.
- **It duplicates.** `git log --follow -1 --format=%cs -- <path>` gives the date, with the author and reason beside it.
- **It creates review noise.** Checking the field against history yields mismatches that cost a fix cycle and improve
  nothing.

The field is a second copy of a fact history already owns — see
[One Source Per Fact](../../principles/one-source-per-fact.md).

## What Is Not Metadata

A date that is part of the content is unaffected: a changelog release heading, an incident timeline, the date a decision
was accepted, or a sentence saying when something happened. Those record events, not maintenance, and never change on
the next edit.

Governed documents under a metadata schema carry no date key at all, because their schema admits none — see
[Schemas by Path](../structure/artifact-metadata/001-schemas-by-path.md). The decisions below concern Markdown outside
such a schema.

## Two Adopter Decisions

Two neighbouring cases are the adopter's to decide, each once, for a named path, never file by file.

### A Set-Once Creation Date

| Option | Gains                                                                                         | Costs                                                                                 |
| ------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| forbid | one rule with no exception; `git log --follow --diff-filter=A -- <path>` answers the question | history is harder to read after renames, imports, or squashed merges                  |
| permit | a first-added date that survives history rewrites and imports, readable without tooling       | a date key invites a second one, and a copied file silently carries its source's date |

A permitted creation date is written once, when the file is created, and never edited. Corrected by hand, it has become
the field this convention forbids.

### A Reader-Facing Tree That Shows Freshness

Some trees are read where history is invisible — a published site, or a notes application that lists and sorts by a
last-updated value — and there the date is part of what the reader sees.

| Option                                   | Gains                                                     | Costs                                                                          |
| ---------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------ |
| exempt the tree with a required field    | readers see freshness where they read, with no build step | it drifts like any hand-kept date unless a check compares it with history      |
| keep the ban; derive the date when built | no drift and nothing to maintain                          | needs a build step and full history; a shallow clone dates every file the same |

An exempt tree is declared by path, and the field is then required there rather than merely allowed, so a check can tell
a missing date from a forbidden one.

## Removing Existing Dates

Forbidden date metadata is removed as part of whatever edit next touches the file, without deferring and without
replacement text. A footer's separator rule goes with it only when the rule exists solely for the footer — never the
frontmatter's closing delimiter or a section rule in the body.

## Enforcement

An adopter enforces this with its own check in its own gate: refuse forbidden keys, footers, and annotation lines
outside declared exempt trees, and require the field inside them.
