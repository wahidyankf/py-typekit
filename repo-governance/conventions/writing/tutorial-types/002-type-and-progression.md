---
description: >-
  Separates a tutorial's type, which fixes its shape, from a repository's progression model, which fixes depth along its
  own stages of mastery, and keeps the two independent of each other.
when_to_use: >-
  Use when a repository keeps its own stages of mastery for learning material and a tutorial has to be placed in them.
---

# Type and Progression

A tutorial's type fixes its shape: the kind of document it is and the coverage it promises, as
[Tutorial Types](../tutorial-types.md) defines. Some repositories also keep a progression model — their own named stages
a learner moves through toward mastery of a subject. Where one exists, a tutorial's stage fixes its depth in that model,
and its type still fixes its shape.

## Two Axes, Kept Separate

- A tutorial's type and its stage are chosen separately; neither is inferred from the other.
- One stage can hold several types: a single stage's material may include a short orientation, a full walkthrough, and a
  set of annotated examples, each shaped for a different reader.
- A type name never stands in for a stage, and a stage never selects a type.

## Why They Stay Apart

A stage answers how far into the subject the learner has come; a type answers what kind of document serves them there.
Folded into one label, the repository loses one of the two answers: either each stage allows only one shape, or each
shape is read as a stage.

A repository without a progression model needs nothing beyond its tutorial types.

## Enforcement

A reviewer checks that no type name stands in for a stage and no stage dictates a type. An adopter that wants this
mechanical adds that check to its own documentation gate.
