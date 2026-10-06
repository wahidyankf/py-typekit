---
name: authoring-documentation
description: >-
  Guides writing documentation that stays true: grounding each claim in the repository before publishing, keeping
  always-read files as navigation, and linking a governing document at its first mention.
when_to_use: >-
  Use when creating or revising a documentation page or an always-read instruction file, or when a draft states facts
  about the repository that nobody has checked.
compatibility: Requires read access to the source, tests, and configuration the documentation describes.
---

# Authoring Documentation

The conventions own the rules. [Documentation Architecture][documentation-architecture] decides where a page lives and
requires that its commands were run; [Content Quality][content-quality] decides how it reads; [Factual
Validation][factual-validation] decides how an external claim is verified; and [Progressive
Disclosure][progressive-disclosure] decides what an always-read file states. This skill covers the author's judgement
those rules rely on.

## Ground Every Claim in the Repository

A statement about the repository is checked against the repository, not against memory or another document. Match each
claim to what can confirm it:

| Claim                           | Confirmed by                                                                |
| ------------------------------- | --------------------------------------------------------------------------- |
| a path, file, or directory      | listing it at the revision being documented                                 |
| a command and its output        | running it                                                                  |
| a function, option, or default  | reading the code or configuration that defines it                           |
| a behaviour                     | a test that exercises it, a behaviour specification, or a run that shows it |
| a link                          | resolving it, per [Internal Links][internal-links]                          |
| a version or external interface | an authoritative source, per Factual Validation                             |

Another document is a lead, not a confirmation: it may be the stale copy. When prose disagrees with the code,
configuration, or behaviour specification, the prose is the defect.

A claim that cannot be checked is either marked as unverified or left out. A confident unverified sentence looks exactly
like a verified one.

## Use the Repository's Own Terms

Use the identifiers, option names, and error text the repository actually uses, as inline code, and name the file that
defines them. A friendlier synonym makes the reader translate twice: once while reading and again while searching.

## Keep Always-Read Files as Navigation

A root instruction file or top-level index is read by everyone, so each line there is a short summary that links to the
document owning the detail. When adding to one:

- write the detail in its owning document first, and complete it there;
- add a line or two naming the rule and linking the owner, repeating nothing the owner explains; and
- where the repository recorded that its root file holds links only, add only the link.

Examples, exhaustive lists, and rationale are what usually push an always-read file past its
[word budget](../../../repo-governance/conventions/structure/document-word-budget.md). Placing them in their owner now
costs less than relocating them later.

## Link a Governing Document Once

The first mention of a governing document on a page is a descriptive link. Later mentions on the same page cite it as
inline code, by its file name or identifier, without linking again. Repeated links to one target make every link on the
page harder to notice, and a reader who needed the target already met it at the first mention.

A long page read in pieces may repeat the link at the start of a major section, where a reader can arrive without having
seen the first one.

## Change the Page With the Behaviour

Update a page in the same change as the behaviour it describes; [Documentation First][documentation-first] argues why.
[Docs Propagation](../../../repo-governance/workflows/quality/docs-propagation.md) owns the sequence.

## Before Publishing

Reread every factual sentence and ask what confirmed it. A sentence whose honest answer is "probably" gets checked now
or removed. No placeholder ships: a heading with nothing beneath it but a promise to write it later advertises a page
that does not exist.

[documentation-architecture]: ../../../repo-governance/conventions/structure/documentation-architecture.md
[content-quality]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/content-quality.md
[factual-validation]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/factual-validation.md
[progressive-disclosure]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/principles/progressive-disclosure.md
[internal-links]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/internal-links.md
[documentation-first]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/principles/documentation-first.md
