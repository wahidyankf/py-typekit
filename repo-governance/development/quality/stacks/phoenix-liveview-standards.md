---
description: >-
  Fixes Phoenix LiveView stack choices on top of the Elixir baseline: logic behind contexts, verified routes,
  authorization at every live entry point, a two-pass mount, streams for large collections, forms from changesets, and
  tests through the framework's live test harness.
when_to_use: >-
  Use when building, structuring, or reviewing a Phoenix LiveView application, or when authorizing a live event,
  rendering a form or a large collection, or testing a live view.
---

# Phoenix LiveView Standards

This standard is canonical for Phoenix with LiveView and holds only the choices the framework leaves open. It inherits
[Elixir Standards](elixir-standards.md), whose gates, failure forms, process rules, and test isolation apply unchanged;
a Phoenix LiveView framework skill defers here for each rule.

It implements [Fail Closed](../../../principles/fail-closed.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Pure Functions](../../../principles/pure-functions.md).

## Gates

The Elixir gates cover the web layer too. Paths are
[verified routes](https://phoenix.hexdocs.pm/Phoenix.VerifiedRoutes.html) (`~p`), checked by the compiler against the
router, so a link to a missing route fails the warnings gate instead of a user's click.

## Contexts Own the Application

A live view, controller, or component calls a [context](https://phoenix.hexdocs.pm/contexts.html) module's public
functions and never reaches the repository or a schema query directly. The context is the application boundary: it holds
the decisions, returns tagged tuples, and knows nothing of sockets, assigns, or templates, per
[Functional Core, Imperative Shell](../architecture/functional-core-imperative-shell.md). A callback translates an event
into one context call and the result into assigns.

## Type and Boundary Safety

LiveView maps [Type and Boundary Safety](../code/type-and-boundary-safety.md) as follows.

- **Every entry point is untrusted.** Parameters and event payloads reach `mount/3`, `handle_params/3`, and
  `handle_event/3` from the client, which can send any event with any payload. Each of the three authorizes its action,
  per the [security model](https://phoenix-live-view.hexdocs.pm/security-model.html); authorizing only in `mount/3`
  leaves every later event open. Shared checks run as `on_mount` hooks declared for a `live_session`, and routes needing
  different authorization sit in different sessions.
- **Logging out ends live sessions.** A user's live sockets carry an identifier, and logging out or revoking access
  disconnects them; a connected live view otherwise keeps its access.
- **External data is cast.** Client input passes through a changeset built with
  [`cast/4`](https://ecto.hexdocs.pm/Ecto.Changeset.html), naming the permitted fields; `change/2` is kept for data the
  application produced. Input with no schema uses a schemaless changeset, not raw map access.

## Lifecycle and Rendering

- **Mount runs twice:** first over plain HTTP, then once the socket connects. Subscriptions, timers, and once-only work
  are guarded by `connected?/1`, and neither pass assumes the other happened.
- **Large or growing collections are streams.** A list the server need not keep in memory is a stream, so the socket
  holds no copy of every row; assigns hold only what later renders read.
- **Forms render from a form value.** A template renders `@form` built with `to_form/2` from a changeset, never the
  changeset itself, and shows a field's errors only after the user interacts with it, per the
  [form bindings](https://phoenix-live-view.hexdocs.pm/form-bindings.html).

## Tests

Layers follow [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md).

- Context functions are unit-tested as plain Elixir, outbound boundaries replaced per
  [Test Doubles](../testing/test-doubles.md).
- A live view is tested through the [live test harness](https://phoenix-live-view.hexdocs.pm/Phoenix.LiveViewTest.html),
  which drives the endpoint pipeline in-process, mounting the view, triggering events and form submissions, and
  asserting on rendered elements; running the framework pipeline makes it an integration test. Each authorization rule
  gets a test sending the event as a user lacking the permission.

What coverage measures follows [Meaningful Coverage](../testing/meaningful-coverage.md); generated scaffolding holding
no decision is a named exclusion.

## Documentation

Each context's public functions are its documented interface, with module and function documentation. A live view
documents the events it handles where the template alone leaves them unclear.

## Enforcement

The Elixir gates enforce formatting, warnings, and route verification in the adopter's own build and pull-request gate.
Review applies context boundaries, per-entry-point authorization, the two-pass mount, and stream use.
