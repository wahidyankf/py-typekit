---
name: adoption
description: >-
  Indexes the two adoption workflows: comparing a repository against the catalog, and copying named artifacts into it on
  explicit request.
when_to_use: >-
  Use when comparing a repository with this catalog, or when adopting a named artifact from it.
---

# Adoption Workflows

One workflow: Adopt Artifact copies what a user named from the `ose-rules` catalog. The catalog's read-only assessment
is not adopted here.

| Workflow                            | Writes                                                  |
| ----------------------------------- | ------------------------------------------------------- |
| [Adopt Artifact](adopt-artifact.md) | only the artifacts a user named, plus their integration |

## Directory Map

- [Adopt Artifact](adopt-artifact.md)
