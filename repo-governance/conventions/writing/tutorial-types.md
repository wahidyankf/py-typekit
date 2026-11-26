---
description: >-
  Defines the seven tutorial types by the coverage each promises, fixes how a type is named and chosen, and requires
  every tutorial to be exactly one type, kept apart from any progression model.
when_to_use: >-
  Use when scoping, titling, or reviewing a tutorial, or when a proposed tutorial seems to fit more than one type.
---

# Tutorial Types

Every tutorial is exactly one of seven types. A type is a promise about depth and audience, made before the learner
opens the document.

## The Types

| Name          | Prerequisite                           | Coverage        | Reader and goal                                                      |
| ------------- | -------------------------------------- | --------------- | -------------------------------------------------------------------- |
| Initial Setup | none                                   | up to 5%        | install, verify, and run a first example                             |
| Quick Start   | none                                   | 5–30%           | enough core concepts to read the documentation and explore alone     |
| Beginner      | none                                   | up to 60%       | a complete foundation: the core features most real work uses         |
| Intermediate  | Beginner, or equivalent experience     | 60–85%          | production practice: testing strategy, security, performance, scale  |
| Advanced      | Intermediate, or equivalent experience | 85–95%          | expert depth: edge cases, profiling, internals, design trade-offs    |
| By Example    | programming experience                 | 95%, cumulative | a language or framework learned through annotated, runnable examples |
| Cookbook      | working knowledge                      | not depth-based | problem-solving recipes, organised by problem, not a learning path   |

Coverage is the share of the subject's domain knowledge a type covers, stated as the author's estimate. By Example's
figure is cumulative across its own levels. The last 5% — research-level and highly specialised topics — belongs to no
type and is written as separate specialised material.

The first three depth types also leave material out:

- **Initial Setup** excludes in-depth explanation and multiple examples or variations.
- **Quick Start** excludes comprehensive coverage and production practice.
- **Beginner** excludes advanced optimization and architectural patterns.

## Why the Ranges Overlap

1. [Why the Ranges Overlap](tutorial-types/001-why-the-ranges-overlap.md) — the short and long paths, and where By
   Example sits.

## Type and Progression

The second module, [Type and Progression](tutorial-types/002-type-and-progression.md), holds a type apart from any
progression model a repository keeps.

## Choosing a Type

Ask about the reader's experience first.

- A reader **still learning the subject** takes the first line that describes them:
  1. They only need to confirm the subject runs — **Initial Setup**.
  2. They already program and are picking up a new language or framework — **By Example**.
  3. They want just enough to explore on their own — **Quick Start**.
  4. They want a complete foundation — **Beginner**.
  5. They are building production systems — **Intermediate**.
  6. They need expert depth — **Advanced**.
- A reader **already experienced with the subject** who needs to solve a specific problem takes a **Cookbook**, which
  assumes that working knowledge.

## Rules

- **One type per tutorial.** A "Beginner and Intermediate" tutorial has no single reader, and keeps neither coverage
  promise. Split it.
- **The title carries the type name**, as in `Initial Setup for <subject>`, `<subject> Quick Start`, or
  `<subject> Cookbook`. Learners choose from titles alone.
- **Content matches the type's coverage.** A Quick Start that drifts into internals has become a different type under
  the wrong name.
- **Intermediate and Advanced require the level below** or equivalent experience, so a learner who skipped it knows
  where to go back.
- **Depth is stated as coverage.** Coverage describes the content, which the author controls. A time estimate may
  accompany it, labelled as an estimate, but never replaces it, because it describes the reader, which the author does
  not.
- **No ad-hoc types.** A new label is a promise no reader has learned to calibrate. A need the seven do not cover is a
  change to this convention, not a local invention.

## Enforcement

A reviewer checks that a tutorial's title, prerequisites, and content agree with its type. An adopter that wants this
mechanical adds a check to its own documentation gate that every tutorial title carries exactly one type name.
