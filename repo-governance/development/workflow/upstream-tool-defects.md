---
description: >-
  Handles a misbehaving pinned upstream tool: watch every use, check for an existing report, file an idea brief at the
  owner and continue, and fix through a bug-fix plan only a blocking defect with no workaround.
when_to_use: >-
  Use when a pinned command-line tool, library, or service the repository consumes behaves unexpectedly, or when
  recording which consumed tools this standard covers.
---

# Upstream Tool Defects

A maturing pinned tool fails in ways its tests have not met, often seen first by a consumer; a defect silently worked
around costs the next consumer the same again. This standard turns each sighting into a record at the owner, and a
blocking one into a fix there.

## Scope

It covers tools the repository consumes as pinned releases from an upstream it can contribute to; the adopter records
which tools and which repository owns each. A tool the repository cannot change is reported through its project's own
channel per [Bug Reports](../../conventions/writing/bug-reports.md); the plan steps below do not apply.

## Watch While Using

Every use is a check. A defect contradicts the tool's documentation, its own output, or its stated contract: a wrong
exit status, a misleading message, a crash, a silent no-op, a documented option that does nothing. A peculiarity — not
wrong, but surprising to a careful user — counts too, since the next user is surprised the same way; its fix may be
documentation.

## On a Sighting

1. **Reproduce** on the pinned version, then on the owner's latest trunk. A defect already fixed there needs a repin,
   not a plan.
2. **Check for duplicates** in the owning repository — open issues, open pull requests, in-flight plans, and idea briefs
   — per Bug Reports.
3. **When a match exists, wait for it.** Link it from the current work, add what it lacks, and continue on a workaround.
   Repin once it lands, releasing it first per step 5 if no release carries it. With no workaround, a match already in
   repair leaves the current work blocked on that link; a match that is only an idea brief becomes a bug-fix plan per
   step 5.
4. **When the defect has a workaround or does not block the work in hand, file it and continue.** Write an
   [idea brief](../../conventions/structure/plans/015-idea-brief-template.md) in the owner's `plans/ideas/`, with the
   report in its problem section and the duplicate check and references in its prior art. Land it through the owner's
   route, then resume on the workaround.
5. **Only when the defect blocks the work in hand and no workaround exists, fix it.** Write a
   [bug-fix plan](../../conventions/structure/plans/019-bug-fix-plan.md) in the owning repository, researching cause and
   solution and citing every source. First land the plan alone on the owner's trunk through its route, run the plan
   quality gate, record its verdict, give each open blocking row an owner, then execute it through the owner's delivery,
   regression test first. Once that test and the owner's full release gate pass on the exact revision, release through
   the owner's [Release Cut](../../workflows/maintenance/release-cut.md) without a further prompt, skipping no step, and
   repin every consumer.

A workaround is any route to the current work's outcome that does not edit the tool or its pin: another option or
command, a documented manual step, or a reliably succeeding retry. Record it beside the link or brief for the next
consumer.

A security defect skips every public step, going through the owner's private security channel.

## Relationship to Root Cause Orientation

This applies [Root Cause Orientation](../../principles/root-cause-orientation.md)'s "fix it at its cause" across a
repository boundary, and its "report it to its owner" to a defect that does not block. The cause, and so the fix, lives
in the owner; the consumer never carries a local patch or vendored copy. The work that found it continues on a
workaround rather than absorbing the fix, staying reviewable.

## Adopter Decision

Record the tools covered, each one's owning repository, and the route a plan lands by. Adopting this standard is the
standing request under which a defect's idea brief, a blocking defect's bug-fix plan, and a merged fix's release once
its tests pass need no further authorization.
