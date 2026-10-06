---
name: validating-links
description: >-
  Guides checking that internal links and anchors resolve under the link form each tree recorded, that external
  addresses are reachable, and how a broken link is repaired without changing what the sentence meant.
when_to_use: >-
  Use when checking or repairing links across documentation, or when a link check reports a broken, redirected, or
  unreachable target.
compatibility: Requires read access to the linked trees, and network access for external addresses.
---

# Validating Links

[Internal Links][internal-links] owns the link form, what an internal check covers, repair in the same change, and the
recorded choices for wiki-style links and archived trees. [Repository Validation
Methodology][repository-validation-methodology] owns how a check resolves a path, and
[Docs Quality Gate](../../../repo-governance/workflows/quality/docs-quality-gate.md) owns the sequence. This skill
covers the checker's and repairer's judgement.

## Apply the Choice the Tree Recorded

Repositories choose link form per tree: a general tree may require standard relative links and reject wiki-style links,
while a tool-bound notes tree may require wiki-style links and reject relative paths. Read the choice the repository
recorded under Internal Links for each tree, and check each tree against its own choice:

| Tree recorded as        | A finding                                                      |
| ----------------------- | -------------------------------------------------------------- |
| standard relative links | a wiki-style link, which no general renderer resolves          |
| wiki-style, tool-bound  | a relative path, which the tool's backlinks will not follow    |
| no choice recorded      | apply standard relative links, and report the missing decision |

A wiki-style tree sits outside a general link checker, so its links are only as sound as the tool the adopter runs for
it.

## What to Resolve, and What to Skip

- **Internal links:** the target exists as a document, resolved from the linking file.
- **Anchors:** the fragment names a heading that exists in the target, as the renderer builds heading identifiers.
- **Images:** the relative path resolves like any other link.
- **Skip:** anything inside a code block or inline code, and commented-out links. Those are examples, not navigation.

When the repository's link gate has already run, carry its result for internal links and check only what it does not
cover.

## Reachable Is Not Broken Is Not Unknown

| External response                         | Result                                                 |
| ----------------------------------------- | ------------------------------------------------------ |
| success                                   | reachable                                              |
| redirect                                  | reachable; report the final address for information    |
| not found or gone                         | broken                                                 |
| server error, timeout, or network failure | inconclusive; check again later before calling it dead |
| refused as automated traffic              | inconclusive; confirm in a browser                     |

A network failure is not a broken link. Reporting it as one sends a repairer after a page that is fine.

## Adopter Decision: Remembering External Results

Record whether external results are remembered between runs, and for how long.

- **no memory; check every address each run** — Gains: every result is current; Costs: slow runs, and hosts that
  rate-limit automated checks
- **a short window per result kind** — Gains: fast, polite runs; failures are retried soon; Costs: a window per kind to
  maintain
- **a long window per address** — Gains: very few requests; Costs: a page that died after its last check reads as
  reachable

Under any option, only reachable results are remembered, and an address no longer used anywhere is dropped.

## Rating What Is Found

A broken internal link breaks navigation for every reader and is `CRITICAL`, as [Criticality
Levels][001-criticality-levels] lists. A dead external address is usually `HIGH`, a link in the wrong form for its tree
`HIGH`, an inconclusive result `MEDIUM` until it persists, and a redirect `LOW`. A file name used as link text fails
[Accessible Content][003-accessible-content].

## Repair Without Changing the Sentence

- Read the sentence to learn what the link was meant to reach before choosing a new target.
- Keep the link text; change only the target.
- For a moved document, link its new location, never its directory.
- For a dead external page, link the current home of the same content, not a similar page.
- When nothing replaces the target, remove the link and keep the sentence true without it.

Then resolve the repaired link again.

[internal-links]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/internal-links.md
[repository-validation-methodology]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/checks/repository-validation-methodology.md
[003-accessible-content]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/content-quality/003-accessible-content.md
[001-criticality-levels]:
  ../../../repo-governance/development/quality/evidence/finding-criticality-and-confidence/001-criticality-levels.md
