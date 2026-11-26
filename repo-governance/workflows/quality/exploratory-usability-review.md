---
name: exploratory-usability-review
description: >-
  Runs one bounded exploratory and usability pass over declared tasks, recording observations, failures, and a terminal
  result. A spec-aware exploratory lens runs before a structurally spec-blind usability lens.
when_to_use: >-
  Use when a user-facing change reaches manual review, after programmatic checks have run.
---

# Exploratory and Usability Review

## Entry

A change with a user-facing surface whose programmatic checks have already run; running this first spends a reviewer's
attention on defects a machine would catch.

- `origin` (`string`, required): the exact address the surface is served from.
- `routes` (`string`, required): the affected routes or screens.
- `viewports` (`string`, optional, default every supported viewport class).

## Sequence

1. **Declare the tasks before starting.** State them as goals in the user's terms, and freeze the list. A task added
   mid-pass is chosen from what was just seen, turning review into a search for confirmation.
2. **Choose a reviewer who did not build it**, where possible: the builder cannot un-know where things are, which is
   exactly what the review must do without.
3. **Attempt each task once**, without hints, without the documentation, and without the author narrating.
4. **Record what happened**, including tasks that went fine; a pass recording only problems cannot tell a flow that
   worked from one nobody tried.
5. **Record failures as behaviour, before explanation.** Stalls, guesses, backtracks, abandonment. "Took 40 seconds to
   find the setting" is a finding; "took a while, but they would learn it" is a defence of one.
6. **Note anything unexpected outside the tasks:** automation structurally cannot, and it is worth more than the
   scripted portion.
7. **Record one terminal result** for the pass.

## Exit

Every declared task carries an outcome, every failure is recorded as behaviour, and the pass has one terminal result.

Both lenses ran in order, each with its own findings section or an explicit none found, and shared root causes are
cross-referenced.

## Two Lenses, in Order

The pass looks through two lenses in a real browser at `origin` across `viewports`, the first finished and recorded
before the second begins. Fetched markup or source inspection is a baseline, never a pass. Steps 3 to 6 run once per
lens, in that order:

1. **Exploratory, spec-aware.** Read the scenarios the change affects, then probe past the scripted cases: edge and
   boundary values, address structure, state transitions, and passive security signals such as an exposed identifier. A
   contradiction is recorded as a finding; proving correctness stays the programmatic layer's.
2. **Usability, spec-blind.** Blindness is structural, not declared. Give this lens to a fresh reviewer or agent context
   holding only `origin`, `routes`, `viewports`, and the frozen task list, never specifications, source, or design
   assets; with none available, label the lens spec-aware. Judge first use by a published heuristic set and a cognitive
   walkthrough, the empty, loading, error, and zero-result states, keyboard and focus, and responsive layout, alongside
   [Usability Probes and Completeness](../../development/quality/manual-verification/008-usability-probes-and-completeness.md).

Findings stay in one section per lens. Two findings sharing a root cause cross-reference each other, so it is fixed
once. Correct behaviour no scenario states becomes a proposed scenario, labelled with its lens, reconciled through
[Behaviour-Driven Development](../../development/quality/testing/behaviour-driven-development.md) as its own delivery
item, and never written into the specification directly.

Both lenses are passive: nothing shared or live is mutated, per
[Live-Service Continuity](../../development/quality/delivery/live-service-continuity.md), identities and data are
isolated per [Test Data Isolation](../../development/quality/testing/test-data-isolation.md), and records name route,
state, category, and result, never a private value.

## Bounded

One pass over the declared tasks. Findings may be repaired within the quality gate's budget and the pass re-run once
against the **same** tasks. That budget belongs to the gate the adopter runs on the surface, such as
[UI Web Quality Gate](ui-web-quality-gate.md) or [API HTTP Quality Gate](api-http-quality-gate.md).

Never re-run against new tasks until it comes back clean: that converges on a clean report, not a usable interface, and
the two are easy to confuse from outside.

## What This Does Not Do

It does not verify correctness; that is the programmatic layer's. It does not check device-specific rendering; that is
its own layer. It does not fix anything it finds.
