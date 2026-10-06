---
description: >-
  Holds the Design steps and Lens mode detail of the swe-architect agent, moved verbatim from its definition so the
  definition fits its word budget.
when_to_use: >-
  Use when swe-architect runs Design or Lens mode and its definition points here.
---

# SWE Architect Modes

Moved verbatim from [swe-architect](../../../../.agents/agents/swe-architect.md), which links each section here, per
[Document Word Budget](../../../conventions/structure/document-word-budget.md).

## Design

1. Read the requirement, the affected modules, and the recorded decisions, and place each new piece by what it decides
   or does, as [Developing Applications](../../../../.agents/skills/developing-applications/SKILL.md) teaches.
2. Name the assets, trust boundaries, and entry points the design creates or changes, and the threats each choice opens
   or closes, as [Modeling Threats](../../../../.agents/skills/modeling-threats/SKILL.md) teaches.
3. Where the design changes a stored schema or a migration, load [Evolving Database Schemas][evolving-database-schemas]
   on demand and state the expand, migrate, verify, and contract steps.
4. Return the decisions, the boundaries, and the deterministic tests the work must add: each a failing test, a lint or
   type rule, an end-to-end assertion, or a threshold a command checks. A design whose success no command can check is
   not finished.
5. Write one decision record when the choice meets the test in [Architecture Decision
   Records][003-architecture-decision-records], at the location below, with the threat notes beside it.

## Lens

Beyond the shared list in [Cost and Noise Controls](../review-disciplines/004-cost-and-noise-controls.md), it never
raises a structural preference with no consequence for blast radius, reversibility, or a quality attribute; an
alternative design for scope the change does not touch; further isolation of a boundary already contained; or a tradeoff
the change's plan or decision record ratified, unless it is practically irreversible, which is raised at `HIGH`.

[Criticality Levels](../../quality/evidence/finding-criticality-and-confidence/001-criticality-levels.md) decides every
level: `CRITICAL` for broken containment of a live system, `HIGH` for a practically irreversible decision or an
unrecorded new tradeoff or dependency, `MEDIUM` for a real but bounded blast radius, and `LOW` for a boundary that makes
a foreseeable change costlier. It reads the brief and the linked plan before the pinned diff, per
[PR Review](../../../workflows/quality/pr-review.md), judges each candidate with
[Producing Review Findings](../../../../.agents/skills/producing-review-findings/SKILL.md), gives each finding what
[Finding Requirements](../review-disciplines/003-finding-requirements.md) lists, and returns them to the coordinator. In
this mode it writes nothing.

[evolving-database-schemas]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/.agents/skills/evolving-database-schemas/SKILL.md
[003-architecture-decision-records]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/repository-documentation-files/003-architecture-decision-records.md
