---
name: 001-external-nx-cache-eviction
description: >-
  Records external Nx cache eviction boundaries and why deleting uncommitted work is permanent.
when_to_use: >-
  Use when a task uses Nx and external cleanup may evict its cache, or when classifying uncommitted artifacts.
---

# External Nx Cache Eviction

If this repository or a task uses Nx, treat its local task cache as regenerable. Keep unique authored work, secrets, and
configuration outside it.

For manual external machine cleanup, require explicit human approval before evicting that cache during active builds or
tasks. Record acceptance of possible cache-read/write failure, reruns, cold tasks, and immediate regrowth.

Resolve the actual configured `cacheDir`, including overrides, and use the installed Nx's
[`nx reset --only-cache`](https://nx.dev/docs/reference/nx-commands#nx-reset). Preserve `.nx/workspace-data`, daemon
state, remote cache, and other build outputs. Never remove all `.nx`.

This consumer awareness grants no cleanup authority. Existing task-owned cleanup guards and scheduled sweeper policies
keep their scope.

**Enforcement: unenforced by decision**, because approval and cache classification require human judgment.

## Deletion Is Permanent

Version control restores only committed work, so deleting an uncommitted artifact is permanent; hence `unknown` routes
to investigation, never removal.
