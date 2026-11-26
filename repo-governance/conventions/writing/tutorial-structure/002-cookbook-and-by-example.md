---
description: >-
  Fixes how Cookbook and By Example tutorials reshape content sections, and the six ordered parts of a cookbook recipe,
  from its title and problem to its solution, explanation, pitfalls, and links onward.
when_to_use: >-
  Reach for this while writing or reviewing a Cookbook recipe, or the examples of a By Example tutorial.
---

# Cookbook and By Example

Two tutorial types reshape the content sections. A Cookbook is organized by problem: each recipe states one problem and
its solution, and recipes need not build on one another. A By Example tutorial teaches through annotated examples, and
each example still opens with a brief explanation, a few sentences long, before its annotated code.

A recipe's six parts replace a concept section's parts and the checkpoint a content section carries. Besides its
explanation and annotated code, a By Example example keeps two concept-section parts: a diagram only where one
clarifies, and a key takeaway.

## Recipe Shape

| #   | Part            | Carries                                                                                                       |
| --- | --------------- | ------------------------------------------------------------------------------------------------------------- |
| 1   | Title           | an action naming the problem solved, specific enough to search for, with no difficulty label                  |
| 2   | Problem         | the problem in a few sentences, with its constraints and edge cases                                           |
| 3   | Solution        | complete, runnable, annotated code ready to copy and paste, every import included                             |
| 4   | How it works    | the approach and the insight behind it, without repeating the code's own annotations                          |
| 5   | Common pitfalls | the mistakes readers make with this problem, each with what to do instead                                     |
| 6   | Related recipes | links to recipes for neighbouring problems, each saying how it relates, as pointers rather than prerequisites |

## Why Recipes Look Like This

A recipe's reader arrives with a problem, usually from a search, and leaves once it is solved. The title names the
problem because that is what the reader searched for; a difficulty label names a level, and the reader did not come for
a level.

The solution is complete because an incomplete one hands the reader a second problem. Pitfalls are listed because a
solution that works in the recipe can still fail the first time it meets the reader's own code.

Each recipe can be used without reading any other, and recipes are grouped by problem area rather than by level. A
grouping by level would make a reader judge their own level before reaching the answer.

## Enforcement

A reviewer checks the six parts in order, that the solution runs as given, and that no recipe title carries a difficulty
label.
