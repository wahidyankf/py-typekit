---
description: >-
  Fixes Ansible's baseline: lint gates, validated role inputs, idempotent tasks, check-mode diffs before real runs, and
  Molecule or ansible-test verification.
when_to_use: >-
  Use when creating, configuring, or reviewing Ansible playbooks, roles, inventories, or collections, or planning how to
  verify a managed-host change.
---

# Ansible Standards

This standard is canonical for Ansible's open choices, and the Ansible infrastructure skill defers to it. It covers
infrastructure and hosts only; development environments follow
[Native-First Toolchain](../../workflow/native-first-toolchain.md), never Ansible.

It implements [Reproducibility](../../../principles/reproducibility.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Fail Closed](../../../principles/fail-closed.md), and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Gates

- **Lint:** ansible-lint at the recorded profile and the [Lint Strictness](../checks/lint-strictness.md) threshold, its
  syntax check covering every playbook.
- **YAML:** ansible-lint's `yaml` rule runs yamllint with the project's configuration, refusing one incompatible with
  its defaults ([yaml rule](https://github.com/ansible/ansible-lint/blob/main/src/ansiblelint/rules/yaml.md)).
  Standalone yamllint applies that configuration to other YAML.

## Adopter Decision

Profiles are cumulative, from `min` to `production`
([profiles](https://github.com/ansible/ansible-lint/blob/main/docs/profiles.md)).

| Profile      | Gains                                                          | Costs                              |
| ------------ | -------------------------------------------------------------- | ---------------------------------- |
| `production` | qualified names everywhere; strictest baseline                 | rewriting legacy short names first |
| `shared`     | change reporting and packaging rules for reused content        | qualified names left to review     |
| `safety`     | rejects risky permissions, unpinned package or source versions | change reporting left to review    |

Record the profile in the repository adapter [Stack Packs](../../../conventions/structure/stack-packs.md) defines. The
rules below hold under any profile.

## Type and Boundary Safety

Ansible maps [Type and Boundary Safety](../code/type-and-boundary-safety.md) this way:

- A role declares every input in `meta/argument_specs.yml` with type, requiredness, choices, and description, so a bad
  value fails before the role runs
  ([roles](https://github.com/ansible/ansible-documentation/blob/devel/docs/docsite/rst/playbook_guide/playbooks_reuse_roles.rst)).
- A play asserts unspecified input before first use.
- Modules use fully qualified collection names, since a short name can resolve to another collection's module.

These run with the play; never present them, or a passing lint, as static typing.

## Idempotence and Change Reporting

- Each task converges: a second run reports no change. Prefer a module over `command` or `shell`; a command task
  declares `changed_when`, `creates`, or `removes` to report change truthfully.
- Pin collections and roles to exact versions in a committed requirements file; upgrades follow
  [Dependency Bump Policy](../../workflow/dependency-bump-policy.md).
- A task handling a secret sets `no_log: true`. Secrets follow
  [No Secrets in Tracked Files](../../../conventions/security/no-secrets-in-tracked-files.md); inventories follow
  [No Machine-Specific Values](../../../conventions/security/no-machine-specific-values.md).

## Tests

[Test-Driven Development](../testing/test-driven-development.md) applies without exemption:

- A role's behaviour starts from a failing Molecule scenario whose verify step asserts the converged state; the default
  sequence converges twice, failing if the second run reports a change
  ([configuration](https://github.com/ansible/molecule/blob/main/docs/configuration.md)). Molecule, driving disposable
  instances, is the integration layer.
- A collection's Python modules and plugins run `ansible-test` sanity, unit, and integration suites
  ([testing](https://github.com/ansible/ansible-documentation/blob/devel/docs/docsite/rst/dev_guide/testing.rst)) and
  follow [Python Standards](python-standards.md).
- A change to real hosts first runs with `--check --diff`, whose diff must show exactly the changes written down
  beforehand. Check mode is evidence, not proof: modules without check support, and tasks conditioned on a registered
  result, report nothing
  ([check mode](https://github.com/ansible/ansible-documentation/blob/devel/docs/docsite/rst/playbook_guide/playbooks_checkmode.rst)).
  After a real run, the play asserts what it configured answers, for example through `uri` or `wait_for`.

Layers and gates follow [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Only unit runs over
collection Python code measure coverage, per [Meaningful Coverage](../testing/meaningful-coverage.md); playbooks, roles,
and inventories carry no numeric coverage or surrogate.

## Documentation

Each role's README states its purpose, supported platforms, and an example play with placeholder hosts. Role input
changes are contract changes under [Public Contract](../architecture/public-contract.md) and
[Specification Maintenance](../evidence/specification-maintenance.md).

## Enforcement

An adopter enforces ansible-lint and yamllint in its own pull-request gate, keeping Molecule, integration suites, and
real runs out of every hook: a real run is a deployment, never a gate's side effect. Review covers argument
specifications, change reporting, secret handling, and check-mode diffs.
