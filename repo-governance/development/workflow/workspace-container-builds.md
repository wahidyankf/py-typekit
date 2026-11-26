---
description: >-
  Fixes how a container image is built for one application in a linking, hoisting package-manager workspace: a
  repository-root build context, a per-application build file, explicit hoisted dependencies, and a recorded
  package-resolution strategy.
when_to_use: >-
  Use when writing or debugging a container build for one application of a workspace repository, especially when a
  shared package or a hoisted dependency fails to resolve.
---

# Workspace Container Builds

Scoped to adopters that build container images for individual applications of a package-manager workspace that links
internal packages into a shared dependency directory and hoists transitive dependencies to its root, for example an npm
workspace built with Docker. A container build sees only its context and what the build copies in, so those links
resolve on the host and break in the image.

This standard implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md),
[Reproducibility](../../principles/reproducibility.md), and
[Root Cause Orientation](../../principles/root-cause-orientation.md).

## The Rules

- **Repository-root build context.** A build of any application that uses a shared workspace package sets its context to
  the repository root and names its build file by path. A context scoped to the application directory cannot reach the
  shared packages, and the build fails at the step that copies them.
- **One build file per application,** kept in that application's directory and referenced from the root context.
- **Every build definition agrees.** When a build file changes, every compose file and pipeline overlay that builds the
  same application changes with it. An overlay left behind passes locally and fails in the pipeline.
- **Hoisted dependencies are handled explicitly.** The workspace hoists shared transitive dependencies to the root
  dependency directory, so an image that installs only the application's declared dependencies lacks them, and the
  failure names a module the application never imports directly. Handle them as the recorded strategy requires, never by
  relaxing peer resolution or mounting host directories.
- **An ignore file keeps the root context small,** excluding version-control data, local build output, and development
  files, but never a directory a later build stage copies.

## Adopter Decision: Resolving Internal Packages

| Strategy                   | How                                                                                                                                                       | Gains                                                                                                                          | Costs                                                                                                                                                                |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| inject package sources     | install the application's dependencies, then copy each internal package's source and package manifest into the dependency directory under its scoped name | a small install limited to one application, and each internal dependency is a visible line in the build file                   | every new internal dependency adds copy lines to the build file and every overlay, and a hoisted transitive dependency is declared in the application's own manifest |
| copy resolved dependencies | install at the workspace root in an earlier stage, then copy the resolved root dependency directory, and any package-level one, into the build stage      | links are resolved at install time, nothing is maintained per package, and hoisted dependencies arrive with the root directory | a larger install and image layer carrying the whole workspace's dependencies, and a missed package-level directory surfaces only at runtime                          |

Record the strategy. Under injection, copy both the source and the package manifest: resolution by file path works
without the manifest, but type declarations and export maps that read it do not.

## When an Application Gains an Internal Dependency

Steps 1 and 2 change declarative configuration, so `swe-developer` makes them, per
[SWE Delegation](../agents/swe-delegation.md).

1. Update its build file for the recorded strategy.
2. Update every compose file and pipeline overlay that builds the application, and confirm each uses the root context.
3. Build the image locally before pushing, and confirm the pipeline job that builds it passes.

## Why

A copy line per dependency is a declaration: the image holds exactly what the build says, locally and in the pipeline
alike. Relying on link resolution inside the image is implicit, and its failure reports a missing module whose real
cause is a link pointing outside the image. Fixing the context and the copy is the repair at that cause.
