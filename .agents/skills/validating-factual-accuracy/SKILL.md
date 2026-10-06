---
name: validating-factual-accuracy
description: >-
  Guides verifying commands, versions, code examples, and interfaces against the source that settles each question,
  choosing between the four verification labels, keeping each label beside its criticality, and deciding when to
  recheck.
when_to_use: >-
  Use when checking documentation or a specification for technical claims that could be wrong, or when a verified claim
  may have gone stale.
compatibility: Requires network access to official sources and read access to the content checked.
---

# Validating Factual Accuracy

[Factual Validation][factual-validation] owns what must be verified, the order of authoritative sources, the four
labels, and what a verification record holds.
[Docs Quality Gate](../../../repo-governance/workflows/quality/docs-quality-gate.md) owns the sequence of a
documentation check. This skill covers the verifier's judgement: which claims to extract, which source settles each,
which label fits, and when a verified claim needs checking again.

## Extract Only What Can Be Wrong

A factual claim is objective and checkable: a command and its flags, a version, a package's availability, an operation's
name and signature, a configuration format, a code example. Narrative flow, style, architectural opinions, and
predictions are outside this check. Marking a style preference as an error spends the label on something no source can
settle.

Group the claims by kind and start with the paths a reader follows first, such as installation and quick-start steps,
where a wrong command stops everyone.

## Ask the Source That Settles the Question

| The question                                 | Settled by                                              |
| -------------------------------------------- | ------------------------------------------------------- |
| does this command, flag, or operation exist? | the tool's official reference for the version targeted  |
| does this version exist, and is it current?  | the package registry                                    |
| did it change, break, or become deprecated?  | official release notes and migration guides             |
| does this example work?                      | running it, or failing that, the official API reference |

A community answer can show where to look. It never confirms a claim alone.

## Verify Each Kind

- **Command:** compare flags, argument order, and option names exactly; a near miss, such as a misspelled flag, is an
  error.
- **Version:** confirm the version exists, then compare it with the current release and look for deprecation. A version
  a major release behind, with breaking changes since, is outdated.
- **Code example:** check imports, signatures, and parameter order against the language and library version it targets,
  and run it where that is possible.
- **Interface:** confirm the name, parameters, and return shape, and whether a replacement has been announced.

A claim with no version context, such as "recently added", is itself a finding: state the version it applies to.

## Choose the Label Carefully

| What the source shows                                             | Label      |
| ----------------------------------------------------------------- | ---------- |
| it confirms the claim as written                                  | Verified   |
| the claim never held, or the command or code fails as written     | Error      |
| the claim held once, and a newer release changed or deprecated it | Outdated   |
| sources disagree, are ambiguous, or none could be reached         | Unverified |

Something deprecated that still works is outdated, not an error. Conflicting sources make a claim unverified, never
verified by majority.

The label records what was observed; the criticality records what it costs a reader. A report keeps both, as
[Assessing Criticality and Confidence](../assessing-criticality-confidence/SKILL.md) explains: an outdated version in an
aside and a wrong install command share a kind of label and differ in level.

## Leave Evidence Someone Else Can Recheck

Cite the exact page that settled each claim. A finding with no source cannot be re-validated by whoever applies it, and
a Verified label with no source is only an assertion. Where sources partly conflict or the targeted version is unclear,
say so in the finding, since whoever applies it rates its confidence from that evidence.

## Recheck When the Ground Moves

Record when each claim was verified and against which source. Verify it again when:

- a major release of the referenced software ships;
- release notes announce a breaking change or deprecation affecting it;
- a reader reports that it fails; or
- more time has passed than the refresh interval the repository records.

A minor or patch release needs a recheck only when the content targets that exact release.

## Related

- [authoring-documentation](../authoring-documentation/SKILL.md) — grounding claims about the repository itself.
- [generating-validation-reports](../generating-validation-reports/SKILL.md) — the report a check writes.

[factual-validation]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/writing/factual-validation.md
