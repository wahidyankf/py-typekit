---
description: >-
  Defines what counts as a secret, which reads and channels the prohibition covers, and what stays outside it.
when_to_use: >-
  Use when judging whether a value, read, or channel falls under the private-key and secret access rule.
---

# Scope and Boundaries

A secret is any password, token, API key, or private key. The prohibition covers reads through a shell, SSH client,
script, scanner, hash, archive, indexer, or other tool; suppressed output authorizes nothing. Agents may inspect names,
paths, and metadata without reading contents, treating a suspected key as protected without opening a header to classify
it.

Public keys and SSH configuration are separate artifacts. Authentication-agent signing that opens no private-key file is
outside this prohibition, which imposes no general SSH ban. Values move only through a hidden prompt, standard input, or
a child environment, never an argument, log, chat, commit, or tracked file. Local development means loopback services
and dummy or example values such as `.env.example`. This convention requests no key removal, relocation, redaction,
replacement, or rotation; [No Secrets in Tracked Files](../no-secrets-in-tracked-files.md) still governs what enters
version history.
