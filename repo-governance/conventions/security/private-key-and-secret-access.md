---
description: >-
  Agents never open private-key contents anywhere; each secret step is one clipboard command the user runs and answers
  with one word; nothing secret reaches the harness session; delivery follows proper pipelines.
when_to_use: >-
  Use when an agent might touch secrets, when handing a secret step to a person, or when operating a leak review.
---

# Private-Key and Secret Access

Agents must not open or read private-key contents anywhere. Every secret step is one copy-ready command carrying its
working directory, placed by the agent on the operator clipboard; the operator runs it in their own terminal and replies
with the success word the step names. Nothing secret reaches the harness session. Sessions lock before any pause.
Agent-assisted delivery needs a proper pipeline. A leak review is a real read of every commit at the pinned head.

Reason: human-only steps keep values out of the session, and proper pipelines earn faster delivery.

## Obligations

1. Agents must not open or read private-key contents anywhere, including outside every repository.
2. Each secret step is exactly one copy-ready command carrying its working directory, placed by the agent on the
   operator clipboard; the operator runs it in their own terminal, entering each secret at a hidden prompt only, and
   replies with the success word the step names; the agent continues only on it.
3. Agents must never request, handle, or record secret values, full outputs, or screenshots, and must avoid any script
   or interaction that prints, echoes, logs, or otherwise exposes a secret to the harness session; diagnosis uses exit
   and error codes alone, and only local-development secrets may appear in session records.
4. The secret session opens only inside the phase that needs it and locks before any review, pause, or PR handoff.
5. Agent-assisted delivery applies only with a proper pipeline and secrets management (tracked wrapper, closed one-word
   outputs, leak screens, green gates); elsewhere the agent stops at the secret boundary.
6. An agent may operate the leak review after reading every commit at the pinned head against the three leak classes; a
   verdict without that reading is fabrication.

The [details](private-key-and-secret-access/README.md) hold the scope and boundaries, the verification observations, and
the enforcement disposition.

## Related

- [No Secrets in Tracked Files](no-secrets-in-tracked-files.md)
- [Security Conventions](README.md)
