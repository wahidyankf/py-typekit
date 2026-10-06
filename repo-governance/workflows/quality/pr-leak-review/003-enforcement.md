---
name: 003-enforcement
description: >-
  Makes the leak review a mechanical precondition through a commit-by-commit screen, hosted checks, and required status,
  and lists the decisions an adopter records once.
when_to_use: >-
  Use when adopting the leak review, or when wiring its screen, hosted checks, and branch protection into a repository.
---

# Enforcement

A precondition stated only in prose is a convention someone forgets. An adopter enforces the leak review in three
layers; each fails closed.

## The Screen

The repository's outbound screen runs at the pre-push hook and on every pull-request range. It screens the range commit
by commit: each commit's added lines at the line numbers they occupy, its file names, its message, and the ref names. A
merge contributes what it resolved beyond the automatic merge. Content the range did not add is not screened again, so
the screen binds from adoption onward. Its shapes include absolute home paths, private addresses, and internal
hostnames, beside a credential scanner.

The screen matches shapes; the review reads context. Neither replaces the other.

## Hosted Checks

- **Range screen.** A hosted check replays the screen over the pull request's base-to-head range, because a local hook
  can be skipped and a hosted check cannot.
- **Record check.** A hosted check passes only when a `pass` record, posted by the designated reviewer identity, names
  the pull request's current repository, base, and head. It runs when the pull request changes and when a review is
  submitted, so posting the record turns it green without a new commit.

Both are required status checks on the default branch, through the forge's branch protection or ruleset. A waiver of
other gates never covers either.

A repository that pushes straight to its default branch has no pull request to gate. Its hosted check replays the screen
over each pushed range after the fact: detective rather than preventive, so the push review stays mandatory.

## Adopter Decisions

Record each once, in the adopting repository's own conventions:

- the record's marker name, which never changes afterward;
- the reviewer identity whose records count;
- the names of the two hosted checks made required; and
- the integration path: pull request, or direct push to the default branch.

Recorded here:

- marker `ose-pr-leak-review`, set in `.github/workflows/leak-review.yml`;
- reviewer identity: the repository owner;
- required checks `quality` and `leak-review`, through the `main` ruleset; and
- integration path: pull request.
