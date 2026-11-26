---
description: >-
  Requires a visible associated label on every form control, programmatic error and required states, declared input
  purpose, and interactive targets of at least 24 by 24 pixels, or 44 by 44 on declared mobile viewports.
when_to_use: >-
  Use when building a form, an input, a validation message, or any small interactive control such as an icon button.
---

# Forms and Targets

## Every Control Has a Visible Label

Every input, select, and text area has a visible label programmatically associated with it, by reference or by wrapping.
A placeholder is not a label: it vanishes as soon as someone types, and its usual contrast is too low for many readers.

An icon-only control has an accessible name that describes its action, and the icon itself is hidden from assistive
technology.

## Errors and Required States Are Programmatic

- A validation message is associated with its input, so a screen reader announces it with the field.
- An input is marked invalid only once validation has run and failed, never before the user has had a chance to answer.
- A message that appears without a page load is announced, as
  [Content, Motion, and Announcements](003-content-motion-and-announcements.md) requires.
- A required field exposes its required state programmatically, and shows a visible indicator that does not depend on
  colour and whose meaning is also available as text to a screen reader.

## Declare Input Purpose

A field that collects the user's own details, such as a name, an email address, a telephone number, a postal address, or
a password, declares its purpose with the standard autocomplete value, so browsers and password managers can fill it.
Where the platform lets a field request a suitable on-screen keyboard, such as numeric or email, the field requests it.

## Targets Are Large Enough

| Viewport                                  | Minimum target size |
| ----------------------------------------- | ------------------- |
| every viewport                            | 24 by 24 CSS pixels |
| a mobile viewport, as the adopter defines | 44 by 44 CSS pixels |

The first row is WCAG 2.2's Target Size (Minimum) criterion at Level AA. The second is stricter, because a fingertip is
far less precise than a mouse pointer.

The adopter records the viewport width below which the mobile size applies. Without that record the stricter size cannot
be checked, and two reviewers apply it differently.

Enlarge a small control's hit area with padding rather than by growing its visible size. Measure the rendered size in
the browser, not the size the design intended, before merging a compact component.
