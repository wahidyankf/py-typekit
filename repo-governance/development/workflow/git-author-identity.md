---
description: >-
  Resolves commit author identity only from user-level git configuration, forbids repository-local identity overrides,
  and forbids agents from setting identity at any scope.
when_to_use: >-
  Use when configuring commit identity, when a repository's local configuration may hold a user override, or when an
  agent is about to set a name or email.
---

# Git Author Identity

Authorship is a claim about who did the work, and once pushed it is permanent. Identity therefore comes from one
declared place per person, never from a setting tucked inside a single repository.

This standard implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md) and
[Reproducibility](../../principles/reproducibility.md).

## Why a Local Override Is the Hazard

Git reads a repository's local configuration after the user's, and the last value read wins. A `[user]` block stored
locally therefore wins for every commit made in that repository. It asks for no confirmation, prints nothing when a
commit is made, and stays until someone removes it, so a wrong identity can accumulate over many commits before anyone
reads the log. Correcting authorship that was already pushed means rewriting published history.

## The Rule

1. **No repository-local identity.** A repository's local configuration holds no `user.name` and no `user.email`. Any
   value is a violation, including one matching the person's real identity, because the mechanism is the fault rather
   than the value.
2. **User-level configuration only.** Identity resolves from the person's own git configuration, in the home directory
   or the XDG location. System-level configuration is reserved for shared automation hosts. A pipeline may set its
   service identity in its own definition, by variables or a write to its own checkout's configuration, which rule 1
   does not cover; that is platform configuration, not an agent setting identity, and the local check below skips that
   checkout.
3. **More than one identity through conditional includes.** A person needing a different identity for a group of
   repositories adds an `includeIf "gitdir:<directory>/"` entry to their user-level configuration, pointing at a file
   that sets it. For a single commit, `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, and
   `GIT_COMMITTER_EMAIL` override configuration without writing to any file.
4. **Agents never set identity.** No agent runs `git config user.*` at any scope, edits a `[user]` block, or supplies
   identity through the environment. An agent that finds a local override stops and reports it; removing it is the
   person's decision.

```ini
# user-level git configuration
[user]
    name = <person-name>
    email = <personal-email>

[includeIf "gitdir:<work-directory>/"]
    path = <work-identity-file>
```

## Checking and Removing

In a compliant repository, `git config --local --get-regexp '^user\.'` prints nothing. A person removing an override
runs `git config --local --unset user.name` and `git config --local --unset user.email`, then
`git config --local --remove-section user` once the section is empty, and repeats the check.

## Enforcement

For agents the rule is behavioural and lives in their instructions. An adopter wanting a mechanical check verifies, in
the pull-request gate, the author and committer identity of every commit in the range, since identity is commit metadata
and no hook runs at commit time. The query above stays the local check; it must read local configuration only, so that a
conditional include in user-level configuration still passes.
