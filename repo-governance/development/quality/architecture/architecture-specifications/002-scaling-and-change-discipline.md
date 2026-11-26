---
description: >-
  Fixes when an architecture model splits into an entrypoint and detail files, and requires every boundary change to
  update the model in the same change with the impact assessment recorded.
when_to_use: >-
  Use when a model has grown hard to scan, or when a change may alter a documented actor, container, interface, data
  flow, or boundary.
---

# Scaling and Change Discipline

## Keep One File While It Works

Keep a single model file while a reader can move from system context to the relevant container or component without
scanning unrelated detail, and while every diagram stays legible at ordinary document width.

Split when any of these holds:

- separate views of subsystems, components, deployment, or runtime behaviour answer different readers' questions and
  crowd the entrypoint;
- a diagram cannot stay legible without losing material boundaries or relationships;
- unrelated areas need separate constraints or separate behaviour traceability; or
- areas that evolve independently keep producing unrelated review noise or merge conflicts.

Never split for anticipated growth alone.

## How to Split

- The original file stays the canonical entrypoint and holds the scope, the system context, shared constraints, and an
  index of the detail files.
- Detail files sit in a sibling directory named after the entrypoint, each named for its view or area.
- Every statement and every diagram has exactly one home. A detail file does not repeat the entrypoint.
- Each detail file links back to the entrypoint, to its behaviour specifications, and to its implementing projects.

## Read Before Changing

Before changing production code, configuration, tests, or specifications, read the relevant model, behaviour
specifications, and tests, and assess the architectural impact before implementing anything.

## Update in the Same Change

Update the model in the same change whenever the implementation changes a documented:

- actor, system, container, or component responsibility;
- relationship or interface;
- runtime or deployment boundary;
- data store or data flow; or
- security or trust boundary.

Synchronize with the **final** boundaries: not before, while the shape is still being decided, and not after, when the
change has landed and the model is briefly false. A boundary that moved beside a model that did not is a defect in that
change, not a follow-up.

## A No-Op Is Recorded

A behaviour-only change, or one below the documented component level, needs no diagram churn when every architectural
statement stays accurate. Do not edit the model merely because a change was nearby.

Either way, the delivery report records the assessment: the update made, or a verified no-op. An unrecorded assessment
cannot be told apart from one that never happened.

## It Complements Executable Specifications

The model replaces neither behaviour specifications nor tests, and they do not replace it. They prove what the system
does; the model states the boundaries it must keep.

Before closing the change, confirm that the model describes the final implemented state, that its links resolve, and
that the affected tests pass. An adopter enforces link resolution and its diagram rule in its own documentation gate.
