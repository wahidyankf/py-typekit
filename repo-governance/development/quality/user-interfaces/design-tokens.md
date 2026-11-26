---
description: >-
  Makes a token layer the single authority for visual values, separates shared structural tokens from per-application
  brand tokens with a dark counterpart for each theme-dependent token, and leaves notation and format to the adopter.
when_to_use: >-
  Use when adding, naming, or overriding a design token, reviewing a stylesheet or component for raw visual values, or
  deciding whether a repeated value should become a token.
---

# Design Tokens

Design tokens are the named values that form a shared visual vocabulary: colours, spacing, radii, type sizes, and
shadows. On the web they are CSS custom properties. The token layer is the one place a visual value is defined, and
everything else refers to it by name.

This standard implements [One Source Per Fact](../../../principles/one-source-per-fact.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Accessibility First](../../../principles/accessibility-first.md), and
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md).

It is written for web stylesheets. A single-application repository keeps both token categories in its one token layer,
and another platform maps the cascade rules below onto its own theming mechanism.

## Modules

1. [Notation, Format, and Dark Activation](design-tokens/001-notation-format-and-dark-activation.md)

## Two Categories

| Category   | Holds                                                          | Defined by             | Overridden per application |
| ---------- | -------------------------------------------------------------- | ---------------------- | -------------------------- |
| structural | spacing scale, radii, type scale, shadows, and base neutrals   | a shared token package | never                      |
| brand      | primary, secondary, and accent colours, each with a foreground | each application       | yes, by design             |

An application imports the shared structural tokens and declares only its brand overrides, after the import, so the
cascade applies them. It never copies a structural token into its own stylesheet, where the copy silently diverges once
the shared package changes.

Base neutrals, such as background, foreground, border, and focus ring, are structural because they carry no brand: every
application needs the same neutral surfaces, so one shared definition keeps them consistent.

## Components Refer by Role

A component refers to a token by its role, such as `primary`, `muted-foreground`, `destructive`, or `border`. It never
uses a raw value, and never a palette step such as `blue-600`. A raw colour bypasses theming entirely. A palette step
survives theming but breaks as soon as the brand changes which step means primary. Referring by role is what lets a
theme or a brand change without touching a component.

## Theme-Dependent Tokens Have Dark Counterparts

Where an interface offers a dark theme, every token whose value can differ by theme, such as colours and shadows, is
defined for the dark theme as well as the light one. An undefined dark token keeps its light value, which is where
invisible text and failed contrast come from. A theme-invariant token, such as a spacing step, radius, or type size,
needs no dark definition.

Contrast is verified separately in each theme, against the floor in
[Accessibility First](../../../principles/accessibility-first.md). A pair that passes in one theme proves nothing about
the other.

## When a Value Becomes a Token

Add a new token only when all three hold:

1. the value is used in three or more places;
2. it names a real concept, such as a sidebar background or a destructive action; and
3. no existing token already covers that concept.

A value that merely coincides across unrelated places is not a token; tokenizing it couples parts that have no reason to
change together.

## Keep the Cascade Working

A token definition never carries an importance override. Brand overrides work because a later declaration wins, and
forcing the shared value to win defeats every application's override at once.

## Notation and Format Are Adopter Decisions

The colour notation, the token value format, and how the dark theme activates are adopter decisions. Their options and
trade-offs are in [Notation, Format, and Dark Activation](design-tokens/001-notation-format-and-dark-activation.md).

## Enforcement

An adopter enforces the mechanical parts in its own stylesheet lint: no raw colour literal in a component file, no
importance override in a token definition, and every theme-dependent light-theme token present in the dark theme.
