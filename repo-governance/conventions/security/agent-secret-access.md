---
description: >-
  Forbids agents from opening private-key contents or running secret access themselves, requires handoff to the user,
  and limits recorded secrets to local-development values.
when_to_use: >-
  Use before opening a suspected private key, before running any command that reads a real secret, or before recording
  a secret in session text.
---

# Agent Secret Access

R-A: Agents must not open or read private-key contents anywhere. Listing metadata, such as a directory listing, is not
reading contents; suspected private-key bytes are never opened to check what they are.

R-B: When private-key or secret access is necessary, agents must hand the command or script to the user, who executes it
in a separate terminal session; agents must not run the access step themselves.

R-C: Agents must not record secrets in the session, except secrets usable only in local development (loopback and
localhost services, dummy or example values such as `.env.example`).

Reason: the user reserves all private-key and secret access to themselves.

Committed files stay under [No Secrets in Tracked Files](no-secrets-in-tracked-files.md); this rule governs the agent's
own reads, runs, and session text.

## Disposition

Unenforced by decision: no mechanical check settles it, so review checks the observations.
