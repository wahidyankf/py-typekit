---
description: >-
  Requires condensing or deduplicating documentation to move substantive content to a durable, linked home and to prove
  that nothing was lost, rather than deleting it.
when_to_use: >-
  Use when shortening, splitting, merging, or deduplicating governance or documentation files, or when a word budget
  pushes content out of a document.
---

# Content Preservation

Shortening a document is a move, not a deletion. Substantive content leaves a document only by arriving somewhere
durable that the original links to, and the move is finished only once it is shown that nothing was lost.

This standard implements [One Source Per Fact](../../../principles/one-source-per-fact.md) and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Why Deletion Is the Default Failure

A word budget, a duplication finding, and a tidy-up all push toward cutting. Cut text raises no error: the rule it
stated simply stops being applied, and the next reader cannot tell it ever existed. Moving it costs one link.

## Choose the Home by What the Content Is

| Option                                  | Use when                                                                           |
| --------------------------------------- | ---------------------------------------------------------------------------------- |
| a new owning document                   | the content is a rule or practice that has no current owner                        |
| merge into an existing owner            | a document already governs the subject and the content extends it                  |
| extract a shared pattern to one owner   | several documents restate the same content; one holds it and the others link there |
| a companion module of the same document | the content belongs to the same rule but exceeds the entrypoint's budget           |

A companion module is this catalog's form of a separate sibling document: it keeps the content beside the rule it
belongs to while giving it a budget of its own.

The home follows the content's kind, not the place it came from. A rule goes where rules of its kind live, and a
procedure where procedures live; [Capability Forms](../../agents/capability-forms.md) sets out the forms available.

## When Content Stays

Not everything that could be condensed should move:

- an application of a rule that only makes sense for the one artifact holding it;
- content already a few lines long, where a link would cost more than the text; and
- context that is meaningful only beside the material around it.

## The Move

1. Identify the substantive statements: rules, rationale, defining examples, exceptions, and decisions.
2. Choose the home using the table above.
3. Write the content there in full, adapted to its new context.
4. Replace the original passage with a short summary and a link to the new home.
5. Update the index of every directory that gained or lost a document.
6. Update every reference that pointed at the moved content.
7. Verify zero loss.

## Verify Zero Loss

Read the original and the destination completely. Confirm that each unique statement of the original is present in the
destination or deliberately omitted, and record every deliberate omission with its reason. Confirm that every link
resolves and that the destination contradicts nothing left in the original.

A move verified by skimming is not verified; the statement most likely to be lost is the one a skim passes over. The
adopter enforces the mechanical part, resolved links and updated indexes, in its own gate or CI.

## Anti-Patterns

| Anti-pattern                                       | Why it fails                                                    |
| -------------------------------------------------- | --------------------------------------------------------------- |
| deleting content with no new home                  | the rule silently stops existing                                |
| moving only part of it                             | the missing part looks deliberate and is never recovered        |
| choosing the wrong home                            | readers who look where content of that kind lives never find it |
| moving artifact-specific logic into a general rule | the rule now binds cases it was never written for               |

## Related Standards

- [Deletion With Proof](../deletion-with-proof.md) governs retiring behaviour or code, where the thing itself is meant
  to disappear and its successor must be proven.
- [Knowledge Capture and Archival](../../../conventions/structure/plans/008-knowledge-capture-and-archival.md) routes
  plan learnings to durable owners.
