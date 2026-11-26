---
description: >-
  Requires every interactive element to be keyboard reachable and operable, with a visible focus indicator, a focus
  order that follows reading order, no keyboard traps, and a skip link past repeated blocks.
when_to_use: >-
  Use when building an interactive element, a dialog, or a layout with repeated navigation, or when reviewing focus
  styles.
---

# Focus and Keyboard

## Everything Interactive Works From the Keyboard

Every interactive element is reachable with Tab and Shift+Tab and responds to the keys its role expects. Anything a
pointer can do, a keyboard can do.

| Key        | Behaviour                                                             |
| ---------- | --------------------------------------------------------------------- |
| Tab        | moves focus forward through interactive elements                      |
| Shift+Tab  | moves focus backward                                                  |
| Enter      | activates a button, follows a link, submits a form                    |
| Space      | activates a button, toggles a checkbox                                |
| Escape     | dismisses a dialog, closes a menu or dropdown, cancels an action      |
| arrow keys | move within a composite widget: a menu, tab list, radio group, slider |
| Home, End  | move to the first or last item of a list or menu                      |

## Focus Is Always Visible

Every focusable element shows a visible focus indicator with at least 3:1 contrast against its adjacent colours.
Suppressing the browser's default indicator is a defect unless an equivalent indicator takes its place.

Tie the indicator to the platform's keyboard-focus state rather than to every focus, so a pointer click does not flash a
ring while a keyboard user never loses one. Offset the indicator from the element wherever the element's own colour
would otherwise swallow it.

## Focus Order Follows Reading Order

Tab order follows visual reading order, and document order matches visual order. Reordering content visually through
layout properties or absolute positioning separates the two without any warning, so a reordered layout is checked with a
keyboard and a screen reader.

Make a non-interactive element focusable only when it genuinely needs focus, and never assign a positive tab index.

## No Keyboard Traps

Focus that enters a component can always leave it by keyboard. The one deliberate containment is a modal dialog:

- while it is open, Tab and Shift+Tab cycle only among its own elements;
- Escape closes it; and
- when it closes, focus returns to the element that opened it.

Anything else that holds focus is a trap.

## Skip Repeated Blocks

A layout with a repeated header, navigation, or sidebar offers a skip link as its first focusable element. The link is
visible when focused and moves focus to the main content, so a keyboard user does not tab through the same navigation on
every page.
