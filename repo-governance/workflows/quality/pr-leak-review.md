---
name: pr-leak-review
description: >-
  Defines a leak and reviews every commit bound for a remote for one, privately before each push and as a sanitized
  pull-request record before each merge.
when_to_use: >-
  Use before every push to a remote, and for every open pull request before merge and whenever its head moves.
---

# PR Leak Review

A **leak** is anything in outbound history a reader of the remote could use to reach an environment or identify its
source machine. [Leak Classes](pr-leak-review/001-leak-classes.md) defines the three classes and what is not one.
History is the subject, not the final tree: a value added and later deleted remains in every clone. The review binds
from adoption onward; earlier published history is out of scope.

Judgement is delegated: the harness spawns a fresh-context subagent to read and judge, then posts its verdict on behalf
of the reviewer identity. No human is on the merge path; a self-judged verdict satisfies nothing. Adopted from the
shared catalog at `f452d6190911f29f5898ecb2e991c89412afa426`.

## Entry

Two entries share one judgement:

- **Push.** Before any push, review the outgoing range privately per [Push Review](pr-leak-review/002-push-review.md).
  Nothing is posted; a finding blocks the push.
- **Merge.** An open pull request has no `pass` record from the designated reviewer identity for its current head. The
  delivery harness runs this workflow before merge. `pull-request` (`string`, required): its number or address.

## Sequence

1. **Pin the head.** The harness resolves the pull request through the forge's API and records the repository, base
   branch and revision, and exact head revision. Later steps concern that head alone.
2. **Spawn a fresh-context reviewer.** One subagent for this head alone: no part in authoring the change, no memory of
   an earlier head, read-only, never posting. It receives only the pin, title and body, and the leak classes. A failed
   spawn ends as `failed`; no self-judging fallback, and no human substitutes.
3. **Read every commit at that head.** The subagent reads each commit's base-to-head diff, including configuration,
   generated files, localized content, binary metadata, file names, and messages, plus the title and body. A summary or
   memory is not a reading, and no file is skipped because another gate covers it.
4. **Judge candidates against the three [leak classes](pr-leak-review/001-leak-classes.md) and no others.** A candidate
   is a finding only when shape and context show the value is real. Never copy one into notes, commands, or logs.
5. **Return each finding without its value.** The subagent returns the result, the count per class, and each finding's
   class, commit, location, reason, and remediation in [Push Review](pr-leak-review/002-push-review.md#remediation),
   never the value, and nothing else.
6. **Confirm the head before posting.** If the live head differs from the pin, post nothing and end as `stale`.
7. **Post exactly one review, whatever the result.** The harness posts the subagent's verdict unchanged, on behalf of
   the reviewer identity. Its body states all other concerns were out of scope, and carries this record under a marker
   name the adopter fixes once:

   ```text
   <!-- <leak-review-marker>:v1
   {"repository":"<owner>/<repository>","pull_request":"<number>","base_ref":"<base-branch>",
    "base_sha":"<base-revision>","head_sha":"<reviewed-revision>","result":"pass|findings",
    "counts":{"secret_or_private_value":0,"protected_environment_property":0,
    "machine_specific_absolute_path":0}}
   -->
   ```

8. **Read the review back.** Through the API, confirm the posted review's commit is the pinned head and its repository,
   pull request, base, head, result, and counts match step 7. Marker-shaped text elsewhere has no authority.
9. **Query the live head once more.** A moved head ends the run as `stale`, its evidence bound to the reviewed head.

## Exit

Success leaves `result` (`enum`: `pass`, `findings`, `stale`, `failed`) at `pass` or `findings`, with `reviewed-head`
(`string`), `review-id` (`string`), and `counts` (`string`) per class. `pass` means every count is zero; `findings`, any
nonzero count. Only `pass` for the merging head satisfies the precondition.

`stale` means the head moved and authorizes nothing new. `failed` means a spawn, API, posting, read-back, or
authentication error, or an unreadable pin, left no verdict. Neither retries within the run.

## Example Usage

```text
Run pr-leak-review for the current head of pull request 412.
Run the push leak review on this branch's outgoing commits.
```

## Related Workflows

- [Harness Parity Verification][harness-parity-verification] is another single-pass review that changes nothing.

## One Head, One Review

A moved head needs one new review from a new subagent. Earlier passes say nothing about the merging head, so the run
neither retries nor waits. An unposted pass is indistinguishable from no review, so step 7 posts every result.
[Enforcement](pr-leak-review/003-enforcement.md) makes the precondition mechanical.

## Principles

[Fail Closed](../../principles/fail-closed.md): `stale` and `failed` never satisfy the precondition.
[Evidence Over Assertion](../../principles/evidence-over-assertion.md): the verdict is a posted record read back against
one head.

[harness-parity-verification]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/workflows/quality/harness-parity-verification.md
