---
description: >-
  Indexes the conventions layer, which holds the choices a repository makes for itself rather than durable constraints.
when_to_use: >-
  Use when locating an existing convention or deciding whether a new rule belongs in this layer.
---

# Conventions

A convention records a choice. Two repositories could reasonably decide differently and both be right; what matters is
that one of them decided, wrote it down, and now applies it consistently.

That is what separates this layer from the one above it. A principle explains why something is true regardless of
repository. A convention says which of several defensible options this repository picked.

- **`security/`**: what enters history, who reads real values, what leaves
- **`structure/`**: how files, directories, and documents are shaped and named, and how governance and plans are
  organized

## Directory Map

- [Markdown Line Length](markdown-line-length.md) — the 120-character limit on every Markdown line, from RHINO
- [Markdown Visualizations](markdown-visualizations.md) — ASCII diagrams in `text` blocks, never Mermaid, from RHINO
- [Writing Style](writing-style.md) — brief, clear comments, commit messages, and development notes
- [Security](security/README.md)
- [Structure](structure/README.md)
