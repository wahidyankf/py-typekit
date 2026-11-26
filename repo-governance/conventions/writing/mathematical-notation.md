---
description: >-
  Requires LaTeX for mathematical notation in Markdown prose, fixes inline and display delimiters and multi-line
  alignment, and keeps math out of code, diagrams, and data files.
when_to_use: >-
  Use when writing a formula in Markdown that a math-aware renderer such as KaTeX or MathJax displays, or when a formula
  renders as raw source.
---

# Mathematical Notation

Mathematics in Markdown prose is written in LaTeX. Plain-text approximations such as `(a/b) * c`, images of equations,
and Unicode symbol art are not used for a formula a reader is meant to read as mathematics.

LaTeX is the one notation that common Markdown renderers display natively, that stays plain text in a diff and a search,
and that has a symbol for everything a formula needs. An image cannot be diffed or searched, and a plain-text
approximation loses grouping and precedence as soon as a formula contains a fraction.

## Inline and Display

| Form    | Delimiters | Placement                                | Use for                                      |
| ------- | ---------- | ---------------------------------------- | -------------------------------------------- |
| inline  | `$...$`    | on the same line as the surrounding text | a variable or short expression in a sentence |
| display | `$$...$$`  | each delimiter on a line of its own      | a formula that stands alone                  |

```markdown
The mean $\bar{x}$ of $n$ observations is:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$
```

Placement is not style. A single `$` on a line by itself is not a display delimiter — on GitHub the formula then renders
as raw source. A display formula therefore always uses `$$`, and a single `$` never leaves its line.

## Multi-Line Formulas

A formula spanning several lines uses the `aligned` environment inside `$$`:

```markdown
$$
\begin{aligned}
(a + b)^2 &= (a + b)(a + b) \\
          &= a^2 + 2ab + b^2
\end{aligned}
$$
```

Never `align`. In LaTeX, `align` opens a display of its own and is not valid inside one, so placing it inside `$$`
depends on a renderer choosing to tolerate an error, and renderers differ in whether they do. `aligned` is the
environment made to sit inside a display, and KaTeX and MathJax both render it.

## Make the Formula Readable

- **Define every symbol** in a list directly after a display formula, unless the surrounding text already has.
- **Keep notation consistent** within a document: one symbol per quantity, and one quantity per symbol.
- **Brace multi-character subscripts and superscripts** — `x_{max}`, `e^{rt}` — because without braces only the first
  character is lowered or raised.
- **Use `\times` or `\cdot` for multiplication**, never `*`, which renders as an asterisk operator.
- **Add a subscript only when it distinguishes something.** Decoration makes a formula harder to read without making it
  more precise.

## Where Math Does Not Go

| Context                                 | Instead                                       | Because                                                                          |
| --------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| a fenced code block or a code comment   | the language's own expression syntax          | code is literal; LaTeX there is never rendered, only misread                     |
| a diagram label                         | plain notation, such as `r = a / b`           | diagram math support varies by renderer and version, and a text diagram has none |
| configuration, JSON, YAML, or data file | plain notation, if a formula is stored at all | a program consumes the value, and LaTeX backslashes need escaping in most data   |
| a plain-text diagram                    | plain notation, per [Diagrams](diagrams.md)   | it is read in a terminal, where nothing renders                                  |

A fenced block that quotes LaTeX source to show how it is written — as the examples above do — is a quotation, not a
place math is meant to render, and is unaffected.
