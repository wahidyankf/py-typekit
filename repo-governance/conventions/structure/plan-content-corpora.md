---
description: >-
  Gives each content corpus a plan authors in its own folder exactly one custodian plan, a declared destination,
  read-only consumers, and an archival hand-off that leaves no broken link.
when_to_use: >-
  Use when a formal plan writes or restructures a body of content inside its folder, or when another plan reads one.
---

# Plan Content Corpora

Some plans produce content: lessons, a glossary, a question bank, a reference set other plans read. Written inside the
plan folder, such a corpus breaks the assumption that only its own plan reads a plan folder. This convention adds to the
[Plans Convention](plans.md) and fixes who changes a corpus, where it ends up, and what its readers face when its plan
closes.

## When It Applies

A plan triggers this convention when its delivery authors a content corpus inside its own folder, or restructures one
there by adding, splitting, merging, renaming, or reordering its documents. Reading a corpus, linking to it, or fixing a
typo does not. A corpus is a directory of documents meant to be read as a set by someone other than the plan's executor.

## One Custodian

Exactly one plan is the custodian: the plan whose folder holds the corpus. The corpus `README.md` names its custodian by
slug, which survives the move to `done/` where a path would not.

Any other plan reading the corpus is a consumer and records the custodian in its technical documentation, beside the
paths it reads, so its reader knows whose change can break it.

Consumers are read-only: a consumer never edits, copies, or forks a corpus file, and a consumer delivery item that
writes into the corpus is a defect. A needed change is an item in the custodian's `delivery.md`. Two plans editing one
corpus produce two delivery records for one set of files, and neither record's proof covers the other's changes.

## A Declared Destination

The custodian plan declares one destination in its technical documentation, apart from the custodian line in the corpus
`README.md`; a consumer plan never declares one. The default, `archive-with-plan`, moves the corpus to `done/` with its
custodian. `promote-to:<path>` moves it to a permanent home outside `plans/`, and replaces the default as soon as a
named reader outside plans exists, including one that appears later.

The named reader is required because a permanent home that nothing outside plans reads is a home nobody maintains.
Promotion is not a rename but a custodian delivery item: move the corpus to `<path>`, rewrite every inbound link, and
prove the link check passes.

## Hand-Off at Archival

For a corpus not yet promoted, the custodian settles it before the first step of
[archival](plans/008-knowledge-capture-and-archival.md), by the state of its consumers:

| Consumers                                  | Hand-off                                                                                                                          |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| none live                                  | the corpus moves with the plan                                                                                                    |
| live, and the corpus is stable             | the corpus moves with the plan, and every consumer's inbound link is rewritten to the archived path                               |
| live, and at least one still needs changes | custody transfers: a successor plan becomes custodian, the corpus moves into its folder, and every record names the new custodian |

A plan under `done/` is never edited again, so a corpus still changing cannot archive with it; the transfer keeps one
custodian at every moment.

An adopter runs its own link check over live plans in the pull-request gate, excluding archived plans as scan sources
but not as link targets, so a link a missed hand-off left behind fails. It cannot see a missing custodian line, which a
structure check or review enforces.

## No Successor Authorized

A transfer needs a successor plan, and a plan is written only on its owner's
[explicit request](plans/010-authorization-and-execution-record.md). When a corpus still needs changes and no successor
was requested, archival waits until a successor is authorized or no consumer still needs changes. Those are the only
exits: a finished plan stays unarchived while it waits, but one custodian and every pending change survive.

## Principles

This convention implements [One Source Per Fact](../../principles/one-source-per-fact.md), because one custodian at a
time owns every change to a corpus, and [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because a
corpus declares its destination instead of leaving it to whoever archives the plan.
