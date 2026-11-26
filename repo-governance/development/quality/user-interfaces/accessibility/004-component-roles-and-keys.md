---
description: >-
  Fixes the roles, states, and keyboard behaviour each common interactive component type carries, from button and dialog
  to combobox and loading region, and the order in which an accessible name is sourced.
when_to_use: >-
  Use when building or reviewing a button, dialog, input, combobox, menu, tooltip, tab list, progress indicator, loading
  region, or status message, or when choosing where an accessible name comes from.
---

# Component Roles and Keys

Each interactive component type carries its required roles and attributes and its keyboard behaviour. For a pattern not
listed here, the [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) is the reference.

| Component          | Roles, states, and properties                                                                | Keyboard behaviour                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| button             | a native button; an accessible name if icon-only; pressed state for a toggle; disabled state | Enter and Space activate it                                                                      |
| dialog             | dialog role, modal state, labelled by its title, and a reference to its description          | focus moves inside on open, Tab cycles within it, Escape closes it, focus returns to the trigger |
| input or text area | invalid state after failed validation, a reference to its error message, required state      | standard text editing                                                                            |
| custom combobox    | combobox role, expanded state, and a reference to the list it controls                       | as the Authoring Practices Guide combobox pattern sets out                                       |
| menu or dropdown   | the trigger exposes expanded state and that it opens a menu; menu and menu item roles        | arrow keys move between items, Home and End jump to the ends, Escape closes it                   |
| tooltip            | tooltip role, referenced from its trigger as the trigger's description                       | appears on keyboard focus as well as on hover                                                    |
| tab list           | tab list, tab, and tab panel roles; selected state; each tab references its panel            | arrow keys move between tabs, Tab moves into the active panel                                    |
| progress indicator | progress bar role with current, minimum, and maximum values; a label if none is visible      | none                                                                                             |
| loading region     | busy state on the container while its content loads                                          | none                                                                                             |
| message            | alert role for a blocking error; a status role or polite live region otherwise               | none                                                                                             |

A generic element given a button role also needs a keyboard handler and a place in the tab order, which is one more
reason a native button is preferred.

## Accessible Names

Every interactive element has an accessible name. Assistive technology takes it from the first of these sources present,
so a higher source silently overrides a lower one:

1. a reference to visible text elsewhere on the page;
2. a name attribute given directly on the element, which nothing on screen shows;
3. an associated label element, for a form control; and
4. a title attribute, only as a last resort, because some assistive technologies never announce it.

## Why a Table

Each row is a contract a reviewer can check and an automated rule can partly enforce. A general instruction to add
"appropriate ARIA" lets every component author invent a pattern, and a screen reader user then learns a different
interaction for every menu they meet.
