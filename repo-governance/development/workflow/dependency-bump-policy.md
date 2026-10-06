---
description: >-
  Requires every dependency, runtime, and base image bump to pin an exact version chosen by the long-term-support,
  sixty-day soak, or security waiver path, cleared against vulnerability sources under a written cutoff date.
when_to_use: >-
  Use when bumping a dependency, runtime, toolchain, base image, or pipeline action version, or when reviewing a change
  that does.
---

# Dependency Bump Policy

Every bump meets three constraints before it merges: an exact pin, so every install reproduces it; a stability path, so
a fresh release's breakage profile is known before it is adopted; and vulnerability clearance, so known vulnerabilities
are patched rather than inherited.

This standard implements [Reproducibility](../../principles/reproducibility.md),
[Explicit Over Implicit](../../principles/explicit-over-implicit.md), and
[Root Cause Orientation](../../principles/root-cause-orientation.md).

## Classify, Then Take the Newest Eligible Version

Classify each package, runtime, toolchain, base image, and pipeline action into one path, then pin the most recent
version that path allows. An update bot may open a bump, but a person classifies it on one path before it merges.

- **long-term support** — Applies when: the upstream designates a long-term-support line; Take: the latest patch on that
  line, whatever its age, provided it is vulnerability-clean
- **soak** — Applies when: there is no long-term-support line; Take: the latest vulnerability-clean version released at
  least 60 days before the bump date
- **security waiver** — Applies when: no version is both past the soak and vulnerability-clean; Take: the most recent
  version that patches the vulnerabilities, or the security-recommended long-term-support release

A long-term-support line already carries the upstream's own soak and curation. Sixty days is the minimum window for a
community to surface regressions and security issues; upstreams without such a line commonly ship patches about monthly,
so the window takes in the next cycle's fixes.

## Write the Cutoff Down

For every bump, record the bump date, the cutoff date (the bump date minus 60 days), and that soak-path versions must be
released on or before the cutoff. Anyone revisiting a release or vulnerability date can then check the decision.

When the work carrying a bump takes more than 60 days to merge, the cutoff has moved. Rerun eligibility before the final
merge, to catch newly eligible versions and newly disclosed vulnerabilities.

## Clear Every Selected Version

Check each selected version, on every path, against the national vulnerability database, the advisory databases covering
its ecosystem, and the project's own security notices. Record one result per package with the change, in its pull
request description or in the plan that introduces the bump:

| Result          | Means                                                         |
| --------------- | ------------------------------------------------------------- |
| clear           | no vulnerability was on record for this release when checked  |
| clear, patch-of | this release is the fix for each vulnerability listed with it |
| waiver          | the security waiver path applied                              |

## A Waiver Is a Durable Record

A waiver names the package and the pinned version, each vulnerability that requires the recent version with a link to
its advisory, each severity, the pinned version's release date, a brief justification, and who applied it. It is kept in
a long-lived waiver register at a location the adopter records, so the exception outlives the change that made it.

## Pin Exactly

Every version specification is an exact string, except the pipeline-action form below: no range operator, no `latest`,
no wildcard. This policy does not cover workspace-internal references, which resolve to local paths, lockfiles the
tooling maintains, or type-only development dependencies with no security surface.

| Where                              | Required form                                               |
| ---------------------------------- | ----------------------------------------------------------- |
| package manifest dependencies      | an exact version                                            |
| runtime and toolchain version pins | an exact version                                            |
| container base images              | an exact tag, with a digest preferred for production images |
| hosted pipeline actions            | a pinned major version, or an exact commit                  |

A range installs whatever was newest when the install ran, which is a version nobody reviewed. An exact pin, unlike a
pinned major version, makes the reviewed version the installed one.

## Enforcement

An adopter checks the exact-pin form after every manifest edit in its own hook or gate, and runs its ecosystem's
vulnerability audit after every lockfile update.
