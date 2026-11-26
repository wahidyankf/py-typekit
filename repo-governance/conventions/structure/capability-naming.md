---
description: >-
  Fixes a scope-first grammar for agent and workflow names, whose final token names the agent's role or the workflow's
  procedure type, and leaves each vocabulary to the adopter.
when_to_use: >-
  Use when naming a new agent or workflow, or when deciding whether to close a repository's role or type vocabulary.
---

# Capability Naming

A listing of agents or workflows is read to find the ones for a concern and to tell what each does before opening it.
Names built to one grammar make both possible from the listing alone.

## The Grammar

| Artifact | Name shape                      | Example                  |
| -------- | ------------------------------- | ------------------------ |
| agent    | `<scope>(-<qualifier>)*-<role>` | `docs-link-checker`      |
| workflow | `<scope>(-<qualifier>)*-<type>` | `release-notes-planning` |

- **Scope** comes first and names the concern — the part of the repository or the domain the capability works on.
- **Qualifiers** narrow the scope, most general first. There may be none.
- **Role** or **type** comes last: what the agent is, such as `maker` or `checker`, or what kind of procedure the
  workflow runs, such as `execution` or `quality-gate`. A role or type may itself be a hyphenated entry.
- Every token is lowercase ASCII letters. Underscores are not used, and capability names deliberately exclude the digits
  the metadata naming rule would otherwise permit.

Scope first makes a sorted listing group by concern, so thirty agents read as a handful of families. The role or type
comes last because it is the part a reader scans for when choosing between members of one family.

The grammar is an adopter's choice for the names it creates once adopted; adopting it does not rename artifacts already
released under other names. Skills are outside the grammar.

The name still matches the path identity, as [Schemas by Path](artifact-metadata/001-schemas-by-path.md) requires; this
convention decides what that identity says. Index files and the modules of a companion directory are not capability
names and follow [File Naming](file-naming.md).

## Decide Whether the Vocabularies Are Closed

The scope, role, and type vocabularies can each be closed or open, and a repository records which.

| Vocabulary                   | Gains                                                                                                                                                | Costs                                                                                                                                                 |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| closed: declared and checked | a name alone says what the artifact does, a misspelled or invented token is caught, and routing, permissions, or reports that read it can rely on it | every new kind of agent or procedure needs a vocabulary amendment first, names bend to fit the list, and a check on a token nothing reads buys little |
| open: grammar only           | a new kind needs no amendment, and no rename follows from a check that prevents no defect                                                            | two names may use different words for one role, and nothing mechanical checks meaning                                                                 |

A closed vocabulary lives in one place, with a one-line meaning for each entry, and is amended before the first name
that uses a new entry. A type is also a claim about behaviour: a workflow typed as a quality gate that does not return
one terminal verdict within a bounded repair budget is misnamed, whatever the validator says — see
[Quality Gate Results](../../development/quality/manual-verification/001-quality-gate-results.md).

## Display Attributes Stay in the Adapter

A harness may show a colour or icon per role. That binding is adapter detail, like the other harness-specific values in
[Portable Capabilities](artifact-metadata/004-portable-capabilities.md). It never becomes part of the name rule or of
canonical metadata.

## Renaming

A rename changes the path, the `name` field, the title, and every live reference in the same change. A harness routes by
name, so one reference left behind fails at invocation rather than at review.

Where the grammar or a closed vocabulary is adopted, the adopter enforces it with its own name check in the pull-request
gate, reading the vocabularies from their one declared place.

## Principles

This convention implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because a name states
what its artifact does, and [One Source Per Fact](../../principles/one-source-per-fact.md), because a closed vocabulary
is declared in one place.
