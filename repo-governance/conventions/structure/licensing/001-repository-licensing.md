---
description: >-
  Requires one default licensing model stated explicitly at the root, inherited by new content, with third-party terms
  preserved and every exception documented beside its directory.
when_to_use: >-
  Use when a directory or package is added, third-party code is vendored, or the placement of license files is chosen.
---

# Repository Licensing

## One Model, Stated at the Root

A repository has exactly one default licensing model, stated explicitly at its root:

- an open-source or other license, in a root `LICENSE` file;
- proprietary terms, in a root `LICENSE` file; or
- for a private repository that grants nothing, an explicit statement that no license is granted and all rights are
  reserved.

New directories, files, applications, libraries, and specifications inherit the root model unless they are a documented
exception. A package manifest declares the same terms as the directory it describes; a package offered under no terms
says so with its manifest's explicit no-license value, rather than leaving the field to a tool's default.

Silence is not a model. A repository with no stated terms leaves each reader to guess, and readers guess differently.

## Third-Party Terms Are Kept

Vendored, forked, or archived third-party code keeps its original license, in its own `LICENSE` file, and is never
relicensed under the root model. Third-party code is admitted only when its terms are compatible with the root model and
with how the repository distributes it.

Material brought in from outside keeps its owner's terms even in a repository that grants nothing: sourced documents,
images, and references stay under their original licenses.

## Exceptions Are Documented

Every directory under terms other than the root model carries its own `LICENSE` file and appears in one root-level
notice that lists each exception with its origin and license. One copyright-notice format is used for every license file
the repository authors.

The notice is the one place a reader checks what differs from the root. An exception documented only inside its
directory is found by whoever happens to open that directory.

## Decide Where License Files Live

| Choice                                                                      | Gains                                                                                       | Costs                                             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| a `LICENSE` in every application and library, even when it matches the root | terms are visible without tracing inheritance, and one project can be relicensed on its own | one identical file per project to keep identical  |
| the root `LICENSE` alone, with per-directory files only for exceptions      | nothing to keep in sync, and any per-directory file signals a real difference               | a reader must know that absence means inheritance |

Per-project files suit a permissively licensed repository whose projects are reused separately. Root-only suits
proprietary or ungranted terms, where a per-directory file would only repeat the root. Under either choice, the rules
above still hold.

An adopter checks mechanically, in its own gate, that manifests agree with their directory's terms and that every
third-party directory appears in the notice.
