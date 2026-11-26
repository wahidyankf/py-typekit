---
description: >-
  Governs starting or restarting the development server of an application users can reach while work continues: reuse
  the identified existing process, keep it where its owner watches it, and restart as soon as its inputs change.
when_to_use: >-
  Use when the development server of a user-reachable application must be started or restarted, including after a failed
  start or a dependency or configuration change.
---

# Restart Discipline

This module shares the scope of [Live-Service Continuity](../live-service-continuity.md): an application users can reach
while work on it continues. The [Invariants](001-invariants.md) apply first.

## Reuse the Server Already Running

1. Before editing anything that triggers a restart, check the expected local endpoint. Where users reach it through a
   route, verify that route and establish a separate healthy backend before touching the only watched server.
2. Identify the existing server process from evidence: its working directory, the process running, and its recent
   output. Stop it there, wait for it to exit, and start the replacement in the same place.
3. Never start a competing server on the same port because the existing one was not found. If no existing server can be
   identified, report that instead of guessing a target, and decide explicitly whether a new server is in scope.

## Keep the Server Where Its Owner Watches It

Never run a watched development server as a background process owned by an agent session. Its output leaves the place
the person is watching, and its lifetime follows the agent's session instead of the terminal it belongs to, so it can
vanish or linger with nobody seeing why.

## Restart When Its Inputs Change

After a dependency, configuration, runtime, or supervision change, restart or replace the server immediately, as part of
the same batch of changes. Never leave a running code reloader to discover the changed inputs on a later user request,
where the failure lands on the user instead of on the change.

When a build mode changes settings fixed at compile time, compile with exactly the environment that will start the
server. A mismatch disqualifies the candidate: keep routing on the healthy backend, rebuild, and verify again rather
than bypassing validation.

## Verify the Start

Confirm startup from the server's own output, then make read-only requests to the local endpoint and one critical route.
On a failed start or health check, keep or restore routing to the previous healthy backend before other work resumes.
