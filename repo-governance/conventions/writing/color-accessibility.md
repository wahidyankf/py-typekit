---
description: >-
  Requires that colour never carries meaning alone, fixes a colour-vision-safe palette with measured text pairings, and
  sets the contrast floor and the tests colour passes before publication.
when_to_use: >-
  Use when choosing, reviewing, or testing a colour that carries meaning, such as a diagram fill, a status marker, a
  chart series, or styling in documentation.
---

# Colour Accessibility

Colour may reinforce meaning but never carries it alone, and every colour meets a contrast floor measured, not judged by
eye.

## Never Colour Alone

Everything colour distinguishes is also distinguished by text, shape, line style, position, or pattern. A reader viewing
the content in greyscale, through a colour-vision simulation, or through a screen reader understands all of it. Colour
also disappears in greyscale printing, projector washout, and forced high-contrast modes. This is WCAG
[1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## Palette

Meaningful colour comes from this qualitative palette, distinguishable under the common colour vision deficiencies:

| Name   | Fill      | Text on the fill | Text contrast |
| ------ | --------- | ---------------- | ------------: |
| blue   | `#0173B2` | white `#FFFFFF`  |        5.13:1 |
| orange | `#DE8F05` | black `#000000`  |        8.04:1 |
| teal   | `#029E73` | black `#000000`  |        6.14:1 |
| purple | `#CC78BC` | black `#000000`  |        6.98:1 |
| brown  | `#CA9161` | black `#000000`  |        7.73:1 |
| grey   | `#808080` | black `#000000`  |        5.32:1 |

The text column is not a preference: for each fill it is the only one of black and white reaching 4.5:1. Black text on
blue measures 4.10:1; white text on any other fill measures between 2.61:1 and 3.95:1. Every ratio uses the WCAG
relative-luminance formula, and any new pairing is measured the same way before use.

## Colours to Avoid

Red, green, yellow, light pink, and bright magenta never carry meaning, and red is never paired with green: red and
green collapse together under the most common deficiencies, and yellow and light pink wash out. A passing state is teal
and labelled, not green.

## Contrast Floor

| Element                                                             | Minimum | Criterion                                                                                      |
| ------------------------------------------------------------------- | ------: | ---------------------------------------------------------------------------------------------- |
| normal text                                                         |   4.5:1 | [1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)  |
| large text: at least 18 point, or 14 point bold                     |     3:1 | 1.4.3 Contrast (Minimum)                                                                       |
| graphical objects and interface components, against adjacent colour |     3:1 | [1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) |

Where text's rendered size cannot be known in advance, such as a diagram label, require 4.5:1: the viewer decides the
size, and only the higher threshold holds at every size.

## Outlines

Every filled shape carries a black or palette-fill outline. The fill or the outline reaches 3:1 against each canvas the
content appears on: the light canvas `#FFFFFF` and the dark canvas `#0D1117`. Against white, orange measures 2.61:1 and
brown 2.72:1, below the 3:1 a graphical object needs, so there the outline defines the shape. Against `#0D1117` every
palette fill measures at least 3.69:1 unaided, and a black outline vanishes. One style holds on both canvases only when
each shape has its outline and its fill.

## Implementation

- Declare each colour once, as a hex value, in a named style that every element sharing that meaning reuses. Colour
  names render differently across tools; scattered inline styles drift.
- Explain each colour's meaning in visible prose near the content wherever labels do not already say it.

## Before Publishing

Test every new or materially changed use of colour:

1. Only palette fills are used, each with its paired text colour and an outline.
2. Every element stays distinct under simulated red-blind, green-blind, and blue–yellow-blind vision.
3. Every contrast ratio is measured, not estimated.
4. The content is checked rendered on a light and on a dark background.
5. The content is fully understandable in greyscale.

## Scope

In scope: colour that carries meaning in documentation — diagrams, status markers, charts, and styled examples.

Out of scope: brand identity, application interface design, and print colour spaces, which have their own constraints
and owners.

## Enforcement

An adopter enforces the palette, the text pairings, and the outline in its own diagram or style validator; the
simulation and rendered checks remain review.
