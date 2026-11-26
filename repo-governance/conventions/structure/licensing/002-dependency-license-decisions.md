---
description: >-
  Requires a recorded, reasoned compliance decision for each dependency under a copyleft, source-available, or
  restricted license, re-audited on a schedule and at major upgrades.
when_to_use: >-
  Use when adding or upgrading a dependency whose license is outside the permissive set, or when running a license
  audit.
---

# Dependency-License Decisions

A dependency's license constrains how a repository may use, modify, and distribute it, judged against the root model in
[Repository Licensing](001-repository-licensing.md). Most dependencies need no thought. The rest need a decision someone
can check later.

## Which Dependencies Need a Decision

A dependency under a license on the repository's permissive allowlist needs no record. Every other dependency needs one:

| License family   | Typical concern                                                         |
| ---------------- | ----------------------------------------------------------------------- |
| copyleft         | obligations triggered by modification, linking mode, or distribution    |
| source-available | use restrictions, often time-limited, and no recognition as open source |
| restricted       | field-of-use, commercial, or network-use conditions                     |

A license change also needs a decision, even when the dependency was previously permissive.

## What a Decision Records

Each record states:

1. the dependency and the license, by its standard identifier;
2. the concern that license raises;
3. how the repository uses it — linked dynamically or statically, loaded at runtime, modified, bundled, or distributed;
4. the decision; and
5. the reasoning, with links to the license text and any authoritative interpretation relied on.

A dual-licensed dependency records which license the repository elects, and why. A dependency approved only for a
particular use says what use would require a new decision.

Usage is the heart of the record. The same license is compatible or not depending on how the code is linked and shipped,
and a decision that omits usage cannot be rechecked when usage changes.

## Keeping Decisions True

- **On a schedule.** An audit reviews dependencies added since the last one and upgrades that may have changed license.
  It records its outcome even when nothing changed, because an unrecorded audit cannot be told apart from a skipped one.
- **At every major upgrade** of a recorded dependency, before the upgrade lands. Licenses change at versions.
- **For delayed conversions.** A license that converts to open-source terms after a period records the conversion date
  for each version in use, and the record is updated when the date passes.

## What an Adopter Decides

| Decision                 | Trade-off                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| the permissive allowlist | a short list sends more licenses to review; a long one lets an unusual clause through unrecorded            |
| the audit cadence        | frequent audits catch a license change early and cost attention each time; rare ones leave it in use longer |

An adopter enforces this with its own dependency-license check in CI, failing on any license outside the allowlist that
has no decision record.
