---
description: >-
  Separates delivering a change to the trunk from deploying it: each project is promoted by moving its own pointer
  branch, gated so no other push builds it, confirmed by the finished build, and cut over to a domain separately.
when_to_use: >-
  Use when adding or changing deployment configuration, promoting a commit to an environment, deciding whether
  automation may promote, or pointing a domain at a project.
---

# Deployment Promotion

Landing on the trunk delivers a change without deploying it. A deployment separately promotes one chosen trunk commit to
one environment of one project, every part explicit.

Scoped to adopters whose hosting platform builds each deployed project from a branch; tag, pipeline, and built-artifact
promotion are out of scope.

This standard implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md) and
[Evidence Over Assertion](../../principles/evidence-over-assertion.md). Development branches follow
[Integration Path](integration-path.md); these pointers are the environment branches it keeps apart.

## Promotion Pointers

- **One pointer branch per deployed project and environment,** named after both, such as `prod-<project>`. A shared name
  would let one project's promotion build another.
- **A pointer receives no commits.** It only moves to a commit already on the trunk, and the platform builds from it;
  nobody deploys a locally built artifact.
- **A lagging pointer is normal:** newer commits are delivered, not yet promoted.
- **Forward moves only.** Promoting a newer trunk commit fast-forwards the pointer. Any other move is a force update
  that follows [No Destructive Git Operations](no-destructive-git-operations.md), so a rollback is a revert on the
  trunk, promoted forward.

## Who Moves a Pointer

A production pointer moves only by a deliberate promotion of a chosen commit, made by whoever the adopter records as
deployment authority. No workflow, hook, scheduled job, or plan step advances it; an automatic advance would turn every
landing into a deployment. Before it moves, the commit is on the trunk with its gates passed, and a promotion run from a
checkout starts on the trunk with a clean working tree.

For a non-production tier the adopter records one option:

| Option           | The pointer moves when                                                | Trade-off                                                                                                                                                             |
| ---------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| deliberate only  | someone promotes it, as for production                                | every change is chosen, and the tier lags until someone acts                                                                                                          |
| gated automation | a workflow that passed the full test suite on a trunk commit moves it | the tier tracks the trunk with evidence attached; a bypass, allowed only while the gate itself is broken and the tier must ship urgently, is recorded with its reason |

## Build Gating

Each project builds only from its own pointer. A build started by any other ref is cancelled before it runs, for example
by an ignored-build step comparing the building branch with the pointer's name, so trunk pushes spend no deploys and one
promotion never builds another project.

The platform's own production-branch setting must name the same pointer. That setting lives outside the repository, and
a mismatch deadlocks silently: trunk pushes start production builds the gate cancels, and pointer pushes produce
previews that never reach the domain. Check it when a project is first connected and after any reconnect, which can
reset it to the default branch.

## A Push Is Not a Deploy

The platform builds asynchronously; from the push, failure and success look identical.

1. Find the deployment whose commit matches the promoted commit. A newest deployment for an older commit means the build
   has not started.
2. Follow it to a terminal state, as [Remote Status Polling](remote-status-polling.md) requires.
3. Report ready with its address, failed with the failing build step, or cancelled, usually by a newer promotion.
4. Where the platform's status cannot be read, say so and fall back to the pointer's pipeline result and a request
   against the live address. Never report success on the push alone.

Name a project by its readable name, never an opaque platform identifier, in messages and committed artifacts.

## Domain Cutover

Pointing a live domain at a project is a separately authorized act; neither landing deployment configuration nor a
passing gate authorizes it. Configuration may be committed for a project with no pointer yet, which keeps it inert.

Deployment configuration names each secret's variable and where it is set, never its value, per
[Environment Variable Contract](../../conventions/security/environment-variable-contract.md).
