---
description: >-
  Indexes the code standards: what added code and dependencies must justify, how code stays clear, how cross-file rules
  are mechanized, how shell scripts and runtime data files are written, and where types are checked.
when_to_use: >-
  Use when adding code or a dependency, writing a shell script or a runtime data file, or keeping a rule that spans
  several files consistent.
---

# Code Standards

Code standards. They answer what code and dependencies must justify, and how code, scripts, and data files stay clear
and consistent.

## Directory Map

- [Dependency Selection](dependency-selection.md) — when a dependency is justified, recorded, locked, and removed
- [Type and Boundary Safety](type-and-boundary-safety.md) — the strongest practical static checker, reasoned type
  escapes, and external input validated where it arrives
