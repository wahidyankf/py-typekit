---
description: >-
  Fixes the six parts of a concept section: title and introduction, a diagram only where one helps, narrative, annotated
  code, a key takeaway, and why the concept matters in real work.
when_to_use: >-
  Use when drafting or reviewing a tutorial content section that teaches one concept.
---

# Concept Sections

A content section that teaches a concept applies the explain-then-show order of
[Tutorial Structure](../tutorial-structure.md) in six parts:

| #   | Part                   | Carries                                                                                                               |
| --- | ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1   | Title and introduction | the concept's name, then a few sentences on what it is, why it matters, and how it relates to concepts already taught |
| 2   | Diagram                | only when components, flow, states, relationships, or a comparison of approaches are clearer drawn than described     |
| 3   | Narrative              | how the concept works, when to use it, its trade-offs, alternatives, and common pitfalls, before any code             |
| 4   | Annotated code         | a worked example whose annotations say what each significant line does and produces                                   |
| 5   | Key takeaway           | the one insight to keep, in a sentence or two                                                                         |
| 6   | Why it matters         | a short note connecting the concept to production use and what it changes there                                       |

## Why These Parts

The introduction relates the concept to earlier ones because a new idea needs something already understood to attach to.

A diagram appears only where structure is the point. Drawn for a simple syntax demonstration, it adds reading without
adding understanding, and a reader learns to skip diagrams, including the ones that matter. Diagrams follow
[Diagrams](../diagrams.md).

The narrative precedes the code for the reason the entrypoint gives: an example met first is copied as a pattern.
Covering trade-offs there, not only the case where the concept works, is what lets a learner choose the concept rather
than merely use it.

The key takeaway gives the summary something to consolidate, and the production note answers the question a practitioner
asks of every concept: when would I need this?

## Enforcement

A reviewer checks that the required parts appear in order and that narrative precedes code; whether a diagram is
warranted stays a review judgement.
