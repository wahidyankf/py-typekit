---
description: >-
  Caps instruction files and governance documents at a declared word ceiling measured over the whole file, and repairs a
  breach by relocating detail rather than cutting or compressing it.
when_to_use: >-
  Use whenever a governed document nears or exceeds its word ceiling, or when setting the ceiling a repository enforces.
---

# Document Word Budget

Instruction files and governance documents are read whole, by people seeking one rule and by coding-agent harnesses that
load them every session and may not read past their own limits. A word ceiling keeps that read affordable. [Progressive
Disclosure][progressive-disclosure] argues why; this convention fixes the mechanics.

## What Is Measured

| Surface                                                                            | Budgeted        |
| ---------------------------------------------------------------------------------- | --------------- |
| the root instruction file and each harness counterpart, alone and with its imports | always          |
| every document in the governance tree, index files included                        | always          |
| each harness's agent-definition directory                                          | adopter decides |
| plans, behaviour specifications, and product documentation                         | adopter decides |

The count covers the entire file, metadata and code included, since any carve-out lets words grow unmeasured; a root
file's imports count with it, since a harness loads them together.

Repository configuration declares the ceiling and the counting rule, and the gate's verdict is the measurement; a quick
shell count is only an estimate.

## What an Adopter Decides

- **the ceiling** — Options: one number, or one per class of surface; Trade-off: one number is simpler; classes fit
  files with different jobs, and overlapping classes then need an order
- **the count** — Options: whitespace-separated tokens, or runs of letters and digits; Trade-off: whitespace is
  reproducible with standard tools; letter runs weigh links and tables more as a reader does
- **agent definitions** — Options: measure them, or leave them unmeasured; Trade-off: measuring catches a definition a
  harness stops reading; leaving them out sizes each by its task
- **a warning band** — Options: none; closed only by relocation; or prompting a simplification or split; Trade-off:
  relocation-only blocks trimming back under the band; a prompt trusts the author; no band fails first
- **excluded trees** — Options: exclude records sized by what they must say, or include them; Trade-off: exclusion keeps
  a delivery record whole; inclusion catches a plan grown too large to follow

When two surface classes match one file, the later declaration decides, so a narrower class is declared after any
broader one it overlaps, and reordering declarations is a policy change. An excluded tree is outside the gate, not
outside [Minimal Sufficiency](../../principles/minimal-sufficiency.md).

## Repair by Relocation

A breach closes by moving detail, whole, into the document that owns it, leaving a one-line summary and a link. The rule
stays reachable; it is no longer inline.

These do not close a breach:

1. **Deleting a rule.** Coverage is lost.
2. **Compressing, or moving text into another always-loaded file.** Neither lowers what a reader pays, as [Progressive
   Disclosure][progressive-disclosure-2] explains.
3. **Linking to an incomplete target.** A link replacing a list that lacks cases the inline text covered quietly drops
   them. Complete the target first, or state the rule as a pattern instead of a list.
4. **Evading the gate.** Cutting a file off mid-rule, parking the excess where the gate never looks, or renaming an
   extension to drop the file from measurement.

Rules that protect safety, such as secret handling and branch protection, move last, and only into a target that already
holds them completely.

A document split for its budget becomes an entrypoint and a companion directory named per [File Naming](file-naming.md),
split along reader tasks. Nothing is split merely to use or avoid the budget. An index at its ceiling follows
[Directory Indexes](directory-indexes.md).

## Changing the Ceiling

A file over its ceiling keeps failing until relocation fixes it; Progressive Disclosure argues why. The ceiling moves
only in a class-wide recalibration that records evidence the signal is broadly unactionable or that harness capacity or
repository policy has changed, states its reasoning, and validates every file in the class.

The adopter enforces the ceiling in its own gate, run in pre-commit or CI wherever its other checks run.

## Principles

This convention implements [Progressive Disclosure][progressive-disclosure] and
[Minimal Sufficiency](../../principles/minimal-sufficiency.md): a reader pays only for the rule in hand, and a ceiling
bounds a document without becoming a length to fill.

[progressive-disclosure]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/principles/progressive-disclosure.md
[progressive-disclosure-2]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/principles/progressive-disclosure.md#a-budget-is-the-usual-mechanical-form
