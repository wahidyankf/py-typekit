---
description: >-
  Fixes how Markdown that displays a fenced code block is itself fenced: an outer fence one backtick longer than the
  fence it holds, each opener closed by one fence of equal length, and no orphan closing fence.
when_to_use: >-
  Use when a Markdown example must show a fenced code block inside it, or when a document's fenced examples render
  broken.
---

# Nested Code Fences

A document that shows how to write Markdown, or displays a README or a template, often has to put one fenced code block
inside another. The inner fence must not close the outer one, and a stray fence must not swallow the prose after it.

## The Rule

- **The outer fence is one backtick longer than the longest fence inside it.** Four backticks hold an example containing
  a three-backtick block; five hold an example containing a four-backtick one.
- **Every opening fence has exactly one closing fence of the same length.**
- **No closing fence is left over.**

A block with no fence inside it uses three backticks, as usual.

A correct example, as it appears in a document's source:

`````markdown
````markdown
## Install

```text
<install command>
```
````
`````

An incorrect one closes both blocks, then leaves a stray three-backtick line after the outer closer:

`````text
````markdown
## Install

```text
<install command>
```
````

```
`````

The leftover line closes nothing. It opens a new block that never closes, so everything after it renders as code.

## Why One Backtick Longer

A CommonMark parser closes a fence at the first later fence at least as long as the opener, so any longer outer fence
would parse. The fixed step is stricter than the parser needs, on purpose: a reader counting backticks can pair every
opener with its closer by length alone, and a reviewer can check the pairing without rendering the file.

Equal length is required for the same reason. A closer longer than its opener still closes the block, but it looks as if
it belonged to an outer fence, and the next reader pairs the fences wrongly.

## Enforcement

A Markdown linter parses an orphan closer as a new, unlabelled code block, so only a rule requiring a language on every
fence reports it. Otherwise an adopter catches it by reviewing changed documents rendered, or with its own check that
pairs every fence with a closer of equal length and reports any fence still open at the end of a file.

## Principles

This convention implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because each fence's
pairing is visible in the source rather than left to a parser's rules, and
[Simplicity Over Complexity](../../principles/simplicity-over-complexity.md), because one fixed step is the only number
a writer needs.
