---
description: >-
  Requires a plan that changes a user interface to carry its exploration as accessible assets, document the selected
  design, and trace device-level proof through delivery.
when_to_use: >-
  Use when a formal plan creates or materially changes user interface behaviour.
---

# Plan UI Design

Interface work is cheapest to change before it is built and hardest to review from prose. This convention makes a plan's
interface design reviewable before implementation and its result provable afterwards.

It adds to the [Plans Convention](plans.md). How alternatives are produced, how one is selected, and why the rest record
their reasons belong to
[Interface Alternatives](../../development/quality/manual-verification/004-interface-alternatives.md); this convention
fixes how a plan carries them.

## The Fidelity Matrix

Both fidelity stages use the same representative task and content, so the comparison is between designs rather than
between examples.

| Stage         | Produces                                                                                        |
| ------------- | ----------------------------------------------------------------------------------------------- |
| low fidelity  | the alternatives Interface Alternatives requires, across the device classes it names            |
| selection     | the reasoned comparison and single selection that module requires                               |
| high fidelity | the alternative or alternatives Interface Alternatives advances, at desktop, tablet, and mobile |

How many alternatives are drawn, which device classes they cover, and the criteria that select one are fixed by
[Interface Alternatives](../../development/quality/manual-verification/004-interface-alternatives.md), not restated
here.

Where another product is studied, record which disciplines are adopted and which visual or product choices are rejected.
A reference is evidence, not permission to copy another identity.

## Assets

Assets live in an `assets/` folder in the plan root, with a `README.md` listing them. They are design artifacts, not
plan documents, and [Required Documents](plans/002-required-documents.md) permits the folder beside the six. Only
`tech-docs/` is a technical shape, and assets alone never justify the directory technical shape — that stays the
[Technical Shape](plans/003-technical-shape-and-companions.md) decision.

- **Format.** SVG by default, because it is deterministic, diffable, and reviewable as text. Raster only where bitmap
  fidelity is material to the decision.
- **Accessibility.** Every SVG carries a unique `<title>` and `<desc>`, every embed carries a text alternative saying
  what the design shows, and no meaning relies on colour alone.
- **Naming.** `ui-<option>-<fidelity>-<device>.<ext>`, where `<ext>` is `svg` by default, fidelity is `lofi` or `hifi`,
  and device is `desktop`, `tablet`, or `mobile`.
- **Content.** Real product copy, and never a real account, credential, or personal value — see
  [Evidence Safety and Accessibility](../../development/quality/manual-verification/005-evidence-safety.md).

Mockups are interface assets rather than conceptual diagrams, so the [Diagrams](../writing/diagrams.md) authoring rule
does not govern them.

## The UI Design Section

A section of `tech-docs.md`, or a UI-design companion in the directory shape, embeds every asset the exploration
produced, labels each alternative selected or not selected, places the rationale beside the comparison, and states:

- the user, their job, the interface states, and the real copy;
- each alternative's behaviour across devices;
- the selected alternative's trade-offs, its palette, type, and layout tokens, and the components it introduces or
  reuses;
- keyboard, focus, error, empty, loading, reduced-motion, and responsive behaviour; and
- every implementation, test, specification, and asset path, through the plan's [File Impact](plans/013-file-impact.md)
  tree.

The plan `README.md` shows at least one selected high-fidelity asset and links the full comparison, so the direction is
visible before the design is read.

## Acceptance and Delivery

Each interface-affecting acceptance criterion names its affected routes or screens, rendered states, and supported
viewport classes.

`delivery.md` traces exploration, selection, implementation, and accessibility checks. It then carries a manual check of
that route, state, and viewport matrix against the running result, at the exact address it is served from, recording a
pass or fail for each combination without private values. Automation, code inspection, inferred layout, and static
assets supplement that check; none replaces it.

Every interface-affecting plan, whatever its size, also carries the
[Exploratory and Usability Review](../../workflows/quality/exploratory-usability-review.md) as required items, with its
findings routed to `learnings.md`. Captures follow [Evidence Files](plans/016-evidence-files.md).

## Principles

This convention implements [Accessibility First](../../principles/accessibility-first.md), because every asset carries a
text alternative from its first draft, and [Evidence Over Assertion](../../principles/evidence-over-assertion.md),
because the running interface is checked at each route, state, and viewport.
