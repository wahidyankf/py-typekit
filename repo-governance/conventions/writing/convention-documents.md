---
description: >-
  Fixes what a convention document must contain, when to create a new convention rather than update or merge an existing
  one, and the checks a convention passes before publication.
when_to_use: >-
  Use when writing, restructuring, splitting, or reviewing a convention, or when deciding whether new guidance needs a
  convention of its own.
---

# Convention Documents

A convention records a choice so someone absent when it was made can apply it; what it must contain follows from that
reader.

## What Every Convention Contains

| Content                                                             | Why it is required                                                                   |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| the rule, stated first and decisively                               | a reader deciding whether the document applies needs the rule, not its history       |
| its scope, including what it excludes                               | an unstated boundary gets guessed, and two readers guess differently                 |
| the reason for every rule that is not self-evident                  | a rule without a reason is followed exactly until the first case it did not foresee  |
| an example wherever the rule is abstract                            | the example is what a reader copies, and a correct and incorrect pair shows the edge |
| metadata per [Artifact Metadata](../structure/artifact-metadata.md) | routing and discovery read metadata before the body                                  |

Write "use" and "never", not "consider" or "you might": a convention that only suggests cannot be checked.

A convention applying a written principle links it instead of re-arguing it, and one touching a concern another artifact
owns links the owner rather than restating it, per [One Source Per Fact](../../principles/one-source-per-fact.md).

## Convention or Something Else

A convention states what must be true whenever it is read, and records a choice another repository could reasonably make
differently. A constraint true for every repository is a [principle](../../principles/README.md). Guidance that only
makes sense as a sequence, as recurring judgement, or as a role with its own tools takes another form — see
[Capability Forms](../../development/agents/capability-forms.md).

## Create, Update, or Merge

| Decision                      | When                                                                                                                                               |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| create a new convention       | the concern is distinct, its scope can be stated without overlapping an existing convention, and more than one document or process will rely on it |
| update an existing convention | the guidance extends or clarifies that convention's scope, or more than 60 percent of it is already covered there                                  |
| merge two conventions         | they overlap by more than 60 percent, they are always consulted together, or readers cannot tell which one to follow                               |

Search the [conventions index](../README.md) before deciding. The expensive mistake is a new convention whose rule
already exists under another name: the two drift apart, and nothing decides which a reader should believe.

## Size

A convention's length is the sum of its files, never the size of one file. The adopting repository declares its
[word budget](../structure/document-word-budget.md) in its repository configuration. A convention that outgrows that
budget becomes an entrypoint and a companion directory of ordered modules, per
[File Naming](../structure/file-naming.md). When those modules start covering concerns that could be adopted separately,
split the convention into several conventions instead of adding modules.

## Naming and Change

A convention's filename is lowercase kebab-case and names its concern; its directory carries the category, and it has no
ordinal prefix. Its change history lives in version control, never in date or version fields.

Retiring a convention updates every reference in the same change. Keeping a deprecation notice and migration path for a
retention period is the adopter's decision: the window lets dependants migrate, while deleting outright under
[Deletion With Proof](../../development/quality/deletion-with-proof.md) leaves no stale entry point.

## Before Publishing

- [ ] The rule comes first, and every rule that is not self-evident carries its reason.
- [ ] The scope names what is excluded.
- [ ] Abstract rules have an example, with correct and incorrect usage where the boundary is subtle.
- [ ] Every term is defined or linked, and nothing another artifact owns is restated.
- [ ] Prose follows [Content Quality](content-quality.md), and links follow [Internal Links](internal-links.md).
- [ ] Images carry alt text, and any diagram follows [Diagrams](diagrams.md).
- [ ] The parent index lists the convention in its table and its directory map.
- [ ] Metadata validates, and every file is within the repository's declared
      [word budget](../structure/document-word-budget.md).

The last two checks are mechanical; an adopter runs them in its own gates, and the rest is review.
