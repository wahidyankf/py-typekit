---
description: >-
  Requires a hosting platform's build to run every prerequisite the workspace task runner declares for the build target,
  and requires traced server output to include the generated and workspace files the runtime reads.
when_to_use: >-
  Use when configuring or reviewing how a hosting platform builds an application whose task-runner build target has
  prerequisites, or whose server output bundles only traced files.
---

# Deployment Build Parity

A hosting platform that builds an application runs its own configured build command. When that command is not the task
runner's build target, the platform never resolves the prerequisites the target declares. A generation step that runs
before every local build can be missing from every deployed build: the deployment succeeds, and the application later
finds its generated files absent at runtime.

Scoped to adopters that deploy through a platform building from its own command, in a workspace whose task runner
declares build prerequisites, or whose server output bundles only traced files. This standard implements
[Reproducibility](../../principles/reproducibility.md) and
[Explicit Over Implicit](../../principles/explicit-over-implicit.md), and builds on
[Task Runner Target Standards](task-runner-target-standards.md).

## The Rule

- **The build target is the source of truth.** Its prerequisite chain says what must run before the framework build. The
  platform configuration follows it; a copy of the chain is never edited on its own.
- **Calling the target satisfies the chain.** A platform command that invokes the runner's build target resolves the
  prerequisites itself, and needs no copied list.
- **Otherwise the platform build runs the whole chain,** every prerequisite in dependency order, then the framework
  build.
- **Both change together.** A change that adds, removes, or reorders a prerequisite updates a copied platform build
  command in the same change. A removed prerequisite leaves the command too, so no stale step keeps running.
- **Paths start where the platform starts.** The platform runs its command from the root directory its project settings
  name, often the application directory rather than the repository root. Confirm that setting before writing a script
  path into the command.
- **A newly deployed application is audited first.** Read its build target's prerequisites before writing its platform
  configuration.

## Traced Output

A framework that bundles server output by tracing imports statically ships only the files that code imports. Files the
build generates, content read from disk at runtime, and files from other workspace packages are invisible to that trace,
so the bundle leaves them out while the build still reports success. Declare every such directory in the framework's
trace-include setting.

## Why the Failure Is Silent

Neither build fails. The local build passes because the task runner ran the chain, and the platform build passes because
the framework build succeeds without the generated files. The defect surfaces only when a request reaches code that
reads a missing file, and a runtime fallback that regenerates the file can then exceed the platform's execution time
limit.

## Example

Illustrative only, with one platform and framework among many: a workspace whose task runner declares two generation
prerequisites for a web application's `build` target, deployed on Vercel as a Next.js standalone build.

| Concern          | Where it is declared                                       | What it holds                                                         |
| ---------------- | ---------------------------------------------------------- | --------------------------------------------------------------------- |
| build target     | the task runner's project configuration                    | prerequisites `generate-index` and `generate-search-data`, then build |
| platform command | `buildCommand` in the platform's project configuration     | both generation scripts, in that order, then the framework build      |
| traced output    | `outputFileTracingIncludes` in the framework configuration | the directories the generation scripts write                          |

```json
{
  "buildCommand": "node scripts/generate-index.mjs && node scripts/generate-search-data.mjs && next build"
}
```

## Enforcement

An adopter checks in its own gate that each deployed application's platform build command invokes its build target or
covers every prerequisite of that target, in order, and that traced output declares each generated directory. Which
applications carry a platform configuration, and their current state, stays in the adopter's own documentation.
