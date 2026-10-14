---
description: >-
  Forbids agents from opening private-key contents anywhere, hands each secret step to the operator on the clipboard,
  and limits session records, delivery, and leak review to leak-free paths.
when_to_use: >-
  Use before opening a suspected private key, before running any command that reads a real secret, before recording a
  secret in session text, or before reviewing a change for leaks.
---

# Agent Secret Access

These rules bind coding agents anywhere they act, inside or outside every repository.

R1: Agents must not open or read private-key contents anywhere, including outside every repository.

R2: Each secret step is exactly one copy-ready command carrying its working directory, placed by the agent on the
operator clipboard; the operator runs it in their own terminal, entering each secret at a hidden prompt only, and
replies with the success word the step names; the agent continues only on it.

R3: Agents must never request, handle, or record secret values, full outputs, or screenshots, and must avoid any script
or interaction that prints, echoes, logs, or otherwise exposes a secret to the harness session; diagnosis uses exit and
error codes alone, and only local-development secrets (loopback services, dummy/example values such as `.env.example`)
may appear in session records.

R4: The secret session opens only inside the phase that needs it and locks before any review, pause, or PR handoff.

R5: Agent-assisted delivery applies only with a proper pipeline and secrets management (tracked wrapper, closed one-word
outputs, leak screens, green gates); elsewhere the agent stops at the secret boundary.

This library has no secret-handling surface; these rules still bind agent behavior if one ever appears.

R6: An agent may operate the leak review after reading every commit at the pinned head against the three leak classes; a
verdict without that reading is fabrication.

Reason: regtech [HUMAN] removes value exposure from the session, and proper pipelines earn faster delivery.

Committed files stay under [No Secrets in Tracked Files](no-secrets-in-tracked-files.md); this rule governs the agent's
own reads, runs, and session text.

## Disposition

Unenforced by decision; review checks the observations. No automated gate settles it.
