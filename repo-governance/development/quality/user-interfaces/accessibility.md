---
description: >-
  Fixes web interface accessibility beyond the principle's floor: interface contrast, focus, keyboard operation, labels,
  target sizes, motion, announcements, component roles, and a release check.
when_to_use: >-
  Use when building or reviewing a web interface component, form, animation, or page layout, or before releasing a
  user-facing web change.
---

# Accessibility

[Accessibility First](../../../principles/accessibility-first.md) fixes what every artifact owes its readers: meaning
never carried by colour alone, text alternatives, real structure, operation without a pointer, and a contrast floor.
This standard applies it to web interfaces, where most failures are interactive.

It also implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md) and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Modules

1. [Focus and Keyboard](accessibility/001-focus-and-keyboard.md)
2. [Forms and Targets](accessibility/002-forms-and-targets.md)
3. [Content, Motion, and Announcements](accessibility/003-content-motion-and-announcements.md)
4. [Component Roles and Keys](accessibility/004-component-roles-and-keys.md)
5. [Release Check](accessibility/005-release-check.md)

## Scope and Target

Every interface an application ships to a browser: pages, components, dialogs, forms, and the motion and notifications
inside them. The conformance target is [WCAG 2.2](https://www.w3.org/TR/WCAG22/) Level AA, which includes every Level A
criterion. An adopter whose stated baseline is higher uses that baseline instead.

It is built in from the first version. An inaccessible component is not a nearly finished accessible one, and undoing it
later costs everything built on top of it.

## Contrast Covers the Whole Interface

The principle's floor covers text. In an interface it also covers every visual element a user needs to perceive:

| Element                                              | Minimum contrast against adjacent colours |
| ---------------------------------------------------- | ----------------------------------------- |
| normal text                                          | 4.5:1                                     |
| large text, at least 18 point or 14 point bold       | 3:1                                       |
| input borders, icons, and other component boundaries | 3:1                                       |
| focus indicators                                     | 3:1                                       |
| graphical objects that convey meaning                | 3:1                                       |

Contrast is verified for every colour combination a change introduces, in every theme the interface offers: a pair that
passes in a light theme can fail in a dark one. Interface colours come from [Design Tokens](design-tokens.md), which is
what makes that verification systematic rather than per component.

## Native Before ARIA

Use the native element that already carries the semantics, such as a button, a link, a navigation region, a heading, a
list, or a form control, before giving a generic element a role. A native element brings keyboard behaviour and an
accessible name with it. A generic element with a role has to reproduce all of that by hand, and usually misses some.

## Enforcement

Automated rules for missing names, missing labels, invalid attributes, and the contrast of declared colours run in the
adopter's own lint and test gates. Automation catches only part of what fails in real use, which is why the
[Release Check](accessibility/005-release-check.md) adds a manual pass it cannot replace.
