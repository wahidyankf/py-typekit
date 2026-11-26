---
description: >-
  Indexes the security conventions governing what may enter version history, who may read real secrets, and what may
  leave a repository under what proof.
when_to_use: >-
  Use before committing or publishing anything sensitive, or when adding a safety control.
---

# Security Conventions

Everything here guards one of three concerns: what enters version history, which no later commit takes back; who may
read real values; and what leaves the repository, which no later deletion recalls.

| Convention                                                        | Governs                                                                          |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [No Secrets in Tracked Files](no-secrets-in-tracked-files.md)     | where credentials live, whatever the visibility, and what remediates a leak      |
| [No Machine-Specific Values](no-machine-specific-values.md)       | keeping one machine's paths, names, and addresses out of commits                 |
| [Environment Variable Contract](environment-variable-contract.md) | the committed key template, key naming, validation, and the secret census        |
| [Agent Environment-File Access](agent-env-file-access.md)         | which real environment files an agent never reads, writes, or edits by any route |
| [Private-Key and Secret Access](private-key-and-secret-access.md) | agent reads of private keys anywhere, who runs key access, and session records   |
| [Public Outbound Safety](public-outbound-safety.md)               | what must be screened before anything is published                               |

## Directory Map

- [No Secrets in Tracked Files](no-secrets-in-tracked-files.md)
- [No Machine-Specific Values](no-machine-specific-values.md)
- [Environment Variable Contract](environment-variable-contract.md)
- [Agent Environment-File Access](agent-env-file-access.md)
- [Private-Key and Secret Access](private-key-and-secret-access.md)
- [Public Outbound Safety](public-outbound-safety.md)
