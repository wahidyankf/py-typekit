---
description: >-
  Sets how a user-facing plan closes: a deployment-configuration sweep with a live smoke test, a checklist kept in step,
  a sign-off that gates archival, a bounded near-end retest of the running system, and a check on collapsed content.
when_to_use: >-
  Use when executing a user-facing plan that moves files or nears archival, or when deciding whether it may be archived,
  or when retesting another plan's reachable behaviour near its end.
---

# Closing a User-Facing Plan

These rules continue the numbering of [Authoring a User-Facing Plan](001-authoring-a-user-facing-plan.md). They bind
while the plan executes and before it is archived.

## 8. Deployment Configuration Is Code

A plan that moves or renames files sweeps every deployment configuration that names a path, such as hosting build
commands, container build files, and pipeline definitions. After deploying, it runs a smoke test against the live
address.

A green local build never runs the hosted build, which can still point at the old path. Only the deployed service shows
whether the configuration moved with the files.

## 9. The Checklist Stays in Step

Each checklist item is ticked as it lands, as [Plan Execution](../../../../workflows/plan/plan-execution.md) requires.
Where an executor also keeps a separate as-built log, the log and the boxes are reconciled in the same change and never
left divergent. A phase whose work is done but whose boxes are not reads as unfinished, and costs a reconciliation pass
nobody planned.

## 10. Archival Waits for the Sign-Off

The done and archival criteria for a user-facing change include the visual sign-off from rule 1, observed on the
deployed build, for every declared viewport class and every supported locale. Archival is blocked until it is recorded.

A sign-off that covered only the default locale is incomplete. Finding that out after archival makes it a defect in an
archived plan, handled under
[Phase Boundaries and Delivery Choices](../../../../conventions/structure/plans/011-phase-boundaries-and-delivery-choices.md).

## 11. A Near-End Retest of the Running System

After implementation and any sign-off, and before archival, the plan runs one retest round against the running system:

| Surface                    | The round looks for                                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| browser-rendered interface | correctness, usability, and design fidelity, in every supported locale                                                         |
| API operation              | contract conformance, status codes, error shape, payload limits, authentication and authorization, pagination, and idempotency |

A plan that changes both surfaces runs both rounds. A plan with neither surface that still changes behaviour someone can
reach, such as a command-line tool, a library, a hook, or a pipeline, exercises that behaviour through its own interface
and records what ran. Only a plan with no reachable behaviour change is exempt, and it states the exemption.

The sign-off confirms that the screen matches the design. It does not hunt for inconsistent behaviour, accessibility and
navigation defects, first-use confusion, or drift from the token layer, and those are the defects that pass green gates.

Findings are recorded and resolved as follows:

- each defect becomes a new unchecked checklist item in a labelled follow-up section, attributed to the round that found
  it;
- every defect item is fixed and ticked before archival, and deferring one needs explicit permission from the plan's
  owner, given only when a fix is genuinely impossible; and
- a proposed specification change is a proposal, not a defect: it is triaged, an accepted one becomes a specification
  update under [Specification Maintenance](../../evidence/specification-maintenance.md), and a deferral records its
  reason under the item.

The round is bounded as
[Exploratory and Usability Review](../../../../workflows/quality/exploratory-usability-review.md) and
[Quality Gate Results](../../manual-verification/001-quality-gate-results.md) bound it. A clean round passes at once,
and no finding triggers an automatic rerun.

## 12. Collapsing Is Not a Density Fix

When a fix for a crowded region hides part of it behind a disclosure control, examine the expanded state before
accepting the fix. Collapsing shortens the region without making it any less dense. If the revealed content's
typography, grouping, and handling of absent values were never specified, the complaint returns the moment someone
expands it.
