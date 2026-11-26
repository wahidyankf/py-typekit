---
name: dependency-bump-planning
description: >-
  Inventories dependency manifests, classifies each candidate bump with security and stability clearance, gets human
  approval, and authors a backlog plan without editing any manifest.
when_to_use: >-
  Use for a periodic dependency-hygiene sweep, before a release to snapshot eligible bumps, or when a runtime's
  long-term-support line advances.
---

# Dependency Bump Planning

## Entry

The working tree is clean, and the repository records the eligibility rule its dependency bumps follow.

- `scope` (`string`, optional): globs limiting which manifests are inventoried. Default: every dependency-pinning
  manifest.
- `ecosystems` (`string`, optional): package ecosystems to include. Default: every ecosystem found.
- `as-of-date` (`string`, optional): eligibility's reference date, as `yyyy-mm-dd`. Default: today.
- `plan-identifier` (`string`, optional): the backlog plan's folder name. Default: `dependency-bump`.

## Sequence

1. **Fix the date and the scope.** Resolve `as-of-date`, compute any cutoff the eligibility rule derives from it, and
   record both verbatim. A dirty working tree ends the run `fail` before anything is read.
2. **Inventory every manifest in scope:** language manifests, toolchain and runtime pins, container base images,
   pipeline action references, and pipeline-pinned tool versions. Lockfiles and workspace-internal references follow
   their manifests and stay out. Record source, ecosystem, package, and current version.
3. **Research candidates by ecosystem.** One batch per ecosystem, in parallel since none reads another's result, handed
   over per [Web Research Delegation](../../development/agents/web-research-delegation.md). Per package: latest version
   and date; any long-term-support line; the newest version the eligibility rule admits; advisories on current and
   proposed versions from multiple authoritative sources; whether an actively exploited vulnerability affects the
   current pin, escalating it regardless of eligibility; and whether the proposed version is withdrawn, deprecated, or
   known broken, with the newest admitted version that is not.
4. **Write the clearance report.** Tabulate bumps (package, current, proposed, eligibility path, advisory status,
   clearance), escalations and holds first, written per
   [Temporary Files](../../conventions/structure/temporary-files.md).
5. **Checkpoint: approve the bump set.** Present the report path and table, escalations first, and confirm the plan
   identifier. Options:
   - **approve** continues to step 6 with the full set;
   - **trim** removes or defers named rows, then continues to step 6;
   - **reject** ends the run `rejected`; and
   - **discuss** returns to this checkpoint.
6. **Author the backlog plan.** Run [Planning](../plan/plan-planning.md) for a backlog plan named `plan-identifier`,
   handing over the inventory, approved table, report path, recorded date, and this definition of done:
   - each in-scope manifest pins its approved version exactly;
   - each lockfile moves with its manifest and re-audits clean, per
     [Dependency Selection](../../development/quality/code/dependency-selection.md);
   - no actively exploited vulnerability remains pinned;
   - every waiver or hold is recorded where the repository records exceptions;
   - a changed license has a
     [Dependency-License Decision](../../conventions/structure/licensing/002-dependency-license-decisions.md); and
   - every affected project's gates pass.
7. **Hand back.** Report the plan path, report path, and verdict, noting the plan snapshots the recorded date: if
   execution starts much later, eligibility is re-researched first.

## Exit

A successful run leaves `plan-path` (`directory`, at `plans/backlog/<plan-identifier>/`), `clearance-report` (`file`, at
`<reports-dir>/dependency-bump-planning-<yyyy-mm-dd-hh-mm>-<uuid>-report.md`), and `verdict` (`enum`: `pass`, `partial`,
`fail`, `rejected`); `pass`, `partial`, and `fail` follow the plan quality gate, and a dirty tree also ends `fail`. No
manifest or lockfile has changed.

`rejected` leaves the clearance report and no plan.

## Example Usage

```text
Run dependency-bump-planning for the container and pipeline ecosystems, as of today.
```

## Related Workflows

- [Planning](../plan/plan-planning.md) authors the plan in step 6.
- [Execution](../plan/plan-execution.md) performs the bumps once the plan is promoted.

## The Plan Is the Deliverable

The run never edits a manifest, updates a lockfile, or installs anything. Surveying stays apart from changing so a
person approves the exact set first and the change runs under a plan's checklist and gates.

## What an Adopter Decides

| Decision         | Options and trade-off                                                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eligibility rule | A soak window admits only versions some days old, preferring long-term-support lines: problems surface first, fixes arrive later. Latest stable adopts fixes at once, unproven. |
| advisory sources | More sources catch what one misses at more research per package; one source is quick but inherits its gaps.                                                                     |

## Principles

This workflow implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md): every proposed version
carries its eligibility path and clearance; and [Reproducibility](../../principles/reproducibility.md): the plan pins
exact versions and moves each lockfile with its manifest.
