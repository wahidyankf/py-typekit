---
description: >-
  Requires comments to explain the reason for code choices rather than narrate visible operations.
when_to_use: >-
  Use when writing or reviewing source, tests, scripts, or their comments.
---

# Code Clarity

## Purpose

A comment earns its place when it preserves a reason that the code cannot show.

## Standards

Explain why code is needed or shaped this way instead of describing what it plainly does. Comment a non-obvious
invariant, safety boundary, ordering, or workaround where a maintainer will need that reason. State a script or public
API's purpose when its name alone does not make the boundary clear. Follow
[Writing Style](../../../conventions/writing-style.md) for brevity and language.

## Examples

"Keep retries bounded to avoid duplicate requests" gives a reason. "Retry the request" narrates the next line.

## Validation

Review reads each comment beside the code it explains; a linter cannot judge whether its reason is useful or true.
