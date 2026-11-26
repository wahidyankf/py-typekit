---
description: >-
  Fixes what a contributing guide contains and how it is written, and requires a code of conduct built on an established
  standard with reporting and enforcement.
when_to_use: >-
  Use when writing or reviewing a contributing guide or a code of conduct.
---

# Contributing and Conduct

## Contributing Guide

`CONTRIBUTING.md` contains:

1. **A welcome** — thanks for the interest, in an inclusive tone.
2. **A table of contents**, once the file runs past about two hundred lines.
3. **Development setup** — prerequisites with versions, installation, running locally, and the setup problems
   contributors commonly hit, with their fixes.
4. **Conventions** — code style, commit message format, and branch naming, each linking to the document that owns it
   rather than restating it.
5. **The contribution process** — finding work, proposing a change, submitting a pull request, what review involves, and
   how long a response typically takes.
6. **Bug reports** — where to file one and the template if one exists, linking [Bug Reports](../bug-reports.md) for what
   a report contains rather than restating it.
7. **Feature requests** — how to propose one and how it is discussed.
8. **Testing** — how to run the tests, the coverage expected, and what new work must add.
9. **The code of conduct** — a link to it.
10. **Getting help** — where to ask questions and how to reach a maintainer.

### How It Is Written

- **Be explicit.** List the actual steps. A new contributor does not know the process, and "follow the usual workflow"
  describes nothing.
- **Anticipate setup failures.** The first hour of contributing is the one most likely to end in giving up, so every
  known setup problem and its fix belongs here.
- **One pull request per change.** State it, and say why: a pull request that does one thing is reviewed faster and
  reverted cleanly.
- **Set expectations.** State the typical review time, what a change needs before it merges, and what happens after. A
  contributor waiting in silence cannot tell a slow review from a rejection.

## Code of Conduct

`CODE_OF_CONDUCT.md` adopts an established standard — the [Contributor Covenant](https://www.contributor-covenant.org/)
is the most widely used — unless an organizational policy requires its own. A custom code covers at least what an
established one does:

- the behaviour expected of participants;
- examples of unacceptable behaviour, including harassment;
- how to report a violation, and to whom — `<conduct-contact>`;
- how reports are investigated and enforced; and
- the consequences of a violation.

An established standard is preferred because many communities have already read it critically, and because contributors
recognize it on sight. A bespoke code has to earn both, and a code whose reporting or enforcement is missing is a
statement of intent rather than a policy.
