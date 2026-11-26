---
description: >-
  Governs small runtime data kept as local files: never tracked, versioned JSON validated on read, written by atomic
  replacement, located without external input, and rooted in one storage profile resolved at process startup.
when_to_use: >-
  Use when an application, tool, or agent persists state in local files instead of a database, or when reviewing code
  that locates, reads, or writes one.
---

# Runtime File Data

Some state is too small or local for a database: one user's progress, a saved preference, a tool's operational record.
Kept in files, it fails in ways a database would prevent: a crash leaves half a document, a hand edit goes unvalidated,
a request chooses the path, or a test writes to the real data. Each rule below closes one.

This standard implements [Fail Closed](../../../principles/fail-closed.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Reproducibility](../../../principles/reproducibility.md).

## Scope

Small, private data that a running application, tool, or agent creates and changes. Source, committed configuration,
committed test inputs, and agent scratch output, which
[Temporary Files](../../../conventions/structure/temporary-files.md) governs, are out of scope.

## Never Tracked

Version control ignores every runtime data directory; the only tracked entry allowed is an approved placeholder keeping
an empty directory present.

Runtime data changes every run and can hold personal data, so a committed copy is either a leak or a stale snapshot
mistaken for a fixture. Each tool that walks the tree also needs its own exclusion, as Temporary Files explains.

## One Directory per Record Kind

Each kind of record lives in its own subdirectory below the data root, such as
`<data-root>/users/<user-id>/<activity>/progress.json`. A directory mixing kinds cannot be backed up, cleared, or
migrated for one kind without touching the others.

## Versioned JSON, Validated on Read

Each file is UTF-8 JSON carrying an explicit schema version. The reader checks the version and validates the whole
document before using any part. A failing file is reported as an error naming its path, never repaired by guesswork or
replaced with defaults.

A data file outlives the code that wrote it: an older release, a hand edit, or an interrupted copy leaves an unexpected
shape. Without a version the reader cannot tell old from corrupt, and a reader substituting defaults overwrites the
user's real data on its next write.

## Written by Atomic Replacement

A writer never changes a data file in place. It writes the complete new document to a temporary file in the same
directory, flushes it to storage, and renames it over the original.

Readers then see the old or new document, never a mixture, and a crash leaves the old intact. The temporary file shares
the directory because a rename is atomic only within one filesystem. Concurrent writers to one file serialize read,
change, and replace; two replacements from one read lose an update.

## Paths Never Come From External Input

No file path derives directly from browser input, a request, or other external value. The code maps the input to an
identifier validated against a strict pattern or looked up, builds the path from the data root and that identifier, then
confirms the resolved path, symbolic links followed, still lies inside the root.

A path taken from input reaches wherever the input says: a parent-directory segment or planted symbolic link turns a
request for one record into a read or write anywhere the process can reach.

## One Storage Profile per Process

At startup each process resolves exactly one storage profile, such as production, development, or a single test run, and
uses its root for life, never switching. When the root is missing or cannot be proven right, the process stops rather
than falling back to another profile.

A fallback hides its triggering misconfiguration: the process seems to work on another profile's data until damaging it.
A test process never reaches production data; [Test Data Isolation](../testing/test-data-isolation.md) owns that rule
and the per-run boundary a test must prove.

## Enforcement

An adopter enforces these in its own tests and lint: a check that data directories are ignored, and single helpers,
which every other caller must use, for resolving the profile, building a path, and writing a file.
