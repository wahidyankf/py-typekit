---
description: >-
  Fixes what an architecture model covers, which views it includes, where constraints and links live, and what stays out
  of it.
when_to_use: >-
  Use when writing or reviewing an architecture model's views, prose, and links.
---

# Model Content

## Required Coverage

Each model identifies:

- its scope, the people who use the system, and the other software systems it interacts with;
- its runtime or deployment containers and its external interfaces;
- the material relationships among all of these;
- every data store, whether it persists or is temporary; and
- the process, network, and trust boundaries that matter to its behaviour or security.

It includes a system-context view and every container view that is useful. A component view is included only where it
materially clarifies internal responsibilities. A component view drawn for completeness is detail the next change leaves
stale.

## Boundaries, Not File Layout

The model describes boundaries, responsibilities, and the direction of dependency among them. A rename that moves no
responsibility changes nothing in it.

Every boundary drawn corresponds to something a test can observe. A layer the tests cannot tell apart from its neighbour
is a drawing, not an architecture.

## Constraints Belong in the Model

Architectural constraints are part of the model, stated in searchable prose beside the views: what a component may never
reach, which processes a supervisor may signal, what a tool refuses to assume. A constraint recorded only in code is one
the next design discussion will not know about.

## Prose Carries Every Claim

Every relationship a diagram shows is also stated in the prose around it. That prose is not a caption. It is the
searchable, screen-reader-reachable form of the same claims, and it is what a reviewer compares with the code.

## Links

The model links to the application's behaviour specifications, and each implementing project's README links back to the
model. A model nobody reaches from the code is a model nobody updates.

## What Stays Out

- implementation detail below the documented component level;
- inventories of modules or files that duplicate the source tree; and
- guidance on using the system, which belongs in user documentation.

The specifications describe what the system must be. User documentation describes what someone can do with it.
