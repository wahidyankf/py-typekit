---
description: >-
  Keeps work open after a push until every pipeline workflow covering the changed blast radius passes on the pushed
  commit, and defines the local replacement gate for a repository with no remote.
when_to_use: >-
  Use right after pushing a change and before calling it done, or when deciding what verification replaces a hosted
  pipeline in a repository that has no remote.
---

# CI Post-Push Verification

A push is not the end of the work. The work is done when every pipeline workflow covering what the push changed has
passed on the pushed commit.

Local hooks are necessary and not sufficient. They are kept fast on purpose, so they leave out integration suites,
end-to-end suites, and deployment workflows, which are precisely what the pipeline exists to run. A green hook is a
prerequisite for pushing, not a verdict on the change.

This standard implements [Evidence Over Assertion](../../principles/evidence-over-assertion.md) and
[Root Cause Orientation](../../principles/root-cause-orientation.md).

## The Rule

After every in-scope push, whether to a pull-request branch or directly to the trunk:

1. **Find the blast radius.** List the changed paths and every component depending on them. Shared code reaches each of
   its consumers, not only the component the change was written for.
2. **Start every covering workflow.** Trigger each one that does not start on its own for this push.
3. **Follow it to a terminal result.** Poll at a spaced interval under a declared ceiling, as
   [Bounded Convergence](bounded-convergence.md) requires. Never use a streaming watch or a tight loop; both spend the
   hosting service's request budget and can lock out the rest of the work.
   [Remote Status Polling](remote-status-polling.md) sets the interval, trigger discipline, and rate-limit recovery.
4. **Fix a failure at its cause.** Push the fix and start again from step 1.

Which workflows cover which components is the adopter's to record, next to the workflows themselves.

## Scope

In scope is any push touching source, tests, build or dependency configuration, pipeline definitions, or a contract
other components consume. An adopter may exempt paths no workflow reads, such as prose-only documentation, by listing
them.

## Not Done

- Calling work done while a covering workflow is pending or red.
- Skipping verification because the local hooks passed.
- Leaving a scheduled run to catch the problem later.
- Treating a failure found after the push as belonging to somebody else.

## Adopter Decision: No Remote

A repository without a remote has no pipeline to wait for, and the rule must not quietly shrink to nothing. Every
repository records which option it takes:

| Option          | Completion requires                                                                                                                                                                                                                                                              | Trade-off                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| hosted pipeline | the rule above, after each push                                                                                                                                                                                                                                                  | evidence from a representative environment, at the cost of waiting and a request budget |
| no remote       | the diff is read for unrelated files and credentials, each failure is fixed at its cause and the gate rerun, the complete local gate passes, no remote is configured, the checkout is the declared branch, and no plan or workflow step fetches, pushes, or opens a pull request | no network dependency and no hosted evidence, so the local gate must carry everything   |

Under the no-remote option, finding a remote configured is a stop rather than a warning: something changed the
repository's shape, and only its owner decides whether to remove it. An adopter enforces those checks inside its own
local gate.
