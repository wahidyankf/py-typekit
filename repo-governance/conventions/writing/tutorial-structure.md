---
description: >-
  Fixes the ordered sections every tutorial carries: introduction, prerequisites, learning objectives, explain-then-show
  content sections with checkpoints, summary, and next steps, plus the parts of concept sections and recipes.
when_to_use: >-
  Reach for this while drafting or reviewing a tutorial, or to decide whether a learning document is a tutorial at all.
---

# Tutorial Structure

Every tutorial carries the same sections in the same order. A learner then knows where to look before reading, and a
reviewer can check a tutorial's shape without first reconstructing its author's intent.

## What Counts as a Tutorial

A tutorial is learning-oriented, teaching through experience as the learner works and understanding builds
incrementally; Cookbook recipes are the problem-solving exception. Any other document listing the steps toward a goal
without teaching the concepts behind them is a how-to guide, and this convention does not apply to it.

The two fail differently. A how-to padded with teaching slows down the reader who only needed the steps; a tutorial
stripped to steps produces a learner who can repeat the procedure and cannot adapt it.

## Required Sections, in Order

| #   | Section             | Carries                                                                                                                                                                |
| --- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Title and metadata  | a title naming the type — see [Tutorial Types](tutorial-types.md) — and the metadata the documentation system requires, stating the outcome rather than only the topic |
| 2   | Introduction        | why the subject matters in real work, and what the learner achieves                                                                                                    |
| 3   | Prerequisites       | the knowledge and setup required before starting, or an explicit "none"                                                                                                |
| 4   | Learning objectives | measurable achievements of the learner, not the content covered                                                                                                        |
| 5   | Content sections    | the learning path, one concept per section, with checkpoints                                                                                                           |
| 6   | Summary             | the key takeaways, consolidated for recall                                                                                                                             |
| 7   | Next steps          | concrete ways to go further                                                                                                                                            |

Section names describe required content; heading wording and level are the adopter's choice.

## Why This Order

The first four sections answer the questions a learner asks before starting: is this worth the time, can I follow it,
and what will I be able to do. A learner who discovers a missing prerequisite halfway through has already spent the time
that section exists to save.

The introduction leads with the outcome rather than a definition. A definition met before the reader knows why it
matters has nothing to attach to.

The summary turns what was learned into something to recall, and next steps keep the tutorial from being a dead end.

## Prerequisites Are Explicit, Even When Empty

"None" is a statement, and it is written. A missing prerequisites section is indistinguishable from one the author
forgot, and the learner cannot tell which.

## Objectives Describe the Learner, Not the Content

An objective states what the learner can do afterwards — "configure a retry policy", not "retries". A list of topics
tells the learner what the tutorial mentions; a list of abilities tells them how to check whether it worked.

## Content Sections Explain, Then Show

Each content section introduces one concept, says why it matters, explains it, then demonstrates it through a worked
example, and may add a practice exercise for the learner.

The explanation comes first. A concept met for the first time inside an example is learned as a pattern to copy: the
learner reproduces the example and does not recognise the concept in a different shape.

Sections build forward: none depends on something introduced later.

## Cookbook and By Example

Two modules fix the inside of a content section:

1. [Concept Sections](tutorial-structure/001-concept-sections.md) — the parts of a section teaching one concept.
2. [Cookbook and By Example](tutorial-structure/002-cookbook-and-by-example.md) — how those types reshape sections, and
   a recipe's parts.

## Checkpoints Confirm Before Moving On

A checkpoint gives the learner a concrete criterion to check before moving on, such as a result to compare against or a
question to answer. "You should now understand" offers no criterion, so it is not a checkpoint.

A checkpoint catches a misunderstanding near where it arose, before it surfaces somewhere the learner cannot trace.

## Enforcement

A reviewer checks section presence, order, and the explain-then-show pattern. An adopter that wants the section order
checked mechanically adds that check to its own documentation gate, mapping each section to its chosen heading; whether
an example follows its explanation stays a review judgement.
