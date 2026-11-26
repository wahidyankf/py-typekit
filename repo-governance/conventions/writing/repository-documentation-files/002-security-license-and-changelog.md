---
description: >-
  Fixes the contents of a security policy, requires unmodified standard license text, and structures the changelog as
  categorized, reader-facing entries per release.
when_to_use: >-
  Use when writing a security policy, adding a license file, or recording a release in the changelog.
---

# Security, License, and Changelog

## Security Policy

`SECURITY.md` gives someone who has found a vulnerability a private way to report it. It contains:

| Section            | States                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------- |
| Supported versions | which versions receive security fixes, and the end-of-support policy                         |
| Reporting          | a private contact such as `<security-contact>`, what to include, and when to expect a reply  |
| Response process   | how a report is acknowledged and assessed, the timeline for a fix, and the disclosure policy |
| Security updates   | how fixes are released and how users are notified                                            |

A report includes a description of the vulnerability, steps to reproduce it, its potential impact, and a suggested fix
if there is one.

The reporting section says plainly not to report a vulnerability in a public issue. A researcher who finds no private
channel uses the public one, and the vulnerability is then disclosed before it is fixed.

A repository whose users operate under a compliance regime also states which standards it addresses, how data is
protected, and how authentication and authorization are designed — or links to where each is documented.

## License

`LICENSE`, with no extension, at the root, holds the standard text of the chosen license with only its placeholders
filled in: the copyright holder and year.

Standard text is never edited. A modified license is a different license: license-detection tools stop recognizing it,
and every user needs legal review to learn what the edit changed.

## Changelog

`CHANGELOG.md` begins once releases are versioned, and follows [Keep a Changelog](https://keepachangelog.com/) with
[Semantic Versioning](https://semver.org/):

```markdown
# Changelog

## [Unreleased]

### Added

- A new capability, described for the person upgrading.

## [1.1.0] - YYYY-MM-DD

### Fixed

- A defect, described by its visible effect.
```

Entries sit under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security`, newest release first, with an
`Unreleased` section collecting changes before they ship. The release date in a version heading is content, not the
maintenance metadata [No Manual Date Metadata](../no-manual-date-metadata.md) forbids.

A changelog is written for the person upgrading, never dumped from commit subjects. A commit log answers what was typed;
a changelog answers what changed for the reader, and a security fix buried among forty commit subjects is a fix nobody
applies.

## Contributor Recognition

`AUTHORS.md` or `CONTRIBUTORS.md` is optional. Where present it is one of three things, and says which: a maintained
list, a list generated from history, or a link to the hosting platform's contributor page.
