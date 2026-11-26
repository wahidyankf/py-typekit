---
description: >-
  Sets what a user-facing plan states before execution: a visual-parity step with evidence, named design-system
  primitives, per-viewport deliverables, exhaustive filter scenarios, value-bearing assertions, labels, and token roles.
when_to_use: >-
  Use when writing or reviewing the checklist and acceptance criteria of a plan that changes a user-facing surface.
---

# Authoring a User-Facing Plan

Each rule below is settled while the plan is written. A plan silent on one leaves the choice to whoever executes it,
under time pressure, where the cheapest option is usually the one that ships the defect.

## 1. A Visual-Parity Step With Evidence

A plan that ships an interface carries an explicit checklist step comparing the rendered interface with each approved
design, for every declared viewport class and every supported locale. The step saves its captures as plan evidence and
cites them, as [Evidence Files](../../../../conventions/structure/plans/016-evidence-files.md) sets out. A parity step
with no cited capture is not signed off.

Automated tests assert that elements exist and respond. None of them looks at the composition a user sees.

## 2. Name the Design-System Primitive

Where a design shows an element the design system already provides, such as tabs, a badge, a segmented control, or a
card, the checklist step names that primitive and asserts that the build uses it.

An unnamed primitive tends to be rebuilt by hand from generic elements, which loses the primitive's styling, its
keyboard behaviour, and its roles. [Accessibility](../accessibility.md) explains why native semantics are hard to
reproduce.

## 3. Every Viewport Design Is Its Own Deliverable

Each viewport-specific design, such as a mobile or a tablet layout, gets its own test-first step and a viewport-specific
assertion. Layout for a narrow viewport is built deliberately, not left as an adjustment after the wide view works.

One technique computes the data once and renders a distinct view per viewport class, such as a table for wide viewports
and stacked cards for narrow ones. Test identifiers then stay on a single view, so each assertion has one target.

## 4. Filter Scenarios Cover Every Level

For a cascading filter or scope, such as region, then country, then city, the plan's scenarios set each level on its own
and each meaningful combination, not only the complete cascade. A level never tested alone is where a filter gets
silently ignored. The scenarios follow [Behaviour-Driven Development](../../testing/behaviour-driven-development.md).

## 5. Assertions Carry Values

A feature that orders, ranks, or splits by a threshold is tested with assertions on concrete positions and identities:
which item falls above the threshold and which below. An assertion that a divider exists, or that some rows are dimmed,
holds under both the correct logic and its inversion.

Choose fixture inputs that genuinely produce the split, probing the data while writing the plan. A fixture that
satisfies the threshold trivially never exercises it. Write each test so it fails when the logic is inverted.
[End-to-End Testing](../../testing/end-to-end-testing.md) requires an assertion to observe what the action produced;
this rule adds that it must also tell a correct result from a wrong one.

## 6. Every Displayed Figure Is Labelled

A plan that presents computed figures requires, in its acceptance criteria, a visible label or legend for each one. A
bare number makes its reader guess what it measures. Units on numeric inputs are covered separately by
[Usability Probes and Completeness](../../manual-verification/008-usability-probes-and-completeness.md).

## 7. Design Colours Are Token Roles

Colours in a plan's designs are annotated with the token role each one represents, such as primary or destructive, never
as a raw swatch. The delivery step maps each role onto the target application's brand tokens.

A raw colour copied from a generic design lands off-brand and can attach the wrong meaning to a state.
[Design Tokens](../design-tokens.md) requires components to refer to colours by role; this rule applies the same
discipline to the plan's designs, before any component exists.
