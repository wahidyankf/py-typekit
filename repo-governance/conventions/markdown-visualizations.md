# Markdown Visualizations

Use a visualization when it makes relationships, sequence, state, hierarchy, or another nontrivial structure materially
easier to understand. Use prose for a simple fact and a table for an exact mapping. A diagram added as decoration, or
duplicating what a neighbouring table already says better, is worse than no diagram.

## Requirements

- Draw every conceptual diagram as a Mermaid block carrying an accessible title and description. Prefer the smallest
  diagram type that carries the point, such as a flowchart, a sequence diagram, or a state diagram.
- Give each diagram its `accTitle` and `accDescr`, so the meaning survives where the diagram does not render.
- Precede each diagram with one sentence that states what it shows. That sentence carries the meaning for a screen
  reader, and for anyone searching the text.
- Keep every visible node label segment within 32 Unicode grapheme clusters and every edge label segment within 24,
  splitting a longer label with `<br/>`.
- Never encode meaning through color alone. Combine color with clear labels and, when distinctions matter, different
  shapes or line styles.
- Take fills from blue `#0173B2`, orange `#DE8F05`, teal `#029E73`, or brown `#CA9161`, with white `#FFFFFF` for the
  default shape; borders are black `#000000`; text is black or white `#FFFFFF`. Do not use red, green, yellow, or pink
  shades, including for success or failure.
- Declare colors with `classDef` hex values, including a complete `classDef default`, rather than color names or
  scattered inline styles. Use black borders, white text on dark fills, and black text on light fills.
- Keep every line within the [Markdown line length](markdown-line-length.md).
- Label each box, and name a category in the label, such as `(system)` or `[check]`.
- Choose the smallest drawing that carries the point. Where a graph would cross its own edges, draw it as a layered
  tree.
- Place the diagram beside the prose it supports, and update it in the same change as the structure it depicts.

Directory trees are not diagrams; they stay in `text` blocks in their usual form. Literal command output, commit
messages, file-name patterns, and example invocations stay in `text` blocks too.

## Enforcement

`policies.markdown.mermaid.authoring-rule: rendered` in [`repo-config.yml`](../../repo-config.yml) makes the `mermaid`
gate check every Mermaid block: it must declare `accTitle` and `accDescr`, take every colour from the palette, keep each
label within its grapheme limit, and stay legible on light and dark backgrounds. For local changed-diagram checks, use
RHINO's `--file` once per changed Markdown file; pre-push stays full-repository. Whether a drawing is clear is a
judgement for review.

The Mermaid validator runs against the release the repository's [`rhino.lock`](../../rhino.lock) pins.
