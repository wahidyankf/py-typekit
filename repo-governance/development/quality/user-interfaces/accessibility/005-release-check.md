---
description: >-
  Requires an automated accessibility audit and a manual keyboard, screen reader, and 200 and 400 percent zoom pass
  before a user-facing web change is released, each recorded as evidence.
when_to_use: >-
  Use before releasing any change to a web interface, or when recording accessibility evidence for one.
---

# Release Check

Automated audits find the mechanical failures, and only those. Whether a focus order makes sense, whether an
announcement is intelligible, and whether a layout survives enlargement appear only when someone uses the interface the
way the affected readers do.

## Automated Audit

Run an automated accessibility engine, such as axe, against every changed page and component state in the adopter's own
test gate, and resolve every violation it reports. A write-time lint rule for markup accessibility catches the same
classes of failure earlier and runs alongside it.

## Manual Pass

Before release, a person completes each of these on the changed surface:

1. **Keyboard only.** With no pointer, move through every interactive element. Confirm that every action is reachable,
   the order follows reading order, focus is always visible, and nothing traps focus outside a modal dialog.
2. **Screen reader.** Operate the changed flow with at least one screen reader on a platform the adopter declares.
   Confirm names, roles, states, and announcements.
3. **Zoom.** View the changed pages at 200 percent browser zoom. Confirm that text and controls stay readable and
   usable, with no content or function lost. Then view them at 400 percent and confirm that the content reflows without
   scrolling in two directions, as [WCAG 2.2 Success Criterion 1.4.10](https://www.w3.org/TR/WCAG22/#reflow) sets out.

## Evidence

Each step is a separate assertion with its procedure, expected observation, failure signal, and evidence, as
[Verification Layers](../../manual-verification/002-verification-layers.md) requires. The automated audit is
programmatic evidence and the manual pass is dispositioned separately from it; neither stands in for the other. Captures
follow [Evidence Safety and Accessibility](../../manual-verification/005-evidence-safety.md).

A change with no web interface surface records this check as not applicable, with a reason.
