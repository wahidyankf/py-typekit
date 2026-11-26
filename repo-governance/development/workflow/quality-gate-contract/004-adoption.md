---
description: >-
  Lists the companions an adopting repository copies or relinks with a quality gate, how it maps the agents' skills, and
  the searches that find blocking-verdict wording and retired inputs an older gate left behind.
when_to_use: >-
  Use when adopting a quality gate or its propagation, or when checking that an adoption left no blocking verdict or
  retired input behind.
---

# Adoption

## Companions to Copy or Relink

A gate and its propagation link the catalog artifacts they apply. An adopting repository copies each linked artifact it
lacks, or relinks the link to its own owner, so no link dangles. The companions to copy or relink are:

- **every family:** this contract and its modules, [Sole-Writer Propagation](../sole-writer-propagation.md), the
  family's judge and repairer agents, by default `<family>-checker` and `<family>-fixer`, and every standard and skill
  the gate, its propagation, and those agents link;
- **`pr-review`:** [PR Review](../../../workflows/quality/pr-review.md), which every audit runs, the agents it
  dispatches, and every [Review Disciplines](../../agents/review-disciplines.md) module those agents link;
- **`ui-web` and `api-http`:** [Red, Green, Refactor](../../../workflows/quality/red-green-refactor.md), which every
  repair follows;
- **each `tutorial-*` family:** the `content` family's gate and propagation, which own the shared content rules.

A family is adopted whole: a repository copies `<family>-quality-gate` and `<family>-propagation` together, never one
alone, and where it declares its gates, it declares the family.

A gate hands its frozen ledger to its propagation, so either file alone is half a family. A declared structural check
for gates rejects an undeclared family's propagation and a declared family missing either file.

A copied agent reads what it links from the adopter's own tree. Most declare no `network`, so a link that resolves only
in the catalog is a rule the agent can never read.

## Agent Skills

An agent's `skills:` list names catalog skills. An adopting repository maps each entry to its own name for that skill,
or copies the skill, so no agent loads a skill the repository lacks. Where two catalog skills map onto one local skill,
the agent lists that local skill once.

## Searches Before Adoption Ends

A gate verdict is advisory, and no input but `max-cycles` bounds a run. Wording kept from an older gate can leave a
verdict blocking or a retired bound alive in a file the gate never names. Before the adoption ends, the adopter searches
`.agents/`, `repo-governance/`, `AGENTS.md`, and `docs/`, not only the workflows directory, case-insensitively:

- **A gate verdict still read as blocking:** `on a passing verdict`, `a passing terminal result`, `a PASS verdict from`,
  `must pass`, `until clean`, `zero findings`.
- **A retired verdict name or mode:** `PASS_EFFECTIVE`, `NEEDS_PROPAGATION`, `BLOCKED_`, `pass-no-change`, an `ocd`
  mode.
- **A retired input or bound:** `max-iterations`, `max-audits`, `min-iterations`, `escalation warning`, `3-5 iteration`.
- **A narrowed audit or a mid-run wait:** a re-check of `only changed files`, or a step that asks a person whether to
  continue.

```text
grep -rniE 'on a passing verdict|a passing terminal result|a PASS verdict from|must pass|until clean|zero findings' \
  .agents repo-governance AGENTS.md docs
grep -rnE 'PASS_EFFECTIVE|NEEDS_PROPAGATION|BLOCKED_|pass-no-change|\bocd\b' .agents repo-governance AGENTS.md docs
grep -rniE 'max-iterations|max-audits|min-iterations|escalation warning|3-5 iteration|only changed files' \
  .agents repo-governance AGENTS.md docs
grep -rniE 'whether to continue|wait(s|ing)? for (a|the) (person|user)' .agents repo-governance AGENTS.md docs
```

Each hit is rewritten to this contract or kept with a reason. Some hits stand: a deterministic tool that must pass; the
execution check's archival verdict, which [Verdicts, Ledger, and Relations](003-verdicts-ledger-and-relations.md) places
outside this contract; a checkpoint a workflow declares outside every gate cycle; a sentence that forbids the pattern,
as this contract's own do; and this module's lists.
