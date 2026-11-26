---
description: >-
  Confines end-to-end tests to the public boundary a user or caller meets, gives each case its own temporary fixtures,
  keeps the suite out of fast hooks, and guarantees browser cleanup.
when_to_use: >-
  Use when writing, placing, or scheduling an end-to-end test for a command-line tool, service, or browser application,
  or when an end-to-end run leaves state behind.
---

# End-to-End Testing

An end-to-end test earns its cost by observing the system exactly as its user does. Once it reaches inside, it becomes a
slow unit test that proves less than a fast one would.

This standard implements [Reproducibility](../../../principles/reproducibility.md) and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Observe Only the Public Boundary

| Subject             | Driven through                                                                | Observed as                                                       |
| ------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| command-line tool   | the built executable, with arguments, standard input, and a working directory | exit code, standard output and error, and the resulting file tree |
| service             | requests to the exact served origin                                           | status, headers, body, and externally visible side effects        |
| browser application | a real browser at the exact served origin                                     | rendered state, URL, network responses, and data the page exposes |

A test that imports a function, a private module, or an internal store has left the boundary. Keep such checks at the
unit or integration layer, and keep in this suite only the journeys no narrower layer can prove.

## Every Case Owns Its Fixtures

Each case creates its own temporary fixture tree and removes it afterwards. No case reads a shared fixture directory,
relies on files another case left behind, depends on execution order, or touches a tree it did not create.

An order-dependent suite passes on one machine and fails on the next with no change to the code, and nobody can tell
which result to believe. Rules for the data inside a fixture belong to [Test Data Isolation](test-data-isolation.md).

## Use the Exact Origin

Point the browser or client at the exact origin the system serves. A loopback alias is not interchangeable with it:
cookies, cross-origin rules, and redirects all key on the precise host, so a test at a different name proves a different
configuration.

Fail the run when an unexpected process already answers the chosen port, instead of testing whatever happens to listen.

## Assert What the Action Produced

Each assertion observes state, a URL, a response, a file, or a document element that the action under test produced.
Text present on every page, a status that was already there, or the mere absence of an error proves nothing about the
action.

No unconditional skip, focus marker, expected-failure baseline, or silent fallback for a missing step is allowed. Each
one lets the suite report success for work it never did. The adopter enforces this ban in its own gate or CI.

## Keep the Suite Out of Hooks

End-to-end runs never execute at the `pre-commit` or `pre-push` surface that
[Surfaces and Mutation](../../../conventions/structure/repository-configuration/003-surfaces-and-mutation.md) declares.
A slow hook is the hook that gets bypassed, and a bypassed hook checks nothing.

Run the journeys a change affects before reporting it complete. The complete suite runs in a `scheduled` or `main`
workflow the repository declares, not per pull request, because it is the slowest suite and may depend on outside
services; every repository with a remote and end-to-end tests has that workflow. A scheduled failure is a real failure:
fix it at its cause, as [Root Cause Orientation](../../../principles/root-cause-orientation.md) requires, rather than
re-running or quarantining it.

A repository with no pull-request gate runs the suite in its local landing gate where its dependencies are local, per
[Automated Quality Gates](../checks/automated-quality-gates.md).

## Clean Up Even After Failure

A browser run closes every page, tab, and context it opened, in cleanup that runs whether the test passed, failed, or
timed out. It never closes a tab it did not open, which may belong to a person working in the same browser.

A failed cleanup fails the run. Leaked browsers and servers hold ports and state that corrupt the runs that follow.

## Related Standards

- [Behaviour-Driven Development](behaviour-driven-development.md) binds end-to-end scenarios to the shared corpus.
- [API Testing](api-testing.md) adds the direct request an API change requires.
- [Manual Verification](../manual-verification.md) owns what a person must still check in a rendered interface.
