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

- [Code as Liability](code-as-liability.md) — what added code buys and costs, and which simpler option lost
- [Code Clarity](code-clarity.md) — visible function phases, caller-meaning names, and intent comments
- [Dependency Selection](dependency-selection.md) — when a dependency is justified, recorded, locked, and removed
- [Mechanize Cross-File Invariants](mechanize-cross-file-invariants.md) — one declared source per multi-file rule,
  generated dependents, gate validation
- [Runtime File Data](runtime-file-data.md) — untracked runtime data files, versioned JSON validated on read, atomic
  replacement writes, paths never built from external input, and one storage profile per process
- [Shell Scripts](shell-scripts.md) — one declared interpreter in strict mode, the committed executable bit, explanatory
  comments, and parsed JSON
- [Type and Boundary Safety](type-and-boundary-safety.md) — the strongest practical static checker, reasoned type
  escapes, and external input validated where it arrives
