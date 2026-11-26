---
description: >-
  Sets out the colour notation, token value format, and dark-theme activation options for a token layer, with the gains
  and costs of each and the default value format.
when_to_use: >-
  Use when choosing or reviewing how a token layer writes colours, formats token values, or switches to the dark theme.
---

# Notation, Format, and Dark Activation

The adopter records one option per decision for the whole token layer.

| Decision        | Option                                                                  | Gains                                                                      | Costs                                                                    |
| --------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| colour notation | HSL                                                                     | familiar, and read by nearly every tool and design handoff                 | equal lightness looks unequal across hues, so palettes need hand tuning  |
| colour notation | OKLCH                                                                   | perceptually even lightness and chroma; reaches wider gamuts               | less familiar; older tools may not read it; conversions add rounding     |
| value format    | direct value: each token holds a complete value (default)               | simplest to read; an override replaces one declaration                     | a translucent variant needs its own token or a colour-mixing function    |
| value format    | channel values wrapped by an alias                                      | one set of channels reused at different opacities                          | two levels kept strictly apart, and every value read through indirection |
| dark activation | a class or attribute on the root                                        | the interface can offer its own theme switch                               | the operating-system preference needs separate handling                  |
| dark activation | a class or attribute on the root, falling back to the system preference | a user can choose a theme, and a user who never chooses follows the system | two activation paths to keep consistent, and a stored choice to honour   |

The direct value is the default format because it removes a layer of indirection that most token layers never use:
declarations stay readable, and an override is a single replacement.
