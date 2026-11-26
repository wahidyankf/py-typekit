---
name: release-cut
description: >-
  Publishes a version by building immutable, digest-recorded artifacts from one verified clean revision and tagging it,
  never moving or replacing a released tag.
when_to_use: >-
  Use when publishing a versioned artifact that consumers pin by version and digest.
---

# Release Cut

## Entry

The revision is on the default branch via the repository's integration path, and the release is authorized. An adopted
[Upstream Tool Defects](../../development/workflow/upstream-tool-defects.md) standard authorizes releasing a covered
tool's merged fix.

- `version` (`string`, required): the version to publish, chosen by the change class
  [Public Contract](../../development/quality/architecture/public-contract.md) assigns.
- `revision` (`string`, required): the full commit identifier to release.

## Sequence

1. **Confirm the checkout.** The local default branch equals the remote one, reconciled after the last integration, not
   assumed; the checkout is exactly at `revision`; the working tree is clean, untracked files included.
2. **Confirm the version is unused.** No `version` tag exists locally or on the remote. If one does, end the run and
   choose the next version: a tag is never deleted or moved.
3. **Run the full gate** on `revision`; a release skipping a gate publishes whatever it would have caught.
4. **Confirm the documentation describes this version.** The changelog records it, per
   [Security, License, and Changelog](../../conventions/writing/repository-documentation-files/002-security-license-and-changelog.md),
   and a [Docs Quality Gate](../quality/docs-quality-gate.md) verdict on subject `all` is recorded.
5. **Build only through the release build command.** One scripted command, run where the build-location decision places
   it, builds each artifact in a clean checkout of `revision`, and itself refuses when the checkout head differs from
   `revision` or `revision` is not a full commit identifier.
6. **Record the digests** through the build tooling, never by hand, covering every step-5 artifact.
7. **Tag `revision` and publish** the artifacts and digests. The tag name and release text pass the outbound screen like
   any publication, per [Public Outbound Safety](../../conventions/security/public-outbound-safety.md).

## Exit

Success leaves `tag` (`string`), naming `version` on `revision`, and `artifacts` (`file-list`, at `<output-dir>/*`) with
the digest file covering each. Every artifact traces to `revision`.

A failure before step 7 leaves no tag, so nothing needs undoing. A defect found after step 7 is not repaired in place;
it becomes a new run with a new version. A failure inside step 7 ends the run `partial`: the tag stays, nothing
published is replaced, and the next version is cut.

## Example Usage

```text
Run release-cut for version 1.4.0 at revision <full-commit-id>.
```

## Related Workflows

- [Dependency Bump Planning](dependency-bump-planning.md) can snapshot eligible bumps first.
- [Dev Artifact Clean-Up](dev-artifact-clean-up.md) removes the release checkout and build scratch afterwards.

## Adopter Decision: Build Location

| Option                | Where steps 5 and 6 run                                       | Trade-off                                                                   |
| --------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| local, before tagging | one machine builds every platform before step 7               | a broken build stops the run before tagging; artifacts are cross-built      |
| native runners        | inside step 7, triggered by the tag on each platform's runner | each executable has started on its platform; a build failure leaves the tag |

Record the option. Under native runners, verify the published release before announcing: an artifact per supported
platform, each matching its digest.

## A Released Tag Never Moves

Consumers pin a release by version and digest; a replaced tag silently falsifies every such pin, since the version
string is unchanged. A published mistake is fixed by publishing the next version: never by replacing a tag, re-uploading
an artifact, or weakening digest verification to accept a bad one. A consumer bootstrap refusing a mismatched digest is
correct; the fix belongs upstream.

An adopter enforces this with forge tag protection and consumer digest checks; the build command's refusals enforce
step 5.

## One Build Path

Nobody can reproduce a hand-built artifact; a clean checkout of the exact revision keeps output independent of the
machine and its disk. Promoting a running service's release adds candidate, migration, and traffic rules, which
[Release Cutover](../../development/quality/delivery/live-service-continuity/002-release-cutover.md) owns.

## Principles

This workflow implements [Immutability](../../principles/immutability.md): a published version gets a successor, not an
edit; [Reproducibility](../../principles/reproducibility.md): every artifact comes from one clean revision through one
command; and [Fail Closed](../../principles/fail-closed.md): an existing tag, dirty tree, or mismatched revision stops
the run.
