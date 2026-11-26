---
description: >-
  Classifies which visual takes a Mermaid diagram and which stays a plain text block, table, or list under the rendered
  rule, and excludes manuals read inside Neovim's help system through a declared path list.
when_to_use: >-
  Use when choosing the form of a visual in a repository that declares the rendered rule, or when a manual is read in an
  editor's help system that cannot render Mermaid.
---

# Visual Classification

Under the rendered rule of [Diagrams](../diagrams.md), a contributor needs one test for which visual becomes Mermaid and
which stays literal; without it, file trees get redrawn as graphs and conceptual drawings stay as ASCII art. The
plain-text rule is unchanged and needs no classification: every conceptual diagram there is ASCII with prose beside it.

## Which Visual Uses What

| Visual                                                         | Form                   | Mermaid type      |
| -------------------------------------------------------------- | ---------------------- | ----------------- |
| flows and pipelines: gate surfaces, delivery steps, data flow  | Mermaid                | `flowchart`       |
| interactions over time: a hook, a runner, a hosted job         | Mermaid                | `sequenceDiagram` |
| states and transitions, such as a document lifecycle           | Mermaid                | `stateDiagram-v2` |
| conceptual hierarchy or ownership: groups, layers              | Mermaid                | `flowchart TD`    |
| data and entity relationships                                  | Mermaid                | `erDiagram`       |
| type and module relationships                                  | Mermaid                | `classDiagram`    |
| file and directory trees                                       | plain `text` block     | none              |
| command output, logs, literal code or configuration            | plain `text` block     | none              |
| terminal or screen layouts, wireframes, keymap grids           | plain `text` block     | none              |
| anything whose exact alignment or characters must be preserved | plain `text` block     | none              |
| exact mappings                                                 | Markdown table         | none              |
| simple sequences                                               | prose or numbered list | none              |

The decision test: if the reader needs the relationships, use Mermaid; if the reader needs the literal characters or
layout, use a `text` block. A table and a prose list are not diagrams.

A mind map is drawn only where the repository's diagram validator supports it. No Gantt chart or timeline is drawn for
planned work, because either implies dates or estimates the work does not promise.

## Neovim Manuals

A manual read inside Neovim's help system cannot render Mermaid, so it may use ASCII art, and the rendered rule does not
reach it:

- **Hand-written help files** are not Markdown, so the rule never applied to them, and a Markdown diagram validator
  never reads them.
- **Markdown that is the source of generated help files** counts as a manual too: a Mermaid block there would reach the
  help system as raw source. Such files keep ASCII diagrams with prose beside them.

The exclusion is declared path configuration, never an ad-hoc skip: the repository lists the generator's source paths in
its diagram validator's exclusion globs, such as `policies.markdown.mermaid.exclude`. Where that list replaces the
standard directory exclusions for the scan, it repeats them. Each adopter records every excluded path with the generator
that justifies it.

## Enforcement

Gated: the repository's diagram validator checks every Mermaid block outside the excluded paths against the accessible
title, description, size limits, and palette.

Unenforced by decision: a conceptual diagram left as ASCII art under the rendered rule is a review finding, because no
reliable heuristic separates a conceptual drawing from a tree, a wireframe, or command output without reading it, and a
guessing check would reject legitimate trees. A stray Mermaid block inside an excluded path is likewise caught by review
only, because the validator reads nothing there.
