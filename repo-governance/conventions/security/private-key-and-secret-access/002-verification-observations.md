---
description: >-
  The followed and violated observations for each obligation of the private-key and secret access rule.
when_to_use: >-
  Use when reviewing whether an agent run followed or violated the rule.
---

# Verification Observations

- Conforming read: a metadata-only inventory lists key paths and modes without opening contents.
- Violating read: an agent-triggered command opens key bytes, even if it prints nothing.
- Conforming step: the step is one command starting in its named directory, placed on the clipboard.
- Violating step: prose instructions, several commands, or a command with no directory or clipboard.
- Conforming reply: the named word arrives before work continues.
- Violating reply: work continues without it, or free-form output counts as success.
- Conforming session: outputs, responses, reports, and artifacts hold no non-local secret, and no script echoes one
  toward the harness.
- Violating session: a non-local secret, full output, or screenshot is requested, transmitted, or recorded.
- Conforming lifecycle: unlock and lock bracket the phase's secret steps.
- Violating lifecycle: a pause, review, or PR handoff occurs while unlocked.
- Conforming incentive: the agent proceeds only after wrapper tests and gates pass.
- Violating incentive: secret-touching automation runs without that pipeline.
- Conforming review: history shows every commit at the pinned head read before posting.
- Violating review: a record posts without those reads or for a different head.
