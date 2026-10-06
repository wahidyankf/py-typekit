---
name: pr-leak-review
description: >-
  Indexes the three modules that define a leak, review a range privately before it is pushed, and make the leak review a
  mechanical precondition.
when_to_use: >-
  Use to decide whether a value is a leak, to run the leak review before a push, or to enforce the review in hooks,
  hosted checks, and branch protection.
---

# PR Leak Review Modules

Read in order. Together these hold the rules the [PR Leak Review](../pr-leak-review.md) entrypoint's sequence applies.

- **001 Leak Classes** holds the three classes, what is not a leak, and why history is the subject.
- **002 Push Review** holds the private review of each outgoing range, and remediation before and after.
- **003 Enforcement** holds the screen, the hosted checks, required status, and the adopter's decisions.

## Directory Map

- [001 Leak Classes](001-leak-classes.md)
- [002 Push Review](002-push-review.md)
- [003 Enforcement](003-enforcement.md)
